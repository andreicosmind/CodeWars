'''Your plan
When a minute is evenly divisible by three, the clock will say the word "Fizz".
When a minute is evenly divisible by five, the clock will say the word "Buzz".
When a minute is evenly divisible by both, the clock will say "Fizz Buzz", with two exceptions:
On the hour, instead of "Fizz Buzz", the clock door will open, and the cuckoo bird will come out and "Cuckoo" between one and twelve times depending on the hour.
On the half hour, instead of "Fizz Buzz", the clock door will open, and the cuckoo will come out and "Cuckoo" just once.
With minutes that are not evenly divisible by either three or five, at first you had intended to have the clock just say the numbers ala Fizz Buzz, but then you decided at least for version 1.0 to just have the clock make a quiet, subtle "tick" sound for a little more clock nature and a little less noise.
Your input will be a string containing hour and minute values in 24-hour time, separated by a colon, and with leading zeros. For example, 1:34 pm would be "13:34".

Your return value will be a string containing the combination of Fizz, Buzz, Cuckoo, and/or tick sounds that the clock needs to make at that time, separated by spaces. Note that although the input is in 24-hour time, cuckoo clocks' cuckoos are in 12-hour time.
'''


def fizz_buzz_cuckoo_clock(time):
    if time[-2:] == '00':
        if int(time[:2]) > 12 or int(time[:2]) == 0:
            a =  'Cuckoo ' * abs(int(time[:2])-12)
            return a.strip()
        else:
            a =  'Cuckoo ' * int(time[:2])
            return a.strip()
    elif time[-2:] == '30':
        return 'Cuckoo'
    else:
        if int(time[-2:]) % 3  == 0 and int(time[-2:]) % 5 == 0:
            return "Fizz Buzz"
        elif int(time[-2:]) % 3  == 0:
            return "Fizz"
        elif int(time[-2:]) % 5  == 0:
            return "Buzz"
        else: return "tick"
        
        
        
