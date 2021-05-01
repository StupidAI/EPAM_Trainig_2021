"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import unicodedata
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    def score_calc(elem: str) -> int:
        elem_len = len(elem)
        elem_unique_symbols = set(list(elem))
        elem_unique_symbols_len = len(elem_unique_symbols)
        elem_score = elem_unique_symbols_len * 1000 + elem_len
        return elem_score

    buffer = ""
    result = []
    with open(file_path, "r", encoding="unicode-escape", errors="ignore") as f:
        for line in f:
            line_arr = line.strip().split()
            # Обработка читаемых строк, удаления символов переноса и знаков препинания в начале и конце слова
            if buffer and line_arr:
                line_arr[0] = buffer[:-1] + line_arr[0]
                buffer = ""
            if line_arr and line_arr[-1].endswith("-"):
                buffer = line_arr.pop()
            for index, word in enumerate(line_arr):
                while unicodedata.category(word[0])[0] in ["P", "S"] and len(word) != 1:
                    word = word[1:]
                    line_arr[index] = word
                while (
                    unicodedata.category(word[-1])[0] in ["P", "S"] and len(word) != 1
                ):
                    word = word[:-1]
                    line_arr[index] = word
            # Выбор 10 уникальных слов
            line_set = set(line_arr)
            for el in line_set:
                result.append(el)
                result = sorted(result, key=score_calc, reverse=True)
                result = result[:10]
    return result


def get_rarest_char(file_path: str) -> str:
    char_dict = dict()
    rar_char_list = []
    min_count = 0
    with open(file_path, "r", encoding="unicode-escape", errors="ignore") as f:
        for char in f.read():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        while not rar_char_list:
            min_count += 1
            rar_char_list = [k for k, v in char_dict.items() if v == min_count]
    return "".join(rar_char_list)


def count_punctuation_chars(file_path: str) -> int:
    count = 0
    with open(file_path, "r", encoding="unicode-escape", errors="ignore") as f:
        for char in f.read():
            if unicodedata.category(char)[0] == "P":
                count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    count = 0
    with open(file_path, "r", encoding="unicode-escape", errors="ignore") as f:
        for char in f.read():
            if not char.isascii():
                count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    char_dict = dict()
    result = ""
    max_count = 0
    with open(file_path, "r", encoding="unicode-escape", errors="ignore") as f:
        for char in f.read():
            if char.isascii():
                continue  # использовал что бы уменьшить вложенность циклов
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
                if max_count < char_dict[char]:  # определим самый частый символ
                    result = char
                    max_count = char_dict[char]
    return result


print(get_longest_diverse_words("data.txt"))
