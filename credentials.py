import json
import os

# BEGIN of python-dotenv section
from os.path import join, dirname
from dotenv import load_dotenv
import os, sys
# END of python-dotenv section


def read_credentials_when_deployed():
    """Parse credentials from the VCAP_SERVICES environment variable
    and from other user defined environment variables
    and outputs them in a unique dictionary.

    Parameters
    ----------
    None

    Returns
    -------
    {dict}: a dictionary containing all the necessary credentials
    """
    print('Reading credentials from VCAP_SERVICES environment variable')
    vcap = json.loads(os.environ.get('VCAP_SERVICES'))

    credentials = {}
    
    
    credentials['CONVERSATION_USERNAME'] = vcap['conversation'][0]['credentials']['username']
    credentials['CONVERSATION_PASSWORD'] = vcap['conversation'][0]['credentials']['password']
    credentials['TRANSLATOR_USERNAME'] = vcap['language_translator'][0]['credentials']['username']
    credentials['TRANSLATOR_PASSWORD'] = vcap['language_translator'][0]['credentials']['password']
    credentials['CONVERSATION_WORKSPACE_ID'] = os.environ["CONVERSATION_WORKSPACE_ID"]

    return(credentials)



def read_credentials_when_local():
    """Parse credentials from the .env file
    and outputs them in a unique dictionary.

    Parameters
    ----------
    None

    Returns
    -------
    {dict}: a dictionary containing all the necessary credentials
    """
    print('Reading credentials from .env file (only for local)')

    # BEGIN of python-dotenv section
    load_dotenv('.env')
    # END of python-dotenv section

    credentials = {}
    key_list = [
        "CONVERSATION_USERNAME",
        "CONVERSATION_PASSWORD",
        "CONVERSATION_WORKSPACE_ID",
        "TRANSLATOR_USERNAME",
        "TRANSLATOR_PASSWORD"
    ]

    for key in key_list:
        credentials[key] = os.environ.get(key)

    return(credentials)


def read_credentials():
    """Wrapper for functions read_credentials_when_local()
    and read_credentials_when_deployed()
    detects which one to use, and returns its value.

    Parameters
    ----------
    None

    Returns
    -------
    {dict}: a dictionary containing all the necessary credentials
    """
    ## IF DEPLOYED : READING CREDENTIALS FROM VCAP_SERVICES
    ## warning: set connections in bluemix before
    if 'VCAP_SERVICES' in os.environ:
        return(read_credentials_when_deployed())

    ## IF LOCAL : READING CREDENTIALS FROM .ENV
    elif os.path.isfile(".env"):
        return(read_credentials_when_local())

    ## IF PROBLEM ^^;
    elif (not os.path.isfile(".env")):
        print("ERROR: found neither a VCAP_SERVICES env variable or a .env file.\n")


if __name__ == '__main__':
    credentials = read_credentials()

    #print(credentials)
    for key in credentials:
        print("found key '{}' with value '{}'".format(key, credentials.get(key)))
