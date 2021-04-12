from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd


strUrlConsumo="https://stats.oecd.org/Index.aspx?DataSetCode=HEALTH_MORTALITY"
import time
time.sleep(1)

session = HTMLSession()


obfrmBusqueda =  session.get(strUrlConsumo).text  
strfrmBusqueda = str(obfrmBusqueda)
soup = BeautifulSoup(obfrmBusqueda, 'html.parser')

print('Buscando tabla')

oTabla = soup.find("table", attrs={'class':'DataTable'}) #.find("tbody").find_all("tr")

sListEncabezados =""
oTHeader = oTabla.find("thead")
oHeadRows = oTHeader.find_all("tr")
oTcells = oHeadRows[4].find_all("th")
sEncabezados = "vacio"
sArrData =[]
sArrData.append([])
#insert_index=0
import numpy as np
for cell in oTcells:
    #if insert_index >0:	
        #if sEncabezados =="vacio":
        #    sEncabezados =  "'" + cell.get_text() +	"'"
        #else:
        #    sEncabezados = sEncabezados + ",'" +cell.get_text() + "'"   	
    sValorActual=''	
    sValorActual = cell.get_text()
    sValorActual = sValorActual.replace(u'\xa0', '')
    sArrData[0].append(sValorActual)
    #print(cell.get_text())
    #lstEncabezados.append([cell.get_text()]) 			
    #insert_index = insert_index + 1		
    
    		

#print(sEncabezados)
oTBody = oTabla.find("tbody")
oRows = oTBody.find_all("tr")
iApuntadorFila=1
for row in oRows:
    Colcells = row.find_all("td")
    sValoresColumnas =""   
    iContador=0    
    sArrData.append([])	
    for col in Colcells:
        if iContador==0 or iContador>=2: 
            sValorActual=''	
            sValorActual = col.get_text()
            sValorActual = sValorActual.replace(u'\xa0', '')
            sValorActual = sValorActual.replace('..', '0')
            sArrData[iApuntadorFila].append(sValorActual)

        iContador = iContador+1			
    iApuntadorFila=iApuntadorFila+1

print('Total filas: ' + str(len(sArrData)))
print(sArrData)




