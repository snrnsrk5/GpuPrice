import requests
from bs4 import BeautifulSoup
import Usd
import time


won = Usd.Won('https://finance.naver.com/marketindex/')

print("달러 :",won)

urlA = 'https://search.shopping.naver.com/search/all?catId=50003103&frm=NVSHPRC&maxPrice='
urlB = '&minPrice='
urlC = '&origQuery='
urlD = '&pagingIndex=1&pagingSize=40&productSet=total&query='
urlE = '&sort=price_asc&timestamp=&viewType=list'

def YsrpBest(gpu, msrp):
    time.sleep(0.5)

    if(gpu[-1] == 'S'):
        gpu = gpu + 'UPER'

    print("그래픽카드명 :", gpu, "\n가격 :", msrp)

    url = (urlA+str((int(msrp)*won*2))+urlB+str((int(msrp)*won))+urlC+gpu+urlD+gpu+urlE)

    print("URL :",url)

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    ser =  soup.select_one('span[class=price_num__2WUXn]')
    if ser == None:
        print("Error")
        return "  Error  "
    else:
        tag = ser.string
        print(tag)
        print("최소",str(int(msrp)*won))
        print("최대",str(int(msrp)*won*2))
        return tag
