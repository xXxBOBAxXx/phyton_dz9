import csv

def read_pb():
    pb = []
    with open("phonebook.csv", encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter = "_")
        for id in reader:
            pb.append(id)
    return pb