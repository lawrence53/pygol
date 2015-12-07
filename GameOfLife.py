import numpy as np
import random
import sys

class GameOfLife(object):
  #array   = []
  #bugarr  = []
  #rows    = 0
  #cols    = 0
  
  def __init__(self):
    print("Initializing game!")
	
  def InitArrayZeros(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.array = np.zeros((rows,cols), dtype=np.bool_)
    #self.bugarr = np.zeros((rows,cols), dtype=np.int16)

  def InitArrayChecker(self):
    for r in range (0, self.rows):
      for c in range (0, self.cols):
        if (r & 0x1) ^ (c & 0x1):
          self.array[r,c] = True
	
  def InitArrayRandom(self):
    for r in range (0, self.rows):
      for c in range (0, self.cols):
        self.array[r,c] = random.choice([True, False])

  def PrettyPrint(self):
     for r in range (0, self.rows):
	  
       for c in range (0, self.cols):
         if self.array[r,c]==True:
           sys.stdout.write('X ')
         else:
           sys.stdout.write('0 ')
       sys.stdout.write('\n')
	
  def LifeStep(self):
    rows = self.rows
    cols = self.cols

    temp_array = np.zeros((rows,cols), dtype=np.bool_)   #Create an array of the size of our world to work on.
    #Look at every element in our world.
    for r in range (0, rows):
      for c in range (0, cols):
        sur_life = 0
        #Look at all the pixels surrounding this element.
        for sur_r in range (-1, 2):
          for sur_c in range (-1, 2):
            #Calculate position after wrap around.
            if ((r + sur_r)==rows):
              r_i = 0;
            elif ((r + sur_r)==-1):
              r_i = rows-1
            else:
              r_i = r + sur_r
            
            if ((c + sur_c)==cols):
              c_i = 0;
            elif ((c + sur_c)==-1):
              c_i = cols-1
            else:
              c_i = c + sur_c

            if not(sur_r==0 and sur_c==0):                #If not the centre bit.
              if(self.array[r_i,c_i]==True):
                sur_life += 1

        #self.bugarr[r,c] = sur_life
		
        if self.array[r,c]==True:                   #If this cell is alive.
          if sur_life < 2:                           #Under population
            temp_array[r,c] = False                 
          if (sur_life > 1) and (sur_life<4):
            temp_array[r,c] = True                  #2 or 3 sustainable.
          if sur_life > 3:
            temp_array[r,c] = False                 #> 3 unsustainable.
		  
        else:                                       #This cell is dead.
          if sur_life == 3:
            temp_array[r,c] = True                  #3 reproduction.
          else:
            temp_array[r,c] = False
			
    
    self.array = temp_array

            
		
if __name__ == "__main__":
  g = GameOfLife()
  #print ("Empty:")
  #g.PrettyPrint()
  
  g.InitArrayZeros(5,7)
  #print ("Zeros:")
  #g.PrettyPrint()
  
  #g.InitArrayChecker()
  #print ("Checkered:")
  #g.PrettyPrint()
  
  g.InitArrayRandom()
  print ("Random:")
  g.PrettyPrint()
  for i in range (0, 10):
    g.LifeStep()
    print ("Life stepped:")
    #print (g.bugarr)
    g.PrettyPrint()
 
  