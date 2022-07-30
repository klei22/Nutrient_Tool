import csv

# GOAL: report the target xor range, distance <min, >max
# TODO: keep nutrient class, but pool designated groups of nutrients


class Nutrient(object):

    """Nutrients class, measured by mass"""

    def __init__(
        self, usda_code, units, code_name, human_readable_name, target, min, max
    ):
        """Nutrients initialized

        All units are refactored into grams

        Args:
            usda_code (int): usually 3 digit code for nutrient
            units (str): usually g, mg, or ug
            code_name (str): all caps codename for nutrient
            human_readable_name (str): human readable long form name
            target (float): single number or None
            min (float): single number or None
            max (float): single number or None
        """
        self._usda_code = usda_code
        self._units = units
        self._code_name = code_name
        self._human_readable_name = human_readable_name
        self._target = target
        self._min = min
        self._max = max
        self._amount_in_grams = 0

    def add(self, amount):
        scaling_factor = 1
        if self._code_name == "g":
            scaling_factor = 1
        if self._code_name == "mg":
            scaling_factor = 1000.0
        if self._code_name == "ug":
            scaling_factor = 1000000.0

        self._amount_in_grams += amount * scaling_factor

    def report(self):
        if self._target != None:
            return self._amount_in_grams - self._target

        if (self._min != None) and (self._max != None):
            if self._amount_in_grams < self._min:
                return self._amount_in_grams - self._min
            if self._amount_in_grams > self._max:
                return self._amount_in_grams - self._max
            return 0

        return None

def get_nutrient_dict():

    nutrient_dict = {}

    with open("number_units_hrname_target_min_max.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="|")
        for row in csv_reader:
            usda_code = int(row[0])
            usda_units = str(row[1])
            usda_codename = str(row[2])
            human_readable_name = str(row[3])

            target = float(row[4]) if (row[4] != "None") else None
            min = float(row[5]) if (row[5] != "None") else None
            max = float(row[6]) if (row[6] != "None") else None

            nutrient_dict[usda_code] = Nutrient(usda_code, usda_codename, usda_units, human_readable_name, target, min, max)

        for usda_code, nutrient in nutrient_dict.items():
            print(usda_code, nutrient.report(), nutrient._human_readable_name)

    return nutrient_dict

def add_values_from_foodcode(foodcode):
    # TODO: read in a csv with the foodcodes, and tally up the nutrient dict, then do report
    pass


get_nutrient_dict()
