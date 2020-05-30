import time
from datetime import datetime as dt

# change hosts path according to your OS
hosts_path = r"c:\Windows\System32\Drivers\etc\hosts"
# localhost's IP
redirect = "127.0.0.1"

# websites That you want to block
num = int(input("How many sites do you want to block? : "))

weblist=[]
for i in range(1,num+1):
    website = input("Enter the url of site to be blocked : ")
    weblist.append(website)

start = int(input("enter the start time in 24 hr format: "))
end = int(input("enter the end time in 24 hr format: "))
while True:

    # time of your work
    if dt(dt.now().year, dt.now().month, dt.now().day, start) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end):
        #print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for websites in weblist:
                if website in content:
                    pass
                else:
                # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in weblist):
                    file.write(line)

                # removing hostnmes from host file
            file.truncate()

    #print("Fun hours...")
    time.sleep(600)