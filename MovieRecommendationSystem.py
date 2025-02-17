import requests
from bs4 import BeautifulSoup

MovieName=input("Enter the name of the Movie: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

link='https://www.imdb.com/chart/top/'
r=requests.get(link, headers=headers)
html=r.text
soup=BeautifulSoup(html,'html.parser')
ul=soup.find('ul',{'class':'ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM compact-list-view ipc-metadata-list--base'})
lis=ul.findAll('li',{'class':'ipc-metadata-list-summary-item'})
count=1
for lis in lis:
    xname=lis.find('h3',{'class':'ipc-title__text'}).string.strip().replace(f"{count}. ", "")
    count+=1
    if xname==MovieName or xname==MovieName.lower():
        url2id=lis.a['href']
        url2=f'https://www.imdb.com/{url2id}'
        r2=requests.get(url2,headers=headers)
        html2=r2.text
        soup2=BeautifulSoup(html2,'html.parser')
        div2=soup2.find('div',{'class':'ipc-metadata-list-item__content-container'})
        dirurl=(div2.a['href'])
        finaldirurl=f'https://www.imdb.com{dirurl}'
        r3=requests.get(finaldirurl,headers=headers)
        html3=r3.text
        soup3=BeautifulSoup(html3,'html.parser')
        div3=soup3.find('div',{'class':'ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid'})
        movies4=div3.findAll('a',{"class":"ipc-primary-image-list-card__title"})
        print(f"Your top 4 movies recommendation based on the entered movie {xname} are:")
        for movies4 in movies4:
            print(movies4.string)
    else:
        print("Movie not found")
        break

