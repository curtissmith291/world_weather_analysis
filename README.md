# world_weather_analysis

This module challenge required obtaining a list of random cities, filtering based on temperature desires, finding the routes between four cities that meet the aforementioned temperature desires. 

This project differs slightely from the starter code/instructions in that all the randomly determined latitude/longitude coordinates were on land before being added to the dataframe using the global-land-mask module by Todd Karin. As Earth is mostly water, random coordinates from which the closest city is determined will thus tend to favor coastal/island cities, and therefore, are not a truly represantative of random locations of cities. Checking that the coordinates are on land helps to ensure that the selection is more representative. 

Citation:
Karin, Todd. Global Land Mask. October 5, 2020. https://doi.org/10.5281/zenodo.4066722
