#!/usr/bin/python3
import os
import urllib.request
from pathlib import Path

def takeSurge(elem):
    #print(elem)
    if "Auto" in elem:
      #print("k")
      return "    "
    elem = elem.replace("香港", "0")
    elem = elem.replace("新加坡", "1")
    elem = elem.replace("日本", "2")
    elem = elem.replace("台湾", "3")
    elem = elem.replace("韩国", "4")
    elem = elem.replace("美国", "5")
    #print(elem)
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
      
def clash(mu, fname):
  base_url = os.environ['SUB_URL']
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
  myurl = base_url + mu;
  print(myurl)
  req = urllib.request.Request(url=myurl, headers=headers)
  txt = urllib.request.urlopen(req).read()
  a = txt.decode('utf-8')
  a.replace("\r\n", "\n")
  lines = a.split("\n")
  
  fname = "./dist/sdw_"+fname+".yaml"
  f = open(fname, "x")
  for i in lines:
    if "Auto" in i:
      before = i.split("[")[0]
      f.write(before)
      f.write("[")
      mid = i.split("[")[1].split("]")[0]
      after = i.split("]")[1]
      m = mid.split(",")
      m.sort(key=takeSurge)
      init = False
      for n in m:
        if init == False:
          f.write(n)
          init = True
        else:
          f.write(",")
          f.write(n)
      f.write("]")
      f.write(after)
      f.write("\r\n")
    else:
      f.write(i)
      f.write("\r\n")
          
def neohost():
   headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
   myurl = "https://cdn.jsdelivr.net/gh/neoFelhz/neohosts@gh-pages/basic/hosts"
   print(myurl)
   req = urllib.request.Request(url=myurl, headers=headers)
   txt = urllib.request.urlopen(req).read()
   a = txt.decode('utf-8')
   a.replace("\r\n", "\n")
   a.replace("\r", "")
   lines = a.split("\n")
   fname = "./dist/"+"ad_host"+".conf"
   f = open(fname, "x")
   for i in lines:
     if "0.0.0.0" in i:
       f.write(i.replace("0.0.0.0", "DOMAIN").strip())
       f.write("\r\n")
    
Path("./dist").mkdir(parents=True, exist_ok=True)
convert("6", "surge", takeSurge)
convert("5", "qx", takeQX)
clash("4", "clash")
neohost()