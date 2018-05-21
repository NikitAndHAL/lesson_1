from time_server import receive


def test_receive():
    assert receive(b'{"1": 1, "2": 4}') == {1: 1, 2: 4}