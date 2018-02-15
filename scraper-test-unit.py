#!/usr/bin/env python

import unittest
import scraper

from lxml import etree, html
from lxml.etree import tostring
import requests

class UnitTest_Iterations(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.setupTest(self)
class TestCases(UnitTest_Iterations):
    def setupTest(self):
        self.header = '<!DOCTYPE html><html lang="en-US"><body><div class="wx_audiobook">'
        self.footer = '</div></body></html>'
        self.author = 'Patrick Shoggothfuss'
        self.title = 'Shame of the Wind'

    #Test Case 1, example 10.1
    def test_p_a_em_a(self):
        body = '<p><a href="a"><em>{}</em></a>, by {},<a href="b">stuff</a>more</p>'.format(self.title, self.author)
        website = self.header + body + self.footer
        result = scraper.getBookData(website)
        self.assertEqual(result, [['Shame of the Wind', 'Patrick Shoggothfuss']])
    #Test Case 2, example 10.2
    def test_p_a_em(self):
        body = '<p><a href="huh"><em>{}</em></a>, by {}, and somesuch</p>'.format(self.title, self.author)
        website = self.header + body + self.footer
        result = scraper.getBookData(website)
        self.assertEqual(result, [['Shame of the Wind', 'Patrick Shoggothfuss']])
    #Test Case 3, example 10.4
    def test_p_em_a(self):
        body = '<p><em><a href="eh">{}</a></em>by {}, and other info</p>'.format(self.title, self.author)
        website = self.header + body + self.footer
        result = scraper.getBookData(website)
        self.assertEqual(result, [['Shame of the Wind', 'Patrick Shoggothfuss']])
    #Test Case 4, example 10.10
    def test_p_em(self):
        body = '<p><em>{}</em>, by {}, and some other info.</p>'.format(self.title, self.author)
        website = self.header + body + self.footer
        result = scraper.getBookData(website)
        self.assertEqual(result, [['Shame of the Wind', 'Patrick Shoggothfuss']])
    #Test Case 5, example 10.20
    def test_p(self):
        body = '<p>{}, by {}</p>'.format(self.title, self.author)
        website = self.header + body + self.footer
        result = scraper.getBookData(website)
        self.assertEqual(result, [['Shame of the Wind', 'Patrick Shoggothfuss']])
    #Test Case 6, example 10.41
    def test_p_ahref(self):
        body = '<p><a href="heh">{}</a>, some info by {}</p>'.format(self.title, self.author)
        website = self.header + body + self.footer
        result = scraper.getBookData(website)
        self.assertEqual(result, [['Shame of the Wind', 'Patrick Shoggothfuss']])

if __name__ == '__main__':
    unittest.main()
