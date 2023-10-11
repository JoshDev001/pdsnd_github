import time
import pandas as pd
import numpy as np
#Load city data
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    global months  # Make months a global variable
    print('Hello! Let\'s explore some US bikeshare data!')

    # Initialize variables for city, month, and day
    city = None
    month = None
    day = None

    # Get user input for city (chicago, washington, or  new york city)
    while city not in CITY_DATA:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city not in CITY_DATA:
            print('Invalid city. Please choose from Chicago, New York City, or Washington.')

    # Get user input for month (all, january, february, ... , june)
    while month not in months:
        month = input('Which month would you like to analyze? (all, january, february, ..., june)\n').lower()
        if month not in months:
            print('Invalid month. Please enter a valid month or "all".')

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days:
        day = input('Which day of the week would you like to analyze? (all, monday, tuesday, ..., sunday)\n').lower()
        if day not in days:
            print('Invalid day. Please enter a valid day or "all".')

    print('-'*40)
    return city, month, day

