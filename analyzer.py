# header here
dataset = "sports.csv"
def load_data(filepath):
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
def main():
    data = load_data(dataset)
main()

def filter_data(data, column, value):
    filtered = []
    for row in data:
        if row[column] == value:
            filtered.append(row)
    return filtered