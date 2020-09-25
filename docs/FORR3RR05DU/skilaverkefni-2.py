"""
#1
Geri Fallið toDecimal sem inni heldur binary comma i sama sem 0

    svo búum við til n brytuna sem tekkur inn leingdina á binary
    svo ef i er sama sem n mínus 1
        svo skilar maður int binary[i] mínus 0
    
    svo skilar maður int binary[i] mínus 0 svo << n mínus i mínus 1 plus
                        toDecimal sem inni heldur binary comma i plus 1

    svo setur maður sérstakt breytu __name__ sama sem "__main__"
        svo gerum við breitunua binary = "1010"
        svo prentum við toDecimal sem inni helur binary

"""

#2 clue n**2
def margfoldun(n):
    if n == 0:
        return 0
    else:
        return margfoldun(n-1) + n**2

inp2 = int(input("#2 Slá inn heiltölu "))
print(margfoldun(inp2))

#3
def runa(m):
    if m == 0:
        return 0
    else:
        print(int(m*(m+1)/2))
        runa(m-1)

inp3 = int(input('#3 slá inn htölu '))
print(runa(inp3))

#4

def cross(n):
    if n == '':
        return 0
    else:
        return int(n[0]) + cross(n[1:])

inp4 = str(input("#4 Slá inn tölu "))
print(cross(inp4))

#5
def se(x, y):
    while(y):
        x, y = y, x % y
    return x

inp5x = int(input("#5 Slá inn x tölu "))
inp5y = int(input("#5 Slá inn y tölu "))
print(se(inp5x, inp5y))

