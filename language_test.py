import pytest
import language


def test_identify():
    language.setup()

    func_input_en = "Good morning, nice to meet you."
    # TBD
    expected_output = None
    output = language.identify(func_input_en)
    assert output == expected_output, "output and expected_output don't match"
    #assert type(output) == dict, "type of output should be dict"
    #assert type(output) == list, "type of output should be list"
    #assert type(output) == str, "type of output should be str"
    #assert "mykey" in output, "output should have a key 'mykey'"

    func_input_fr = "Bonjour, ravi de vous rencontrer."
    expected_output = {'confidence': 0.99873, 'language': 'fr'}
    output = language.identify(func_input_fr)
    assert output == expected_output, "output and expected_output don't match"
    #assert type(output) == dict, "type of output should be dict"
    #assert type(output) == list, "type of output should be list"
    #assert type(output) == str, "type of output should be str"
    #assert "mykey" in output, "output should have a key 'mykey'"

    func_input_de = "Guten tag. Erfreut, Sie kennen zu lernen."
    expected_output = {'confidence': 0.999997, 'language': 'de'}
    output = language.identify(func_input_de)
    assert output == expected_output, "output and expected_output don't match"
    #assert type(output) == dict, "type of output should be dict"
    #assert type(output) == list, "type of output should be list"
    #assert type(output) == str, "type of output should be str"
    #assert "mykey" in output, "output should have a key 'mykey'"



def test_translate():
    language.setup()

    # TBD
    func_input = None

    # TBD
    expected_output = None

    output = language.identify(func_input)

    assert output == expected_output, "output and expected_output don't match"
    #assert type(output) == dict, "type of output should be dict"
    #assert type(output) == list, "type of output should be list"
    #assert type(output) == str, "type of output should be str"
    #assert "mykey" in output, "output should have a key 'mykey'"
