import pytest
import yaml
import os
import json


# @pytest.fixture
# def config(config_path="params.yaml"):
#     with open(config_path) as yaml_file:
#         config = yaml.safe_load(yaml_file)
#     return config

# @pytest.fixture
# def schema_in(schema_path="schema_in.json"):
#     with open(schema_path) as json_file:
#         schema = json.load(json_file)
#     return schema

class NotinRange(Exception):
    def __init__(self,message="value not in range"):
        #self.input_ = input_
        self.message = message
        super().__init__(self.message)

def test_generic():
    a=5

    with pytest.raises(NotinRange):
        if a not in range(10,20):
            raise NotinRange

