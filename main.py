def main():
    filename = "books/frankenstein.txt"
    text = getBookText(filename)
    words = getBookWords(text)
    wordQuantity = getWordsQuantity(words)
    charMap = getCharMap(text)
    sortedLetters = sortLettersToReport(charMap)
    generateBookReport(sortedLetters, wordQuantity, filename)
    
def getBookText(filename):
    with open(filename) as f:
        text = f.read()
    return text

def getBookWords(text):
    words = text.split()
    return words

def getWordsQuantity(words):
    return len(words)

def getCharMap(text):
    charMap = {}
    for chars in text:
        charsLowered = chars.lower()
        if charsLowered in charMap:
            charMap[charsLowered] += 1
        else:
            charMap[charsLowered] = 1
    return charMap

def sortKey(d):
    return d["num"]

def sortLettersToReport(charMap):
    letterList = []
    for ch in charMap:
        if ch.isalpha():
            letterList.append({"char": ch, "num": charMap[ch]})
    letterList.sort(reverse=True, key=sortKey)
    return(letterList)

def generateBookReport(letterQuantity, wordQuantity, filename):
    print(f"--- Begin report of {filename} ---")
    print(f"{wordQuantity} words were found in the document \n")

    for letter in letterQuantity:
        print(f"The '{letter['char']}' character was found {letter['num']} times")
main()
