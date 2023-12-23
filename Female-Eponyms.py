import pandas as pd

### Data File Preparation
# reads the data file and stores it in the variable "raw_data"
raw_data = pd.read_csv('WomenPlantGenera_v1-3.csv')

# stores just the rows we want: [id, genus-name (name to be searched by), genus-wfo-status (Accepted, Unplaced, Synonym for XY), family-name-wfo (plant family name), eponymy-name (named after whom), eponymy-yob (birthyear of person), eponymy-yod (deathyear of person), eponomy-occupation, eponymy-is-real, eponymy-country]
selected_data = raw_data[['id', 'genus-name', 'genus-wfo-status', 'family-name-wfo', 'eponymy-name', 'eponymy-yob', 'eponymy-yod', 'eponymy-occupation', 'eponymy-is-real', 'eponymy-country']]

# gets the user input
plant_name = input('Please enter the plant name you want to check:')

# checks the existence of a plant_name in 'genus-name'
def name_existence(plant_name):
    name_exists = plant_name in selected_data['genus-name'].values
    return name_exists

# returns more information about the plant the user was searching for
def more_information(plantname):
    string = str("The plant...." + plantname) # Instead, this will take all the information about the plant and do something with it in the future
    return string

# calls the function 'name_existence' with the plant of the user input
plant_exists = name_existence(plant_name)

# gives out if plant exists
if plant_exists:
    print(f'The plant name "{plant_name}" exists in the selected data. ' + more_information(plant_name))
else:
    print(f'The plant name "{plant_name}" does not exist in the selected data.')



# for debugging 
# print('..........................')
# print(selected_data.head())






# Missing: LOOP!

# diagram idea: are more plants named after her (needs: eponymy name, yob and yod)
# diagram idea: if is-real = true => Country visualization

