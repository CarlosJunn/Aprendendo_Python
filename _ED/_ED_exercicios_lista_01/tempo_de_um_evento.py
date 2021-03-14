dia, horario = input().split()
dia_inicio = int(dia)
hora_inicio, minuto_inicio, segundo_inicio = (int(e) for e in horario.split(':'))

dia, horario = input().split()
dia_final = int(dia)
hora_final, minuto_final, segundo_final = (int(e) for e in horario.split(':'))

dias = dia_final - dia_inicio
horas = hora_final - hora_inicio
minutos = minuto_final - minuto_inicio
segundos = segundo_final - segundo_inicio

if segundos < 0:
    segundos += 60
    minutos -= 1
if minutos < 0:
    minutos += 60
    horas -= 1
if horas < 0:
    horas += 24
    dias -= 1
if dias < 0 or (dias == 0 and horas == 0 and minutos == 0 and segundos == 0):
    print('Data inválida!')
else:
    print(f'{dias} dia(s)')
    print(f'{horas} hora(s)')
    print(f'{minutos} minuto(s)')
    print(f'{segundos} segundo(s)')