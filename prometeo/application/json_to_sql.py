import json
from pathlib import Path

def load_json_data(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data

def generate_insert_scripts(json_data, table_name, column_mapping):
        insert_statements = []
        for record in json_data:
            columns = []
            values = []
            for json_key, db_column in column_mapping.items():
                if json_key in record:
                    columns.append(db_column)
                    # Handle different data types and potential escaping
                    value = record[json_key]
                    if isinstance(value, str):
                        #values.append(f"'{value.replace("'", "''")}'") # Escape single quotes
                        values.append(f"'{value}'") # Escape single quotes
                    elif isinstance(value, (int, float)):
                        values.append(str(value))
                    elif value is None:
                        values.append("NULL")
                    else:
                        values.append(str(value))
            
            if columns and values:
                columns_str = ", ".join(columns)
                values_str = ", ".join(values)
                insert_statements.append(f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});")
                print(insert_statements)
        return insert_statements

table_name = "account"
    # Example: if your JSON has keys 'id', 'name', 'email', and your table has columns 'user_id', 'user_name', 'user_email'
column_mapping = {
        "account_id": "account_id",
        "parent_id": "parent_account_id",
        "code": "account_code",
        "name": "account_name",
        "description": "description",
        "type": "type",
        "nivel": "level"
    }

base_path = Path(__file__).parent
print(base_path)
json_file_path = "plan_cuentas.json"

json_file_path = base_path.joinpath("data") / json_file_path
data = load_json_data(json_file_path)
#print(data)
scripts = generate_insert_scripts(data, table_name, column_mapping)

sql_file_path = "/insert_accounts.sql"
sql_file_path = Path(__file__).parent.joinpath("data") /sql_file_path
with open(sql_file_path, "w") as f:
    for statement in scripts:
        f.write(statement + "\n")