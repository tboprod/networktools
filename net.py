import socket
import platform
import subprocess
import speedtest
import requests

def ping_host(host):
    """
    Esegue un ping a un host e restituisce il tempo di risposta
    """
    try:
        # Determina il comando ping in base al sistema operativo
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        
        # Esegue il ping
        output = subprocess.check_output(
            ['ping', param, '4', host], 
            universal_newlines=True
        )
        
        return f"Ping a {host} riuscito:\n{output}"
    except subprocess.CalledProcessError:
        return f"Impossibile raggiungere {host}"

def check_website_status(url):
    """
    Verifica lo stato di un sito web
    """
    try:
        response = requests.get(url, timeout=5)
        return f"{url} è online (Codice: {response.status_code})"
    except requests.ConnectionError:
        return f"{url} non raggiungibile"

def get_network_info():
    """
    Ottiene informazioni di base sulla configurazione di rete
    """
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    return {
        "Hostname": hostname,
        "Indirizzo IP Locale": ip_address
    }

def test_internet_speed():
    """
    Testa la velocità della connessione internet
    """
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000  # Converti in Mbps
        upload_speed = st.upload() / 1_000_000  # Converti in Mbps
        
        return {
            "Download Speed": f"{download_speed:.2f} Mbps",
            "Upload Speed": f"{upload_speed:.2f} Mbps"
        }
    except Exception as e:
        return f"Errore nel test di velocità: {e}"

def main():
    print("Informazioni di Rete:")
    print(get_network_info())
    
    print("\nTest Ping:")
    print(ping_host("google.com"))
    
    print("\nStato Siti Web:")
    websites = ["https://www.google.com", "https://www.github.com"]
    for site in websites:
        print(check_website_status(site))
    
    print("\nTest Velocità Internet:")
    print(test_internet_speed())

if __name__ == "__main__":
    main()
