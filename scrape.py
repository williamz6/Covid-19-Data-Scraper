import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import urllib.request
import csv



f= open('cases.csv', 'w', newline='') #covid-19 csv file
writer= csv.writer(f)
soup = BeautifulSoup(urllib.request.urlopen("https://en.m.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Nigeria_medical_cases").read(), 'lxml')

tbody=soup('table', {'class':'wikitable sortable'})[0].find_all('tr')
#Adding data to our csv file
for row in tbody:
    cols= row.findChildren(recursive=False)
    cols = [element.text.strip() for element in cols]
    writer.writerow(cols)
    print(cols)

# change "-" values in Active column  to nan
# df= pd.read_csv('dataCases.csv', encoding='cp1252', dtype='object')
# df = df.replace(['-'], np.NaN)


# replace NaN values on Active to zeros
# df['Active'] = df.Active.replace(np.nan, 0)

# save to csv file Writing to another CSV file
# df.to_csv('Updatedcases.csv')
