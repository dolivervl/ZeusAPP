# -*- coding: utf-8 -*-

import mysql.connector
import fileinput

# CONFIG
DBUSER="hercules"
DBPWD="Poseidon01"
DBNAME="ZEUS"
DBHOST="zeus.cdtvxdjfmpg3.us-east-1.rds.amazonaws.com"
ARQUIVO="NEXTEL_SVA_ALES_ATIVAR_20180227_000000.TXT"

def grava_banco(QUERY):
    cnx = mysql.connector.connect(user=DBUSER, password=DBPWD, host=DBHOST, database=DBNAME)
    #QUERY = "SELECT * FROM diego limit 0,10"
    #result = cnx.cmd_query(QUERY)
    result = cnx.cursor()
    result.executemany(QUERY)
    #for row in result.fetchall():
        #print(row[0]," ", row[1])
        #print(row)
    cnx.commit()
    cnx.close()
    return(result)

#QUERY = "SELECT * FROM assinantes limit 0,10"

#conn()

def prepara_arquivo(ARQUIVO):
    with open(ARQUIVO) as f:
        #content = f.read()
        next(f)
        for content in f:
            content = f.readline()
            #print("oi")
            content = content.split(";")
            QUERY = 'insert into diego (msisdn, cpf, nome, codigoplano, categoria, dataativacao, tipopacotesva) values (%s);' % content
            print(QUERY)
    return(grava_banco(QUERY))
    #return(QUERY)
prepara_arquivo(ARQUIVO)

#QUERY = 'insert into diego (msisdn, cpf, nome, codigoplano, categoria, dataativacao, tipopacotesva) values (1111,11111,11111,111111,1111,1111,111);'
#grava_banco(QUERY)

#with open(arquivo) as f:
#    content = f.read()
#    print(content)

#QUERY = ("SELECT * FROM diego limit 0,10")
#conn(QUERY)
