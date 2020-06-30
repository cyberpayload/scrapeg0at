#! python3

import requests
import re
from bs4 import BeautifulSoup
from xeger import Xeger
import rstr
import time
#This program is to scrape the current Linkedin occupation of someone.

pp = pprint.PrettyPrinter()
URL = 'https://www.google.com/search?rlz=1C1CHBF_enUS900US900&biw=1101&bih=1039&sxsrf=ALeKk02nIIgzxBoZRZLRcaPXCNQWWEqW_A%3A1593459510560&ei=NkP6XsXlIY-4sQXYrouIBA&q=site%3Alinkedin.com+intitle%3A%22William+Helsel%22&oq=site%3Alinkedin.com+intitle%3A%22William+Helsel%22&gs_lcp=CgZwc3ktYWIQA1C5EVj7MmCFPWgAcAB4AIABmQGIAdUTkgEEOS4xNZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwjF2Nyg46fqAhUPXKwKHVjXAkEQ4dUDCAw&uact=5'
googleResultsPage = requests.get(URL)
GRP = googleResultsPage.content
GRPstring = str(GRP)

time.sleep(2)
print('Enter first name')
firstName = input()
print("First name is set to " + "'" + firstName + "'")
time.sleep(.5)
print("Enter last name")
lastName = input()
print("Last name is set to " + "'" + lastName + "'")
time.sleep(.5)
print("Search the web for " + firstName + " " + lastName + "'s occupation?" )
time.sleep(.5)
input("<enter>")
print("Scraping the web.")
fullName = firstName + " " + lastName

for i in GRPstring:
    Name = re.search(r'(?<=['+fullName+']\s{1}\-{1}\s{1})(?:(?!\-)(?!\<)(?!\|).)*', GRPstring)
print(str(fullName) + "\'s occupation is a " + Name.group(0), end="")

