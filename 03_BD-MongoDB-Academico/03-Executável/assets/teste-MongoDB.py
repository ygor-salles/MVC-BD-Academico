from pymongo import MongoClient
from pprint import pprint
import datetime
import json

if __name__ == '__main__':
    # CONEXÃO COM O MONGO DB
    client = MongoClient('localhost', 27017)
    db = client.trabalho
    col = db.api

    # CONSULTA AO DOCUMENTO DE PK = 239
    pedidos = col.find({'_id': 239})
    for document in pedidos:
        pprint(document)

    # INSERÇÃO DE UM DOCUMENTO ALTERADO NO BANCO
    novoDoc = {
        'CustId': 11111.0,
        '_id': 22222,
        'invoiceDate': datetime.datetime(2016, 11, 24, 23, 25, 55, 81000),
        'lineItems': [
            {'Cost': 1192.0, 'prodCount': 2.0, 'prodId': 5594.0},
            {'Cost': 574.0, 'prodCount': 1.0, 'prodId': 4770.0},
            {'Cost': 192.0, 'prodCount': 8.0, 'prodId': 4103.0}
        ],
        'orderStatus': 'C',
        'statusDate': datetime.datetime(2016, 11, 25, 5, 42, 15, 667000) 
    }
    del novoDoc['orderStatus']
    doc_inserido = col.insert_one(novoDoc).inserted_id

    # CONSULTA AO DOCUMENTO DE PK = 22222
    pedidos = col.find({'_id': 22222})
    for document in pedidos:
        pprint(document)
