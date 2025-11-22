import os
import random
print("\033[48;2;250;218;221m")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def show_menu():
    clear()
    print("\n\n\n\n\n")
    print("\033[38;2;255;105;180m          日本語　Study. ひらがな　and カタカナ　trainer")
    print("\n")
    print("\033[38;2;255;105;180m       ░░░░░░░        ░░░░░░░")
    print("\033[38;2;255;105;180m  ░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░")
    print("\033[38;2;255;105;180m    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("\033[38;2;255;105;180m    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("\033[38;2;255;105;180m     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("\033[38;2;255;105;180m       ░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("\033[38;2;255;105;180m            ░░░░░░░░░░░░░░░")
    print("\033[38;2;255;105;180m             ░░░░░░░░░░░░")
    print("\033[38;2;139;69;19m                    ▐")
    print("\033[38;2;139;69;19m                    ▐▌")
    print("\033[38;2;139;69;19m                     ▀▌")
    print("\033[38;2;139;69;19m                      ▌")
    print("\033[38;2;139;69;19m                    ▄▀")
    print("\033[38;2;139;69;19m                  ▄▀▀")
    print("\033[38;2;139;69;19m               ▄▀▀")
    print("\033[38;2;139;69;19m          ▀▀▀▀▀▀▀▀▀▀▀")
    print(" "*5, "\033[38;2;75;0;130m╒════════════════════╕   ╒════════════════════╕")
    print(" "*5, "│     ひらがな       ╞═══╡     カタカナ       │")
    print(" "*5, "╘════════════════════╛   ╘════════════════════╛\033[38;2;75;0;130m")
    print(" "*5, "\nMode: h - ひらがな, k - カタカナ, exit - EXIT")
    print("\n")
    choice = input("\033[38;2;200;160;255m>_ ").lower()
    clear()
    print("\033[38;2;255;105;180m せーの！\033[37m")
    return choice

hiragana = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    # K
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    # S
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    # T
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    # N
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    # H
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    # M
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    # Y
    "や": "ya", "ゆ": "yu", "よ": "yo",
    # R
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    # W + N
    "わ": "wa", "を": "wo", "ん": "n",
}
katakana = { 
    "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
    # K
    "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
    # S
    "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
    # T
    "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
    # N
    "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
    # H
    "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
    # M
    "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
    # Y
    "ヤ": "ya", "ユ": "yu", "ヨ": "yo",
    # R
    "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
    # W + N
    "ワ": "wa", "ヲ": "wo", "ン": "n",
}
def run_trainer(charset):
    correct = 0
    wrong = 0
    for _ in range(10):
        symbol = random.choice(list(charset.keys()))
        print(f"\n\033[38;2;200;160;255mHow to read: {symbol}")
        answer = input("\033[38;2;255;105;180m>_ ").strip().lower()
        if answer == "0":
            clear()
            continue
        if answer == charset[symbol]:
            print(" "*5, "\033[32m╒════════════╕")
            print(" "*5, "│ ✓ Correct! │")
            print(" "*5, "╘════════════╛\033[37m")
            correct += 1
        else:
            print(" "*5, "\033[31m╒═════════════╕ ╒═════════════════════╕")
            print(" "*5, f"│ ✗ Uncorrect │ │Correct variant is {charset[symbol]}│")
            print(" "*5, "╘═════════════╛ ╘═════════════════════╛\033[37m")
            wrong += 1
    print("\n\033[38;2;255;105;180mありがとう！\033[37m")
    print(" "*5, f"\033[38;2;200;160;255m\nSo: {correct} Correct, {wrong} Mistakes.\n")
    input("\033[38;2;200;160;255mPress ENTER, to back to the menu...")

while True:
    mode = show_menu()
    if mode == "h":
        run_trainer(hiragana)
    elif mode == "k":
        run_trainer(katakana)
    elif mode == "exit":
        break
    else:
        print("\033[31mOption ERROR!")