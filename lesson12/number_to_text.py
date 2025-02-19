
NUMBER_TO_WORD = {1: 'одна', 2: 'дві', 3: 'три', 4: 'чотири', 5: 'п\'ять',
                  6: 'шість', 7: 'сім', 8: 'вісім', 9: 'дев\'ять',
        10: 'десять', 11: 'одинадцять', 12: 'дванадцять', 13: 'тринадцять', 14: 'чотирнадцять',
        15: 'п\'ятнадцять', 16: 'шістнадцять', 17: 'сімнадцять', 18: 'вісімнадцять', 19: 'дев\'ятнадцять',
        20: 'двадцять', 30: 'тридцять', 40: 'сорок', 50: 'п\'ятдесят', 60: 'шістдесят',
        70: 'сімдесят', 80: 'вісімдесят', 90: 'дев\'яносто',
        100: "сто", 200: "двісті", 300: "триста", 400: "чотириста", 500: "п'ятсот", 600: "шістсот",
        700: "сімсот", 800: "вісімсот", 900: "дев'ятсот"}
#  1 345.45 => тисяча триста сорок п'ять грив-ень сорок п'ять копій-ок
#  1 343.42 => тисяча триста сорок три грив-ні сорок дві копій-ки
#  345 341.41 => тисяча триста сорок одна грив-ня сорок одна копій-ка
#  1 311.42 => тисяча триста одинадцять грив-ень сорок дві копій-ки  

def convert_units(units, curensy_base=''):  # , suffix=''
    result = ""
    if units:
        result = NUMBER_TO_WORD[units]
        result += ' ' + curensy_base
       
        if units == 1:
            result +='ня'
        elif 2 <= units <= 4:
            result +='ні'
        else:
            result +='ень'

    return result


def convert_decades(dec):
    if dec:
        return NUMBER_TO_WORD[dec]


# def convert_hundredes(hund):
#     return NUMBER_TO_WORD[hund]


def main(number):
    word = []
    units = int(number) % 10
    word.append(convert_units(units, curensy_base='грив'))
    dec = int(number) % 100
    dec = dec - units if 10 < dec and dec > 19 else dec
    print(dec)
    if convert_decades(dec):
        word.append(convert_decades(dec))
    hund = int(number) % 1000 - int(number) % 100
    word.append(NUMBER_TO_WORD[hund])
    return ' '.join(word[::-1])


if __name__ == '__main__':
    print(1345, main(1345))
    print(1343, main(1343))
    print(1341, main(1341))
    print(1318, main(1318))
    print(1301, main(1301))
    print(1301, main(1301))
    print(1302, main(1302))
    print(1300, main(1300))
