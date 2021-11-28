import os
input("Press enter to start adding pymenager as command line command...")
os.system("chmod +x pymen")
os.system("mkdir -p ~/bin")
os.system("cp pymen ~/bin")
os.system('export PATH=$PATH":$HOME/bin"')
print("Use 'pymen' command to run")