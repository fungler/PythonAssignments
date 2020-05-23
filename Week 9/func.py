import requests
import re
from bs4 import BeautifulSoup
import pymysql

def listToDict(lst):
    aye = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return aye

def displayInfo():
    with open('ips.log', 'r') as fo:
        log = fo.read()

    pattern = re.compile(r";((\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3}));")
    ips = pattern.findall(log)

    response = requests.get("https://www.whois.com/whois/"+ips[1][0])
    soup = BeautifulSoup(response.content, 'html.parser')

    info = soup.find(id='registryData')


    find = ("NetName", "NetRange", "OrgName", "Address", "City", "StateProv", "PostalCode", "Country", "RegDate")
    infoList = info.text.split("\n")
    #infoList

    res = []

    for line in infoList:
        for tag in find:
            if tag in line:
                x = line.strip().split(":")
                res.append(x[0].strip())
                res.append(x[1].strip())


    dictres = listToDict(res)

    return dictres
