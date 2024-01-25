# class Anagram:
#     def __init__(self, aword=""):
#         self.aword = sorted(aword)

#     def match(self, word_list):
#         return [word for word in word_list if sorted(word) == self.aword]

# listen = Anagram("enlist")
# print(listen.match(['listen','silent', 'hipopotamus']))


# second solution

# class Anagram:
#     def __init__(self, aword=""):
#         self.current_word = sorted(aword)

#     def match(self, word_list):
#         result = []
#         for word in word_list:
#             if sorted(word) == self.current_word:
#                 result.append(word)
#         return result

# listen = Anagram("enlist")
# print(listen.match(['hello', 'hipopotamus']))

# Third solution: this code was trying to follow the instruction from the content and ended up reinventing the whell
# Yet sorted() works on string also not only on list

# class Anagram:
#     def __init__(self, aword=""):
#         global current_word
#         self.aword = aword
#         list_a_word = [letter for letter in aword]
#         current_word = list_a_word
#         # print(list_a_word) 

    

#     def match(self, word_list):

#         list_new = []

        
#         list_new.append(n for n in word_list)
        
        
#         # the new created list is not a real list extract element from it an create a realist named list
#         for list in list_new:
#             list = [n for n in list]

#             # print(list)

#             # try to extract the letter in each list element of list_new
#             for anyword in list:
#                 anyword = [letter for letter in anyword if sorted (anyword) == sorted(current_word)]
#                 # print(anyword)
#                 print(''.join(anyword))
            
#             #for each anyword compare it with word to see their intersection
#                 # if sorted(anyword) == sorted(current_word):
#                 #     # print(anyword)
#                 #     print(''.join(anyword))
#                 # else:
#                 #     print([])
                


#         return list
        
# listen = Anagram("enlist")
# listen.match(['hello', 'hipopotanus'])