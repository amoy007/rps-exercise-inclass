def test_my_thing():
    print("testing")

#def test_example():
#    assert 2 == 3

from game import my_message # determine_winner

def test_my_message():
    x = my_message()
    assert x == "HELLO"