# py-activerecord

## requirements
- Python 3.x
- mysql.connector

## functions
### class functions
- create()
- remove()
- query()

### instance functions
- save()
- delete()

## tutorial
1 create model class
```
import model
from column import Column as Column


class SampleModel(model.Model):

    title = Column(type="varchar")
    context = Column(type="text")
    number = Column(type="int")
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
value of "database" must be snake-case of the model class name.
