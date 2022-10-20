maney = int(input('Введите сумму вклада: '))
print ("money =", maney)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
Bank_1 = (per_cent['ТКБ'])
Bank_2 = (per_cent['СКБ'])
Bank_3 = (per_cent['ВТБ'])
Bank_4 = (per_cent['СБЕР'])
deposit = [int((maney*Bank_1)/100), int((maney*Bank_2)/100), int((maney*Bank_3)/100), int((maney*Bank_4)/100)]
print ("deposit =", deposit)
print ("Максимальная сумма, которую вы можете заработать —", max(deposit))