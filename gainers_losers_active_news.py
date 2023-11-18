import requests
from bs4 import BeautifulSoup
import used_functions

def gainers():
    url = 'https://www.google.com/finance/markets/gainers?hl=en'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    line = soup.find_all("div", class_ = 'SxcTic')
    list_gainers_names = []
    for x in line:
        w = x.find("div", class_ = "ZvmM7")
        list_gainers_names.append(w.get_text())


    price = soup.find_all("div", class_ = "Bu4oXd")
    list_gainers_price = []
    for y in price:
        q = y.find("div", class_ = "YMlKec")
        list_gainers_price.append(q.get_text())
    list_gainers_price = list_gainers_price[:50]
   
    dictionary_gainers = {}
    for index in range(len(list_gainers_names)):
        dictionary_gainers[list_gainers_names[index]]=list_gainers_price[index]

    change = soup.find_all("div", class_ = "BAftM")
    list_gainers_price_change = []
    for z in change:
        p = z.find("span", class_ = "P2Luy Ez2Ioe")
        if p!=None:
            list_gainers_price_change.append(p.text)
    list_gainers_price_change = list_gainers_price_change[1:]
    

    changeperce = soup.find_all("span", class_ = "NydbP nZQ6l")

    list_gainerperc_price_change = []
    for z in changeperce:
        p = z.get('aria-label')
        if 'Up by' in p:
            p = p.replace('Up by ',"+")
        elif 'Down by' in p:
            p = p.replace('Down by ','-')
        list_gainerperc_price_change.append(p)
    list_gainerperc_price_change = list_gainerperc_price_change[4:54]


    dictionary_gainers = {}
    for index in range(len(list_gainers_names)):
        g = used_functions.make_list(list_gainers_price[index],list_gainers_price_change[index],list_gainerperc_price_change[index]  )
        dictionary_gainers[list_gainers_names[index]]= g
    return dictionary_gainers

def losers():
    url = 'https://www.google.com/finance/markets/losers'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    line2 = soup.find_all("div", class_ = 'SxcTic')
    list_losers_names = []
    for x in line2:
        w = x.find("div", class_ = "ZvmM7")
        list_losers_names.append(w.get_text())
    

    price2 = soup.find_all("div", class_ = "Bu4oXd")
    list_losers_price = []
    for y in price2:
        q = y.find("div", class_ = "YMlKec")
        list_losers_price.append(q.get_text())
    list_losers_price = list_losers_price[:50]
    

    change2 = soup.find_all("div", class_ = "BAftM")
    
    list_losers_price_change = []
    for z in change2:
        p = z.find("span", class_ = "P2Luy Ebnabc")
        if p!=None:
            list_losers_price_change.append(p.text)
    list_losers_price_change = list_losers_price_change[1:]
    
    changeperce2 = soup.find_all("span", class_ = "NydbP VOXKNe")

    list_loserperc_price_change = []
    for z in changeperce2:
        p = z.get('aria-label')
        if 'Up by' in p:
            p = p.replace('Up by ',"+")
        elif 'Down by' in p:
            p = p.replace('Down by ','-')
        list_loserperc_price_change.append(p)
    list_loserperc_price_change = list_loserperc_price_change[1:51]

    dictionary_losers = {}
    for index in range(len(list_losers_names)):
        g = used_functions.make_list(list_losers_price[index],list_losers_price_change[index],list_loserperc_price_change[index] )
        dictionary_losers[list_losers_names[index]]= g
    return dictionary_losers

def most_active():
    url = 'https://www.google.com/finance/markets/most-active'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    line3 = soup.find_all("div", class_ = 'Q8lakc W9Vc1e')
    list_active_names = []
    for x in line3:
        w = x.find("div", class_ = "ZvmM7")
        list_active_names.append(w.get_text())


    price3 = soup.find_all("div", class_ = "Bu4oXd")
    list_active_price = []
    for y in price3:
        q = y.find("div", class_ = "YMlKec")
        list_active_price.append(q.get_text())
    list_active_price = list_active_price[:50]


    change3 = soup.find_all("div", class_ = "BAftM")
    
    list_active_price_change = []
    for z in change3:
        p = z.find("span", class_ = "P2Luy")
        if p!=None:
            list_active_price_change.append(p.text)
    list_active_price_change = list_active_price_change[5:]

    
    changeperc3 = soup.find_all("span", class_ = "NydbP")
    list_activeperc_price_change = []
    for z in changeperc3:
        p = z.get('aria-label')
        if 'Up by' in p:
            p = p.replace('Up by ',"+")
        elif 'Down by' in p:
            p = p.replace('Down by ','-')
        list_activeperc_price_change.append(p)
    list_activeperc_price_change = list_activeperc_price_change[16:66]
    

    dictionary_active = {}
    for index in range(len(list_active_names)):
        g = used_functions.make_list(list_active_price[index],list_active_price_change[index], list_activeperc_price_change[index] )
        dictionary_active[list_active_names[index]]= g
    return dictionary_active



def news(symbol):
    header = {'User-Agent' : "your user-agent"}
    url = f'https://www.google.com/finance/quote/{symbol}:NASDAQ'

    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.content, 'html.parser')

    header = soup.find_all('a', class_ = 'TxRU9d')
    news_titles = []
    for x in header:
        w = x.find('div', class_ = 'F2KAFc')
        title = w.text
        if '\n' in title:
            t = title.replace('\n','')
            news_titles.append(t)
        news_titles.append(title)
    return news_titles

