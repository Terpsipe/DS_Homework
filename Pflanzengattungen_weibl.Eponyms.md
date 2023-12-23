Input file: WomenPlantGenera_v1-3.csv (https://zenodo.org/records/10038070)
Liste von Pfalnzengattungen, die nach Frauen benannt wurden (oft Frauen, die eine Rolle in der Wissenschaft gespielt haben) plus Information ueber diese Frauen


•	Input: Importieren einer Liste von Pflanzengattungen
# Test hierzu evtl.: Gibt es eine Liste, die importiert wird? Gibt es Null values
# Muss noch geschrieben werden

Output – Array mit Namen der Gattung + des weiblichen eponyms
2 Werte pro Spalte: 
1.	gesuchte Kategorie = Wert (ob Person und wenn ja wer)
2.	Schlüssel: Pflanzengattung 

•	Test:
Falls Kategorie nicht gegeben ist (anhängen csv. File nicht geladen) = Kein Input file gefunden
Negativ output = Text (”Das gesucht Taxon wurde leider nicht gefunden. Der Name scheint noch nicht vergeben zu sein – gehen sie gerne raus und benennen sie eine noch unentdeckte Pflanze!”)
# Funktion für die Eingabeverarbeitung (also für die Kategorie)
# Tests hier: gibt es einen Input? Existiert die Kategorie?

1.	Funktion = Import der Array liste (.csv)
Import random (= LIBRARY; random nr. zwischen 0 und 1, damit man später eine beliebige Pflanze hat; Abfrage nicht nacheinander sonder man muss so weiter gehen, damit wir bei der Pflanze sind, die durch die random Nummer kompiliert wurde = LOOP)

2.	Funktion
Aus array liste von function 1 wird eine Frage gestellt:
Computer sendet an das terminal einen text mit einem Pflanzennamen: “Wurde dieses Pflanzentaxon nach einer Frau benannt (ein Pflanzengattung aus der Liste)?”

-	Input kommt
-	Person muss etwas schreiben (extra Funktion?) ->Funktion schreibt Kategorie
-	Output true or false (Satz; DECISION – wenn der Pflanzenname in der Liste  ist 
-	Richtig – diese Pflanzengattung wurde nach blablabla benannt”; 
Falsch – (”Das gesucht Taxon wurde leider nicht gefunden. Der Name scheint noch nicht vergeben zu sein – gehen sie gerne raus und benennen sie eine noch unentdeckte Pflanze!”)
-	DIAGRAM = Anzahl der Arten in der Liste
-	One function with an interface – Person gibt eine Frage ein = INTERFACE
Datenanalyse – richtig – wurde nach einer Frau benannt (Name) UND es gibt eventuell noch andere Gattungen in der Liste, die nach dieser Frau benannt wurden?)

# Nimmt einen Gattungsnamen aus der Liste und erfragt die Kategorie (= das eponym)
# Randomnumber zur Auswahl einer Array-Stelle; der Pflanzenname dort wird ausgegeben mit der Frage, zu welcher Kategorie das gehört
# Ausgabe am Ende: Text (mit Entscheidung, ob Eingabe richtig war); Diagramm/Infos zur Person, die hinter dem eponym steht


Data file in Zenodo:
https://zenodo.org/records/10038070
Publikation:
Mering S, Gardiner LM, Knapp S, Lindon H, Leachman S, Ulloa Ulloa C, Vincent S, Vorontsova MS (2023) Creating a multi-linked dynamic dataset: a case study of plant genera named for women. Biodiversity Data Journal 11: e114408. https://doi.org/10.3897/BDJ.11.e114408