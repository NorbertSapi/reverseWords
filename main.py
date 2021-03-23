# This is an exercise to reverse words in sentence.
# "Hello World" -> "Word Hello"

sentence = "Hello World New Part"
test_sentence = sentence


def cut(test):
    number = test.index(" ")
    test = test[(number+1):]
    return test


def proceed(test):
    number = test.index(" ")
    while number:
        # number = test.index(" ")
        if number == test.index(" "):
            word = test_sentence[0:number]
            return word


# 1st round
word1 = proceed(test_sentence)
# 2nd round
test_sentence = cut(test_sentence)
word2 = proceed(test_sentence)
# 3rd round
test_sentence = cut(test_sentence)
word3 = proceed(test_sentence)
# 4th round
test_sentence = cut(test_sentence)

print("Original:\n\t", sentence)
print("Test:\n\t", test_sentence, word3, word2, word1)
