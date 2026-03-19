# Gyasi Hayes
# Description
# Submitting date
# Chosen dataset: sports.csv
dataset = "sports.csv"
def load_data(filepath):
    """
    Thus function reads the CSV file and turns it into a list
    The parameter is (filepath), which is the path to the CSV file
    The list containing the data is returned
    """
    data = []
    with open(filepath, "r") as file:
        header = file.readline().strip().split(",")

        for line in file:
            values = line.strip().split(",")
            row = {}

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
        if row[column] == value:
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
        stat_values = float(row[column])
        stat_numbers.append(stat_values)
    max_num = max(stat_numbers)
    min_num = min(stat_numbers)
    average = sum(stat_numbers) / len(stat_numbers)
    return min_num, max_num, average

def summarize(data):
    """
    This function creates a summary of tha data in my chosen dataset
    The parameter is (data), which is just where the data from the CSV is stored
    The dictionary cotaining the number of records, number of genres, and average
    rating is returned.
    """
    num_records = len(data)
    genres = set()
    total_rating = 0
    for row in data:
        genres.add(row["genre"])
        total_rating += float(row["rating"])
    num_of_genres = len(genres)
    total_rating = sum(total_rating)
    average_rating = round(total_rating / num_records, 2)

    summary = {"num_records": num_records, "num_of_genres": num_of_genres, "average_rating": average_rating}
    return summary

def display_summary(data):
    """
    This function outputs the summarized data from the summarize(data) function
    The parameter is (data), which is where the data from the CSV is scored
    Nothing is returned
    """
    summary = summarize(data)
    print("Here is a summary of the data:")
    print(f"The total number of records is: {summary['num_records']}")
    print(f"The total number of genres is: {summary['num_of_genres']}")
    print(f"The average player rating is: {summary['average_rating']}")

def generate_insights(data):
    """
    This function creates a list with my 4 insights about the dataset I picked
    The parameter is (data), which is where the data from the CSV is scored
    The list of my insights is returned
    """
    insights = []
    insights.append("The sport with the most people in the data is Basketball")
    insights.append("Despite being the fastest man in history, Usain Bolt has a extremely low value")
    insights.append("The sport with the highest values is Soccer")
    insights.append("The sport with the lowest values are winter sports, such as Skiing and Snowboarding")
    return insights

def main():
    """
    
    """
    data = load_data(dataset)
        
