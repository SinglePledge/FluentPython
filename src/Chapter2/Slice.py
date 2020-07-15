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
