'''Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying F(n) * F(n+1) = prod.
Your function productFib takes an integer (prod) and returns an array: [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return 
[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)'''

def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b] 
