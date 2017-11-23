import math
from operator import itemgetter, attrgetter
class Point:
  def __init__(self, a=0, b=0):
    self.x=a
    self.y=b

class Solution:
  """
  @param: points: a list of points
  @param: origin: a point
  @param: k: An integer
  @return: the k closest points
  """
  def kClosest(self, points, origin, k):
    # if list < knum just return
    if len(points)<=k: return points
    # function to calculate distance between origin and certain point
    def distanceBetween(pin):
      return math.sqrt(math.pow(pin.x-origin.x,2)+math.pow(pin.y-origin.y,2))
    allDis=[]
    for pin in points:
      dis=distanceBetween(pin)
      allDis.append({
        "x":pin.x,
        "y":pin.y,
        "dis":dis
      })
    sortValues=sorted(allDis, key=lambda p:(p["dis"],p["x"],p["y"]))
    print(sortValues)
    result=[[dic["x"],dic["y"]] for dic in sortValues]
    print(result)


if __name__=="__main__":
  solver=Solution()
  origin=Point(0,0)
  points=[
    Point(4,6),
    Point(4,7),
    Point(4,4),
    Point(2,5),
    Point(1,1)
  ]
  k=3
  solver.kClosest(points, origin, 3)

