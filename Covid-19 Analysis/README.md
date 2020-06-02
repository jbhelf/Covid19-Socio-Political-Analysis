# Covid-19 Response: Socio-Political Analysis

## Brief overview:

Provided in this directory is an analysis of Covid-19 data to determine the impact that three political metrics had in the response to the Covid-19 outbreak.

## In this folder you will find:
**Plots**: 
- A folder with the results of plotting data with various political metrics as filters

**CovidData**: 
- A folder with data used as political metrics for comparison

**updateFiles.sh**: 
- A shell file to pull the most recent data on Covid-19 confirmed cases and deaths

**Python Files**:
- main: Coordinates all actions for analysis
- assignDict: Manipulates data for the purposes of creating, modifying, and categorizing country-indexed dictionaries
- detResponse: Performs a regression analysis on a given data set
- plotByCat: Plots dictionaries based on their categorizations
- readFiles: Reads files from CovidData folder

### Data Sources:
- Covid-19 Data (files kept with same names): https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
- World Population Data: https://population.un.org/wpp/Download/Standard/CSV/
- Human Development Data (HDI): http://hdr.undp.org/en/data#
- Press Freedom Index (PFI): https://tcdata360.worldbank.org/indicators/h3f86901f?indicator=32416&viz=line_chart&years=2001,2019
- Education Level Data (Mean Years of Schooling): http://data.uis.unesco.org/index.aspx?queryid=242
