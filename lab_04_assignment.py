class FlightTable:
    def __init__(self, data):
        self.data = data

    def sort_data(self, sort_by):
        if sort_by == 1:
            self.data.sort(
                key=lambda x: x[0]
            )  # lambda x: x[0] is a function that returns the first element of the tuple x and is used as a key for sorting
        elif sort_by == 2:
            self.data.sort(
                key=lambda x: x[2]
            )  # lambda x: x[2] is a function that returns the third element of the tuple x and is used as a key for sorting
        elif sort_by == 3:
            priority_order = {
                "High": 1,
                "MID": 2,
                "Low": 3,
            }  # priority_order is a dictionary that maps priority to a number
            self.data.sort(
                key=lambda x: priority_order[x[3]]
            )  # lambda x: priority_order[x[3]] is a function that returns the priority number of the tuple x and is used as a key for sorting

    def print_data(self):  # prints the data in a tabular format
        print("P_ID\tProcess\tStart Time (ms)\tPriority")
        for row in self.data:
            print(
                "\t".join(map(str, row))
            )  # map(str, row) is a function that converts all elements of the tuple row to string and returns a map object. '\t'.join() is a function that joins all elements of the map object with a tab and returns a string


data = [
    ("P1", "VSCode", 100, "MID"),
    ("P23", "Eclipse", 234, "MID"),
    ("P93", "Chrome", 189, "High"),
    ("P42", "JDK", 9, "High"),
    ("P9", "CMD", 7, "High"),
    ("P87", "NotePad", 23, "Low"),
]

flight_table = FlightTable(data)
sort_by = int(input("Enter sorting parameter [1. P_ID, 2. Start Time, 3. Priority]: "))
flight_table.sort_data(sort_by)
flight_table.print_data()
