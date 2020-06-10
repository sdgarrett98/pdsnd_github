import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input('Would you like to see data for Chicago, New york city, or Washington?\n').lower()
            if city == CITY_DATA[city]:
                pass
            break
        except:
            print('Please enter a valid city.')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        try:
            month = input('Please enter the name of a month (january, february, ..., june), or specify \'all\':\n').lower()
            if (month == 'january') or (month == 'february') or (month == 'march') or (month == 'april') or (month == 'may') or (month == 'june') or (month == 'all'):
                pass
                break
            else:
                print('Please enter a valid month.')
                continue
        except:
            print('\nPlease enter a valid month.')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try:
            day = input('Please enter day of week (monday, tuesday, ..., sunday), or specify \'all\': \n').lower()
            if (day == 'monday') or (day == 'tuesday') or (day == 'wednesday') or (day == 'thursday') or (day == 'friday') or (day == 'saturday') or (day == 'sunday') or (day == 'all'):
                pass
                break
            else:
                print('Please enter a valid day.')
                continue
        except:
            print('\nPlease enter a valid day.')
            continue

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day, and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df.month.mode()[0]
    print('The most common month is: ', common_month,'\n')

    # TO DO: display the most common day of week
    common_day = df.day_of_week.mode()[0]
    print('The most common day is: ', common_day,'\n')

    # TO DO: display the most common start hour
    common_hour = df.hour.mode()[0]
    print('The most common hour is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ',common_start_station,'\n')

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ',common_end_station,'\n')

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End Station'] = df['Start Station'] + '-' + df['End Station']
    frequent_combo = df['Start and End Station'].mode()[0]
    print('The most frequently used combination of start and end stations is: ',frequent_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_time,'\n')

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The average travel time is: ',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('The counts of type of user are: \n',user_type_count,'\n')

    # TO DO: Display counts of gender
    if not 'Gender' in df.columns:
        print('Unfortunately there is no gender data available for this city\'s data set.')
    else:
        gender_count = df['Gender'].value_counts()
        print('The gender counts are: \n',gender_count,'\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if not 'Birth Year' in df.columns:
        print('Unfortunately there is no birth year data available for this city\'s data set.')
    else:
        earliest_birth = df['Birth Year'].min()
        print('The earliest birth year is: ', earliest_birth,'\n')

        most_recent_birth = df['Birth Year'].max()
        print('The most recent birth year is: ', most_recent_birth,'\n')

        most_common_birth = df['Birth Year'].mode()[0]
        print('The most common birth year is: ', most_common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # create a loop to allow user input about displaying raw data five rows at a time
        while True:
            raw_data = input('\nWould you like to see raw data? (\'yes\' or \'no\')\n')
            if raw_data.lower() == 'yes':
                print(df.head())
                df = df.iloc[5:]
                continue
            else:
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
