import unittest

INPUT = """
str: "hello"
int: 2
list:
- a
- b
"""

class TestPyYAML(unittest.TestCase):

    def test_basic(self):
        import yaml
        self.assertEqual({"str": "hello", "int": 2, "list": ["a", "b"]}, yaml.load(INPUT))
