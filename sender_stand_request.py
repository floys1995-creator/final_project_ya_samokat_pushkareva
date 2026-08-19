import requests
from configuration import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH
from data import DEFAULT_HEADERS

# Создание заказа
def post_new_order(order_body):

    response = requests.post(
        URL_SERVICE + CREATE_ORDER_PATH,
        json=order_body,
        headers=DEFAULT_HEADERS
    )
    return response

# Получение заказа по треку
def get_order_by_track(track):

    params = {"t": track}
    response = requests.get(
        URL_SERVICE + GET_ORDER_BY_TRACK_PATH,
        params=params,
        headers=DEFAULT_HEADERS
    )
    return response

