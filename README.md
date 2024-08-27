# Aplicación Web de Diario Personal

Esta es una aplicación web simple para llevar un diario personal, desarrollada con Flask.

## Características

- Crear entradas de diario
- Ver lista de entradas
- Ver entradas individuales
- Agregar eventos a las entradas (por ejemplo, ejercicio, sueño, etc.)

## Requisitos

- Python 3.7+
- Flask
- Flask-SQLAlchemy

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/diario-personal.git
   cd diario-personal
   ```

2. Crea un entorno virtual y actívalo:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Inicializa la base de datos:
   ```
   flask db upgrade
   ```

5. Ejecuta la aplicación:
   ```
   flask run
   ```

6. Abre un navegador y ve a `http://localhost:5000`

## Uso

- Para crear una nueva entrada, haz clic en "Nueva Entrada" en la barra de navegación.
- Para ver una entrada existente, haz clic en ella en la página principal.
- Para agregar un evento a una entrada, ve a la página de la entrada y usa el formulario en la parte inferior.

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios importantes antes de crear un pull request.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)