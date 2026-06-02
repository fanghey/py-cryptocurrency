from unittest.mock import patch
from app.main import cryptocurrency_action

@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_predict: "Mock") -> None:
    mock_predict.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"

@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_predict: "Mock") -> None:
    mock_predict.return_value = 90
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"

@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_predict: "Mock") -> None:
    mock_predict.return_value = 102
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
