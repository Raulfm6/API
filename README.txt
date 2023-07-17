Instrucciones para ejecutar el archivo:

1- Crear el entorno virtual dentro de la carpeta API:
	- python -m venv .env

1- Activar el entorno de python en local:
	-Windows: .\.env\Scripts\activate
	-Linux: source .env/bin/activate

2- Instalar paquetes:
	Ejecutar: pip install -r requirements.txt

3- Ejecutar el programa:
	- Si se usa algún IDE como VSCode presionar el botón de ejecutar
	- Si no, abrir un terminal en la carpeta API y ejecutar python app.py

Si por algún motivo da error al ejecutar debido a SQLAlchemy será necesario salir del entorno virtual con CTRL+C e installar los requirements de nuevo con 
pip install -r requirements.txt

4- Importar la colección postman (en este caso se ha decidido usar postman):

5- Lanzar las peticiones

Testing:

1- Instalar paquetes:
	Ejecutar: pip install -r requirements.txt (Se han añadido nuevos archivos necesarios)

2- Ejecutar testing:
	- Si se usa algún IDE como VSCode presionar el botón de ejecutar
	- Si no, abrir un terminal en la carpeta API y ejecutar python app.py

Dentro de la carpeta DB se encuentra la base de datos.
En la carpeta swagger se encuentra el swagger.json con la información de la API.
