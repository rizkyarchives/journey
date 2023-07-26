BACKGROUND_COLOR = "#B1DDC6"

import csv
import pykakasi

kakasi = pykakasi.kakasi()
text = '人物'
result = kakasi.convert(text)
print(result)
header = ['Japan', 'Romaji']
data = []

with open("D://Documents/Kuliah/100days/day-31/data/japan_words.csv", "r", newline='', encoding="utf8") as csvdata:
    japan_word = csv.reader(csvdata)
    for row in japan_word:
        result = kakasi.convert(row[0])
        eachrow = [row[0], result[0]['hepburn']]
        data.append(eachrow)

with open("D://Documents/Kuliah/100days/day-31/data/japan_words_finalbeta.csv", "w", newline='', encoding="utf8") as csvdata:
    writer = csv.writer(csvdata)
    writer.writerow(header)
    writer.writerows(data)