''' Linear Search '''

def linear(arr,key):
     n = len(arr)
     for i in range (0,n):
         if (arr[i] == key):
             return i;
     return -1;

'   Driver Code '
arr = [32,4,341,7,56,4,2]
key = 32
result = linear(arr,key)
if (result == -1):
    print(' Key does not exits! ');
else:
    print(' Key '+ str(key) +' Exits at '+ str(result) + ' index');
