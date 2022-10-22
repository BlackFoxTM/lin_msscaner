import socket
import asyncio
import pyfiglet
from colorama import Fore


async def ssh_scan():
    sshfiles = input(Fore.GREEN + "[-] Please Enter your file : ")
    ssh_ips = open(sshfiles,"r").readlines()
    for ip in ssh_ips:
        test = ip.strip()
        try:
            sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            sock.connect((test,22))
            open("success.txt","a").write(f"{ip}\n")
            print (Fore.GREEN + "Hit Now , Saved success.txt")
            sock.close()
        except socket.gaierror:
            print (f"{Fore.RED} Failed ! ")
            sock.close()
            pass
        except TimeoutError:
            print (f"{Fore.RED} {test} is not open port : 22 ")
            sock.close()
            continue

async def rdp_scan():

    rdpfiles = input(Fore.GREEN + "[-] Enter Your File txt RDP : ")
    rdp_ips = open(rdpfiles,"r").readlines()
    for ip in rdp_ips:
        test = ip.strip()
        try:
            sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            sock.connect((test,3389))
            open("success.txt","a").write(f"{ip}\n")
            print (Fore.GREEN + "Hit Now , Saved success.txt")
            sock.close()
        except socket.gaierror:
            print ("Failed ! ")
            sock.close()
            pass
        except TimeoutError:
            print (f"{Fore.RED} {test} is not open port : 3389 ")
            sock.close()
            continue


def banner():
    figlet = pyfiglet.Figlet(font="small").renderText("Fox SSH RDP Scanner ")
    return Fore.BLUE + figlet
print (banner())
print (Fore.MAGENTA + "\t RDP , SSH Scanner Version 1.0")
print (Fore.CYAN + "\tCoded By : Maximum Radikali")
mode = input(Fore.YELLOW + f"[1] SSH Scanner\n[2] RDP Scanner \n{Fore.MAGENTA}[$] Select an Option : ")
if mode == "1":
    asyncio.run(ssh_scan())
elif mode == "2":
    asyncio.run(rdp_scan())
else:
    print ("Enter valid Option ! ")

