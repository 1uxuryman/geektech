nar = int(input("Naryn °C ?"))
tal = int(input("Talas °C ?"))
lal = int(input("Jalal - Abad °C ?"))
osh = int(input("Osh °C ?"))
chu = int(input("Chyi °C  ?"))
bat = int(input("Batken °C  ?"))
ysk = int(input("Yssyk - Kol °C ?"))
sum_regions = nar + tal + lal + osh + chu + bat + ysk
s = sum_regions/7
s2 = '%.1f' % s
print(f'Cредний показатель температуры воздуха по КР на сегодня {s2} °C' )








