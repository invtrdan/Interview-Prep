def sortSentence(s: str) -> str:
    words = s.split(" ")
    sorted_words = ["" for i in range(len(words))]

    for word in words:
        index = int(word[-1]) - 1
        word = word[:-1]
        sorted_words[index] = word
    print(sorted_words)

    result = ""
    i = 0
    for word in sorted_words:
        if i == len(sorted_words) - 1:
            result += word
        else:
            result += word + " "
        i += 1

    return result


s = "is2 sentence4 This1 a3"
print(sortSentence(s))
