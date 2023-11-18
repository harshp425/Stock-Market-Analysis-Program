import requests
from bs4 import BeautifulSoup

def stock_info(symbol):

    header = {'User-Agent' : "your user agent"}
    url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}'

    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.content, 'html.parser')

    label = soup.find('div', class_ = 'D(ib) Mend(20px)')

    summ_table = soup.find_all('tr', class_ = 'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)')
    lis = []
    for x in summ_table:
        p=x.find('td', class_ = 'Ta(end) Fw(600) Lh(14px)')
        lis.append(p.text)

    stock = {
    'Symbol' : symbol,
    'Price' : label.find('fin-streamer', class_ = 'Fw(b) Fz(36px) Mb(-4px) D(ib)').text,
    'Change' : label.find('fin-streamer', class_ = 'Fw(500) Pstart(8px) Fz(24px)').text,
    'Change_Percent' : label.find_all('fin-streamer', class_ = 'Fw(500) Pstart(8px) Fz(24px)')[1].text,
    'Days Range' : lis[4],
    'Volume' : lis[6],
    '52 Week Range' : lis[5],
    'PE Ratio' : lis[9],
    'EPS' : lis[10]
    }
    
    return stock


def extended_stats1(symbol,key):
    header = {'User-Agent' : "your user agent"}
    url = f'https://finance.yahoo.com/quote/{symbol}/key-statistics?p={symbol}'

    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.content, 'html.parser')
    label = soup.find_all('div', class_ = 'Mb(10px) Pend(20px) smartphone_Pend(0px)')
    for x in range(len(label)):
        w = label[x].find_all('td', class_ = 'Fw(500) Ta(end) Pstart(10px) Miw(60px)')
    lis_stat = w[2:]
    lis_stats = []
    for n in lis_stat:
        lis_stats.append(n.text)
    
    if key=='Profitability':
        return lis_stats[:2]
    elif key=='Management Effectiveness':
        return lis_stats[2:4]
    elif key=='Income Statement Information':
        return lis_stats[4:12]
    elif key=='Balance Sheet Information':
        return lis_stats[12:18]
    elif key=='Cash Flow Statement':
        return lis_stats[18:]

def valuation_measures(symbol, key):
    header = {'User-Agent' : "your user agent"}
    url = f'https://finance.yahoo.com/quote/{symbol}/key-statistics?p={symbol}'

    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.content, 'html.parser')

    if key=='1':
        label = soup.find('tr', class_ = 'Bxz(bb) H(36px) BdY Bdc($seperatorColor) fi-row Bgc($hoverBgColor):h')
        nums = label.find_all('td')
        market_cap = []
        for x in nums:
            market_cap.append(x.contents)
        market_cap = market_cap[1:]
        Market_cap = []
        for x in market_cap:
            Market_cap.append(x[0])
        return remove_NA(Market_cap)

    elif key=='2':
        label2 = soup.find('tr', class_ = 'Bxz(bb) H(36px) BdB Bdbc($seperatorColor) fi-row Bgc($hoverBgColor):h')
        nums2 = label2.find_all('td')
        enterprise_value = []
        for x in nums2:
            enterprise_value.append(x.contents)
        enterprise_value = enterprise_value[1:]
        Enterprise_value = []
        for x in enterprise_value:
            Enterprise_value.append(x[0])
        return remove_NA(Enterprise_value)

    elif key=='3':
        label3 = soup.find_all('tr', class_ = 'Bxz(bb) H(36px) BdB Bdbc($seperatorColor) fi-row Bgc($hoverBgColor):h')[1]
        nums3 = label3.find_all('td')
        trailing = []
        for x in nums3:
            trailing.append(x.contents)
        trailing = trailing[1:]
        Trailing = []
        for x in trailing:
            Trailing.append(x[0])
        return remove_NA(Trailing)
    
    elif key=='4':
        label4 = soup.find_all('tr', class_ = 'Bxz(bb) H(36px) BdB Bdbc($seperatorColor) fi-row Bgc($hoverBgColor):h')[2]
        nums4 = label4.find_all('td')
        forward = []
        for x in nums4:
            forward.append(x.contents)
        forward = forward[1:]
        Forward = []
        for x in forward:
            Forward.append(x[0])
        return remove_NA(Forward)

    elif key=='5':
        label5 = soup.find_all('tr', class_ = 'Bxz(bb) H(36px) BdB Bdbc($seperatorColor) fi-row Bgc($hoverBgColor):h')[3]
        nums5 = label5.find_all('td')
        pegratio = []
        for x in nums5:
            pegratio.append(x.contents)
        pegratio = pegratio[1:]
        PEGratio = []
        for x in pegratio:
            PEGratio.append(x[0])
        return remove_NA(PEGratio)

    elif key=='6':
        label6 = soup.find_all('tr', class_ = 'Bxz(bb) H(36px) BdB Bdbc($seperatorColor) fi-row Bgc($hoverBgColor):h')[4]
        nums6 = label6.find_all('td')
        pricesales = []
        for x in nums6:
            pricesales.append(x.contents)
        pricesales = pricesales[1:]
        Pricesales = []
        for x in pricesales:
            Pricesales.append(x[0])
        return remove_NA(Pricesales)
    
    elif key=='7':
        label7 = soup.find_all('tr', class_ = 'Bxz(bb) H(36px) BdB Bdbc($seperatorColor) fi-row Bgc($hoverBgColor):h')[5]
        nums7 = label7.find_all('td')
        entervalue_revenue = []
        for x in nums7:
            entervalue_revenue.append(x.contents)
        entervalue_revenue = entervalue_revenue[1:]
        Entervalue_revenue = []
        for x in entervalue_revenue:
            Entervalue_revenue.append(x[0])
        return remove_NA(Entervalue_revenue)

    elif key=='8':
        label8 = soup.find_all('tr', class_ = 'Bxz(bb) H(36px) BdB Bdbc($seperatorColor) fi-row Bgc($hoverBgColor):h')[6]
        nums8 = label8.find_all('td')
        entervalue_ebitda = []
        for x in nums8:
            entervalue_ebitda.append(x.contents)
        entervalue_ebitda = entervalue_ebitda[1:]
        Entervalue_ebitda = []
        for x in entervalue_ebitda:
            Entervalue_ebitda.append(x[0])
        return remove_NA(Entervalue_ebitda)


def historical_data(symbol, key):
    header = {'User-Agent' : "your user agent"}
    url = f'https://finance.yahoo.com/quote/{symbol}/history?period1=1531612800&period2=1689379200&interval=1wk&filter=history&frequency=1wk&includeAdjustedClose=true'
    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_ = 'W(100%) M(0)')

    rows = soup.find_all('tr', class_ = "BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)")

    
    lis_dates = []
    for row in rows:
        date = row.find('td', class_ = 'Py(10px) Ta(start) Pend(10px)')
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



def give_NA(finalist):
    lis2=[]
    for p in finalist:
        z = str(type(p))
        z=z.replace('<', '')
        z=z.replace('class', '')
        z=z.replace('>', '')
        lis2=lis2+[z]
    removevalue = 'L'
    for x in lis2:
        if 'bs4.element.Tag' in x:
            removevalue=lis2.index(x)
            lis2.remove(x)
    return removevalue


def remove_NA(list):
    v = give_NA(list)
    if type(v)==int:
        list.remove(list[v])
    return [list, v]



