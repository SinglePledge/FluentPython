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
#seq[start:stop:step]求值,python会调用seq.__getitem__(slice(