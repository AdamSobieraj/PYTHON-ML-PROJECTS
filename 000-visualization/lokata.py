import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

# Dane
initial_price = 120000  # Początkowa cena mieszkania w PLN
growth_rate = 0.05  # Roczny wzrost cen mieszkań (5%)
years = 5  # Okres oszczędzania w latach
months = years * 12  # Liczba miesięcy
bank_rate = 0.12  # Nominalna roczna stopa procentowa banku (12%)
monthly_rate = bank_rate / 12  # Miesięczna stopa procentowa

# Przyszła cena mieszkania
future_house_price = initial_price * (1 + growth_rate) ** years

# Miesięcznej wpłaty do banku
pmt = npf.pmt(rate=monthly_rate, nper=months, pv=0, fv=future_house_price)

# Dane do wykresu
monthly_deposit = pmt
time = np.arange(1, months + 1)

# Wartość mieszkania w każdym miesiącu (liniowy wzrost)
house_prices = initial_price * (1 + growth_rate) ** (time / 12)

# Wartość lokaty na koniec każdego miesiąca
balance = npf.fv(rate=monthly_rate, nper=time, pmt=monthly_deposit, pv=0)

# Wykres
plt.figure(figsize=(10, 6))
plt.plot(time, house_prices, label='Cena mieszkania', color='red')
plt.plot(time, balance, label='Wartość lokaty', color='green')
plt.title('Cena mieszkania i wartość lokaty w czasie')
plt.xlabel('Miesiące')
plt.ylabel('Wartość (PLN)')
plt.legend()
plt.grid(True)
plt.show()

# Wyniki
print(f"Przewidywana cena mieszkania za 5 lat: {future_house_price:.2f} PLN")
print(f"Kwota miesięcznej wpłaty do banku: {monthly_deposit:.2f} PLN")