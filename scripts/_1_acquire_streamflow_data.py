import matplotlib
import matplotlib.pyplot as plt
from climata.usgs import DailyValueIO
from pandas.plotting import register_matplotlib_converters
import numpy as np
import pandas as pd 
import datetime 
import geopandas as gpd 
register_matplotlib_converters()


class get_streamflow_data(): 

	def __init__(self,station_id,start_date='1980-10-01',end_date='2020-09-30',param_id='00060'): 
		self.start_date=start_date
		self.end_date=end_date
		self.station_id=station_id
		self.param_id=param_id

	def get_data(self): 
		print(start_date)
		print(end_date)
		#datelist = pd.date_range(end=datetime.datetime.today(), periods=ndays).tolist()
		data = DailyValueIO(
		    start_date=start_date,#datelist[0],
		    end_date=end_date,#datelist[-1],
		    station=station_id,
		    parameter=param_id,
		)
		return data 

	def clean_data(self): 
		# create lists of date-flow values
		count = 0 
		for series in self.get_data(): #this iterates through the stations you query in get_data()
			flow = [r[1] for r in series.data]
			dates = [r[0] for r in series.data] #.strftime('%y-%m-%d') make datetime objects into strings if you want 

			output = dict(zip(dates,flow)) #zip these two lists into a dict that looks like {date:flow} for the full time period for one station
		#print(output)
		return output 


def get_streamflow_gage_ids(input_file): 
	"""Read in a csv or shapefile of gage locations."""
	if input_file.endswith('csv'): 
		df = pd.read_csv(input_file)

	elif input_file.endswith('shp'): 
		df = gpd.read_file(input_file)
	return df 


df = get_streamflow_gage_ids("/vol/v1/general_files/user_files/ben/chapter_3/streamflow_data/shapefiles/gagesII_9322_sept30_2011.shp")
print(df.columns)
#df = df[df['STAID'].astype('str')==In [14]: s.loc[s.str.startswith('a', na=False)]
df = df.loc[df['STATE'].isin(['OR','ID','WA'])]

print(df)

def main(start_date,end_date,station_id,param_id): 
	data=get_streamflow_data(start_date,end_date,station_id,param_id).clean_data()
	
if __name__ == '__main__':
    
	# set parameters
	start_date = '2018-10-01'
	end_date = '2020-09-30'
	station_id = str(df['STAID'].iloc[0])#"06730200"
	param_id = "00060" #this is discharge in cuft/s one day average 
	main(start_date,end_date,station_id,param_id) #call the functions and/or instantiate the class
