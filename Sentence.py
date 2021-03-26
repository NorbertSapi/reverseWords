# this is a class for the sentences

class Sentence:
    pass

    def __init__(self, sentence, test_sentence, new_sentence):
        self.sentence = sentence
        self.test_sentence = test_sentence
        self.new_sentence = new_sentence

    def cut(self, test, new):
        number = 0
        # it prints the new sentence
        print(new)
        # iterate throw the String
        while number <= len(test):
            number += 1
            # condition " ", helps to separate the words in String
            if number == test.index(" "):
                # return the substring of the Original String, to build the new String.
                self.new_sentence = test[0:number] + " " + self.new_sentence
                # substring of the tested sentence. Original String without the first word  of the String.
                test = test[(number + 1):]
                # start the sequence again, until no more word in the String.
                Sentence.cut(self, test, self.new_sentence)
            elif number != test.index(" "):
                test = test + " " + self.new_sentence
        return test
