# test_hello.py

import hello

def test_hello(capsys):
    hello.print_hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"

