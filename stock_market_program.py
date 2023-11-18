import json
import yahoo_scraper
import itertools
import gainers_losers_active_news
import data_analysis

def main():
    running=True
    while running:
        print()
        print("How can I help you today?")
        print("-------------------------")
        print("1. Current Status of a Stock")           #done
        print("2. Basic Statistics")                    #done
        print("3. Valuation Measures and Trends")       #done
        print("4. Profitability")                       #done
        print("5. Management Effectiveness")            #done
        print("6. Income Statement Information")        #done
        print("7. Balance Sheet Information")           #done
        print("8. Cash Flow Statement")                 #done
        print("9. Historical Data Analysis")            #done
        print("10. Current Market Gainers")             #done
        print("11. Current Market Losers")              #done
        print("12. Most Active in Current Market")      #done
        print("13. Related News")                       #done
        print("14. Compare Stocks")

        print("X. Exit")

        choice=input("Your choice?  ")
        if choice=="X":
            print("Have a good day!")
            running=False

        elif choice=="1":
            running = True
            while running:
                response = input("What stock would you like to know more about? ")
                if response == 'X':
                    running = False
                    main()
                else:
                    name_stock = response
                    dictionary = yahoo_scraper.stock_info(name_stock)
                    print('--------------------------------------------------')
                    print(dict(itertools.islice(dictionary.items(),6)))

        elif choice=="2":
            while running:
                response = input("What stock would you like to know more about? ")
                if response == 'X':
                    running = False
                    main()
                else:
                    name_stock = response
                    dictionary = yahoo_scraper.stock_info(name_stock)
                    print('--------------------------------------------------')
                    print(dict(itertools.islice(dictionary.items(),6,9)))

        elif choice=="3":
            response1 = input("What stock would you like to know more about? ")
            print("1. Market Cap")
            print("2. Enterprise Value")                    
            print("3. Trailing P/E")       
            print("4. Forward P/E")                       
            print("5. PEG Ratio")            
            print("6. Price/Sales")        
            print("7. Enterprise Value/Revenue")           
            print("8. Enterprise Value/EBITDA")
            response2 = input("What measure would you like to see? ")
            name_stock = response1
            key = response2
            print('--------------------------------------------------')
            print(data_analysis.analysis1(name_stock, key))

            main()

        elif choice=="4":
            running = True
            while running:
                response = input("What stock would you like to know more about? ")
                if response == 'X':
                    running = False
                    main()
                else:
                    name_stock = response
                    list = yahoo_scraper.extended_stats1(name_stock,'Profitability')
                    dictionary = {
                        'Profit Margin' : list[0],
                        'Operating Margin' : list[1]
                    }
                    print('--------------------------------------------------')
                    for x in dictionary:
                        print(x+' : '+str(dictionary[x]))

        elif choice=="5":
            running = True
            while running:
                response = input("What stock would you like to know more about? ")
                if response == 'X':
                    running = False
                    main()
                else:
                    name_stock = response
                    list = yahoo_scraper.extended_stats1(name_stock,'Management Effectiveness')
                    dictionary = {
                        'Return on Assets' : list[0],
                        'Return on Equity' : list[1]
                    }
                    print('--------------------------------------------------')
                    for x in dictionary:
                        print(x+' : '+str(dictionary[x]))

        elif choice=="6":
            running = True
            while running:
                response = input("What stock would you like to know more about? ")
                if response == 'X':
                    running = False
                    main()
                else:
                    name_stock = response
                    list = yahoo_scraper.extended_stats1(name_stock,'Income Statement Information')
                    dictionary = {
                        'Revenue' : list[0],
                        'Revenue Per Share' : list[1],
                        'Quarterly Revenue Growth' : list[2],
                        'Gross Profit' : list[3],
                        'EBITDA' : list[4],
                    }
                    print('--------------------------------------------------')
                    for x in dictionary:
                        print(x+' : '+str(dictionary[x]))

        elif choice=="7":
            running = True
            while running:
                response = input("What stock would you like to know more about? ")
                if response == 'X':
                    running = False
                    main()
                else:
                    name_stock = response
                    list = yahoo_scraper.extended_stats1(name_stock,'Balance Sheet Information')
                    dictionary = {
                        'Total Cash' : list[0],
                        'Total Cash Per Share' : list[1],
                        'Total Debt' : list[2],
                        'Total Debt/Equity' : list[3],
                        'Current Ratio' : list[4],
                        'Book Value Per Share' : list[5]
                    }
                    print('--------------------------------------------------')
                    for x in dictionary:
                        print(x+' : '+str(dictionary[x]))

        elif choice=="8":
            running = True
            while running:
                response = input("What stock would you like to know more about? ")
                if response == 'X':
                    running = False
                    main()
                else:
                    name_stock = response
                    list = yahoo_scraper.extended_stats1(name_stock,'Cash Flow Statement')
                    dictionary = {
                        'Operating Cash Flow' : list[0],
                        'Levered Free Cash Flow' : list[1],
                    }
                    print('--------------------------------------------------')
                    for x in dictionary:
                        print(x+' : '+str(dictionary[x]))

        elif choice=="9":
            running = True
            while running:
                response = input("What stock would you like to know more about? ")
                if response == 'X':
                    running = False
                    main()
                else:
                    running = True
                    while running:
                        print('1.Line chart with Open, High, Low, Close, and Volume')
                        print('2.Line chart with Open price')
                        print('3.Line chart with Close price')
                        print('4.Line chart with High price')
                        print('5.Line chart with Low price')
                        print('6.Line chart with Volume')
                        print('7.Candlestick Chart')
                        print('8.Closing Price Moving Average Chart')
                        print('X.Back')
                        response2 = input("What type of graph would you like to see? ")
                        if response2 == 'X':
                            running = False
                            main()
                        elif response2=='1':
                            name_stock = response
                            print('--------------------------------------------------')
                            data_analysis.historical_analysis(name_stock,["Open","High", "Low", "Close", "Volume"], "1")
                            main()
                        elif response2=='2':
                            name_stock = response
                            print('--------------------------------------------------')
                            data_analysis.historical_analysis(name_stock,["Open"], "2")
                        elif response2=='3':
                            name_stock = response
                            print('--------------------------------------------------')
                            data_analysis.historical_analysis(name_stock,["Close"], "3")
                        elif response2=='4':
                            name_stock = response
                            print('--------------------------------------------------')
                            data_analysis.historical_analysis(name_stock,["High"], "4")
                        elif response2=='5':
                            name_stock = response
                            print('--------------------------------------------------')
                            data_analysis.historical_analysis(name_stock,["Low"], "5")
                        elif response2=='6':
                            name_stock = response
                            print('--------------------------------------------------')
                            data_analysis.historical_analysis(name_stock,["Volume"], "6")
                        elif response2=='7':
                            name_stock = response
                            print('--------------------------------------------------')
                            data_analysis.historical_analysis(name_stock,["Open","High", "Low", "Close", "Volume"], "7")
                        elif response2=='8':
                            name_stock = response
                            print('--------------------------------------------------')
                            data_analysis.historical_analysis(name_stock,["Close"], "8")
            main()

        elif choice=='10':
            dictionary = gainers_losers_active_news.gainers()
            print('--------------------------------------------------')
            for x in dictionary:
                print(x+' : '+str(dictionary[x]))

        elif choice=='11':
            dictionary = gainers_losers_active_news.losers()
            print('--------------------------------------------------')
            for x in dictionary:
                print(x+' : '+str(dictionary[x]))
                
        elif choice=='12':
            dictionary = gainers_losers_active_news.most_active()
            print('--------------------------------------------------')
            for x in dictionary:
                print(x+' : '+str(dictionary[x]))

        elif choice=='13':
            running = True
            while running:
                response = input("What stock would you like to know more about? ")
                if response == 'X':
                    running = False
                    main()
                else:
                    name_stock = response
                    list = gainers_losers_active_news.news(name_stock)
                    print('--------------------------------------------------')
                    for x in list:
                        print('* '+x)


if __name__ == '__main__':
    main()