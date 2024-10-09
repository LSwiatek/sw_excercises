import time


def shouldSkip(dictionary: set, word: str):
    # must be exectly 5 letters
    if len(word) != 5:
        return True
    # must have all unique letters
    if len(set(x for x in word)) != 5:
        return True
    # remove anagrams
    if word[::-1] in dictionary:
        return True



def loadFile(filename: str):
    words = set()
    with open(filename, "r") as fh:
        for line in fh:
            line = line.strip()
            if not shouldSkip(words, line):
                words.add(line)
    return words


def word_use_same_letter(word1: str, word2: str):
    return any(word2_letter in word1 for word2_letter in word2)

def word_has_repeated_letters(word: str):
    return len(set(l for l in word)) != len(word)

def no_repeated_letters(words: [str]):
    for w in words:
        if word_has_repeated_letters(w):
            return False
    if len(words) < 2:
        return True
    i=0
    j=1
    while j < len(words) and i < len(words):
        if word_use_same_letter(words[i], words[j]):
            return False

        if j + 1 == len(words):
            i+=1
            j=i+1
        else:
            j+=1

    return True

def no_repeated_letters2(words: [str]):
    pass
def find_words(words: [str], word_number: int):
    pointers = [0] * word_number

    while pointers[0] < len(words) - word_number + 1:
        pointers[len(pointers)] += 1
        if pointers[len(pointers)] >= len(words)


def find_words(words):
    results = set()
    i = 0
    for word1 in words:
        for word2 in words:
            for word3 in words:
                for word4 in words:
                    for word5 in words:
                        i += 1
                        if i > 1_000_000:
                            return
                        if no_repeated_letters([word1, word2, word3, word4, word5]):
                            results.add(frozenset([word1, word2, word3, word4, word5]))
                            # print(f"{word1} - {word2} - {word3} - {word4} - {word5}")
    return results

def main():
    #load file
    # words = loadFile("words_short.txt")
    words = loadFile("words.txt")
    print(len(words))
    start_time = time.time()
    # time.clock_gettime_ns()
    results = find_words(words)
    print("--- %s seconds ---" % (time.time() - start_time))

    print(results)




if __name__ == '__main__':
    main()
    # print(no_repeated_letters(["asd", "zxc", "qwery", "kwa"]))