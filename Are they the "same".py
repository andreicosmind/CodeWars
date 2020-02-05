'''Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" 
elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
'''


def comp(array1, array2):
    if array1 == None or array2 == None: return False
    else:
        a = [x**2 for x in array1]
        return sorted(a) == sorted(array2)
