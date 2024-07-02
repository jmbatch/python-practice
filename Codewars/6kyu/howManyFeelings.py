
#You have two arguments: string - a string of random letters(only lowercase) and array - an array of strings(feelings). Your task is to return how many specific feelings are in the array.
#
#For example:
#string -> 'yliausoenvjw'
#array -> ['anger', 'awe', 'joy', 'love', 'grief']
#output -> '3 feelings.' // 'awe', 'joy', 'love'
#
#string -> 'griefgriefgrief'
#array -> ['anger', 'awe', 'joy', 'love', 'grief']
#output -> '1 feeling.' // 'grief'

#string -> 'abcdkasdfvkadf'
#array -> ['desire', 'joy', 'shame', 'longing', 'fear']
#output -> '0 feelings.'

def count_feelings(st, arr):
    zero = 0
    empty_list = []
    if len(arr) <= 0:
        return '0 feelings.'
    else:
        for element in arr:
            elem_list = empty_list
            count = zero
            str_replace = st
            for char in element:
                str_index = str_replace.find(char)
                if str_index != -1:
                    str_replace =  str_replace.replace(char, '', 1)
                    count += 1
                if count == len(element):
                    elem_list.append(element)
        if len(elem_list) == 1:
            return (f'{len(elem_list)} feeling.')
        else:
            return (f'{len(elem_list)} feelings.')


count_feelings('longi', ['anger', 'awe', 'joy', 'longing', 'grief'])
count_feelings('yliausoenvjw', ['anger', 'awe', 'joy', 'love', 'grief'])
count_feelings('angerw', ['anger', 'awe', 'joy', 'love', 'grief'])
count_feelings('griefgriefgrief', ['anger', 'awe', 'joy', 'love', 'grief'])
count_feelings('abcdkasdfvkadf', ['desire', 'joy', 'shame', 'longing', 'fear'])

