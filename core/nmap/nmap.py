import os
import time

def banner():
	print('''banner here''')

def clear():
	os.system("clear")

def nmapppp():
	nampm()

def nampm():
	nmap=str(input("Your Nmap Command Here: "))
	if nmap=="exit":
		os.system("cd .. && cd.. && python main.py")
	else:
		os.system(nmap)
		nmapppp()

nampm()