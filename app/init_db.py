from app.db import forms_collection, client

form_1 = {
    "name": "OrderForm",
    "user_name": "text",
    "order_date": "date",
    "lead_email": "email",
    "phone_number": "phone",
}

form_2 = {
    "name": "LoginForm",
    "user_name": "text",
    "password": "text",
}

form_3 = {
    "name": "RegistrationForm",
    "user_name": "text",
    "lead_email": "email",
    "password": "text",
}


async def init_db() -> None:
    forms_collection.insert_many([form_1, form_2, form_3])


async def drop_db() -> None:
    await client.drop_database("leadhit")
