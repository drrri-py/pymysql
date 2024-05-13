from connection import get_db
from interfaces.Entityinterface import EntityInterface

class CoreModel(EntityInterface):
    def __init__(self, table_name, table_id):
        self.table_name = table_name
        self.table_id = table_id
    
    def all(self):
        try:
            connection = get_db()
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.table_name};"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("Error fetching all records:", e)
            return []
        finally:
            cursor.close()
            connection.close()
    
    def store(self, obj):
        try:
            connection = get_db()
            cursor = connection.cursor()
            set_columns = []
            set_placeholders = []
            set_values = []
            for key, value in vars(obj).items():
                if key not in ['table_name', 'table_id']:
                    set_columns.append(key)
                    set_placeholders.append('%s')
                    set_values.append(value)
            columns_string = ', '.join(set_columns)
            placeholders_string = ', '.join(set_placeholders)
            sql_query = f"INSERT INTO {self.table_name} ({columns_string}) VALUES ({placeholders_string});"
            cursor.execute(sql_query, tuple(set_values))
            connection.commit()
        except Exception as e:
            print("Error storing record:", e)
        finally:
            cursor.close()
            connection.close()
        
    def find(self, obj_id):
        try:
            connection = get_db()
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.table_name} WHERE {self.table_id} = %s LIMIT 1;"
            cursor.execute(query, (obj_id,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("Error finding record:", e)
            return None
        finally:
            cursor.close()
            connection.close()
    
    def update(self, obj_id, obj):
        try:
            connection = get_db()
            cursor = connection.cursor()
            set_columns = []
            set_values = []
            for key, value in vars(obj).items():
                if key not in ['table_name', 'table_id']:
                    column = f"{key} = %s"
                    set_columns.append(column)
                    set_values.append(value)
            set_column_string = ', '.join(set_columns)
            sql_query = f"UPDATE {self.table_name} SET {set_column_string} WHERE {self.table_id} = %s;"
            set_values.append(obj_id)
            cursor.execute(sql_query, tuple(set_values))
            connection.commit()
        except Exception as e:
            print("Error updating record:", e)
        finally:
            cursor.close()
            connection.close()
        
    def delete(self, obj_id):
        try:
            connection = get_db()
            cursor = connection.cursor()
            query = f"DELETE FROM {self.table_name} WHERE {self.table_id} = %s;"
            cursor.execute(query, (obj_id,))
            connection.commit()
        except Exception as e:
            print("Error deleting record:", e)
        finally:
            cursor.close()
            connection.close()
