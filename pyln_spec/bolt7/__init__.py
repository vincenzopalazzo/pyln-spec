# This is the same __init__.py for all bolt dirs.
from pyln_spec.bolt7.csv import csv
from .gen_csv_version import __csv_version__
from .bolt import namespace
import sys

__all__ = [
    "csv",
    "namespace",
]

mod = sys.modules[__name__]
for d in namespace.subtypes, namespace.tlvtypes, namespace.messagetypes:
    for name in d:
        setattr(mod, name, d[name])
        __all__.append(name)
