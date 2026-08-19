import json
from copy import deepcopy

from configuration import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH
from data import ORDER_BODY, DEFAULT_HEADERS
from sender_stand_request import post_new_order, get_order_by_track


#Тест: Клиент создает заказ и проверка что по треку заказа можно получить данные о заказе
# Юлия Пушкарева, 46-я когорта, Дипломная работа: Яндекс Самокат
def test_create_order_and_get_by_track():

    # Шаг 1. Выполнить запрос на создание заказа
    order_body = deepcopy(ORDER_BODY)
    response_create = post_new_order(order_body)

    # Проверяем, что заказ создан успешно (код 201)
    assert response_create.status_code == 201, (
        f"Ожидался код 201, получен {response_create.status_code}"
    )

    # Шаг 2. Сохранить номер трека заказа
    track = response_create.json().get("track")
    assert track is not None, "Трек-номер не получен в ответе"

    # Шаг 3. Выполнить запрос на получение заказа по треку заказа
    response_get = get_order_by_track(track)

    # Шаг 4. Проверить, что код ответа равен 200
    assert response_get.status_code == 200, (
        f"Ожидался код 200, получен {response_get.status_code}"
    )
