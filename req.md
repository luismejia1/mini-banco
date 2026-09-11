# mini-banco — v1

**Fecha límite:** domingo 13 de septiembre de 2026
**Terminado =** corre sin explotar ante entradas malas + está en GitHub. Feo cuenta como
terminado.

**Qué se practica acá:** clases y excepciones propias. Nada más. El resto del proyecto es
deliberadamente aburrido y conocido para que lo único nuevo sea eso.

## Requisitos (esto y nada más)

1. **Crear cuenta.** Titular y un número de cuenta único que asigna el programa.
2. **Depositar** en una cuenta.
3. **Retirar** de una cuenta.
4. **Consultar saldo** de una cuenta.
5. **Historial de movimientos** de una cuenta: qué operación, cuánto, y el saldo que quedó.
6. **Transferir** de una cuenta a otra.
7. **Excepciones propias.** Mínimo `SaldoInsuficiente` y `MontoInvalido`, las dos
   heredando de una base común del proyecto.

## Decisiones ya tomadas (no reabrir)

- Un solo archivo `.py`. Sin módulos.
- Solo librería estándar.
- **Todo en memoria.** Al cerrar el programa se pierde todo. La persistencia ya la
  practicaste en track-gastos.
- Menú por `input()` en un loop, como en track-gastos. A propósito repetido.
- **La clase nunca imprime y nunca pide input.** Lanza excepciones. El menú es el único
  que atrapa, imprime y pregunta. Esta separación es media razón de ser del proyecto.
- Montos con `int` o con `float`: decidí en un minuto y no lo cambies.
- Sin IA escribiendo el código. Preguntar conceptos sí, pedir soluciones no.

## Casos que no deben tumbar el programa

- Depositar o retirar un monto negativo o cero.
- Escribir letras donde va un monto.
- Retirar exactamente todo el saldo.
- Retirar más de lo que hay.
- Transferir a la misma cuenta.
- Operar sobre un número de cuenta que no existe.

## Prohibido en v1

- Guardar en archivo o base de datos
- Tipos de cuenta distintos, ahorro y corriente, con herencia
- Intereses, comisiones, límites de retiro
- Varias monedas
- Fechas en los movimientos
- Borrar o cerrar cuentas
- Login, usuarios, contraseñas
- Colores o formato lindo en la terminal
- Tests
- Cualquier cosa que empiece con "sería genial si..."

Todo eso es v2. v2 solo existe si v1 está terminada.

## Orden de trabajo

1. Clase con saldo y depositar, y un `print` del saldo al final del archivo. Con eso ya
   rompiste el cero el primer día.
2. Retirar, y la primera excepción propia cuando no alcanza.
3. El menú por `input()` usando la clase y atrapando esa excepción.
4. Historial.
5. Transferencia entre dos cuentas.

Cada paso deja el programa usable. Si el domingo llegás hasta el 4, se entrega hasta el 4.

## Reglas anti-sabotaje

- Ganas de rediseñar las clases a mitad de camino = seguir escribiendo, no rediseñar.
- 30 min de código malo le ganan a 2 horas de diagrama de clases.
- Si aparece la duda de si algo "debería ser un método o una función suelta", elegí en un
  minuto y seguí.
