#
# 種別（月間電気料金）
# 区別   単位       料金単価（円）　 　　　　　　　　　　　　　
# 10    1契約.A       341
# 15    1契約.A       511.5
# 20    1契約.A       682
# 30    1契約.A      1023
# 40    1契約.A      1364
# 50    1契約.A      1705
# 60    1契約.A      2046
#
# 電気量料金
# 使用量                    単位      料金単価（円）
# 最初の120kwh              1KWh       23.25
# 120kwhを超え300kwhまで    1KWh       29.35
# 300kwhを超える分          1KWh       32.96
#
# ※基本料金の設定は特にありません
#

# 契約アンペア毎の料金単価
#         区分   料金単価
amps10 = ('10A', 341,)
amps15 = ('15A', 511.5,)
amps20 = ('20A', 682,)
amps30 = ('30A', 1023,)
amps40 = ('40A', 1346,)
amps50 = ('50A', 1705,)
amps60 = ('60A', 2046,)

amps = [amps10, amps15, amps20, amps30, amps40, amps50, amps60]

# 契約種別
# type_a = ('従量電灯A', 'A')
# type_b = ('従量電灯B', 'B')
# type_c = ('従量電灯C', 'C')
#
# types = [type_a, type_b, type_c]

# 電気使用量ごとの料金単価 ( a < n <= b )
#        from(a) to(b) 料金単価
amount120 = (0, 120, 23.25,)
amount300 = (120, 300, 29.35,)
amountmax = (300, 99999999, 32.96,)

amounts = [amount120, amount300, amountmax]

print('--------------------')
print('契約区分')
index = 0
for amp in amps:
    print(str(index) + '. ' + amp[0])
    index += 1

# print('契約種別')
# index = 0
# for type in types:
#     print(str(index) + '. ' + type.info())
#     index += 1

print('--------------------')

amp_order = int(input('契約区分(A)を選択してください: '))
selected_amp = amps[amp_order]

# type_order = int(input('契約種別を選択してください: '))
# selected_type = types[type_order]

answer = int(input('電気使用量(kWh)を入力してください: '))
print('--------------------')

total_price = 0
result = 0
for amount in amounts:
    if amount[0] < answer <= amount[1]:
        total_price += (answer - amount[0]) * amount[2]
        break
    else:
        total_price += (amount[1] - amount[0]) * amount[2]

total_price += selected_amp[1]
result = round(total_price)

print('電気量利用料金は ' + str(result) + ' 円です')
