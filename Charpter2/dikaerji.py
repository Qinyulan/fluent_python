"""用列表生成式生成两个或两个以上的可迭代的第卡尔积"""

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
"""先以颜色排列再以尺码排列"""
for color in colors:
    for size in sizes:
        print(color, size)
"""先以尺码排列再以颜色排列"""
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)