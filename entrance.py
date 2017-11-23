
class Reactangel:
  width=0.0
  height=0.0
  def __init__(self, width, height):
    self.width=width
    self.height=height
  
  def getArea(self):
    return self.width*self.height

def sortArray():
  list=[3,2,1,4,5]
  list=answerSortArray(list)
  print(list)
def answerSortArray(list):
  if len(list)<=1 or list is None:
    return list
  sorted=[list[0]]
  for i in range(1,len(list)):
    num=list[i]
    for j in range(0,len(sorted)):
      insertIndex=len(sorted)
      cur=sorted[j]
      if num<cur:
        insertIndex=j
        break
    sorted.insert(insertIndex,num)
  return sorted


# singelton 
# 装饰器
def singelton(cls):
  # every class has a instace
  instances={}
  @wraps(cls)
  def getInstance(*args, **kw):
    if cls not in instances:
      instances[cls]=cls(*args, **kw)
      return instances[cls]
  return getInstance



if __name__ == "__main__":
  # react=Reactangel(3,4)
  # area=react.getArea()
  # print("area is %s" % area)
  sortArray()


