#!/bin/bash
# 98f98f8db5c2e4320db42d8653be979b6d57b797

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
