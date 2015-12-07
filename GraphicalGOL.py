import matplotlib.pyplot as plt
import GameOfLife as GOL
import matplotlib.cm as cm
import pylab

if __name__ == "__main__":
  g = GOL.GameOfLife()
  g.InitArrayZeros(20,30)
  g.InitArrayRandom()
  
  fig = plt.figure()
  fig.show()
  fig_ax = fig.add_subplot(111)

  for i in range (0, 10000):
    g.LifeStep()
    #g.PrettyPrint()
    fig_ax.imshow(g.array, cm.gray)
    fig.canvas.draw()
    print("Life step:{0:d}\n", i)
    pylab.pause(0.001)
    fig_ax.clear()
    
