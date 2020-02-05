Write a function with the signature shown below:
def is_int_array(arr):
    return True

returns true / True if every element in an array is an integer or a float with no decimals.
returns true / True if array is empty.
returns false / False for every other input '''

def is_int_array(arr):
    if arr == []:
        return True
    elif arr == None or arr == "":
        return False
    else:
        for i in arr:
            if type(i) is int or (type(i) is float and  i.is_integer()):
                pass
            else:
                return False
        return True
