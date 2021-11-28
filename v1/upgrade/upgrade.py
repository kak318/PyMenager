import requests, os
from termcolor import colored

def info(n):
  print(colored(f"Info: {n}", 'blue'))
def warn(n):
  print(colored(f"Warn: {n}", 'yellow'))
def err(n):
  print(colored(f"Err: {n}", 'red'))

input(colored("Press ENTER key to upgrade PyMenager...", 'green'))
info("Starting request...")
try:
  r = requests.get("https://pymenagerserver.jaszkospam.repl.co/files/latest.zip")
except:
  err("Make sure you are connected to the internet!")
  exit(1)
file = open("latest.zip", "wb")
file.write(r.content)
file.close()
info("File was downloaded...")
try:
  os.system("unzip latest.zip")
except:
  err("Make sure you have downloaded UNZIP!")
  exit(1)
info("File was un ziped...")
cmd = """
  rm latest.zip
"""
os.system(cmd)
#try:
#  from PyMenager import setup
#except:
#  err("File 'setup.py' not found")
#  exit(1)
info("Your PyMenager was upgraded! (In PyMenager/)")
warn("PyMenager is still under development! In next version is planned to add setup.py!")
exit(0)