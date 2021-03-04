Download and clean USGS streamflow data
=======================================

Documentation for the script ``_1_acquire_streamflow_data.py``

Acquisition of streamflow data from the USGS National Water Information System. This script is mostly a wrapper for the climata USGS data acquision tool. 
It implements that code, downloads and pickles data for user-defined time periods and gauging stations. 

**Example:**::


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
			for series in self.get_data(): #this iterates through the stations you query in get_data()
				flow = [r[1] for r in series.data]
				dates = [r[0] for r in series.data] #.strftime('%y-%m-%d') make datetime objects into strings if you want 

				output = dict(zip(dates,flow)) #zip these two lists into a dict that looks like {date:flow} for the full time period for one station
			return output 

This can be instantiated with args like: ::

	start_date = '2018-10-01'
	end_date = '2020-09-30'
	station_id = str(df['STAID'].iloc[0])#"06730200"
	param_id = "00060" #this is discharge in cuft/s one day average