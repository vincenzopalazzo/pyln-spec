#! /usr/bin/python3
from pyln_spec.core.message import MessageNamespace
import pyln_spec.bolt4 as bolt4


# FIXME: more tests
def test_bolt_04_csv():
    MessageNamespace(bolt4.csv)
