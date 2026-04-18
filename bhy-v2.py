import os
import sys
import time

# Professional Colors
R, G, Y, C, W = '\033[31m', '\033[32m', '\033[33m', '\033[36m', '\033[37m'

def banner():
    os.system('clear')
    print(f"{R} ██████╗ ██╗  ██╗██╗   ██╗    ██╗   ██╗██████╗ ")
    print(f"{R} ██╔══██╗██║  ██║╚██╗ ██╔╝    ██║   ██║╚════██╗")
    print(f"{R} ██████╔╝███████║ ╚████╔╝     ██║   ██║ █████╔╝")
    print(f"{R} ██╔══██╗██╔══██║  ╚██╔╝      ╚██╗ ██╔╝██╔════╝")
    print(f"{R} ██████╔╝██║  ██║   ██║        ╚████╔╝ ███████╗")
    print(f"{Y}================================================")
    print(f"{G} AUTHOR : {W}tranminhvang | {G}DEVICE : {W}Kali Linux ")
    print(f"{Y}================================================\n")

def menu():
    print(f"{C}[01] {W}Network Scan       {G}(Nmap)")
    print(f"{C}[02] {W}SQL Vulnerability  {G}(Sqlmap)")
    print(f"{C}[03] {W}Exploit Search     {G}(Searchsploit)")
    print(f"{C}[04] {W}Domain Lookup      {G}(Whois)")
    print(f"{C}[05] {W}Legacy Script      {G}(bhy.py)")
    print(f"{R}[00] {W}Exit System")
    print(f"{Y}------------------------------------------------")
    
    opt = input(f"{G}bhy_v2@terminal:~# {W}")

    if opt == '1' or opt == '01':
        target = input(f"{Y}Target IP/Domain: {W}")
        os.system(f"nmap {target}")
    elif opt == '2' or opt == '02':
        url = input(f"{Y}Target URL: {W}")
        os.system(f"sqlmap -u {url} --batch")
    elif opt == '3' or opt == '03':
        query = input(f"{Y}Exploit Query: {W}")
        os.system(f"searchsploit {query}")
    elif opt == '4' or opt == '04':
        domain = input(f"{Y}Target Domain: {W}")
        os.system(f"whois {domain}")
    elif opt == '5' or opt == '05':
        if os.path.exists("bhy.py"):
            os.system("python bhy.py")
        else:
            print(f"{R}[!] File bhy.py not found.")
    elif opt == '0' or opt == '00':
        sys.exit()
    else:
        print(f"{R}Invalid Option."); time.sleep(1); banner(); menu()

if __name__ == "__main__":
    banner()
    menu()
