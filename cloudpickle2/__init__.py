from cloudpickle2.cloudpickle2 import *  # noqa
from cloudpickle2.cloudpickle_fast import CloudPickler, dumps, dump  # noqa

# Conform to the convention used by python serialization libraries, which
# expose their Pickler subclass at top-level under the  "Pickler" name.
Pickler = CloudPickler

__version__ = '2.3.0.dev0'