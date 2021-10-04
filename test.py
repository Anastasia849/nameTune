# -*- coding: cp1251 -*-

import unittest
import game
import re


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = game.Game()

    def test_get_tune(self):
        tune = self.game.get_tune()
        self.assertEqual('.mp3', tune[-4:])

    def test_check_tune(self):
        self.game.tune='Рома, извини.mp3'
        self.game.inp = 'рома, извини.mp3'
        self.assertTrue(self.game.check_tune())

if __name__ == '__main__':
    unittest.main(verbosity=2)