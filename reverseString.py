# Given an input string, reverse the string word by word. 
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces 
# and the words are always separated by a single space.
# For example, Given s = "the sky is blue", return "blue is sky the".

# Exercise discovered on www.programcreek.com


testSentence = "The sky is blue"

def reverseString(sentence):
    
    newSentence = ""
    
    for word in range(len(sentence.split())):
        newSentence += sentence.split()[len(sentence.split()) - word - 1]
        newSentence += " "

    return newSentence

print reverseString(testSentence)
