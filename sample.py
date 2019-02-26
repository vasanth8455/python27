'''
def vasanth(x,y):
    return x*y,x+y,x%y
print vasanth(11,20)

#local variable
def get(x=10,y=30):
   return x+y,x*y,x%y
print get()

#global variable

x = 'sekhar'
y = 'reddy'
def sam():
   global x,y
   x=30
   return x+y
print sam()
'''
#revers of the string
s=raw_input('Enter your stirng :')
s1=''
for x in s:
   s1=x+s1
print s1
