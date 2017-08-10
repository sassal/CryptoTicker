import json
import urllib2

# balances - add your balances
#  cryptocurrencies are floats, spentaud is type int
btc = 0.0
eth = 0.0
dnt = 0.0
spentaud = 0

# apis
bitcoin = "https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=AUD"
ethereum = "https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=AUD"
district0x = "https://api.coinmarketcap.com/v1/ticker/district0x/?convert=AUD"

# download data
bitcoindata = json.load(urllib2.urlopen(bitcoin))
ethereumdata = json.load(urllib2.urlopen(ethereum))
district0xdata = json.load(urllib2.urlopen(district0x))

print 'Current Prices (AUD):'
print 'Bitcoin: ', bitcoindata[0]['price_aud']
print 'Ethereum: ', ethereumdata[0]['price_aud']
print 'District0x: ', district0xdata[0]['price_aud']
print '\n'

totalbtc = float(bitcoindata[0]['price_aud']) * btc
totaleth = float(ethereumdata[0]['price_aud']) * eth
totaldnt = float(district0xdata[0]['price_aud']) * dnt

print 'Assets (AUD):'
print 'Bitcoin: ', totalbtc
print 'Ethereum: ', totaleth
print 'District0x: ', totaldnt
print '\n'

grandtotal = totalbtc + totaleth + totaldnt

print 'Total (AUD):'
print '$', grandtotal
print '\n'
print 'Profit (AUD):'
print '$', grandtotal - spentaud
