# py-activerecord
py-activerecord is python activerecord library.

## features
- activerecord like mysql wrapper
- ORM

## requirements
- Python 3.x
- mysql.connector

## functions
### class functions
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
### instance functions
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

## tutorial
1 create model class
```
import model
from column import Column as Column


class SampleModel(model.Model):

    number = Column(type="int")
    title = Column(type="varchar")
    text = Column(type="text")
    date = Column(type="timestamp")
```

2 add setting.json file
ex.
```
{
  "host": "localhost",
  "database": "sample_model",
  "user": "root",
  "password": ""
}
```
value of "database" must be lower-case of the model class name.
