# -*- coding: utf-8 -*-
"""
unit test: developer isidir.

regresyon, gerileme, calisan birseyin calismaz hale gelmesi.

test kodu, test edilen kodun ne kadarini cover ediyor / kapsiyor?
test coverage: 45

Microsoft, %80+

https://dzone.com/articles/7-popular-unit-test-naming
"""

import unittest

from string2 import validate_pwd, middlestrip


class ValidatePwdTestCase(unittest.TestCase):
    def validatepwd_strongpwd_true(self):
        # isAdult_AgeLessThan18_False
        # validatepwd_strongpwd_true
        actual = validate_pwd("DarkLord666-")
        self.assertTrue(actual)

    def validatepwd_weakpwd_false1(self):
        actual = validate_pwd("1111111")
        self.assertFalse(actual)

    def validatepwd_weakpwd_false2(self):
        actual = validate_pwd("darkLord666-")
        self.assertFalse(actual)

class MiddleStripTestCase(unittest.TestCase):
    def middlestrip_strwithleadingspace_pass(self):
        actual = middlestrip("  def")
        expected = "  def"
        self.assertEqual(expected, actual)

def main():
    unittest.main()


if __name__ == "__main__":
    main()
