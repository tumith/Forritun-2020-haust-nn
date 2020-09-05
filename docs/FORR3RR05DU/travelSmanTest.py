import random
kH = 703
kR = 47
kKir = 296
kS = 332

rS = 290
rH = 628
rKir = 257

sKir = 532
sH = 394

kirH = 471

i = [703,47,296,332,290,628,257,532,394,471]

def f():
    global i 
    nui = random.randint(0,10)
    while len(i) > 0:
        i.pop(nui)

f()

