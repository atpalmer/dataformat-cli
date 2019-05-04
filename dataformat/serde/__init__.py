import json
import toml
from . import yaml


CHOICES = ('json', 'yaml', 'toml')


def get(deserializer_name, serializer_name):
    de = globals().get(deserializer_name).load
    ser = globals().get(serializer_name).dump
    return de, ser
