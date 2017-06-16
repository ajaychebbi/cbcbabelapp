# -*- coding: utf-8 -*-
import json
from watson_developer_cloud import LanguageTranslatorV2

import credentials


def setup():
    """Sets up the language translator component
    by using its credentials.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    pass


def identify(input_str):
    """Identifies the language of a text.

    Parameters
    ----------
    input_str : {str}

    Returns
    -------
    TBD
    """
    pass


def translate(input_str, lang_source, lang_target):
    """Translates a string from one language to another.

    Parameters
    ----------
    input_str : {str}
    lang_source : {str}
    lang_target : {str}

    Returns
    -------
    TBD
    """
    pass


if __name__ == '__main__':
    print("*** Setting up LanguageTranslator")
    setup()

    print("*** Identifying the lang of your input...")
    # gets some input from the prompt
    input_content = input('Identify> ')
    print(json.dumps(identify(input_content), indent=2))

    print("*** Translating 'Bonjour' from fr to en")
    input_content = "Bonjour!"
    lang_in = 'fr'
    lang_out = 'en'
    print(json.dumps(translate(input_content, lang_in, lang_out), indent=2))
