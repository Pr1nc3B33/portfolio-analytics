import math
import statistics


def total_return(start_price, end_price):
    if start_price == 0:
        raise ValueError("start_price cannot be zero")
    return (end_price - start_price) / start_price


def annualized_return(start_price, end_price, years):
    if start_price == 0:
        raise ValueError("start_price cannot be zero")
    if years <= 0:
        raise ValueError("years must be greater than zero")
    return (end_price / start_price) ** (1 / years) - 1    # CAGR = Compound Annual Growth Rate


def annualized_volatility(daily_returns):
    if len(daily_returns) < 2:
        raise ValueError("need at least 2 daily_returns to compute volatility")
    return statistics.stdev(daily_returns) * math.sqrt(252)   





