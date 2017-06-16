import pytest
import conversation


def test_hello():
    conversation.setup()

    # TBD
    expected_output = None

    output = conversation.hello()

    assert output == expected_output, "output and expected_output don't match"
    #assert type(output) == dict, "type of output should be dict"
    #assert type(output) == list, "type of output should be list"
    #assert type(output) == str, "type of output should be str"
    #assert "mykey" in output, "output should have a key 'mykey'"


def test_exchange():
    conversation.setup()
    conversation.hello()

    # TBD
    func_input = None

    # TBD
    expected_output = None

    output = conversation.exchange(func_input)

    assert output == expected_output, "output and expected_output don't match"
    #assert type(output) == dict, "type of output should be dict"
    #assert type(output) == list, "type of output should be list"
    #assert type(output) == str, "type of output should be str"
    #assert "mykey" in output, "output should have a key 'mykey'"
