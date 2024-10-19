# KaggleX Time Series Analysis project

Climate Time Series Analysis
---

Motivation / Problem Statement

For some time, I have been interested in learning about time series and analyzing historical weather data to identify long-term patterns. With the increasing occurrence of uncommon weather events in different regions, it has become even more important to understand how the temperature is changing over time. Have temperature variations, whether colder or hotter, influenced weather patterns over time?

Weather Datasets -
I selected these datasets because of my interest in climate data and desire to explore the intricacies of time series analysis. By leveraging these datasets, I hope to identify meaningful trends and gain an understanding of the complex factors that influence the planet's climate. For a future extension, I will incorporate both datasets below and/or find additional datasets to enrich the dataset to review temperature and weather events together.

Datasets from Kaggle
- [The Weather Dataset](https://www.kaggle.com/datasets/guillemservera/global-daily-climate-data?select=cities.csv)
- [US Weather Events (2016 - 2022)](https://www.kaggle.com/datasets/sobhanmoosavi/us-weather-events)

### Learnings / Project Tasks
Use Kaggle API for climeate/ weather data datasets

Explore/Transform data 
- explor missing values
- standarize the naming of countries across the different data sets (cities and countries)
- reviewe distribtion of quantitative data for the global weather data set
- filter the global weather data set by years that included more data
- dropp NaN values
- sort
- remove outliers
- aggregate
- reset index
- encode

Visualize data
- histogram
- scatter plot
- box plot/violin plot
- area

Research Time Series Modeling Methods and Develop Models
- Moving Average (MA)
- Autoregression (AR)
- Autoregressive Moving Average (ARMA)
- Autoregressive Integrated Moving Average (ARIMA)
- Seasonal Autoregressive Integrated Moving-Average (SARIMA)
- LSTM
- Prophet

Forecasting Accuracy Metrics
- MAE
- RMSE
- MSE
- MAPE

MVP output - Dash Application comparing the different forecasting Accuracy Metrics
