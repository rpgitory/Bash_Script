import numpy as np

def create_table(data_dict):
    # Create a structured array from the dictionary
    table = np.array(list(data_dict.values())).T
    columns = list(data_dict.keys())
    dtypes = [(col, table.dtype) for col in columns]
    table = table.view(dtypes)

    return table

def main():
    # Create a dictionary with the data
    data = {
        'Name': ['John', 'Emma', 'Michael', 'Sophia'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'London', 'Los Angeles', 'Paris']
    }

    # Call the function to create the table
    table = create_table(data)

    # Print the table
    print(table)

if __name__ == "__main__":
    main()
