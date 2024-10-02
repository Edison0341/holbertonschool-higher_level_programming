#!/usr/bin/python3
import pickle
"""txt"""


def serialize_and_save_to_file(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, "rb") as file:
        load_data = pickle.load(file)
    return (load_data)
