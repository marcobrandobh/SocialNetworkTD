#!/bin/bash

echo "$(tput setaf 1)##########################################################################
#                                                                        #
# Script para solicitação de takedown de páginas falsas em redes sociais #
#                                                                        #
#     Para denunciar páginas do Facebook ou Instagram                    #
#         digite a url da página falsa e depois tecle enter              #
#                                                                        #
#     Para denunciar páginas do Twitter                                  #
#  digite @ e o usuário que deseja denunciar e depois tecle enter        #
##########################################################################"

# Verify if URL has been passed as argument and translate it to lowercase
if [ -z $1 ]
then
    echo -e "$(tput setaf 2)\n                   Digite a URL a ser denunciada: \n $(tput setaf 7)"
    read url
    url=$(echo "$url" | tr '[:upper:]' '[:lower:]')
else
    url=$(echo "$1" | tr '[:upper:]' '[:lower:]')
fi

# Switch Case to select wich TakeDown will run
case $url in

    *facebook* )
	echo -e "TakeDown do FACEBOOK:\n" $url "\nExecutando...\n"
	`python Facebook.py $url`
	echo -e "\nFormulário preenchido"
;;
    *instagram* )
        echo -e "TakeDown do INSTAGRAM:\n" $url "\nExecutando...\n"
	`python Instagram.py $url`
        echo -e "\nFormulário preenchido"
;;
    *@* )
    echo -e "TakeDown do Twitter:\n" $url "\nExecutando...\n"
    url2=`echo $url | cut -d@ -f2`
    `python Twitter.py $url2`
    echo -e "\nFormulário preenchido"
esac
