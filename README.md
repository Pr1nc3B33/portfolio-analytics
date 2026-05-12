# Portfolio Analytics

A Python application for analyzing investment portfolio performance using
quantitative finance metrics.

## Overview

This project computes core performance metrics for an investment portfolio
and benchmarks results against a market index (S&P 500). The implementation
focuses on mathematically rigorous, test-driven financial calculations.

## Current Features

- **Total Return**: Computes overall percentage return on a portfolio
- **Annualized Return**: Scales returns to a yearly basis with proper compounding
- **Annualized Volatility**: Computes standard deviation of returns scaled by the square root of 252 trading days

Each metric is unit-tested.

## Roadmap

- [ ] Sharpe Ratio (combines return and volatility into a risk-adjusted score)
- [ ] Max Drawdown (largest peak-to-trough decline)
- [ ] Live market data integration via yfinance
- [ ] Beta and Alpha calculations
- [ ] Performance visualizations

## Tech Stack

- Python 3
- pytest for testing
- (Planned) yfinance for live market data

## Running the Tests

\`\`\`
pytest test_analytics.py
\`\`\`

## About This Project

I'm building this as part of my transition into software engineering from a
career in film and TV production. I chose a quantitative finance project
specifically to stretch beyond tutorial-style work and engage with real
mathematical and engineering challenges.
