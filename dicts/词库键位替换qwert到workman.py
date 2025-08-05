# 普通键盘的键位，到workman键位的a-z字母替换字典
qwerty_to_workman = {
    'q': 'q', 'w': 'd', 'e': 'r', 'r': 'w', 't': 'b', 'y': 'j', 'u': 'f',
    'i': 'u', 'o': 'p', 'p': 'i', 'a': 'a', 's': 's', 'd': 'h', 'f': 't',
    'g': 'g', 'h': 'y', 'j': 'n', 'k': 'e', 'l': 'o', ';': 'i', 'z': 'z',
    'x': 'x', 'c': 'm', 'v': 'c', 'b': 'v', 'n': 'k', 'm': 'l'
}

with open('wubi98_base.dict.yaml', 'r', encoding='utf-8') as file:
    strings = file.read()

sep = '...'
strings_split = strings.split(sep)
title = strings_split[0]
text = strings_split[1].strip()
text_split = text.split('\n')


def letters_sub(line):
    result = ''
    for letter in line:
        if letter in qwerty_to_workman:
            result += qwerty_to_workman[letter]
        else:
            result += letter
    return result


result_list = []
for elements in text_split:
    result_list.append(letters_sub(elements))

result_last = title + sep + '\n\n' + '\n'.join(result_list)

with open('wubi98_result.yaml', 'w', encoding='utf-8') as file:
    file.write(result_last)
