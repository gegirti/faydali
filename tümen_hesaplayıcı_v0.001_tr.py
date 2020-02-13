import datetime

Dogum_gunu = int(input("Ayın kaçında doğduğunuzu giriniz: "))
Dogum_ayi = int(input("Doğduğunuz ayı giriniz: "))
Dogum_yili = int(input("Doğduğunuz yılı giriniz: "))

DT = datetime.date(Dogum_yili, Dogum_ayi, Dogum_gunu)
Tumen_gun = datetime.timedelta(10000)

Tumen_hesabi = DT + Tumen_gun
print(Tumen_hesabi, "tarihi senin Tümen günün")