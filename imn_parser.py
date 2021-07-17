import urllib.request as ul
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import pdb



class Parser:

    def get_webpage(self,url):
        req = ul.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        client = ul.urlopen(req)
        htmldata = client.read()
        client.close()
        return htmldata

    def get_datetime(self):
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y_%H-%M")
        return dt_string

    def get_headers(self, bs):
       
        header = bs.find_all("table")[0].find("tr")
        for items in header:
            try:
                list_header.append(items.get_text())
            except:
                continue



parser = Parser()
url = 'https://www.imn.ac.cr/especial/tablas/elcarmen.html'
htmldata = parser.get_webpage(url)
bs = BeautifulSoup(htmldata, features="html.parser")


list_header = parser.get_headers(bs)
data = []



# for getting the data 
HTML_data = bs.find_all("table")[0].find_all("tr")[1:]
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data = (sub_element.get_text().rstrip('\n').split('\n'))
        except:
            continue

    data.append(sub_data)


# Storing the data into Pandas
# DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header)
   
# Converting Pandas DataFrame
# into CSV file
dataFrame.to_csv('{}-Resultados.csv'.format(parser.get_datetime()))


