alph = list('qwertyuiopasdfghjklzxcvbnm')
class codificator:
    def __init__(self,coded,decoded):
        self.coded: str = coded
        self.decoded: str = decoded
    def codification(self,decoded):
        global alph
        coded = ""
        for i in range(0,len(decoded)):
            coded+=alph[(i+3)%len(alph)]
        return coded
    def decoding(self,coded):
        global alph
        decoded = ""
        for i in range(0,len(coded)):
            decoded+=alph[(i-3)%len(alph)]
            return decoded
