'''   Bubble Sort  '''

def sort(lst):
    n=len(lst)
    swap=False
    for i in range(n):
        swap=False
        for j in range(n-i-1):
            if(lst[j]> lst[j+1]):
                lst[j],lst[j+1]=lst[j+1],lst[j] 
                swap=True
        if (swap==False):
            break

'  list for sorting  '
list=[]
n=int(input('Enter length of collection elements!'))
for i in range(n):
    ele=int(input('Enter '+str(i)+' Element!'))
    list.append(ele)
sort(list)
print('Sorted elements are:')
for j in range(n):
    print(str(list[j]))
    

