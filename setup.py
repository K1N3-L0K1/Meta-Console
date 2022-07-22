import os
import time

code = ''''''
import pyfiglet as pyg  
res= pyg.figlet_format("Welcome to Meta-Console!")     
print(res) 
print("Installing Pkgs")
time.sleep(5)
os.system("bash core/setup.sh && cd..")
os.system("pkg install nmap")
os.system("pkg install python")
os.system("pkg install figlet")
os.system("pip install pyfiglet") 
file = open("main.py", "w")
file.write('''import os
import math


def clear():
	os.system("clear")

def bann():
	res= pyg.figlet_format("Meta-Console")     
print(res)  

def ip():
	clear()
	print(pyg.figlet_format("Ip Addr"))
	print("")
	os.system("ifconfig")
	main()

def exit():
	print(pyg.figlet_format("Bye..!"))
	exit()

def brute():
	os.system("python core/brute/main.py")
	main()

def help2():
	print("Meta-Console Commands:")
	print("")
	print("ipaddr : To See The Ip Address")
	print("phish : To Make Phishing Pages")
	print("brute : To Do Brute Force Attack")
	print("spam : To Send Unlimted SmS")
	print("msfconsole : To Open Metasploit")
	print("msfinstall : To Install Metasploit")
	print("namp : To Use Nmap")
	print("iptrack : To Track Ip")
	print("ddos : To Do Ddos Attack")
	print("exit : To Exit From The Console")

def spam():
	os.system("python core/bomb/start.py")
	main()

def msfconsole():
	os.system("msfconsole")

def iptrack():
	os.system("bash core/iptrack/ip.sh")

def phish():
	os.system("chmod +x && bash core/phish/phish.sh")

def msfinstall():
	os.system("bash core/msf/file.sh")
	main()

def ddos():
	os.system("python core/ddos/ddos.py")
	main()

def nmap():
	clear()
	os.system("python core/nmap/nmap.py")

def main():
	clear()
	bann()
	print("")
	main=str(input("Enter Your Command Here: "))
	if main=="ipaddr":
		ip()
	if main=="exit":
	    exit()
	if main=="brute":
		brute()
	if main=="spam":
		spam()
	if main=="msfconsole":
		msfconsole()
	if main=="msfinstall":
		msfinstall()
	if main=="nmap":
		nmap()
	if main=="iptrack":
		iptrack()
	if main=="ddos":
		ddos()
	if main=="phish":
		phish()    
	if main=="help":
		help2()



main()''')
file.close
time.sleep(5)
res1= pyg.figlet_format("100% Completed")     
print(res1)
time.sleep(3)
os.system("rm -rf setup.py")
