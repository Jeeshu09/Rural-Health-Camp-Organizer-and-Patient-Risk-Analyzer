import pandas as pd
import os

FILE_PATH = "data/"

def add_patient():
    try:
        name = input("Enter Name: ")
        village = input("Enter Village: ")
        age = int(input("Enter Age: "))
        bp = int(input("Enter BP: "))
        sugar = float(input("Enter Sugar Level: "))
        weight = float(input("Enter Weight: "))
        symptoms = input("Enter Symptoms: ")

        patient = {
            "Name": name,
            "Village": village,
            "Age": age,
            "BP": bp,
            "Sugar": sugar,
            "Weight": weight,
            "Symptoms": symptoms
        }

        return patient

    except ValueError:
        print("❌ Invalid input! Please enter correct values.")
        return None


def save_to_csv(data, filename):
    try:
        df = pd.DataFrame(data)
        path = FILE_PATH + filename

        if not os.path.exists(FILE_PATH):
            os.makedirs(FILE_PATH)

        df.to_csv(path, index=False)
        print(f"✅ Data saved to {path}")

    except Exception as e:
        print("❌ Error saving file:", e)


def load_data(filename):
    try:
        df = pd.read_csv(FILE_PATH + filename)
        return df
    except FileNotFoundError:
        print("❌ File not found!")
        return None