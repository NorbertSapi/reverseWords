# This is an exercise to reverse words in sentence.
# "Hello World" -> "Word Hello"

sentence = "Hello World New Part"
sentence2 = "This Is A Good Day"
test_sentence = sentence
new_sentence = ""


# this is a method to return the String back words.
def cut(test, new):
    number = 0
    # it prints the new sentence
    print(new)
    # iterate throw the String
    while number <= len(test):
        number += 1
        global new_sentence
        # condition " ", helps to separate the words in String
        if number == test.index(" "):
            # return the substring of the Original String, to build the new String.
            new_sentence = test[0:number] + " " + new_sentence
            # substring of the tested sentence. Original String without the first word  of the String.
            test = test[(number + 1):]
            # start the sequence again, until no more word in the String.
            cut(test, new_sentence)
        elif number != test.index(" "):
            test = test + " " + new_sentence
    return test


print("Second test:\n\t")
word2 = cut(sentence2, new_sentence)
print(word2)
print("First test:\n\t")
word1 = cut(test_sentence, new_sentence)
print(word1, "\n")
