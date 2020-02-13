import datetime

Dogum_gunu = int(input("Please enter your Birth Year: "))
Dogum_ayi = int(input("Please enter your Birth Month: "))
Dogum_yili = int(input("Please enter your Birth Day: "))

DT = datetime.date(Dogum_yili, Dogum_ayi, Dogum_gunu)
Tumen_gun = datetime.timedelta(10000)

Tumen_hesabi = DT + Tumen_gun
print(Tumen_hesabi, "is you myriad day!")
