def arithmetic_arranger(problems: str, show_answers: bool = False) -> str:
    operandos1 = []
    operandos2 = []
    guiones = []
    resultados = []
    if len(problems) >5:
        return('Error: Too many problems.')

    for problem in problems:
        partes = problem.split()
        operando1 = partes[0]
        operador = partes[1]
        operando2 = partes[2]

        if not operador in ('+', '-'):
            return("Error: Operator must be '+' or '-'.")

        if not operando1.isdigit() or not operando2.isdigit():
            return('Numbers must only contain digits.')

        if len(operando1)>4 or len(operando2)>4:
            return('Error: Numbers cannot be more than four digits.')        

        longitud_problema = max(len(operando1), len(operando2)) + 2
        operandos1.append(operando1.rjust(longitud_problema))
        operandos2.append(operador + operando2.rjust(longitud_problema-1))
        guiones.append('_'*longitud_problema)

        if show_answers:
            if operador == '+':
                respuesta = str(int(operando1) + int(operando2))
            else:
                respuesta = str(int(operando1) - int(operando2))
            resultados.append(respuesta.rjust(longitud_problema))


    problemas_verticales = '    '.join(operandos1) + '\n' + '    '.join(operandos2) + '\n' + '    '.join(guiones) + '\n' + '    '.join(resultados)
    
       
    
    return problemas_verticales

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}') 