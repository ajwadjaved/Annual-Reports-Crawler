# Scrapes all pdfs off from www.annualreports.com 
# Haven't tested yet but should be somewhere around 70,963 pdfs since my empty search returned 5,479/5,674 stated companies

import requests
from urllib.parse import urljoin
import pandas as pd
from bs4 import BeautifulSoup as bs
import os, re
import pickle

def extract_table():
    r = requests.get('http://www.annualreports.com/Companies?search=')
    soup = bs(r.content, 'lxml')
    df = pd.DataFrame([(i.text, 'http://www.annualreports.com' + i['href']) for i in soup.select('tbody td:nth-of-type(1) a')], columns = ['Company','Link'])
    df.to_pickle('links.pkl') # saves into a dataframe the name of the company plus the href link it points to

def scrap_pdfs():
    df = pd.read_pickle('links.pkl')
    a = 0 # for naming the filenames numerically
    
    for x in range(df.Link.count()): 
                
        url = df['Link'][x] # reads the "Link" column from the dataframe

        folder_location = r'/home/duke/Annual_Reports/Data' # SPECIFY FULL DIRECTORY 

        response = requests.get(url)
        soup= bs(response.text, "html.parser")     

        for link in soup.select("a[href$='.pdf']"): #goes through all the .pdfs in all of the href links
           
            #filename = os.path.join(folder_location, ['href'].split('/')[-1]) # Names the pdf files using the last portion of each link
           
            filename = os.path.join(folder_location, str(a))
            a+=1 

            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(url,link['href'])).content)
