'''   Prime Test   '''

def is_prime(n):
    'prime started 2,3,5 ....'
    if (n>=2):
        'divides number by its whole range numbers'
        for i in range(2,n):
            'if whole dividisible returns false=0'
            if not(n%i):
                return False
    else:
        return False
    return True
'Test Number'
count=0
for i in range(int(input("Enter number for prime test! "))):
    if(is_prime(i)):
        count+=1
        print(i)

print('There '+str(count)+' prime number/s found!')
