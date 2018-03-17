# -*- coding:utf-8 -*-
from schematics.models import Model
from schematics.types import StringType, EmailType, BooleanType, IntType, ListType, ModelType, DateTimeType
from datetime import datetime

class Unprocessed(Model) :
    _name = 'unprocessed'
    id = IntType(required=False)
    city,country = StringType(required=True)
    c_min = IntType(required=False)
    c_max = IntType(required=False)
    c_current = IntType(required=False)
    status = IntType(required=False)
    wind = IntType(required=False)
    site = StringType(required=True)
    time = DateTimeType(required=True, default=datetime.now())
    user = StringType(required=False)
class Processed(Model) :
    _name = 'processed'
    id = IntType(required=False)
    city,country = StringType(required=True)
    c_min = IntType(required=False)
    c_max = IntType(required=False)
    c_current = IntType(required=False)
    status = IntType(required=False)
    wind = IntType(required=False)
    time = DateTimeType(required=True, default=datetime.now())
    user = StringType(required=False)

class User(Model) :
    _name='user'
    id=IntType(required=False)
    user_tag=StringType(required=False)
    locations=IntType(required=False)
if __name__ == '__main__':
    pass
