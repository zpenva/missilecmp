def age(n):
    if n == 1:
        return 10
    else:
        return age(n-1)+2

print(age(5))

result = []
def fenjie(n):
    if n>0:
        result.insert(0,n%10)
        fenjie(n//10)

fenjie(123456)
print(result)
    
