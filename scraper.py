#!/usr/bin/env python

from lxml import etree, html
from lxml.etree import tostring
import requests

def scrapeBooks(url):
    pageContent = downloadPage(url)
    BookData = getBookData(pageContent)
    return BookData

def downloadPage(url):
    page = requests.get(url)
    return page.content

def getBookData(pageContent):
    retVal = []

    tree = html.fromstring(pageContent)
    audiobookList = tree.xpath('//div[@class="wx_audiobook"]')
    for book in audiobookList:
        bookInfo = getTitleAndAuthor(book)
        retVal.append(bookInfo)
    return(retVal)

def getTitleAndAuthor(bookData):
    titleList = []
    authorList = []
    retVal = []

    for el in bookData.iter():
        if el.text:
            titleList.append(el.text)
        if el.tail and len(el.tail.strip()) > 0:
            authorList.append(el.tail)

    if len(authorList) == 0:
        splitList = titleList[0].split(",")
        retVal.append(trimTitleData(splitList[0]))
        retVal.append(trimAuthorData(splitList[1]))
    else:
        retVal.append(trimTitleData(titleList[0]))
        retVal.append(trimAuthorData(authorList[0]))
    return retVal

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

def trimTitleData(title):
    title = title.replace(u'\xa0', u' ')
    comma = title.find(",")
    if comma > 0:
        title = title[:comma]
    return title
