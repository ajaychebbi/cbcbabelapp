# -*- coding: utf-8 -*-
import json

import credentials
import conversation
import language


def setup():
    """Sets up ALL the necessary components.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    pass


def home():
    """Resets the conversation and returns the greeting message from Conversation
    *in the language of the user* (default: english)

    Parameters
    ----------
    None

    Returns
    -------
    TBD
    """
    return {'labels': [], 'answer': ['Hello World from control']}


def interact(input_text):
    """Sends a message to conversation and returns the answer.
    *Identifies* the language of the user to returns the answer *in the user language*.
    If that language is different from previous exchanges,
    interact() will *restart the conversation* (hello again, in the user language)
    and switch to that new language.
    Note: first language assumed is english.

    Parameters
    ----------
    input_text: {}

    Returns
    -------
    TBD
    """
    result = {  'labels': ['#fakeintent', '@fakeentity', 'faketag'],
                'answer': ["Control has no idea what you're saying cause I'm dumb.",
                         "But I'm going to say something anyway ^^;"],
                'action': {'fake_action': 'what am I doing?'}
            }
    return result


if __name__ == '__main__':
    print("*** Setting up components...")
    setup()

    print("*** First reponse...")
    print(home())

    # let's do an infinite loop
    while True:
        # gets some input from the prompt
        input_content = input('Control> ')

        # if you type one of those words, it will exit the while loop
        if (input_content.lower() in {'exit', 'quit', 'q', 'n'}):
            break

        print("*** Interact with system...")
        print(interact(input_content))
