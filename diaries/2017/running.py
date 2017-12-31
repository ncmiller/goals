from datetime import datetime, timedelta
import math

# How long will it take to run a 5K with a certain treadmill speed
def time_for_5k(mph):
  secs = ((mph/3.107)**-1)*3600.0
  return datetime.fromtimestamp(secs).strftime('%M:%S')


# What should the treadmill speed be to run a 5k in a certain time
def mph_for_5k_time(mins, secs):
  td = timedelta(minutes=mins, seconds=secs)
  total_seconds = td.total_seconds()
  mph = ((total_seconds/3600.0)/3.107)**-1

  # Only keep one decimal place, and always round up
  return math.ceil(mph*10.0)/10.0
