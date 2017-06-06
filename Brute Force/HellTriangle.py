import ast
import sys

#Triangle used to test and show like example
data = """                         55
                        94 48
                       95 30 96
                     77 71 26 67
                    97 13 76 38 45
                  07 36 79 16 37 68
                 48 07 09 18 70 26 06
               18 72 79 46 59 79 29 90
              20 76 87 11 32 07 07 49 18
            27 83 58 35 71 11 25 57 29 85
           14 64 36 96 27 11 58 56 92 18 55
         02 90 03 60 48 49 41 46 33 36 47 23
        92 50 48 02 36 59 42 79 72 20 82 77 42
      56 78 38 80 39 75 02 71 66 66 01 03 55 72
     44 25 67 84 71 67 11 61 40 57 58 89 40 56 36
   85 32 25 85 57 48 84 35 47 62 17 01 01 99 89 52
  06 71 28 75 94 48 37 10 23 51 06 48 53 18 74 98 15
27 02 92 23 08 71 76 84 15 52 92 63 81 10 44 10 69 93"""


class HellTriangle(object):

    def __init__(self):
        self.max_sum=0
        self.best_way=0
        #Create example by default
        self._load_example()
    
    def load_triangle_input(self):
        try:
            self.tri_data = ast.literal_eval(sys.argv[1])
        except:
            print("Input format incorrect.", file=sys.stderr)
            print("Try input like this: [[6],[3,5],[9,7,1],[4,6,8,4]]", file=sys.stderr)
            print("Solving example:", file=sys.stderr)
            print(data, file=sys.stderr)
    
    def _load_example(self):
        #Transform data (string) in multidimensional array of int
        self.tri_data = [list(map(int, row.split())) for row in data.splitlines()]
    
    def solve(self):
        """ Return total of maximum sum from top to bottom 
            
        """
        for i in range( 2**(len(self.tri_data)-1) ):
            elements_way = self.get_elements_way(i)
            current_sum = sum(elements_way)
            self._compare_best_way(current_sum, i)
        return self.max_sum

    def _get_bin_way(self, way):
        """ Return string with binary configuration about one way.
            This way tell when go to left(0) or right(1) starting in root(first element in top)
            Calc:
                -Convert way to binary number (string),             ex: >>>bin(30) >>>'0b11110'
                -Remove binary mark ("0b"),                         ex: >>>'11110'
                -Fill with zero in left to complete way tringule,   ex: >>>'011110'
            Parameters:
                way: Integer
        """
        return (bin(way)[2:]).zfill(len(self.tri_data)-1)
    
    def get_elements_way(self, way):
        """ Return list with elements in one way
            Parameters:
                way: Integer
        """
        bin_way = self._get_bin_way(way)
        elements = [ self.tri_data[0][0] ]
        last_index = 0
        for row in range(len(self.tri_data)-1):
            if(bin_way[row]=="0"):
                elements.append(self.tri_data[row+1][last_index])
            else:
                last_index += 1
                elements.append(self.tri_data[row+1][last_index])
        return elements
           
    def _compare_best_way(self, current_sum, way):
        """ Compare last max value saved and current values 
            to find what way has bigger total
            Parameters:
                current_sum: Integer 
                way: Integer
        """
        if(current_sum>self.max_sum):
            self.max_sum = current_sum
            self.best_way = way
            printvv("Best way found :D    Way: {}".format(way))


def printv(text):
    verbose = False
    if(verbose):
        print(text)
def printvv(text):
    more_verbose = False
    if(more_verbose):
        print(text)
        
if __name__ == '__main__':
    triangle = HellTriangle()
    triangle.load_triangle_input()
    print(triangle.solve())
    printv("Best way is {}".format(triangle.best_way))
    printv( "The elements in this way: {}".format(triangle.get_elements_way(triangle.best_way)) )
