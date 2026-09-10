# pythonSecurity

Repositorio con ejercicios de Python (fundamentos, estructuras de datos, funciones, validaciones) y un proyecto de seguridad: un escáner de puertos TCP.

## Contenido

- Ejercicios sueltos de práctica: listas, funciones, bucles, validaciones de usuarios, cálculos, etc.
- `escaneadorPuertos.py`: escáner de puertos TCP.
- `EnunciadosEjercicios/`: capturas con los enunciados de cada ejercicio.

## Escáner de puertos (`escaneadorPuertos.py`)

Script hecho con la librería `socket` de Python. Pide un host y un rango de puertos, intenta conectarse por TCP a cada uno (con timeout de 1 segundo) y reporta cuáles están abiertos, con un modo verboso opcional para ver el resultado puerto por puerto.

### Uso

```bash
python escaneadorPuertos.py
```

El script va a pedir:
1. El host a escanear (IP o nombre, ej. `127.0.0.1`)
2. Puerto inicial y puerto final del rango
3. Si querés modo verboso (`s`/`n`)

## Referencias

- https://www.python.org/
- https://code.visualstudio.com/
- https://thonny.org/
- https://www.python.org.ar
- https://pyscript.net/
- https://pypi.org/project/Flask/
- https://www.djangoproject.com/
