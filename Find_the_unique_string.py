'''There is an array of strings. All strings contains similar letters except one. Try to find it!
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings. '''


def find_uniq(arr):

    b = [("".join(set(sorted(x.lower())))) for x in arr]
    b = [x.replace(' ', '') for x in b]
    c = list(set(b))
    for x in c:
        if b.count(x) == 1:
            return arr[b.index(x)]
            break
