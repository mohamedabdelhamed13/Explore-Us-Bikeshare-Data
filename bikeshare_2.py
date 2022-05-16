import time
import pandas as pd

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        print("would you like to see data for chicago, new york city,or washington")
        x=input()
        if x.lower()== "chicago" :
            city=x.lower()
            break
        elif x.lower()=="new york city" :
            city=x.lower()
            break 
        elif x.lower()=="washington" :
            city=x.lower()
            break 
        else :
            print('its invalid city')
            continue

    # get user input for month (all, january, february, ... , june)
    while True :
        print("would you like to see data for month ( January, February, March, April, May, June) or (all)")
        y=input()
        if y not in ("January", "February", "March", "April", "May", "June","all"):
            print("invalid month")
            continue
        else :
            month= y
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        print("would you like to see data for day ( Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) or (all)")
        z=input()
        if z not in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","all"):
            print("invalid day")
            continue
        else :
            day= z
            break
        
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
    df=pd.read_csv("C:\\Users\\moham\\OneDrive\\Desktop\\Fwd\\{}".format(CITY_DATA[city]))
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week
    
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    mm=df["month"].mode()[0]
    print("the common month is ",mm)
    # TO DO: display the most common day of week

    dd=df["day_of_week"].mode()[0]
    print("the common day is ",dd)


    # TO DO: display the most common start hour
    df['hour'] = df["Start Time"].dt.hour
    hh=df["hour"].mode()[0]
    print("the common hour is ",hh)
 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    ss= df["Start Station"].mode()[0]
    print("the common start station is ",ss)
    # TO DO: display most commonly used end station

    ee= df["End Station"].mode()[0]
    print("the common endstation is ",ee)

    # TO DO: display most frequent combination of start station and end station trip

    #Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', ss, " & ", ee)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""



    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time

    Means = df['Trip Duration'].mean()
    print('Mean travel time:', Means/60, " Minutes")



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    uu= df['User Type'].value_counts()
    print("the types is ",uu)
    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


