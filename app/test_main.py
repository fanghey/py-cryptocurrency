from unittest.mock import patch
from app.main import cryptocurrency_action
@patch('app.main.get_exchange_rate_prediction')
def test_buy_more(mock_predict):
    mock_predict.return_value = 110 
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"
