import math

"""CONSTANTS"""
ALLOWABLE_FLEXURAL_STRENGTH_FACTOR = 1.67
DESIGN_FLEXURAL_STRENGTH_FACTOR = 0.9

"""Functions for formulas in Chapter F of the AISC Manual"""


# Return Cb, Lateral-Torsional Buckling Modification Factor - Chapter F1
# mmax = Absolute value of maximum moment in unbraced segment
# ma = Absolute value of moment at quarter point of the unbraced segment
# mb = Absolute value of moment at centerline of the unbraced segment
# mc = Absolute value of moment at three-quarters point of the unbraced segment
def f1_cb(mmax, ma, mb, mc):
	return 12.5 * mmax / (2.5 * mmax + 3 * ma + 4 * mb + 3 * mc)


# Return Mn (Mp), Nominal Moment (Plastic Moment) Capacity - Chapter F2.1
# fy = Specified minimum yield stress of the type of steel being used
# zx = Plastic section modulus about the x-axis
def f2_yielding(fy, zx):
	return fy * zx


# Return Mn, Nominal Moment Capacity - Chapter F2.2
# lb = Length between point that are either braced against lateral displacement of the compression flange or braced
# against twist of the cross section
# lp = Limiting laterally unbraced length for the limit state of yielding
# lr = Limiting laterally unbraced length for the limit state of inelastic lateral-torsional buckling
# fy = Specified minimum yield stress of the type of steel being used
# ry = Radius of gyration about y-axis
# cb = Lateral-Torsional buckling modification factor
# e = Modulus of Elasticity
# iy = Moment of inertia about the y-axis
# cw = Warping Constant
# j = Torsional constant
# rts = Effective radius of gyration
# ho = Distance between the flange centroids
# sx = Section modulus about x-axis
# c = coefficient
# fcr = Critical stress
def f2_ltb(shape, lb, ry, fy, e, rts, cb, iy, cw, j, sx, ho):
	lp = 1.76 * ry * (e/fy) ** .5
	if shape == "w":
		c = 1
		x = j * c / (sx * ho)
		lr = 1.95 * rts * e / (.7 * fy)*(x + ((x ** 2) + 6.76 * (.7 * fy / e) ** 2) ** .5) ** .5
		fcr2 = cb * (math.pi ** 2) * e / ((lb / rts) ** 2) * (1 + .078 * x *(lb / rts) ** 2) ** .5
	elif shape == "c":
		c = ho / 2 * (iy / cw) ** .5
		x = j * c / (sx * ho)
		lr = 1.95 * rts * e / (.7 * fy) * (x + ((x ** 2) + 6.76 * (.7 * fy / e) ** 2) ** .5) ** .5
		fcr2 = cb * (math.pi ** 2) * e / ((lb / rts) ** 2) * (1 + .078 * x * (lb / rts) ** 2) ** .5
	else:
		return "Invalid check for shape"
	if lb <= lp:
		return "LTB Does Not Apply"
	elif lb > lr:
		fcr1 = cb * (math.pi ** 2) * e / ((lb / rts) ** 2)
		fcr = max(fcr1, fcr2)
		return fcr * sx


