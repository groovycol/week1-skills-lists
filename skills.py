"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def print_list(my_list):
    """Print each item in the input list

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9

    """

    #iterate through the passed in variable "my_list" and print each item
    for item in my_list:
        print item


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    #create an empty list to store odd numbers
    odd_list = []

    #iterate through the number_list passed in to this function
    for number in number_list:
        #use modulo to find the remainder when a number is / 2
        remainder = number % 2

        #if the remainder is anything but 0, the number is odd
        #only even numbers return a remander of 0 with %
        if remainder != 0:
            #append odd numbers to the odd_list list
            odd_list.append(number)
    #return a list of only the odd numbers from the original list
    return odd_list


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    #create an empty list to store even numbers
    even_list = []

    #iterate through the number_list passed in to this function
    for number in number_list:
        #use modulo to find the remainder when a number is / 2
        remainder = number % 2

        #if the remainder is zero, the number is even.
        if remainder == 0:
            #append even numbers to the even_list list
            even_list.append(number)
    #return a list of only the even numbers from the original list
    return even_list


def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']

    """
    #dcreate a new list and bind to it every second value from the input list
    new_list = my_list[::2]
    return new_list


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    #iterate through the list passed in and print the index number
    #using the .index method and the list item itself
    for item in my_list:
        print '{} {}'.format(my_list.index(item), item)



def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """

    #create an empty list to store long words
    greater_than_4char_words = []

    #iterate through the word_list passed in to this function
    for word in word_list:
        #use len() to determine the number of chars
        length = len(word)

        #if the word is > 4 characters, append word to the new list
        if length > 4:
            #append even numbers to the even_list list
            greater_than_4char_words.append(word)
    #return the list of words greater than 4 chars
    return greater_than_4char_words

def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']
    """

    #create an empty list to store long words
    variable_long_words = []

    #iterate through the word_list passed in to this function
    for word in word_list:
        #use len() to determine the number of chars
        length = len(word)

        #if the word is > n characters, append word to the new list
        if length > n:
            #append even numbers to the even_list list
            variable_long_words.append(word)
    #return the list of words greater than 4 chars
    return variable_long_words


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """

    #set the smallest_num to None, it'll be reset when needed
    smallest_num = None

    #check to see if we received an empty set, return None if so
    if number_list == []:
        return None

    #iterate through the items in number_list.
    for number in number_list:
        #handle the first time thorugh the loop, and set smallest_num to the current working number
        #then continue
        if smallest_num == None:
            smallest_num = number
            continue

        #if the current number is lower than the stored smallest_num, reset smallest_num to the current number
        #set the smallest_num to the current num
        if smallest_num > number:
            smallest_num = number

    #after we have completed iterating through the numbers
    #return the stored smallest_num
    return smallest_num


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    #set the largest_num to None, it'll be reset when needed
    largest_num = None

    #check to see if we received an empty set, return None if so
    if number_list == []:
        return None

    #iterate through the items in number_list.
    for number in number_list:
        #handle the first time thorugh the loop, and set largest_num to the current working number
        #then continue
        if largest_num == None:
            largest_num = number
            continue

        #if the current number is higher than the stored largest_num, reset largest_num to the current number
        #set the smallest_num to the current num
        if largest_num < number:
            largest_num = number

    #after we have completed iterating through the numbers
    #return the stored smallest_num
    return largest_num


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    #create an empty list to store halved values in
    new_halved_list = []

    #iterate through the number_list and append the value of the float of each number divided by two to the new list.
    for number in number_list:
        new_halved_list.append(float(number) / 2.0)

    #return the new list
    return new_halved_list



def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    #create an empty list to store the values of the lengths of words from the passed in word_list
    lengths = []

    #iterate through the word_list and append the length of each word to the new list
    for word in word_list:
        lengths.append(len(word))

    #return the new list
    return lengths


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    sum_of_nums = 0

    #check to see if we received an empty set, return None if so
    if number_list == []:
        return sum_of_nums

    #iterate through the number_list passed in and add each number to the sum total
    for number in number_list:
        sum_of_nums +=number

    #return the sum_of_nums
    return sum_of_nums


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    #set an initial value of the product to 1
    #this will ensure that if the list is empty, we'll return 1
    #if the list contains only one element, it will be multiplied by one, and the return will
    #be the value of the single item in the list
    product = 1

    #iterate through the list and multiply each item by the current, cumulative value of product
    for number in number_list:
        product *= number
    
    #return the value of product
    return product


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    #create a variable to store concatenated strings
    new_string = ""

    #iterate through the passed in word_list and add each word to new_string
    for word in word_list:
        new_string += word

    #return the new string
    return new_string



def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    #find the length of the list
    list_length = len(number_list)

    #define a starting sum variable
    total_sum = 0

    #iterate through the numbers in number_list and add each number to the sum
    for num in number_list:
        total_sum += num

    #Find the average by dividing the float of the total sum by the float of the length of the list
    average = float(total_sum) / float(list_length)

    #return the average
    return average


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """
    #create a variable to store concatenated strings
    string_with_commas = ""

    #This was my first try, but it had issues: trying to access the index
    #just flat-out didn't work. In addition, the logic was wrong as it would 
    #never put a comma between the first and second elements.
    #iterate through the list of words, and add words to our string.
    #for the first and last words do not add a ", "
    #for word in list_of_words:
    #     if enumerate(list_of_words) == 0 or enumerate(list_of_words) == -1:
    #         string_with_commas += word
    #     else:
    #         string_with_commas = string_with_commas + word + ", "

    # #return the string with the words joined with comma separation.
    # return string_with_commas

    #second try, read more on enumerate, and looked at several examples online
    for index, word in enumerate(list_of_words):
        
        #identify the last_item's index
        last_item = len(list_of_words) - 1
        #for the first and last elements, just add the word to the string
        if index == 0 or index == last_item:
            string_with_commas += word
        #for the second element, add commas on both sides of the word string
        elif index == 1:
            string_with_commas = string_with_commas + ", " + word + ", "
        #in all other cases, add a comma and space to the end of the string
        else:
            string_with_commas = string_with_commas + word + ", "

    return string_with_commas
    


def foods_in_common(foods1, foods2):
    """Using ANY Python data structure presented in the last week, given 2 lists of foods, 
    return a set of items that are in common between the two. (Don't include any duplicates
    in the output collection.)
    
    For example:

    >>> foods_in_common(["cheese", "bagel", "cake"], ["hummus", "beets", "bagel", "lentils"])
    set(['bagel'])

    If there are no foods in common, return an empty set.

    >>> foods_in_common(["lamb", "chili", "cheese"], ["cake", "ice cream"])
    set([])

    """
    #turn the lists passed in into sets
    food_set1 = set(foods1)
    food_set2 = set(foods2)

    #return a set of the shared values in both sets by using the set operater & to find the intersection
    return food_set1 & food_set2


def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python methed reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """
    #create a new list using the slicing notation with a step of -1 to work backwards
    new_list = my_list[::-1]
    #return the list
    return new_list


def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions 
       in the same list.

       Do not use the python methed reverse()/reversed()

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']


    """
    #return the list, reordered using the notation from the beginning(empty):to the end(empty):step by one, backwards (-1)
    return my_list[::-1]


def duplicates(my_list):
    """Return a list of words which are duplicated in the input list.

    Return a list of words which are duplicated in the input list. The returned list should be in ascending order. 
    >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
    ['apple', 'banana']

    >>> duplicates([1, 2, 2, 4, 4, 4, 7])
    [2, 4]
    

    """
    #create a new list to store duplicate values
    new_list = []

    #iterate through a sorted version of my_list.  
    for word in sorted(my_list):
        #If the word has already been added to the new_list, skip it.
        if word in new_list:
            continue
        #If the word appears more than once, append it to the new_list
        if my_list.count(word) > 1:
            new_list.append(word)

    #return the newly created list, which should contain a sorted list of items that appear more than one time in the original list.
    return new_list



def find_letter_indices(list_of_words, letter):
    """Given a list of words and a letter, return a list of integers that correspond
    to the index of the first occurance of the letter in that word.

    Do not use the .index() list method.

    >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
    [0, 1, 2]

    If the letter doesn't occur in one of the words, use None for that word in
    the output list. For example:

    >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
    [0, 1, 2, None]

    """
    new_list = []
    match = False

    #iterate through the list_of_words:
    for word in list_of_words:
        #and then iterate through the word itself, char by char, keeping track of the index
        for index, character in enumerate(word):
            #if the character matches the letter passed in, append the index of that char to the new_list
            if character == letter:
                new_list.append(index)
                match = True
                #the first time we match a letter in this word, break out of the loop
                break
            #now, check if we set the value of match to True, and reset to false, then continue
        if match == True:
            match = False
            continue
        #otherwise, add None to the new_list
        else:
            new_list.append(None)

    #return the new list
    return new_list

def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a 
    list of the largest n numbers in the input list in ascending order. 

    You can assume that n will be less than the length of the list. 

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """
    #sort the list in ascending order
    sorted_list = sorted(input_list)
    #use list slicing to make a list of the last n items.
    largest_n_nums = sorted_list[-n:]
    
    #return the new list 
    return largest_n_nums
    
   

##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
