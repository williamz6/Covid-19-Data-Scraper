import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import urllib.request
import csv



f= open('cases.csv', 'w', newline='') #covid-19 csv file
writer= csv.writer(f)
soup = BeautifulSoup(urllib.request.urlopen("http://covid19.ncdc.gov.ng/").read(), 'lxml')

tbody=soup('table', {'id':'custom1'})[0].find_all('tr')
#Adding data to our csv file
for row in tbody:
    cols= row.findChildren(recursive=False)
    cols = [element.text.strip() for element in cols]
    writer.writerow(cols)
    print(cols)
