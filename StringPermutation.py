import math

class Resolution:

  # 判断是否是置换字符串
  def is_permutation(self, A, B):
    if len(A)!=len(B): return False
    if A==B: return True
    if A is B: return False
    # check if charactors count in A is equal to B
    listA=list(A)
    listB=list(B)
    setA=set(A)
    for c in setA:
      if listA.count(c) != listB.count(c):
        return False
    return True

    """给出两个字符串, 你需要修改第一个字符串，
       将所有与第二个字符串中相同的字符删除, 
       并且第二个字符串中不同的字符与第一个字符串的不同字符连接
    """
  def concatenetedString(self, s1, s2):
    list1=list(s1)
    list2=list(s2)
    sameList=[]
    for c in list1:
      if list2.count(c)>0:
        sameList.append(c)

    def remove_all(array,c):
      for x in array:
        if x==c:
          array.remove(c)

    for x in sameList:
      remove_all(list1,x)
      remove_all(list2,x)

    list1.extend(list2)
    final="".join(list1)
    return final
  
  
  """3. 判断是否为平方数之和
  """
  def checkSumOfSquareNumbers(self,num):
    if num<=0: return False
    suitNum=[]
    maxNum = math.ceil(math.sqrt(num))
    midIndex=math.ceil(maxNum/2.0)
    for i in range(midIndex):
      for j in range(midIndex,maxNum):
        if i*i+j*j==num:
          print([i,j])
          return True
    print("pair does not exists")
    return False




if __name__=="__main__":
    solver=Resolution()
    """1. 置换字符串
    """
    # isMutation=solver.is_permutation("abdkfjdksjc","abfjfjdksjc")
    # print("is mutation %s" % isMutation)
    """2. 拼接不同字符串
    """
    # s1="wksljnwdkzkmrbqwcsftgqwtlztzupyasqpzjppuphcdfjsshqlukhqytmlgaaxnwksttdtcj"
    # s2="pmiaiswrxkzbbqrfejtmgclwwpwibctdovhflxcswhueplkfcdefthnbtwemucuaxaqpavbrrpcdriwdhfzahqmyq"
    # final=solver.concatenetedString(s1, s2)
    # print("concatenetedString final is %s" % final)

    """3. 判断是否为平方数之和
    """
    solver.checkSumOfSquareNumbers(4000900)
