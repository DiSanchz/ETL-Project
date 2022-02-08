# ETL (Extract - Transform - Load) Project 
## Project made as part of the Ironhack Data Analytics bootcamp program

This project's aim is to Extract data employing web-scrapping tools, the then transform and enrich it with further data in order to finally store it in a database and ultimately analyze the data in search for rlevant insights. 

Python was the vihecular tool for the project, but its different stages have been conducted in combination with other libraries/toola. For the web scrapping segment selenium has been the main tool employed, while the transfromation was carried out mainly with pandas library. Lastly the data was stored in the non-relational database MongoDB. The full tehc stack is detailed below.

### > The Idea

Beyond the employment of data handling and analysis tools, the purpose of this project is to inspect if there is a positive relation between the number of visitors from a given country that a region receives, and the volume of imports from that same country. In other words, inspect if an increased influx of tourists from country "b"  into region "a" will be associated with an increased demand for products from "b" in "a".

With this intention, two Spanish insular regions where the tourist sector represents a notable share of the GDP are studied: the Balearic Islands and the Canary Islands. The fact that the economies of these regions is so reliant on tourism (between a third and a half of the total gdp) makes them specially suitable for such a study as imports variation (and overall trade flows) is more closely linked with touristic activity, allowing for a relatively lower chance of a capturing phenoena out of the scope of the study (or at least that the weight of such out-of-our-scope phenomena on trade flows is smaller).

Lastly, data on foreign residents is also considered within the study besides that of visitors/tourists as these may also drive an increased demand for foreign products given that these comunities are large enough.

### > The Data

The sample is different for each region. For the Canaries it cover a time frame of 20 years (2000-2019) and 12 countries of origin while for the Balearic islands the time frame is slightly shorter (2005-2019) as well as the nummber of sampled countries (6) due to data coverage limitations.

Three different sources have provided the employed data: 

For data on Balearic Islands' number of visitors and trade flows:

- Balearic Islands Institute of Statistics [IBESTAT](https://ibestat.caib.es/ibestat/inici)

For data on Canary Islands' number of visitors and trade flows:

- Canary Institute of Statistics
[ISTAC](http://www.gobiernodecanarias.org/istac/)

For data on foreign residents in both the Canaries and the Balearic Islands:

- (Spanish) National Institute of Statistics [INE](https://www.ine.es/)

The data is obtained in two different formats from the sources cited above. A part of the data has been scrapped from the sources' webapges, while another part has been directly downloaded and imported as .csv or .xlsx files. 

(Note: though csv was the preferred format for non-scrapped data, some necessary datasets were only available in xlsx format and thus they had to be employed as such)

### > Summary

The analisys segment of the project is currently unfinished, all relevant findings will be posted and summarized in this section.

### > Selected Technology Stack:

- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Selenium](https://www.selenium.dev/)
- [MongoDB](https://www.mongodb.com/es/)
- [Seaborn](https://seaborn.pydata.org/)

### > About this repository

The current rpository has been thought as an independet unit where all the elements of the project are contained. Scrapping code is divided for each region (CI - Canary Islands / BI - Balearic Islands) and offered in two different formats (.py and .ipynb). The "Cleaning + Enriching + Loading.ipynb" file contains the processes that its title describes, the cleaning of the employed datasets, their erichment by aggregation and the final loading to MongoDB.

The "Data" folder contains all the non-scrapped employed data plus other files and directories which are necessary for the proper functioning of the code. Finally, the "src" directory contained in the repository includes a .py file from where some functions employed during the project are defined and imported.

    