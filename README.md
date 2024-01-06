# DS_Homework

## Documentation of the problem
This is an easy programming-example for the Data-Steward Certificate Course. 
The project is focusing on names of plant genera that are named after famous women. 

By providing a plant genus name as input, users of our program can research whether the plant was named after a famous woman.
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