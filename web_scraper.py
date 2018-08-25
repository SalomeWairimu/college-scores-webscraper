import urllib2
from bs4 import BeautifulSoup
import csv


quote_page='https://blog.prepscholar.com/sat-scores-for-colleges'
page=urllib2.urlopen(quote_page)
soup=BeautifulSoup(page,'html.parser')
table_rows=soup.find_all('tr')
school_scores=[]
for row in table_rows[1:]:
    cols=row.find_all('td')
    if len(cols)>4:
        name=cols[0].text.encode('utf-8').split('\n')[1].split('\xc2\xa0')[0]
        #name=name.text.split('\n')[1]
        #if '\xa0' in name:
            #name=name.split('\xa0')[0]
        score=cols[4].text.encode('utf-8').split('\n')[1]
        school_scores+=[[name,score]]

with open('school_scores.csv','a') as sch_scores:
    writer=csv.writer(sch_scores)
    writer.writerow(['School','Avg score'])
    for name,scores in school_scores:
        writer.writerow([name,scores])