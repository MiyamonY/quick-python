# /usr/bin/env python
# -*- coding:utf-8 -*-

### 文字列
## 文字のシーケンスとしての文字列
x = "Hello"
print(x[0])

print(x[-1])

print(x[1:])

x = "Goodbye\n"
x = x[:-1]
print(x)

print(len("Goodbye"))

# 文字列はイミュータブル
# x[1:2] = "abc" エラー

## 基本的な文字列操作
x = "Hello " + "World"
print(x)

print(8 * "x")

## 特殊文字とエスケープシーケンス
print("\a")
print("aa\b")

# 8進数と16進数
print("m", "\155", "\x6D")

print("\n", "\012", "\x0A")     # すべて改行

unicode_a = '\N{LATIN SMALL LETTER A}'
print(unicode_a)

unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'
print(unicode_a_with_acute)

print('\u00E1')                 # unicodeをそのまま

print('a\n\tb')
print("abc\n")

print("abc\n", end="")          # endパラメータに""を渡し改行を行なわなくする

## 文字列のメソッド
print(" ".join(["join", "puts", "spaces", "between", "elements"]))
print("::".join(["Separated", "with", "colons"]))
print("".join(["Separated", "by", "nothing"]))

x = "You\t\t can have tabs\t\n \t and newlines \n\n "\
"mixied in"

print(x.split())
x = "Mississippi"
print(x.split("ss"))

x = 'a b c d'
print(x.split(' ', 1))          # 二番目の引数でsplit回数を指定
print(x.split(' ', 2))          # デフォルトの値でsplitしたい、かつ二番目の引数を指定した場合は、一番目の引数にNoneを渡す
print(x.split(' ', 9))

print(float("123.456"))
# float('xxyy') エラー

print(int('33333'))
# print(int('123.456')) エラー

print(int('10000', 8))          # 8進数として解釈
print(int('101', 2))

print(int('ff' , 16))
# int('123456', 6) エラー

x = " Hello, World\t\t "
print(x.strip())
print(x.lstrip())
print(x.rstrip())

# 空白文字はstring.whitespaceで指定さている
import string
print(string.whitespace)

x = "www.python.org"
print(x.strip("w"))
print(x.strip("gor"))
print(x.strip(".gorw"))

# 文字列の検索
x = "Mississippi"
print(x.find("ss"))
print(x.find("zz"))             # 見つからない場合は-1を返す

x = "Mississippi"
print(x.find("ss", 3))          # 3番目以降で探す
print(x.find("ss", 0, 3))       # 0~3番目で探す
print(x.rfind("ss"))            # 後ろから探す

x = "Mississippi"
print(x.count("ss"))

x = "Mississippi"
print(x.startswith("Miss"))
print(x.startswith("Mist"))
print(x.endswith("pi"))
print(x.endswith("p"))

print(x.endswith(("i", "u")))   # タプルを渡したらorで確認

x = "Mississippi"
print(x.replace("ss", "+++"))

x = "~x ^ (y % z)"
table = x.maketrans("~^()", "!&[]") # 変換テーブルを作って
print(x.translate(table))           # 変換させる

# 文字列を編集する場合、一旦リストに変換してから編集して文字列に戻す方法もある
text = "Hello, World"
wordList = list(text)
wordList[6:] = []
wordList.reverse()
text = "".join(wordList)
print(text)

# 便利なメソッドと定数
x = "123"
print(x.isdigit(), x.isalpha())

x = "M"
print(x.islower(), x.isupper())

### オブジェクトから文字列への変換
print(repr([1, 2, 3, 4]))

x = [1]
x.append(2); x.append([3, 4])
print("the list x is " + repr(x))

print(repr(len))

## formatメソッドの利用
print("{0} is the {1} of {2}".format("Ambrosia", "food", "the gods"))
print("{{Ambrosia}} is the {0} of {1}".format("food", "the gods")) # {}を印字したいときは{}で囲む

print("{food} is the food of {user}".format(food="Ambrosia", user="the gods"))
print("{0} is the food of {user[1]}".format("Ambrosia", user=["men", "the gods", "others"]))

print("{0:10} is the food of gods".format("Ambrosia")) # 左詰めで10
print("{0:{1}} is the food of gods".format("Ambrosia", 10)) # 値を指定することもできる

print("{food:{width}} is the food of gods".format(food="Ambrosia", width=10))

print("{0:>10} is the food of gods".format("Ambrosia")) # 右詰め
print("{0:&>10} is the food of gods".format("Ambrosia")) # &でパディングする


# %の書式設定は古いもので今後削除される予定

## bytes
unicode_a_with_acute = "\N{LATIN SMALL LETTER A WITH ACUTE}" # unicode
xb = unicode_a_with_acute.encode()                           # unicodeをbytesに変換
print(xb)
# xb += 'A' エラー bytes型と文字列型の値は連結できない

print(xb.decode())

