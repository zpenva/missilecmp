list1=[]
def get_digits(n):
    if n > 0:
        list1.insert(0,n%10)
        get_digits(n//10)

get_digits(12345)
print(list1)
    
