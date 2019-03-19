# Problem 661 -- incomplete

from math import sqrt

"""

def E(pw, pl, p):

	# result
	e = 0.0
	x = 0

	# draw
	pd = 1.0 - (pw + pl)

	# continuing / ending
	pc = 1.0 - p
	pe = p

	# first layer
	PwC = pw * pc
	PwE = pw * pe * 1.0
	PdC = pd * pc
	PdE = pd * pe * 0.0
	PlC = pl * pc
	PlE = pl * pe * 0.0
	
	e += (PwE)

	# second layer
	PwwC = PwC * pw * pc
	PwwE = PwC * pw * pe * 2.0
	PwdC = PwC * pd * pc
	PwdE = PwC * pd * pe * 1.0
	PwlC = PwC * pl * pc
	PwlE = PwC * pl * pe * 0.0
	
	PdwC = PdC * pw * pc
	PdwE = PdC * pw * pe * 1.0
	PddC = PdC * pd * pc
	PddE = PdC * pd * pe * 0.0
	PdlC = PdC * pl * pc
	PdlE = PdC * pl * pe * 0.0
	
	PlwC = PlC * pw * pc
	PlwE = PlC * pw * pe * 0.0
	PldC = PlC * pd * pc
	PldE = PlC * pd * pe * 0.0
	PllC = PlC * pl * pc
	PllE = PlC * pl * pe * 0.0

	e += (PwwE + PwdE + PdwE)
	
	# third layer
	PwwwC = PwwC * pw * pc * 3.0
	PwwwE = PwwC * pw * pe * 3.0
	PwwdC = PwwC * pd * pc * 3.0
	PwwdE = PwwC * pd * pe * 3.0
	PwwlC = PwwC * pl * pc * 3.0
	PwwlE = PwwC * pl * pe * 3.0
	PwdwC = PwdC * pw * pc * 3.0
	PwdwE = PwdC * pw * pe * 3.0
	PwddC = PwdC * pd * pc * 3.0
	PwddE = PwdC * pd * pe * 3.0
	PwdlC = PwdC * pl * pc * 2.0
	PwdlE = PwdC * pl * pe * 2.0
	PwlwC = PwlC * pw * pc * 2.0
	PwlwE = PwlC * pw * pe * 2.0
	PwldC = PwlC * pd * pc * 1.0
	PwldE = PwlC * pd * pe * 1.0
	PwllC = PwlC * pl * pc * 1.0
	PwllE = PwlC * pl * pe * 1.0

	e += (PwwwC + PwwwE + PwwdC + PwwdE + PwwlC + PwwlE + PwdwC + PwdwE + PwddC + PwddE + PwdlC + PwdlE + PwlwC + PwlwE + PwldC + PwldE + PwllC + PwllE)

	PdwwC = PdwC * pw * pc * 2.0
	PdwwE = PdwC * pw * pe * 2.0
	PdwdC = PdwC * pd * pc * 2.0
	PdwdE = PdwC * pd * pe * 2.0
	PdwlC = PdwC * pl * pc * 1.0
	PdwlE = PdwC * pl * pe * 1.0
	PddwC = PddC * pw * pc * 1.0
	PddwE = PddC * pw * pe * 1.0
	PdddC = PddC * pd * pc * 0.0
	PdddE = PddC * pd * pe * 0.0
	PddlC = PddC * pl * pc * 0.0
	PddlE = PddC * pl * pe * 0.0
	PdlwC = PdlC * pw * pc * 0.0
	PdlwE = PdlC * pw * pe * 0.0
	PdldC = PdlC * pd * pc * 0.0
	PdldE = PdlC * pd * pe * 0.0
	PdllC = PdlC * pl * pc * 0.0
	PdllE = PdlC * pl * pe * 0.0

	e += (PdwwC + PdwwE + PdwdC + PdwdE + PdwlC + PdwlE + PddwC + PddwE)

	PlwwC = PlwC * pw * pc * 1.0
	PlwwE = PlwC * pw * pe * 1.0
	PlwdC = PlwC * pd * pc * 0.0
	PlwdE = PlwC * pd * pe * 0.0
	PlwlC = PlwC * pl * pc * 0.0
	PlwlE = PlwC * pl * pe * 0.0
	PldwC = PldC * pw * pc * 0.0
	PldwE = PldC * pw * pe * 0.0
	PlddC = PldC * pd * pc * 0.0
	PlddE = PldC * pd * pe * 0.0
	PldlC = PldC * pl * pc * 0.0
	PldlE = PldC * pl * pe * 0.0
	PllwC = PllC * pw * pc * 0.0
	PllwE = PllC * pw * pe * 0.0
	PlldC = PllC * pd * pc * 0.0
	PlldE = PllC * pd * pe * 0.0
	PlllC = PllC * pl * pc * 0.0
	PlllE = PllC * pl * pe * 0.0

	e += (PlwwC + PlwwE)

	return e

def H(n):
	s = 0.0
	k = 3.0
	while k <= n:
		pa = 1.0  / sqrt(k + 3.0)
		pb = pa + (1.0 / (k ** 2))
		p = 1.0 / (k ** 3)
		e = E(pa, pb, p)
		s += e
		k += 1.0
	return s

print H(50)

"""
