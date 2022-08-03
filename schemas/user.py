from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    user_cpf: str
    user_password: str
    user_password_confirm: str
    user_birth_date: str
    user_sex: str
    user_fone: str
    user_fone_whatsapp: str
    user_receive_offers: str
    user_receive_offers_whatsapp: str
    user_status: str
