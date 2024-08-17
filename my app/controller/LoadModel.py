import pickle

def LoadModel(file_path: str):

    with open(file_path, "rb") as f:
        loaded_model = pickle.load(f)
    
    return loaded_model