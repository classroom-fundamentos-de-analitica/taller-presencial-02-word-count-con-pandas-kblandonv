"""Taller evaluable"""

import glob

import pandas as pd

import string

def load_input(input_directory):
    """
    Load text files in 'input_directory/' and store the content in a Pandas DataFrame.
    
    Each line of the text file will be treated as a separate entry in the DataFrame.
    
    Parameters:
        input_directory (str): The directory path where the text files are located.
        
    Returns:
        pandas.DataFrame: A DataFrame containing the text content of the files.
    """
    files = glob.glob(f"{input_directory}/*.txt")
    data = []
    for file in files:
        with open(file, "r") as f:
            lines = f.readlines()
            data.extend(lines)
    df = pd.DataFrame(data, columns=["text"])
    return df


def clean_text(dataframe):
    """
    Text cleaning
    
    This function takes a dataframe as input and performs text cleaning operations on the 'text' column.
    It removes punctuation and converts the text to lowercase.
    
    Args:
        dataframe (pandas.DataFrame): The input dataframe containing the 'text' column.
        
    Returns:
        pandas.DataFrame: The dataframe with cleaned text.
    """
    dataframe['text'] = dataframe['text'].apply(lambda x: x.lower().translate(str.maketrans('', '', string.punctuation)))
    return dataframe


def count_words(dataframe):
    """Word count
    
    Count the number of words in the text.
    
    Args:
        dataframe (pandas.DataFrame): The input dataframe containing the text column.
        
    Returns:
        pandas.DataFrame: The input dataframe with an additional column 'word_count' containing the word count for each text.
    """
    dataframe['word_count'] = dataframe['text'].apply(lambda x: len(x.split()))
    return dataframe


def save_output(dataframe, output_filename):
    """Save output to a file.
    
    Args:
        dataframe (pandas.DataFrame): The DataFrame to be saved.
        output_filename (str): The name of the output file.
    """
    dataframe.to_csv(output_filename, index=False, sep='\t', header=True)



#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions.

    Args:
        input_directory (str): The directory containing the input files.
        output_filename (str): The name of the output file.

    Returns:
        None
    """
    # Load input files into a DataFrame
    input_df = load_input(input_directory)

    # Clean text
    clean_df = clean_text(input_df)

    # Count words
    word_count_df = count_words(clean_df)

    # Save output
    save_output(word_count_df, output_filename)



if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
