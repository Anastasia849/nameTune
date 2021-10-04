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
        self.assertTrue(self.game.tune==self.game.inp)

if __name__ == '__main__':
    unittest.main(verbosity=2)