import sqlite3
class BaseTable():
    def __init__(self, db_connection: sqlite3.Connection, table_name: str, pk: str):
        self.db = db_connection
        self.cursor = self.db.cursor()
        self.table_name = table_name
        self.pk_field = pk

    def updateid(self, entity_id: int, **kwargs):
        """
        dynamically updates, placeholder text:
        if given kwargs: key = ? appends, then joins as key = ?, key = ?,
        UPDATE Engineer SET Value WHERE EngineerID = 1

        """
        if not kwargs:
            print("Nothing to update.")
            return
        
        columns = [F"{key} = ?" for key in kwargs.keys()]

        join_columns = ", ".join(columns)

        sql_execution = f"UPDATE {self.table_name} SET {join_columns} WHERE {self.pk_field} = ?"

        values = list(kwargs.values())
        values.append(entity_id)

        try:
            self.cursor.execute(sql_execution, values)
            self.db.commit()
        except Exception as e:
            print(f"Could not update {self.pk_field}, occured as {e}")
        

    def deleteid(self, entity_id: int):
        try:
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE {self.pk_field} = ?", (entity_id,))
            self.db.commit()
        except Exception as e:
            print(f"Exception occured as {e}")

    def insertvalue(self, **kwargs):
        keys = [key for key in kwargs.keys()]
        joined_keys = (", ").join(keys)

        increments = ["?" for _ in keys]
        joined_increment = (", ").join(increments)

        values = tuple(kwargs.values())

        try:
            self.cursor.execute(f"INSERT INTO {self.table_name}({joined_keys}) VALUES ({joined_increment})", values)
            self.db.commit()
        except Exception as e:
            print(f"Could not insert value from {self.pk_field}, {e}")