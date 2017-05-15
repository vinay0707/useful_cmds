import fibo

s = 'Hello, world.'
print s

str(s)
print s

repr(s)
print s

for x in range(1,11):
    print repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4)

10 * (1/1)

fibo.fib(500)



def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print "Divide by Zero"
    else:
        print "Result is: " , result
    finally:
        print "executing finally clause"

divide(5,2)