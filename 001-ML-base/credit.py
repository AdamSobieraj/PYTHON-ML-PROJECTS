import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

freq = 12
rate = 0.0675 # 6,75 %
years = 30
pv = 600_000
rate /= freq # konwersja stopy do okresu miesięcznego
nper = years * freq # liczba wszystkich okresów

print("rate per miesiąc {}".format(rate))
print("miesięcy {}".format(nper))

periods = np.arange(1,nper+1,dtype=int)

print("wektor kolejnych części odsetkowych dla równych płatności")
interest_equal = - np.around(npf.ipmt(rate,periods,nper,pv),2)
print(interest_equal)

principal_decreasing = np.around(np.zeros(nper)+(pv/nper),2)
print("malejące wektor, który będzie zawierał tylko część kapitałową spłacanej raty")
print(principal_decreasing)

balance = np.zeros(nper) + pv
print("balance beg")
print(balance)
balance_close = np.around(balance - np.cumsum(principal_decreasing),2)
print("balance closed")
print(balance_close)
print("principal")
print(np.cumsum(principal_decreasing))

balance_open = balance_close + principal_decreasing

interest_decreasing = np.around(balance_open * rate,2)
print("części odsetkowe każdej płatności")
print(interest_decreasing)

print("Wartość odsetek do zapłaty w wariancie kredytu w równych ratach wynosi: " + str("{:.2f}".format(interest_equal.sum())))
print("Wartość odsetek do zapłaty w wariancie kredytu w ratach malejących wynosi: " + str("{:.2f}".format(interest_decreasing.sum())))

plt.plot(interest_equal.cumsum(),label='raty równe')
plt.plot(interest_decreasing.cumsum(),label='raty malej?ce')
plt.legend()
plt.xlabel('Liczba okresów')
plt.ylabel('Skumulowana warto?? odsetek')
plt.show()