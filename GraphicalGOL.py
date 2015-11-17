from scipy.misc.pilutil import toimage
import GameOfLife as GOL

if __name__ == "__main__":
  g = GOL.GameOfLife()
  g.InitArrayZeros(200,300)
  g.InitArrayRandom()
  for i in range (0, 5):
    toimage(g.array).show()
    g.LifeStep()
    toimage(g.array).show()