from analytics import total_return, annualized_return, annualized_volatility
import pytest


def test_total_return_gain():
    result = total_return(100, 120)
    assert result == 0.2  # 100 → 120 is a 20% gain #


def test_total_return_loss():
    result = total_return(100, 80)
    assert result == -0.2    


def test_no_gain():
    result = total_return(100, 100)
    assert result == 0

def test_zero_start_raises_error():
    with pytest.raises(ValueError):
        total_return(0, 100)


def test_double_annualized_return():
    result = annualized_return(100, 200, 1)
    assert result == 1.0


def test_multi_year_annualized_return():
    result = annualized_return(100, 200, 10)
    assert result == pytest.approx(0.0717734625)


def test_zero_start_annualized_error():
    with pytest.raises(ValueError):
        annualized_return(0, 200, 1)


def test_zero_years_annualized_error():
    with pytest.raises(ValueError):
        annualized_return(100, 200, 0)


def test_annualized_volatility_zero_for_flat_returns():
    result = annualized_volatility([0.01, 0.01, 0.01])
    assert result == 0                  


def test_annualized_volatility_daily_return():
    result = annualized_volatility([0.01, -0.005, 0.02, -0.01, 0.015])
    assert result == pytest.approx(0.2048, rel=0.01) 

def test_annualized_volatility_too_short_error():
    with pytest.raises(ValueError):
        annualized_volatility([0.01])


def test_annualized_volatility_empty_error():
    with pytest.raises(ValueError):
        annualized_volatility([])     














