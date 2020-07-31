import numpy as np
import argparse


dict_hepburn={
    1: "a", 2: "i", 3: "u", 4: "e", 5: "o",
    6: "ka", 7: "ki", 8: "ku", 9: "ke", 10: "ko",
    11: "sa", 12: "shi", 13: "su", 14: "se", 15: "so",
    16: "ta", 17: "chi", 18: "tsu", 19: "te", 20: "to",
    21: "na", 22: "ni", 23: "nu", 24: "ne", 25: "no",
    26: "ha", 27: "hi", 28: "fu", 29: "he", 30: "ho",
    31: "ma", 32: "mi", 33: "mu", 34: "me", 35: "mo",
    36: "ya", 37: "i", 38: "yu", 39: "e", 40: "yo",
    41: "ra", 42: "ri", 43: "ru", 44: "re", 45: "ro",
    46: "wa", 47: "i", 48: "u", 49: "e", 50: "(w)o",
    51: "n"
    }

dict_hiragana={
    "a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
    "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
    "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
    "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と",
    "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
    "ha": "は", "hi": "ひ", "fu": "ふ", "he": "へ", "ho": "ほ",
    "ma": "ま", "mi": "み", "mu": "む", "me": "め", "mo": "も",
    "ya": "や", "yu": "ゆ", "yo": "よ",
    "ra": "ら", "ri": "り", "ru": "る", "re": "れ", "ro": "ろ",
    "wa": "わ", "(w)o": "を",
    "n": "ん"
    }

dict_katakana={
    "a": "ア", "i": "イ", "u": "ウ", "e": "エ", "o": "オ",
    "ka": "カ", "ki": "キ", "ku": "ク", "ke": "ケ", "ko": "コ",
    "sa": "サ", "shi": "シ", "su": "ス", "se": "セ", "so": "ソ",
    "ta": "タ", "chi": "チ", "tsu": "ツ", "te": "テ", "to": "ト",
    "na": "ナ", "ni": "ニ", "nu": "ヌ", "ne": "ネ", "no": "ノ",
    "ha": "ハ", "hi": "ヒ", "fu": "フ", "he": "ヘ", "ho": "ホ",
    "ma": "マ", "mi": "ミ", "mu": "ム", "me": "メ", "mo": "モ",
    "ya": "ヤ", "yu": "ユ", "yo": "ヨ",
    "ra": "ラ", "ri": "リ", "ru": "ル", "re": "レ", "ro": "ロ",
    "wa": "ワ", "(w)o": "ヲ",
    "n": "ン"
    }


def gen_rdarr(x):
    return np.random.permutation(x)

def gen_idx_arr(x):
    count = len(x)
    idx_arr = gen_rdarr(count)
    return count, idx_arr

def play(qn, ans):
    print("Q:", qn)
    input()
    print("A:", ans)

def main(args):
    if args.mode2 == "hiragana":
        dict_q = dict_hiragana
        print("Start Practising Hiragana...\nPress 'Enter' to continue, Type 'exit' to quit.")
    else:
        dict_q = dict_katakana
        print("Start Practising Katakana...\nPress 'Enter' to continue, Type 'exit' to quit.")

    count, idx_arr = gen_idx_arr(dict_hepburn)

    def update_count():
        nonlocal count
        nonlocal idx_arr
        print("update count:", count, "->", count-1)
        if count <= 1:
            # re-generate indices
            count, idx_arr = gen_idx_arr(dict_hepburn)
        else:
            count -= 1

    while True:
        choice = input("> ")

        if choice != 'exit':
            idx = idx_arr[count - 1] + 1
            if idx in [37, 39, 47, 48, 49]:
                print("idx:", idx, "---> pass")
                update_count()
                idx = idx_arr[count - 1] + 1
                print("updated idx to", idx)
            update_count()
            qn = dict_hepburn[idx]
            ans = dict_q[qn]
            print("count:", count)
            if args.mode1 == "kana":
                play(qn, ans)
            else:
                play(ans, qn)

        else:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='50-Laute-Tafel Übung')
    parser.add_argument('--mode1', default='kana',
        help='given kana to practise hepburn')
    parser.add_argument('--mode2', default='hiragana',
        help='practise hiragana or katakana')
    args = parser.parse_args()
    main(args)
