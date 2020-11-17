import pickle


def load_path(path):
    """Loads and returns an object from a pickle file in path

    Parameters:
    path (string): Path where the pickle file resides

    Returns:
    object: Object in pickle file
    """
    infile = open(path, 'rb')
    df = pickle.load(infile)
    infile.close()
    return df


def save_df(df, path):
    """Saves an object as a pickle file in path

    Parameters: 
    df (object): Object to store in pickle file
    path (string): Path where the pickle file should reside
    """
    outfile = open(path, 'wb')
    pickle.dump(df, outfile)
    outfile.close
 