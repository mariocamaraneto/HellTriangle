import unittest
from HellTriangle import HellTriangle

class TestHellTriangle(unittest.TestCase):
    def test_triangle_example(self):
        triangle = HellTriangle()
        result = triangle.solve()
        self.assertEqual(result, 1320)

    def test_input(self):
        triangle = HellTriangle()
        triangle.tri_data = [[6],[3,5],[9,7,1],[4,6,8,4]]
        result = triangle.solve()
        self.assertEqual(result, 26)    
    
    def test_input_with_error(self):
        triangle = HellTriangle()
        triangle.load_triangle_input()
        result = triangle.solve()
        self.assertEqual(result, 1320)

    def test_get_elements_way_1(self):
        triangle = HellTriangle()
        triangle.tri_data = [[6],[3,5],[9,7,1],[4,6,8,4]]
        result = triangle.get_elements_way(0)
        self.assertEqual(result, [6,3,9,4])
    
    def test_get_elements_way_2(self):
        triangle = HellTriangle()
        triangle.tri_data = [[6],[3,5],[9,7,1],[4,6,8,4]]
        result = triangle.get_elements_way(15)
        self.assertEqual(result, [6,5,1,4])
    
    def test_get_bin_way_1(self):
        triangle = HellTriangle()
        triangle.tri_data = [[6],[3,5],[9,7,1],[4,6,8,4]]
        result = triangle._get_bin_way(0)
        self.assertEqual(result, "000")

    def test_get_bin_way_2(self):
        triangle = HellTriangle()
        triangle.tri_data = [[6],[3,5],[9,7,1],[4,6,8,4]]
        result = triangle._get_bin_way(15)
        self.assertEqual(result, "1111")

if __name__ == '__main__':
    unittest.main(buffer=True)