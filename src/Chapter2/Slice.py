#列表list,元组tuple,字符串str都支持切片操作

l = [10, 20, 30, 40, 50, 60]
print(l[:2])#在下标2的地方分割
print(l[2:])
print(l[:3])#在下标3的地方分割
print(l[3:])
#list[start:stop],返回下标为stop-start

#对象切片,s[a:b:c],对s在a和b之间以c为间隔取值
s='bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])
#seq[start:stop:step]求值,python会调用seq.__getitem__(slice(start,stop,step))

invoice = """
0.....6................................40........52...55........
1909    Pimoroni PiBrella                 $17.50     3     $52.50
1489    6mm Tactile Switch x20            $4.95      2     $9.90
1510    Panavise Jr. - PV-201             $28.00     1     $28.00
1601    PiTFT Mini Kit 320x240            $34.95     1     $34.95
"""
SKU=slice(0,6)
DESCRIPTION=slice(6,40)
UNIT_PRICE=slice(40,52)
QUANTITY = slice(52,55)
ITEM_TOTAL = slice(55,None)
line_items= invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE],item[DESCRIPTION],item[SKU],item[QUANTITY],item[ITEM_TOTAL])

#[]运算符里还可以使用逗号分开多个索引或者是切片

#如果将切片放在赋值语句的左边,或把它作为del操作的对象,我们就可以对序列进行嫁接,切除或就地修改操作
l1 = list(range(10))
print(l1)
l1[2:5] = [20, 30]
print(l1)
del l1[5:7]
print(l1)
l1[3::2] = [11,22]
print(l1)
#l1[2:5]=100 typeerror: can only assign an iterable
#如果赋值的对象是一个切片,那么赋值语句的右侧必须是个可以迭代对象.即使只有单独的值,也要把它转换成可迭代的序列
l1[2:5] = [100]
print(l1)
#对序列使用+和*
l = list(range(3))
print(l*5)
print(8*'ab')
#+号两侧相同类型的数据
#两个操作符号都遵循着一个规律,不修改原有的操作对象,而是构建一个全新的序列
#如果在a*n这个语句中,如果序列a里的元素是对其他可变对象的引用的话,需要格外注意
#如:my_list=[[]]*3来初始化一个有列表组成的列表,你得到的列表包含的3个元素其实是3个引用,这三个引用执行的都是同一列表

#建立有列表组成的列表
board = [['_']*3 for i in range(3)]
print(board)
board[1][2] ='x'
print(board)
#wrong example
weird_board = [['_']*3]*3
print(weird_board)
weird_board[1][2] = 'o'
print(weird_board)
#same type wrong with last example
row = ['_']*3
board = []
for i in range(3):
    board.append(row)
#right example
board = []
for i in range(3):
    row=['_']*3
    board.append(row)
print(board)
board[0][0]='X'
print(board)