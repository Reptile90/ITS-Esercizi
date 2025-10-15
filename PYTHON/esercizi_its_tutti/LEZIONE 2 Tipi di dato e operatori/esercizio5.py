'''Si scriva un programma che converta la temperatura da Fahrenheit a Celsius utilizzando la formula

gradiCelsius=5∗(gradiFahrenheit−32)/9

Si inizializzi una temperatura espressa in gradi Fahrenheit con un numero intero.

La temperatura deve essere convertita e visualizzata in gradi Celsius con un numero in virgola mobile con una precisione di un decimo di grado.

Un possibile esempio di output potrebbe essere il seguente:

72 gradi Fahrenheit corrispondono a 22.2 gradi Celsius.'''


fahrenheit:int = 72

celsius = 5 * (fahrenheit - 32) / 9

print(f"{fahrenheit}° fahrenheit equivalgono a {celsius:.1f}°celsius")

