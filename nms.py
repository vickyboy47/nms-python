import numpy as np
from numpy import *

# boxes is a list of size (n x 5)
# trial is a numpy array of size (n x 5)
# Author: Vicky

def nms (boxes,overlap):
  if not boxes:
		pick = []
	else:
		trial = zeros((len(boxes),5),dtype=float64)
		trial[:] = boxes[:]
		x1 = trial[:,0]
		y1 = trial[:,1]
		x2 = trial[:,2]
		y2 = trial[:,3]
		score = trial[:,4]
		area = (x2-x1+1)*(y2-y1+1)
	
		#vals = sort(score)
		I = argsort(score)
		pick = []
		count = 1
		while (I.size!=0):
			#print "Iteration:",count
			last = I.size
			i = I[last-1]
			pick.append(i)
			suppress = [last-1]
			for pos in range(last-1):
				j = I[pos]
				xx1 = max(x1[i],x1[j])
				yy1 = max(y1[i],y1[j])
				xx2 = min(x2[i],x2[j])
				yy2 = min(y2[i],y2[j])
				w = xx2-xx1+1
				h = yy2-yy1+1
				if (w>0 and h>0):
					o = w*h/area[j]
					print "Overlap is",o
					if (o >overlap):
						suppress.append(pos)
			I = delete(I,suppress)
			count = count + 1
	return pick
