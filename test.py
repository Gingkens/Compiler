#coding:utf-8
import re
from config import *

express = 'abc'
express = express.replace(' ','')
relate = relation.replace(' ','')
# print(relate)
# print(re.findall( '(.*)(?:%s)(.*)'%relate,express ))
# s = ' \*| / | \+ | - | >= | =< |=  | <> | > | <|\; | \( | \) '
# s = s.replace(' ','')
# print(s)
# res = re.findall( '(.*?)(%s)(.*)'%s,express )
# print(res)
# print(len(res))
# print( res[0] )
# print( '(?:%s)'%relate )
# print( re.findall('(.*?)(?:%s)(.*)'%relate ,express) )
#print(re.findall('(?:aP|ap)ython','Hello aPython'))
#print('(?:%s)'%all_operator.replace(' ',''))
#print(all_operator)
#alls = all_operator.replace(' ','')
#print(alls)
#print( re.findall('(.*?)(?:%s)(.*)'%alls ,express) )
# c = [x+'|' for x in all_operator]
# t = ''.join(c)
# t = t.replace(' ','')
# print(t)
# t = t[:-1]
# print(t)
# print(all2)
# print(c)
# c  = ''.join(all_operator)
# c = c.replace(' ','')
# print(c)
# c = re.escape(c)
# print(c)

# print( re.findall('.*a(?:/*)a.*','a*aaaabb') )
word = 'sum=sum+x'
res = re.findall('(^[a-z]+[a-z|0-9]*$)',word)
print(res)