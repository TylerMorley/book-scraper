#!/usr/bin/env python

import scraper
from lxml import html
import requests
import unittest

class ScraperTest(unittest.TestCase):
    def test_scrapeInfo(self):
        data = scraper.getRawBookData(seasonTenUrl)
        
        self.assertEqual(len(data), len(seasonTenData))
        self.assertEqual(data, seasonTenData)

seasonTenUrl = "http://www.writingexcuses.com/category/season/season-10/"
seasonTenData = [['Lock In', 'John Scalzi'],
['Shipstar', 'Gregory Benford and Larry Niven'],
['Maplecroft', 'Cherie Priest'],
['City of Stairs', 'Robert Jackson Bennett'],
['Wolf Hall', 'Hilary Mantel'],
['Three Parts Dead', 'Max Gladstone'],
['The Splendour Falls', 'Susanna Kearsley'],
['Furies of Calderon', 'Jim Butcher'],
['Ancillary Justice', 'Anne Leckie'],
['The Man in the High Castle', 'Phillip K. Dick'],
['The Hero’s Guide to Storming the Castle', 'Christopher Healy'],
['The Immortal Life of Henrietta Lacks', 'Rebecca Skloot'],
['Words of Radiance', 'Brandon Sanderson'],
['The Three-Body Problem', 'Cixin Liu'],
['The Rebirths of Tao', 'Wesley Chu'],
['The Golem and the Jinni', 'Helen Wecker'],
['The Shepherdess of Sienna: A Novel of Renaissance Tuscany', 'Linda Lafferty'],
['Stormdancer: The Lotus War', 'Jay Kristoff'],#, Book One
['A Spy in the House: The Agency 1', 'Y.S. Lee'],
['The Autumn Republic', 'Brian McClellan'],
['A Wilder Rose', 'Susan Wittig Albert'],
['Of Noble Family', 'Mary Robinette Kowal'],
['The Unhappening of Genesis Lee', 'Shallee McArthur'],
['Uprooted', 'Naomi Novik'],
['The Devil’s Only Friend', 'Dan Wells'],
['Perfume: The Story of a Murderer', 'Patrick Süskind'],
['The Goblin Emperor', 'Katherine Addison'],
['The Winner’s Curse', 'Marie Rutkowski'],
['The Edge of the World: Terra Incognita', 'Kevin J. Anderson'],#, Book 1
['The Summer Prince', 'Alaya Dawn Johnson'],
['Time Salvager', 'Wesley Chu'],
['Seveneves: A Novel', 'Neal Stephenson'],
['A Natural History of Dragons: A Memoir by Lady Trent', 'Marie Brennan'],
['Nothing to Envy: Ordinary Lives in North Korea', 'Barbara Demick'],
['I Am Princess X', 'Cherie Priest'],
['A Darker Shade of Magic', 'V. E. Schwab'],
['Wolf Hall', 'Hilary Mantel'],
['Clockwork Angels', 'Kevin J. Anderson'],
['Sister Mine', 'Nalo Hopkinson'],
['The Merchant Adventurer', 'Patrick E. McLean'],
['Shadows of Self', 'Brandon Sanderson'],
['The Freedom Maze', 'Delia Sherman'],
['Off To Be The Wizard', 'Scott Meyer'],
['The Mirror Empire: Worldbreaker Saga', 'Kameron Hurley'],
['Swordspoint: A Melodrama of Manners', 'Ellen Kushner'],
['Blindsight', 'Peter Watts'],
['The Devil’s Only Friend', 'Dan Wells'],
['Half-Resurrection Blues: Bone Street Rumba', 'Daniel José Older'],#, Book 1
['The Providence of Fire: Chronicles of the Unhewn Throne', 'Brian Staveley'],#, book 2
['Mystic', 'Jason Denzel'],
['The Cloud Roads', 'Martha Wells']]

if __name__ == '__main__':
    unittest.main()
