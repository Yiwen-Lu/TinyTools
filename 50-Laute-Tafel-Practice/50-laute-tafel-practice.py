import numpy as np
import argparse


dict_hepburn={
    1: "a", 2: "i", 3: "u", 4: "e", 5: "o",
    6: "ka", 7: "ki", 8: "ku", 9: "ke", 10: "ko",
    11: "sa", 12: "shi", 13: "su", 14: "se", 15: "so"
    }

dict_hiragana={
    "a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
    "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
    "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ"
    }

dict_katakana={
    "a": "ア", "i": "イ", "u": "ウ", "e": "エ", "o": "オ",
    "ka": "カ", "ki": "キ", "ku": "ク", "ke": "ケ", "ko": "コ",
    "sa": "サ", "shi": "シ", "su": "ス", "se": "セ", "so": "ソ"
    }


def gen_num(low = 1, high = 15, size = 1):
    return np.random.randint(low = 1, high = 15, size = 1)

def play(qn, ans):
    print("Q:", qn)
    input()
    print("A:", ans)

def main(mode1, mode2):
    if mode2 == True:
        dict_q = dict_hiragana
        print("Start Practising Hiragana...")
    else:
        dict_q = dict_katakana
        print("Start Practising Katakana...")

    while True:
        choice = input("> ")

        if choice != 'exit':
            np.random.seed(np.random.choice(1234567, 1)[0])
            idx = np.random.randint(low = 1, high = 15, size = 1)[0]
            qn = dict_hepburn[idx]
            ans = dict_q[qn]
            if mode1 == True:
                play(qn, ans)
            else:
                play(ans, qn)

        else:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='50-Laute-Tafel Übung')
    parser.add_argument('--mode1', default='True',
        help='given kana practise hepburn')
    parser.add_argument('--mode2', default='True',
        help='True: practice hiragana; False: practise katakana')
    args = parser.parse_args()
    main(False, False)
