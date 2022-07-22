import os
import math


def clear():
	os.system("clear")

def bann():
	print('''banner here''')

def ip():
	clear()
	os.system("ifconfig")
	main()

def exit():
	exit()

def brute():
	os.system("python core/brute/main.py")
	main()

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



main()