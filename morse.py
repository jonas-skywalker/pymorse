#!/usr/bin/env python
import numpy
import soundfile

morse = { "A" : ".−", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....",
         "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.",
         "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-",
         "Y" : "-.--", "Z" : "--.." }


def find_element(dict, val):
    for key in dict.keys():
        if dict[key] == val:
            return key


def to_normal(code):
    translated = ""
    for word in code:
        for letter in word:
            translated += find_element(morse, letter)
        translated += " "
    return translated


def to_morse(normal):
    translated = ""
    for word in normal:
        for letter in word:
            translated += morse[letter]
            translated += " "
        translated += " / "
    return translated[:-4]


def case_morse():
    user_morse = input("Translate this: ")
    user_morse_split = user_morse.split("/")
    word_set = []
    for element in user_morse_split:
        word_set.append(element.split(" "))

    for i in range(len(word_set)):
        try:
            word_set[i].remove(" ")
        except ValueError:
            pass
        word_set[i] = list(filter(None, word_set[i]))

    print(to_normal(word_set))


def case_ascii():
    user_ascii = input("Translate this: ").upper()
    user_ascii_split = user_ascii.split(" ")
    word_set = []
    for element in user_ascii_split:
        word_set.append(list(element))

    print(to_morse(word_set))


def main():
    while True:
        case = input("Select your Input type [Ascii/Morse]: ")
        if case == "Ascii" or case == "ascii":
            case_ascii()
        elif case == "Morse" or case == "morse":
            case_morse()
        else:
            print("Wrong input!")


if __name__ == '__main__':
    main()
