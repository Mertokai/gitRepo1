#10 dolar ödeyerek başla 
#10 dolar içinde 12 ayda bitiyor mu ? eğer öyleyse ayı yazdır 
# her ay bakiyeyi güncelle ve ona göre yaz 
#bakiye = önceki bakiye(g) * (1 + aylık faiz oranı(g)/12) - 10$ 
#her 12 ayda bir 10 dolar ekle 
#minimum aylık ödemeyi yazdır 

balance = float(input("Please Enter Balance: "))
annualInterest = float(input("Please Enter annual interest rate with decimal: "))
minPayment = float(input("Minimum Payment"))
month = 0
result = []
while month < 12: 
    balance = balance *(1 + annualInterest / 12) - minPayment
    month += 1 
    result.append(balance)
    if result[-1] < 0:
         print(str(round(result[-1],2)))
         print(month)
         break
    else:
        continue
result2 = []
while month>12: 
        balance = balance *(1 + annualInterest / 12) - minPayment * (month - 12)
        month += 1 
        result2.append(balance)
        if result2[-1] < 0:
            print(str(round(result[-1],2)))
            print(month)
            break
        else:
            continue
