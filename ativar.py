# -*- coding: utf-8 -*-
import MySQLdb as mysql




def dados():
    global line
    with open(file) as f:
        next(f)
        x = 0
        for line in f:
            line = f.readline().replace(';', '","').replace('3G', '"')
            #print('contador {} linha {}'.format(x, line))
            #print('Inicio')
            #print('insert into "%s" ' %line)
            #print('Fim')
            conn(line)
            x += 1
    return line

def conn(line):
    cnx = mysql.connect(user=DBUSER, passwd=DBPWD, host=DBHOST, db=DBNAME)
    cursor = cnx.cursor()
    query = 'insert into diego (msisdn, cpf, nome, codigoplano, categoria, dataativacao, tipopacotesva) values ("{});'.format(line)
    #print('"%s' %line)
    #cursor.execute(query)
    #cnx.send_query(query)
    print('Ok')
    cnx.commit()
    cursor.close()
    cnx.close()


dados()