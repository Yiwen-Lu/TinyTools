import numpy as np
import argparse


dict_hepburn={
    1: "a", 2: "i", 3: "u", 4: "e", 5: "o",
    6: "ka", 7: "ki", 8: "ku", 9: "ke", 10: "ko",
    11: "sa", 12: "shi", 13: "su", 14: "se", 15: "so",
    16: "ta", 17: "chi", 18: "tsu", 19: "te", 20: "to",
    21: "na", 22: "ni", 23: "nu", 24: "ne", 25: "no",
    26: "ha", 27: "hi", 28: "fu", 29: "he", 30: "ho"
    }

dict_hiragana={
    "a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
    "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
    "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
    "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と",
    "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
    "ha": "は", "hi": "ひ", "fu": "ふ", "he": "へ", "ho": "ほ"
    }

dict_katakana={
    "a": "ア", "i": "イ", "u": "ウ", "e": "エ", "o": "オ",
    "ka": "カ", "ki": "キ", "ku": "ク", "ke": "ケ", "ko": "コ",
    "sa": "サ", "shi": "シ", "su": "ス", "se": "セ", "so": "ソ",
    "ta": "タ", "chi": "チ", "tsu": "ツ", "te": "テ", "to": "ト",
    "na": "ナ", "ni": "ニ", "nu": "ヌ", "ne": "ネ", "no": "ノ",
    "ha": "ハ", "hi": "ヒ", "fu": "フ", "he": "ヘ", "ho": "ホ"
    }


def gen_rdarr(x):
    return np.random.permutation(x)

def play(qn, ans):
    print("Q:", qn)
    input()
    print("A:", ans)

def main(mode1, mode2):
    if mode2 == True:
        dict_q = dict_hiragana
        print("Start Practising Hiragana...\nPress 'Enter' to continue, Type 'exit' to quit.")
    else:
        dict_q = dict_katakana
        print("Start Practising Katakana...\nPress 'Enter' to continue, Type 'exit' to quit.")

    count = len(dict_q)
    idx_arr = gen_rdarr(count)
    # print(idx_arr)

    while True:
        choice = input("> ")

        if choice != 'exit':
            idx = idx_arr[count - 1] + 1
            print("count:", count)
            if count <= 1:
                # re-generate new indices
                count = len(dict_q)
                idx_arr = gen_rdarr(count)
            else:
                count -= 1
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
        help='given kana to practise hepburn, vice versa')
    parser.add_argument('--mode2', default='True',
        help='True: practise hiragana; False: practise katakana')
    args = parser.parse_args()
    main(False, False)
