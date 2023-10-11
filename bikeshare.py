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
# Load data for specified city
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        month_num = months.index(month)  # Convert month name to numerical value
        df = df[df['Month'] == month_num]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['Day_of_Week'] == day.title()]  # Title case for consistency

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    print('Most common month:', df['Month'].mode()[0])

    # Display the most common day of the week
    print('Most common day of the week:', df['Day_of_Week'].mode()[0])

    # Display the most common start hour
    print('Most common start hour:', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
