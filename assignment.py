#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 09:49:00 2019

@author: manzar
"""

url ="http://www.aiea.org.sg/membership-directory"
import requests
from bs4 import BeautifulSoup

req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
divs = soup.findAll("tr")

file = open('assignment.csv', 'w')
file.write("Company name, Telephone, contact person, email\n")


#12 - 98

for div in divs[12: 99]:
    name = div.contents[3].text
    telephone = div.contents[7].text
    contact_person = div.contents[9].text
    email = div.contents[13].text
    print(name.replace('\n', ''), telephone.replace('\n', ''), contact_person.replace('\n', ''), email.replace('\n', ''))
    file.write(name.replace('\n', '').replace(",", " | ") + ", " + telephone.replace('\n', '').replace(",", " | ") + ", " + contact_person.replace('\n', '').replace(",", " | ") + ", " + email.replace('\n', '').replace(",", " | ") + "\n")
file.close()

import pandas
file = pandas.read_csv('assignment.csv')