from pymongo import MongoClient

client = 'mongodb+srv://thecgman60:iamragnarok04123@cluster0.yy14chf.mongodb.net/'

connection_string = MongoClient(client)

database_name = connection_string['Onepiece']

collection_name = database_name['Server_info' ]

reserved_collection_name = database_name['Reserved_data']

profile_data = database_name['Users_info']
