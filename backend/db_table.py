import sqlite3
class BaseTable():
    SQL_KEYWORDS = [
        "SELECT", "INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "CREATE",
        "UNION", "OR", "AND", "--", "/*", "*/", ";", "'", "\"", "`",
        "EXEC", "EXECUTE", "TRUNCATE", "MERGE"
    ]
    def __init__(self, db_connection: sqlite3.Connection, cursor: sqlite3.Cursor, table_name: str, pk: str):

        self.db = db_connection
        self.cursor = cursor
        self.table_name = table_name
        self.pk_field = pk

    def update_id(self, entity_id: int, **kwargs):
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
        

    def delete_id(self, entity_id: int):
        try:
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE {self.pk_field} = ?", (entity_id,))
            self.db.commit()
        except Exception as e:
            print(f"Exception occured as {e}")

    def insert_value(self, **kwargs):
        if kwargs.keys() in self.SQL_KEYWORDS:
            print("SQL keywords are prohibited.")
            return False # if false then window will close.

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

    def select(self, *column):
        if not column:
            columns = "*"
        else:
            columns = ", ".join(column)

        try:
            self.cursor.execute(f"SELECT {columns} FROM {self.table_name}")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Could not show tables from {self.table_name}: {e}")