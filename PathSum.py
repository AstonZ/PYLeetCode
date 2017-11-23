
class TreeNode:
  def __init__(self,val):
    self.val=val
    self.left, self.right = None, None

class Solution:
  """
  二叉树的路径和 {1,2,4,2,3} 总和是 5 的所有路径
  """
  allPath=[]
  def binaryTreePathSum(self, root, target):
    if root is None: return None
    self.recuitPath(root,[root.val])
    desPaths=[]
    print("get all paths = %s" % self.allPath)
    for path in self.allPath:
      if sum(path)==target:
        desPaths.append(path)
    return desPaths

  def recuitPath(self, node, halfPath):
    if node is None:
      return halfPath
    if node.left:
      leftPath=halfPath.copy()
      leftPath.append(node.left.val)
      self.recuitPath(node.left, leftPath)
    if node.right:
      rightPath=halfPath.copy()
      rightPath.append(node.right.val)
      self.recuitPath(node.right, rightPath)
    if node.left is None or node.right is None:
      self.allPath.append(halfPath)

if __name__=="__main__":    
    rootNode = TreeNode(1)
    node11=TreeNode(2)
    node12=TreeNode(4)
    rootNode.left=node11
    rootNode.right=node12

    node21=TreeNode(2)
    node22=TreeNode(3)
    node11.left=node21
    node11.right=node22

    solution=Solution()
    pathList=solution.binaryTreePathSum(rootNode,5)
    print(pathList)