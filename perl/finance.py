import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


class stock:
    def stock_price(self):
        start_date = '2020-01-01'
        end_date = '2021-01-01'
        ticker = 'GOOGL'
        data = yf.download(ticker, start_date, end_date)
        print(data.tail())
        data.to_csv("GOOGL.csv")

    def stock_graph(self):
        df = pd.read_csv('GOOGL.csv')
        ax = df.plot.hist(rot=0)
        plt.show()

    def graph_Stock(self):
        data = pd.read_csv('GOOGL.csv', delimiter=',')
        volume = data['Open']
        date = data['Date']
        plt.bar(date, volume, color='r', label="Stock")
        plt.xticks(rotation=25)
        plt.xlabel('DATE')
        plt.ylabel('STOCK')
        plt.title('google STOCK')
        plt.legend()
        plt.show()


obj = stock()
obj.stock_price()
obj.stock_graph()
obj.graph_Stock()
