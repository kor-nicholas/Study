# pip install shedule requests

import shedule
import requests

def test_func():
	print('test_func')

def main():
	shedule.every(4).seconds.do(test_func) # run test_func every 4 seconds
	shedule.every(5).minutes.do(test_func) # run test_func every 5 minutes
	shedule.every().hour.do(test_func) # run test_func every 4 seconds

	shedule.every().day.at('21:45').do(test_func) # run test_func every day at 21:45
	shedule.every().friday.do(test_func) # run test_func every friday
	shedule.every().thursday.at('22:30').do(test_func) # run test_func every thursday at 22:30

if __name__ == '__main__':
	main()