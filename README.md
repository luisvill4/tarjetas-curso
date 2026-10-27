# Tarjetas del curso

Proyecto colaborativo de 4° Medio Programación. Cada estudiante agrega **su propia tarjeta de presentación** en la carpeta `estudiantes/` y la sube con un commit.

## Cómo participar

1. Copia `plantilla.py` dentro de `estudiantes/` con el nombre `apellido_nombre.py` (minúsculas, sin tildes ni espacios).
2. Abre tu archivo y completa tus datos y la función `presentarme()`.
3. Prueba tu tarjeta: `python main.py` (debe aparecer tu mensaje).
4. Sube tu cambio:

   ```
   git add estudiantes/tuapellido_tunombre.py
   git commit -m "Agrega tarjeta de Nombre Apellido"
   git pull --rebase
   git push
   ```

   `git pull --rebase` trae las tarjetas que tus compañeros subieron antes que tú. Sin ese paso, `git push` te rechaza ya que hay cambios que tu no tienes en tu equipo.

## Cómo ejecutar el proyecto

```
python main.py
```

`main.py` encuentra todos los archivos de `estudiantes/` y muestra la tarjeta de cada compañero.
