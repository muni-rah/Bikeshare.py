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

    # to do: get user input for city chicago, new york city or washington.
    city = input("you want data about chicago, new york city or washington?").strip().capitalize().lower()
    while (city != "chicago" and city != "new york city" and city != "washington"):
        city = input("you want data about chicago, new york city or washington?").strip().capitalize().lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("which month?").strip().lower().capitalize()
    while (month != "January" and month != "February" and month != "March" and month != "April" and month != "May" and month != "June" and month != "July" and month != "August" and month != "September" and month != "October" and month != "November" and month != "December"):
      month = input("which month?").strip().lower().capitalize()



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("which day?").strip().lower().capitalize()
    while (day != "Saturday" and day != "Sunday" and day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday"):
        day = input(day).strip().lower().capitalize()

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
    # filters by the city
    df = pd.read_csv(CITY_DATA[city])

    # convert the start and end times from strings to dates, so we can extract the day and month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract the day and monthinto their separate colums
    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()

     # filter by month if applicable
    if month != 'All':
        df = df[df['month'] == month]

    # filter by day if applicable
    if day != 'All':
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

  # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("most common start month:\n{} \n".format(popular_month))


  # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print("most common start day:\n{} \n".format(popular_day))

  # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("most common start hour:\n{} \n".format(popular_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print("most common start station is:\n{} \n".format(most_common_start))

    # TO DO: display most commonly used end station
    most_common_End = df['End Station'].mode()[0]
    print("most common end station is:\n{} \n".format(most_common_End))

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'] + df['End Station']
    most_common_route = df['route'].mode()[0]
    print("most common frequent combination of start station and end station trip:\n{} \n".format(most_common_route))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total = df['Trip Duration'].sum()
    print('total travel time is:\n')
    print(Total)


    # TO DO: display mean travel time
    Average = df['Trip Duration'].mean()
    print('average travel time is:\n')
    print(Average)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    df = pd.read_csv('chicago.csv')
    user_types = df['User Type'].value_counts()

    print(user_types)


    # TO DO: Display counts of gender
    Gender = df['Gender'].value_counts().unique()
    print(Gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year_of_birth = df['Birth Year'].min()
    print('earliest year of birth:')
    print(earliest_year_of_birth)

    recent_year_of_birth = df['Birth Year'].max()
    print('recent year of birth:')
    print(recent_year_of_birth)

    most_common_year_of_birth = df['Birth Year'].mode()[0]
    print('most common year of birth is:')
    print(most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        want_raw_data = input("would you like to see more of the raw data?").strip().lower()
        start = 0
        end = 5
        while(want_raw_data == "yes"):
            print(df.iloc[start:end])
            start += 5
            end += 5
            want_raw_data = input("would you like to see more of the raw data?").strip().lower()


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
