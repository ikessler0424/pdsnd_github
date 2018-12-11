import time
import datetime
import calendar
import pandas as pd
import numpy as np

pd.options.display.float_format = '{:,.2f}'.format

# Dict of City names and csv city file names
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
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Which city would you like to GEAR UP to analyze from the following list? \n (Enter the number associated to city to continue) \n")
    
    # To reduce user input error a number is assigned to each city
    # This also has the added benefit of dynamically updating the user message if a new city is added
    # I could see myself living in one of these cities!
    # Chicago could be a really cool city to live in
    city = ''
    cities = []
    for city_name in CITY_DATA:
        cities.append(city_name)
        
    for i, city in enumerate(cities):
            print("     {} -> {}".format(i, city))

    city_input = input("\n ENTER HERE: ")



    while True: # for handling unexpected input by user
        # User City Input 
        # Converted the user input into the city name        
        if city_input == '0' or city_input == '1' or city_input == '2':
            print('-'*40)
            print("\n {} here we come! Keep Pedaling!\n".format(cities[int(city_input)].title()))
            city = cities[int(city_input)]
            break
            return city
        # error handled by implementing 'else' and provided another option to input data
        else:
            print('\n Whoops! Looks like we got a flat tire!\n')
            city_input = input("\n Please enter new city number here: ")
            
            if city_input == '0' or city_input == '1' or city_input == '2':
                print('-'*40)
                print("\n {} here we come! Keep Pedaling!\n".format(cities[int(city_input)].title()))
                city = cities[int(city_input)]
                break
            else:
                # print('\n Again?!?! This is going to be a long ride!\n')
                continue

    print('-'*40)

    # get user input for month (all, january, february, ... , june)
    month_input = ''
    months_options = ['all','january', 'february', 'march', 'april','may', 'june']

    # City value previously entered by user is added to the text to keep the user informed
    while month_input.lower() not in months_options:
        print('\n Which month from the following list would you like to analyse the {} dataset for? \n ** You can also enter \'all\' to run the analysis for all months available **\n'.format(city.title()))
        for month in months_options:
            print(month)
        month_input = input('\n Enter Month Here: ').lower()
        
        if month_input in months_options:
            month = month_input
            print('-'*40)
            print('\n {} is always a great choice! We\'re rolling up to our last selection now.\n'.format(month.title()))
            break
        else:
            print('\n Uh oh, something went wrong. Please try entering a month name again (or \'all\' for no filter')
            continue
        return month

    print('-'*40)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_input = ''
    days_options = ['all','monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']

    while day_input.lower() not in days_options:
        # City and Month values previously entered by user is added to the text to keep the user informed
        print('\n Which day from the following list would you like to analyse the {} in {} month(s) dataset for? \n ** You can also enter \'all\' to run the analysis for all days available **\n'.format(city.title(), month.title()))
        for day in days_options:
            print(day)
        day_input = input('\n Enter Day Here: ').lower()
        
        if day_input in days_options:
            day = day_input
            print('-'*40)
            print('\n {} it is! Now let\'s kick this into high gear.\n'.format(day.title()))
            break
        else:
            print('\n Uh oh, something went wrong. Please try entering a month name again (or \'all\' for no filter')
            continue
        return day
    
    print('-'*40)
    
    return city, month, day,


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
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    
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
    """
    Analyzes Time Statistics using the loaded data (df)

    Output:
        Most Commom Stats for:
        - Month
        - Day of Week
        - Start Hour
    """


    """Displays statistics on the most frequent times of travel."""
    print('-'*40 + '\n')
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_months_counts = df['month'].value_counts()

    most_common_months_max_number = df['month'].value_counts().index[0]
    most_common_months_max_name = calendar.month_name[most_common_months_max_number]
    most_common_months_max_total_count = most_common_months_counts.max()
    
    print('The most common month of riders was: \n {} at a Total Count of: {} rides \n'.format(most_common_months_max_name, most_common_months_max_total_count))

    # display the most common day of week
    most_common_day_of_week_counts = df['day_of_week'].value_counts()
    most_common_day_of_week_max_name = df['day_of_week'].value_counts().index[0]
    most_common_day_of_week_max_total_count = most_common_day_of_week_counts.max()
    
    print('The most common day_of_week of riders was: \n {} at a Total Count of: {} rides \n'.format(most_common_day_of_week_max_name, most_common_day_of_week_max_total_count))


    # display the most common start hour
    most_common_start_hour_counts = df['start_hour'].value_counts()
    # print(str(most_common_start_hour_counts))
    most_common_start_hour_raw = most_common_start_hour_counts.index[0]
    # Formatted the output into a more readable format for the user instead of military time 
    most_common_start_hour_formatted = datetime.datetime.strptime(str(most_common_start_hour_raw), '%H').strftime('%I:00 %p')

    print('The most commom Start Hour for riders was: {}'.format(most_common_start_hour_formatted))


    print("\nThis took %s seconds to calculate." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """
    Analyzes Station Statistics using the loaded data (df)

    Output:
        Most Commom Stats for:
        - Start Station
        - End Station
        - Combined Start + End Station
    """

    """Displays statistics on the most popular stations and trip."""
    print('-'*40 + '\n')
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station_counts = df['Start Station'].value_counts()
    # print(str(most_common_start_station_counts))
    most_common_start_station_max_name = most_common_start_station_counts.index[0]
    most_common_start_station_max_total_count = most_common_start_station_counts.max()

    print('-'*40)
    print('\n The most common Start Station for riders: {} \n'.format(most_common_start_station_max_name))


    # display most commonly used end station
    most_common_end_station_counts = df['End Station'].value_counts()
    # print(str(most_common_end_station_counts))
    most_common_end_station_max_name = most_common_end_station_counts.index[0]
    most_common_end_station_max_total_count = most_common_end_station_counts.max()

    print('\n The most common End Station for riders: {} \n'.format(most_common_end_station_max_name))


    # display most frequent combination of start station and end station trip
    # most_frequent_combo_of_stations = pd.DataFrame(df.groupby(['Start Station', 'End Station'], as_index=False).count()).sort_values(by='start_hour', ascending=False)
    # most_frequent_combo_of_stations = pd.DataFrame(df.groupby(['Start Station', 'End Station'], as_index=False).count()).sort_values(by='start_hour', ascending=False)
    
    # "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.idxmax.html#pandas.Series.idxmax"
    # "https://www.reddit.com/r/learnpython/comments/5j8h4x/pandas_groupby_to_get_max_occurrences_of_value/"
    most_frequent_combo_of_stations = df.groupby(['Start Station', 'End Station'])['start_hour'].count().idxmax()
    # most_frequent_combo_of_stations_max = most_frequent_combo_of_stations[]
    
    print("\n The most frequented combination of \'Start Stations\' and \'End Stations\' was: \n {}".format(most_frequent_combo_of_stations))
    # print(str(most_frequent_combo_of_stations_max))



    print("\nThis took %s seconds to calculate." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Analyzes Bike Trip Duration Statistics using the loaded data (df)

    Output:
        - Total Travel Time
        - Mean Travel Time
    """

    """Displays statistics on the total and average trip duration."""
    print('-'*40 + '\n')
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('  -  '*20)

    # display total travel time
    travel_time_total = df['Trip Duration'].sum()
    print('\n The total Trip Travel time for this analysis was: \n \"{0:.2f}\" seconds\n'.format(travel_time_total))


    # display mean travel time
    travel_time_mean = df['Trip Duration'].mean()
    print('\n The Average Trip Travel time for this analysis was: \n \"{0:.2f}\" seconds \n'.format(travel_time_mean))


    print("\nThis took %s seconds to calculate." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """
    Analyzes Bike Share User Statistics using the loaded data (df) and the City value

    ** Due to the "Washington" dataset not including Gender + Birth Year data a generic message 
        is generated when the user tries to calculate these statistics **

    Output:
        Most Commom Stats for:
        - User Types Counts
        - Gender Counts
        - Earliest year of Birth
        - Latest year of Birth
        - Most common year of Birth
    """
    """Displays statistics on bikeshare users."""
    print('-'*40 + '\n')    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    #   "https://stackoverflow.com/questions/35523635/extract-values-in-pandas-value-counts/35523820"
    user_types_count = df['User Type'].value_counts()

    # Uncomment to test user type counts
    # print(type(user_types_count))
    # print('\n\nTotal rides by User Type: \n{}'.format(user_types_count))

    # "https://stackoverflow.com/questions/38387529/how-to-iterate-over-pandas-series-generated-from-groupby-size"
    print('\n\nTotal rides by User Type are shown below:\n')
    for user_type, user_type_count in user_types_count.items():
        print('{}\'s: {}'.format(user_type,user_type_count))

    # Exception handling for users that input city = "washington" because there currently is no Gender OR Birth Year Data
    while True:
        if city == 'washington':
            print('\n*** NOTE: Unfortunately Washington currently does not support gender and birth year calculations. ***\n')
            break
        else:
            # Display counts of gender
            gender_counts = df['Gender'].value_counts()
            print('\n\nTotal rides by Gender are shown below:\n')
            # print(str(gender_counts))


            
            for gender, gender_count in gender_counts.items():
                print('{}: {}'.format(gender,gender_count))



            # Display earliest, most recent, and most common year of birth
            # Could refactor this code to show the actual age for each of the below stats
            birth_year_min = df['Birth Year'].min()
            birth_year_max = df['Birth Year'].max()
            birth_years_most_common = df['Birth Year'].value_counts()

            print("\nCheck out the the oldest and youngest customers, as well as your most popular age \n")
            print("The Oldest Customer was born in: {} \n".format(int(birth_year_min)))
            print("The Youngest Customer was born in: {} \n".format(int(birth_year_max)))
            print("Most popular Customer age: {} \n".format(int(birth_years_most_common.index[0])))
            break




    print("\nThis took %s seconds to calculate." % (time.time() - start_time))
    print('-'*40)

# Provides user the ability to reset the program and create checkpoints between each set of calculations
def master_reset_options():
    print('-'*40 + '\n')
    rabbit_hole_status = ""
    restart = ""
    while True:
        rabbit_hole_status = input('\n Everything good so far?\n If so enter \'yes\' (or just press the \'ENTER\' button) \n... if you\'re having a bad ride enter \'no\' here:')
        if rabbit_hole_status.lower() == 'no':
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == 'yes':
                break
        elif rabbit_hole_status.lower() == 'yes':
            print('-'*40 + '\n\nGreat! let\'s keep moving!\n\n' + '-'*40)
            break
        else:
            break
    if restart.lower() == 'yes':
        return main()



def main():
    while True:
        # set the users inputs to local variables for use this analysis
        city, month, day = get_filters()

        # load data to dataframe from the CSV file identified by user input
        df = load_data(city, month, day)

        # allow user to print data from the raw csv file
        print('Before going any further would you like to see the raw data \n used for this analysis? \n')
        user_raw_data_input_request_status = input('Enter \'yes\' to see 5 records from the raw data: ')

        raw_data_row_counter =5 

        while user_raw_data_input_request_status == 'yes':            
            print(df.head(raw_data_row_counter))
            user_raw_data_input_request_status = input('Want to see more? Enter \'yes\' here:').lower()
            raw_data_row_counter +=5

        master_reset_options()

        print('-'*40 + "\n\n\n Lets start off with some Date and Time Metrics: \n " + '-'*40)
        # run time stats
        time_stats(df)

        master_reset_options()

        print('-'*40 + "\n\n\n Next peg in this analysis are our Station Stats: \n " + '-'*40)
        # run Station Stats
        station_stats(df)
        
        master_reset_options()

        print('-'*40 + "\n\n\n Make sure to fuel up for the Trip Duration Analytics below: \n " + '-'*40)
        # run Trip Duration Stats
        trip_duration_stats(df)

        master_reset_options()

        print('-'*40 + "\n\n\n We\'re all similar in one way or another, let\'s checkout our User Stats: \n " + '-'*40)
        # run User Stats
        user_stats(df, city)

        print('\n\nThank you for holding on tight while riding through this crazy analysis! \n\n Hope you enjoyed it!\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
