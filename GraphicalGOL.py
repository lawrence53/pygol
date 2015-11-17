import matplotlib.pyplot as plt
import GameOfLife as GOL
import matplotlib.cm as cm
import time

if __name__ == "__main__":
  g = GOL.GameOfLife()
  g.InitArrayZeros(100,150)
  g.InitArrayRandom()
  
  fig = plt.figure()
  fig.show()
  #fig.add_axes(aspect="equal",extent=[0, g.rows, 0, g.cols])
  #fig_ax = fig.gca() #Get the current axis
  fig_ax = fig.add_subplot(111)

  for i in range (0, 1000):
    g.LifeStep()
    #g.PrettyPrint()
    fig_ax.imshow(g.array, cm.gray)
    fig.canvas.draw()
    print("Life step:{0:d}\n", i)
    time.sleep(0.1)
    fig_ax.clear()
    
