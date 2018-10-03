import binance

x = binance.set("API_Key", "API_Secret")


#Type A coin must come first (small one first)
#print(binance.depth("ZRXBTC", limit=5))
#print(binance.prices())
#print(binance.depth('BTCETH', limit = 5))

class TypeACoin:

    def __init__(self, name):
        self.name = name
        self.bid_price = 0.0
        self.ask_price = 0.0
        self.bid_qty = 0.0
        self.ask_qty = 0.0

    def setAllValues(self, bid_price, ask_price, bid_qty, ask_qty):
        self.bid_price = bid_price
        self.ask_price = ask_price
        self.bid_qty = bid_qty
        self.ask_qty = ask_qty
       
    def get_name(self):
        return self.name

    def getTypeBMarkets(self):
        #Returns all markets where this 'Type A' coin can be purhcased
        #When the 'Type A' coin is the KEY rather than the VALUE program must act differently
        if self.name == 'BTC':
            return {'BCC BTC', 'BNB BTC', 'ETH BTC', 'LTC BTC', 'QTUM BTC', 'NEO BTC'}
        elif self.name == 'ETH':
            return {'BCC ETH', 'BNB ETH', 'ETH BTC', 'LTC ETH', 'QTUM ETH', 'NEO ETH'}
        elif self.name == 'BNB':
            return {'BCC BNB', 'BNB BTC', 'BNB ETH', 'LTC BNB', 'QTUM BNB', 'NEO BNB'}
        else:
            return {self.name+' BTC', self.name+' ETH', self.name+' BNB'}

    def oppAvailable(self):
        return ((self.bid_price-self.ask_price) / self.ask_price)*.9995*.9995*.9995 #accounting for the .05% transaction fees for each of the three transactions


BCC = TypeACoin('BCC')
BTC = TypeACoin('BTC')
BNB = TypeACoin('BNB')
QTUM = TypeACoin('QTUM')
LTC = TypeACoin('LTC')
ETH = TypeACoin('ETH')
NEO = TypeACoin('NEO')

type_a_coins = [BCC, BTC, BNB, QTUM, LTC, ETH, NEO]
while True:
    for coin in type_a_coins:
        coin_markets = coin.getTypeBMarkets()
        coin_name = coin.get_name()

        for market in coin_markets:
            temp = market.split()
            other = temp[0]
            base = temp[1]

            if coin_name == other:
                base_temp = binance.depth(base+'USDT', limit=100)[0]
                bid_temp = binance.depth(other+base, limit=5)[0][0]
                ask_temp = binance.depth(other+'USDT', limit=5)[0][0]

                bid_qty = float(bid_temp[1])
                ask_qty = float(ask_temp[1])
                

                #base_price = float(base_temp[0][0])

                qty_temp = min(bid_qty, ask_qty)
                x = qty_temp
                i = 0
                base_price = 0.0
                while x != 0.0:
                    qty = float(base_temp[i][1])
                    price = float(base_temp[i][0])
                    minimum = min(x, qty)
                    base_price += minimum*price
                    x = x - minimum
                    i+=1
                    if i == 100:
                        base_price = 0.0
                        break

                print(market,' ',base_price,' i = ',i)
                bid_price = float(bid_temp[0]) * base_price                
                ask_price = float(ask_temp[0])

                coin.setAllValues(bid_price, ask_price, bid_qty, ask_qty)
                prof_percent = coin.oppAvailable()
                if prof_percent > 0:
                    print('\n% profit would be ',prof_percent,'\nprofit would be ',prof_percent*min(bid_qty,ask_qty),' USD\n')
                    print('Market is ',market)
                else:
                    #print('Damn... off by ',prof_percent,'%')
                    poop = 'pee'
            else:
                #base_price = float(binance.depth(other+'USDT', limit=5)[0][0][0])
                #sbid_temp = binance.depth(base+other, limit=5)[0][0]
                poop = 'pee'


'''
                qty_temp = min(bid_qty, ask_qty)
                x = qty_temp
                i = 0
                base_price = 0
                while x != 0:
                    qty = float(base_temp[i][1])
                    price = float(base_temp[i][0])
                    minimum = min(x, qty)
                    base_price += minimum
                    x = x - minimum
                    i+=1
                    if i == 50:
                        base_price = 0
                        break

                print(base_price, ' i = ',i)
'''
