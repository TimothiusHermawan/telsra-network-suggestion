# Telsra Network Suggestion

Telsra Challenge on kaggle

## Background

Telstra is on a journey to enhance the customer experience - ensuring everyone in the company is putting customers first. In terms of its expansive network, this means continuously advancing how it predicts the scope and timing of service disruptions. Telstra wants to see how you would help it drive customer advocacy by developing a more advanced predictive model for service disruptions and to help it better serve its customers.In the end, we also project the prediction result into australian base station map to see which location that needed maintenance the most

## Getting Started

This program uses the following programs to run:
 * [Jupyter Notebook](https://jupyter.org/)
 * [Dash](Dash.plot.ly)
 * [Python](https://www.python.org/downloads/)
 
 ## Data Description
 
The goal of the problem is to predict Telstra network's fault severity at a time at a particular location based on the log data available. Each row in the main dataset (train.csv, test.csv) represents a location and a time point. They are identified by the "id" column, which is the key "id" used in other data files.

Fault severity has 3 categories: 0,1,2 (0 meaning No Fault, 1 meaning only A Few Faults, and 2 meaning Many Faults). 

Different types of features are extracted from log files and other sources: event_type.csv, log_feature.csv, resource_type.csv, severity_type.csv.

Also, we included base station map latitude and longitude in autralian so the prediction can be plotted to the map.

#### Note: 
“severity_type” is a feature extracted from the log files (in severity_type.csv). Often this is a severity type of a warning message coming from the log. "severity_type" is categorical. It does not have an ordering. “fault_severity” is a measurement of actual reported faults from users of the network and is the target variable (in train.csv).
 
 ## Layout
 
 ![alt text](/Media/Layout1.png)
 
 ![alt text](/Media/Layout2.png)
