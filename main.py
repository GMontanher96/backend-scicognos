from fastapi import FastAPI
from schemas.user import User
from config.db import connection
from models.index import users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS VERIFY
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000/api/new",
    "http://localhost:3001",
    "http://127.0.0.1:8000/api/users",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ENDING CORS VERIFY

# ROUTES API

@app.get('/api/users')
async def index():
    data = connection.execute(users.select()).fetchall()
    return {
        "success": True,
        "data": data
    }

# insert data
@app.post('/api/users/new')
async def store(user:User):
    data = connection.execute(users.insert().values(
    user_name=user.user_name,
    user_email=user.user_email,
    user_cpf=user.user_cpf,
    user_password=user.user_password,
    user_password_confirm=user.user_password_confirm,
    user_birth_date=user.user_birth_date,
    user_sex=user.user_sex,
    user_fone=user.user_fone,
    user_fone_whatsapp=user.user_fone_whatsapp,
    user_receive_offers=user.user_receive_offers,
    user_receive_offers_whatsapp=user.user_receive_offers_whatsapp,
    user_status=user.user_status
    ))

    if data.is_insert:
        return {
            "success": True,
            "msg": "User Store Successfully"
        }
    else:
        return {
            "success": False,
            "msg": "Some Problem"
        }

# edit data

@app.patch('/api/users/{id}')
async def edit_data(id:int):
    data = connection.execute(users.select().where(users.c.id == id)).fetchall()
    return {
        "success": True,
        "data": data
    }

# update data

@app.put('/api/users/{id}')
async def update(id: int, user: User):
    data = connection.execute(users.update().values(
     user_name=user.user_name,
    user_email=user.user_email,
    user_cpf=user.user_cpf,
    user_password=user.user_password,
    user_password_confirm=user.user_password_confirm,
    user_birth_date=user.user_birth_date,
    user_sex=user.user_sex,
    user_fone=user.user_fone,
    user_fone_whatsapp=user.user_fone_whatsapp,
    user_receive_offers=user.user_receive_offers,
    user_receive_offers_whatsapp=user.user_receive_offers_whatsapp,
    user_status=user.user_status,
    ).where(users.c.user_id == id))
    if data:
        return {
            "success": True,
            "msg": "User Update Successfully"
        }
    else:
        return {
            "success": False,
            "msg": "Some Problem"
        }
# delete data

@app.delete('/api/users/{id}')
async def delete(id: int):
    data = connection.execute(users.delete().where(users.c.user_id == id))
    if data:
        return {
            "success": True,
            "msg": "User Delete Successfully"
        }
    else:
        return {
            "success": False,
            "msg": "Some Problem"
        }

# search data

@app.get('/api/users/{search}')
async def search(search):
    data = connection.execute(users.select().where(
        users.c.name.like('%'+search+'%'))).fetchall()
    return {
        "success": True,
        "data": data
    }

#