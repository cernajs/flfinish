from datetime import timezone 
import datetime 

def get_utc_time_stamp():
	dt = datetime.datetime.now() 
	utc_time = dt.replace(tzinfo = timezone.utc) 
	utc_timestamp = utc_time.timestamp()
	return utc_timestamp 
