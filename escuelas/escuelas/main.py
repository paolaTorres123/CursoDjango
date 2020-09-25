import pandas as pd
import sqlite3

#Leer archivo sql
def leerScript(nombre):
    with open(nombre, 'r') as sql_file:
        script = sql_file.read()
        cursor.execute(script)
    return script

con = sqlite3.connect('Escuela.db')
cursor = con.cursor()

cursor.executescript(leerScript('Escuela.sql'))

url = 'Escuelas.csv'
registro = pd.read_csv(url)


cabecera = [
 'PERIODO', 'TIPO EDUCATIVO', 'NIVEL EDUCATIVO', 'SERVICIO EDUCATIVO', 
 'CLAVE ENTIDAD','ENTIDAD','CLAVE MUN./DEL.', 'MUNICIPIO', 'CLAVE LOCALIDAD',
 'LOCALIDAD', 'CLAVE', 'TURNO', 'AMBITO', 'CENTRO EDUCATIVO', 'CONTROL', 
 'DOMICILIO', 'NUM. EXTERIOR', 'ENTRE CALLE', 'Y CALLE', 'CALLE POSTERIOR',
 'CP', 'LADA', 'TELEFONO', 'CORREO', 'TOTAL DE PERSONAL', 'PERSONAL MUJERES', 
 'PERSONAL HOMBRES', 'TOTAL DE DOCENTES','DOCENTES MUJERES', 'DOCENTES HOMBRES',
 'TOTAL DE ALUMNOS', 'ALUMNOS MUJERES', 'ALUMNOS HOMBRES', 'GRUPOS',
 'AULAS EXISTENTES', 'AULAS EN USO', 'LABORATORIOS', 'TALLERES', 'COMP_OPERA', 
 'COMP_OPERA_INTER', 'COMP_OPERA_EDU','ALTITUD (msnm)', 'LONGITUD', 'LATITUD', 
 'LONGITUD (gms)', 'LATITUD (gms)']


registro.columns = cabecera

conexion.commit()
conexion.close()