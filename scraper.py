#!/usr/bin/env python

from lxml import html
import requests

page = requests.get('http://www.writingexcuses.com/')
tree = html.fromstring(page.content)

bookData = tree.xpath(
'//div[@class="wx_audiobook"]/p/em/a/text() | ' +
'//div[@class="wx_audiobook"]/p/a/text() | ' +
'//div[@class="wx_audiobook"]/p/a/em/text()'
)

authorData = tree.xpath('//div[@class="wx_audiobook"]/p/text()')
cleanAuthorData = []
for name in authorData:
    if len(name) > 3:
        begin = name.find("by") + 3
        name = name[begin:]
        comma = name.find(",")
        if comma > 0:
            name = name[:comma]
        cleanAuthorData.append(name)

combinedData = []
if len(bookData) == len(cleanAuthorData):
    for index, val in enumerate(bookData):
        print(index)
        print(bookData[index])
        print(cleanAuthorData[index])
        entry = [bookData[index], cleanAuthorData[index]]
        combinedData.append(entry)

print(combinedData)

"""expectedResult = ["The Savage Dead", "Plea",
"Seventy Maxims of Maximally Effective Mercenaries",
"Contracted Defense", "Vicious",
"An Astronaut’s Guide to Life on Earth: What Going to Space Taught Me About " +
"Ingenuity, Determination, and Being Prepared for Anything"
]
print(expectedResult)"""
