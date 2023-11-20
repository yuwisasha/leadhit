## Формы находящиеся в базе данных

```
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
```

## Запуск

1. 
```
git clone https://github.com/yuwisasha/leadhit.git
```

2. 
```
make build
```

3. 
```
make up
```

## Тестирование

Запускает запросы с тестовыми данными из директории tests

```
make test
```
