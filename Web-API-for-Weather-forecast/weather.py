import pyowm
from config import API_KEY

def weather_condition(country, state):
	try:
		owm = pyowm.OWM(API_KEY)
		obs = owm.weather_at_place('{0},{1}'.format(country, state))
		w = obs.get_weather()
		wind = w.get_wind()
		temp = w.get_temperature(unit='kelvin')

		data = {
			'code':'00',
			'wind': wind['speed'],
			'temp': temp['temp']
		}

		return(data)
	except Exception as e:
		return({'code':'01','msg':str(e)})
	

country = str(input("\n Welcome to Global Weather forecast \n\nEnter your country\n"))
state = str(input("Enter your state\n"))

results = weather_condition(country,state)
if results['code']=='00':
	print("Your Current, \nWind for {2},{3} : {0} m/s\nTemperature for {2},{3}: {1}K".format(results['wind'],results['temp'],country,state))
else:
	print('Oops!'+  results['msg'])