import pandas as pd

def categorical_to_binary(csv_file):
    df = pd.read_csv(csv_file)
    transactional_data = []
    attribute_value_map = {}
    index = 1


    for _, row in df.iterrows():
        transaction = []
        for attr in df.columns:
            pair = f"{attr}={row[attr]}"
            transaction.append(pair)
            if pair not in attribute_value_map:
                attribute_value_map[pair] = index
                index += 1
        transactional_data.append(transaction)


    num_columns = len(attribute_value_map)
    binary_dataset = []

    for transaction in transactional_data:
        binary_row = [0] * num_columns
        for item in transaction:
            col_index = attribute_value_map[item] - 1
            binary_row[col_index] = 1
        binary_dataset.append(binary_row)


    binary_df = pd.DataFrame(binary_dataset, columns=[str(i+1) for i in range(num_columns)])


    print("Attribute-Value to Number Map:")
    for key, val in attribute_value_map.items():
        print(f"{val}: {key}")

    print("\nBinary Dataset:")
    print(binary_df)

#outputfile name:009_binary_output.csv
    binary_df.to_csv("009_binary_output.csv", index=False)

#inputfile used:009_giveninput.csv
categorical_to_binary("009_giveninput.csv")