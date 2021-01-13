# def sub (num1,num2):
#     return num1-num2

def syb_dec(func):
    def wrap(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
            return func(num1,num2)
        else:
            return func(num1, num2)
    return wrap
@syb_dec
def sub(num1,num2):
    return num1-num2

res=sub(60,50)
print(res)


