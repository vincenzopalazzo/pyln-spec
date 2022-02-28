# This is the same __init__.py for all bolt dirs.
from pyln_spec.bolt1.gen_csv_version import __csv_version__
from pyln_spec.bolt1.bolt import namespace
from .csv import csv
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
