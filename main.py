
# Import needed resources.
import csv
import sys

from country import *

print("Starting FBIC simulation ...")
print("Python:", sys.version)

print("Instantiating countries ...")
# Country codes for all countries.
country_codes = {'AFG', 'CHE', 'FRA', 'GBR', 'IRN',
                 'IRQ', 'ITA', 'SYR', 'TUR', 'USA'}
print("Country Codes:", country_codes)
# Codes for just the primary countries for analysis.
primary_codes = {'CHN', 'RUS', 'USA'}
print("Primary Codes:", primary_codes)

# Read and instantiate countries from the CSV file
# based on the country code set.
secondary_countries = []
with open('data/countries.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[0] in country_codes - primary_codes:
            print(row)
            secondary_countries.append(SecondaryCountry(
                row[1], row[0], row[2], row[3], row[4], 0, primary_codes))

print("Instantiated", len(secondary_countries), "secondary countries.")
print(secondary_countries)

for c in secondary_countries:
    c.show()
    c.pprint()

# Read and instantiate primary countries from the CSV file
# based on the primary country code set.
primary_countries = []
with open('data/countries.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[0] in primary_codes:
            print(row)
            primary_countries.append(PrimaryCountry(
                row[1], row[0], row[2], row[3], row[4], 0, secondary_countries))

print("Instantiated", len(primary_countries), "primary countries.")

# Test account balance update.
accs = secondary_countries[0].liabilities()
accs[0].deposit(100)
secondary_countries[0].pprint()

print(primary_countries)
primary_countries[0].show()
primary_countries[0].pprint()

print("End of FBIC simulation.")
