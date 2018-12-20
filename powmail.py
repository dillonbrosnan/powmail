import forecastio
import config
from datetime import date, timedelta

api_key = config.api_key

lat = 39.1970
lng = 120.2357

squawForecast = forecastio.load_forecast (api_key, lat, lng )

byDay = squawForecast.daily()
print byDay.summary
# print byDay.icon

for dailyData in byDay.data:
  print dailyData.precipType
  break