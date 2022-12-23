import pandas as pd


def lookup():
	while True:
		"""Import shapes database from AISC and convert to dataframe"""
		shape_db = pd.read_excel("AISC_Database/aisc-shapes-database-v15.0.xlsx", sheet_name="Database v15.0")
		shape_df = pd.DataFrame(shape_db)

		"""Set AISC_Manual_Label column as index on dataframe"""
		shape_df.set_index("AISC_Manual_Label", inplace=True)

		"""Ask user for input information on steel beam"""
		shape = input("Beam Size (wXXxXXX): ").upper()
		"""Utilize .loc method to search for specific shape"""
		try:
			shape_properties = shape_df.loc[shape].to_dict()
		except KeyError:
			print("Invalid Beam Size. Try again.")
		else:
			break
	return shape_properties

