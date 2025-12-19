alph = list('qwertyuiopasdfghjklzxcvbnm')
def codification(decoded):
    global alph
    coded = ""
    for i in range(0,len(decoded)):
        coded+=alph[(i+3)%len(alph)]
    return coded
def decoding(coded):
    global alph
    decoded = ""
    for i in range(0,len(coded)):
        decoded+=alph[(i-3)%len(alph)]
        return decoded
