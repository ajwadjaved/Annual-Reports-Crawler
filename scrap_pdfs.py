# Scrapes all pdfs off from www.annualreports.com 
# Haven't tested yet but should be around 70,963 pdfs since my empty search returned 5,479/5,674 stated companies

import requests
from urllib import request
from urllib.parse import urljoin
import pandas as pd
from bs4 import BeautifulSoup as bs
import os, re
import pickle

def extract_table():
    r = requests.get('http://www.annualreports.com/Companies?search=')
    soup = bs(r.content, 'lxml')
    df = pd.DataFrame([(i.text, 'http://www.annualreports.com' + i['href']) for i in soup.select('tbody td:nth-of-type(1) a')], columns = ['Company','Link'])
    df.to_pickle('links.pkl')

def scrap_pdfs():
    df = pd.read_pickle('links.pkl')
    
    for x in range(df.Link.count()): 
                
        url = df['Link'][x]

        #If there is no such folder, the script will create one automatically
        folder_location = r'/home/duke/Annual_Reports/Data' #SPECIFY FULL DIRECTORY

        response = requests.get(url)
        soup= bs(response.text, "html.parser")     
        for link in soup.select("a[href$='.pdf']"):
            #Name the pdf files using the last portion of each link which are unique in this case
            filename = os.path.join(folder_location,link['href'].split('/')[-1])
            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(url,link['href'])).content)




scrap_pdfs()


