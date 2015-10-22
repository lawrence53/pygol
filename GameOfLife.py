import numpy as np

class GameOfLife():
  array   = []
  rows    = 0
  cols    = 0
  
  def __init__(self):
    print("Initializing game!")
	
  def InitArrayZeros(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.array = np.zeros((rows,cols), dtype=np.bool_)

  def InitArrayChecker(self):
    for r in range (0, self.rows):
      for c in range (0, self.cols):
        if (r & 0x1) ^ (c & 0x1):
          self.array[r,c] = True
	
if __name__ == "__main__":
  g = GameOfLife()
  print (g.array)
  g.InitArrayZeros(4,5)
  print (g.array)
  g.InitArrayChecker()
  print (g.array)
  