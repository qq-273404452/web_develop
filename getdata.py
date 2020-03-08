from pymongo import MongoClient


db=MongoClient()
col=db['testdb']['users']
time=[]
TS1 = []
def getdate():
    for x in col.find({},{'_id':0,'time':1,'value':1}):
        time.append(x['time'])
        TS1.append(x['value'])

if __name__ == '__main__'():
    getdate()
