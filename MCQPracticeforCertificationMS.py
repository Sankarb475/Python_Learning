f = 100
print("outside F", f)
def meth1(a):
    global f
    f = f + a
    print("Inside F", f)

meth1(12)

output ==> 
outside F 100
Inside F 112

==============================================================================================================================

f = 100
print("outside F", f)
def meth1(a):
    global f
    f = f + a
    print("Inside F", f)
    return f

def meth2(a):
    global f
    f = a + 10
    f = f + meth1(a)
    print(f)

meth2(10)

output ==>

outside F 100
Inside F 130
250

==============================================================================================================================





