from shape_lookup.shape_lookup import lookup
import steel_properties as sp
import flexure.flexure_f as flexure_check

"""All user inputs should be converted to inches and kips"""

"""Call lookup function to get the starting shapes properties"""
shape_properties = lookup()
beam_length = int(input("Length of beam (ft): ")) * 12
unbraced_length = int(input("Maximum unbraced segment of beam (ft): ")) * 12


"""Check f2 flexural capacity"""
f2_yielding = flexure_check.f2_yielding(
	fy=sp.yield_stress,
	zx=shape_properties["Zx"]
)

print(f2_yielding)

"""Check f3 flexural capacity"""
f2_ltb = flexure_check.f2_ltb(
	shape=shape_properties["Type"].lower(),
	lb=unbraced_length,
	ry=shape_properties["ry"],
	fy=sp.yield_stress,
	e=sp.modulus_of_elasticity,
	rts=shape_properties["rts"],
	iy=shape_properties["Iy"],
	cw=shape_properties["Cw"],
	j=shape_properties["J"],
	sx=shape_properties["Sx"],
	ho=shape_properties["ho"],
	cb=1.14
)

print(f2_ltb)
