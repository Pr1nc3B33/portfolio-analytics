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


def sharpe_ratio(start_price, end_price, years, daily_returns, risk_free_rate=0):
    ann_return = annualized_return(start_price, end_price, years)
    vol = annualized_volatility(daily_returns)
    if vol == 0:
        raise ValueError("volatility cannot be zero")
    return (ann_return - risk_free_rate) / vol 


def max_drawdown(prices):
    if len(prices) < 2:
        raise ValueError("need at least two prices to compute drawdown")
    running_peak = prices[0]
    worst_drawdown = 0

    for price in prices:
        if price > running_peak:
            running_peak = price
        current_drawdown = (price - running_peak) / running_peak
        worst_drawdown = min(worst_drawdown, current_drawdown)               
    return worst_drawdown




