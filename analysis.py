import json
from datetime import datetime
import statistics

def main():
	temperature = []

	with open('data.txt', "r") as f:
		for line in f:
			r = json.loads(line)
			room = list(r.keys())[0]
			time = datetime.fromisoformat(r[room]["time"])
			temperature.append(r[room]["temperature"][0])

	temperature.sort()
	print(statistics.median(temperature))
	print(statistics.variance(temperature))

if __name__ == "__main__":
	main()