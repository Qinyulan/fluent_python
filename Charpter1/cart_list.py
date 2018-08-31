import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
# Returns a new subclass of tuple with named fields.


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')


print(beer_card)
deck = FrenchDeck()


print(len(deck))
print(deck[13])


print(type(Card))
"""
首先明确一点，特殊方法的存在是为了被 Python 解释器调用的，你自己并不需要调用它
们。也就是说没有 my_object.__len__() 这种写法，而应该使用 len(my_object)。在
执行 len(my_object) 的时候，如果 my_object 是一个自定义类的对象，那么 Python 会
自己去调用其中由你实现的 __len__ 方法。
然而如果是 Python 内置的类型，比如列表（list）、字符串（str）、字节序列
（bytearray）等，那么 CPython 会抄个近路，__len__ 实际上会直接返回
PyVarObject 里的 ob_size 属性。PyVarObject 是表示内存中长度可变的内置对象的 C
语言结构体。直接读取这个值比调用一个方法要快很多。
很多时候，特殊方法的调用是隐式的，比如 for i in x: 这个语句，背后其实用的是
iter(x)，而这个函数的背后则是 x.__iter__() 方法。当然前提是这个方法在 x 中被实
现

"""