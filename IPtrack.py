#! usr/bin/python

# Author : mzhasan
# Site   : www.mzainihasan.com

import sys
import random
import time
import requests
import urllib
import os
def writing(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#speed writing
        time.sleep(random.random() * 17.0/50)
writing('Author BY M Zaini Hasan')
writing('Website >>> www.mzainihasan.com')
writing('Contact >>> zaini.hasan13@gmail.com') 
os.system("clear")
author = raw_input("klik enter  bosku. . .")
ip = raw_input("masukkan ipnya bosku_>")
true	= True
url 	= "http://free.ipwhois.io/json/"+ip+"?lang=en"
json_open = urllib.urlopen(url)
data	= {"ip":"8.8.4.4"}
r	= requests.post(url = url, data = data)
file	= eval(r.text)
print "ip yang dilacak : %s"%(file['ip'])
print "kota : %s"%(file['city'])
print "negara : %s"%(file['country'])
print "ibukota : %s"%(file['country_capital'])
print "benua : %s"%(file['continent'])
print "ip type : %s"%(file['type'])
print "garis lintang : %s"%(file['latitude'])
print "garis bujur : %s"%(file['longitude'])
print "kode telpon : %s"%(file['country_phone'])
print "kode negara : %s"%(file['country_code'])