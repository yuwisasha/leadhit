from fastapi import APIRouter, Request

from app.db import forms_collection
from app.validators import (
    validate_value,
    validate_date,
    validate_phone,
    validate_email,
)

router = APIRouter()


@router.post("/get_form/")
async def get_form(r: Request):
    form = r.query_params
    db_form = {}

    for field, value in form.items():
        value_type = await validate_value(
            value.strip(),
            validators=[validate_date, validate_phone, validate_email],
        )
        db_form[field] = value_type

    form_name = None

    if (forms := await forms_collection.find().to_list(length=None)) is not None:
        for form in forms:
            form.pop("_id")
            name = form.pop("name")
            if form.items() <= db_form.items():
                form_name = name

    return db_form if form_name is None else form_name
