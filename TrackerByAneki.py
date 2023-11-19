import os
import requests
import subprocess
import dns.resolver
import socket 
import random
import string


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

BLUE = "\033[94m"

def IPLOOKUP():
    print(BLUE + "IP LOOK UP")
    ip_address = input("Veuillez entrer l'adresse IP cible : ")
    
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Informations pour l'adresse IP :", ip_address)
        print("Pays :", data.get("country", "N/A"))
        print("Région :", data.get("region", "N/A"))
        print("Ville :", data.get("city", "N/A"))
        print("Code Postal :", data.get("postal", "N/A"))
        print("Organisation :", data.get("org", "N/A"))
        print("Hôte :", data.get("hostname", "N/A"))
        print("Localisation :", data.get("loc", "N/A"))

    else:
        print("Impossible d'obtenir des informations pour cette adresse IP.")

    input("Appuyez sur Entrée pour continuer...")
    clear_screen()

def PINGIP():
    print(BLUE + "PING IP")
    ip_address = input("Veuillez entrer l'adresse IP cible : ")

    try:
        response = subprocess.check_output(["ping", "-c", "4", ip_address])
        print(response.decode())
    except subprocess.CalledProcessError:
        print("Impossible de réaliser le ping vers cette adresse IP.")

    input("Appuyez sur Entrée pour continuer...")
    clear_screen()

def GEOIP_DETAILED():
    print(BLUE + "GEO IP DÉTAILLÉE")
    ip_address = input("Veuillez entrer l'adresse IP cible : ")

    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

    else:
        print("Impossible d'obtenir des informations de géolocalisation pour cette adresse IP.")

    input("Appuyez sur Entrée pour continuer...")
    clear_screen()

def VPN_TOR_LOOKUP():
    print(BLUE + "VPN/TOR LOOKUP")
    ip_address = input("Veuillez entrer l'adresse IP cible : ")

    url = f"https://ipinfo.io/{ip_address}/vpn"
    response = requests.get(url)
    
    if response.status_code == 200:
        vpn_tor = response.text.strip()
        if vpn_tor == "true":
            print("L'adresse IP est associée à un service VPN ou à l'utilisation de TOR.")
        else:
            print("L'adresse IP n'est pas associée à un service VPN ou à l'utilisation de TOR.")
    else:
        print("Impossible de déterminer si l'adresse IP est associée à un service VPN ou à l'utilisation de TOR.")

    input("Appuyez sur Entrée pour continuer...")
    clear_screen()    

def OPEN_PORTS_LOOKUP():
    print(BLUE + "RECHERCHE DE PORTS OUVERTS")
    ip_address = input("Veuillez entrer l'adresse IP cible : ")

    try:
        response = subprocess.check_output(["nmap", "-p", "1-65535", "-T4", ip_address])
        print(response.decode())
    except subprocess.CalledProcessError:
        print("Impossible de réaliser la recherche de ports ouverts pour cette adresse IP.")

    input("Appuyez sur Entrée pour continuer...")
    clear_screen()

def DNS_LEAK_CHECK():
    print(BLUE + "LEAK DNS")
    domain_name = input("Veuillez entrer un domaine : ")

    try:
        resolver = dns.resolver.Resolver()
        answers = resolver.query(domain_name, 'A')
        for rdata in answers:
            print("Adresse IP associée au domaine :", rdata.address)
    except dns.resolver.NXDOMAIN:
        print("Le domaine n'existe pas.")
    except dns.resolver.NoAnswer:
        print("Pas de réponse DNS pour ce domaine.")
    except dns.exception.Timeout:
        print("Délai d'attente dépassé lors de la résolution DNS.")

    input("Appuyez sur Entrée pour continuer...")
    clear_screen()

def LOCAL_NETWORK_INFO():
    print(BLUE + "INFORMATIONS SUR LE RÉSEAU LOCAL")
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"Nom de l'hôte : {hostname}")
    print(f"Adresse IP locale : {local_ip}")

    try:
        gateway = socket.gethostbyname(socket.getfqdn())
        print(f"Passerelle par défaut : {gateway}")
    except socket.gaierror:
        print("Impossible de déterminer la passerelle par défaut.")

    input("Appuyez sur Entrée pour continuer...")
    clear_screen()
    
def generate_email_addresses(first_name, last_name):
    email_addresses = []

    email_addresses.append(f"{first_name}{last_name}@gmail.com")
    email_addresses.append(f"{first_name}_{last_name}@gmail.com")
    email_addresses.append(f"{first_name}.{last_name}@gmail.com")
    email_addresses.append(f"{last_name}{first_name}@gmail.com")
    email_addresses.append(f"{last_name}_{first_name}@gmail.com")
    email_addresses.append(f"{last_name}.{first_name}@gmail.com")

    email_addresses.append("/////Gmail/////")

    email_addresses.append(f"{first_name}{last_name}@outlook.com")
    email_addresses.append(f"{first_name}_{last_name}@outlook.com")
    email_addresses.append(f"{first_name}.{last_name}@outlook.com")
    email_addresses.append(f"{last_name}{first_name}@outlook.com")
    email_addresses.append(f"{last_name}_{first_name}@outlook.com")
    email_addresses.append(f"{last_name}.{first_name}@outlook.com")


    email_addresses.append("/////Outlook/////")

    email_addresses.append(f"{first_name}{last_name}@yahoo.com")
    email_addresses.append(f"{first_name}_{last_name}@yahoo.com")
    email_addresses.append(f"{first_name}.{last_name}@yahoo.com")
    email_addresses.append(f"{last_name}{first_name}@yahoo.com")
    email_addresses.append(f"{last_name}_{first_name}@yahoo.com")
    email_addresses.append(f"{last_name}.{first_name}@yahoo.com")

    return email_addresses
    
def main():
    while True:
        clear_screen()
        print(BLUE + r"""
   _    ___   _   _  _____  _   __ _____  _____ ______   ___   _____  _   
 / _ \ | \ | ||  ___|| | / /|_   _||_   _|| ___ \ / _ \ /  __ \| | / /    --------------------------------
/ /_\ \|  \| || |__  | |/ /   | |    | |  | |_/ // /_\ \| /  \/| |/ /     MokTracker - Local - IP ADDRESS
|  _  || . ` ||  __| |    \   | |    | |  |    / |  _  || |    |    \             @CODE BY ANEKI
| | | || |\  || |___ | |\  \ _| |_   | |  | |\ \ | | | || \__/\| |\  \    ---------------------------------
\_| |_/\_| \_/\____/ \_| \_/ \___/   \_/  \_| \_|\_| |_/ \____/\_| \_/
    

 
        """)

        choix = input("\n1- TrackIP\nChoisissez une option (ou tapez 'exit' pour quitter) : ")

        if choix == '1':
            IPLOOKUP()
        elif choix == '3':
            PINGIP()
        elif choix == '2':
            IPLOOKUP()
        elif choix == '4':
            VPN_TOR_LOOKUP()
        elif choix == '5':
            first_name = input("Veuillez entrer le prénom : ")
            last_name = input("Veuillez entrer le nom : ")
            email_addresses = generate_email_addresses(first_name, last_name)
            for email in email_addresses:
                print(email)
        elif choix.lower() == 'exit':
            print(BLUE)
            print("Succès de la sortie.")
            break
        else:
            print("Option invalide")

        input("Appuyez sur Entrée pour continuer...")

    clear_screen()

if __name__ == "__main__":
    main()
