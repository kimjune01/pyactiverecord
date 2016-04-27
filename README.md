# pyactiverecord
pyactiverecord is python active-record like mysql wrapper.

## Features
- active-record like mysql wrapper
- ORM

## Requirements
- Python 3.x
- mysql
- mysql-connector-python

## Usage
create model class
```
import model


class SampleModel(model.Model):

    number = model.Column(type="int")
    title = model.Column(type="varchar")
    text = model.Column(type="text")
    date = model.Column(type="timestamp")
    
```
connect to database
```
import model

model.Database.setup(
    host="localhost",
    database="database_name",
    user="root",
    password=""
)
```

## Methods
### class methods
- query
```
data = SampleModel.query()
for d in data:
    print(d.title)

# where
data = SampleModel.query(where=["title='py-activerecord'", "text like '%Python%'"])

# order
data = SampleModel.query(order=["id asc", "title desc"])
```
### instance methods
- save
```
s = SampleModel()
s.number = 1
s.title = "py-activerecord"
s.text = "ActiveRecord for Python Library"
s.date = "2016-01-01 00:00:00"

s.save()
```
- delete
```
s = SampleModel.query(where=["title='py-activerecord'"], order=["id asc"]).first()
s.delete()
```

### License
This software is released under the MIT License, see [LICENSE.md](./LICENSE.md)
