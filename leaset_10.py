n=32499;
if(n<10):
    len=0;
else:
    len=1;
while(n>=10):
    len = len*10;
    n=n/10;
print(len)
