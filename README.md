# Nutrient Tool

Tool for obtaining nutrient info from the USDA Database

## TODO

- [x] create dictionary .py file with the mappings of interest
  - [x] amino acids
  - [x] fatty acids
  - [x] bacteria?
  - [x] minerals
  - [x] vitamins
  - [x] macronutrients
- [x] create tool for calculating the total amount from code (to standard unit of grams)
- [ ] create tool for adding up the different values of each nutrient from a meal
- [ ] create tool for calculating the missing nutrients
- [ ] create tool to try to find recommended foods to fill in the gaps

adding totals of each nutrient (code) into the nutrient dictionary, then
reporting results.

could do this with simply creating a dictionary with the key being the usda
code, and looping through the matching food

first would be good to just get the json for the matching foods though

need to get the id list into python, then add the nutrients from each
