import numpy as np

class GameOfLife():
  array   = []
  rows    = []
  cols    = []
  
  def __init__(self):
    print("Initializing game!")
	
  def InitArrayZeros(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.array = np.zeros((rows,cols), dtype=np.bool_)
	
if __name__ == "__main__":
  g = GameOfLife()
  print (g.array)
  g.InitArrayZeros(4,5)
  print (g.array)
  