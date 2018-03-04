# -*- coding: utf-8 -*-
from numpy import loadtxt, genfromtxt

from _mysql import connect, connection, Error



# CONFIG
DBUSER="hercules"
DBPWD="Poseidon01"
DBNAME="ZEUS"
DBHOST="zeus.cdtvxdjfmpg3.us-east-1.rds.amazonaws.com"
ARQUIVO="NEXTEL_SVA_ALES_ATIVAR_20180227_000000.TXT"

def insert_assinantes(assinantes):
    #query = 'INSERT INTO diego(msisdn, cpf, nome, codigoplano, categoria, dataativacao, tipopacotesva) ' \
    #        'VALUES(%s,%s,%s,%s,%s,%s,%s)'
    query = 'SELECT * FROM diego;'


    try:
        conn = connect(user=DBUSER, password=DBPWD, host=DBHOST, database=DBNAME)

        cursor = conn.cursor()
        cursor.executemany(query)

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()


def main(ARQUIVO):
    with open(ARQUIVO) as f:
        #content = f.read()
        content = ARQUIVO
        next(f)
        for content in f:
            content = f.read()
            print(content)
    #    #print("Open %s" % content)
    #    assinantes = content
        #assinantes = content.insert(0, "(")
            #assinantes+=str("(%s)" % content)
    #print(assinantes)
            #assinantes = [('5511947222332', '35209905802', 'ALINE FERREIRA DA SILVA', '2211', 'POS', '27/02/2018', 'Pacote serviÃ§os promocional 5 3G\n')]
    insert_assinantes(content)


if __name__ == '__main__':
    main(ARQUIVO)