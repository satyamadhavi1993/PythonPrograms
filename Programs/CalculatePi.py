# Leibniz's Formula for Pi: 𝜋 = 4∑((−1)**𝑘) * (1/2𝑘+1) where 𝑘≥0

def calculate_pi(n):
    pi = 0
    for i in range(n):
        pi += ((-1) ** i) / ((2 * i + 1))
    return 4 * pi


n = 1000
print(calculate_pi(n))
