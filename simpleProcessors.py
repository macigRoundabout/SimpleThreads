import subprocess 

t = subprocess.Popen("gedit")

while t.poll() is None:
    print("Still working...")


print("I am back")
