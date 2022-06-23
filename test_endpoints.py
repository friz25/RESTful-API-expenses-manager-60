import pytest
import requests

url = 'http://127.0.0.1:5000'

def test_index_page():
    """тест - работает ли 'index page'?"""
    r = requests.get(url+'/')
    assert r.status_code == 200


def test_get_balance_in_transactions():
    """ Как (Пользователь) , я хочу (иметь снимок моих расходов) , чтобы я (знал, куда я трачу свои деньги) """
    r = requests.get(url+'/transactions/')
    data = r.json()
    assert r.status_code == 200
    """ проверяет содержимое ответа на наличие || баланса |||| 0 || . """
    assert data['balance'] == 0

def test_get_number_of_transactions():
    """ проверяет общее количество транзакций > 0 ? """
    r = requests.get(url+'/transactions/')
    data = r.json()

    assert r.status_code == 200
    assert len(data['transactions']) != 0


