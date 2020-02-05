'''There is an array with some numbers. All numbers are equal except for one. Try to find it!
findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance. '''


def find_uniq(arr):
    arr1 = list(set(arr))
    return arr1[1] if arr.count(arr1[0]) != 1 else arr1[0]
    
