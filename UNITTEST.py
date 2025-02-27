import unittest
from p4 import question 
class TestQuestionFunction(unittest.TestCase):
    def test_question(self):
        result = question("AI","ML")
        self.assertEqual(result, "How do AI and ML relate to each other.What are their roles in current technology.")
if __name__== "__main__":
    unittest.main(verbosity=2)
