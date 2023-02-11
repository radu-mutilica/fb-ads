import csv

def get_countries():
    with open('countries.csv', 'r') as file:
        reader = csv.DictReader(file)
        return [{'country': row['name'], 'iso': row['alpha-2']} for row in reader]
