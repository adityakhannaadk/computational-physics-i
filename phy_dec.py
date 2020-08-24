atom_choices = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Initialise the atoms with a 1/6 chance of decay 

import random


# Recursive function which takes the remaining number of atoms, applies decay and then returns the remaining number of unstable atoms.

def decay(nleft):
  atoms = [] 
  for x in range(nleft):
    atoms.append(random.choice(atom_choices))
  remaining = len(list(filter(lambda a: a != 1, atoms)))
  return remaining

# Applying the recursive function from before in a loop

def main(startnum):
  flag = True
  nleft = startnum
  nlefts = [startnum]
  while flag:
    nleft = decay(nleft)
    nlefts.append(nleft)
    print(nleft)
    if nleft == 0 or nleft < 0:
      flag = False
  return nlefts
print("simulation")
v = main(10000)
print("half life")
#print(v.index(5000))
from matplotlib import pyplot as plt
plt.plot(v)
plt.show()
