class Vault:
    def __init__(self, won=0, yen=0, usd=0):
        self.won = won
        self.yen = yen
        self.usd = usd

    def __str__(self):
        return f"{self.won} wons, {self.yen} yens, {self.usd} dollars"

    def __add__(v1,v2):
        w = v1.won+v2.won
        y = v1.yen+v2.yen
        d = v1.usd+v2.usd
        return Vault(w,y,d)

vLisa = Vault(100000,5000,2500)
print(vLisa)

vRose = Vault(100000,50000,25000)
print(vRose)

total = vLisa + vRose
print("Total is: ",total)
