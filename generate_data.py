
import sys, inspect

from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import mysql
import flask_and_restless.models as models

def print_schema():
    '''
    generates a schema from the models and writes the
    sql to file
    :return:
    '''

    table_sql = ''

    out_file = open('./mock_data_schema.sql', 'w+')
    for model in get_model_classes():
        table_sql = CreateTable(model.__table__).compile(dialect=mysql.dialect())
        out_file.write(str(table_sql) + ';')
        print(table_sql)
    out_file.close()

def get_model_classes():

    # flag to filter out classes not defined in models.py
    is_class_member = lambda member: inspect.isclass(member) \
                                     and member.__module__ == models.__name__

    cls_members = inspect.getmembers(models, is_class_member)
    # fetch only BaseModel subclasses
    base_model_cls = models.BaseModel
    model_members = filter(lambda m: issubclass(m[1], base_model_cls) and m[1] is not base_model_cls, cls_members)
    model_classes = [m[1] for m in model_members]

    print 'model classes: ', model_classes
    return model_classes

if __name__ == '__main__':
    print 'running data generator'

    print_schema()
