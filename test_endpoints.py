import pytest
import requests

url = 'http://127.0.0.1:5000'


# noinspection LanguageDetectionInspection
class TestTransactions():

    """=====================================================
        GET (tests)
        =====================================================
        Получить список транзакций :

        Как (Пользователь) , я хочу (иметь снимок моих расходов) ,
        чтобы я (знал, куда я трачу свои деньги)
        ====================================================="""
    def test_index_page(self):
        """тест - работает ли 'index page'?"""
        r = requests.get(url + '/')
        assert r.status_code == 200

    def test_get_balance_in_transactions(self):
        """ проверяет содержимое ответа на наличие || баланса |||| 0 || . """
        r = requests.get(url + '/transactions/')
        data = r.json()
        assert r.status_code == 200
        assert data['balance'] == 0

    def test_get_number_of_transactions(self):
        """ проверяет общее количество транзакций > 0 ? """
        r = requests.get(url + '/transactions/')
        data = r.json()

        assert r.status_code == 200
        assert len(data['transactions']) != 0

    def test_individual_transaction_fields(self):
        """тесты для проверки полей внутри транзакций """
        r = requests.get(url + '/transactions/')
        data = r.json()
        fields = list(data['transactions'])

        assert r.status_code == 200
        assert fields[0]['amount'] >= 0.00
        assert fields[0]['current_balance'] < 240
        assert 'jeans' in fields[0]['description']
        assert 0 < fields[0]['id']
        assert 300 == fields[0]['initial_balance']
        assert "2019-01-12 09:00:00" == fields[0]['time']
        assert fields[0]['type'] != 'income'

    """=====================================================
        POST (tests)
        =====================================================
        Создайте новую транзакцию :
        
        Как (Пользователь) , я хочу (иметь запись моих расходов) так, чтобы 
        Я (знал, куда идут мои деньги)
        ====================================================="""

    def test_post_number_of_transactions(self):
        """ проверяет общее количество транзакций > 0 ? """
        r = requests.get(url + '/transactions/')
        data = r.json()

        assert r.status_code == 200
        assert len(data['transactions']) != 0

    def test_individual_transaction_fields(self):
        """тесты для проверки полей внутри транзакций """
        r = requests.get(url + '/transactions/')
        data = r.json()
        fields = list(data['transactions'])

        assert r.status_code == 200
        assert fields[0]['amount'] >= 0.00
        assert fields[0]['current_balance'] < 240
        assert 'jeans' in fields[0]['description']
        assert 0 < fields[0]['id']
        assert 300 == fields[0]['initial_balance']
        assert "2019-01-12 09:00:00" == fields[0]['time']
        assert fields[0]['type'] != 'income'
    """=====================================================
        PUT (tests)
        =====================================================
        Обновить отдельную транзакцию :
        
        Как (Пользователь) , я хочу (отредактировать конкретную транзакцию)
        так, чтобы (У меня был правильный баланс)
        ====================================================="""
    def test_put_number_of_transactions(self):
        """ проверяет общее количество транзакций > 0 ? """
        r = requests.get(url + '/transactions/')
        data = r.json()

        assert r.status_code == 200
        assert len(data['transactions']) != 0

    def test_individual_transaction_fields(self):
        """тесты для проверки полей внутри транзакций """
        r = requests.get(url + '/transactions/')
        data = r.json()
        fields = list(data['transactions'])

        assert r.status_code == 200
        assert fields[0]['amount'] >= 0.00
        assert fields[0]['current_balance'] < 240
        assert 'jeans' in fields[0]['description']
        assert 0 < fields[0]['id']
        assert 300 == fields[0]['initial_balance']
        assert "2019-01-12 09:00:00" == fields[0]['time']
        assert fields[0]['type'] != 'income'
    """=====================================================
        DELETE (tests)
        =====================================================
        Удалить отдельную транзакцию :
        
        Как (Пользователь) , я хочу (удалить транзакцию) так,
        чтобы (У меня был правильный баланс в моем менеджере расходов)
        ====================================================="""
    def test_del_number_of_transactions(self):
        """ проверяет общее количество транзакций > 0 ? """
        r = requests.get(url + '/transactions/')
        data = r.json()

        assert r.status_code == 200
        assert len(data['transactions']) != 0

    def test_individual_transaction_fields(self):
        """тесты для проверки полей внутри транзакций """
        r = requests.get(url + '/transactions/')
        data = r.json()
        fields = list(data['transactions'])

        assert r.status_code == 200
        assert fields[0]['amount'] >= 0.00
        assert fields[0]['current_balance'] < 240
        assert 'jeans' in fields[0]['description']
        assert 0 < fields[0]['id']
        assert 300 == fields[0]['initial_balance']
        assert "2019-01-12 09:00:00" == fields[0]['time']
        assert fields[0]['type'] != 'income'

if __name__ == '__main__':
    pytest.main()
