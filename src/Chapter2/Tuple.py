from collections import namedtuple

# 洛杉矶的国际机场的经纬度
lax_coordinates = (33.9425, -118.408056)
# 东京市的一些信息:名字,年份,人口(单位:百万),人口变化(单位:百分比)和面积(单位:平方千米)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# 一个元组列表,元组的形式为(country_code,passport_number)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# 在迭代的过程中,passport变量绑定到每个元组上
for passport in sorted(traveler_ids):
    print('%s %s' % passport)
# for循环可以分别提取元组中的元素,叫做拆包(unpacking),由于该元组中的第二个元组没有用,将他赋值给占位符placeholder'_'
for country, _ in traveler_ids:
    print(country)
# 平行赋值:将一个可迭代对象里的元素,一并赋值到相对应变量组组成的元组中
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)
# 用运算符*可以把可迭代对象拆开作为函数的参数
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient)
print(remainder)
# 让一个函数可以用元组的形式返回多个值,然后偶调用函数的代码就能接受这些返回值
import os

_, filename = os.path.split('d:\\1.txt')
print(filename)
# _在gettext模块中,这个符号是一个特殊的函数常用名

# *来处理剩下的元素
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)
# 在平行赋值中,*前缀智能用在一个变量名面前
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(head, b, c, d)
# 嵌套元组(a,b,(c,d)),拆包unpacking
# 每个元组中有四个元素,其中最后一个元素是一对坐标
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('CityName', 'lag.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
# 把最后一个元素拆包有变量构成的元组里,就获取到了坐标
for name, cc, pop, (latitude, longitude) in metro_areas:
    # 条件判断,限制在西半球的城市
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
# python3中不在支持将元组最为参数,放置于函数声明中

# 具名元组
# collections.namedtuple是一个工厂函数,他可以用来构建一个带字段的院子和一个有名字的累
# 创建一个具名元组需要两个参数,一个是类名,另一个是类的各个字段的名字
# 后者一般由数个字符串组成可迭代对象,或者由空格分开的字段组成的字符串
City = namedtuple('City', 'name country population coordinates')
# 存放在对应字段里的数据要以一串参数的形式传入到构建函数中
# 元组的构造函数却只能接受单一的可迭代对象
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
# _fieled类属性
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# _make(iterable)实例方法
delhi = City._make(delhi_data)
# 和*一样
delhi1 = City(*delhi_data)
# _asdict(),把具名元组以collections.OrderedDict的形式返回
print(delhi._asdict())
print(delhi1._asdict())
for key, value in delhi._asdict().items():
    print(key + ' : ', value)
