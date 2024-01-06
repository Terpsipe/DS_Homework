# DS_Homework

## Documentation of the problem
This is an easy programming-example for the Data-Steward Certificate Course, written by Carolin Rebernig-Hedman and Annerose Tartler. The project is focusing on names of plant genera that are named after famous women. 

Plant names are traditionally given by the person who first described the plant (ditto in the case of higher taxonomic levels such as genera etc.). This practice is often used to honour individuals. This so-called epynomy is widespread in botany. The higher the taxonomic level, the more significant the naming. Women are not only in the minority in the scientific field in natural sciences, they are also significantly less likely to be used as a name model for naming new taxa. 
An international initiative of female scientists wanted to use a dataset of flowering plants to show how many and which women in the botanical field have been honoured to date for their contributions to science through epynomy. 

In our project we use this dataset (WomenPlantGenera_v1-3.csv). The aim is to enable interested users to find out whether a plant genus of interest was named after a woman, and if so, who that woman was.
The data contains, among other things:
- Genus name (all plant names at genus level)
- Epynomy (name of the woman)
- Epynomy occupation 
- Epynomy is mythical 
- Epynomy country (positive if the person is a real person)
- Year of birth
- Year of death

The programme loads the data. The user writes an input (plant genus name) and the programme first searches for the name in the data. If the name is available, the user receives a positive response, which displays the available information about the first corresponding plant genus in the list.
Furthermore, the programme filters the results according to whether the person was/is real or not. If the person was/is not real, the information consists of the name and occupation (in this case mythological figure or similar). A plot based on the result is the second output. 
In the case of a real person, the result includes the name, occupation, country of origin, date of birth and date of death. A plot is drawn based on the country of origin information.


<!---->

## Documentation of the design
<img src="Eponyms_FlowDia.png" alt="Diagram" width="200">

## Documentation of the tests
For our project we used various tests as given by the Skriptum:

*Syntax Testing* was mostly done by installing pylance's syntax highlighting. This helped prevent most incorrect spellings, missing brackets, statements or use of undeclared variables.

*Black box testing* was used by providing user input ourselves and manually checking the output with the expected outcome in the CSV. For written out testing code, more coding space would be needed.

*White box testing* was undergone thoroughly through the whole programming process by carefully considering input and output as well as reviewing the code in between coding sessions. Checks (like 'if connected_entries.empty:' in the function 'plant_information' or 'if not connected_entries.empty:' before calling 'plot_visualization()') were added to make sure the expected input data was given. If error messages were thrown throughout the programming process, error messages provided the needed guidance to correct the mistakes. The Debugger was not used, as all the problems turning up in the process were pretty straight forward. 

Due to the small amount of both, data and functionality, our code was not further tested for *performance*.


## Additional information regarding resources:
Data file in Zenodo:
https://zenodo.org/records/10038070

Publikation:
Mering S, Gardiner LM, Knapp S, Lindon H, Leachman S, Ulloa Ulloa C, Vincent S, Vorontsova MS (2023) Creating a multi-linked dynamic dataset: a case study of plant genera named for women. Biodiversity Data Journal 11: e114408. https://doi.org/10.3897/BDJ.11.e114408