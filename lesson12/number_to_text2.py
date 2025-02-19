NUMBER_TO_WORD = {
    1: 'одна', 2: 'дві', 3: 'три', 4: 'чотири', 5: 'п\'ять',
    6: 'шість', 7: 'сім', 8: 'вісім', 9: 'дев\'ять',
    10: 'десять', 11: 'одинадцять', 12: 'дванадцять', 13: 'тринадцять', 14: 'чотирнадцять',
    15: 'п\'ятнадцять', 16: 'шістнадцять', 17: 'сімнадцять', 18: 'вісімнадцять', 19: 'дев\'ятнадцять',
    20: 'двадцять', 30: 'тридцять', 40: 'сорок', 50: 'п\'ятдесят', 60: 'шістдесят',
    70: 'сімдесят', 80: 'вісімдесят', 90: 'дев\'яносто',
    100: "сто", 200: "двісті", 300: "триста", 400: "чотириста", 500: "п'ятсот", 600: "шістсот",
    700: "сімсот", 800: "вісімсот", 900: "дев'ятсот"
}

def convert_units(units, currency_base=''):
    result = ""
    if units:
        result = NUMBER_TO_WORD[units]
    result += ' ' + currency_base
        
    if units == 1:
        result += 'ня'
    elif 2 <= units <= 4:
        result += 'ні'
    else:
        result += 'ень'
    return result

def convert_decades(dec):
    if dec in NUMBER_TO_WORD:
        return NUMBER_TO_WORD[dec]
    return ''

def convert_hundreds(hund):
    if hund in NUMBER_TO_WORD:
        return NUMBER_TO_WORD[hund]
    return ''

def main(number):
    word = []
    units = int(number) % 10
    word.append(convert_units(units, currency_base='грив'))
    
    dec = int(number) % 100
    dec = dec - units if 10 < dec < 20 else dec
    if convert_decades(dec):
        word.append(convert_decades(dec))
    
    hund = int(number) // 100 * 100
    if convert_hundreds(hund):
        word.append(convert_hundreds(hund))
    
    return ' '.join(word[::-1])

if __name__ == '__main__':
    print(1345, main(1345))
    print(1343, main(1343))
    print(1341, main(1341))
    print(1318, main(1318))
    print(1301, main(1301))
    print(1302, main(1302))
    print(1300, main(1300))
