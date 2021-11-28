import argparse, os, json
from termcolor import colored

def info(t):
  print(colored("Info: ", "blue") + t)
def err(t):
  print(colored("Err: ", "red") + t)
def warn(t):
  print(colored("Info: ", "yellow") + t)
def succes(t):
  print(colored("Succes: ", "green") + t)

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", help="current PyMenager version", action="store_true")
parser.add_argument("-p", "--project", help="create new python project", action="store_true")
parser.add_argument("-r", "--run", help="run project", action="store_true")
parser.add_argument("-i", "--install", help="install packages from package.json file", action="store_true")
args = parser.parse_args()

if args.version:
  info("2.0")
elif args.project:
  info("PyMenager new project")
  name = input("> ")

  fltr = " " in name
  if fltr:
    err("You cant add spaces to your project name!")
    exit(1)
  else:
    info("Name saved...")

  cmd = f"""
    mkdir {name}
    cd {name}
    touch main.py
    touch package.json
    mkdir assets
  """

  try:
    os.system(cmd)
    info("Files created...")
  except:
    err("Something went wrong!")
    exit(1)
  
  pack = {
    "name": name,
    "version": "1.0",
    "GB": "PM",
    "lang": "python3",
    "run": "python3 main.py"
  }

  final = json.dumps(pack, indent=2)
  filename = f"{name}/package.json"
  file = open(filename, "w")
  file.write(final)
  file.close()

  info("package.json file created...")

  succes("Done!")
#elif args.run:
#  info("Looking for package.json...")
#  try:
#    file = open("package.json", "r")
#  except:
#    err("package.json not found!")