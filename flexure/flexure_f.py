import math

"""CONSTANTS"""
ALLOWABLE_FLEXURAL_STRENGTH_FACTOR = 1.67
DESIGN_FLEXURAL_STRENGTH_FACTOR = 0.9

"""Functions for formulas in Chapter F of the AISC Manual"""


def f1_cb(mmax, ma, mb, mc):
	"""
	:param mmax: Absolute value of maximum moment in unbraced segment
	:param ma: Absolute value of moment at quarter point of the unbraced segment
	:param mb: Absolute value of moment at centerline of the unbraced segment
	:param mc: Absolute value of moment at three-quarters point of the unbraced segment
	:return: Cb, Lateral-Torsional Buckling Modification Factor - Chapter F1
	"""
	return 12.5 * mmax / (2.5 * mmax + 3 * ma + 4 * mb + 3 * mc)


def f2_yielding(fy, zx):
	"""
	:param fy: Specified minimum yield stress of the type of steel being used
	:param zx: Plastic section modulus about the x-axis
	:return: Mn (Mp), Nominal Moment (Plastic Moment) Capacity - Chapter F2.1
	"""
	return {
		"Ultimate_Moment_Capacity": round(fy * zx * DESIGN_FLEXURAL_STRENGTH_FACTOR),
		"Allowable_Moment_Capacity": round(fy * zx / ALLOWABLE_FLEXURAL_STRENGTH_FACTOR)
	}


def f2_ltb(shape, lb, ry, fy, e, rts, iy, cw, j, sx, ho, cb=1):
	"""
	:param shape: The shape of the beam (w, c, hss, l, etc.)
	:param lb: Length between point that are either braced against lateral displacement of the compression flange or
	braced against twist of the cross-section
	:param ry: Radius of gyration about y-axis
	:param fy: Specified minimum yield stress of the type of steel being used
	:param e: Modulus of Elasticity
	:param rts: Effective radius of gyration
	:param cb: Lateral-Torsional buckling modification factor
	:param iy: Moment of inertia about the y-axis
	:param cw: Warping Constant
	:param j: Torsional constant
	:param sx: Section modulus about x-axis
	:param ho: Distance between the flange centroids
	:return: Mn, Nominal Moment Capacity - Chapter F2.2
	"""
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
		return {
			"Ultimate_Moment_Capacity": round(fcr * sx * DESIGN_FLEXURAL_STRENGTH_FACTOR),
			"Allowable_Moment_Capacity": round(fcr * sx / ALLOWABLE_FLEXURAL_STRENGTH_FACTOR)
		}
