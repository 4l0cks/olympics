from olympics.__main__ import main
import pytest 
import argparse

def test_countries():
    argv = ['countries']
    main(argv)


def test_collective():
    argv = ["collective"]
    main(argv)


def test_individual():
    argv = ["individual"]
    main(argv)


def test_countries_top():
    argv = ["countries", "--top", "5"]
    main(argv)


def test_collective_top():
    argv = ["collective", "--top", "3"]
    main(argv)


def test_individual_top():
    argv = ["individual", "--top", "7"]
    main(argv)

def test_invalid_value():
    argv = ["countries", "--top", "-1"]
    with pytest.raises(argparse.ArgumentTypeError, match="-1 is not a positive number"):
        main(argv)
