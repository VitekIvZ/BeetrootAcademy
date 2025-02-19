
NUMBER_TO_WORD = {1: 'одна', 2: 'дві', 3: 'три', 4: 'чотири', 5: 'п\'ять', 
                  6: 'шість', 7: 'сім', 8: 'вісім', 9: 'дев\'ять', 
        10: 'десять', 11: 'одинадцять', 12: 'дванадцять', 13: 'тринадцять', 14: 'чотирнадцять', 
        15: 'п\'ятнадцять', 16: 'шістнадцять', 17: 'сімнадцять', 18: 'вісімнадцять', 19: 'дев\'ятнадцять', 
        20: 'двадцять', 30: 'тридцять', 40: 'сорок', 50: 'п\'ятдесят', 60: 'шістдесят', 
        70: 'сімдесят', 80: 'вісімдесят', 90: 'дев\'яносто',
        100: "сто", 200: "двісті", 300: "триста", 400: "чотириста", 500: "п'ятсот", 600: "шістсот",
        700: "сімсот", 800: "вісімсот", 900: "дев'ятсот"} 
#  1 345.45 => тисяч-а триста сорок п'ять грив-ень сорок п'ять копій-ок
#  2 343.42 => тисяч-і триста сорок три грив-ні сорок дві копій-ки
#  5 343.42 => тисяч триста сорок три грив-ні сорок дві копій-ки
#  345 341.41 => тисяча триста сорок одна грив-ня сорок одна копій-ка
#  1 311.42 => тисяча триста одинадцять грив-ень сорок дві копій-ки  


def add_curency(units, curensy_base, suffix=('ня', 'ні', 'ень')):
    result = curensy_base 
    if units == 1:
        result +=suffix[0]
    elif 2 <= units <= 4:
        result += suffix[1]
    else:
        result += suffix[2]
    return result


def convert_units(dec, units):  # , suffix=''
    # result = ""
    if units and (dec < 11 or dec > 19):
        result = NUMBER_TO_WORD[units] 
        return result


def convert_decades(dec, units):
    dec = (dec - units) if (dec < 10 or dec > 19) else dec
    if dec:
        return NUMBER_TO_WORD[dec]


def convert_hundredes(hund, dec):
    hund = hund - dec
    if hund:
        return NUMBER_TO_WORD[hund]

def convert_coins(coins):
    units = int(coins) % 10
    dec = int(coins) % 100
    result = ''
    
    dec_word = convert_decades(dec, units)
    if dec_word:
        result += dec_word + ' '
    unit_word = convert_units(dec, units)
    if unit_word:
        result += unit_word + ' '
    if dec_word or unit_word:
        result += add_curency(units, 'копій', suffix=('ка', 'ки', 'ок'))
    return result


def main(number):
    def append_word(words, sec, first, converter):
        word = converter(sec, first)
        if word:
            words.append(word)

    words = []

    coins = (number * 100) % 100

    units = int(number) % 10
    dec = int(number) % 100
    hund = int(number) % 1000

    words.append(convert_coins(coins))

    words.append(add_curency(units, 'грив', suffix=('ня', 'ні', 'ень')))

    append_word(words, dec, units, convert_units)
    append_word(words, dec, units, convert_decades)
    append_word(words, hund, dec, convert_hundredes)
    
    # unit_word = convert_units(dec, units)
    # if unit_word:
    #     words.append(unit_word)
    
    # dec_word = convert_decades(dec, units)
    # if dec_word: 
    #     words.append(dec_word)
    
    # hund_word = convert_hundredes(hund, dec)
    # if hund_word: 
    #     words.append(hund_word)

    th_units = int(number/1000) % 10 
    th_dec = int(number/1000) % 100
    th_hund = int(number/1000) % 1000

    if th_units or th_dec or th_hund:
        words.append(add_curency(th_units, 'тисяч', suffix=('а', 'і', '')))

    append_word(words, th_dec, th_units, convert_units)
    append_word(words, th_dec, th_units, convert_decades)
    append_word(words, th_hund, th_dec, convert_hundredes)
    
    # th_unit_word = convert_units(th_dec, th_units)
    # if th_unit_word:
    #     words.append(th_unit_word)
    
    # th_dec_word = convert_decades(th_dec, th_units)
    # if th_dec_word: 
    #     words.append(th_dec_word)
    
    # hund_word = convert_hundredes(th_hund, th_dec)
    # if hund_word: 
    #     words.append(hund_word)

    return ' '.join(words[::-1])


if __name__ == '__main__':
    print(456345.45, main(456345.45))
    print(673343.43, main(673343.43))
    print(801341.41, main(801341.41))
    print(1318.18, main(1318.18))
    print(1305.05, main(1305.05))
    print(1301.01, main(1301.01))
    print(1302, main(1302))
    print(1300, main(1300))
    print(301, main(301))

