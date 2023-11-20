import re
from datetime import datetime


async def validate_phone(phone: str) -> str | None:
    pattern = re.compile(
        r"(^8|7|\+7)((\d{10})|(\s\(\d{3}\)\s\d{3}\s\d{2}\s\d{2}))"  # noqa
    )

    if pattern.match(phone):
        return "phone"


async def validate_date(date: str) -> str | None:
    patterns = ("%d.%m.%Y", "%Y-%m-%d")

    for pattern in patterns:
        try:
            datetime.strptime(date, pattern)
            return "date"
        except ValueError:
            pass


async def validate_email(email: str) -> str | None:
    pattern = re.compile(r"^\S+@\S+\.\S+$")  # noqa

    if pattern.match(email):
        return "email"


async def validate_value(value: str, validators: list[callable]) -> str:
    for validator in validators:
        type_of_value = await validator(value)

        if type_of_value is not None:
            return type_of_value

    return "text"
