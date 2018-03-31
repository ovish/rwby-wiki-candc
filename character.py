#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs

with open('j0-all.md', 'r') as f:
    strJpn = f.read()

# maketranseを使う

table = str.maketrans({
    'Ruby Rose': 'ルビー・ローズ',
    'Weiss Schnee': 'ワイス・シュニー',
    'Blake Belladonna': 'ブレイク・ベラドンナ',
    'Yang Xiao Long': 'ヤン・シャオロン',

    'Jaune Arc': 'ジョーン・アーク',
    'Nora Valkyrie': 'ノーラ・ヴァルキリー',
    'Pyrrha Nikos': 'ピュラ・ニコス',
    'Lie Ren': 'ライ・レン',

    'Ozpin': 'オズピン',
    'Glynda Goodwitch': 'グリンダ・グッドウィッチ',
    'Peter Port': 'ピーター・ポート',
    'Bartholomew Oobleck': 'バーソロミュー・ウーブレック',

    'James Ironwood': 'ジェームズ・アイアンウッド',
    'Winter Schnee': 'ウィンター・シュニー',
    'Penny Polendina': 'ペニー・ポレンディーナ',

    'Summer Rose': 'サマー・ローズ',
    'Taiyang Xiao Long': 'タイヤン・シャオロン',
    'Raven Branwen': 'レイヴン・ブランウェン',
    'Qrow Branwen': 'クロウ・ブランウェン',

    'Salem': 'セイラム',
    'Arthur Watts': 'アーサー・ワッツ',
    'Hazel Rainart': 'ヘイゼル・レイナート',
    'Tyrian Callows': 'ティリアン・キャロウズ',

    'Cinder Fall': 'シンダー・フォール',
    'Roman Torchwick': 'ローマン・トーチウィック',
    'Emerald Sustrai': 'エメラルド・サストライ',
    'Mercury Black': 'マーキュリー・ブラック',
    'Neopolitan': 'ニオポリタン',

    'Adam Taurus': 'アダム・トーラス',
    'White Fang Lieutenant': 'ホワイト・ファングの中尉',

    'Cardin Winchester': 'カーディン・ウィンチェスター',
    'Russel Thrush': 'ラッセル・スラッシュ',
    'Dove Bronzewing': 'ダヴ・ブロンズウィング',
    'Sky Lark': 'スカイ・ラーク',

    'Coco Adel': 'ココ・アデル',
    'Fox Alistair': 'フォックス・アリステア',
    'Velvet Scarlatina': 'ヴェルヴェット・スカーラティーナ',
    'Yatsuhashi Daichi': 'ヤツハシ・ダイチ',

    'Sun Wukong': 'サン・ウーコン',
    'Scarlet David': 'スカーレット・デイビッド',
    'Sage Ayana': 'セージ・アヤナ',
    'Neptune Vasilias': 'ネプチューン・ヴァシリアス'


})

result = strJpn.translate(table)

with open('result.md', 'w') as f:
        f.write(result)
