from tqdm import tqdm
import time

def should_skip(dictionary: [str], word: str):
    if len(word) != 5:
        return True
    if len(set(word)) != 5:
        return True
    if word[::-1] in dictionary:
        return True



def load_file(filename: str):
    words=[]
    with open(filename, "r") as fh:
        for line in fh:
            line = line.strip()

            if should_skip(words, line):
                continue

            words.append(line)
    return words

def word_has_repeated_letters(word: str):
    return len(set(word)) != len(word)

def word_use_same_letter(word1: str, word2: str):
    return len(set(word1).intersection(set(word2))) == 0

def word_use_same_letter(word1: str, word2: str):
    return any(word2_letter in word1 for word2_letter in word2)

def no_repeated_letters(words: [str]):
    for word in words:
        if word_has_repeated_letters(word):
            return False

    if len(words) < 2:
        return True

    i=0
    j=1
    while j < len(words) and i < len(words):
        if word_use_same_letter(words[i], words[j]):
            return False

        j += 1
        if j >= len(words):
            i+=1
            j=i+1

    return True


def main():
    words = load_file("words.txt")

    print(len(words))

    # i, j = 0, 1

    # while i < len(words) and j < len(words):
    #
    #     word1 = words[i]
    #     word2 = words[j]
    #
    #     if word_use_same_letter(word1, word2):
    #         print(f"{word1} - {word2}")
    #
    #     j += 1
    #     if j >= len(words):
    #         i += 1
    #         j = i + 1


    #
    start_time = time.time()
    results = find_words(words)
    print("--- %s seconds ---" % (time.time() - start_time))


    print(results)


def find_words(words):
    results = set()
    i=0
    for word1 in tqdm(words):
        for word2 in words:
            for word3 in words:
                for word4 in words:
                    for word5 in words:
                        i+=1
                        if i >= 1_000_000:
                            return results
                        if no_repeated_letters([word1, word2, word3, word4, word5]):
                            results.add(frozenset([word1, word2, word3, word4, word5]))
                            # print(f"{word1} - {word2} - {word3}")
    return results


# 5 slow
# piecio literowe
# z pliku
# zadna litera nie moze sie powtazac

if __name__ == '__main__':
    main()
