import math
from scipy.stats import norm


def black_scholes(option_type,S,K,T_days,r,sigma,days_in_year=252):
    T = T_days / days_in_year

    # Calculate d1 and d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Calculate the option price based on option type (call or put)
    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'")

    return option_price

# Example usage
if __name__ == "__main__":
    S = 100      # Stock price
    K = 95       # Strike price
    T_days = 30  # Time to maturity in days
    r = 0.05     # Risk-free rate (5%)
    sigma = 0.2  # Volatility (20%)

# Calculate the price of a call option
    call_price = black_scholes('call', S, K, T_days, r, sigma)
    print(f"Call Option Price: {call_price:.2f}")

# Calculate the price of a put option
    put_price = black_scholes('put', S, K, T_days, r, sigma)
    print(f"Put Option Price: {put_price:.2f}")