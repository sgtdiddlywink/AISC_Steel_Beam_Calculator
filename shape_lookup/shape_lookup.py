import pandas as pd


def lookup():
	while True:
		"""Import shapes database from AISC and convert to dataframe"""
		shape_db = pd.read_excel("AISC_Database/aisc-shapes-database-v15.0.xlsx", sheet_name="Database v15.0")
		shape_df = pd.DataFrame(shape_db)

		"""Set AISC_Manual_Label column as index on dataframe"""
		shape_df.set_index("AISC_Manual_Label", inplace=True)

		"""Ask user for input information on steel beam"""
		shape = input(
			"Shapes:"
			"\nW-Shape --> wXXxXXX"
			"\nM-Shape --> mXXxXX"
			"\nS-Shape --> sXXxXX"
			"\nHP-Shape --> hpXXxXXX"
			"\nChannels --> cXXxXX"
			"\nChannels --> mcXXxXX"
			"\nAngles --> lXxXxX-X/X"
			"\nWT-Shape --> wtXXxXX"
			"\nMT-Shape --> mtXXxXX"
			"\nST-Shape --> stXXxXX"
			"\nDouble Angles --> 2lXXxXXxX-X/X(LLBB/SLBB)"
			"\nHollow Structural Section (Square/Rectangular) --> hssXXxXXxX/X"
			"\nHollow Structural Section (Round) --> hssXX.XXXxX.XXX"
			"\nPipe --> pipeX-X/X(std/xs/xxs)\n"
			"What Shape would you like to Check? --> "
		).upper()

		"""Utilize .loc method to search for specific shape"""
		try:
			shape_properties = shape_df.loc[shape].to_dict()
		except KeyError:
			print("Invalid Beam Size. Try again.")
			lookup()
		else:
			break
	return shape_properties

