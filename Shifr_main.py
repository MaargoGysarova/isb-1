import random

def get_word_in_text(text):
    word_list = list(set(text))
    print(word_list)
    return word_list


def alpha(n):
    mlist = []
    rand = [i for i in range(97, 97 + n)]
    random.shuffle(rand)
    for i in rand:
        mlist.append(chr(i))
    print(mlist)
    return mlist


def write_file(text, key):
    with open('shifr.txt', "w+") as f:
        f.write(text)
        f.write('\nКлюч:\n')
        for key, value in key.items():
            f.write('%s:%s\n' % (key, value))


def shifr(text):
    key = {}
    count_word = len(get_word_in_text(text))
    change_words = alpha(count_word)
    print(f'rfrf{change_words}')
    print(get_word_in_text(text))
    print(f'буквы,которые заменят {change_words}')
    print(f'буквы исходного текста {get_word_in_text(text)}')
    j = 0
    for i in (get_word_in_text(text)):
        print(i)
        change_word = change_words[j]
        key[change_word] = i
        text = text.replace(i, change_word)
        j = j + 1
    print(f'зашифрованный текст:\n{text}')
    print(f'ключ:\n{key}')
    write_file(text, key)

shifr('ученица ибаса представляет Вам свою лабораторную работу по ОИБ')
