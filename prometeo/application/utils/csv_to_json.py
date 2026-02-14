import pandas as pd
import json
import uuid
from pathlib import Path


def convert_excel_to_accounting_json(file_path, entity_id):
    # Leer el archivo Excel
    df = pd.read_excel(file_path)
    
    accounts = []
    
    for index, row in df.iterrows():
        # Determinar el nivel basado en los puntos del código (ej: 1.1.01 -> nivel 3)

        print(f"Index: {index}, Code: {row['code']}, Name: {row['name']}, Category: {row['type']}, Normal Side: {row['normal_side']}, Is Postable: {row['is_postable']}")


        level = str(row['code']).count('.') + 1
        
        # Determinar el código padre (si existe)
        code_str = str(row['code'])

        parent_code = None
        if '.' in code_str:
            parent_code = '.'.join(code_str.split('.')[:-1])

        account = {
            "account_code": code_str,
            "account_name": row['name'].lstrip(),
            "category": row['type'].upper(),
            "normal_side": row['normal_side'].upper(),
            "is_postable": bool(row['is_postable']),
            "parent_code": parent_code,
            "level": level
        }
        accounts.append(account)
    
    # Estructura final para la API
    final_payload = {
        "entity_id": entity_id,
        "accounts": accounts
    }
    
    # Guardar como JSON
    with open('plan_cuentas_listo.json', 'w', encoding='utf-8') as f:
        json.dump(final_payload, f, indent=2, ensure_ascii=False)
    
    print(f"Éxito: Se han procesado {len(accounts)} cuentas.")

def create_sql_insert_statements(json_file, table_name):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    entity_id = data['entity_id']
    accounts = data['accounts']
    
    sql_statements = []
    
    for account in accounts:
        columns = ', '.join(['entity_id'] + list(account.keys()))
        values = ', '.join([f"'{entity_id}'"] + [f"'{str(value).replace("'", "''")}'" for value in account.values()])
        
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        sql_statements.append(sql)
    
    with open('insert_accounts.sql', 'w', encoding='utf-8') as f:
        for statement in sql_statements:
            f.write(statement + '\n')
    
    print(f"Éxito: Se han generado {len(sql_statements)} sentencias SQL.")


    
# Uso del script
if __name__ == '__main__':
    folder = Path(r"C:\Users\GOLIAT_PC01\Downloads")
    filename = 'PlanCuentas_ABC.xls'
    file_path = folder / filename
    convert_excel_to_accounting_json(file_path, str(uuid.uuid4()))