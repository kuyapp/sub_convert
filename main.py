#!/usr/bin/python3
import os
import urllib.request
from pathlib import Path

def takeSurge(elem):
    if "Auto" in elem:
      return "0"

    elem = elem.replace("香港", "a")
    elem = elem.replace("新加坡", "b")
    elem = elem.replace("日本", "c")
    elem = elem.replace("台湾", "d")
    elem = elem.replace("韩国", "e")
    elem = elem.replace("美国", "f")
    elem = elem.replace("京港", "g")
    elem = elem.replace("沪港", "h")
    elem = elem.replace("沪台", "i")
    elem = elem.replace("通用", "j")
    return elem

def takeQX(elem):
    if elem == "":
      return "0"
    elem = elem.split("tag=")[1]
    return takeSurge(elem)

def convert_o(mu, fname, take):
    base_url = os.environ['O_SUB_URL']
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    myurl = base_url + mu;
    print(myurl)
    req = urllib.request.Request(url=myurl, headers=headers)
    txt = urllib.request.urlopen(req).read()
    a = txt.decode('utf-8')
    a.replace("\r\n", "\n")
    lines = a.split("\n")
    lines.sort(key=take, reverse=False)
    fname = "./dist/qq_"+fname+".conf"
    f = open(fname, "x")
    for i in lines:
      if "到期时间" not in i and "剩余流量" not in i:
        f.write(i)
        f.write("\r\n")    

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
    lines.sort(key=take, reverse=False)
    fname = "./dist/sdwsdw_"+fname+".conf"
    f = open(fname, "x")
    for i in lines:
      if "到期时间" not in i and "剩余流量" not in i:
        f.write(i)
        f.write("\r\n")
        

      
def convertEx(fname):
    base_url = os.environ['ME_URL']
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    myurl = base_url
    print(myurl)
    req = urllib.request.Request(url=myurl, headers=headers)
    txt = urllib.request.urlopen(req).read()
    a = txt.decode('utf-8')
    a.replace("\r\n", "\n")
    lines = a.split("\n")
    new_list = []
    end_list = []
    for i in lines:
      if i.startswith("【") and "回国" not in i:
        if "V4 |" in i:
          end_list.append(i)
        #else:
        #  new_list.append(i)
    fname = "./dist/sdwsdw_"+fname+".conf"
    f = open(fname, "x")
    for i in end_list:
      f.write(i)
      f.write("\r\n")
    new_list.reverse()
    for i in new_list:
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
      #print(i)
      mid = "\"" + i.split("[\"")[1].split("\"]")[0] + "\""
      #print(mid)
      after = i.split("\"]")[1]
      #print(after)
      m = mid.split(",")
      print(m)
      m.sort(key=takeSurge, reverse=False)
      print(m)
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
       f.write(i.replace("0.0.0.0 ", "DOMAIN,").strip())
       f.write("\r\n")

def fix():
    base_url = os.environ['SUB_URL']
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    myurl = base_url + "surge=4";
    print(myurl)
    req = urllib.request.Request(url=myurl, headers=headers)
    txt = urllib.request.urlopen(req).read()
    a = txt.decode('utf-8')
    a.replace("\r\n", "\n")
    lines = a.split("\n")
    fname = "./dist/sdwsdw_0929.conf"
    f = open(fname, "x")
    for i in lines:
      if "CGq46cJj6vet42v0" in i:
        f.write("#!MANAGED-CONFIG https://s.kuyapp.xyz/sdwsdw_0929.conf")
        f.write("\r\n")
        continue
      if "PROCESS-NAME" in i:
        continue
      if "URL-REGEX" in i:
        continue
      if i.startswith("#"):
        continue
      if len(i) = 0:
        continue
      f.write(i)
      f.write("\r\n")
       
Path("./dist").mkdir(parents=True, exist_ok=True)
fix()

#convert("6", "surge", takeSurge)
#
#convert("5", "qx", takeQX)
#clash("4", "clash")
#neohost()
#convertEx("me_surge")
#
#convert("6&tls", "surge_tls", takeSurge)
#convert("5&tls", "qx_tls", takeQX)
#clash("4&tls", "clash_tls")
# 
#convert_o("6", "surge", takeSurge)
