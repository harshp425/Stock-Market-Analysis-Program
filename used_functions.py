import yahoo_scraper

def make_list(price, change, changeperc):
    return [price, change, changeperc]

def make_num(num):
    if 'B' in num:
        i = num.index('.')
        t = len(num[i+1:])
        w=num.replace('.','')
        g=w.replace('B','')
        j= g
        for x in range(9-t+1):
            j=j+'0'
        return j
    elif 'T' in num:
        i = num.index('.')
        t = len(num[i+1:])
        w=num.replace('.','')
        g=w.replace('T','')
        j= g
        for x in range(12-t+1):
            j=j+'0'
        return j
    else:
        return num
    

def remove_NA(finalist):
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

dictionary_keys = {'1':'Market Cap', '2': 'Enterprise Value', '3':'Trailing P/E', '4':'Forward P/E', '5':'PEG Ratio', '6':'Price/Sales', '7':'Enterprise Value/Revenue', '8':'Enterprise Value/EBITDA'}