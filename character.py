#!/usr/local/bin/python3
# -*- coding, utf-8 -*-

import re
import sys
import os
import codecs

with open('j0-all.md', 'r') as f:
    strJpn = f.read()

# maketranseを使う
result =
    strJpn.replace('Ruby Rose', 'ルビー・ローズ'
    ).replace('Weiss Schnee', 'ワイス・シュニー'
    ).replace('Blake Belladonna', 'ブレイク・ベラドンナ'
    ).replace('Yang Xiao Long', 'ヤン・シャオロン'

    ).replace('Jaune Arc', 'ジョーン・アーク'
    ).replace('Nora Valkyrie', 'ノーラ・ヴァルキリー'
    ).replace('Pyrrha Nikos', 'ピュラ・ニコス'
    ).replace('Lie Ren', 'ライ・レン'

    ).replace('Ozpin', 'オズピン'
    ).replace('Glynda Goodwitch', 'グリンダ・グッドウィッチ'
    ).replace('Peter Port', 'ピーター・ポート'
    ).replace('Bartholomew Oobleck', 'バーソロミュー・ウーブレック'

    ).replace('James Ironwood', 'ジェームズ・アイアンウッド'
    ).replace('Winter Schnee', 'ウィンター・シュニー'
    ).replace('Penny Polendina', 'ペニー・ポレンディーナ'

    ).replace('Summer Rose', 'サマー・ローズ'
    ).replace('Taiyang Xiao Long', 'タイヤン・シャオロン'
    ).replace('Raven Branwen', 'レイヴン・ブランウェン'
    ).replace('Qrow Branwen', 'クロウ・ブランウェン'

    ).replace('Salem', 'セイラム'
    ).replace('Arthur Watts', 'アーサー・ワッツ'
    ).replace('Hazel Rainart', 'ヘイゼル・レイナート'
    ).replace('Tyrian Callows', 'ティリアン・キャロウズ'

    ).replace('Cinder Fall', 'シンダー・フォール'
    ).replace('Roman Torchwick', 'ローマン・トーチウィック'
    ).replace('Emerald Sustrai', 'エメラルド・サストライ'
    ).replace('Mercury Black', 'マーキュリー・ブラック'
    ).replace('Neopolitan', 'ニオポリタン'

    ).replace('Adam Taurus', 'アダム・トーラス'
    ).replace('White Fang Lieutenant', 'ホワイト・ファングの中尉'

    ).replace('Cardin Winchester', 'カーディン・ウィンチェスター'
    ).replace('Russel Thrush', 'ラッセル・スラッシュ'
    ).replace('Dove Bronzewing', 'ダヴ・ブロンズウィング'
    ).replace('Sky Lark', 'スカイ・ラーク'

    ).replace('Coco Adel', 'ココ・アデル'
    ).replace('Fox Alistair', 'フォックス・アリステア'
    ).replace('Velvet Scarlatina', 'ヴェルヴェット・スカーラティーナ'
    ).replace('Yatsuhashi Daichi', 'ヤツハシ・ダイチ'

    ).replace('Sun Wukong', 'サン・ウーコン'
    ).replace('Scarlet David', 'スカーレット・デイビッド'
    ).replace('Sage Ayana', 'セージ・アヤナ'
    ).replace('Neptune Vasilias', 'ネプチューン・ヴァシリアス'
    )


with open('result.md', 'w') as f:
        f.write(result)
