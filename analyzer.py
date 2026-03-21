# Gyasi Hayes
# Description: This program loads data from a csv file, then filters through it, summarizes it, calculates 
# some more advanced stats, generates my insights, and then outputs them into a separate file.
# Submitting date: 3/20/26
# Chosen dataset: sports.csv
DATASET = "sports.csv"
def load_data(filepath):
    """
    This function reads the CSV file and turns it into a list
    The parameter is (filepath), which is the path to the CSV file
    The list containing the data is returned
    """
    data = []
    with open(filepath, "r") as file:
        header = file.readline().strip().split(",") #Takes the first line strips the white face, and separates them by commas

        for line in file:
            values = line.strip().split(",") #Splits the current line into separate values
            row = {}
            #Makes each column header a key and its corresponding value from the row
            for i in range(len(header)):
                row[header[i]] = values[i] 
            data.append(row) 
    return data
        
def filter_data(data, column, value):
    """
    This function filters the dataset based on a chosen column and value
    The parameters are (data), which is just where the data from the CSV is stored, and
    (column), which will hold whatever columun you want to get stats for, and (value) is whatever value is picked
    """
    filtered = []
    for row in data:
        if row[column] == value: #Only includes rows where the column matches the chosen value
            filtered.append(row)
    return filtered

def get_category_stats(data, column):
    """
    This function calculates the minimum, maximum, and average for whichever column is picked
    The parameters are (data), which is just where the data from the CSV is stored, and
    (column), which will hold whatever columun you want to get stats for
    The minimum, maximum, and average are returned.
    """
    stat_numbers = []
    for row in data:
        stat_values = float(row[column]) # Converts the string values into floats
        stat_numbers.append(stat_values) # Adds the stat numbers to the list of stat values
    
    #Finds the minimum, maximum, and average(rounded to 2 decimal points)
    max_num = max(stat_numbers)
    min_num = min(stat_numbers)
    average = round(sum(stat_numbers) / len(stat_numbers), 2) 
    return min_num, max_num, average

def summarize(data):
    """
    This function creates a summary of the data in my chosen dataset
    The parameter is (data), which is just where the data from the CSV is stored
    The dictionary cotaining the number of records, number of genres, and average
    rating is returned.
    """
    num_records = len(data)
    genres = set()
    total_rating = 0
    for row in data:
        genres.add(row["genre"]) #Tracks the unique genres
        total_rating += float(row["rating"]) #The sum of all the ratings
    num_of_genres = len(genres)
    average_rating = round(total_rating / num_records, 2)

    #Creates a dictionary with the total amount of records, number of genres, and averaged rating
    summary = {"total_records": num_records, "unique_genres": num_of_genres, "average_rating": average_rating}
    return summary

def display_summary(data):
    """
    This function outputs the summarized data from the summarize(data) function
    The parameter is (data), which is where the data from the CSV is scored
    Nothing is returned
    """
    #Outputs the summary
    summary = summarize(data)
    print("Here is a summary of the data:")
    print(f"The total number of records is: {summary['total_records']}")
    print(f"The total number of genres is: {summary['unique_genres']}")
    print(f"The average player rating is: {summary['average_rating']}")

def generate_insights(data):
    """
    This function creates a list with my 4 insights about the dataset I picked
    The parameter is (data), which is where the data from the CSV is scored
    The list of my insights is returned
    """
    #Creates a list, where my insights are later appended to
    insights = []
    insights.append("The sport with the most people in the data is Basketball")
    insights.append("Despite being the fastest man in history, Usain Bolt has a extremely low value")
    insights.append("The sport with the highest values is Soccer")
    insights.append("The sport with the lowest values are winter sports, such as Skiing and Snowboarding")
    return insights


def export_report(data, output_filepath, top_n=5):
    """
    Writes a summary report to a new file that is created
    The parameters are (data) which is where the CSV is scored, (output_filepath) which is the file path
    that the summary will be written to, and (top_n) which is the number of top rated entries
    Nothing is returned
    """

    top_entries = []
    temp_data = data[:] #Makes a copy of the data so only the top 5 ratings can be taken out without messing with the other data

    for i in range(top_n):
        highest = temp_data[0]
        for row in temp_data:
            if float(row["rating"]) > float(highest["rating"]):
                highest = row
        top_entries.append(highest) #Adds the highest entried into the list 
        temp_data.remove(highest) #Removes the previous items so it won't be checked again
    summary = summarize(data)
    insights = generate_insights(data)

    with open(output_filepath, "w") as file: #Opens a new file to be written to
        #Writes my summary into the newly created file
        file.write("Summary:\n")
        file.write(f"Total Records: {summary['total_records']}\n")
        file.write(f"Unique Genres: {summary['unique_genres']}\n")
        file.write(f"Average Rating: {summary['average_rating']}\n\n")

        file.write(f"Top {top_n} Players:\n")
        for row in top_entries:
            file.write(f"{row['title']} - Rating: {row['rating']}\n")
        file.write("Here are my insights:\n")
        for insight in insights:
            file.write(insight + "\n")

def main():
    #Calls all the functions in order
    """
    This function is where all the needed functions are called
    No parameters
    Nothing is returned.
    """
    data = load_data(DATASET)
    display_summary(data)
    generate_insights(data)
    export_report(data, "report.txt")

main()