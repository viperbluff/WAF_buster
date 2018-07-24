#!/usr/bin/python 
import sys
import subprocess
import requests as re
import os

def banner():
	print "[*]Usage: python WAF_buster.py Payload_URL"
	print "[*]Run this script only if the Payload_URL is getting blocked by firewall "
def check_response():
        global g
        f=re.get(sys.argv[1])
        g=f.status_code
def ssl_check(domain,payload):
        x="domain/payload"
        os.system('touch file.txt')
	os.system('echo `subprocess.check_output("sslscan domain",shell=True)` > file.txt')
	file_open=open("file.txt",'r')
	for line in file_open.readlines():
                if "Accepted" in line:
                        os.system('touch cipher.txt')
                        file_write=open("cipher.txt",'w')
                        file_write.write(line)
                else:
                        continue
        open("final_cipher.txt",'w') as fi
        for line in cipher.txt:
                line=line.strip(' ')
                if len(line)==5:
                        del line[0]
                        del line[1]
                        del line[2]
                        del line[3]
                        del line[5]
                fi.write(line[4]+"\n")
                else:
                        quit()
        fi.close()
	file_write.close()
	file_open.close()
                try:
                        cipher_open=open("final_cipher.txt",'r')
                        for i in cipher_open.readlines():
                                output=subprocess.check_output("curl -cipher i $x",shell=True)
                                if g in output:
                                        print "Firewall blocked Cipher %s" %i
                                elif payload in output:
                                        print "Firewall Bypassed using Cipher :%s and attack executed" %i
                                else:
                                        print "firewall Bypassed using Cipher %s but attack blocked" %i
                        cipher_open.close()
                except:
                        print "Something went wrong"
	
def main():
	if sys.argv[1]==0:
		banner()
	else:
		d=sys.argv[1]
		split=d.split("/")
		ssl_check(split[0],split[1])


