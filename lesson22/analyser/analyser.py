# import analyser.text_handler.TextHandler as TextHandler
from analyser import TextHandler
from analyser import DictHandler
from analyser import WordContainer


def main():
    # hand = TextHandler()
    from time import time
    start = time()
    dictionary_uk = DictHandler(".\\analyser\\ukenglish_utf8.txt")
    dictionary_big = DictHandler(".\\analyser\\english3.txt")
    counter_uk = 0
    counter_big = 0
    source_file_name = ".\\analyser\\shakespeare.txt"
    missed_words_path = ".\\analyser\\missed_1.txt"
    with TextHandler(source_file_name) as handler, WordContainer(missed_words_path) as word_con:  #, :
        for word in handler:
            if word not in dictionary_uk:
                counter_uk += 1
                # if counter_uk < 200 and word.isalpha(): #  
                #     print(word)
                # missed_word.add(word)
            if word not in dictionary_big:
                counter_big += 1
                if word.isalpha(): word_con.add(word)
    print(f"{counter_uk=}")
    print(f"{counter_big=}")
    print(f"process time: {time() - start}")


if __name__ == '__main__':
    main()