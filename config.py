#coding:utf-8

"""
配置所有关键字以及操作符
"""

digital = [0,1,2,3,4,5,6,7,8,9]
char = 'a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z'
strong_operator = ' * | / '
weak_operator = '+ | -'
relation = '>= | =< |=  | <> | > | <'
grammar = '; | ( | ) '
keyword = ['read','write','if','then','else','fi','to','do','end','while','end']
s_operators = strong_operator.strip().split('|')
w_operators = weak_operator.strip().split('|')
relations = relation.strip().split('|')
chars = char.split('|')
grammars = grammar.strip().split('|')
#all_operator = strong_operator+'|'+weak_operator+'|'+relation+'|'+grammar
#all_operator = s_operators + w_operators + relations + grammars
# all_operator = [x+'|' for x in all_operator]
# all_operator = ''.join(all_operator)
# all_operator = all_operator.replace(' ','')
# all_operator = all_operator[:-1]
all_operator = ' \* | / | \+ | - |>=* | =< |=  | <> | > | <|\; | \( | \) '

operators = '= | =< | >= | < | > | <> |+ | -| * | /| ( | ) | := '
operators = operators.replace(' ','')
operators = operators.split('|')
type_list = [keyword,s_operators,w_operators,relations,grammars]
#print(type_list)

type_code ={
'fi':1,
'if':2,
'then':3,
'while':4,
'do':5,
'end':6,
'else':7,
'to':8,
'read':9,
'write':10,
'+':14,
'-':15,
'*':16,
'/':17,
':=':18,
'<':20,
'<>':21,
'<=':22,
'>':23,
'>=':24,
'=':25,
';':26,
'(':27,
')':28,
'<var>':29,
'<const>':30,
'#':0
}
