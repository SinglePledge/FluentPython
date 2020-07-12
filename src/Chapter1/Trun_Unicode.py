#普通的写法
symbols = '!@#$%^'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

print('---')
#列表推导
codes1= [ord(symbol) for symbol in symbols]
print(codes1)
#filter with map
beyond_ascii = [ord(s) for s in symbols if ord(s) > 33]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c:c>33,map(ord ,symbols)))
print(beyond_ascii)
# if you need a list , in this list, it has 3 different type of T-shirt,each size have 2 type of color
colors = ['blue','red']
sizes = ['S','M','L']
#order by color
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)
#It's same order as last one
for color in colors:
    for size in sizes:
        print((color,size))
#Order by size
tshirts = [(color,size) for size in sizes
                        for color in colors]
print(tshirts)