import http.client


class marketData():
    def __init__(self) -> None:
        self.__url = "coinranking1.p.rapidapi.com"
        
        
        self.headers = {'X-RapidAPI-Key': "f27c6fab33msh64745564e4b19d2p133fcdjsn07aa65cef4eb",'X-RapidAPI-Host': "coinranking1.p.rapidapi.com"}
        
    def ___getCoins(self):
        conn = http.client.HTTPSConnection(self.__url)
        conn.request("GET", "/coins?referenceCurrencyUuid=yhjMzLPhuIDl&timePeriod=24h&tiers%5B0%5D=1&orderBy=marketCap&orderDirection=desc&limit=50&offset=0", headers=self.headers)
        res = conn.getresponse()
        data = res.read()
        print(type(data))
        return data.decode("utf-8")
    def getEth(self):
        res = self.___getCoins()
        #print(type(res))
    


if __name__ == "__main__":
    clen = marketData()
    clen.getEth()


