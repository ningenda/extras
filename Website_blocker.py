import time
from datetime import datetime as dt

host_temp="Hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("working Hours...")
        with open(host_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+""+ website+"\n")
    else:
        print("fun Hours")
    time.sleep(5)
