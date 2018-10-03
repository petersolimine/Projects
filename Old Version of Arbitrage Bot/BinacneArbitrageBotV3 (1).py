import binance

x = binance.set("API_Key", "API_secret")


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

    def oppAvailable(self):
        return ((self.bid_price-self.ask_price) / self.ask_price)*.9995*.9995*.9995*.9995 #accounting for the .05% transaction fees for each of the four transactions

    def getTypeBMarkets(self):
        #Returns all markets where this 'Type A' coin can be purhcased
        #When the 'Type A' coin is the KEY rather than the VALUE program must act differently
        if self.name == 'ETH':
            return {'ETH BTC'}
        elif self.name == 'BNB':
            return {'BNB BTC', 'BNB ETH'}
        elif self.name == 'XRP':
            return {'XRP BTC', 'XRP ETH'}
        else:
            return {self.name+' BTC', self.name+' ETH', self.name+' BNB'}


BCC = TypeACoin('BCC')
XRP = TypeACoin('XRP')
QTUM = TypeACoin('QTUM')
LTC = TypeACoin('LTC')
ADA = TypeACoin('ADA')
NEO = TypeACoin('NEO')
ETH = TypeACoin('ETH')
BNB = TypeACoin('BNB')

type_a_coins = [BCC, XRP, ADA, QTUM, LTC, NEO, ETH, BNB]


def actual_price(coin, qty, buyORsell):
    #The 'actual price' is contingnt on who is willing to trade with you and what THEIR price is. 
    #If you are to be buying that coin, you must be willing to pay the ask price (have to cross the spread for speed purposes)
    x = 0
    if buyORsell == 'SELL':
        x = 1
    pq_list = binance.depth(coin+'USDT', limit = 20)[x]
    p = float(pq_list[0][0]) #first book price
    q = float(pq_list[0][1]) #first book quantity

    #Test to see if the first book quantity is enough for purchase size
    # if so, return the first book price
    if q>qty:
        return p
    tq = q #if not, set total quantity = to first quantity (for now)
    cost = p*q #Keeping track of all prices and quantities (later to be divided by total quantity)
    counter = 1
    while tq <= qty: #operate until total quantity is > or = quantity of purchase
        p = float(pq_list[counter][0]) #next available book price (as per the counter)
        q = float(pq_list[counter][1]) #next available book quantity (as per the counter)
        if q + tq > qty: 
            cost+= p*(qty-tq)
            tq+=q
        else:
            tq+=q
            cost+= p*q
        counter+=1
    return cost/qty

def main(i):
    while True:
        for coin in type_a_coins:
            coin_name = coin.get_name()
            coin_markets = coin.getTypeBMarkets()

            for market in coin_markets:
                temp = market.split()
                base_name = temp[1]
                #get the USD market bid price
                book_holder = binance.depth(coin_name+'USDT', limit=5)[0][0] #the first [0] gives 'asks' second [0] gives first ask in book
                ask_qty = float(book_holder[1]) #ask quantity in terms of typeA coin (ie '50 XRP')
                ask_price = float(book_holder[0])         

                base_v_coin_holder = binance.depth(coin_name+base_name, limit=5)[1][0] #[1] gives 'bids', followed by [0] that gives first bid in book
                bid_qty = float(base_v_coin_holder[1]) #bid quantity in terms of typeA coin (ie '50 XRP')
                temp_bid_price = float(base_v_coin_holder[0])
                bid_price = temp_bid_price * actual_price(base_name, temp_bid_price*bid_qty, 'SELL')
                print('Made it',i)
                if bid_price > ask_price:
                    print('Market = ',market,'\nBid Price =',bid_price,'\nAsk Price =',ask_price,'\nqty =',min(bid_qty,ask_qty))
                i+=1
                    
'''
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
                    print(base,': ',base_price)

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
main(0)

