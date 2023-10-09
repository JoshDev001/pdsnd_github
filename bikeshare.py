import time
import pandas as pd
import numpy as np

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

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    print('Most commonly used start station:', df['Start Station'].mode()[0])

    # Display most commonly used end station
    print('Most commonly used end station:', df['End Station'].mode()[0])

    # Display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    print('Most frequent combination of start and end station trip:', df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    print('Total travel time (in seconds):', df['Trip Duration'].sum())

    # Display mean travel time
    print('Mean travel time (in seconds):', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of each user type:\n', df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df:
        print('Counts of each gender:\n', df['Gender'].value_counts())
    else:
        print('Gender data not available for this city.')

    # Display earliest, most recent, and most common year of birth 
    if 'Birth Year' in df:
        print('Earliest birth year:', int(df['Birth Year'].min()))
        print('Most recent birth year:', int(df['Birth Year'].max()))
        print('Most common birth year:', int(df['Birth Year'].mode()[0]))
    else:
        print('Birth year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        # Get user input for city, month and day
        city, month, day = get_filters()
        
        # Display the input
        print('\nHere are your choices :')
        print('City:', city)
        print('Month:', month)
        print('Day:', day)
        print('-'*40)
        
        # Ask the user if they want to edit their choices
        edit_choices = input('\nDo you want to edit your choices? Enter yes or no.\n')
        if edit_choices.lower() == 'yes':
            continue  # Restart the loop to get new input
        elif edit_choices.lower() != 'no':
            print('Invalid input. Assuming no.')
        print('-'*40)
        # Load data based on user input
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

         # Displaying 5 lines of raw data
        start_idx = 0
        while True:
            show_raw_data = input('\n Display 5 lines of raw data? Enter yes or no.\n')
            if show_raw_data.lower() == 'yes':
                print(df.iloc[start_idx:start_idx+5])
                start_idx += 5
            else:
                break
        print('-'*40)
       # Additional questions about the data
        print('\nAdditional Questions about the Data:')
        print('1. What is the most common start station?')
        print('Most common start station:', df['Start Station'].mode()[0])

        print('\n2. What is the most common trip (from start station to end station)?')
        df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
        print('Most frequent combination of start and end station trip:', df['Trip'].mode()[0])
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()