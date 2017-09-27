#!/bin/bash
#4. piemers
echo "tiek pildīts skripts:" $0
echo $0
echo $n
echo "Skriptam nodoto argumentu skaits:"$#
echo "Skriptam nodoti argumenti (attēlošana/grupēšana 1):"$*
echo "Skriptam nodoti argumenti (attēlošana/grupēšana 2):"$@
#echo $?
echo "Skriptam piešķirtais procesa numurs"$$
echo $!

#3. piemērs
#NAME="Vaards Uzvaards"
#echo $NAME
#unset NAME
#echo $NAME

#2. piemērs
#NAME="Vaards Uzvaards"
#readonly NAME
#echo $NAME
#NAME="Uzvaards Vaards"
#echo $NAME

#1. piemērs
#NAME="Vaards Uzvaards"
#echo $NAME
