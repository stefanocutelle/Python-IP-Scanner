#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

from subprocess import Popen

devnull = open(os.devnull, 'wb')

ipscanner_ico = '''
#########################################################
#       LOCAL NETWORK IP SCANNER - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
'''

print ipscanner_ico

star = "**********************************************************************"

print star

ip_araligi_deger = raw_input("Enter the IP Range, enter the first part of the ip address excluding the hosts ( example: 192.168.0 ) ---> ")

print star

print "Thread range scanned ",ip_araligi_deger 

print star

if ip_araligi_deger == "":
 print star
 print "Try a valid rope pick ..."
 print star

import sys

p = []
aktif = 0
yanit_yok = 0
pasif = 0

for aralik in range(0,255):
    ip = ip_araligi_deger + ".%d" % aralik
    p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
while p:
    for i, (ip, proc) in enumerate(p[:]):
        if proc.poll() is not None:
            p.remove((ip, proc))
            if proc.returncode == 0:
                print('%s Aktif' % ip)
                aktif = aktif + 1
            elif proc.returncode == 2:
                print('%s Yanıt yok' % ip)
                aktif = yanit_yok + 1
            else:
                print('%s Pasif' % ip)
                pasif = pasif + 1
    time.sleep(.04)
devnull.close()

print star

print "LOCAL NETWORK IP SCANNER. By GH0ST-SOFTWARE."

print star

import os

print "Current operating system",os.name
print "Network Status"
print "Active Threads [ ",aktif," ]"
print "Passive IPs [ ",pasif," ]"
print "No answer  [ ",yanit_yok," ]"

print star

bitis_mesaj = "Scan completed ..."

print bitis_mesaj

print star
