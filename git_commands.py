# Git:

#       
#     //Header -> Indicates which file commit version we are looking at

#     //git clone <repo>
#     //git fetch -> Descarga metadata github
#     //git pull origin main
#     //git push origin main
#     //git commit -am "mensaje"
#     //cd .. -> devolverse de carpeta
#     //git checkout -b {branch name} -> create new branch and move to it
#     //git checkout HEAD -- <archivo a reiniciar al último commit>
#     //git checkout HEAD~1 -> ir un commit atrás
#     //git add <archivo a agregar>
#     //git add . -> "add files in the current directory"
#     //git log -> historia de commits
#     //git log --oneline -> historia reducida de commits
#     //git log --oneline --graph -> historia con gráfico de commits
#     //git rm -cached <file> -> unstage and untrack a file

# Git commands for big projects:

    # git log --oneline: Te muestra el id commit y el título del commit.
    # git log --decorate: Te muestra donde se encuentra el head point en el log.
    # git log --stat: Explica el número de líneas que se cambiaron brevemente.
    # git log -p: Explica el número de líneas que se cambiaron y te muestra que se cambió en el contenido.
    # git shortlog: Indica que commits ha realizado un usuario, mostrando el usuario y el título de sus commits.
    # git log --graph --oneline --decorate y
    # git log --pretty=format:"%cn hizo un commit %h el dia %cd": Muestra mensajes personalizados de los commits.
    # git log -3: Limitamos el número de commits.
    # git log --after=“2018-1-2”
    # git log --after=“today” y
    # git log --after=“2018-1-2” --before=“today”: Commits para localizar por fechas.
    # git log --author=“Name Author”: Commits hechos por autor que cumplan exactamente con el nombre.
    # git log --grep=“INVIE”: Busca los commits que cumplan tal cual está escrito entre las comillas.
    # git log --grep=“INVIE” –i: Busca los commits que cumplan sin importar mayúsculas o minúsculas.
    # git log – index.html: Busca los commits en un archivo en específico.
    # git log -S “Por contenido”: Buscar los commits con el contenido dentro del archivo.
    # git log > log.txt: guardar los logs en un archivo txt
    
