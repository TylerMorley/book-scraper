#!/usr/bin/env python

from lxml import etree, html
from lxml.etree import tostring
import requests

def getRawBookData(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    retVal = []

    audiobookList = tree.xpath('//div[@class="wx_audiobook"]')
    for book in audiobookList:
        bookInfo = findTitleAndAuthor(book)
        bookInfo[0] = trimTitleData(bookInfo[0])
        bookInfo[1] = trimAuthorData(bookInfo[1])
        retVal.append(bookInfo)
    return(retVal)

def trimTitleData(title):
    title = title.replace(u'\xa0', u' ')
    comma = title.find(",")
    if comma > 0:
        title = title[:comma]
    return title

def trimAuthorData(author):
    author = author.replace(u'\xa0', u' ')
    begin = author.find("by") + 3
    if begin > 0:
        author = author[begin:]
        comma = author.find(",")
        if comma > 0:
            author = author[:comma]
        if author[-1] == ".":
            author = author[:-1]
        return author
    print("trimAuthorData failed on ", author)

def findTitleAndAuthor(bookData):
    titleList = []
    authorList = []
    for el in bookData.iter():
        if el.text:
            titleList.append(el.text)
        if el.tail and len(el.tail.strip()) > 0:
            authorList.append(el.tail)
    if len(authorList) == 0:
        splitList = titleList[0].split(",")
        return [splitList[0], splitList[1]]
    return [titleList[0], authorList[0]]
