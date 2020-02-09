#!/usr/bin/python3
import os
import urllib.request
from pathlib import Path

def takeSurge(elem):
    elem = elem.replace("香港", "0")
    elem = elem.replace("新加坡", "1")
    elem = elem.replace("日本", "2")
    elem = elem.replace("台湾", "3")
    elem = elem.replace("韩国", "4")
    elem = elem.replace("美国", "5")
    return elem

def takeQX(elem):
    if elem == "":
      return "0"
    elem = elem.split("tag=")[1]
    return takeSurge(elem)
    

def convert(mu, fname, take):
    base_url = os.environ['SUB_URL']
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    myurl = base_url + mu;
    print(myurl)
    req = urllib.request.Request(url=myurl, headers=headers)
    txt = urllib.request.urlopen(req).read()
    a = txt.decode('utf-8')
    a.replace("\r\n", "\n")
    lines = a.split("\n")
    lines.sort(key=take)
    fname = "./dist/sdw_"+fname+".conf"
    f = open(fname, "x")
    for i in lines:
      f.write(i)
      f.write("\r\n")
    
Path("./dist").mkdir(parents=True, exist_ok=True)
convert("6", "surge", takeSurge)
convert("5", "qx", takeQX)