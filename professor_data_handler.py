import os
import json
import shutil
import sqlite3
import pandas as pd
from typing import List, Dict


class ProfessorDataHandler:
    def __init__(self, db_template_path, table_name):
        self.db_template_path = db_template_path
        self.table_name = table_name

    def read_professor_data(self) -> List[Dict]:
        with sqlite3.connect(self.db_path) as conn:
            df = pd.read_sql(f"SELECT * FROM {self.table_name}", conn)
        return df.to_dict(orient="records")

    def update_database(self, professor_record: Dict, db_path) -> None:
        with sqlite3.connect(db_path) as conn:
            placeholders = ", ".join([f"{key} = ?" for key in professor_record])
            values = list(professor_record.values())
            query = f"UPDATE {self.table_name} SET {placeholders} WHERE Employee = ?"
            conn.execute(query, values + [professor_record["Employee"]])
            conn.commit()

    def setup_database(self) -> (List[Dict], str):
        # Get the folder name from the user
        folder_name = input("Enter the name of the folder: ")
        db_path = os.path.join(folder_name, "professors.db")

        # Check if the professors.db file exists
        if os.path.isfile(db_path):
            self.db_path = db_path
            return self.read_professor_data(), db_path

        # If professors.db does not exist, proceed with existing setup
        folder_exists = input(
            "Does the folder exist and contain professor data? (yes/no): "
        )
        if folder_exists.lower() != "yes":
            print("Folder does not exist or does not contain professor data.")
            return [], None

        if not os.path.isdir(folder_name):
            print("Folder not found in the current directory.")
            return [], None

        # Check if the JSON file exists within the folder
        json_file_path = os.path.join(folder_name, "professors.json")
        if not os.path.isfile(json_file_path):
            print("JSON file not found in the specified folder.")
            return [], None

        # Load data from the JSON file
        with open(json_file_path, "r") as file:
            data = json.load(file)

        # Copy the template database to create a new professors.db file
        shutil.copyfile(self.db_template_path, db_path)

        # Update the database path to the new database
        self.db_path = db_path

        # Connect to the new database and create a DataFrame from JSON data
        with sqlite3.connect(db_path) as conn:
            df = pd.DataFrame(data)
            df.to_sql(self.table_name, conn, if_exists="append", index=False)

        return data, db_path
