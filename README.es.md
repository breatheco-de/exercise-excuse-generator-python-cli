<!--hide-->
# Generador de excusas CLI (en python)
<!--endhide-->

Disneylandia para procrastinadores y personas "muy relajadas"

Este proyecto es ideal para evitar a alguien molestoso, ¡no toma más de 20 líneas de código y puede salvarte por el resto de tu vida!

![this exact same picture](https://github.com/breatheco-de/exercise-excuse-generator-python-cli/blob/master/preview.gif?raw=true)

## Objetivo

Queríamos un proyecto que usara muy poco Python, pero aún con una aplicación muy divertida, el generador de excusas o exuse generator toma 20 líneas de código, es fácil de entender y es el primer proyecto perfecto para cualquier desarrollador principiante.

## Instrucciones

Cree un script de Python que genere una excusa cada vez que se ejecute.

## Primero arma una estrategia con compañeros

¿Cómo podemos generar una excusa? ¿Cómo se construye una oración?

![Explicación del generador de excusas](https://github.com/breatheco-de/tutorial-project-excuse-generator-javascript/blob/master/explanation.gif?raw=true)

¡La idea es generar cada parte de la oración al azar para encontrar excelentes excusas!

<onlyfor saas="false" withBanner="false">
  
## 🌱  Cómo iniciar este proyecto


1. No clones este repositorio. El primer paso para comenzar a codificar es clonar el [python boilerplate](https://github.com/4GeeksAcademy/flask-rest-hello) en tu compjutador local o con Gitpod.

a) Si usas Gitpod (recomendada) puedes clonar el boilerplate [clic aquí](https://github.com/4GeeksAcademy/flask-rest-hello).

b) Si trabajas localmente, escribe el siguiente comando en tu terminal: 
```sh
git clone  git clone https://github.com/4GeeksAcademy/flask-rest-hello
```

2. Ejecuta la aplicación escribiendo en la terminal:

```bash
$ python3 app.py
```

💡 Importante: Recuerda actualizar el `remote` del proyecto con el de tu repositorio usando `git remote set-url origin <your new url>`, y luego guardar tu código en tu nuevo repositorio usando `add`, `commit` y `push`.

</onlyfor>

## Pista

1. Crea un archivo `app.py` con una excusa codificada en una variable.
2. La excusa debe estar en una variable:
```python
excuse = 'The dog eat my homework when I finished'
```
3. Usando python, crea una función que genere y devuelva una excusa aleatoria con la siguiente estructura:
```python
who = ['the dog','my granma','his turtle','my bird']
what = ['eat','pissed','crushed','broked']
when = ['before the class','right in time','when I finished','during my lunch','while I was praying']
```
4. Para crear una excusa consistente tienes que concatenar un ítem por cada array en el orden correcto.
5. Imprime la excusa en la consola usando la función `print`


## Tecnologías

Python.

## Fundamentos

Este ejercicio cubre los siguientes fundamentos:

1. Ejecutar archivos python
2. Cómo trabajar con listas (arrays).
3. Generar números aleatorios
4. Concatenar strings
5. Usar funciones (un poco).
