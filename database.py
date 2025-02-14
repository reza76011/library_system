import os
import pickle

DATA_PATH = "C:/Users/reza/Desktop/New folder/"
FILES = ["users.dat", "books.dat", "borrows.dat"]

def check_validation():
    """Ensure all required data files exist."""
    for file in FILES:
        path = os.path.join(DATA_PATH, file)
        if not os.path.exists(path):
            with open(path, "wb") as f:
                pickle.dump({}, f)

def load_data(filename):
    """Load data from a given file."""
    check_validation()
    with open(os.path.join(DATA_PATH, filename), "rb") as f:
        return pickle.load(f)

def save_data(filename, data):
    """Save data to a given file."""
    with open(os.path.join(DATA_PATH, filename), "wb") as f:
        pickle.dump(data, f)
