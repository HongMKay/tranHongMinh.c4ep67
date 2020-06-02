siz = [5, 7, 300, 90, 24, 50, 75]

input(f"Hello my name is Kay and these are my sheep sizes {siz}")
big1 = max(siz)
ind = siz.index (big1)
siz[ind]= 8
input(f"Now my biggest sheep has size {big1} let's shear it")
print(f"After shearing, here is my flock {siz}")
print()

month = ["MONTH 1:", 'MONTH 2:', "MONTH 3:"]
for b in range (3):
    input(month[b])
    for i in range (0,7):
            siz[i] += 50
    input(f"One month has passed, now here is my flock {siz}")
    if b < 2:
# find the biggest sheep
        big1 = max(siz)
        ind = siz.index (big1)
        siz[ind]= 8
        input(f"Now my biggest sheep has size {big1} let's shear it")
        print(f"After shearing, here is my flock {siz}")
        print()

    else:
        c = sum(siz)
        input(f"My flock has size in total: {c}")
        d = c *2
        input(f"I would get {c} * 2$ = {d}$")
print()




