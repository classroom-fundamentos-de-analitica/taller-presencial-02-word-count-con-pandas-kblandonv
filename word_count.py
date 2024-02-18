"""Taller evaluable"""

import glob

import pandas as pd

import string

def load_input(input_directory):
    """Load input files into a DataFrame.
    
    Args:
        input_directory (str): The directory containing the input files.
        
    Returns:
        pandas.DataFrame: The DataFrame containing the input files.
    """
    # Get a list of all input files
    input_files = glob.glob(input_directory + '/*.txt')
    
    # Read all input files into a single DataFrame
    df = pd.concat((pd.read_csv(f, sep='\t', header=None, names=['text']) for f in input_files), ignore_index=True)
    
    return df


def clean_text(dataframe):
    """Clean text
    
    Remove punctuation and convert text to lowercase.
    
    Args:
        dataframe (pandas.DataFrame): The input dataframe containing the text column.
        
    Returns:
        pandas.DataFrame: The input dataframe with an additional column 'clean_text' containing the cleaned text.
    """
    dataframe['clean_text'] = dataframe['text'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)).lower())
    return dataframe


def count_words(dataframe):
    """Count words.
    
    Args:
        dataframe (pandas.DataFrame): The input dataframe containing the clean_text column.
        
    Returns:
        pandas.DataFrame: A DataFrame containing the word counts.
    """
    # Split the text into words
    words = dataframe['clean_text'].str.split(expand=True).stack()
    
    # Count the words
    word_counts = words.value_counts().reset_index()
    word_counts.columns = ['word', 'count']
    
    return word_counts


def save_output(dataframe, output_filename):
    """Save output.
    
    Args:
        dataframe (pandas.DataFrame): The DataFrame containing the word counts.
        output_filename (str): The name of the output file.
        
    Returns:
        None
    """
    dataframe.to_csv(output_filename, sep='\t', index=False, header=False)



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
