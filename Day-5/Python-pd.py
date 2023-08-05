import pandas as pd

def create_table(data_dict):
    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data_dict)

    return df

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
