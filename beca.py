PA = float(input())
horas = int(input())
Saber_Pro = int(input())
BI = int(input())

print(f"PA: {PA}")
print(f"horas: {horas}")
print(f"Saber Pro: {Saber_Pro}")
print(f"BI: {BI}")

if BI == 1:
    print(True)
elif PA < 3.5:
    print(False)
elif horas < 100:
    print(False)
elif Saber_Pro < 260:
    print(False)
else:
    print(True)
result= BI == 1 or (PA >= 3.5 and horas >= 100 and Saber_Pro >= 260)
