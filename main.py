#!/usr/bin/env python

import json
import sys
import os
from termcolor import colored
try:
  print(colored("Warn: PyMenager still under development", 'yellow'))

  if sys.argv[1] == "-i":
      print("Info: Welcome to PyMenager install maker!")
      installs = input(
          "Enter installs do you want to use in your projest (space = next pack)\n> "
      )
      print("Installs saved")
      git = input(
          "If you need to clone git repo when installing paste link here (if no leave   blank)\n> "
      )
      if git == "":
          print("Info: No repo")
      else:
          print(git)
      projname = input("Enter your project name\n> ")
      print("Info: Name saved")
      print("Info: Writing config file...")
      conf = {"name": projname, "installs": installs, "repo": git}
      convert = json.dumps(conf)
      file = open("pymenager.pmx", "w")
      file.write(convert)
      file.close()
      print("Info: Creating installer...")
      filei = open("installer.py", "w+")
      fin = ("""print("Info: Welcome to PyMenager install")\n
  input("Info: Press enter to start installing...")\n
  import os\n
  os.system("clear")\n
  import json\n
  conf = open("pymenager.pmx", "r")\n
  cnv = conf.read()\n
  data = json.loads(cnv)\n
  g = data["repo"]\n
  if g == "":\n
    print("No repo to clone")\n
  else:\n
    cmd = "git clone "+g\n
    os.system(cmd)\n
  i = data["installs"]\n
  cmd = "pip install "+i\n
  os.system(cmd)\n
  conf.close()\n
  print("Info: PyMenager installer delete")\n
  os.system("rm pymenager.pmx")\n
  os.system("rm installer.py")\n
  print("Info: PyMenager files was deleted")\n
  print("Info: PyMenager installer exit")\n
  exit()""")
      filei.write(fin)
      filei.close()
      print("Info: Your installer and data file are ready!")
      exit()
  elif sys.argv[1] == "-p":
      print("---PyMenager project mode---")
      projname = input("Your project name\n> ")
      debug = ' ' in projname
      if debug == True:
        print(colored("Error: The project name cannot contain spaces!", 'red'))
        print(colored("Error: Can't create project!", 'red'))
        exit(1)
      cmd = "mkdir " + projname
      os.system(cmd)
      cmd = """cd """ + projname + """ 
              touch app.py
              touch package.json
              mkdir assets
              """
      os.system(cmd)
      filename = projname+"/assets/readme.txt"
      read = open(filename, "w")
      read.write("In this folder add your assets.")
      read.close()
      filename = projname + "/package.json"
      package = open(filename, "w")
      pack = {
          "name": projname,
          "run": "python3 app.py",
          "create": "PyMenager",
          "lang": "python3",
      }
      print("Warn: Do not edit 'lang' in package.json")
      final = json.dumps(pack, indent=3, sort_keys=True)
      package.write(final)
      print("Info: File package.json is ready!")
      package.close()
      filename = projname+"/runner.py"
      runner = open(filename, "w")
      runner.write("""import json, os
  try:
    filer = open("package.json", "r")
    process = filer.read()
    data = json.loads(process)
    ##############################
    run = data["run"]
    name = data["name"]
    create = data["create"]
    lang = data["lang"]
    if create == "PyMenager":
      print("Info: Processing package file...")
      if lang == "python3":
        print("Info: Attempting to run "+name+"...")
        os.system(run)
      else:
        print("Error: PyMenager supports only python3!")
        exit(1)
    else:
      print("Error: package.json is not from PyMenager!")
      exit(1)
  except:
    print("Error: package.json not found!")
    exit(1)""")
      print("Info: File runner.py is ready!")
      filename = projname+"/app.py"
      app = open(filename, "w")
      app.write("""def main():
    print("Hello World!")

  if __name__ == "__main__":
    main()""")
      print("Info: File app.py is ready!")
      print("Info: Your app is ready to run!")
      exit()
  elif sys.argv[1] == "-h":
      print("-i create installer package\n-p create new project\n-f fix package.json  file\n-pi [package] installs pip package\n-v version\n-r run from package.json\n-h   help")
  elif sys.argv[1] == "-r":
    try:
      filer = open("package.json", "r")
      process = filer.read()
      data = json.loads(process)
      ##############################
      run = data["run"]
      name = data["name"]
      create = data["create"]
      lang = data["lang"]
      if create == "PyMenager":
        print("Info: Processing package file...")
        if lang == "python3":
          print("Info: Attempting to run "+name+"...")
          os.system(run)
        else:
          print(colored("Error: PyMenager supports only python3!", 'red'))
          exit(1)
      else:
        print(colored("Error: package.json is not from PyMenager!", 'red'))
        exit(1)
    except:
      print(colored("Error: package.json not found!", 'red'))
      exit(1)
  elif sys.argv[1] == "-f":
    print("Info: PyMenager file fix mode")
    dire = input("Were is your package.json file to fix?\n> ")
    fix = open(dire, "w")
    print("Info: Package.json rewrite...")
    projname = input("Enter your project name\n> ")
    print("Info: Attempting to rewrite file...")
    pack = {
          "name": projname,
          "run": "python3 app.py",
          "create": "PyMenager",
          "lang": "python3",
          "packages": None
    }
    final = json.dumps(pack, indent=3, sort_keys=True)
    fix.write(final)
    print("Info: File was rewrited!")
    fix.close()
    exit()
  elif sys.argv[1] == "-pi":
    print("Info: Loading...")
    cmd = "pip install "+sys.argv[2]
    os.system(cmd)
    print("Info: Done!")
    exit()
  elif sys.argv[1] == "-v":
    print("Info: PyMenager Version = 1.4")
    exit()
  elif sys.argv[1] == "install":
    try:
      file = open("package.json", "r")
      print("Info: Loading package...")
      package = json.loads(file.read())
      packages = package["packages"]
      cmd = "pip install "+packages
      os.system(cmd)
      print(colored("Info: package operation succes", 'green'))
    except:
      print(colored("Error: Something went wrong!", 'red'))
  elif sys.argv[1] == "-up":
    inp = input("Do you want to upgrade your PIP? [y/n]\n> ")
    if inp == "y":
      cmd = "python3 -m pip install --upgrade pip"
      os.system(cmd)
    else:
      print("Info: Cancel")
  else:
    print(colored("Error: For help use -h", 'red'))
except:
  print(colored("Info: Use '-h' for help", 'blue'))