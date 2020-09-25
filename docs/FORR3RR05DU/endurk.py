

"""
#leggjum saman n fyrstu tölurnar í rununni frá 1 upp í n t.d. 1+2+3+4+5....+n
def summan(n):
    if n == 1:
        return 1
    else:
        return n + summan(n-1)

print(summan(3))


#endurkvæmt fall sem leggur saman talnarunu
def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n-1)


#telur niður
def teljaNiður(n):
    if n == 1:
        print(n, end=' ')
    else:
        print(n, end=' ')
        teljaNiður(n-1)


#telur upp
def teljaUpp(n):
    if n == 1:
        print(n, end=' ')
    else:
        teljaUpp(n-1)
        print(n, end=' ')
 

cnt = int(input("Slá inn heiltölu "))
teljaNiður(cnt)
print('----------')
teljaUpp(cnt)
print('----------')
print(summa(cnt))
print('----------')
"""
#verkefni Endurkvæmni

#1
def margfoldun(n):
    if n == 1:
        print(2**n)
    else:
        margfoldun(n-1)
        print(2**n)

inp1 = int(input("#1 Slá inn heiltölu "))
margfoldun(inp1)

#2
def teljaUpp2(n):
    if n == 1:
        print(n, end=' ')
    else:
        teljaUpp2(n-1)
        print(n, end=' ')

inp2 = int(input("#2 Slá inn heiltölu "))
teljaUpp2(inp2)

#3
def teljaUpp3(n):
    if n == 0:
        print(n, end=' ')
    else:
        teljaUpp3(n-1)
        print(n, end=' ')

inp3 = int(input("#3 Slá inn heiltölu "))
teljaUpp3(inp3)

#4
def teljaUpp4(n):
    if n == 0:
        print(n, end=' ')
    else:
        print(n, end=' ')
        teljaUpp4(n-1)

inp4 = int(input("#4 Slá inn heiltölu "))
teljaUpp4(inp4)

#5
def summan(n):
    if n == 1:
        return 1
    else:
        return n + summan(n-1)
    
inp5 = int(input("#5 Slá inn heiltölu "))
print(summan(inp5))

#6
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)
    
inp6 = int(input("#6 Slá inn heiltölu "))
print(fac(inp6))


#7
def howLongStr(str):
    if str == True:
        return str
    else:
        return len(str)

inp7 = str(input("#7 Slá inn orð "))
print(howLongStr(inp7)) 


#8
def texti(s):
    if s == "":
        print()
    else:
        print(s[0])
        texti(s[1:])

inp8 = str(input("#8 Slá inn orð "))
texti(inp8)


#9
listi = ["a","e","i","o","u"]
def readlist(i):
    if i == "":
        return 0
    else:
        if i[0].lower() in listi:
            return 1 + readlist(i[1:])
        else:
            return readlist(i[1:])

inp9 = str(input("#9 Slá inn orð "))
print("Fjöldi sérhljóða" ,readlist(inp9))

#10
def texts(s):
    if s == "":
        print()
    else:
        print(s[:])
        texts(s[1:])

inp10 = str(input("#10 Slá inn orð "))
texts(inp10)