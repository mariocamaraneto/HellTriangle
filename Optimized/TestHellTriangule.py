import unittest
from HellTriangle import HellTriagle

class TestHellTriangle(unittest.TestCase):
    def test_triangle_example(self):
        triangle = [[6],[3,5],[9,7,1],[4,6,8,4]]
        result = solve(triangle)
        self.assertEqual(result, 26)
        
    def test_triangle_example(self):
        triangle = [[6],[3,5],[9,7,1],[9,6,8,4]]
        result = solve(triangle)
        self.assertEqual(result, 27)   

if __name__ == '__main__':
    unittest.main(buffer=True)