count = 0
summe = 0.0
while True:
    sval = input("Geben Sie eine Zahl ein: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except ValueError:
        print("Invalid input")
        continue
    count += 1
    summe += fval

print(summe, count, summe / count)
