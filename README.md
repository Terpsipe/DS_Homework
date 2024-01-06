# DS_Homework

## Documentation of the problem
This is an easy programming-example for the Data-Steward Certificate Course. 
The project is focusing on names of plant genera that are named after famous women. 

Pflanzennamen werden traditionell von jener Person vergeben, die die Pflanze zuerst beschrieben hat (dito im Fall von höherliegenden taxonomischen Ebenen wie Gattungen usw.). Nicht selten wird diese Praxis dazu verwendet, um Personen zu ehren. Diese sogenannte Epynomy ist in der Botanik weit verbreitet. Je höher die taxonomische Ebene desto bedeutender die Namensgebung. Frauen sind nicht nur im wissenschaftlichen Bereich in den Naturwissenschaften in der Minderzahl, sie werden auch bedeutend seltener als Namensvorbild zur Benennung neuer Taxa herangezogen. 
Eine internationale Inititaive von Wissenschaftlerinnen wollte anhand eines Datensets von Bluetenpflazen aufzeigen, wieviel und welche Frauen im botanischen Bereich fuer ihre Beiträge zur Wissenschaft durch Epynomy bis dato geehrt wurden. 

In unserem Projekt verwenden wir dieses Datenset (WomenPlantGenera_v1-3.csv). Das Ziel ist es, es interessierten Benutzerinnen zu ermöglichen herauszufinden, ob eine gesuchte Pflanzengattung nach einer Frau benannt wurde, und wenn ja, wer diese Frau war.
Die Daten enthalten unter anderem:
-	Genus name (alle Pflanzennamen am Genus level)
-	Epynomy (Name der Frau)
-	Epynomy occupation 
-	Epynomy is mythical 
-	Epynomy country (positiv, wenn es sich bei der Person um eine reale Person handelt)
-	Year of birth
-	Year of death

Das Program lädt die Daten. Der user schreibt einen Input (Pflanzennamen) und das Program sucht zuerst nach dem gesuchten Namen in den Daten. Wenn der Name vorhanden ist bekommt die Anwenderin eine positive Rueckmeldung in der die Information ueber die erste entsprechende Pflanzengattung in der Liste ausgegeben wird.
Des weiteren filtert das Program die Ergebnisse je nachdem ob es sich um eine reale Person handelt oder nicht. War/ist die Person nicht real besteht die Information aus dem Namen und dem Beruf (in dem Fall mythologische Figur o.Ä.). Ein Plot basierend auf dem Ergebnis wird ausgegeben. 
Im Falle einer realen Person beinhaltet das Ergebnis den Namen, den Beruf, das Herkunftsland, das Geburts- und Sterbedatum. Ein Plot wird gezeichnet basierend auf der Infromation zum Herkunftsland.

Data file in Zenodo:
https://zenodo.org/records/10038070
Publikation:
Mering S, Gardiner LM, Knapp S, Lindon H, Leachman S, Ulloa Ulloa C, Vincent S, Vorontsova MS (2023) Creating a multi-linked dynamic dataset: a case study of plant genera named for women. Biodiversity Data Journal 11: e114408

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