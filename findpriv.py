from bitcoin import *   # need to import https://pypi.org/project/bitcoin/  a very clean lib from Vitalik Butarin

print('Starting scan...')
Yourname='Yourname'

while True:

    priv=random_key()
    pub=privtopub(priv)
    addr=pubtoaddr(pub)
    if pub[1:len(Yourname)]=='Yourname':   #Find a btc address with "Yourname" eg.: 1Yournamexxxxxxxxxxx
            print(priv,pub,addr)   
