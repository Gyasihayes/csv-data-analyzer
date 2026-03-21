# Gyasi Hayes
# Description
# Submitting date
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
        genres.add(row["genre"])
        total_rating += float(row["rating"])
    num_of_genres = len(genres)
    average_rating = round(total_rating / num_records, 2)

    summary = {"total_records": num_records, "unique_genres": num_of_genres, "average_rating": average_rating}
    return summary

def display_summary(data):
    """
    This function outputs the summarized data from the summarize(data) function
    The parameter is (data), which is where the data from the CSV is scored
    Nothing is returned
    """
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
    temp_data = data[:]

    for i in range(top_n):
        highest = temp_data[0]
        for row in temp_data:
            if float(row["rating"]) > float(highest["rating"]):
                highest = row
        top_entries.append(highest)
        temp_data.remove(highest)
    summary = summarize(data)
    insights = generate_insights(data)

    with open(output_filepath, "w") as file:
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
    """
    
    """
    data = load_data(DATASET)
    display_summary(data)
    generate_insights(data)
    export_report(data, "report.txt")

main()

        
