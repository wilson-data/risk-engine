returns = [-0.01, 0.02, -0.03, 0.01]

returns.sort()
var = returns[int(0.05 * len(returns))]

print("VaR:", var)
