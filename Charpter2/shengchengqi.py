import array

symbols = "@#$%^&"
num = tuple(ord(symbol) for symbol in symbols)
print(num)
num1 = array.array('I', (ord(symbol) for symbol in symbols))
print(num1)
colors = ['black', 'white']
size = ['S', 'M', 'L']
for tshirt in ('%s %s'%(c, s)for c in colors for s in size):
    print(tshirt)


"""生成器表达式逐个产出元素，不会一次性吧所有的元素产出放在一个列表中"""