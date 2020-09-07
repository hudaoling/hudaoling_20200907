
from pymongo import MongoClient

class MongoAPI(object):
    def __init__(self, db_ip, db_port, db_name, table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.conn = MongoClient(host=self.db_ip, port=self.db_port)
        self.db = self.conn[self.db_name]
        self.table = self.db[self.table_name]
    def find_one(self, query=None):
        return self.table.find_one(query, projection={"_id": False})
    def find(self, query=None,**kwargs):
        return self.table.find(query)
    def insert(self, kv_dict):
        return self.table.insert(kv_dict)

    def insert_check(self, kv_dict,key):
        if self.table.find_one({key:kv_dict[key]}) !=None:
            print('{} already exists ,go here pass'.format(kv_dict[key]))
        else:
            return self.table.insert(kv_dict)
            print('go here insert')

    def delete(self, query=None):
        return self.table.deleteMany(query)

    def check_exist(self, query=None):
        ret = self.table.find_one(query)
        return ret != None

    # 更新内容，如果没有会新建
    def update(self, query, kv_dict):
            self.table.update_one(query,{
              '$set': kv_dict
            }, upsert=True)


# webchat_spider = MongoAPI("localhost",  27017,  "webchat_spider", "webchat_t1")