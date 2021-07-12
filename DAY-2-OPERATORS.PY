
import math
import os
import random
import re
import sys

def get_total_cost_of_meal():
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    tip = (meal_cost*tip_percent)/100
    tax = (tax_percent*tip_percent)/100
    total_cost = int(round(meal_cost+tip+tax))
    return str(total_cost)
print(get_total_cost_of_meal())

