# Sensor Mini-Project 

Authors: McKenna Damschroder and Zongxin Cui

Date: 9/14/2020

## Responses

### Task 0:

What is the greeting string issued by the server to the client upon first connecting?

 - "ECE Senior Capstone IoT simulator""

### Task 1:

In this task, code was added to [src/sp_iotsim/client.py](https://github.com/zongxinc/2020-sensor-miniproject/blob/main/src/sp_iotsim/client.py) to save the JSON sensor data to a text file as it comes in. The resulting text file is named [data.txt](https://github.com/zongxinc/2020-sensor-miniproject/blob/main/data.txt).

### Task 2:

In this task, the Pandas library was used to do numerical analysis on the data set from Task 1. All analysis code can be found in [analysis.py](https://github.com/zongxinc/2020-sensor-miniproject/blob/main/analysis.py). The first three questions answered below involved analyzing sensor data for a specific room. The room that we chose to examine is the office.

1. What are the median and variance observed from the temperature data (in Celsius)? 

 - Median: 23.018693542662476
 - Variance: 9.790063333923133

2. What are the median and variance observed from the occupancy data?

 - Median: 2.0
 - Variance: 2.2173377088504274

3. Plot the probability density functions for each sensor type.

Below are the graphed probability density functions. Once again, this is solely for data taken from the office sensors. The plots below were created using Pandas's kde() function. This function generates Kernel Density Estimate (KDE) plots using Gaussian kernels. A KDE is a way, in statistics, to estimate the probability density function. We also have created histogram plots for each data set and they can be found in the [images](https://github.com/zongxinc/2020-sensor-miniproject/tree/main/images) folder. 

<img src="./images/temp.png" alt="Temperature PDF" width="40%" height="40%" />

<img src="./images/occupancy.png" alt="Occupancy PDF" width="40%" height="40%" />

<img src="./images/co2.png" alt="CO2 PDF" width="40%" height="40%" />

4. What is the mean and variance of the time interval of the sensor readings (in seconds)? Plot its probability density function. 

 - Mean: 1.0368927617675312
 - Variance: 1.0847226416405662
 
Below is the PDF for the time interval of the sensor readings. A histogram of this data can be found in the [images](https://github.com/zongxinc/2020-sensor-miniproject/tree/main/images) folder.

<img src="./images/timeInterval.png" alt="Time Interval PDF" width="40%" height="40%" />

Does it mimic a well-known distribution for connection intervals in large systems?

Yes, this mimics what the distribution would look like for connection intervals in large systems. The majority of the time intervals fall in a narrow strip of small values. In our data, this would be in the 0-1 second range. Connections and messages would probably be expected to occur in this interval range. However, it is impossible for the data to be sent and received at an exact consistent time. For instance, if a server has many distinct clients, as is possible with our simulation, the nature of scheduling tasks might make it that some messages take longer for the server to send and/or the client to receive. Our time interval distribution may have more points deviated from the median than in actual systems, but in general, its shape mimics that of a well-known distribution.

### Task 3:

In order to detect enomalies in temperature sensor data, we implemented an algorithm that checks if a temperature data point is further than 2 standard deviations away from the mean. To be consistent with Task 2, we implemented this only looking at the temperature data from the office sensor. Our code for this task can be found in [analysis.py](https://github.com/zongxinc/2020-sensor-miniproject/blob/main/analysis.py). The anomalies detected in our data set using this algorithm can be found in [anomalies.txt](https://github.com/zongxinc/2020-sensor-miniproject/blob/main/anomalies.txt).

1. Find the percent of "bad" data points and determine the temperature median and variance with these bad data points discarded. Do this for the same room used in Task 2 (the office).

The percentage of all points that are bad points is: 0.01729106628242075.

The new median and variance with the bad points removed are:

- Median: 23.019330104257943
- Variance: 1.0823557009382205

2. Does a persistent change in temperature	always indicate a failed sensor?

A persistent change in temperature doesn't necessarily indicate a failed sensor. The sensor being faulty depends on the actual temperature reading obtained. If a persistent change occurs, and the sensor no longer gives readings in a range one could expect for its location, that is when one can assume a failed sensor. Outside factors must be taken into consideration when setting these parameters to avoid false negatives.

3. What are possible bounds on temperature for each room type?

When deciding on temperature bounds for each room type, one must consider the normal expected temperatures for these locations, but also low-probability scenarios like broken heating or AC systems. Below are possible bounds for each room:

- Lab: 13 - 30 degrees Celsius
- Class: 15 - 30 degrees Celsius
- Office: 16 - 32 degrees Celsius 

### Task 4:

How is this simulation reflective of the real world?
How is this simulation deficient? What factors does it fail to account for?
How is the difficulty of initially using this Python websockets library as compared to a compiled language e.g. C++ websockets?
Would it be better to have the server poll the sensors, or the sensors reach out to the server when they have data?

In this exercise, we utilized a 

