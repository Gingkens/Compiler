#coding:utf-8
from config import *
from testcase import *
import re

class LittleWord:

    def __init__(self):
        self.out = []
        self.funcs = [self.is_keyword,self.is_number,self.is_variable,
            self.is_operator,self.is_sentence,self.is_expression]

    def is_invaild(self,word):
        res = re.findall('([0-9]+[a-z]+[0-9|a-z]*)', word)
        if len(res) != 0:
            print('非法标识符：' + res)
            return True
        return False

    def is_keyword(self,word):
        if word in keyword:
            return (type_code[word],word)       
        return False
        
    def is_number(self,word):
        try:
            float(word)
            return (type_code['<const>'],float(word))
        except ValueError:
            return False
    
    def is_variable(self,word):
        res = re.findall('([a-z]+[a-z|0-9]*$)',word)
        if not res:
            return False
        return (type_code['<var>'] , word)

    def is_operator(self,word):
        if word in operators:
            return (type_code[word],word)
        return False

    def is_sentence(self,word):
        res = re.findall('^([a-z]*.*?):=(.*)',word)
        if len(res) == 0:
            return False

        if len(res[0]) == 2:
            if res[0][0] != '':

                if not self.add(res[0][0]):
                    
                    return False
            else:
                if not self.add(res[0][1]):
                    
                    return False
        else:
            var = res[0][0]
            if not self.add(var):
                return False
            self.out.append(( type_code[':=' ,':='] ))

            experssion = res[0][1]
            if not self.add(experssion):
                return False

        return True

    def is_expression(self,word):
        reg = ' \*| / | \+ | - | >= | =< |=  | <> | > | <'
        reg = reg.replace(' ','')
        res = re.findall('(.*?)(%s)(.*)'%reg ,word)
        if len(res) == 0:
            return False
        
        exp1 = res[0][0]
        if not self.add(exp1):
            return False
        operator = res[0][1]
        self.out.append( (type_code[operator],operator) )
        exp2 = res[0][2]
        if not self.add(exp2):
            return False
        return True

    def add(self,word):
        for func in self.funcs:             
            temp = func(word)
            if temp:
                if temp == True:
                    return True
                self.out.append(temp)
                return True

        print('Syntax error!  ' + word)
        return False

    def parse(self,words):
    
        for word in words:
            word = word.replace('','')

            if self.is_invaild(word):
                return False

            sub_words = word.split(';')
            for sub in sub_words:   
                if sub == '':
                    continue  
                if not self.add(sub):
                    return False
                
                if len(sub_words) > 1:
                    self.out.append(( type_code[';'] ,';'))

    def getList(self):
        return self.out
    
         
if __name__ == '__main__':
    compiler = LittleWord()
    print(test2.split())
    compiler.parse(test2.split())
    res = compiler.getList()
    print(res)
    


        

