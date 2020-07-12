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
