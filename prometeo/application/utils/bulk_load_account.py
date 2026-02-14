from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from pydantic import BaseModel
from typing import List, Optional
import uuid
import urllib

from application.utils.database import SessionLocal, get_db


# --- Modelos de Pydantic para recibir el JSON ---
class AccountSchema(BaseModel):
    account_code: str
    account_name: str
    category: str
    normal_side: str
    is_postable: bool
    parent_code: Optional[str] = None
    level: int

class BulkAccountUpload(BaseModel):
    tenant_id: uuid.UUID
    accounts: List[AccountSchema]

class Account(BaseModel):
    tenant_id: uuid.UUID
    account_id: Optional[uuid.UUID] = None
    account_code: str
    account_name: str
    category: str
    normal_side: str
    parent_account_id: Optional[uuid.UUID] = None
    is_postable: bool
    level: int
   
app = FastAPI()



router = APIRouter()

@router.post("/accounts/import-chart")
def import_chart_of_accounts(payload: BulkAccountUpload, db: Session = Depends(get_db)):
    """
    Importa el plan de cuentas procesado desde Excel.
    Ordena por nivel para asegurar que el padre exista antes que el hijo.
    """
    # 1. Ordenar por nivel (1, 2, 3...)
    sorted_accounts = sorted(payload.accounts, key=lambda x: x.level)
    
    # Mapa para convertir códigos de texto a IDs de base de datos (UUID)
    code_to_uuid_map = {}

    try:
        for acc in sorted_accounts:
            # 2. Buscar el ID del padre si no es nivel 1
            parent_id = None
            if acc.parent_code:
                parent_id = code_to_uuid_map.get(acc.parent_code)
                if not parent_id:
                    raise HTTPException(
                        status_code=400, 
                        detail=f"Error jerárquico: No se encontró el padre {acc.parent_code} para {acc.account_code}"
                    )

            # 3. Crear el registro en la base de datos
            new_account = Account(
                tenant_id=payload.tenant_id,
                account_code=acc.account_code,
                account_name=acc.account_name,
                category=acc.category,
                normal_side=acc.normal_side,
                parent_account_id=parent_id,
                is_postable=acc.is_postable,
                level=acc.level
            )
            
            db.add(new_account)
            db.flush() # Genera el UUID sin hacer commit aún
            
            # Registrar en el mapa para que sus hijos puedan encontrarlo
            code_to_uuid_map[acc.account_code] = new_account.account_id

        db.commit()
        return {"status": "success", "accounts_created": len(sorted_accounts)}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Fallo en la carga: {str(e)}")