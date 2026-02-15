import requests

def testar_link(url):
    try:
        # Verifica apenas o cabeçalho para ser rápido
        r = requests.head(url, timeout=10, allow_redirects=True)
        return r.status_code == 200
    except:
        return False

def processar():
    url_fonte = "https://iptv-org.github.io/iptv/countries/br.m3u"
    print("Coletando dados do iptv-org...")
    
    response = requests.get(url_fonte)
    linhas = response.text.split('\n')
    
    # Lista final organizada e testada
    canais_validos = []
    
    # Lógica de extração
    for i in range(len(linhas)):
        if linhas[i].startswith("#EXTINF"):
            info = linhas[i]
            url = linhas[i+1] if (i+1) < len(linhas) else ""
            
            if url.startswith("http"):
                print(f"Testando: {url[:40]}...")
                if testar_link(url):
                    canais_validos.append(info)
                    canais_validos.append(url)

    # Escrita final
    with open("lists/brazil.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n" + "\n".join(canais_validos))
    print("Sucesso! Lista atualizada.")

if __name__ == "__main__":
    processar()
