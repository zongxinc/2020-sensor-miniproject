import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def main():
	temperature = []
	occupancy = []
	co = []
	timeInterval = []

	time = -1;
	with open('data.txt', "r") as f:
		for line in f:
			r = json.loads(line)
			room = list(r.keys())[0]
			if time == -1:
				time = datetime.fromisoformat(r[room]["time"])
			else:
				prevTime = time;
				time = datetime.fromisoformat(r[room]["time"])
				timeInterval.append((time-prevTime).total_seconds())
			if r[room]["temperature"][0] > 35:
				print("temperature anomalies: %s in %s \n" %(r[room]["temperature"][0], room))
			temperature.append(r[room]["temperature"][0])
			occupancy.append(r[room]["occupancy"][0])
			co.append(r[room]["co2"][0])
			

	tempData = pd.Series(temperature)
	print("Temperature Median: ", tempData.median())
	print("Temperature Variance: ", tempData.var())
	ax = tempData.plot.kde()
	plt.xlabel("Temperature (in Celsius)")
	plt.savefig("images/temp.png")
	plt.clf()

	occupData = pd.Series(occupancy)
	print("Occupancy Median: ", occupData.median())
	print("Occupancy Variance: ", occupData.var())
	ax = occupData.plot.kde()
	plt.xlabel("Occupancy")
	plt.savefig("images/occupancy.png")
	plt.clf()
	
	coData = pd.Series(co)
	ax = coData.plot.kde()
	plt.xlabel("CO2 Level")
	plt.savefig("images/co2.png")
	plt.clf()

	timeData = pd.Series(timeInterval)
	print("Time Median: ", timeData.mean())
	print("Time Variance: ", timeData.var())
	ax = timeData.plot.kde()
	plt.xlabel("Time (seconds)")
	plt.savefig("images/timeInterval.png")

if __name__ == "__main__":
	main()