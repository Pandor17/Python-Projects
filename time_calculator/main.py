def add_time(start: str, duration: str, day: str = None):
    #Calling add_time('8:16 PM', '466:02', 'tuesday') should return '6:18 AM, Monday (20 days later)'
    
    #aquí saco los datos pasados por parámetros
    tiempo_actual, franja_actual = start.split()
    hora_actual, minuto_actual = tiempo_actual.split(':')
    hora_sumar, minuto_sumar = duration.split(':')
    

    #creo una lista de franjas y dias para cuando sume la duración ir avanzando en la lista que corresponda
    franja_horaria = ['AM', 'PM'] 
    dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Mecánica de actualización del tiempo
    minuto_final = (int(minuto_actual) + int(minuto_sumar)) % 60
    hora_final = (int(hora_actual) + int(hora_sumar) + (int(minuto_actual) + int(minuto_sumar))// 60) % 12

    # Ajustar la hora_final para que no sea 0
    if hora_final == 0:
        hora_final = 12

    # Calcular el número total de horas sumadas
    total_horas = int(hora_actual) + int(hora_sumar) + (int(minuto_actual) + int(minuto_sumar)) // 60
    cambios_franja = total_horas // 12  # Contar cambios de AM a PM
    franja_final = franja_horaria[(franja_horaria.index(franja_actual) + cambios_franja) % 2]

    # Calcular el nuevo día
    if franja_actual == 'PM':
        total_dias = int(cambios_franja//2 + cambios_franja%2)
    else:
        total_dias = int(cambios_franja//2)

    if day:
        dia_actual = day.capitalize()
        indice_dia_semana = dias.index(dia_actual)
        dia_final = dias[(indice_dia_semana + total_dias) % 7]
    else:
        dia_final = ''
    
   

    resultado = ''
    # Calcular si hay días transcurridos después de la suma de minutos
    if (int(minuto_actual) + int(minuto_sumar)) // 60 > 0:
        total_dias += (int(minuto_actual) + int(minuto_sumar)) // 60 // 24  # Ajustar el total de días

    if total_dias == 0:
        resultado += f'{hora_final}:{minuto_final:02} {franja_final}{", " + dia_final if dia_final else ""}'
    elif total_dias == 1:
        resultado += f'{hora_final}:{minuto_final:02} {franja_final}{", " + dia_final if dia_final else ""} (next day)'
    else:
        resultado += f'{hora_final}:{minuto_final:02} {franja_final}{", " + dia_final if dia_final else ""} ({total_dias} days later)'

    print(resultado)
    return resultado

if __name__ == '__main__':
    add_time('3:30 PM', '2:12', 'Monday')
