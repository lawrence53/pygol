import numpy as np
import random

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
	
  def InitArrayRandom(self):
    for r in range (0, self.rows):
      for c in range (0, self.cols):
        self.array[r,c] = random.choice([True, False])

  def LifeStep(self):
    rows = self.rows
    cols = self.cols

    temp_array = np.zeros((rows,cols), dtype=np.bool_)   #Create an array of the size of our world to work on.
    #Look at every element in our world.
    for r in range (0, rows):
      for c in range (0, cols):
        sur_life = 0
        #Look at all the pixels surrounding this element.
        for sur_r in range (-1, 1):
          for sur_c in range (-1, 1):
            #Calculate position after wrap arounds.
            if ((r + sur_r)==rows):
              r_i = 0;
            elif ((r + sur_r)<0):
              r_i = rows-1
            else:
              r_i = r + sur_r
            
            if ((c + sur_c)==cols):
              c_i = 0;
            elif ((c + sur_c)<0):
              c_i = cols-1
            else:
              c_i = c + sur_r

            if not(r_i==0 and c_i==0):                #If not the centre bit.
              if(self.array[r_i,c_i]==True):
                sur_life += 1

        if self.array[r,c]==True:                   #If this cell is alive.
          if sur_life < 2:                           #Under population
            temp_array[r,c] = False                 
          if (sur_life > 1) and (sur_life<4):
            temp_array[r,c] = True                  #2 or 3 sustainable.
          if sur_life > 3:
            temp_array[r,c] = True                  #> 3 usustainable.
		  
        else:                                       #This cell is dead.
          if sur_life == 3:
            temp_array[r,c] = True                  #3 repoduction.
    
    self.array = temp_array

            
		
if __name__ == "__main__":
  g = GameOfLife()
  print ("Empty:")
  print (g.array)
  
  g.InitArrayZeros(4,10)
  print ("Zeros:")
  print (g.array)
  
  g.InitArrayChecker()
  print ("Checkered:")
  print (g.array)
  
  g.InitArrayRandom()
  print ("Random:")
  print (g.array)
  g.LifeStep()
  print ("Life stepped:")
  print (g.array)
  
  
  
  