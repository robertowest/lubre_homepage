#!/bin/bash
# 0b1bd623c1bf75cc618ddd120ea1e96b9a0f65da
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
