import json
import time
import random
import json
from locust import HttpUser, task, tag, between

#cd C:\Users\LENOVO\Downloads\Лабораторная работа № 4-5-20210629
#pip install locust
#locust -f locust_test.py --host=http://localhost:23991 --tags get_task
#locust -f locust_test.py --host=http://localhost:23991 --tags get_task post_task

# Класс иммитирующий пользователя/клиента сервера
class RESTServerUser(HttpUser):
    wait_time = between(1.0, 5.0)       # время ожидания пользователя перед выполнением новой task

    # Метод, запускающийся самым первым для пользователя
    def on_start(self):
        self.client.get("/weatherforecast")

    # GET Запрос списка всех агентов
    @tag("get_task")
    @task(3)
    def get_task(self):
        # отправляем GET-запрос на адрес <SERVER>/mas/json/agents
        with self.client.get("/api/product", catch_response=True, name="/api/product") as response:
            # Если получаем код HTTP-код 200, то оцениваем запрос как "успешный"
            if response.status_code == 200:
                response.success()
            # Иначе обозначаем как "отказ"
            else:
                response.failure("Status code is %s" % response.status_code)

    # POST Добавление нового агента в БД
    @tag("post_task")
    @task(1)
    def post_task(self):
        number = random.randint(100, 10000000000)
        kilocalories = random.randint(1, 600)
        protein = random.randint(0, 60)
        fats = random.randint(1, 100)
        carbohydrates = random.randint(10, 120)
        POST_DATA = json.dumps({ 'name': 'product #' + str(number), 'kilocalories': str(kilocalories), 'protein': str(protein), 'fats': str(fats), 'carbohydrates': str(carbohydrates)})
        # отправляем POST-запрос с данными (POST_DATA) на адрес <SERVER>/mas/json/agents
        with self.client.post("/api/product", catch_response=True, name="/api/product", data=POST_DATA, headers={'content-type': 'application/json'}) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure("Status code is %s" % response.status_code)
