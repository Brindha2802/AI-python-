import math
l=[]
MAX, MIN=1000,-1000
def minimax(cur_depth,node_index,max_turn,scores,target_depth,b_factor,alpha, beta):
    if cur_depth==target_depth:
        return scores[node_index]
    if (max_turn):

        largest=None
        for i in range(b_factor):
            index= node_index*b_factor+i
            if index>=len(scores):
                continue
            cur=minimax(cur_depth+1,index,False,scores,target_depth,b_factor, alpha, beta)
            if largest==None or cur>largest:
                largest =cur
            alpha=max(alpha, largest)
            l.append(cur)
            if beta<=alpha:
              break
        return (largest)
    else:
        smallest=None
        for i in range(b_factor):
            index = node_index*b_factor +i
            if index>=len(scores):
                continue
            cur = minimax(cur_depth+1,index,True,scores,target_depth,b_factor, alpha, beta)
            if smallest==None or cur<smallest:
                smallest=cur
            beta=min(beta,smallest)
            l.append(cur)
            if beta<=alpha:
              break
        return (smallest)

scores=[int(s)for s in input("Enter the scores:").split()]
b_factor=int(input("enter the branching factor:",))
player=int(input("maximizer or minimizer?(Enter 1 for maximizer and 0 for minimizer):"))
tree_depth=math.ceil(math.log(len(scores),b_factor))
print("the optimal value is:",end="")
print(minimax(0,0,player,scores,tree_depth,b_factor,MIN,MAX))

diff=[]

for i in scores:
  if i not in l:
    diff.append(i)

if not diff:
  print("No nodes were pruned")
else:
  print("Pruned nodes are:")
  for i in diff:
    print(i, sep = '')
