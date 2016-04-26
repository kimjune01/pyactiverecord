# pyactiverecord
pyactiverecord is python active-record like mysql wrapper.

## features
- active-record like mysql wrapper
- ORM

## requirements
- Python 3.x
- mysql
- mysql-connector-python

## Usage
create model class
```
import pyactiverecord.model as model
from pyactiverecord.database import Database as Database


class SampleModel(model.Model):

    number = Column(type="int")
    title = Column(type="varchar")
    text = Column(type="text")
    date = Column(type="timestamp")
    
```
connect to database
```
Database.connect(
    host="localhost",
    database="database_name",
    user="root",
    password=""
)
```

## method
### class method
- query
```
data = SampleModel.query()
print(len(data))
for d in data:
    print(d.title)

# where
data = SampleModel.query(where=["title='py-activerecord'", "text like '%Python%'"])

# order
data = SampleModel.query(order=["id asc", "title desc"])
```
### instance method
- save
```
model = SampleModel()
model.number = 1
model.title = "py-activerecord"
model.text = "ActiveRecord for Python Library"
model.date = "2016-01-01 00:00:00"

model.save()
```
- delete
```
obj = SampleModel.query(where=["title='py-activerecord'"], order=["id asc"]).first()
obj.delete()
```
