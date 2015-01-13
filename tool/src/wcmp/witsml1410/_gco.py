# .\_gco.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2bd68004d120daf987d63b2efda66ae3eda8eaea
# Generated 2013-06-21 14:42:08.005000 by PyXB version 1.2.1
# Namespace http://www.isotc211.org/2005/gco [xmlns:gco]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9ff8bbae-daaa-11e2-b2e7-08002718187b')

# Import bindings for namespaces imported into schema
import _nsgroup

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.isotc211.org/2005/gco', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)

from _nsgroup import CharacterString # {http://www.isotc211.org/2005/gco}CharacterString
from _nsgroup import Boolean # {http://www.isotc211.org/2005/gco}Boolean
from _nsgroup import DateTime # {http://www.isotc211.org/2005/gco}DateTime
from _nsgroup import Decimal # {http://www.isotc211.org/2005/gco}Decimal
from _nsgroup import Real # {http://www.isotc211.org/2005/gco}Real
from _nsgroup import Integer # {http://www.isotc211.org/2005/gco}Integer
from _nsgroup import Record # {http://www.isotc211.org/2005/gco}Record
from _nsgroup import AbstractGenericName # {http://www.isotc211.org/2005/gco}AbstractGenericName
from _nsgroup import LocalName # {http://www.isotc211.org/2005/gco}LocalName
from _nsgroup import ScopedName # {http://www.isotc211.org/2005/gco}ScopedName
from _nsgroup import Date # {http://www.isotc211.org/2005/gco}Date
from _nsgroup import UnlimitedInteger # {http://www.isotc211.org/2005/gco}UnlimitedInteger
from _nsgroup import Binary # {http://www.isotc211.org/2005/gco}Binary
from _nsgroup import AbstractObject_ as AbstractObject # {http://www.isotc211.org/2005/gco}AbstractObject
from _nsgroup import TypeName # {http://www.isotc211.org/2005/gco}TypeName
from _nsgroup import MemberName # {http://www.isotc211.org/2005/gco}MemberName
from _nsgroup import Multiplicity # {http://www.isotc211.org/2005/gco}Multiplicity
from _nsgroup import MultiplicityRange # {http://www.isotc211.org/2005/gco}MultiplicityRange
from _nsgroup import RecordType # {http://www.isotc211.org/2005/gco}RecordType
from _nsgroup import Measure # {http://www.isotc211.org/2005/gco}Measure
from _nsgroup import Length # {http://www.isotc211.org/2005/gco}Length
from _nsgroup import Angle # {http://www.isotc211.org/2005/gco}Angle
from _nsgroup import Scale # {http://www.isotc211.org/2005/gco}Scale
from _nsgroup import Distance # {http://www.isotc211.org/2005/gco}Distance
from _nsgroup import Date_Type # {http://www.isotc211.org/2005/gco}Date_Type
from _nsgroup import UnlimitedInteger_Type # {http://www.isotc211.org/2005/gco}UnlimitedInteger_Type
from _nsgroup import Binary_Type # {http://www.isotc211.org/2005/gco}Binary_Type
from _nsgroup import AbstractObject_Type # {http://www.isotc211.org/2005/gco}AbstractObject_Type
from _nsgroup import CodeListValue_Type # {http://www.isotc211.org/2005/gco}CodeListValue_Type
from _nsgroup import TypeName_Type # {http://www.isotc211.org/2005/gco}TypeName_Type
from _nsgroup import MemberName_Type # {http://www.isotc211.org/2005/gco}MemberName_Type
from _nsgroup import Multiplicity_Type # {http://www.isotc211.org/2005/gco}Multiplicity_Type
from _nsgroup import MultiplicityRange_Type # {http://www.isotc211.org/2005/gco}MultiplicityRange_Type
from _nsgroup import RecordType_Type # {http://www.isotc211.org/2005/gco}RecordType_Type
from _nsgroup import TypeName_PropertyType # {http://www.isotc211.org/2005/gco}TypeName_PropertyType
from _nsgroup import MemberName_PropertyType # {http://www.isotc211.org/2005/gco}MemberName_PropertyType
from _nsgroup import Multiplicity_PropertyType # {http://www.isotc211.org/2005/gco}Multiplicity_PropertyType
from _nsgroup import MultiplicityRange_PropertyType # {http://www.isotc211.org/2005/gco}MultiplicityRange_PropertyType
from _nsgroup import Measure_PropertyType # {http://www.isotc211.org/2005/gco}Measure_PropertyType
from _nsgroup import Length_PropertyType # {http://www.isotc211.org/2005/gco}Length_PropertyType
from _nsgroup import Angle_PropertyType # {http://www.isotc211.org/2005/gco}Angle_PropertyType
from _nsgroup import Scale_PropertyType # {http://www.isotc211.org/2005/gco}Scale_PropertyType
from _nsgroup import Distance_PropertyType # {http://www.isotc211.org/2005/gco}Distance_PropertyType
from _nsgroup import CharacterString_PropertyType # {http://www.isotc211.org/2005/gco}CharacterString_PropertyType
from _nsgroup import Boolean_PropertyType # {http://www.isotc211.org/2005/gco}Boolean_PropertyType
from _nsgroup import GenericName_PropertyType # {http://www.isotc211.org/2005/gco}GenericName_PropertyType
from _nsgroup import LocalName_PropertyType # {http://www.isotc211.org/2005/gco}LocalName_PropertyType
from _nsgroup import ScopedName_PropertyType # {http://www.isotc211.org/2005/gco}ScopedName_PropertyType
from _nsgroup import UomAngle_PropertyType # {http://www.isotc211.org/2005/gco}UomAngle_PropertyType
from _nsgroup import UomLength_PropertyType # {http://www.isotc211.org/2005/gco}UomLength_PropertyType
from _nsgroup import UomScale_PropertyType # {http://www.isotc211.org/2005/gco}UomScale_PropertyType
from _nsgroup import UnitOfMeasure_PropertyType # {http://www.isotc211.org/2005/gco}UnitOfMeasure_PropertyType
from _nsgroup import UomArea_PropertyType # {http://www.isotc211.org/2005/gco}UomArea_PropertyType
from _nsgroup import UomVelocity_PropertyType # {http://www.isotc211.org/2005/gco}UomVelocity_PropertyType
from _nsgroup import UomTime_PropertyType # {http://www.isotc211.org/2005/gco}UomTime_PropertyType
from _nsgroup import UomVolume_PropertyType # {http://www.isotc211.org/2005/gco}UomVolume_PropertyType
from _nsgroup import DateTime_PropertyType # {http://www.isotc211.org/2005/gco}DateTime_PropertyType
from _nsgroup import Date_PropertyType # {http://www.isotc211.org/2005/gco}Date_PropertyType
from _nsgroup import Number_PropertyType # {http://www.isotc211.org/2005/gco}Number_PropertyType
from _nsgroup import Decimal_PropertyType # {http://www.isotc211.org/2005/gco}Decimal_PropertyType
from _nsgroup import Real_PropertyType # {http://www.isotc211.org/2005/gco}Real_PropertyType
from _nsgroup import Integer_PropertyType # {http://www.isotc211.org/2005/gco}Integer_PropertyType
from _nsgroup import UnlimitedInteger_PropertyType # {http://www.isotc211.org/2005/gco}UnlimitedInteger_PropertyType
from _nsgroup import Record_PropertyType # {http://www.isotc211.org/2005/gco}Record_PropertyType
from _nsgroup import RecordType_PropertyType # {http://www.isotc211.org/2005/gco}RecordType_PropertyType
from _nsgroup import Binary_PropertyType # {http://www.isotc211.org/2005/gco}Binary_PropertyType
from _nsgroup import ObjectReference_PropertyType # {http://www.isotc211.org/2005/gco}ObjectReference_PropertyType
