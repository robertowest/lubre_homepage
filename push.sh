#!/bin/bash

git add .
git add -f requirements.txt

# quitamos archivos que no queremos modificar
# git reset config/desarrollo.py

git commit -m "modificaciones en casa"
git push -u origin master

# para descartar todos los cambios locales
# git reset --hard HEAD

# para descartar un archivo
# git reset HEAD app/PRUEBA/urls.py

# eliminamos carpeta del repositorio
# git rm -r .idea/
# git commit -m "borrar carpeta idea"
# git push

# Limpiando archivos ignorados
# git clean -Xn      - Vista previa de todos los archivos que serán limpiados
# git clean -Xf      - Se eliminarán todos los archivos ignorados del directorio actual y todos los subdirectorios
