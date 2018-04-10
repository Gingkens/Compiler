#coding:utf-8
test1 = '''
read n; 
to n do
read x;
if x>0 then
y := 1; z :=1;
while z<>x do
z := z+1;
y := y*z
end;
write y
fi
end
'''

test2 = '''
n=1;
while n<>0 do
read x;
sum=0;
while x>0 do
sum=sum+x;
x=x-1;
end;
write sum;
read n;
end;

'''