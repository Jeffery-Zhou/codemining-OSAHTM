# coding:utf-8
"""
python中的编码：
ascll编码：只用来将常用的英文字符编入，1byte。
每个国家有各自的编码，中文有GB2312，韩文Euc-kr，日文有Shift_jis等。
Unicode统一了所有各国编码，都编入其中，通常2byte。
但是为了节省（考虑传输的unicode中含有大量的英文），可变长UTF-8编码。
将Unicode编成1~6byte。
计算机的内存中统一是unicode编码
"""

print ord('B')
print ord('b')
print chr(98)
print chr(66)

print u'周鹏'
print u'周'
print u'鹏'


print len("ABC")
print len(u"ABC")
print len(u"ABC".encode('utf-8'))

print len(u'周鹏')
print len(u'周鹏'.encode('utf-8'))

print "周鹏".decode('utf-8')

classmates = ['Michael', 'Bob', 'Tracy']
print classmates[0]

for i in classmates:
    print i

name_lst = ["周鹏", "邓爷", "陶总"]
print name_lst
for j in name_lst:
    print j


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


