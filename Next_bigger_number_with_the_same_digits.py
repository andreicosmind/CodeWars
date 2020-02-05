# You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

def next_bigger(n):

    digits = [int(x) for x in str(n)]
    
    for x in range(len(digits)-1, 0, -1):
        if digits[x] > digits[x-1]:
            slice = [digits[x-1]] + sorted(digits[x:])
            digits[x-1:] = []
            
            for i in range(len(slice)-1):
                if slice[0] < slice[i+1]:
                    slice[0], slice[i+1] = slice[i+1], slice[0]
                    digits.append(slice[0])
                    slice.pop(0)
                    digits += sorted(slice)
                    break
                    
            return int(''.join([str(i) for i in digits]))
    return -1
