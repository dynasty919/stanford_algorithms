# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 3:57
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : week1_pa1.py
# @Software: PyCharm

def multiply(x, y):

    l1 = len(x)
    l2 = len(y)


    if min(l1, l2) == 1:
        return int(x) * int(y)
    else:
        if min(l1, l2)%2 != 0:
            l = int(min(l1, l2)/2 +0.5)
        else:
            l = int(min(l1, l2)/2)

        l3 = len(x) - l
        b = x[l3:]
        a = x[:l3]
        l4 = len(y) - l
        d = y[l4:]
        c = y[:l4]

        e = str(int(a) + int(b))
        f = str(int(c) + int(d))
        return (10**(2*l) - 10**(l)) * multiply(a, c) + (1 - 10**(l)) * multiply(b, d) + 10**(l) * multiply(e, f)

x = '3141592653589793238462643383279502884197169399375105820974944592'*99
y = '2718281828459045235360287471352662497757247093699959574966967627'*99
result = multiply(x, y)
print(result)
print(int(x) * int(y))