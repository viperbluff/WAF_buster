# WAF_buster
Disrupt WAF by abusing SSL/TLS Ciphers

# About WAF_buster
This tool was created to Analyze the ciphers that are supported by the Web application firewall being used at the web server end.(Reference:https://0x09al.github.io/waf/bypass/ssl/2018/07/02/web-application-firewall-bypass.html).It works by first triggering SslScan to look for all the supported ciphers during SSL/TLS negotiation with the web server.After getting the text file of all the supported ciphers, then we use Curl to query web server with each and every Cipher to check which of the ciphers are unsupported by WAF and supported by Web server , if any such Cipher is found then a message is displayed that "Firewall is bypassed".

## Screenshots 

![WAF_buster](https://raw.github.com/viperbluff/WAF_buster/master/screenshots/woof.png)


## Installation 

> **git clone https://github.com/viperbluff/WAF_buster.git**

## Python2

This tool has been created using Python2 and below modules have been used throughout:-

1.requests

2.os

3.sys

4.subprocess

## Usage 

> **Open terminal** 

> **python2 WAF_buster.py --input**

![Usage](https://raw.github.com/viperbluff/WAF_buster/master/screenshots/waf.png)

## Credits

Sahil Tikoo

Hacker



