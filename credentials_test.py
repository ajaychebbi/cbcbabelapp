import pytest
import json
import credentials
import os

def test_read_credentials_when_deployed():
    with open('pytest_data/vcap_services.json') as ifile:
        json_string = ifile.read()

    os.environ['VCAP_SERVICES'] = json_string
    os.environ['CONVERSATION_WORKSPACE_ID'] = "fake workspace id"

    expected_output = {
        'CONVERSATION_USERNAME': 'fake username for conversation',
        'CONVERSATION_PASSWORD': 'fake password for conversation',
        'CONVERSATION_WORKSPACE_ID': "fake workspace id",
        'TRANSLATOR_USERNAME': 'fake username for language_translator',
        'TRANSLATOR_PASSWORD': 'fake password for language_translator'
    }
    output = credentials.read_credentials_when_deployed()
    assert output == expected_output

    output = credentials.read_credentials()
    assert output == expected_output
