open_file = open('CupcakeInvoices.csv')

total = 0

for line in open_file:
    line = line.strip()
    values = line.split(',')
    quanity = int(values[3])
    price = float(values[4])
    total = total + (quanity * price)

print(total)

open_file.close()