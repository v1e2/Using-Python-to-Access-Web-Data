# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:13:06 2022

@author: YYW
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

position = 3 
n = 4 
init = 'Fikret' 
print(f'http://py4e-data.dr-chuck.net/known_by_{init}.html')
for i in range(n):
    
    url = 'http://py4e-data.dr-chuck.net/known_by_'+init+'.html'
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    times = 0
    for tag in tags:
        if times < position-1:
            times +=1 
        else: 
            init = tag.contents[0]
            print(tag.get('href',None))
            break 
        #print(tag.get('href', None))
        
    