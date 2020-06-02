#!/usr/bin/env bash

#Global confirmed link
curl 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv' > CovidData/time_series_covid19_confirmed_global.csv

#US confirmed link
curl 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv' > CovidData/time_series_covid19_confirmed_US.csv

#US deaths link
curl 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv' > CovidData/time_series_covid19_deaths_US.csv

#Global death link
curl 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv' > CovidData/time_series_covid19_deaths_global.csv
