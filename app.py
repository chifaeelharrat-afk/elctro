import streamlit as st

st.set_page_config(page_title="Generat VMTA", layout="wide")

st.title("🌐 Generat VMTA")

# Colonne 1 : Domaines
col1, col2 = st.columns(2)
with col1:
    st.subheader("1. Domaines")
    domains_input = st.text_area("Entrez les domaines (un par ligne)", value="enet.com.cn\ndmm.com\nnaukri.com\nblog.jp\nwebtretho.com\nliputan6.com")

# Colonne 2 : Sous-domaines
with col2:
    st.subheader("2. Sous-domaines")
    subdomains_input = st.text_area("Entrez les sous-domaines (un par ligne)", value="one\nstore")

st.markdown("---")
st.subheader("Server Boxes")

# Configuration des Server Boxes
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("**Server Box #1**")
    s1_ip = st.number_input("IP (Box 1)", value=1, key="ip1")
    s1_class = st.number_input("Class (Box 1)", value=1, key="class1")
    s1_servers = st.text_area("Serveurs (Box 1)", value="bss0001\nbss0002", key="srv1")

with c2:
    st.markdown("**Server Box #2**")
    s2_ip = st.number_input("IP (Box 2)", value=2, key="ip2")
    s2_class = st.number_input("Class (Box 2)", value=2, key="class2")
    s2_servers = st.text_area("Serveurs (Box 2)", value="bss0003\nbss0004", key="srv2")

with c3:
    st.markdown("**Server Box #3**")
    s3_ip = st.number_input("IP (Box 3)", value=2, key="ip3")
    s3_class = st.number_input("Class (Box 3)", value=2, key="class3")
    s3_servers = st.text_area("Serveurs (Box 3)", value="bss0005", key="srv3")

st.markdown("---")

# Bouton de génération
if st.button("🚀 Générer la sortie"):
    # Nettoyer et supprimer les doublons de l'entrée des domaines et sous-domaines
    domains = list(dict.fromkeys([d.strip() for d in domains_input.split("\n") if d.strip()]))
    subdomains = list(dict.fromkeys([s.strip() for s in subdomains_input.split("\n") if s.strip()]))
    
    # Récupérer tous les serveurs uniques
    all_servers = []
    for srv_text in [s1_servers, s2_servers, s3_servers]:
        for s in srv_text.split("\n"):
            if s.strip() and s.strip() not in all_servers:
                all_servers.append(s.strip())

    results = []
    
    if all_servers and subdomains and domains:
        num_servers = len(all_servers)
        
        # Diviser les domaines équitablement entre les serveurs sans répétition globale
        domains_per_server = [[] for _ in range(num_servers)]
        for idx, domain in enumerate(domains):
            domains_per_server[idx % num_servers].append(domain)
            
        first = True
        for srv_idx, srv in enumerate(all_servers):
            srv_domains = domains_per_server[srv_idx]
            
            if srv_domains:
                if not first:
                    results.append("")  # Ligne vide entre chaque serveur
                
                # Alterner les sous-domaines pour chaque domaine de ce serveur pour qu'ils ne se répètent pas
                for i, domain in enumerate(srv_domains):
                    sub = subdomains[i % len(subdomains)]
                    results.append(f"{srv}.{sub}.{domain}")
                
                first = False

    valid_lines_count = len([r for r in results if r])
    
    st.subheader(f"Final Output (Lignes : {valid_lines_count})")
    st.code("\n".join(results), language="text")
