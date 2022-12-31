# Desafio 014 - Escreva um programa que converta uma temperatura digitada em °C( graus celsius) e converta para °F(Fahrenheit).

temperatura_graus_celcius = int(input('Digite a temperatura em ºC[graus celsius]: '))
# C = A escala Celsius é "baseada na temperatura de congelação e de ebulição da água".
temperatura_fahrenheit = 1.8 * temperatura_graus_celcius + 32  #fórmula F = 1,8 * C + 32
# F = A escala Fahrenheit é "baseada em uma temperatura de referência específica do corpo humano".
print(f'A temperatura de ºC {temperatura_graus_celcius} para ºF {temperatura_fahrenheit}.')



