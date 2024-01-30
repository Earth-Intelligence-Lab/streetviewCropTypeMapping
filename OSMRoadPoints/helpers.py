import pandas as pd
import os
def decreasePointRes(file_path):
    # Load the CSV file into a Pandas dataframe
    df = pd.read_csv(file_path)
    # Remove every other column from the dataframe
    df = df.iloc[::4, :]
    # Save the modified dataframe back into the same file
    df.to_csv(file_path, index=False)



def split_csv_file(root, input_file, chunk_size=300000):
    # Read the input CSV file
    df = pd.read_csv(os.path.join(root, input_file))
    # Get the total number of rows in the dataframe
    total_rows = len(df)
    print(total_rows)
    # Calculate the number of chunks needed
    num_chunks = total_rows // chunk_size + 1

    # Split the dataframe into chunks
    chunks = [df[i:i + chunk_size] for i in range(0, total_rows, chunk_size)]


    # Save each chunk as a separate CSV file
    for i, chunk in enumerate(chunks):
        output_file = os.path.join(root,"splitFieldPoints/"+input_file[:-4]+"-"+str(i)+".csv")
        chunk.to_csv(output_file, index=False)
        print(f"Chunk {i+1} saved as {output_file}")

def change_column_names(input_file):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Change the column names of columns 0 and 1
    df.rename(columns={df.columns[0]: 'y', df.columns[1]: 'x'}, inplace=True)

    # Save the modified dataframe back to the same CSV file
    df.to_csv(input_file, index=False)
    print(f"Modified CSV file saved: {input_file}")

FOLDER_PATH ="/Users/jordi/Desktop/MIT-Research/India/fieldPoints/"
# for i in range(76,77):
#     change_column_names("/Users/jordi/Desktop/MIT-Research/GSV-test/ThailandStreetPoints/thaiRoadPoints"+str(i)+".csv")
for i in range(1,2):
    decreasePointRes(FOLDER_PATH+"fieldPointsNW4_"+str(i)+".csv")

for i in range(1,2):
    split_csv_file(FOLDER_PATH, "fieldPointsNW4_"+str(i)+".csv", chunk_size=300000)


for i in range(76,77):
    split_csv_file("/Users/jordi/Desktop/MIT-Research/GSV-test/ThailandStreetPoints/", "thaiRoadPoints"+str(i)+".csv")
