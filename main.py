# This is an exercise to reverse words in sentence.
# "Hello World" -> "Word Hello"
from Sentence import Sentence


# use the built in split() method to convert String to List
def string_to_list(string):
    listRes = list(string.split(" "))
    return listRes


original = "Millie Bobby Brown Hello Word New Part"
new_list = string_to_list(original)
new_list = new_list[::-1]


# convert List to String join() method
def list_to_string(add_list):
    str1 = " "
    return str1.join(add_list)


convertedStr = list_to_string(new_list)
print("Reversed String:\n\t", convertedStr, "\n")

# this is the original idea
sentence = "Hello World New Part"
sentence2 = "This Is A Good Day"
test_sentence = sentence
new_sentence = ""

print("This is the Original String: ", sentence)
first_variable = Sentence(sentence, test_sentence, new_sentence)
Sentence.cut(first_variable, test_sentence, new_sentence)
