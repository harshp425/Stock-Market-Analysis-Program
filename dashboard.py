import requests
from bs4 import BeautifulSoup


def historical_data(symbol, key):
    
    header = {'User-Agent' : "your user agent"}
    url = f'https://finance.yahoo.com/quote/TSLA/history?p=TSLA'
    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_ = 'W(100%) M(0)')

    rows = soup.find_all('tr', class_ = "BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)")

    lis_dates = []
    for row in rows:
        date = row.find('td')
        if date!=None:
            lis_dates = lis_dates+[date.text]
    
    lis_open = []
    for row in rows:
        open = row.find('td', class_ = 'Py(10px) Pstart(10px)')
        if open!=None:
            lis_open = lis_open+[open.text]
    
    lis_high = []
    for x in rows:
        high = x.find_all('td', class_ = 'Py(10px) Pstart(10px)')
        if high!=[]:
            lis_high = lis_high+[high[1].text]

    lis_low = []
    for r in rows:
        low = r.find_all('td', class_ = 'Py(10px) Pstart(10px)')
        if low!=[]:
            lis_low = lis_low+[low[2].text]

    lis_close = []
    for c in rows:
        close = c.find_all('td', class_ = 'Py(10px) Pstart(10px)')
        if close!=[]:
            lis_close = lis_close+[close[3].text]

    lis_adjclose = []
    for a in rows:
        adjclose = a.find_all('td', class_ = 'Py(10px) Pstart(10px)')
        if adjclose!=[]:
            lis_adjclose = lis_adjclose+[adjclose[4].text]

    lis_volume = []
    for v in rows:
        volume = v.find_all('td', class_ = 'Py(10px) Pstart(10px)')
        if volume!=[]:
            lis_volume = lis_volume+[volume[5].text]
    lis_volume2 = []
    for x in lis_volume:
        z = x.replace(',','')
        lis_volume2 = lis_volume2 + [z]

    if key=='Date':
        lis_dates.reverse()
        return lis_dates
    elif key=='Open':
        lis_open.reverse()
        return lis_open
    elif key=='High':
        lis_high.reverse()
        return lis_high
    elif key=='Low':
        lis_low.reverse()
        return lis_low
    elif key=='Close':
        lis_close.reverse()
        return lis_close
    elif key=='Adjusted Close':
        lis_adjclose.reverse()
        return lis_adjclose
    elif key=='Volume':
        lis_volume2.reverse()
        return lis_volume2