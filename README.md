# MadLab
Este repositorio incluye todo el codigo fuente para el proyecto final del curso de desarrollo de software II
# Integrantes:

Luis David Restrepo Hoyos - 1427086 - Scrum Master

Juan David Gómez Orozco - 1631689 - Developer

Walter Alberto Santacruz Gallo - 1630645 - Developer

Miguel Angel Gutierrez Prieto - 1626057 - Developer

# Instrucciones

Una vez creado el ambiente virtual de python, se procede a instalar las librerias necesarias.

Ejecutar el siguiente comando para instalar los dependecias del proyecto ubicados en el archivo **requirements.txt**

        pip install -r requirements.txt
        
En caso de agregar una libreria o modificar la version de una libreria existente guardar los cambios en el archivo **requirements.txt** asi:

        pip freeze > requirements.txt

Debido a que las carpetas **migrations** de las apps del proyecto se ignoran en el seguimiento que realiza git, es 
necesario crear para cada app una carpeta denominada **migrations** y dentro de esta un archivo denominado **__ init __.py**
- **Nota:** Esto se debe realizar cada vez que se clona el proyecto o que, por alguna razón no esten estas carpetas en las
apps del proyecto django.

Ejecutar los siguientes comandos para efectuar los cambios realizados en los modelos a la base de datos
        
        python manage.py makemigrations
        python manage.py migrate
 
Por último, para ejecutar el servidor de pruebas del proyecto ejecutar el siguiente comando:

        python manage.py runserver
        
