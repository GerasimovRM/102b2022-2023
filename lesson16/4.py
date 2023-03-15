def spamogenerator(email, name, date, place="Перми"):
    return f"""To: {email}
Здравствуйте, {name}!
Были бы рады видеть вас на встрече начинающих программистов """ \
           f"""в {place}, которая пройдет {date}."""


kwargs = {"email": "ivan.melnikov@email.com",
          "name": 'Иван',
          "date": "27.03.2023",
          "place": "Лицей №1, г. Пермь"}
kwargs2 = {"email": "romagrizly@gmail.com",
           "name": 'Roman',
           "date": "27.03.2023"}
print(spamogenerator(**kwargs))
print(spamogenerator(**kwargs2))
