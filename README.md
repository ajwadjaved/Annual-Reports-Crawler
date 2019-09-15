Scraps data off from www.annualreports.com, around 71,000 in total right now.
  
# Description
  
```extract_tables()``` downloads the page source and makes a dataframe with two columns. **Company** lists the name of the company and **Link** points to the href link where that specific Company's annual reports are stored. Later I use a for loop to go through all the href links/pdfs row by row
  
```scrap_pdfs()``` goes page by page and downloads all the pdfs in one page (even the hidden ones)
