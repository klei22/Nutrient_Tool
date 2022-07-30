#!/bin/bash

while read line; do
  python3 usda_request.py -f "$line" > ./food_jsons/"${line}.json"
done < foods.txt



