class Node: 
    # Smiður, frumstillir d og núllstillir bendana prv og nxt
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    # Endurkvæmt fall sem prentar listann.
    def printList(self):
        if self.nxt is None:
            print(self.data, end=' ')
        else:
            print(self.data, end=' ')
            self.nxt.printList()

    # Endurkvæmt fall sem bætir aftast á listann.   
    def append(self,d):
        if self.nxt is None:
            n  = Node(d)
            self.nxt = n
            self.nxt.prv = self
        else:
            return self.nxt.append(d)


             
    # Endurkvæmt fall sem athuga hvort stak d er í listanum.
    def find(self, d):
        if self.data == d and self.nxt is None:
            print('True')
            return True
        elif self.data == d and self.nxt is not None:
            print('True')
            return True
        elif self.data != d and self.nxt is None:
            print('False')
            return False
        else:
            return self.nxt.find(d)

    # Endurkvæmt fall sem eyðir staki d úr listanum.
    def delete(self, d):
        if self.data == d and self.nxt is None:                     # erum að eyða endahnút ...
            self.prv.nxt = None
            self.prv = None
            return True
        elif self.data == d and self.nxt is not None:               # erum að eyða hnút sem er ekki í enda ...
            self.prv.nxt = self.nxt
            self.nxt.prv = self.prv
            return True
        elif self.data != d and self.nxt is None:                   # erum komin út í enda en finnum ekki hnútinn, eyðum engu
            return False
        else:                                                       # ekki réttur hnútur, förum í næsta enduerkvæmt
            return self.nxt.delete(d)

class DLL:
    # Smiður, núllstillir Haus listans
    def __init__(self):
        self.head = None

    # Bætir við fremst á listann, hnúturinn verður Head -> förum ekki í Node klasann.
    def push(self,d):
        if self.head is None:
            self.head = Node(d)
        else:
            n = Node(d)
            n.nxt = self.head
            self.head.prv = n
            self.head = n
    
    # Bætir við aftast á listann -> kallar á endurkvæmnt fall í Node.
    def append(self, d):
        if self.head is None:
            self.head = Node(d)
        else:
            self.head.append(d)

    # Prentar listann allan á skjá -> kallar á endurkvæmt fall í Node.
    def printList(self):
        if self.head is None:
            print('Tómur................................................................................................................................................................')
        else:
            self.head.printList()
   
    # Finnur stak d í ef til -> kallar á endurkvæmnt fall í Node.
    def find(self, d):
        if self.head is None:
            print('Það er ekkert í listanum')
            return False
        else:
            return self.head.find(d)

    # Eyðir staki d úr lista ef til -> kallar á endurkvæmnt fall í Node.
    def delete(self, d):
        if self.head is None:                                   # Ef satt þá er listinn tómur, ekkert til að eyða skilum False
            print('Það er ekkert til að eyða')
            return False
        elif self.head.nxt is None and self.head.data == d:      # Aðeins einn hnútur í lista, eyðum honum og skilum True
            self.head = None
            return True
        elif self.head.data == d:                                # Eyðum fremsta en það eru fleiri hnútar
            self.head = self.head.nxt
            self.head.prv.nxt = None
            self.head.prv = None
            return True
        else:
            # Förum yfir í Node og þræðum okkur eftir listanum...
            return self.head.delete(d)
        
"""
# Keyrslurútína
dbl = DLL()
dbl.push(5)           # 5
dbl.push(3)           # 3 5
dbl.append(7)         # 3 5 7
dbl.append(4)         # 3 5 7 4
dbl.printList()
dbl.delete(3)         # 5 7 4
print('\n')
dbl.printList()
print('\n',dbl.find(3))

"""
dbl = DLL()
dbl.append(5)           # 5
dbl.append(7)           # 5 7         
dbl.push(1)             # 1 5 7 
dbl.push(0)             # 0 1 5 7 
dbl.append(10)          # 0 1 5 7 10
dbl.printList()         
print()
print(dbl.delete(5))   # 0 1 7 10
dbl.printList() 
print()
dbl.find(5)     # False
dbl.find(7)     # True
