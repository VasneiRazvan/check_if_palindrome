# create a function to check if a range of 
# random characters can form a palindrome
def is_palindrome(string):
    # initialised an empty list
    empty_list = []
    # for each character in list, it is deleted if the list already contains it
    # if not, it adds it to the list
    for i in range(len(string)):
        if string[i] in empty_list:
            empty_list.remove(string[i])
        else:
            empty_list.append(string[i])
            # if the lenght of the list is even, the list is empty
            # or if the lenght of the list is odd, lenght of the list should be 1
    if len(string) % 2 == 0 and len(empty_list) == 0 or len(string) % 2 == 1 and len(empty_list) == 1:
        return True
    else:
        return False
palindrome_key = str(input('Please type random characters -> '))
if is_palindrome(palindrome_key):
    print('Yes, this is a palindrome')
else:
    print('No, this is not a palindrome')