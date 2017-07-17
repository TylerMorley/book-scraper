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

print(bookData)

expectedResult = ["The Savage Dead", "Plea",
"Seventy Maxims of Maximally Effective Mercenaries",
"Contracted Defense", "Vicious",
"An Astronaut’s Guide to Life on Earth: What Going to Space Taught Me About " +
"Ingenuity, Determination, and Being Prepared for Anything"
]
print(expectedResult)
