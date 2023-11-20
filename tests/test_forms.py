import pytest

from httpx import Response

form_1 = {
    "user_name": "yuwisasha",
    "order_date": "26.05.2000",
    "lead_email": "yuwi@mail.ru",
    "phone_number": "+79223227697",
}

form_2 = {
    "user_name": "sanek",
    "password": "123321",
}

form_3 = {
    "user_name": "sane4ek",
    "lead_email": "qwezxc@gmail.com",
    "password": "123",
}


@pytest.mark.asyncio
async def test_form_1_1(client) -> None:
    response: Response = await client.post("/get_form/", params=form_1)

    assert response.status_code == 200
    assert response.json() == "OrderForm"


@pytest.mark.asyncio
async def test_form_1_2(client) -> None:
    form_1["name"] = "sanek"

    response: Response = await client.post("/get_form/", params=form_1)

    assert response.status_code == 200
    assert response.json() == "OrderForm"


@pytest.mark.asyncio
async def test_form_1_3(client) -> None:
    form_1.pop("user_name")

    response: Response = await client.post("/get_form/", params=form_1)

    assert response.status_code == 200
    assert response.json() == {
        "name": "text",
        "phone_number": "phone",
        "order_date": "date",
        "lead_email": "email",
    }


@pytest.mark.asyncio
async def test_form_2_1(client) -> None:
    response: Response = await client.post("/get_form/", params=form_2)

    assert response.status_code == 200
    assert response.json() == "LoginForm"


@pytest.mark.asyncio
async def test_form_2_2(client) -> None:
    form_2.pop("user_name")

    response: Response = await client.post("/get_form/", params=form_2)

    assert response.status_code == 200
    assert response.json() == {
        "password": "text",
    }


@pytest.mark.asyncio
async def test_form_2_3(client) -> None:
    form_2["date"] = "2000-05-26"

    response: Response = await client.post("/get_form/", params=form_2)

    assert response.status_code == 200
    assert response.json() == {
        "password": "text",
        "date": "date",
    }


@pytest.mark.asyncio
async def test_form_3_1(client) -> None:
    response: Response = await client.post("/get_form/", params=form_3)

    assert response.status_code == 200
    assert response.json() == "RegistrationForm"


@pytest.mark.asyncio
async def test_form_3_2(client) -> None:
    form_3["date"] = "26.05.2000"

    response: Response = await client.post("/get_form/", params=form_3)

    assert response.status_code == 200
    assert response.json() == "RegistrationForm"


@pytest.mark.asyncio
async def test_form_3_3(client) -> None:
    form_3.pop("password")

    response: Response = await client.post("/get_form/", params=form_3)

    assert response.status_code == 200
    assert response.json() == {
        "lead_email": "email",
        "user_name": "text",
        "date": "date",
    }
