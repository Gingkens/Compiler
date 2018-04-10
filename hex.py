#coding:utf-8

dex_str = ['0','1','2','3','4','5','6','7','8','9',
'A','B','C','D','E','F']

def recognize(strings):
    strings = strings.upper()

    if strings[-1] != 'H':
        print('符号串应以H结束')
        return False

    res = map(lambda x:1 if x not in dex_str else 0,strings[:-1])  
    if sum(res) != 0:
        print('字符应为：%s 之一'%dex_str)
        return False
    print(strings)
    return True

recognize('0AFH')

    