import pandas as pd
import sqlite3
from typing import List, Dict


class ProfessorDataHandler:
    def __init__(self, db_path: str, table_name: str):
        self.db_path = db_path
        self.table_name = table_name

    def read_professor_data(self) -> List[Dict]:
        with sqlite3.connect(self.db_path) as conn:
            df = pd.read_sql(f"SELECT * FROM {self.table_name}", conn)
        return df.to_dict(orient="records")

    def update_database(self, professor_record: Dict) -> None:
        with sqlite3.connect(self.db_path) as conn:
            placeholders = ", ".join([f"{key} = ?" for key in professor_record])
            values = list(professor_record.values())
            query = f"UPDATE {self.table_name} SET {placeholders} WHERE Employee = ?"
            conn.execute(query, values + [professor_record["Employee"]])
            conn.commit()
