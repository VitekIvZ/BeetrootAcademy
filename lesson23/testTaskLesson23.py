#testTaskLesson23.py


import unittest
from typing import List, Tuple
from taskLesson23 import question1, question2, question3, question4, question5, question6

class TestTaskLesson23(unittest.TestCase):
    def test_question1(self):
        self.assertEqual(question1([1, 2, 3], [2, 3, 4]), [2, 3])
        self.assertEqual(question1([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(question1([], [1, 2, 3]), [])
        self.assertEqual(question1([1, 2, 3], []), [])

    def test_question2(self):
        self.assertEqual(question2(2), 1024)
        self.assertEqual(question2(1), 1)
        self.assertEqual(question2(0), 0)

    def test_question3(self):
        self.assertEqual(question3([1, 2, 3], [3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(question3([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(question3([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(question3([1, 2, 3], []), [1, 2, 3])

    def test_question4(self):
        self.assertEqual(question4([1, 2, 3, 4, 5]), 5)
        self.assertEqual(question4([5, 4, 3, 2, 1]), 5)
        self.assertEqual(question4([1]), 1)
        self.assertEqual(question4([]), 0)

    def test_question5(self):
        self.assertEqual(question5(2), [(0, 0), (0, 1), (1, 0), (1, 1)])
        self.assertEqual(question5(1), [(0, 0)])
        self.assertEqual(question5(0), [])

    def test_question6(self):
        self.assertEqual(question6(8), 1)
        self.assertEqual(question6(1), 1)
        self.assertEqual(question6(0), 0)

if __name__ == "__main__":
    unittest.main()
