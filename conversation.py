# -*- coding: utf-8 -*-
import json
from watson_developer_cloud import ConversationV1

import credentials


def setup():
    """Sets up the conversation component
    by using its credentials.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    pass


def hello():
    """Returns the very first hello from Conversation.

    Parameters
    ----------
    None

    Returns
    -------
    TBD
    """
    pass


def exchange(input_text):
    """Sends an input text to Conversation and returns its answer.

    Parameters
    ----------
    input_text: {str}

    Returns
    -------
    TBD
    """
    pass


if __name__ == '__main__':
    print("*** Setting up Conversation")
    setup()

    print("*** hello()")
    print(hello())

    # let's do an infinite loop
    while True:
        # gets some input from the prompt
        input_content = input('Conversation> ')

        # if you type one of those words, it will exit the while loop
        if (input_content.lower() in {'exit', 'quit', 'q', 'n'}):
            break

        print(exchange(input_content))
