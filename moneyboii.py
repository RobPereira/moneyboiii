x = float(input("what is the annual multiplier"))
y = float(input("how much per year"))
z = int(input("how many years"))
t = float(input("starting total"))
temp = t
for i in range(z):
    t = t*x + y


for i in range(z):
    temp = temp+y
print("money in bank is", t)
print("total money input is", temp) 
print("mad profit is", t - temp)
    
