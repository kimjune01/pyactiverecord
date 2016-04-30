# pyactiverecord
pyactiverecord is python active-record like mysql wrapper.

## Features

- active-record like mysql wrapper
- ORM

## Requirements

- Python 3.x
- mysql
- mysql-connector-python

## Install

```
pip install pyactiverecord
```

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
at this time, if the lower-case of this model class name of the tabale is't exist, it is automatically created.


pyactiverecord needs to connecte to the database, so first of all, program is required to call Databese.setup method.
```
import model

def execute():
    s = SampleModel()
    s.title = "test"
    s.save()
    
    s = SampleModel.query().first()
    print(s.title)


if __name__ == '__main__':
    
    model.Database.setup(
        host="localhost",
        database="stardust",
        user="root",
        password=""
    )
    
    execute()
```

## Methods
### class methods
query
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
save
```
s = SampleModel()
s.number = 1
s.title = "py-activerecord"
s.text = "ActiveRecord for Python Library"
s.date = "2016-01-01 00:00:00"

s.save()
```
delete
```
s = SampleModel.query(where=["title='py-activerecord'"], order=["id asc"]).first()
s.delete()
```

### License
This software is released under the MIT License, see [LICENSE.md](./LICENSE.md)
