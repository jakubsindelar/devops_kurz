# test_hello.py

def print_hello():
    print("Hello, World!")

def test_print_hello(capsys):
    print_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"

