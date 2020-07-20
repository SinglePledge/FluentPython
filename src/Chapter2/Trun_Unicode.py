# 普通的写法
symbols = '!@#$%^'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

print('---')
# 列表推导
codes1 = [ord(symbol) for symbol in symbols]
print(codes1)
# filter with map
beyond_ascii = [ord(s) for s in symbols if ord(s) > 33]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 33, map(ord, symbols)))
print(beyond_ascii)
# if you need a list , in this list, it has 3 different type of T-shirt,each size have 2 type of color
colors = ['blue', 'red']
sizes = ['S', 'M', 'L']
# order by color
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
# It's same order as last one
for color in colors:
    for size in sizes:
        print((color, size))
# Order by size
tshirts = [(color, size) for size in sizes
           for color in colors]
print(tshirts)
# 生成器表达式
symbols = "!@#$%^"
# 如果生成器表达式是函数调用过程中的唯一参数,那么就不需要用括号括起来
symbols_tuple = tuple(ord(symbol) for symbol in symbols)
print(symbols_tuple)
import array

# array函数需要两个参数,所以需要括号,array构造方法的第一个参数指定了数组中数字的存储方式
a1 = array.array('I', (ord(symbol) for symbo in symbols))
print(a1)
# 使用生成器表达式计算卡迪尔积
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
for tshirts in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirts)
# 使用生成器表达式,内存中不会留下6个组合的列表,因为生成器会在每次for循环时才生成一个组合,
