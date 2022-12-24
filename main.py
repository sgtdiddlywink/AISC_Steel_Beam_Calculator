from shape_lookup.shape_lookup import lookup
import steel_properties as sp
import flexure.flexure_f as flexure_check

"""All user inputs should be converted to inches and kips"""

"""Ask user what they want to do"""
user_input = input("What design do you want to check? (Beam, Column, Tension)\n").lower()

"""Call lookup function to get the starting shapes properties"""
shape_properties = lookup()
shape = shape_properties["Type"]

if user_input == "beam":
	axis = input("Is bending about major axis? (Y/N)").lower()
	beam_length = int(input("Length of beam (ft): ")) * 12
	unbraced_length = int(input("Maximum unbraced segment of beam (ft): ")) * 12

	if axis == "y":  # Specifies bending about major axis
		if shape == "W" or shape == "S" or shape == "M" or shape == "C" or shape == "MC":
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

# TODO add an exception for the shapes called out in the "user note" in section F2 for shapes with non-compact flanges
# This is an F3 check
