import pandas as pd
import matplotlib.pyplot as plt

### Data File Preparation
# reads the data file and stores it in the variable "raw_data"
raw_data = pd.read_csv('WomenPlantGenera_v1-3.csv')

# stores just the rows we want: [id, genus-name (name to be searched by), genus-wfo-status (Accepted, Unplaced, Synonym for XY), family-name-wfo (plant family name), eponymy-name (named after whom), eponymy-yob (birthyear of person), eponymy-yod (deathyear of person), eponomy-occupation, eponymy-is-real, eponymy-country]
selected_data = raw_data[['id', 'genus-name', 'genus-wfo-status', 'family-name-wfo', 'eponymy-name', 'eponymy-yob', 'eponymy-yod', 'eponymy-occupation', 'eponymy-is-real', 'eponymy-country']]

# gets the user input
plant_name = input('Please enter the plant name you want to check: ')

# gives out a series of all the entries that have plant_name as genus-name
connected_entries = selected_data[selected_data['genus-name']==plant_name]

def plant_information(plant_name):
    if connected_entries.empty:
        print(f'The plant name "{plant_name}" does not exist in the selected data.')
    else:
        print(exist_information(plant_name))
       
# returns more information about the plant the user was searching for
def exist_information(plant_name):
    string = str(f'The plant name "{plant_name}" exists in the selected data. It has {len(connected_entries)} results: \n') + combined_eponomy_information() + combined_exist_informations()
    return string

def combined_eponomy_information():
    if len(connected_entries) == 1:
        return eponomy_information()
    elif (connected_entries['genus-name'].nunique()==1 and connected_entries['eponymy-yob'].nunique()==1): # Hier könnte man auch alle einzelnen angeben, wenns uns freut
        return eponomy_information()
    else:
        return 'The different plants come from different women with the same name. To the first woman in the list, the following information is aviable: ' + eponomy_information() # Mögliche Erweiterung: tatsächlich einzeln nennen
    
def eponomy_information():
    string = f'The flowers namesake is {connected_entries["eponymy-name"].iloc[0]}. She ' + reality_information()
    return string

def reality_information():
    if connected_entries['eponymy-is-real'].iloc[0]:
        return f'was a {connected_entries["eponymy-occupation"].iloc[0]} and lived from {connected_entries["eponymy-yob"].iloc[0]} to {connected_entries["eponymy-yod"].iloc[0]} in {connected_entries["eponymy-country"].iloc[0]}. \n'
    else:
        return f'is a {connected_entries["eponymy-occupation"].iloc[0]}. \n'

# sends the individual rows to indiv_exist_information(row_data) in order to be processed 
def combined_exist_informations():
    individual_rows = []
    
    for i, (index, row) in enumerate(connected_entries.iterrows(), start = 1):
        row_info = indiv_exist_information(row, i)
        individual_rows.append(row_info)
    
    string = '\n'.join(individual_rows)
    
    return string

# evtl mit nummerierung durchschicken?
def indiv_exist_information(row_data, number):
    string = f'Entry number {number} belongs to the wfo-family of the {row_data["family-name-wfo"]}. Its wfo-Status is: {row_data["genus-wfo-status"]}'
    return string

def plot_visualization():
    if connected_entries['eponymy-is-real'].iloc[0]:
        plot_country_visualization()
    else:
        plot_category_visualization()

def plot_country_visualization(): # not exactly the plot we want to include, this needs way more looping etc => change
    country_counts = connected_entries['eponymy-country'].value_counts()
    country_counts.plot(kind='bar', color='skyblue')
    plt.title('Plants Named After Real People - Country Visualization')
    plt.xlabel('Country')
    plt.ylabel('Number of Plants')
    plt.show()

def plot_category_visualization(): # not exactly the plot we want to include, this needs way more looping etc => change
    category_counts = connected_entries['eponymy-occupation'].value_counts()
    category_counts.plot(kind='bar', color='lightcoral')
    plt.title('Plants Named After Mythical/Fictional Characters - Category Visualization')
    plt.xlabel('Category')
    plt.ylabel('Number of Plants')
    plt.show()

result = plant_information(plant_name)

if not connected_entries.empty:
    plot_visualization()
# diagram idea: are more plants named after her (needs: eponymy name, yob and yod)
# diagram idea: if is-real = true => Country visualization