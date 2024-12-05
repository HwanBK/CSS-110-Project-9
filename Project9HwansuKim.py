# CSC110
# Project 9 - Gettysburg Word Analysis
# Hwansu Kim (Billy)
# 12/03/2021
# Reads a file then generates a file containing the words, sorted in ascending order, and outputs
# numerical statistics of the file.


# Reads the designated file and returns a set.
def readFile(fileName):
    addressFile = open(fileName, "r")

    addressList = addressFile.readlines()
    wordList = addressList[0].split(" ")
    wordSet = set(wordList)

    addressFile.close()

    return wordSet


# Returns the longest word and the length of that word found in a set.
def findLongest(wordSet):
    longestWord = ""
    lengthOfWord = 0

    for word in wordSet:
        if len(word) > lengthOfWord:
            longestWord = word
            lengthOfWord = len(word)

    return longestWord, lengthOfWord


# Returns a sorted list from a set.
def generateSortedList(wordSet):
    wordList = list(wordSet)
    for passIndex in range(len(wordList) - 1):
        smallestIndex = passIndex

        for checkIndex in range(passIndex + 1, len(wordList)):
            if wordList[checkIndex] < wordList[smallestIndex]:
                smallestIndex = checkIndex

        temp = wordList[passIndex]
        wordList[passIndex] = wordList[smallestIndex]
        wordList[smallestIndex] = temp

    return wordList


# Creates or overwrites a file containing the sorted list of words.
def writeWordFile(fileName, wordList):
    wordFile = open(fileName, "w")

    for eachWord in wordList:
        wordFile.write(eachWord + "\n")

    wordFile.close()


# Returns a list of counts based on word length.
def generateLenFreqs(wordSet, lengthOfWord):
    wordFreqList = [0] * lengthOfWord
    for indexCount in range(0, lengthOfWord):

        for word in wordSet:
            if len(word) == (indexCount + 1):
                wordFreqList[indexCount] += 1

    return wordFreqList


def main():
    setOfWords = readFile("GettysburgAddress.txt")
    lengthiestWord, wordLength = findLongest(setOfWords)
    listOfWords = generateSortedList(setOfWords)

    writeWordFile("GettysburgWords.txt", listOfWords)
    frequencyList = generateLenFreqs(setOfWords, wordLength)

    print("Number of distinct words:", len(setOfWords))
    print("Length of longest word:", wordLength)
    print("Longest word:", lengthiestWord, "\n")

    for indexCount in range(len(frequencyList)):
        print("Length =", format(indexCount + 1, "4"), ", Count =",
              format(frequencyList[indexCount], "4"))


if __name__ == "__main__":
    main()


# SUMMARY
#    I approached this project by splitting up and working on the project one function definition
# at a time; Initially, I had all the function definitions stubbed, aside from the one being worked
# on, and after individual function tests, I would call them within the main function. Once I
# reached the generateSortedList function I hit my first wall because I couldn't remember the
# selection sort logic off the top of my head. Eventually, I went back to the pre-recorded lecture
# for selection sorting to review the logic and code to get unstuck.
#    For testing, I had tested in-program through individual function calls, when possible, and
# later I used PyUnit tests to double-check that outputs were correct. One thing that didn't work
# , at least initially, was testing for findLongest when there could have been multiple potential
# outputs; due to the random sorting of elements every time the set is generated. Although, I
# eventually got the tests to pass properly using tips provided in the discussion board.
#    The project was good practice for manipulating lists and using list elements and indexes
# to write loops; one thing I feel like I need more practice on is definitely selection sorting, as
# I feel like I still don't have a grasp on it yet. On future projects, whether personal or in
# future classes, I'll definitely take advantage of the design and analysis philosophy taught in
# this class and that I learned while working on projects; and I'll be looking to develop this skill
# indefinitely, as long as I continue to program.


# TEST CASES
# readFile Function
#    -File opens, closes, and is read properly.
#       -Tested via running the program and running the test script for multiple text documents.
#           -Properly returns a set of strings.
#       -Calling readFile() within a print statement displayed a set of the text document's
#        contents; with the elements separated at where a single whitespace used to be.
#    -Properly accepts text documents regardless of the file's name, as long as it exists and is
#     is the same directory. i.e. not hardcoded to only accept GettysburgAddress.txt.

# findLongest Function
#    -Tested via test script.
#    -If there are multiple words of the maximum length, the function will return the first of
#     those words that were encountered.
#       -When the program is ran, a new set is generated each time, randomizing the order.
#       -For GettysburgAddress.txt there were three possible outputs for the longest word.
#           -Battlefield, consecrated, and proposition. (Eleven characters).
#    -If a set only contains an empty string, it will return the empty string as the longest word
#     and a length of 0.

# generateSortedList Function
#    -Tested via test script.
#       -Properly sorts, in ascending order, based on ASCII code.
#           -Letters of the same casing are sorted in alphabetical order.
#               -Uppercase letters come before lowercase letters.
#       -Fails if anything other than a string is included.
#           -When tested with the test script, using a mix of integers and strings, the test failed.
#       -The length of the generated list is the same as the length of the longest word argument.
#           -If the length argument passed is 6, then the list will have a length of 6; indexes
#            0 through 5, inclusive.

# writeWordFile Function
#    -Tested via GettysburgAddress.txt/GettysburgWords.txt and the test script.
#       -Properly creates a new file, if one of the designated name doesn't exist, or overwrites if
#        the file already exists.
#       -Properly outputs the sorted list of words, from generateSortedList, in a text document
#        with one word per line.
#           -Files created by the test script will display the words, one per line, based on the
#            order of the list provided as an argument.

# generateLenFreqs Function
#    -Tested via running the program and with the test script.
#       -Number of distinct words counted by opening the file generated by writeWordFile in Python
#        and using the row count to see what number the final number was.
#           -GettysburgWords.txt returned a number of distinct words of 138 and opening the file
#            showed 138 rows of words + 1 empty row at the bottom for 139.
#               -The empty row at the bottom is from the newline from writeWordFile.
#       -Length of the longest word and the longest word are straight from findLongest and
#        displays the same output as the return from findLongest.
#       -When running the program the output correctly displays the maximum length, from
#        findLongest, as the highest length. Also displays all the length counts below the maximum.
#           -GettysburgAddress.txt results in lengths 1 through 11.
#       -Manually counted some of the lengths with a low count by checking the original text file.
#           -For example GettysburgAddress.txt returned that there was 1 word of length 1.

# main Function
#    -Properly calls functions that read, create , and or overwrite files.
#       -Verified by checking whether the file and its contents were generated.
#    -Output properly displays all the returns from function calls.
#       -Length and count list aligns properly, unless the original file contains over tens of
#        thousands of words.