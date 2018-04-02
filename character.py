#!/usr/local/bin/python3
# -*- coding, utf-8 -*-

import re
import sys
import os
import codecs

with open('j0-all.md', 'r') as f:
    strJpn = f.read()

# maketranseを使う
result = strJpn.replace('Ruby Rose', 'ルビー・ローズ'
    ).replace('Weiss Schnee', 'ワイス・シュニー'
    ).replace('Blake Belladonna', 'ブレイク・ベラドンナ'
    ).replace('Yang Xiao Long', 'ヤン・シャオロン'

    ).replace('Jaune Arc', 'ジョーン・アーク'
    ).replace('Nora Valkyrie', 'ノーラ・ヴァルキリー'
    ).replace('Pyrrha Nikos', 'ピュラ・ニコス'
    ).replace('Lie Ren', 'ライ・レン'

    ).replace('Young Ren', '幼いレン'
    ).replace('Young Nora', '幼いノーラ'

    ).replace('Ozpin', 'オズピン'
    ).replace('Glynda Goodwitch', 'グリンダ・グッドウィッチ'
    ).replace('Peter Port', 'ピーター・ポート'
    ).replace('Bartholomew Oobleck', 'バーソロミュー・ウーブレック'

    ).replace('James Ironwood', 'ジェームズ・アイアンウッド'
    ).replace('Winter Schnee', 'ウィンター・シュニー'
    ).replace('Jacques Schnee', 'ジャック・シュニー'
    ).replace('Whitley Schnee', 'ウィットリー・シュニー'
    ).replace('Klein Sieben', 'クライン・ジーベン'

    ).replace('Penny Polendina', 'ペニー・ポレンディーナ'
    ).replace('Ciel Soleil', 'シエル・ソレイユ'
    ).replace('Flynt Coal', 'フリント・コール'
    ).replace('Neon Katt', 'ネオン・カット'

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

    ).replace('Leonardo Lionheart', 'レオナルド・ライオンハート'

    ).replace('Adam Taurus', 'アダム・トーラス'
    ).replace('White Fang Lieutenant', 'ホワイト・ファングの中尉'
    ).replace('Ilia Amitola', 'イリア・アミトーラ'
    ).replace('Sienna Khan', 'シエナ・カーン'
    ).replace('Corsac Albain', 'コサック・アルベイン'
    ).replace('Fennec Albain', 'フェネック・アルベイン'

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

    ).replace('Arslan Altan', 'アルスラーン・アルタン'
    ).replace('Bolin Hori', 'ボリン・オーリ'
    ).replace('Reese Chloris', 'リース・クロリス'
    ).replace('Nadir Shiko', 'ナディール・シコ'

    ).replace('Nebula Violette', 'ネビュラ・ヴィオレッテ'
    ).replace('Dew Gayl', 'デュー・ゲイル'
    ).replace('Gwen Darcy', 'グウェン・ダーシー'
    ).replace('Octavia Ember', 'オクタヴィア・エンバー'

    ).replace('Brawnz Ni', 'ブロンズ・ニー'
    ).replace('Roy Stallion', 'ロイ・スタリオン'
    ).replace('Nolan Porfirio', 'ノーラン・ポーフィリオ'
    ).replace('May Zedong', 'メイ・ツィートン'

    ).replace('Ghira Belladonna', 'ギラ・ベラドンナ'
    ).replace('Kali Belladonna', 'カーリー・ベラドンナ'

    ).replace('Junior Xiong', 'ジュニア・ション'
    ).replace('Melanie', 'メラニー・マラカイト'
    ).replace('Melanie Malachite', 'メラニー・マラカイト'
    ).replace('Miltia Malachite', 'ミルシャ・マラカイト'

    ).replace('Li Ren', 'リー・レン'
    ).replace('An Ren', 'アン・レン'

    ).replace('Zwei', 'ツヴァイ'
    ).replace('Shopkeep', '店主'
    ).replace('Tukson', 'タクソン'
    ).replace('Oscar Pine', 'オスカー・パイン'
    ).replace('Amber', 'アンバー'
    ).replace('Vernal', 'ヴァーナル'
    ).replace('Grimm', 'グリム'
    ).replace('Reporter', 'リポーター'
    ).replace('Businesswoman', '女性実業家'
    ).replace('Businessman', '男性実業家'
    ).replace('Captain', '船長'
    ).replace('Deery', 'ディアリー'
    ).replace('Detective', '刑事'
    ).replace('Henry Marigold', 'ヘンリー・マリーゴールド'
    ).replace('Yuma', 'ユマ'
    ).replace('Mata', 'マタ'
    ).replace('Huntsman', 'ハンター'
    ).replace('Doctor Merlot', 'ドクター・メルロー'
    ).replace('Trophy', 'トロフィー'
    ).replace('First Mate', '一等航海士'
    )


with open('result.md', 'w') as f:
        f.write(result)
