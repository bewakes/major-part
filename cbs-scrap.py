from bs4 import BeautifulSoup as bs
import urllib
import requests

import os

url = "http://cbs.gov.np/sectoral_statistics/"
url = "http://cbs.gov.np/sectoral_statistics/population/VDC_municipality_detail/"

cnt = 0

def dig_inside(link, path):
    global cnt
    resp = requests.get(link)
    resp_html = resp.text

    path = path.replace(' ', '-')
    path = path.replace('(', '-')
    path = path.replace(')', '-')
    
    print('MAKING DIRECTORY : '+ path)
    os.system('mkdir -p '+path)

    soup = bs(resp_html, 'html.parser')

    content = soup.find_all(attrs={'class':'col-md-6'})

    uls = content[0].find_all('table')

    for ul in uls:
        links = ul.find_all('a')
        for link in links:
            i = link['href'].rfind('/')
            filename = link['href'][i+1:]
            href = 'http://'+urllib.parse.quote(link['href'][7:i+1])
            href = href+filename
            if '.pdf' in href:
                #print('total count ', cnt)
                #filename = link['href'][last_slash+1:]
                #print('THE FILE IS : ' + filename)
                file_exists = os.popen("ls "+path+" | grep '"+filename+"'").read()
                if len(file_exists.strip()) != 0:
                    cnt+=1
                    print('file exists')
                    continue
                #last_slash = link['href'].rfind('/')
                os.system('wget '+ href + ' -P '+"'"+path+"'")
            else:
                valid_path = link.text.replace('/', '-')
                dig_inside(href, path+'/'+valid_path)

dig_inside(url, './vdc-municipality')
