
class HellTriagule(object):

    def __init__(self):
        self.max_sum=0
        self.best_way=0
        #Create exemple by default
        self._load_exemple()
        
    def _load_exemple(self):
        self.tri_data = [[6],[3,5],[9,7,1],[9,6,8,4]]
        self.tri_len = len(self.tri_data)
    
    def max_total(self):
        """ Return total of maximum sum from top to bottom 
            
        """
        for i in range( 2**(self.tri_len-1) ):
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
        return (bin(way)[2:]).zfill(self.tri_len-1)
    
    def get_elements_way(self, way):
        """ Return list with elements in one way
            Parameters:
                way: Integer
        """
        bin_way = self._get_bin_way(way)
        elements = [ self.tri_data[0][0] ]
        last_index = 0
        for row in range(self.tri_len-1):
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
    verbose = True
    if(verbose):
        print(text)
def printvv(text):
    more_verbose = False
    if(more_verbose):
        print(text)
        
if __name__ == '__main__':
    triangle = HellTriagule()
    print( "The maximum total in Hell Triangle is {}".format(triangle.max_total()) )
    printv("Best way is {}".format(triangle.best_way))
    printv( "The elements in this way: {}".format(triangle.get_elements_way(triangle.best_way)) )
