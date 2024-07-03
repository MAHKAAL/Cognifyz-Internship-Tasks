import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def get_user_input():
    print("Enter your dataset:")
    print("Input format: Column names on the first line separated by commas")
    print("Then input each row of data, also separated by commas")
    print("Type 'end' to finish input")

    # Read column names
    columns = input("Column names: ").split(',')

    # Read data rows
    data = []
    while True:
        row = input()
        if row.lower() == 'end':
            break
        data.append(row.split(','))

    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Prompt user to specify data types for columns
    for column in columns:
        while True:
            dtype = input(f"Enter data type for column '{column}' (str, int, float): ").strip().lower()
            if dtype in ['str', 'int', 'float']:
                break
            else:
                print("Invalid input. Please enter 'str', 'int', or 'float'.")
                
        if dtype == 'int':
            df[column] = pd.to_numeric(df[column], errors='coerce', downcast='integer')
        elif dtype == 'float':
            df[column] = pd.to_numeric(df[column], errors='coerce', downcast='float')
    
    return df

def generate_visualization(dataframe, x, y, chart_type, title, color=None, size=None):
    plt.figure(figsize=(12, 8))
    
    try:
        if chart_type == 'scatter':
            sb.scatterplot(data=dataframe, x=x, y=y, hue=color, size=size, sizes=(20, 200))
        elif chart_type == 'line':
            sb.lineplot(data=dataframe, x=x, y=y, hue=color)
        elif chart_type == 'bar':
            sb.barplot(data=dataframe, x=x, y=y, hue=color)
        elif chart_type == 'histogram':
            sb.histplot(data=dataframe, x=x, hue=color, element="step")
        elif chart_type == 'boxplot':
            sb.boxplot(data=dataframe, x=x, y=y, hue=color)
        else:
            print("Unsupported chart type. Please use 'scatter', 'line', 'bar', 'histogram', or 'boxplot'.")
            return
        plt.title(title)
        plt.show()
    except Exception as e:
        print(f"An error occurred while generating the visualization: {e}")

def display_menu():
    print("\n--- Data Visualization Tool ---")
    print("1. Load Dataset")
    print("2. Create Visualization")
    print("3. Exit")

def main():
    df = None
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            df = get_user_input()
            print("\nDataset loaded successfully.")
            print(df)
        elif choice == '2':
            if df is None:
                print("Please load a dataset first.")
                continue

            x_column = input("Enter the column name for the x-axis: ")
            y_column = input("Enter the column name for the y-axis (optional, press Enter to skip): ") or None
            chart_type = input("Enter the type of chart (scatter, line, bar, histogram, boxplot): ").strip().lower()
            title = input("Enter the title for the chart: ")
            color = input("Enter the column name for color (optional, press Enter to skip): ") or None
            size = input("Enter the column name for size (optional, press Enter to skip): ") or None

            generate_visualization(df, x_column, y_column, chart_type, title, color, size)
        elif choice == '3':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()