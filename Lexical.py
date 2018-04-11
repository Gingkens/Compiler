#coding:utf-8

class Lexical():
    def __init__(self,filename,ErrorInfo,line):
        self.line = line
        self.ErrorInfo = ErrorInfo
        self.filename = filename
    
    def __str__(self):
        error = '\nFile "{}", line {} \n  {}\n\n SyntaxError: invalid syntax'.format(
            self.filename,self.line,self.ErrorInfo
        )
        return error
    
    def get_info(self):
        return self.__str__()


