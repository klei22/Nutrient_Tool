from api_key import usda_api_key
from rich import print_json
import json

import requests
import argparse


def search_for_food(foodname):
    """Get full request from USDA for specific food

    Args:
        foodname(str): string name of the food to search for

    Returns:
        json file of request
    """
    base_url = "https://api.nal.usda.gov/fdc/v1/foods/search?"
    r = requests.get(base_url + "&query=" + str(foodname) + "&api_key=" + usda_api_key)
    return r.json()


def print_food_json(food_json):
    """Pretty print output to stdout for the food_json

    Args:
        food_json(json): json result from usda query
    """
    print_json(json.dumps(food_json))


def get_hr_listing_of_nutrients(usda_json):
    """Get the listing of nutrients in human readable form

    Args:
        usda_json: json formatted nutrient response from usda database
    """
    # TODO: make this more general
    for item in usda_json["foods"][12]["foodNutrients"]:
        print(item["nutrientName"])


def parse_args():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    p.add_argument(
        "-f",
        "--foodname",
        type=str,
        help="name of food to search",
    )

    return p.parse_args()


def main():
    args = parse_args()
    food_nutrients_json = search_for_food(args.foodname)
    # get_hr_listing_of_nutrients(food_nutrients_json)
    print_food_json(food_nutrients_json)


if __name__ == "__main__":
    main()
