# -*- coding: utf-8 -*-
import MySQLdb as mysql



# CONFIG
DBUSER="hercules"
DBPWD="Poseidon01"
DBNAME="ZEUS"
DBHOST="zeus.cdtvxdjfmpg3.us-east-1.rds.amazonaws.com"
ARQUIVO="NEXTEL_SVA_ALES_ATIVAR_20180227_000000.TXT"

def conn(query):
    cnx = mysql.connect(user=DBUSER, passwd=DBPWD, host=DBHOST, db=DBNAME)
    result = cnx.cursor()
    result.execute(query)
    x = result.rowcount
    print("Fora %s" % x)
    while x != 0:
        print("Entrando %s" % x)
        result = result.fetchmany(2)
        print(result)
        x = x - 1
    #result = cnx.
        cnx.close()
    return (result)


conn(query="SELECT * FROM diego;")
