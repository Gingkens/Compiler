#coding:utf-8
from config import *
from testcase import *
from Lexical import Lexical
import re

class LittleWord:
    def __init__(self,file):
        self.out = []
        self.file = file
        self.funcs = [self.is_keyword,self.is_number,self.is_variable,
            self.is_operator,self.is_sentence,self.is_expression]
        self.cur_num = 0
        self.cur_line = ''

    def is_invaild(self,word):
        res = re.findall(reg_is_invaild, word)
        if len(res) != 0:
            self.get_error()

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
        res = re.findall(reg_is_variable,word)
        if not res:
            return False
        return (type_code['<var>'] , word)

    def is_operator(self,word):
        if word in operators:
            return (type_code[word],word)
        return False

    def is_sentence(self,word):
        res = re.findall(reg_is_sentence,word)
        if len(res) == 0:
            return False
        try:
            self.check(res[0][0])
            self.out.append(( type_code[':='],':=' ))
            self.check(res[0][1])
        except IndexError:
            return True

        return True

    def is_expression(self,word):
        res = re.findall(reg_is_expression ,word)       
        if len(res) == 0:
            return False
        try:
            self.check(res[0][0])
            self.out.append(( type_code[res[0][1]],res[0][1]))
            self.check(res[0][2])
        except IndexError:
            return True
        return True


    def check(self,word):
        if word == '':
            return True
        for func in self.funcs:             
            temp = func(word)
            if temp:
                if temp == True:
                    return True
                self.out.append(temp)
                return True

        self.get_error()

    def get_error(self):
        error = Lexical(self.file,self.cur_line,self.cur_num)
        error_info = error.get_info()
        print(error_info)
        exit(0)

    def parse(self,context):
        
        lines = context.split('\n')
        for line in lines:
            self.cur_num += 1
            self.cur_line = line
            if line.strip() == '':
                continue 
            words = line.split()
            for word in words:
                self.is_invaild(word)             
                sub_words = word.split(';')
                for sub in sub_words:     
                    self.check(sub)                                     
                    if len(sub_words) > 1:
                        self.out.append(( type_code[';'] ,';'))

    def getList(self):
        return self.out
             
if __name__ == '__main__':
    compiler = LittleWord('test1')
    print(test1.split('\n'))
    compiler.parse(test1)
    res = compiler.getList()
    print(res)
    


        

