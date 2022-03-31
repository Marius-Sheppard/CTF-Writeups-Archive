#!/usr/bin/env python3

from bs4 import BeautifulSoup;
import requests;
import hashlib;

session = requests.session();
url = "http://142.93.45.58:31843/";
html = session.get(url);
soup = BeautifulSoup(html.content,"html.parser");
selector = 'h3';
result = soup.select(selector);
data = result[0].text.split(';')[-1].strip();

#print(data);
hashobject = hashlib.md5(data.encode())
md5hash = hashobject.hexdigest()

payload = {'hash':md5hash}
request = session.post(url,data=payload)
print(request.text)

# Flag Format: HTB{}