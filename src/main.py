import execjs
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('./base64.js', 'r') as f:
  content = f.read()
Base64 = execjs.compile(content)

with open('./des.js', 'r') as f:
  content = f.read()
DES = execjs.compile(content)

with open('./md5.js', 'r') as f:
  content = f.read()
MD5 = execjs.compile(content)

def loop(n_times: int, MY_USERNAME: str, MY_PASSWD: str):
  for _ in range(n_times):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 \
        Safari/537.36 Edg/107.0.1418.42'
    })

    web = session.get('https://elearning.nkust.edu.tw/mooc/login.php', verify=False)
    soup = BeautifulSoup(web.text, "html5lib")

    node = soup.find(id="loginForm")

    pwdmask = "********************************"
    login_key = node.find('input', {'name':'login_key'}).get('value')
    md5key = MD5.call('MD5', MY_PASSWD)
    cypkey = md5key[:4] + login_key[:4]
    passwd = Base64.call('stringToBase64', MY_PASSWD)
    encrypt_pwd = Base64.call('stringToBase64', DES.call('des', cypkey, MY_PASSWD, 1))
    password = pwdmask[:len(MY_PASSWD)]

    res = session.post('https://elearning.nkust.edu.tw/login.php', data={
      'login_key': login_key,
      'encrypt_pwd': encrypt_pwd,
      'passwd': passwd,
      'username': MY_USERNAME,
      'password': password,
    })

    res = session.get('https://elearning.nkust.edu.tw/logout.php')
    session.close

    print("Times:", _)

loop(<n_times>, '<your-username>', '<your-password>')
