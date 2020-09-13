# McKenna Damschroder and Zongxin Cui - 09/2020
#
# All code written for the sensor mini-project is contained in this
# file except for Task 1. Code for task 1 was added directly to client.py.
# This file includes the analysis code for finding the median/variance of
# the sensor data and graphing the probability distributions as well as 
# an algorithm for detecting anomalies in the temperature data. 

import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def main():
	temperature = []
	occupancy = []
	co = []
	timeInterval = []

	# Reading in sensor data
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
			temperature.append(r[room]["temperature"][0])
			occupancy.append(r[room]["occupancy"][0])
			co.append(r[room]["co2"][0])
		f.close()
			

	# Using Pandas series to find median, variance, and probabiltiy distribution for each set of data
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

	# Detecting temperature anomalies and printing anomalies to file
	o = open("anomalies.txt", "w")
	print("\nTemperature anomalies: ")
	with open('data.txt', "r") as f:
		for line in f:
			r = json.loads(line)
			room = list(r.keys())[0]
			if (
				r[room]["temperature"][0] > tempData.median() + 2** tempData.std()
				or r[room]["temperature"][0] < tempData.median() - 2**tempData.std()
			):
				print("%s in %s at %s" %(r[room]["temperature"][0], room, r[room]["time"]))
				o.write("%s in %s at %s\n" %(r[room]["temperature"][0], room, r[room]["time"]))
		f.close()
		o.close()

if __name__ == "__main__":
	main()