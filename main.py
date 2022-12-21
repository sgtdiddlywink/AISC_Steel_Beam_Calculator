import pandas
import pandas as pd

"""Currently this only works for simply supported wide flange beams with a uniform load on their strong axis.
This utilizes ASD. 
This is based on the 14th Ed. AISC with the 15th Ed. database.
Assumes fully braced beam.
"""

# TODO LIST
# TODO create functions for each section limit check to make this way easier
# TODO add option for LRFD
# TODO add other shapes besides wide flange
# TODO add option for other type of supported beams
# TODO add option for other type of loading scenarios
# TODO include function for calculating Cb
# TODO add option to specify material properties
# TODO add options for changing allowable deflection limits
# TODO add options for changing braced length of beam

# CONSTANTS
MODULUS_ELASTICITY = 29000  # ksi
YIELD_STRESS = 50  # ksi
TENSILE_STRESS = 65  # ksi
DEFLECTION_LIMIT = 240

# Lateral Torsional Buckling Factor
Cb = 1.14

"""Import shapes database from AISC and convert to dataframe"""
shape_db = pd.read_excel("AISC_Database/aisc-shapes-database-v15.0.xlsx", sheet_name="Database v15.0")
shape_df = pandas.DataFrame(shape_db)

"""Set AISC_Manual_Label column as index on dataframe"""
shape_df.set_index("AISC_Manual_Label", inplace=True)

"""Utilize .loc method to search for specific shape"""
result = shape_df.loc["W44X335"]

"""Look up and assign values for each column of that table"""
print(result["Type"])

# # User Input
# beam_length = int(input("Length of beam in feet: ")) * 12  # Length of beam in inches
# trib_width = int(input("Beam tributary width in feet: ")) * 12  # Tributary width in inches
# unfactored_total_loads = int(input("Total unfactored loads in pounds per square feet: ")) / (1000 * 144)  # Unfactored total loads in kips per square inch
#
# # Beam Information
# print("\nBEAM INFORMATION")
# print(f"Beam length = {beam_length} inches")
# print(f"Tributary width = {trib_width} inches")
# print(f"Unfactored total loads = {unfactored_total_loads} kips/in2")
#
# # Calculate maximum applied forces on beam
# tributary_load = trib_width * unfactored_total_loads  # kip per in
# max_moment = (tributary_load * beam_length ** 2 / 8)  # kip-in
# max_shear = (tributary_load * beam_length / 2)  # kip
# max_deflection = beam_length / DEFLECTION_LIMIT  # in
#
# # AISC Limit Checks
# # F2.1 Yielding
# minimum_plastic_section_modulus = max_moment / YIELD_STRESS  # in3
#
# # F2.2 Lateral_Torsional Buckling
# # TODO right now it assumes a fully braced beam
#
# # Calculate minimum moment of inertia of beam needed to meet deflection criteria
# minimum_moment_of_inertia = 5 * tributary_load * beam_length ** 4 / (384 * MODULUS_ELASTICITY * max_deflection)  # in4



