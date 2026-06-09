# .\witsml1411_obj_toolErrorTermSet.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:bff9e1cadb696f69d77e8e135b7b2cb67426d3a5
# Generated 2013-03-20 17:54:38.692000 by PyXB version 1.2.1
# Namespace http://www.witsml.org/schemas/1series

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:23af8300-91b1-11e2-8e96-08002712d133')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
from . import _abs

Namespace = pyxb.namespace.NamespaceForURI('http://www.witsml.org/schemas/1series', create_if_missing=True)
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
    saxer.parse(io.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractBoolean
class abstractBoolean (pyxb.binding.datatypes.boolean):

    """This type disallows an "empty" boolean value.
			This type should not be used directly except to derive another type.
			All boolean types should be derived from this type rather than using xsd:boolen."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractBoolean')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 24, 1)
    _Documentation = 'This type disallows an "empty" boolean value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll boolean types should be derived from this type rather than using xsd:boolen.'
abstractBoolean._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractBoolean._CF_pattern.addPattern(pattern='.+')
abstractBoolean._InitializeFacetMap(abstractBoolean._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractBoolean', abstractBoolean)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractDateTime
class abstractDateTime (pyxb.binding.datatypes.dateTime):

    """This type disallows an "empty" dateTime value.
			This type should not be used directly except to derive another type.
			All dateTime types should be derived from this type rather than using xsd:dateTime."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractDateTime')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 35, 1)
    _Documentation = 'This type disallows an "empty" dateTime value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll dateTime types should be derived from this type rather than using xsd:dateTime.'
abstractDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDateTime._CF_pattern.addPattern(pattern='.+')
abstractDateTime._InitializeFacetMap(abstractDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractDateTime', abstractDateTime)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractDate
class abstractDate (pyxb.binding.datatypes.date):

    """This type disallows an "empty" date value.
			This type should not be used directly except to derive another type.
			All dateTime types should be derived from this type rather than using xsd:dateTime."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractDate')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 46, 1)
    _Documentation = 'This type disallows an "empty" date value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll dateTime types should be derived from this type rather than using xsd:dateTime.'
abstractDate._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDate._CF_pattern.addPattern(pattern='.+')
abstractDate._InitializeFacetMap(abstractDate._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractDate', abstractDate)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractDouble
class abstractDouble (pyxb.binding.datatypes.double):

    """This type disallows an "empty" double value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractDouble')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 57, 1)
    _Documentation = 'This type disallows an "empty" double value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractDouble._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDouble._CF_pattern.addPattern(pattern='.+')
abstractDouble._InitializeFacetMap(abstractDouble._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractDouble', abstractDouble)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractShort
class abstractShort (pyxb.binding.datatypes.short):

    """This type disallows an "empty" short value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractShort')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 67, 1)
    _Documentation = 'This type disallows an "empty" short value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractShort._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractShort._CF_pattern.addPattern(pattern='.+')
abstractShort._InitializeFacetMap(abstractShort._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractShort', abstractShort)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractInt
class abstractInt (pyxb.binding.datatypes.int):

    """This type disallows an "empty" int value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractInt')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 77, 1)
    _Documentation = 'This type disallows an "empty" int value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractInt._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractInt._CF_pattern.addPattern(pattern='.+')
abstractInt._InitializeFacetMap(abstractInt._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractInt', abstractInt)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractString
class abstractString (pyxb.binding.datatypes.string):

    """The intended abstract supertype of all strings.
			This abstract type allows the control over whitespace for all strings to be defined at a high level. 
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 87, 1)
    _Documentation = 'The intended abstract supertype of all strings.\n\t\t\tThis abstract type allows the control over whitespace for all strings to be defined at a high level. \n\t\t\tThis type should not be used directly except to derive another type.'
abstractString._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
abstractString._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
abstractString._InitializeFacetMap(abstractString._CF_minLength,
   abstractString._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'abstractString', abstractString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractUncollapsedString
class abstractUncollapsedString (pyxb.binding.datatypes.string):

    """The intended abstract supertype of all strings that must maintain whitespace. 
			The type abstractString should normally be used.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractUncollapsedString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 138, 1)
    _Documentation = 'The intended abstract supertype of all strings that must maintain whitespace. \n\t\t\tThe type abstractString should normally be used.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractUncollapsedString._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
abstractUncollapsedString._InitializeFacetMap(abstractUncollapsedString._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'abstractUncollapsedString', abstractUncollapsedString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractMaximumLengthString
class abstractMaximumLengthString (abstractString):

    """This defines the maximum acceptable length of a
			string that can be stored in a data base."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractMaximumLengthString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 122, 1)
    _Documentation = 'This defines the maximum acceptable length of a\n\t\t\tstring that can be stored in a data base.'
abstractMaximumLengthString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
abstractMaximumLengthString._InitializeFacetMap(abstractMaximumLengthString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractMaximumLengthString', abstractMaximumLengthString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractPositiveCount
class abstractPositiveCount (abstractShort):

    """A positive integer (one based count or index) with a maximum value of 32767 (2-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractPositiveCount')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 155, 1)
    _Documentation = 'A positive integer (one based count or index) with a maximum value of 32767 (2-bytes).'
abstractPositiveCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=abstractPositiveCount, value=pyxb.binding.datatypes.short(1))
abstractPositiveCount._InitializeFacetMap(abstractPositiveCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'abstractPositiveCount', abstractPositiveCount)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractTimeZone
class abstractTimeZone (abstractString):

    """A time zone conforming to the XSD:dateTime specification.
			It should be of the form "Z" or "shh.mm" where 
				"s" is "+" or "-", 
				"hh" is 00 to 23 and
				"mm" is 00 to 59."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractTimeZone')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 170, 1)
    _Documentation = 'A time zone conforming to the XSD:dateTime specification.\n\t\t\tIt should be of the form "Z" or "shh.mm" where \n\t\t\t\t"s" is "+" or "-", \n\t\t\t\t"hh" is 00 to 23 and\n\t\t\t\t"mm" is 00 to 59.'
abstractTimeZone._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractTimeZone._CF_pattern.addPattern(pattern='[Z]|([\\-+](([01][0-9])|(2[0-3])):[0-5][0-9])')
abstractTimeZone._InitializeFacetMap(abstractTimeZone._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractTimeZone', abstractTimeZone)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractNameString
class abstractNameString (abstractString):

    """The intended abstract supertype of all user assigned human 
			recognizable contextual name types. 
			There should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.
			This type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractNameString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 184, 1)
    _Documentation = 'The intended abstract supertype of all user assigned human \n\t\t\trecognizable contextual name types. \n\t\t\tThere should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.\n\t\t\tThis type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration.'
abstractNameString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
abstractNameString._InitializeFacetMap(abstractNameString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractNameString', abstractNameString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractUidString
class abstractUidString (abstractString):

    """The intended abstract supertype of all locally unique identifiers. 
			The value is not intended to convey any semantic content (e.g., it may be computer generated). 
			The value is only required to be unique within a context in a document (e.g., defined via key and keyref). 
			There is no guarantee that the same data in multiple documents will utilize the same uid value 
			unless enforced by the source of the document (e.g., a document server).
			Spaces are not allowed."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractUidString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 196, 1)
    _Documentation = 'The intended abstract supertype of all locally unique identifiers. \n\t\t\tThe value is not intended to convey any semantic content (e.g., it may be computer generated). \n\t\t\tThe value is only required to be unique within a context in a document (e.g., defined via key and keyref). \n\t\t\tThere is no guarantee that the same data in multiple documents will utilize the same uid value \n\t\t\tunless enforced by the source of the document (e.g., a document server).\n\t\t\tSpaces are not allowed.'
abstractUidString._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractUidString._CF_pattern.addPattern(pattern='[^ ]*')
abstractUidString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
abstractUidString._InitializeFacetMap(abstractUidString._CF_pattern,
   abstractUidString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractUidString', abstractUidString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractDescriptionString
class abstractDescriptionString (abstractString):

    """A textual description of something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractDescriptionString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 222, 1)
    _Documentation = 'A textual description of something.'
abstractDescriptionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
abstractDescriptionString._InitializeFacetMap(abstractDescriptionString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractDescriptionString', abstractDescriptionString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractString32
class abstractString32 (abstractString):

    """A 32 character string."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractString32')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 232, 1)
    _Documentation = 'A 32 character string.'
abstractString32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
abstractString32._InitializeFacetMap(abstractString32._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractString32', abstractString32)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractTypeEnum
class abstractTypeEnum (abstractString):

    """The intended abstract supertype of all enumerated "types".
			This abstract type allows the maximum length of a type enumeration to be centrally defined.
			This type should not be used directly except to derive another type.
			It should also be used for uncontrolled strings which are candidates to become enumerations at a future date."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 242, 1)
    _Documentation = 'The intended abstract supertype of all enumerated "types".\n\t\t\tThis abstract type allows the maximum length of a type enumeration to be centrally defined.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tIt should also be used for uncontrolled strings which are candidates to become enumerations at a future date.'
abstractTypeEnum._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
abstractTypeEnum._InitializeFacetMap(abstractTypeEnum._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractTypeEnum', abstractTypeEnum)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractUomEnum
class abstractUomEnum (abstractString):

    """The intended abstract supertype of all "units of measure".
			This abstract type allows the maximum length of a UOM enumeration to be centrally defined. 
			This type is abstract in the sense that it should not be used directly 
			except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractUomEnum')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 254, 1)
    _Documentation = 'The intended abstract supertype of all "units of measure".\n\t\t\tThis abstract type allows the maximum length of a UOM enumeration to be centrally defined. \n\t\t\tThis type is abstract in the sense that it should not be used directly \n\t\t\texcept to derive another type.'
abstractUomEnum._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(24))
abstractUomEnum._InitializeFacetMap(abstractUomEnum._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractUomEnum', abstractUomEnum)

# Atomic simple type: {http://www.witsml.org/schemas/1series}date
class date (abstractDate):

    """A julian date."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'date')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 29, 1)
    _Documentation = 'A julian date.'
date._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'date', date)

# Atomic simple type: {http://www.witsml.org/schemas/1series}timestamp
class timestamp (abstractDateTime):

    """A date with a time of day and a mandatory time zone offset.
			This must captute the correct date-time relative to UTC. It is not necessary to 
			use a local time zone because software may convert the date-time to a different 
			local time zone (while retaining correct date-time relative to UTC).
			See acquisitionTmeZone in commonData for the original time zone of times in an object."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timestamp')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 36, 1)
    _Documentation = 'A date with a time of day and a mandatory time zone offset.\n\t\t\tThis must captute the correct date-time relative to UTC. It is not necessary to \n\t\t\tuse a local time zone because software may convert the date-time to a different \n\t\t\tlocal time zone (while retaining correct date-time relative to UTC).\n\t\t\tSee acquisitionTmeZone in commonData for the original time zone of times in an object.'
timestamp._CF_pattern = pyxb.binding.facets.CF_pattern()
timestamp._CF_pattern.addPattern(pattern='.+T.+[Z+\\-].*')
timestamp._InitializeFacetMap(timestamp._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'timestamp', timestamp)

# Atomic simple type: {http://www.witsml.org/schemas/1series}calendarYear
class calendarYear (abstractInt):

    """A calendar year (CCYY) in the gregorian calendar.
			This type is meant to captute original invariant values. 
			It is not intended to be used in "time math" where knowledge of the time zone is needed."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'calendarYear')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 79, 1)
    _Documentation = 'A calendar year (CCYY) in the gregorian calendar.\n\t\t\tThis type is meant to captute original invariant values. \n\t\t\tIt is not intended to be used in "time math" where knowledge of the time zone is needed.'
calendarYear._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=calendarYear, value=pyxb.binding.datatypes.int(9999))
calendarYear._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=calendarYear, value=pyxb.binding.datatypes.int(1000))
calendarYear._InitializeFacetMap(calendarYear._CF_maxInclusive,
   calendarYear._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'calendarYear', calendarYear)

# Atomic simple type: {http://www.witsml.org/schemas/1series}logicalBoolean
class logicalBoolean (abstractBoolean):

    """Values of "true" (or "1") and "false" (or "0")."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'logicalBoolean')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 95, 1)
    _Documentation = 'Values of "true" (or "1") and "false" (or "0").'
logicalBoolean._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'logicalBoolean', logicalBoolean)

# Atomic simple type: {http://www.witsml.org/schemas/1series}unitlessQuantity
class unitlessQuantity (abstractDouble):

    """A unitless quantity. This should not 
			be confused with a dimensionless measure."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unitlessQuantity')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 138, 1)
    _Documentation = 'A unitless quantity. This should not \n\t\t\tbe confused with a dimensionless measure.'
unitlessQuantity._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'unitlessQuantity', unitlessQuantity)

# Atomic simple type: {http://www.witsml.org/schemas/1series}shortDescriptionString
class shortDescriptionString (abstractString):

    """A short textual description of something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'shortDescriptionString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 360, 1)
    _Documentation = 'A short textual description of something.'
shortDescriptionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
shortDescriptionString._InitializeFacetMap(shortDescriptionString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'shortDescriptionString', shortDescriptionString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}schemaVersionString
class schemaVersionString (abstractString):

    """The version of the schema.
			The first level is fixed. The fourth level can vary
			to represent on the constraints defined in enumerations and 
			XML loader files. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'schemaVersionString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 426, 1)
    _Documentation = 'The version of the schema.\n\t\t\tThe first level is fixed. The fourth level can vary\n\t\t\tto represent on the constraints defined in enumerations and \n\t\t\tXML loader files. '
schemaVersionString._CF_pattern = pyxb.binding.facets.CF_pattern()
schemaVersionString._CF_pattern.addPattern(pattern='1\\.[4-9]\\.[0-9]\\.([0-9]|([1-9][0-9]))')
schemaVersionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
schemaVersionString._InitializeFacetMap(schemaVersionString._CF_pattern,
   schemaVersionString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'schemaVersionString', schemaVersionString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}uncollapsedString
class uncollapsedString (abstractUncollapsedString):

    """A textual string that retains all whitespace."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uncollapsedString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 492, 1)
    _Documentation = 'A textual string that retains all whitespace.'
uncollapsedString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
uncollapsedString._InitializeFacetMap(uncollapsedString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'uncollapsedString', uncollapsedString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}iadcBearingWearCode
class iadcBearingWearCode (abstractString):

    """IADC bearing wear code: integer 0 - 8 or one of the letters E, F, N or X. ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'iadcBearingWearCode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 501, 1)
    _Documentation = 'IADC bearing wear code: integer 0 - 8 or one of the letters E, F, N or X. .'
iadcBearingWearCode._CF_pattern = pyxb.binding.facets.CF_pattern()
iadcBearingWearCode._CF_pattern.addPattern(pattern='[0-8EFNX]')
iadcBearingWearCode._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
iadcBearingWearCode._InitializeFacetMap(iadcBearingWearCode._CF_pattern,
   iadcBearingWearCode._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'iadcBearingWearCode', iadcBearingWearCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}geodeticZoneString
class geodeticZoneString (abstractString):

    """A geodetic zone with values from 1 to 60 and a required direction 
			of "N" (North) or "S" (South). For example, "21N"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geodeticZoneString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 511, 1)
    _Documentation = 'A geodetic zone with values from 1 to 60 and a required direction \n\t\t\tof "N" (North) or "S" (South). For example, "21N".'
geodeticZoneString._CF_pattern = pyxb.binding.facets.CF_pattern()
geodeticZoneString._CF_pattern.addPattern(pattern='([1-9]|[1-5][0-9]|60)[NS]')
geodeticZoneString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
geodeticZoneString._InitializeFacetMap(geodeticZoneString._CF_pattern,
   geodeticZoneString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'geodeticZoneString', geodeticZoneString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}sectionNumber
class sectionNumber (abstractString):

    """Sections are numbered "1" through "36." 
			Irregular sections may be designated with a single value after a decimal point.
			USA Public Land Survey System."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sectionNumber')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 657, 1)
    _Documentation = 'Sections are numbered "1" through "36." \n\t\t\tIrregular sections may be designated with a single value after a decimal point.\n\t\t\tUSA Public Land Survey System.'
sectionNumber._CF_pattern = pyxb.binding.facets.CF_pattern()
sectionNumber._CF_pattern.addPattern(pattern='[+]?([1-9]|[1-2][0-9]|3[0-6])\\.?[0-9]?')
sectionNumber._InitializeFacetMap(sectionNumber._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'sectionNumber', sectionNumber)

# Atomic simple type: {http://www.witsml.org/schemas/1series}publicLandSurveySystemQuarterTownship
class publicLandSurveySystemQuarterTownship (abstractString):

    """Designates a particular quarter of a township.
			USA Public Land Survey System."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'publicLandSurveySystemQuarterTownship')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 669, 1)
    _Documentation = 'Designates a particular quarter of a township.\n\t\t\tUSA Public Land Survey System.'
publicLandSurveySystemQuarterTownship._CF_pattern = pyxb.binding.facets.CF_pattern()
publicLandSurveySystemQuarterTownship._CF_pattern.addPattern(pattern='NE|NW|SW|SE')
publicLandSurveySystemQuarterTownship._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
publicLandSurveySystemQuarterTownship._InitializeFacetMap(publicLandSurveySystemQuarterTownship._CF_pattern,
   publicLandSurveySystemQuarterTownship._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'publicLandSurveySystemQuarterTownship', publicLandSurveySystemQuarterTownship)

# Atomic simple type: {http://www.witsml.org/schemas/1series}publicLandSurveySystemQuarterSection
class publicLandSurveySystemQuarterSection (abstractString):

    """Some combination of NE,NW,SW,SE,N2,S2,E2,W2,C,TRxx,LTnn.
			USA Public Land Survey System."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'publicLandSurveySystemQuarterSection')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 681, 1)
    _Documentation = 'Some combination of NE,NW,SW,SE,N2,S2,E2,W2,C,TRxx,LTnn.\n\t\t\tUSA Public Land Survey System.'
publicLandSurveySystemQuarterSection._CF_pattern = pyxb.binding.facets.CF_pattern()
publicLandSurveySystemQuarterSection._CF_pattern.addPattern(pattern='(NE|NW|SW|SE|N2|S2|E2|W2|C|LT[0-9]{2,2}|TR[a-zA-Z0-9]{1,2}){1,3}')
publicLandSurveySystemQuarterSection._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
publicLandSurveySystemQuarterSection._InitializeFacetMap(publicLandSurveySystemQuarterSection._CF_pattern,
   publicLandSurveySystemQuarterSection._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'publicLandSurveySystemQuarterSection', publicLandSurveySystemQuarterSection)

# Atomic simple type: {http://www.witsml.org/schemas/1series}gtZeroAndLeOne
class gtZeroAndLeOne (abstractDouble):

    """A floating point value which is greater than zero and 
			less than or equal to one."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gtZeroAndLeOne')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 741, 1)
    _Documentation = 'A floating point value which is greater than zero and \n\t\t\tless than or equal to one.'
gtZeroAndLeOne._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=abstractDouble, value=pyxb.binding.datatypes.anySimpleType('0'))
gtZeroAndLeOne._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=gtZeroAndLeOne, value=pyxb.binding.datatypes.double(1.0))
gtZeroAndLeOne._InitializeFacetMap(gtZeroAndLeOne._CF_minExclusive,
   gtZeroAndLeOne._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'gtZeroAndLeOne', gtZeroAndLeOne)

# Atomic simple type: {http://www.witsml.org/schemas/1series}nonNegativeCount
class nonNegativeCount (abstractShort):

    """A non-negative integer (zero based count or index) with a maximum value of 32767 (2-bytes).
			For items that represent "number of" something or a "sequential" count or index."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nonNegativeCount')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 752, 1)
    _Documentation = 'A non-negative integer (zero based count or index) with a maximum value of 32767 (2-bytes).\n\t\t\tFor items that represent "number of" something or a "sequential" count or index.'
nonNegativeCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=nonNegativeCount, value=pyxb.binding.datatypes.short(0))
nonNegativeCount._InitializeFacetMap(nonNegativeCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'nonNegativeCount', nonNegativeCount)

# Atomic simple type: {http://www.witsml.org/schemas/1series}positiveBigCount
class positiveBigCount (abstractInt):

    """A large positive integer (one based count or index) with a maximum value of 2,147,483,647 (4-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positiveBigCount')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 779, 1)
    _Documentation = 'A large positive integer (one based count or index) with a maximum value of 2,147,483,647 (4-bytes).'
positiveBigCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveBigCount, value=pyxb.binding.datatypes.int(1))
positiveBigCount._InitializeFacetMap(positiveBigCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'positiveBigCount', positiveBigCount)

# Atomic simple type: {http://www.witsml.org/schemas/1series}integerCount
class integerCount (abstractInt):

    """A positive or negative count with a maximum positive value of 2147483647 (4-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerCount')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 792, 1)
    _Documentation = 'A positive or negative count with a maximum positive value of 2147483647 (4-bytes).'
integerCount._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'integerCount', integerCount)

# Atomic simple type: {http://www.witsml.org/schemas/1series}beaufortScaleIntegerCode
class beaufortScaleIntegerCode (abstractShort):

    """An estimate wind strength based on the Beaufort Wind Scale. 
			Values range from 0 (calm) to 12 (hurricane). """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'beaufortScaleIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 799, 1)
    _Documentation = 'An estimate wind strength based on the Beaufort Wind Scale. \n\t\t\tValues range from 0 (calm) to 12 (hurricane). '
beaufortScaleIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=beaufortScaleIntegerCode, value=pyxb.binding.datatypes.short(12))
beaufortScaleIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=beaufortScaleIntegerCode, value=pyxb.binding.datatypes.short(0))
beaufortScaleIntegerCode._InitializeFacetMap(beaufortScaleIntegerCode._CF_maxInclusive,
   beaufortScaleIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'beaufortScaleIntegerCode', beaufortScaleIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}pumpActionIntegerCode
class pumpActionIntegerCode (abstractShort):

    """Pump Action: 1 = Single acting, 2 = double acting."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pumpActionIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 810, 1)
    _Documentation = 'Pump Action: 1 = Single acting, 2 = double acting.'
pumpActionIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=pumpActionIntegerCode, value=pyxb.binding.datatypes.short(2))
pumpActionIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=pumpActionIntegerCode, value=pyxb.binding.datatypes.short(1))
pumpActionIntegerCode._InitializeFacetMap(pumpActionIntegerCode._CF_maxInclusive,
   pumpActionIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'pumpActionIntegerCode', pumpActionIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}iadcIntegerCode
class iadcIntegerCode (abstractShort):

    """IADC codes: 0 to 8."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'iadcIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 820, 1)
    _Documentation = 'IADC codes: 0 to 8.'
iadcIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=iadcIntegerCode, value=pyxb.binding.datatypes.short(8))
iadcIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=iadcIntegerCode, value=pyxb.binding.datatypes.short(0))
iadcIntegerCode._InitializeFacetMap(iadcIntegerCode._CF_maxInclusive,
   iadcIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'iadcIntegerCode', iadcIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}levelIntegerCode
class levelIntegerCode (abstractShort):

    """Integer level code from 1 through 5."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'levelIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 830, 1)
    _Documentation = 'Integer level code from 1 through 5.'
levelIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=levelIntegerCode, value=pyxb.binding.datatypes.short(8))
levelIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=levelIntegerCode, value=pyxb.binding.datatypes.short(0))
levelIntegerCode._InitializeFacetMap(levelIntegerCode._CF_maxInclusive,
   levelIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'levelIntegerCode', levelIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}str2
class str2 (abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'str2')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 878, 1)
    _Documentation = ''
str2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
str2._InitializeFacetMap(str2._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'str2', str2)

# Atomic simple type: {http://www.witsml.org/schemas/1series}str16
class str16 (abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'str16')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 887, 1)
    _Documentation = ''
str16._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
str16._InitializeFacetMap(str16._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'str16', str16)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractCommentString
class abstractCommentString (abstractMaximumLengthString):

    """The intended abstract supertype of all comments or remarks 
			intended for human consumption. 
			There should be no assumption that semantics can be extracted from the field by a computer. 
			Neither should there be an assumption that any two humans will interpret the information 
			in the same way (i.e., it may not be interoperable)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractCommentString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 211, 1)
    _Documentation = 'The intended abstract supertype of all comments or remarks \n\t\t\tintended for human consumption. \n\t\t\tThere should be no assumption that semantics can be extracted from the field by a computer. \n\t\t\tNeither should there be an assumption that any two humans will interpret the information \n\t\t\tin the same way (i.e., it may not be interoperable).'
abstractCommentString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'abstractCommentString', abstractCommentString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ActivityClassType
class ActivityClassType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActivityClassType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 26, 1)
    _Documentation = None
ActivityClassType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ActivityClassType, enum_prefix=None)
ActivityClassType.planned = ActivityClassType._CF_enumeration.addEnumeration(unicode_value='planned', tag='planned')
ActivityClassType.unplanned = ActivityClassType._CF_enumeration.addEnumeration(unicode_value='unplanned', tag='unplanned')
ActivityClassType.downtime = ActivityClassType._CF_enumeration.addEnumeration(unicode_value='downtime', tag='downtime')
ActivityClassType.unknown = ActivityClassType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ActivityClassType._InitializeFacetMap(ActivityClassType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ActivityClassType', ActivityClassType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ActivityCode
class ActivityCode (abstractTypeEnum):

    """Activity codes.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActivityCode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 53, 1)
    _Documentation = 'Activity codes.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
ActivityCode._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ActivityCode', ActivityCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AuthorizationStatus
class AuthorizationStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AuthorizationStatus')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 62, 1)
    _Documentation = ''
AuthorizationStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AuthorizationStatus, enum_prefix=None)
AuthorizationStatus.draft = AuthorizationStatus._CF_enumeration.addEnumeration(unicode_value='draft', tag='draft')
AuthorizationStatus.authorized = AuthorizationStatus._CF_enumeration.addEnumeration(unicode_value='authorized', tag='authorized')
AuthorizationStatus.superceded = AuthorizationStatus._CF_enumeration.addEnumeration(unicode_value='superceded', tag='superceded')
AuthorizationStatus.withdrawn = AuthorizationStatus._CF_enumeration.addEnumeration(unicode_value='withdrawn', tag='withdrawn')
AuthorizationStatus.unknown = AuthorizationStatus._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
AuthorizationStatus._InitializeFacetMap(AuthorizationStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AuthorizationStatus', AuthorizationStatus)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AziRef
class AziRef (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AziRef')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 97, 1)
    _Documentation = None
AziRef._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AziRef, enum_prefix=None)
AziRef.magnetic_north = AziRef._CF_enumeration.addEnumeration(unicode_value='magnetic north', tag='magnetic_north')
AziRef.grid_north = AziRef._CF_enumeration.addEnumeration(unicode_value='grid north', tag='grid_north')
AziRef.true_north = AziRef._CF_enumeration.addEnumeration(unicode_value='true north', tag='true_north')
AziRef.unknown = AziRef._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
AziRef._InitializeFacetMap(AziRef._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AziRef', AziRef)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BearingType
class BearingType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BearingType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 129, 1)
    _Documentation = None
BearingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BearingType, enum_prefix=None)
BearingType.oil_seal = BearingType._CF_enumeration.addEnumeration(unicode_value='oil seal', tag='oil_seal')
BearingType.mud_lube = BearingType._CF_enumeration.addEnumeration(unicode_value='mud lube', tag='mud_lube')
BearingType.other = BearingType._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
BearingType.unknown = BearingType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BearingType._InitializeFacetMap(BearingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BearingType', BearingType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BitDullCode
class BitDullCode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent a classification of a drill bit based 
			on its reason for being declared inoperable, as originally defined by the IADC."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BitDullCode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 156, 1)
    _Documentation = 'These values represent a classification of a drill bit based \n\t\t\ton its reason for being declared inoperable, as originally defined by the IADC.'
BitDullCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BitDullCode, enum_prefix=None)
BitDullCode.BC = BitDullCode._CF_enumeration.addEnumeration(unicode_value='BC', tag='BC')
BitDullCode.BT = BitDullCode._CF_enumeration.addEnumeration(unicode_value='BT', tag='BT')
BitDullCode.BU = BitDullCode._CF_enumeration.addEnumeration(unicode_value='BU', tag='BU')
BitDullCode.CC = BitDullCode._CF_enumeration.addEnumeration(unicode_value='CC', tag='CC')
BitDullCode.CD = BitDullCode._CF_enumeration.addEnumeration(unicode_value='CD', tag='CD')
BitDullCode.CI = BitDullCode._CF_enumeration.addEnumeration(unicode_value='CI', tag='CI')
BitDullCode.CR = BitDullCode._CF_enumeration.addEnumeration(unicode_value='CR', tag='CR')
BitDullCode.CT = BitDullCode._CF_enumeration.addEnumeration(unicode_value='CT', tag='CT')
BitDullCode.ER = BitDullCode._CF_enumeration.addEnumeration(unicode_value='ER', tag='ER')
BitDullCode.FC = BitDullCode._CF_enumeration.addEnumeration(unicode_value='FC', tag='FC')
BitDullCode.HC = BitDullCode._CF_enumeration.addEnumeration(unicode_value='HC', tag='HC')
BitDullCode.JD = BitDullCode._CF_enumeration.addEnumeration(unicode_value='JD', tag='JD')
BitDullCode.LC = BitDullCode._CF_enumeration.addEnumeration(unicode_value='LC', tag='LC')
BitDullCode.LN = BitDullCode._CF_enumeration.addEnumeration(unicode_value='LN', tag='LN')
BitDullCode.LT = BitDullCode._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
BitDullCode.NO = BitDullCode._CF_enumeration.addEnumeration(unicode_value='NO', tag='NO')
BitDullCode.OC = BitDullCode._CF_enumeration.addEnumeration(unicode_value='OC', tag='OC')
BitDullCode.PB = BitDullCode._CF_enumeration.addEnumeration(unicode_value='PB', tag='PB')
BitDullCode.PN = BitDullCode._CF_enumeration.addEnumeration(unicode_value='PN', tag='PN')
BitDullCode.RG = BitDullCode._CF_enumeration.addEnumeration(unicode_value='RG', tag='RG')
BitDullCode.RO = BitDullCode._CF_enumeration.addEnumeration(unicode_value='RO', tag='RO')
BitDullCode.SD = BitDullCode._CF_enumeration.addEnumeration(unicode_value='SD', tag='SD')
BitDullCode.SS = BitDullCode._CF_enumeration.addEnumeration(unicode_value='SS', tag='SS')
BitDullCode.TR = BitDullCode._CF_enumeration.addEnumeration(unicode_value='TR', tag='TR')
BitDullCode.WO = BitDullCode._CF_enumeration.addEnumeration(unicode_value='WO', tag='WO')
BitDullCode.WT = BitDullCode._CF_enumeration.addEnumeration(unicode_value='WT', tag='WT')
BitDullCode.unknown = BitDullCode._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BitDullCode._InitializeFacetMap(BitDullCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BitDullCode', BitDullCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BitReasonPulled
class BitReasonPulled (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the reason for pulling a drill bit 
			from the wellbore, as originally defined by the IADC."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BitReasonPulled')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 302, 1)
    _Documentation = 'These values represent the reason for pulling a drill bit \n\t\t\tfrom the wellbore, as originally defined by the IADC.'
BitReasonPulled._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BitReasonPulled, enum_prefix=None)
BitReasonPulled.BHA = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='BHA', tag='BHA')
BitReasonPulled.CM = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='CM', tag='CM')
BitReasonPulled.CP = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='CP', tag='CP')
BitReasonPulled.DMF = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='DMF', tag='DMF')
BitReasonPulled.DP = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='DP', tag='DP')
BitReasonPulled.DST = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='DST', tag='DST')
BitReasonPulled.DTF = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='DTF', tag='DTF')
BitReasonPulled.FM = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='FM', tag='FM')
BitReasonPulled.HP = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='HP', tag='HP')
BitReasonPulled.HR = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='HR', tag='HR')
BitReasonPulled.LOG = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='LOG', tag='LOG')
BitReasonPulled.PP = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='PP', tag='PP')
BitReasonPulled.PR = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
BitReasonPulled.RIG = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='RIG', tag='RIG')
BitReasonPulled.TD = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='TD', tag='TD')
BitReasonPulled.TQ = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='TQ', tag='TQ')
BitReasonPulled.TW = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='TW', tag='TW')
BitReasonPulled.WC = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='WC', tag='WC')
BitReasonPulled.unknown = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BitReasonPulled._InitializeFacetMap(BitReasonPulled._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BitReasonPulled', BitReasonPulled)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BitType
class BitType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drill/core bit."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BitType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 408, 1)
    _Documentation = 'These values represent the type of drill/core bit.'
BitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BitType, enum_prefix=None)
BitType.diamond = BitType._CF_enumeration.addEnumeration(unicode_value='diamond', tag='diamond')
BitType.diamond_core = BitType._CF_enumeration.addEnumeration(unicode_value='diamond core', tag='diamond_core')
BitType.insert_roller_cone = BitType._CF_enumeration.addEnumeration(unicode_value='insert roller cone', tag='insert_roller_cone')
BitType.PDC = BitType._CF_enumeration.addEnumeration(unicode_value='PDC', tag='PDC')
BitType.PDC_core = BitType._CF_enumeration.addEnumeration(unicode_value='PDC core', tag='PDC_core')
BitType.roller_cone = BitType._CF_enumeration.addEnumeration(unicode_value='roller cone', tag='roller_cone')
BitType.unknown = BitType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BitType._InitializeFacetMap(BitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BitType', BitType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BhaStatus
class BhaStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BhaStatus')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 453, 1)
    _Documentation = None
BhaStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BhaStatus, enum_prefix=None)
BhaStatus.final = BhaStatus._CF_enumeration.addEnumeration(unicode_value='final', tag='final')
BhaStatus.progress = BhaStatus._CF_enumeration.addEnumeration(unicode_value='progress', tag='progress')
BhaStatus.plan = BhaStatus._CF_enumeration.addEnumeration(unicode_value='plan', tag='plan')
BhaStatus.unknown = BhaStatus._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BhaStatus._InitializeFacetMap(BhaStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BhaStatus', BhaStatus)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BladeShapeType
class BladeShapeType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BladeShapeType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 480, 1)
    _Documentation = None
BladeShapeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BladeShapeType, enum_prefix=None)
BladeShapeType.dynamic = BladeShapeType._CF_enumeration.addEnumeration(unicode_value='dynamic', tag='dynamic')
BladeShapeType.melon = BladeShapeType._CF_enumeration.addEnumeration(unicode_value='melon', tag='melon')
BladeShapeType.spiral = BladeShapeType._CF_enumeration.addEnumeration(unicode_value='spiral', tag='spiral')
BladeShapeType.straight = BladeShapeType._CF_enumeration.addEnumeration(unicode_value='straight', tag='straight')
BladeShapeType.variable = BladeShapeType._CF_enumeration.addEnumeration(unicode_value='variable', tag='variable')
BladeShapeType.unknown = BladeShapeType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BladeShapeType._InitializeFacetMap(BladeShapeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BladeShapeType', BladeShapeType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BladeType
class BladeType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BladeType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 517, 1)
    _Documentation = None
BladeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BladeType, enum_prefix=None)
BladeType.clamp_on = BladeType._CF_enumeration.addEnumeration(unicode_value='clamp-on', tag='clamp_on')
BladeType.integral = BladeType._CF_enumeration.addEnumeration(unicode_value='integral', tag='integral')
BladeType.sleeve = BladeType._CF_enumeration.addEnumeration(unicode_value='sleeve', tag='sleeve')
BladeType.welded = BladeType._CF_enumeration.addEnumeration(unicode_value='welded', tag='welded')
BladeType.unknown = BladeType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BladeType._InitializeFacetMap(BladeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BladeType', BladeType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BopType
class BopType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BopType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 549, 1)
    _Documentation = None
BopType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BopType, enum_prefix=None)
BopType.annular_preventer = BopType._CF_enumeration.addEnumeration(unicode_value='annular preventer', tag='annular_preventer')
BopType.shear_ram = BopType._CF_enumeration.addEnumeration(unicode_value='shear ram', tag='shear_ram')
BopType.blind_ram = BopType._CF_enumeration.addEnumeration(unicode_value='blind ram', tag='blind_ram')
BopType.pipe_ram = BopType._CF_enumeration.addEnumeration(unicode_value='pipe ram', tag='pipe_ram')
BopType.drilling_spool = BopType._CF_enumeration.addEnumeration(unicode_value='drilling spool', tag='drilling_spool')
BopType.flexible_joint = BopType._CF_enumeration.addEnumeration(unicode_value='flexible joint', tag='flexible_joint')
BopType.connector = BopType._CF_enumeration.addEnumeration(unicode_value='connector', tag='connector')
BopType.unknown = BopType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BopType._InitializeFacetMap(BopType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BopType', BopType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BoxPinConfig
class BoxPinConfig (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of Box/Pin configuration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoxPinConfig')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 596, 1)
    _Documentation = 'These values represent the type of Box/Pin configuration.'
BoxPinConfig._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BoxPinConfig, enum_prefix=None)
BoxPinConfig.bottom_box_top_box = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value='bottom box, top box', tag='bottom_box_top_box')
BoxPinConfig.bottom_box_top_pin = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value='bottom box, top pin', tag='bottom_box_top_pin')
BoxPinConfig.bottom_pin_top_box = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value='bottom pin top box', tag='bottom_pin_top_box')
BoxPinConfig.bottom_pin = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value='bottom pin', tag='bottom_pin')
BoxPinConfig.unknown = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BoxPinConfig._InitializeFacetMap(BoxPinConfig._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BoxPinConfig', BoxPinConfig)

# Atomic simple type: {http://www.witsml.org/schemas/1series}CementJobType
class CementJobType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CementJobType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 631, 1)
    _Documentation = None
CementJobType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CementJobType, enum_prefix=None)
CementJobType.primary = CementJobType._CF_enumeration.addEnumeration(unicode_value='primary', tag='primary')
CementJobType.plug = CementJobType._CF_enumeration.addEnumeration(unicode_value='plug', tag='plug')
CementJobType.squeeze = CementJobType._CF_enumeration.addEnumeration(unicode_value='squeeze', tag='squeeze')
CementJobType.unknown = CementJobType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
CementJobType._InitializeFacetMap(CementJobType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CementJobType', CementJobType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ChangeInfoType
class ChangeInfoType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChangeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 658, 1)
    _Documentation = ''
ChangeInfoType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ChangeInfoType, enum_prefix=None)
ChangeInfoType.add = ChangeInfoType._CF_enumeration.addEnumeration(unicode_value='add', tag='add')
ChangeInfoType.update = ChangeInfoType._CF_enumeration.addEnumeration(unicode_value='update', tag='update')
ChangeInfoType.delete = ChangeInfoType._CF_enumeration.addEnumeration(unicode_value='delete', tag='delete')
ChangeInfoType._InitializeFacetMap(ChangeInfoType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ChangeInfoType', ChangeInfoType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ChronostratigraphyUnit
class ChronostratigraphyUnit (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Specifies the unit of chronostratigraphy."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChronostratigraphyUnit')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 681, 1)
    _Documentation = 'Specifies the unit of chronostratigraphy.'
ChronostratigraphyUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ChronostratigraphyUnit, enum_prefix=None)
ChronostratigraphyUnit.era = ChronostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value='era', tag='era')
ChronostratigraphyUnit.period = ChronostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value='period', tag='period')
ChronostratigraphyUnit.epoch = ChronostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value='epoch', tag='epoch')
ChronostratigraphyUnit.stage = ChronostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value='stage', tag='stage')
ChronostratigraphyUnit._InitializeFacetMap(ChronostratigraphyUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ChronostratigraphyUnit', ChronostratigraphyUnit)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ConnectionPosition
class ConnectionPosition (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the position of a connection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConnectionPosition')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 727, 1)
    _Documentation = 'These values represent the position of a connection.'
ConnectionPosition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ConnectionPosition, enum_prefix=None)
ConnectionPosition.both = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value='both', tag='both')
ConnectionPosition.bottom = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value='bottom', tag='bottom')
ConnectionPosition.top = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value='top', tag='top')
ConnectionPosition.unknown = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ConnectionPosition._InitializeFacetMap(ConnectionPosition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ConnectionPosition', ConnectionPosition)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DeflectionMethod
class DeflectionMethod (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent method used to direct the 
			deviation of the trajectory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeflectionMethod')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 757, 1)
    _Documentation = 'These values represent method used to direct the \n\t\t\tdeviation of the trajectory.'
DeflectionMethod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeflectionMethod, enum_prefix=None)
DeflectionMethod.point_bit = DeflectionMethod._CF_enumeration.addEnumeration(unicode_value='point bit', tag='point_bit')
DeflectionMethod.push_bit = DeflectionMethod._CF_enumeration.addEnumeration(unicode_value='push bit', tag='push_bit')
DeflectionMethod._InitializeFacetMap(DeflectionMethod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeflectionMethod', DeflectionMethod)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DerrickType
class DerrickType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drilling derrick."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DerrickType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 780, 1)
    _Documentation = 'These values represent the type of drilling derrick.'
DerrickType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DerrickType, enum_prefix=None)
DerrickType.double = DerrickType._CF_enumeration.addEnumeration(unicode_value='double', tag='double')
DerrickType.quadruple = DerrickType._CF_enumeration.addEnumeration(unicode_value='quadruple', tag='quadruple')
DerrickType.slant = DerrickType._CF_enumeration.addEnumeration(unicode_value='slant', tag='slant')
DerrickType.triple = DerrickType._CF_enumeration.addEnumeration(unicode_value='triple', tag='triple')
DerrickType.unknown = DerrickType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
DerrickType._InitializeFacetMap(DerrickType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DerrickType', DerrickType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DrawWorksType
class DrawWorksType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DrawWorksType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 815, 1)
    _Documentation = None
DrawWorksType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DrawWorksType, enum_prefix=None)
DrawWorksType.mechanical = DrawWorksType._CF_enumeration.addEnumeration(unicode_value='mechanical', tag='mechanical')
DrawWorksType.standard_electric = DrawWorksType._CF_enumeration.addEnumeration(unicode_value='standard electric', tag='standard_electric')
DrawWorksType.diesel_electric = DrawWorksType._CF_enumeration.addEnumeration(unicode_value='diesel electric', tag='diesel_electric')
DrawWorksType.ram_rig = DrawWorksType._CF_enumeration.addEnumeration(unicode_value='ram rig', tag='ram_rig')
DrawWorksType.unknown = DrawWorksType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
DrawWorksType._InitializeFacetMap(DrawWorksType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DrawWorksType', DrawWorksType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DriveType
class DriveType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of work string drive (rotary system)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DriveType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 847, 1)
    _Documentation = 'These values represent the type of work string drive (rotary system).'
DriveType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DriveType, enum_prefix=None)
DriveType.coiled_tubing = DriveType._CF_enumeration.addEnumeration(unicode_value='coiled tubing', tag='coiled_tubing')
DriveType.rotary_kelly_drive = DriveType._CF_enumeration.addEnumeration(unicode_value='rotary kelly drive', tag='rotary_kelly_drive')
DriveType.top_drive = DriveType._CF_enumeration.addEnumeration(unicode_value='top drive', tag='top_drive')
DriveType.unknown = DriveType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
DriveType._InitializeFacetMap(DriveType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DriveType', DriveType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}EastOrWest
class EastOrWest (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EastOrWest')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 877, 1)
    _Documentation = ''
EastOrWest._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EastOrWest, enum_prefix=None)
EastOrWest.east = EastOrWest._CF_enumeration.addEnumeration(unicode_value='east', tag='east')
EastOrWest.west = EastOrWest._CF_enumeration.addEnumeration(unicode_value='west', tag='west')
EastOrWest.unknown = EastOrWest._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
EastOrWest._InitializeFacetMap(EastOrWest._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EastOrWest', EastOrWest)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ElevCodeEnum
class ElevCodeEnum (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The type of local or permanent reference datum for vertical gravity based 
			(i.e., elevation and vertical depth) and measured depth coordinates within the context of a well.
			This list includes local points (e.g., kelly bushing) used as a datum and 
			vertical reference datums (e.g., mean sea level)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElevCodeEnum')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 902, 1)
    _Documentation = 'The type of local or permanent reference datum for vertical gravity based \n\t\t\t(i.e., elevation and vertical depth) and measured depth coordinates within the context of a well.\n\t\t\tThis list includes local points (e.g., kelly bushing) used as a datum and \n\t\t\tvertical reference datums (e.g., mean sea level).'
ElevCodeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ElevCodeEnum, enum_prefix=None)
ElevCodeEnum.CF = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='CF', tag='CF')
ElevCodeEnum.CV = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='CV', tag='CV')
ElevCodeEnum.DF = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='DF', tag='DF')
ElevCodeEnum.GL = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='GL', tag='GL')
ElevCodeEnum.KB = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='KB', tag='KB')
ElevCodeEnum.RB = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='RB', tag='RB')
ElevCodeEnum.RT = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='RT', tag='RT')
ElevCodeEnum.SF = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='SF', tag='SF')
ElevCodeEnum.LAT = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='LAT', tag='LAT')
ElevCodeEnum.SL = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='SL', tag='SL')
ElevCodeEnum.MHHW = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='MHHW', tag='MHHW')
ElevCodeEnum.MHW = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='MHW', tag='MHW')
ElevCodeEnum.MLLW = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='MLLW', tag='MLLW')
ElevCodeEnum.MLW = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='MLW', tag='MLW')
ElevCodeEnum.MTL = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='MTL', tag='MTL')
ElevCodeEnum.KO = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='KO', tag='KO')
ElevCodeEnum.unknown = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ElevCodeEnum._InitializeFacetMap(ElevCodeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ElevCodeEnum', ElevCodeEnum)

# Atomic simple type: {http://www.witsml.org/schemas/1series}Ellipsoid
class Ellipsoid (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of ellipsoid (spheroid) 
			defining geographic or planar coordinates. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ellipsoid')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1010, 1)
    _Documentation = 'These values represent the type of ellipsoid (spheroid) \n\t\t\tdefining geographic or planar coordinates. '
Ellipsoid._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Ellipsoid, enum_prefix=None)
Ellipsoid.AGD66 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='AGD66', tag='AGD66')
Ellipsoid.AIRY_MOD = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='AIRY_MOD', tag='AIRY_MOD')
Ellipsoid.AIRY30 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='AIRY30', tag='AIRY30')
Ellipsoid.AIRY49 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='AIRY49', tag='AIRY49')
Ellipsoid.AUST_NAT = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='AUST_NAT', tag='AUST_NAT')
Ellipsoid.BESL_DHD = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='BESL-DHD', tag='BESL_DHD')
Ellipsoid.BESL_NGL = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='BESL-NGL', tag='BESL_NGL')
Ellipsoid.BESL_RT9 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='BESL-RT9', tag='BESL_RT9')
Ellipsoid.BESS41 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='BESS41', tag='BESS41')
Ellipsoid.BESSNAM = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='BESSNAM', tag='BESSNAM')
Ellipsoid.BOGOTA = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='BOGOTA', tag='BOGOTA')
Ellipsoid.CL58 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL58', tag='CL58')
Ellipsoid.CL58_1 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL58-1', tag='CL58_1')
Ellipsoid.CL66 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL66', tag='CL66')
Ellipsoid.CL66_M = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL66-M', tag='CL66_M')
Ellipsoid.CL80 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL80', tag='CL80')
Ellipsoid.CL80_A = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL80-A', tag='CL80_A')
Ellipsoid.CL80_B = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL80-B', tag='CL80_B')
Ellipsoid.CL80_I = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL80-I', tag='CL80_I')
Ellipsoid.CL80_J = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL80-J', tag='CL80_J')
Ellipsoid.CL80_M = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL80-M', tag='CL80_M')
Ellipsoid.CL80_P = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CL80-P', tag='CL80_P')
Ellipsoid.CMPOINCH = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='CMPOINCH', tag='CMPOINCH')
Ellipsoid.DAN = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='DAN', tag='DAN')
Ellipsoid.DELA = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='DELA', tag='DELA')
Ellipsoid.ED50 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='ED50', tag='ED50')
Ellipsoid.EGYPT07 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='EGYPT07', tag='EGYPT07')
Ellipsoid.EVER = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='EVER', tag='EVER')
Ellipsoid.EVER48 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='EVER48', tag='EVER48')
Ellipsoid.EVER56 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='EVER56', tag='EVER56')
Ellipsoid.EVER69 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='EVER69', tag='EVER69')
Ellipsoid.EVER_BR = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='EVER-BR', tag='EVER_BR')
Ellipsoid.EVERMOD = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='EVERMOD', tag='EVERMOD')
Ellipsoid.EVER_P = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='EVER-P', tag='EVER_P')
Ellipsoid.EVER_TM = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='EVER-TM', tag='EVER_TM')
Ellipsoid.EVTM = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='EVTM', tag='EVTM')
Ellipsoid.FISC60 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='FISC60', tag='FISC60')
Ellipsoid.FISC60MOD = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='FISC60MOD', tag='FISC60MOD')
Ellipsoid.FISC68 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='FISC68', tag='FISC68')
Ellipsoid.FISCMOD = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='FISCMOD', tag='FISCMOD')
Ellipsoid.GDA94 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='GDA94', tag='GDA94')
Ellipsoid.GRS67 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='GRS67', tag='GRS67')
Ellipsoid.GRS80 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='GRS80', tag='GRS80')
Ellipsoid.HAY09 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='HAY09', tag='HAY09')
Ellipsoid.HEIS = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='HEIS', tag='HEIS')
Ellipsoid.HEL06 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='HEL06', tag='HEL06')
Ellipsoid.HEL07 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='HEL07', tag='HEL07')
Ellipsoid.HOUG = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='HOUG', tag='HOUG')
Ellipsoid.IAG_75 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='IAG-75', tag='IAG_75')
Ellipsoid.INDIAN75 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='INDIAN75', tag='INDIAN75')
Ellipsoid.INDO_74 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='INDO-74', tag='INDO_74')
Ellipsoid.INT24 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='INT24', tag='INT24')
Ellipsoid.IUGG67 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='IUGG67', tag='IUGG67')
Ellipsoid.IUGG75 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='IUGG75', tag='IUGG75')
Ellipsoid.JEFF48 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='JEFF48', tag='JEFF48')
Ellipsoid.KAU63 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='KAU63', tag='KAU63')
Ellipsoid.KRSV = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='KRSV', tag='KRSV')
Ellipsoid.MERIT83 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='MERIT83', tag='MERIT83')
Ellipsoid.NAD27 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='NAD27', tag='NAD27')
Ellipsoid.NAHRAN = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='NAHRAN', tag='NAHRAN')
Ellipsoid.NEWINT67 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='NEWINT67', tag='NEWINT67')
Ellipsoid.NWL_10D = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='NWL-10D', tag='NWL_10D')
Ellipsoid.NWL_9D = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='NWL-9D', tag='NWL_9D')
Ellipsoid.OSGB36 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='OSGB36', tag='OSGB36')
Ellipsoid.OSU86F = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='OSU86F', tag='OSU86F')
Ellipsoid.OSU91A = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='OSU91A', tag='OSU91A')
Ellipsoid.PLESSIS_1817 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='PLESSIS-1817', tag='PLESSIS_1817')
Ellipsoid.PSAD56 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='PSAD56', tag='PSAD56')
Ellipsoid.PTNOIRE = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='PTNOIRE', tag='PTNOIRE')
Ellipsoid.SA69 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='SA69', tag='SA69')
Ellipsoid.SPHR = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='SPHR', tag='SPHR')
Ellipsoid.STRU = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='STRU', tag='STRU')
Ellipsoid.WALB = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='WALB', tag='WALB')
Ellipsoid.WAR24 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='WAR24', tag='WAR24')
Ellipsoid.WGS60 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='WGS60', tag='WGS60')
Ellipsoid.WGS66 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='WGS66', tag='WGS66')
Ellipsoid.WGS72 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='WGS72', tag='WGS72')
Ellipsoid.WGS84 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='WGS84', tag='WGS84')
Ellipsoid.unknown = Ellipsoid._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
Ellipsoid._InitializeFacetMap(Ellipsoid._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Ellipsoid', Ellipsoid)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ErrorTermSource
class ErrorTermSource (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The codes for the various classes of error source."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErrorTermSource')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1416, 1)
    _Documentation = 'The codes for the various classes of error source.'
ErrorTermSource._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErrorTermSource, enum_prefix=None)
ErrorTermSource.sensor = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value='sensor', tag='sensor')
ErrorTermSource.azimuth_reference = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value='azimuth reference', tag='azimuth_reference')
ErrorTermSource.magnetic = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value='magnetic', tag='magnetic')
ErrorTermSource.alignment = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value='alignment', tag='alignment')
ErrorTermSource.misalignment = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value='misalignment', tag='misalignment')
ErrorTermSource.depth = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value='depth', tag='depth')
ErrorTermSource.reference = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value='reference', tag='reference')
ErrorTermSource.unknown = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ErrorTermSource._InitializeFacetMap(ErrorTermSource._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ErrorTermSource', ErrorTermSource)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ErrorPropagationMode
class ErrorPropagationMode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The codes for the various propagation modes."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErrorPropagationMode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1473, 1)
    _Documentation = 'The codes for the various propagation modes.'
ErrorPropagationMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErrorPropagationMode, enum_prefix=None)
ErrorPropagationMode.B = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
ErrorPropagationMode.R = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
ErrorPropagationMode.S = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
ErrorPropagationMode.W = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
ErrorPropagationMode.G = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value='G', tag='G')
ErrorPropagationMode.unknown = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ErrorPropagationMode._InitializeFacetMap(ErrorPropagationMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ErrorPropagationMode', ErrorPropagationMode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ErrorModelMisalignmentMode
class ErrorModelMisalignmentMode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The enums for the various misalignment maths."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErrorModelMisalignmentMode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1514, 1)
    _Documentation = 'The enums for the various misalignment maths.'
ErrorModelMisalignmentMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErrorModelMisalignmentMode, enum_prefix=None)
ErrorModelMisalignmentMode.n1 = ErrorModelMisalignmentMode._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
ErrorModelMisalignmentMode.n2 = ErrorModelMisalignmentMode._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
ErrorModelMisalignmentMode.n3 = ErrorModelMisalignmentMode._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
ErrorModelMisalignmentMode.unknown = ErrorModelMisalignmentMode._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ErrorModelMisalignmentMode._InitializeFacetMap(ErrorModelMisalignmentMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ErrorModelMisalignmentMode', ErrorModelMisalignmentMode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ExtensionName
class ExtensionName (abstractTypeEnum):

    """The name of a data extension.
			The list of standard values is contained in the WITSML enumValues.xml file."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionName')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1545, 1)
    _Documentation = 'The name of a data extension.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file.'
ExtensionName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ExtensionName', ExtensionName)

# Atomic simple type: {http://www.witsml.org/schemas/1series}GasPeakType
class GasPeakType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GasPeakType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1554, 1)
    _Documentation = None
GasPeakType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=GasPeakType, enum_prefix=None)
GasPeakType.circulating_background_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value='circulating background gas', tag='circulating_background_gas')
GasPeakType.connection_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value='connection gas', tag='connection_gas')
GasPeakType.drilling_background_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value='drilling background gas', tag='drilling_background_gas')
GasPeakType.drilling_gas_peak = GasPeakType._CF_enumeration.addEnumeration(unicode_value='drilling gas peak', tag='drilling_gas_peak')
GasPeakType.flow_check_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value='flow check gas', tag='flow_check_gas')
GasPeakType.no_readings = GasPeakType._CF_enumeration.addEnumeration(unicode_value='no readings', tag='no_readings')
GasPeakType.other = GasPeakType._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
GasPeakType.shut_down_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value='shut down gas', tag='shut_down_gas')
GasPeakType.trip_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value='trip gas', tag='trip_gas')
GasPeakType.unknown = GasPeakType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
GasPeakType._InitializeFacetMap(GasPeakType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'GasPeakType', GasPeakType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}GeodeticDatum
class GeodeticDatum (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of geodetic datum. 
			The source (except for "none", "unknown" and "UserDefined") of the values 
			and the descriptions is Geoshare V13."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeodeticDatum')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1611, 1)
    _Documentation = 'These values represent the type of geodetic datum. \n\t\t\tThe source (except for "none", "unknown" and "UserDefined") of the values \n\t\t\tand the descriptions is Geoshare V13.'
GeodeticDatum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=GeodeticDatum, enum_prefix=None)
GeodeticDatum.ADND = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='ADND', tag='ADND')
GeodeticDatum.ARC50 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='ARC50', tag='ARC50')
GeodeticDatum.AUSG = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='AUSG', tag='AUSG')
GeodeticDatum.CAA = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='CAA', tag='CAA')
GeodeticDatum.CHAS = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='CHAS', tag='CHAS')
GeodeticDatum.CORAL = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='CORAL', tag='CORAL')
GeodeticDatum.ED50 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='ED50', tag='ED50')
GeodeticDatum.ED87 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='ED87', tag='ED87')
GeodeticDatum.ERIN65 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='ERIN65', tag='ERIN65')
GeodeticDatum.GD49 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='GD49', tag='GD49')
GeodeticDatum.GHANA = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='GHANA', tag='GHANA')
GeodeticDatum.GUAM63 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='GUAM63', tag='GUAM63')
GeodeticDatum.HJRS55 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='HJRS55', tag='HJRS55')
GeodeticDatum.HTS = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='HTS', tag='HTS')
GeodeticDatum.INCH = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='INCH', tag='INCH')
GeodeticDatum.INDIA1 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='INDIA1', tag='INDIA1')
GeodeticDatum.INDIA2 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='INDIA2', tag='INDIA2')
GeodeticDatum.INDNS74 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='INDNS74', tag='INDNS74')
GeodeticDatum.LIB64 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='LIB64', tag='LIB64')
GeodeticDatum.LUZON = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='LUZON', tag='LUZON')
GeodeticDatum.MRCH = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='MRCH', tag='MRCH')
GeodeticDatum.NAD27 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='NAD27', tag='NAD27')
GeodeticDatum.NAD83 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='NAD83', tag='NAD83')
GeodeticDatum.NGRA = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='NGRA', tag='NGRA')
GeodeticDatum.None_ = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
GeodeticDatum.NPRM = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='NPRM', tag='NPRM')
GeodeticDatum.OSGB36 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='OSGB36', tag='OSGB36')
GeodeticDatum.POTS1 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='POTS1', tag='POTS1')
GeodeticDatum.PULK1 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='PULK1', tag='PULK1')
GeodeticDatum.PULK2 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='PULK2', tag='PULK2')
GeodeticDatum.QRNQ = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='QRNQ', tag='QRNQ')
GeodeticDatum.SA56 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='SA56', tag='SA56')
GeodeticDatum.SRL60 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='SRL60', tag='SRL60')
GeodeticDatum.TNRV25 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='TNRV25', tag='TNRV25')
GeodeticDatum.TOKYO = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='TOKYO', tag='TOKYO')
GeodeticDatum.UserDefined = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
GeodeticDatum.VROL = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='VROL', tag='VROL')
GeodeticDatum.WGS72 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='WGS72', tag='WGS72')
GeodeticDatum.WGS84 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='WGS84', tag='WGS84')
GeodeticDatum.YACR = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='YACR', tag='YACR')
GeodeticDatum.unknown = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
GeodeticDatum._InitializeFacetMap(GeodeticDatum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'GeodeticDatum', GeodeticDatum)

# Atomic simple type: {http://www.witsml.org/schemas/1series}Hemispheres
class Hemispheres (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Hemispheres')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1828, 1)
    _Documentation = None
Hemispheres._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Hemispheres, enum_prefix=None)
Hemispheres.northern = Hemispheres._CF_enumeration.addEnumeration(unicode_value='northern', tag='northern')
Hemispheres.southern = Hemispheres._CF_enumeration.addEnumeration(unicode_value='southern', tag='southern')
Hemispheres.unknown = Hemispheres._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
Hemispheres._InitializeFacetMap(Hemispheres._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Hemispheres', Hemispheres)

# Atomic simple type: {http://www.witsml.org/schemas/1series}HoleCasingType
class HoleCasingType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HoleCasingType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1850, 1)
    _Documentation = None
HoleCasingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HoleCasingType, enum_prefix=None)
HoleCasingType.blow_out_preventer = HoleCasingType._CF_enumeration.addEnumeration(unicode_value='blow out preventer', tag='blow_out_preventer')
HoleCasingType.casing = HoleCasingType._CF_enumeration.addEnumeration(unicode_value='casing', tag='casing')
HoleCasingType.conductor = HoleCasingType._CF_enumeration.addEnumeration(unicode_value='conductor', tag='conductor')
HoleCasingType.curved_conductor = HoleCasingType._CF_enumeration.addEnumeration(unicode_value='curved conductor', tag='curved_conductor')
HoleCasingType.liner = HoleCasingType._CF_enumeration.addEnumeration(unicode_value='liner', tag='liner')
HoleCasingType.open_hole = HoleCasingType._CF_enumeration.addEnumeration(unicode_value='open hole', tag='open_hole')
HoleCasingType.riser = HoleCasingType._CF_enumeration.addEnumeration(unicode_value='riser', tag='riser')
HoleCasingType.tubing = HoleCasingType._CF_enumeration.addEnumeration(unicode_value='tubing', tag='tubing')
HoleCasingType.unknown = HoleCasingType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
HoleCasingType._InitializeFacetMap(HoleCasingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HoleCasingType', HoleCasingType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}HoleOpenerType
class HoleOpenerType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HoleOpenerType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1902, 1)
    _Documentation = None
HoleOpenerType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HoleOpenerType, enum_prefix=None)
HoleOpenerType.under_reamer = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value='under-reamer', tag='under_reamer')
HoleOpenerType.fixed_blade = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value='fixed blade', tag='fixed_blade')
HoleOpenerType.unknown = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
HoleOpenerType._InitializeFacetMap(HoleOpenerType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HoleOpenerType', HoleOpenerType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}InnerBarrelType
class InnerBarrelType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InnerBarrelType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1924, 1)
    _Documentation = ''
InnerBarrelType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InnerBarrelType, enum_prefix=None)
InnerBarrelType.undifferented = InnerBarrelType._CF_enumeration.addEnumeration(unicode_value='undifferented', tag='undifferented')
InnerBarrelType.aluminum = InnerBarrelType._CF_enumeration.addEnumeration(unicode_value='aluminum', tag='aluminum')
InnerBarrelType.gel = InnerBarrelType._CF_enumeration.addEnumeration(unicode_value='gel', tag='gel')
InnerBarrelType.fiberglass = InnerBarrelType._CF_enumeration.addEnumeration(unicode_value='fiberglass', tag='fiberglass')
InnerBarrelType.unknown = InnerBarrelType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
InnerBarrelType._InitializeFacetMap(InnerBarrelType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InnerBarrelType', InnerBarrelType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ItemState
class ItemState (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the state of a WITSML object. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ItemState')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1960, 1)
    _Documentation = 'These values represent the state of a WITSML object. '
ItemState._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ItemState, enum_prefix=None)
ItemState.actual = ItemState._CF_enumeration.addEnumeration(unicode_value='actual', tag='actual')
ItemState.model = ItemState._CF_enumeration.addEnumeration(unicode_value='model', tag='model')
ItemState.plan = ItemState._CF_enumeration.addEnumeration(unicode_value='plan', tag='plan')
ItemState.unknown = ItemState._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ItemState._InitializeFacetMap(ItemState._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ItemState', ItemState)

# Atomic simple type: {http://www.witsml.org/schemas/1series}JarType
class JarType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JarType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1990, 1)
    _Documentation = None
JarType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=JarType, enum_prefix=None)
JarType.mechanical = JarType._CF_enumeration.addEnumeration(unicode_value='mechanical', tag='mechanical')
JarType.hydraulic = JarType._CF_enumeration.addEnumeration(unicode_value='hydraulic', tag='hydraulic')
JarType.hydro_mechanical = JarType._CF_enumeration.addEnumeration(unicode_value='hydro mechanical', tag='hydro_mechanical')
JarType.unknown = JarType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
JarType._InitializeFacetMap(JarType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'JarType', JarType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}JarAction
class JarAction (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JarAction')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2017, 1)
    _Documentation = None
JarAction._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=JarAction, enum_prefix=None)
JarAction.up = JarAction._CF_enumeration.addEnumeration(unicode_value='up', tag='up')
JarAction.down = JarAction._CF_enumeration.addEnumeration(unicode_value='down', tag='down')
JarAction.both = JarAction._CF_enumeration.addEnumeration(unicode_value='both', tag='both')
JarAction.vibrating = JarAction._CF_enumeration.addEnumeration(unicode_value='vibrating', tag='vibrating')
JarAction.unknown = JarAction._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
JarAction._InitializeFacetMap(JarAction._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'JarAction', JarAction)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LithologySource
class LithologySource (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Specifies the source of lithology information."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LithologySource')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2049, 1)
    _Documentation = 'Specifies the source of lithology information.'
LithologySource._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LithologySource, enum_prefix=None)
LithologySource.interpreted = LithologySource._CF_enumeration.addEnumeration(unicode_value='interpreted', tag='interpreted')
LithologySource.core = LithologySource._CF_enumeration.addEnumeration(unicode_value='core', tag='core')
LithologySource.cuttings = LithologySource._CF_enumeration.addEnumeration(unicode_value='cuttings', tag='cuttings')
LithologySource.unknown = LithologySource._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
LithologySource._InitializeFacetMap(LithologySource._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LithologySource', LithologySource)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LithologyType
class LithologyType (abstractTypeEnum):

    """The type of lithology.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LithologyType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2082, 1)
    _Documentation = 'The type of lithology.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
LithologyType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'LithologyType', LithologyType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LithostratigraphyUnit
class LithostratigraphyUnit (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Specifies the unit of lithostratigraphy."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LithostratigraphyUnit')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2091, 1)
    _Documentation = 'Specifies the unit of lithostratigraphy.'
LithostratigraphyUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LithostratigraphyUnit, enum_prefix=None)
LithostratigraphyUnit.group = LithostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value='group', tag='group')
LithostratigraphyUnit.formation = LithostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value='formation', tag='formation')
LithostratigraphyUnit.member = LithostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value='member', tag='member')
LithostratigraphyUnit.bed = LithostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value='bed', tag='bed')
LithostratigraphyUnit._InitializeFacetMap(LithostratigraphyUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LithostratigraphyUnit', LithostratigraphyUnit)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LogDataType
class LogDataType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The endcoding allowed in a log curve value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogDataType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2146, 1)
    _Documentation = 'The endcoding allowed in a log curve value.'
LogDataType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogDataType, enum_prefix=None)
LogDataType.byte = LogDataType._CF_enumeration.addEnumeration(unicode_value='byte', tag='byte')
LogDataType.date_time = LogDataType._CF_enumeration.addEnumeration(unicode_value='date time', tag='date_time')
LogDataType.double = LogDataType._CF_enumeration.addEnumeration(unicode_value='double', tag='double')
LogDataType.float = LogDataType._CF_enumeration.addEnumeration(unicode_value='float', tag='float')
LogDataType.int = LogDataType._CF_enumeration.addEnumeration(unicode_value='int', tag='int')
LogDataType.long = LogDataType._CF_enumeration.addEnumeration(unicode_value='long', tag='long')
LogDataType.short = LogDataType._CF_enumeration.addEnumeration(unicode_value='short', tag='short')
LogDataType.string = LogDataType._CF_enumeration.addEnumeration(unicode_value='string', tag='string')
LogDataType.string40 = LogDataType._CF_enumeration.addEnumeration(unicode_value='string40', tag='string40')
LogDataType.string16 = LogDataType._CF_enumeration.addEnumeration(unicode_value='string16', tag='string16')
LogDataType.unknown = LogDataType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
LogDataType._InitializeFacetMap(LogDataType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogDataType', LogDataType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LogIndexDirection
class LogIndexDirection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the direction of movement within a wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogIndexDirection')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2229, 1)
    _Documentation = 'These values represent the direction of movement within a wellbore.'
LogIndexDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogIndexDirection, enum_prefix=None)
LogIndexDirection.decreasing = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value='decreasing', tag='decreasing')
LogIndexDirection.increasing = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value='increasing', tag='increasing')
LogIndexDirection.unknown = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
LogIndexDirection._InitializeFacetMap(LogIndexDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogIndexDirection', LogIndexDirection)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LogIndexType
class LogIndexType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of data used as an index value for a log. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogIndexType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2256, 1)
    _Documentation = 'These values represent the type of data used as an index value for a log. '
LogIndexType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogIndexType, enum_prefix=None)
LogIndexType.date_time = LogIndexType._CF_enumeration.addEnumeration(unicode_value='date time', tag='date_time')
LogIndexType.elapsed_time = LogIndexType._CF_enumeration.addEnumeration(unicode_value='elapsed time', tag='elapsed_time')
LogIndexType.length = LogIndexType._CF_enumeration.addEnumeration(unicode_value='length', tag='length')
LogIndexType.measured_depth = LogIndexType._CF_enumeration.addEnumeration(unicode_value='measured depth', tag='measured_depth')
LogIndexType.vertical_depth = LogIndexType._CF_enumeration.addEnumeration(unicode_value='vertical depth', tag='vertical_depth')
LogIndexType.other = LogIndexType._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
LogIndexType.unknown = LogIndexType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
LogIndexType._InitializeFacetMap(LogIndexType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogIndexType', LogIndexType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LogTraceOrigin
class LogTraceOrigin (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogTraceOrigin')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2301, 1)
    _Documentation = None
LogTraceOrigin._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogTraceOrigin, enum_prefix=None)
LogTraceOrigin.realtime = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value='realtime', tag='realtime')
LogTraceOrigin.modeled = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value='modeled', tag='modeled')
LogTraceOrigin.unknown = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
LogTraceOrigin._InitializeFacetMap(LogTraceOrigin._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogTraceOrigin', LogTraceOrigin)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LogTraceState
class LogTraceState (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogTraceState')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2323, 1)
    _Documentation = None
LogTraceState._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogTraceState, enum_prefix=None)
LogTraceState.depth_adjusted = LogTraceState._CF_enumeration.addEnumeration(unicode_value='depth adjusted', tag='depth_adjusted')
LogTraceState.edited = LogTraceState._CF_enumeration.addEnumeration(unicode_value='edited', tag='edited')
LogTraceState.joined = LogTraceState._CF_enumeration.addEnumeration(unicode_value='joined', tag='joined')
LogTraceState.processed = LogTraceState._CF_enumeration.addEnumeration(unicode_value='processed', tag='processed')
LogTraceState.raw = LogTraceState._CF_enumeration.addEnumeration(unicode_value='raw', tag='raw')
LogTraceState.unknown = LogTraceState._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
LogTraceState._InitializeFacetMap(LogTraceState._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogTraceState', LogTraceState)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MaterialType
class MaterialType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2360, 1)
    _Documentation = None
MaterialType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MaterialType, enum_prefix=None)
MaterialType.aluminum = MaterialType._CF_enumeration.addEnumeration(unicode_value='aluminum', tag='aluminum')
MaterialType.beryllium_copper = MaterialType._CF_enumeration.addEnumeration(unicode_value='beryllium copper', tag='beryllium_copper')
MaterialType.chrome_alloy = MaterialType._CF_enumeration.addEnumeration(unicode_value='chrome alloy', tag='chrome_alloy')
MaterialType.composite = MaterialType._CF_enumeration.addEnumeration(unicode_value='composite', tag='composite')
MaterialType.other = MaterialType._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
MaterialType.non_magnetic_steel = MaterialType._CF_enumeration.addEnumeration(unicode_value='non-magnetic steel', tag='non_magnetic_steel')
MaterialType.plastic = MaterialType._CF_enumeration.addEnumeration(unicode_value='plastic', tag='plastic')
MaterialType.steel = MaterialType._CF_enumeration.addEnumeration(unicode_value='steel', tag='steel')
MaterialType.steel_alloy = MaterialType._CF_enumeration.addEnumeration(unicode_value='steel alloy', tag='steel_alloy')
MaterialType.titanium = MaterialType._CF_enumeration.addEnumeration(unicode_value='titanium', tag='titanium')
MaterialType.unknown = MaterialType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
MaterialType._InitializeFacetMap(MaterialType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MaterialType', MaterialType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MatrixCementType
class MatrixCementType (abstractTypeEnum):

    """Lithology matrix/cement description.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MatrixCementType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2422, 1)
    _Documentation = 'Lithology matrix/cement description.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
MatrixCementType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'MatrixCementType', MatrixCementType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MeasureClass
class MeasureClass (abstractTypeEnum):

    """Measure class values.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasureClass')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2432, 1)
    _Documentation = 'Measure class values.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
MeasureClass._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'MeasureClass', MeasureClass)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MeasurementType
class MeasurementType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The source (except for "CH density porosity", "CH neutron porosity", "OH density porosity"
			and "OH neutron porosity") of the values and the descriptions is the POSC V2.2 "well log trace class" 
			standard instance values which are documented as "A classification of well log traces based on 
			specification of a range of characteristics. Traces may be classed according to the type of physical 
			characteristic they are meant to measure." """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasurementType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2442, 1)
    _Documentation = 'The source (except for "CH density porosity", "CH neutron porosity", "OH density porosity"\n\t\t\tand "OH neutron porosity") of the values and the descriptions is the POSC V2.2 "well log trace class" \n\t\t\tstandard instance values which are documented as "A classification of well log traces based on \n\t\t\tspecification of a range of characteristics. Traces may be classed according to the type of physical \n\t\t\tcharacteristic they are meant to measure."'
MeasurementType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MeasurementType, enum_prefix=None)
MeasurementType.acceleration = MeasurementType._CF_enumeration.addEnumeration(unicode_value='acceleration', tag='acceleration')
MeasurementType.acoustic_caliper = MeasurementType._CF_enumeration.addEnumeration(unicode_value='acoustic caliper', tag='acoustic_caliper')
MeasurementType.acoustic_casing_collar_locator = MeasurementType._CF_enumeration.addEnumeration(unicode_value='acoustic casing collar locator', tag='acoustic_casing_collar_locator')
MeasurementType.acoustic_impedance = MeasurementType._CF_enumeration.addEnumeration(unicode_value='acoustic impedance', tag='acoustic_impedance')
MeasurementType.acoustic_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='acoustic porosity', tag='acoustic_porosity')
MeasurementType.acoustic_velocity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='acoustic velocity', tag='acoustic_velocity')
MeasurementType.acoustic_wave_matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='acoustic wave matrix travel time', tag='acoustic_wave_matrix_travel_time')
MeasurementType.acoustic_wave_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='acoustic wave travel time', tag='acoustic_wave_travel_time')
MeasurementType.amplitude = MeasurementType._CF_enumeration.addEnumeration(unicode_value='amplitude', tag='amplitude')
MeasurementType.amplitude_of_acoustic_wave = MeasurementType._CF_enumeration.addEnumeration(unicode_value='amplitude of acoustic wave', tag='amplitude_of_acoustic_wave')
MeasurementType.amplitude_of_E_M_wave = MeasurementType._CF_enumeration.addEnumeration(unicode_value='amplitude of E-M wave', tag='amplitude_of_E_M_wave')
MeasurementType.amplitude_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value='amplitude ratio', tag='amplitude_ratio')
MeasurementType.area = MeasurementType._CF_enumeration.addEnumeration(unicode_value='area', tag='area')
MeasurementType.attenuation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='attenuation', tag='attenuation')
MeasurementType.attenuation_of_acoustic_wave = MeasurementType._CF_enumeration.addEnumeration(unicode_value='attenuation of acoustic wave', tag='attenuation_of_acoustic_wave')
MeasurementType.attenuation_of_E_M_wave = MeasurementType._CF_enumeration.addEnumeration(unicode_value='attenuation of E-M wave', tag='attenuation_of_E_M_wave')
MeasurementType.auxiliary = MeasurementType._CF_enumeration.addEnumeration(unicode_value='auxiliary', tag='auxiliary')
MeasurementType.average_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='average porosity', tag='average_porosity')
MeasurementType.azimuth = MeasurementType._CF_enumeration.addEnumeration(unicode_value='azimuth', tag='azimuth')
MeasurementType.barite_mud_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='barite mud correction', tag='barite_mud_correction')
MeasurementType.bed_thickness_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='bed thickness correction', tag='bed_thickness_correction')
MeasurementType.bit_size = MeasurementType._CF_enumeration.addEnumeration(unicode_value='bit size', tag='bit_size')
MeasurementType.blocked = MeasurementType._CF_enumeration.addEnumeration(unicode_value='blocked', tag='blocked')
MeasurementType.borehole_environment_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='borehole environment correction', tag='borehole_environment_correction')
MeasurementType.borehole_fluid_composition_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='borehole fluid composition correction', tag='borehole_fluid_composition_correction')
MeasurementType.borehole_fluid_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='borehole fluid correction', tag='borehole_fluid_correction')
MeasurementType.borehole_size_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='borehole size correction', tag='borehole_size_correction')
MeasurementType.bromide_mud_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='bromide mud correction', tag='bromide_mud_correction')
MeasurementType.bulk_compressibility = MeasurementType._CF_enumeration.addEnumeration(unicode_value='bulk compressibility', tag='bulk_compressibility')
MeasurementType.bulk_density = MeasurementType._CF_enumeration.addEnumeration(unicode_value='bulk density', tag='bulk_density')
MeasurementType.bulk_volume = MeasurementType._CF_enumeration.addEnumeration(unicode_value='bulk volume', tag='bulk_volume')
MeasurementType.bulk_volume_gas = MeasurementType._CF_enumeration.addEnumeration(unicode_value='bulk volume gas', tag='bulk_volume_gas')
MeasurementType.bulk_volume_hydrocarbon = MeasurementType._CF_enumeration.addEnumeration(unicode_value='bulk volume hydrocarbon', tag='bulk_volume_hydrocarbon')
MeasurementType.bulk_volume_oil = MeasurementType._CF_enumeration.addEnumeration(unicode_value='bulk volume oil', tag='bulk_volume_oil')
MeasurementType.bulk_volume_water = MeasurementType._CF_enumeration.addEnumeration(unicode_value='bulk volume water', tag='bulk_volume_water')
MeasurementType.CO_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value='C/O ratio', tag='CO_ratio')
MeasurementType.caliper = MeasurementType._CF_enumeration.addEnumeration(unicode_value='caliper', tag='caliper')
MeasurementType.cased_hole_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='cased hole correction', tag='cased_hole_correction')
MeasurementType.casing_collar_locator = MeasurementType._CF_enumeration.addEnumeration(unicode_value='casing collar locator', tag='casing_collar_locator')
MeasurementType.casing_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='casing correction', tag='casing_correction')
MeasurementType.casing_diameter_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='casing diameter correction', tag='casing_diameter_correction')
MeasurementType.casing_inspection = MeasurementType._CF_enumeration.addEnumeration(unicode_value='casing inspection', tag='casing_inspection')
MeasurementType.casing_thickness_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='casing thickness correction', tag='casing_thickness_correction')
MeasurementType.casing_weight_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='casing weight correction', tag='casing_weight_correction')
MeasurementType.cement_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='cement correction', tag='cement_correction')
MeasurementType.cement_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='cement density correction', tag='cement_density_correction')
MeasurementType.cement_evaluation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='cement evaluation', tag='cement_evaluation')
MeasurementType.cement_thickness_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='cement thickness correction', tag='cement_thickness_correction')
MeasurementType.cement_type_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='cement type correction', tag='cement_type_correction')
MeasurementType.CH_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='CH density porosity', tag='CH_density_porosity')
MeasurementType.CH_dolomite_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='CH dolomite density porosity', tag='CH_dolomite_density_porosity')
MeasurementType.CH_dolomite_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='CH dolomite neutron porosity', tag='CH_dolomite_neutron_porosity')
MeasurementType.CH_limestone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='CH limestone density porosity', tag='CH_limestone_density_porosity')
MeasurementType.CH_limestone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='CH limestone neutron porosity', tag='CH_limestone_neutron_porosity')
MeasurementType.CH_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='CH neutron porosity', tag='CH_neutron_porosity')
MeasurementType.CH_sandstone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='CH sandstone density porosity', tag='CH_sandstone_density_porosity')
MeasurementType.CH_sandstone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='CH sandstone neutron porosity', tag='CH_sandstone_neutron_porosity')
MeasurementType.compressional_wave_dolomite_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='compressional wave dolomite porosity', tag='compressional_wave_dolomite_porosity')
MeasurementType.compressional_wave_limestone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='compressional wave limestone porosity', tag='compressional_wave_limestone_porosity')
MeasurementType.compressional_wave_matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='compressional wave matrix travel time', tag='compressional_wave_matrix_travel_time')
MeasurementType.compressional_wave_sandstone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='compressional wave sandstone porosity', tag='compressional_wave_sandstone_porosity')
MeasurementType.compressional_wave_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='compressional wave travel time', tag='compressional_wave_travel_time')
MeasurementType.conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='conductivity', tag='conductivity')
MeasurementType.conductivity_from_attenuation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='conductivity from attenuation', tag='conductivity_from_attenuation')
MeasurementType.conductivity_from_phase_shift = MeasurementType._CF_enumeration.addEnumeration(unicode_value='conductivity from phase shift', tag='conductivity_from_phase_shift')
MeasurementType.connate_water_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='connate water conductivity', tag='connate_water_conductivity')
MeasurementType.connate_water_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='connate water resistivity', tag='connate_water_resistivity')
MeasurementType.conventional_core_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='conventional core porosity', tag='conventional_core_porosity')
MeasurementType.core_matrix_density = MeasurementType._CF_enumeration.addEnumeration(unicode_value='core matrix density', tag='core_matrix_density')
MeasurementType.core_permeability = MeasurementType._CF_enumeration.addEnumeration(unicode_value='core permeability', tag='core_permeability')
MeasurementType.core_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='core porosity', tag='core_porosity')
MeasurementType.corrected = MeasurementType._CF_enumeration.addEnumeration(unicode_value='corrected', tag='corrected')
MeasurementType.count_rate = MeasurementType._CF_enumeration.addEnumeration(unicode_value='count rate', tag='count_rate')
MeasurementType.count_rate_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value='count rate ratio', tag='count_rate_ratio')
MeasurementType.cross_plot_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='cross plot porosity', tag='cross_plot_porosity')
MeasurementType.decay_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='decay time', tag='decay_time')
MeasurementType.deep_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='deep conductivity', tag='deep_conductivity')
MeasurementType.deep_induction_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='deep induction conductivity', tag='deep_induction_conductivity')
MeasurementType.deep_induction_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='deep induction resistivity', tag='deep_induction_resistivity')
MeasurementType.deep_laterolog_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='deep laterolog conductivity', tag='deep_laterolog_conductivity')
MeasurementType.deep_laterolog_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='deep laterolog resistivity', tag='deep_laterolog_resistivity')
MeasurementType.deep_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='deep resistivity', tag='deep_resistivity')
MeasurementType.density = MeasurementType._CF_enumeration.addEnumeration(unicode_value='density', tag='density')
MeasurementType.density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='density porosity', tag='density_porosity')
MeasurementType.depth = MeasurementType._CF_enumeration.addEnumeration(unicode_value='depth', tag='depth')
MeasurementType.depth_adjusted = MeasurementType._CF_enumeration.addEnumeration(unicode_value='depth adjusted', tag='depth_adjusted')
MeasurementType.depth_derived_from_velocity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='depth derived from velocity', tag='depth_derived_from_velocity')
MeasurementType.deviation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='deviation', tag='deviation')
MeasurementType.dielectric = MeasurementType._CF_enumeration.addEnumeration(unicode_value='dielectric', tag='dielectric')
MeasurementType.diffusion_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='diffusion correction', tag='diffusion_correction')
MeasurementType.dip = MeasurementType._CF_enumeration.addEnumeration(unicode_value='dip', tag='dip')
MeasurementType.dipmeter = MeasurementType._CF_enumeration.addEnumeration(unicode_value='dipmeter', tag='dipmeter')
MeasurementType.dipmeter_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='dipmeter conductivity', tag='dipmeter_conductivity')
MeasurementType.dipmeter_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='dipmeter resistivity', tag='dipmeter_resistivity')
MeasurementType.dolomite_acoustic_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='dolomite acoustic porosity', tag='dolomite_acoustic_porosity')
MeasurementType.dolomite_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='dolomite density porosity', tag='dolomite_density_porosity')
MeasurementType.dolomite_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='dolomite neutron porosity', tag='dolomite_neutron_porosity')
MeasurementType.edited = MeasurementType._CF_enumeration.addEnumeration(unicode_value='edited', tag='edited')
MeasurementType.effective_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='effective porosity', tag='effective_porosity')
MeasurementType.electric_current = MeasurementType._CF_enumeration.addEnumeration(unicode_value='electric current', tag='electric_current')
MeasurementType.electric_potential = MeasurementType._CF_enumeration.addEnumeration(unicode_value='electric potential', tag='electric_potential')
MeasurementType.electromagnetic_wave_matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='electromagnetic wave matrix travel time', tag='electromagnetic_wave_matrix_travel_time')
MeasurementType.electromagnetic_wave_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='electromagnetic wave travel time', tag='electromagnetic_wave_travel_time')
MeasurementType.element = MeasurementType._CF_enumeration.addEnumeration(unicode_value='element', tag='element')
MeasurementType.elemental_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value='elemental ratio', tag='elemental_ratio')
MeasurementType.enhanced = MeasurementType._CF_enumeration.addEnumeration(unicode_value='enhanced', tag='enhanced')
MeasurementType.filtered = MeasurementType._CF_enumeration.addEnumeration(unicode_value='filtered', tag='filtered')
MeasurementType.flowmeter = MeasurementType._CF_enumeration.addEnumeration(unicode_value='flowmeter', tag='flowmeter')
MeasurementType.fluid_density = MeasurementType._CF_enumeration.addEnumeration(unicode_value='fluid density', tag='fluid_density')
MeasurementType.fluid_velocity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='fluid velocity', tag='fluid_velocity')
MeasurementType.fluid_viscosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='fluid viscosity', tag='fluid_viscosity')
MeasurementType.flushed_zone_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='flushed zone conductivity', tag='flushed_zone_conductivity')
MeasurementType.flushed_zone_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='flushed zone resistivity', tag='flushed_zone_resistivity')
MeasurementType.flushed_zone_saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='flushed zone saturation', tag='flushed_zone_saturation')
MeasurementType.force = MeasurementType._CF_enumeration.addEnumeration(unicode_value='force', tag='force')
MeasurementType.formation_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='formation density correction', tag='formation_density_correction')
MeasurementType.formation_properties_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='formation properties correction', tag='formation_properties_correction')
MeasurementType.formation_salinity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='formation salinity correction', tag='formation_salinity_correction')
MeasurementType.formation_saturation_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='formation saturation correction', tag='formation_saturation_correction')
MeasurementType.formation_volume_factor_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='formation volume factor correction', tag='formation_volume_factor_correction')
MeasurementType.formation_water_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='formation water density correction', tag='formation_water_density_correction')
MeasurementType.formation_water_saturation_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='formation water saturation correction', tag='formation_water_saturation_correction')
MeasurementType.free_fluid_index = MeasurementType._CF_enumeration.addEnumeration(unicode_value='free fluid index', tag='free_fluid_index')
MeasurementType.friction_effect_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='friction effect correction', tag='friction_effect_correction')
MeasurementType.gamma_ray = MeasurementType._CF_enumeration.addEnumeration(unicode_value='gamma ray', tag='gamma_ray')
MeasurementType.gamma_ray_minus_uranium = MeasurementType._CF_enumeration.addEnumeration(unicode_value='gamma ray minus uranium', tag='gamma_ray_minus_uranium')
MeasurementType.gas_saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='gas saturation', tag='gas_saturation')
MeasurementType.gradiomanometer = MeasurementType._CF_enumeration.addEnumeration(unicode_value='gradiomanometer', tag='gradiomanometer')
MeasurementType.high_frequency_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='high frequency conductivity', tag='high_frequency_conductivity')
MeasurementType.high_frequency_electromagnetic = MeasurementType._CF_enumeration.addEnumeration(unicode_value='high frequency electromagnetic', tag='high_frequency_electromagnetic')
MeasurementType.high_frequency_electromagnetic_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='high frequency electromagnetic porosity', tag='high_frequency_electromagnetic_porosity')
MeasurementType.high_frequency_E_M_phase_shift = MeasurementType._CF_enumeration.addEnumeration(unicode_value='high frequency E-M phase shift', tag='high_frequency_E_M_phase_shift')
MeasurementType.high_frequency_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='high frequency resistivity', tag='high_frequency_resistivity')
MeasurementType.hydrocarbon_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='hydrocarbon correction', tag='hydrocarbon_correction')
MeasurementType.hydrocarbon_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='hydrocarbon density correction', tag='hydrocarbon_density_correction')
MeasurementType.hydrocarbon_gravity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='hydrocarbon gravity correction', tag='hydrocarbon_gravity_correction')
MeasurementType.hydrocarbon_saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='hydrocarbon saturation', tag='hydrocarbon_saturation')
MeasurementType.hydrocarbon_viscosity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='hydrocarbon viscosity correction', tag='hydrocarbon_viscosity_correction')
MeasurementType.image = MeasurementType._CF_enumeration.addEnumeration(unicode_value='image', tag='image')
MeasurementType.interpretation_variable = MeasurementType._CF_enumeration.addEnumeration(unicode_value='interpretation variable', tag='interpretation_variable')
MeasurementType.iron_mud_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='iron mud correction', tag='iron_mud_correction')
MeasurementType.joined = MeasurementType._CF_enumeration.addEnumeration(unicode_value='joined', tag='joined')
MeasurementType.KCl_mud_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='KCl mud correction', tag='KCl_mud_correction')
MeasurementType.length = MeasurementType._CF_enumeration.addEnumeration(unicode_value='length', tag='length')
MeasurementType.limestone_acoustic_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='limestone acoustic porosity', tag='limestone_acoustic_porosity')
MeasurementType.limestone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='limestone density porosity', tag='limestone_density_porosity')
MeasurementType.limestone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='limestone neutron porosity', tag='limestone_neutron_porosity')
MeasurementType.lithology_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='lithology correction', tag='lithology_correction')
MeasurementType.log_derived_permeability = MeasurementType._CF_enumeration.addEnumeration(unicode_value='log derived permeability', tag='log_derived_permeability')
MeasurementType.log_matrix_density = MeasurementType._CF_enumeration.addEnumeration(unicode_value='log matrix density', tag='log_matrix_density')
MeasurementType.magnetic_casing_collar_locator = MeasurementType._CF_enumeration.addEnumeration(unicode_value='magnetic casing collar locator', tag='magnetic_casing_collar_locator')
MeasurementType.matrix_density = MeasurementType._CF_enumeration.addEnumeration(unicode_value='matrix density', tag='matrix_density')
MeasurementType.matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='matrix travel time', tag='matrix_travel_time')
MeasurementType.measured_depth = MeasurementType._CF_enumeration.addEnumeration(unicode_value='measured depth', tag='measured_depth')
MeasurementType.mechanical_caliper = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mechanical caliper', tag='mechanical_caliper')
MeasurementType.mechanical_casing_collar_locator = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mechanical casing collar locator', tag='mechanical_casing_collar_locator')
MeasurementType.medium_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='medium conductivity', tag='medium_conductivity')
MeasurementType.medium_induction_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='medium induction conductivity', tag='medium_induction_conductivity')
MeasurementType.medium_induction_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='medium induction resistivity', tag='medium_induction_resistivity')
MeasurementType.medium_laterolog_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='medium laterolog conductivity', tag='medium_laterolog_conductivity')
MeasurementType.medium_laterolog_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='medium laterolog resistivity', tag='medium_laterolog_resistivity')
MeasurementType.medium_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='medium resistivity', tag='medium_resistivity')
MeasurementType.micro_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='micro conductivity', tag='micro_conductivity')
MeasurementType.micro_inverse_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='micro inverse conductivity', tag='micro_inverse_conductivity')
MeasurementType.micro_inverse_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='micro inverse resistivity', tag='micro_inverse_resistivity')
MeasurementType.micro_laterolog_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='micro laterolog conductivity', tag='micro_laterolog_conductivity')
MeasurementType.micro_laterolog_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='micro laterolog resistivity', tag='micro_laterolog_resistivity')
MeasurementType.micro_normal_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='micro normal conductivity', tag='micro_normal_conductivity')
MeasurementType.micro_normal_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='micro normal resistivity', tag='micro_normal_resistivity')
MeasurementType.micro_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='micro resistivity', tag='micro_resistivity')
MeasurementType.micro_spherically_focused_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='micro spherically focused conductivity', tag='micro_spherically_focused_conductivity')
MeasurementType.micro_spherically_focused_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='micro spherically focused resistivity', tag='micro_spherically_focused_resistivity')
MeasurementType.mineral = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mineral', tag='mineral')
MeasurementType.mud_cake_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud cake conductivity', tag='mud_cake_conductivity')
MeasurementType.mud_cake_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud cake correction', tag='mud_cake_correction')
MeasurementType.mud_cake_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud cake density correction', tag='mud_cake_density_correction')
MeasurementType.mud_cake_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud cake resistivity', tag='mud_cake_resistivity')
MeasurementType.mud_cake_resistivity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud cake resistivity correction', tag='mud_cake_resistivity_correction')
MeasurementType.mud_cake_thickness_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud cake thickness correction', tag='mud_cake_thickness_correction')
MeasurementType.mud_composition_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud composition correction', tag='mud_composition_correction')
MeasurementType.mud_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud conductivity', tag='mud_conductivity')
MeasurementType.mud_filtrate_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud filtrate conductivity', tag='mud_filtrate_conductivity')
MeasurementType.mud_filtrate_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud filtrate correction', tag='mud_filtrate_correction')
MeasurementType.mud_filtrate_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud filtrate density correction', tag='mud_filtrate_density_correction')
MeasurementType.mud_filtrate_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud filtrate resistivity', tag='mud_filtrate_resistivity')
MeasurementType.mud_filtrate_resistivity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud filtrate resistivity correction', tag='mud_filtrate_resistivity_correction')
MeasurementType.mud_filtrate_salinity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud filtrate salinity correction', tag='mud_filtrate_salinity_correction')
MeasurementType.mud_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud resistivity', tag='mud_resistivity')
MeasurementType.mud_salinity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud salinity correction', tag='mud_salinity_correction')
MeasurementType.mud_viscosity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud viscosity correction', tag='mud_viscosity_correction')
MeasurementType.mud_weight_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='mud weight correction', tag='mud_weight_correction')
MeasurementType.neutron_die_away_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='neutron die away time', tag='neutron_die_away_time')
MeasurementType.neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='neutron porosity', tag='neutron_porosity')
MeasurementType.nuclear_caliper = MeasurementType._CF_enumeration.addEnumeration(unicode_value='nuclear caliper', tag='nuclear_caliper')
MeasurementType.nuclear_magnetic_decay_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='nuclear magnetic decay time', tag='nuclear_magnetic_decay_time')
MeasurementType.nuclear_magnetism_log_permeability = MeasurementType._CF_enumeration.addEnumeration(unicode_value='nuclear magnetism log permeability', tag='nuclear_magnetism_log_permeability')
MeasurementType.nuclear_magnetism_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='nuclear magnetism porosity', tag='nuclear_magnetism_porosity')
MeasurementType.OH_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='OH density porosity', tag='OH_density_porosity')
MeasurementType.OH_dolomite_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='OH dolomite density porosity', tag='OH_dolomite_density_porosity')
MeasurementType.OH_dolomite_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='OH dolomite neutron porosity', tag='OH_dolomite_neutron_porosity')
MeasurementType.OH_limestone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='OH limestone density porosity', tag='OH_limestone_density_porosity')
MeasurementType.OH_limestone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='OH limestone neutron porosity', tag='OH_limestone_neutron_porosity')
MeasurementType.OH_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='OH neutron porosity', tag='OH_neutron_porosity')
MeasurementType.OH_sandstone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='OH sandstone density porosity', tag='OH_sandstone_density_porosity')
MeasurementType.OH_sandstone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='OH sandstone neutron porosity', tag='OH_sandstone_neutron_porosity')
MeasurementType.oil_based_mud_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='oil based mud correction', tag='oil_based_mud_correction')
MeasurementType.oil_saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='oil saturation', tag='oil_saturation')
MeasurementType.perforating = MeasurementType._CF_enumeration.addEnumeration(unicode_value='perforating', tag='perforating')
MeasurementType.permeability = MeasurementType._CF_enumeration.addEnumeration(unicode_value='permeability', tag='permeability')
MeasurementType.phase_shift = MeasurementType._CF_enumeration.addEnumeration(unicode_value='phase shift', tag='phase_shift')
MeasurementType.photoelectric_absorption = MeasurementType._CF_enumeration.addEnumeration(unicode_value='photoelectric absorption', tag='photoelectric_absorption')
MeasurementType.photoelectric_absorption_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='photoelectric absorption correction', tag='photoelectric_absorption_correction')
MeasurementType.physical_measurement_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='physical measurement correction', tag='physical_measurement_correction')
MeasurementType.plane_angle = MeasurementType._CF_enumeration.addEnumeration(unicode_value='plane angle', tag='plane_angle')
MeasurementType.porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='porosity', tag='porosity')
MeasurementType.porosity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='porosity correction', tag='porosity_correction')
MeasurementType.potassium = MeasurementType._CF_enumeration.addEnumeration(unicode_value='potassium', tag='potassium')
MeasurementType.pressure = MeasurementType._CF_enumeration.addEnumeration(unicode_value='pressure', tag='pressure')
MeasurementType.pressure_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='pressure correction', tag='pressure_correction')
MeasurementType.processed = MeasurementType._CF_enumeration.addEnumeration(unicode_value='processed', tag='processed')
MeasurementType.pulsed_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='pulsed neutron porosity', tag='pulsed_neutron_porosity')
MeasurementType.quality = MeasurementType._CF_enumeration.addEnumeration(unicode_value='quality', tag='quality')
MeasurementType.ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value='ratio', tag='ratio')
MeasurementType.raw = MeasurementType._CF_enumeration.addEnumeration(unicode_value='raw', tag='raw')
MeasurementType.relative_bearing = MeasurementType._CF_enumeration.addEnumeration(unicode_value='relative bearing', tag='relative_bearing')
MeasurementType.resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='resistivity', tag='resistivity')
MeasurementType.resistivity_factor_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='resistivity factor correction', tag='resistivity_factor_correction')
MeasurementType.resistivity_from_attenuation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='resistivity from attenuation', tag='resistivity_from_attenuation')
MeasurementType.resistivity_from_phase_shift = MeasurementType._CF_enumeration.addEnumeration(unicode_value='resistivity from phase shift', tag='resistivity_from_phase_shift')
MeasurementType.resistivity_phase_shift = MeasurementType._CF_enumeration.addEnumeration(unicode_value='resistivity phase shift', tag='resistivity_phase_shift')
MeasurementType.resistivity_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value='resistivity ratio', tag='resistivity_ratio')
MeasurementType.salinity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='salinity', tag='salinity')
MeasurementType.sampling = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sampling', tag='sampling')
MeasurementType.sandstone_acoustic_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sandstone acoustic porosity', tag='sandstone_acoustic_porosity')
MeasurementType.sandstone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sandstone density porosity', tag='sandstone_density_porosity')
MeasurementType.sandstone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sandstone neutron porosity', tag='sandstone_neutron_porosity')
MeasurementType.saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='saturation', tag='saturation')
MeasurementType.shale_volume = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shale volume', tag='shale_volume')
MeasurementType.shallow_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shallow conductivity', tag='shallow_conductivity')
MeasurementType.shallow_induction_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shallow induction conductivity', tag='shallow_induction_conductivity')
MeasurementType.shallow_induction_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shallow induction resistivity', tag='shallow_induction_resistivity')
MeasurementType.shallow_laterolog_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shallow laterolog conductivity', tag='shallow_laterolog_conductivity')
MeasurementType.shallow_laterolog_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shallow laterolog resistivity', tag='shallow_laterolog_resistivity')
MeasurementType.shallow_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shallow resistivity', tag='shallow_resistivity')
MeasurementType.shear_wave_dolomite_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shear wave dolomite porosity', tag='shear_wave_dolomite_porosity')
MeasurementType.shear_wave_limestone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shear wave limestone porosity', tag='shear_wave_limestone_porosity')
MeasurementType.shear_wave_matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shear wave matrix travel time', tag='shear_wave_matrix_travel_time')
MeasurementType.shear_wave_sandstone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shear wave sandstone porosity', tag='shear_wave_sandstone_porosity')
MeasurementType.shear_wave_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shear wave travel time', tag='shear_wave_travel_time')
MeasurementType.shifted = MeasurementType._CF_enumeration.addEnumeration(unicode_value='shifted', tag='shifted')
MeasurementType.sidewall_core_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sidewall core porosity', tag='sidewall_core_porosity')
MeasurementType.sigma = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sigma', tag='sigma')
MeasurementType.sigma_formation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sigma formation', tag='sigma_formation')
MeasurementType.sigma_gas = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sigma gas', tag='sigma_gas')
MeasurementType.sigma_hydrocarbon = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sigma hydrocarbon', tag='sigma_hydrocarbon')
MeasurementType.sigma_matrix = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sigma matrix', tag='sigma_matrix')
MeasurementType.sigma_oil = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sigma oil', tag='sigma_oil')
MeasurementType.sigma_water = MeasurementType._CF_enumeration.addEnumeration(unicode_value='sigma water', tag='sigma_water')
MeasurementType.slippage_velocity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='slippage velocity correction', tag='slippage_velocity_correction')
MeasurementType.smoothed = MeasurementType._CF_enumeration.addEnumeration(unicode_value='smoothed', tag='smoothed')
MeasurementType.spectral_gamma_ray = MeasurementType._CF_enumeration.addEnumeration(unicode_value='spectral gamma ray', tag='spectral_gamma_ray')
MeasurementType.spherically_focused_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='spherically focused conductivity', tag='spherically_focused_conductivity')
MeasurementType.spherically_focused_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='spherically focused resistivity', tag='spherically_focused_resistivity')
MeasurementType.spontaneous_potential = MeasurementType._CF_enumeration.addEnumeration(unicode_value='spontaneous potential', tag='spontaneous_potential')
MeasurementType.spreading_loss_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='spreading loss correction', tag='spreading_loss_correction')
MeasurementType.synthetic_well_log_trace = MeasurementType._CF_enumeration.addEnumeration(unicode_value='synthetic well log trace', tag='synthetic_well_log_trace')
MeasurementType.temperature = MeasurementType._CF_enumeration.addEnumeration(unicode_value='temperature', tag='temperature')
MeasurementType.temperature_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='temperature correction', tag='temperature_correction')
MeasurementType.tension = MeasurementType._CF_enumeration.addEnumeration(unicode_value='tension', tag='tension')
MeasurementType.ThK_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value='Th/K ratio', tag='ThK_ratio')
MeasurementType.thorium = MeasurementType._CF_enumeration.addEnumeration(unicode_value='thorium', tag='thorium')
MeasurementType.time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='time', tag='time')
MeasurementType.tool_diameter_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='tool diameter correction', tag='tool_diameter_correction')
MeasurementType.tool_eccentricity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='tool eccentricity correction', tag='tool_eccentricity_correction')
MeasurementType.total_gamma_ray = MeasurementType._CF_enumeration.addEnumeration(unicode_value='total gamma ray', tag='total_gamma_ray')
MeasurementType.total_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='total porosity', tag='total_porosity')
MeasurementType.tracer_survey = MeasurementType._CF_enumeration.addEnumeration(unicode_value='tracer survey', tag='tracer_survey')
MeasurementType.travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='travel time', tag='travel_time')
MeasurementType.true_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='true conductivity', tag='true_conductivity')
MeasurementType.true_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='true resistivity', tag='true_resistivity')
MeasurementType.true_vertical_depth = MeasurementType._CF_enumeration.addEnumeration(unicode_value='true vertical depth', tag='true_vertical_depth')
MeasurementType.tube_wave_dolomite_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='tube wave dolomite porosity', tag='tube_wave_dolomite_porosity')
MeasurementType.tube_wave_limestone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='tube wave limestone porosity', tag='tube_wave_limestone_porosity')
MeasurementType.tube_wave_matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='tube wave matrix travel time', tag='tube_wave_matrix_travel_time')
MeasurementType.tube_wave_sandstone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='tube wave sandstone porosity', tag='tube_wave_sandstone_porosity')
MeasurementType.tube_wave_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value='tube wave travel time', tag='tube_wave_travel_time')
MeasurementType.uranium = MeasurementType._CF_enumeration.addEnumeration(unicode_value='uranium', tag='uranium')
MeasurementType.velocity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='velocity', tag='velocity')
MeasurementType.volume = MeasurementType._CF_enumeration.addEnumeration(unicode_value='volume', tag='volume')
MeasurementType.water_based_fluid_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='water based fluid correction', tag='water_based_fluid_correction')
MeasurementType.water_holdup_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value='water holdup correction', tag='water_holdup_correction')
MeasurementType.water_saturated_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='water saturated conductivity', tag='water_saturated_conductivity')
MeasurementType.water_saturated_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value='water saturated resistivity', tag='water_saturated_resistivity')
MeasurementType.water_saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value='water saturation', tag='water_saturation')
MeasurementType.unknown = MeasurementType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
MeasurementType._InitializeFacetMap(MeasurementType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MeasurementType', MeasurementType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MessageProbability
class MessageProbability (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageProbability')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 3931, 1)
    _Documentation = None
MessageProbability._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageProbability, enum_prefix=None)
MessageProbability.low = MessageProbability._CF_enumeration.addEnumeration(unicode_value='low', tag='low')
MessageProbability.medium = MessageProbability._CF_enumeration.addEnumeration(unicode_value='medium', tag='medium')
MessageProbability.high = MessageProbability._CF_enumeration.addEnumeration(unicode_value='high', tag='high')
MessageProbability.unknown = MessageProbability._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
MessageProbability._InitializeFacetMap(MessageProbability._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageProbability', MessageProbability)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MessageSeverity
class MessageSeverity (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageSeverity')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 3958, 1)
    _Documentation = None
MessageSeverity._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageSeverity, enum_prefix=None)
MessageSeverity.catastrophic = MessageSeverity._CF_enumeration.addEnumeration(unicode_value='catastrophic', tag='catastrophic')
MessageSeverity.major = MessageSeverity._CF_enumeration.addEnumeration(unicode_value='major', tag='major')
MessageSeverity.minor = MessageSeverity._CF_enumeration.addEnumeration(unicode_value='minor', tag='minor')
MessageSeverity.unknown = MessageSeverity._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
MessageSeverity._InitializeFacetMap(MessageSeverity._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageSeverity', MessageSeverity)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MessageType
class MessageType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a message. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 3985, 1)
    _Documentation = 'These values represent the type of a message. '
MessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageType, enum_prefix=None)
MessageType.alarm = MessageType._CF_enumeration.addEnumeration(unicode_value='alarm', tag='alarm')
MessageType.event = MessageType._CF_enumeration.addEnumeration(unicode_value='event', tag='event')
MessageType.informational = MessageType._CF_enumeration.addEnumeration(unicode_value='informational', tag='informational')
MessageType.warning = MessageType._CF_enumeration.addEnumeration(unicode_value='warning', tag='warning')
MessageType.unknown = MessageType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
MessageType._InitializeFacetMap(MessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageType', MessageType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MudClass
class MudClass (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Defines the class of a drilling fluid."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MudClass')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4020, 1)
    _Documentation = 'Defines the class of a drilling fluid.'
MudClass._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MudClass, enum_prefix=None)
MudClass.water_based = MudClass._CF_enumeration.addEnumeration(unicode_value='water based', tag='water_based')
MudClass.oil_based = MudClass._CF_enumeration.addEnumeration(unicode_value='oil based', tag='oil_based')
MudClass.other = MudClass._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
MudClass.pneumatic = MudClass._CF_enumeration.addEnumeration(unicode_value='pneumatic', tag='pneumatic')
MudClass.unknown = MudClass._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
MudClass._InitializeFacetMap(MudClass._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MudClass', MudClass)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MudLogParameterType
class MudLogParameterType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """ "Text value" indicates that a text value is expected. 
			"Pressure value" indicates that an equivalentMudWeight value is expected.
			"Pressure gradient value" indicates that an equivalentMudWeight value is 
			  commonly expected but a pressureGradient value may also be specified.
			"Concentration value" indicates that a concentration value is expected.
			"Force value" indicates that a force value is expected.
			"Only" indicates that no other value is expected."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MudLogParameterType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4057, 1)
    _Documentation = '"Text value" indicates that a text value is expected. \n\t\t\t"Pressure value" indicates that an equivalentMudWeight value is expected.\n\t\t\t"Pressure gradient value" indicates that an equivalentMudWeight value is \n\t\t\t  commonly expected but a pressureGradient value may also be specified.\n\t\t\t"Concentration value" indicates that a concentration value is expected.\n\t\t\t"Force value" indicates that a force value is expected.\n\t\t\t"Only" indicates that no other value is expected.'
MudLogParameterType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MudLogParameterType, enum_prefix=None)
MudLogParameterType.bit_parameters = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='bit parameters', tag='bit_parameters')
MudLogParameterType.bit_type_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='bit type comment', tag='bit_type_comment')
MudLogParameterType.casing_point_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='casing point comment', tag='casing_point_comment')
MudLogParameterType.chromatograph_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='chromatograph comment', tag='chromatograph_comment')
MudLogParameterType.circulation_system_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='circulation system comment', tag='circulation_system_comment')
MudLogParameterType.core_interval_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='core interval comment', tag='core_interval_comment')
MudLogParameterType.cuttings_gas = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='cuttings gas', tag='cuttings_gas')
MudLogParameterType.direct_fracture_pressure = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='direct fracture pressure', tag='direct_fracture_pressure')
MudLogParameterType.direct_pore_pressure_measurements = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='direct pore pressure measurements', tag='direct_pore_pressure_measurements')
MudLogParameterType.drilling_data_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='drilling data comment', tag='drilling_data_comment')
MudLogParameterType.fracture_PG_estimate_most_likely = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='fracture PG estimate most likely', tag='fracture_PG_estimate_most_likely')
MudLogParameterType.gas_peaks_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='gas peaks comment', tag='gas_peaks_comment')
MudLogParameterType.gas_ratio_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='gas ratio comment', tag='gas_ratio_comment')
MudLogParameterType.general_engineering_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='general engineering comment', tag='general_engineering_comment')
MudLogParameterType.kicks_and_flows = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='kicks and flows', tag='kicks_and_flows')
MudLogParameterType.lithlog_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='lithlog comment', tag='lithlog_comment')
MudLogParameterType.lost_returns = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='lost returns', tag='lost_returns')
MudLogParameterType.LWD_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='LWD comment', tag='LWD_comment')
MudLogParameterType.marker_or_formation_top_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='marker or formation top comment', tag='marker_or_formation_top_comment')
MudLogParameterType.midnight_depth_date = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='midnight depth date', tag='midnight_depth_date')
MudLogParameterType.mud_check_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='mud check comment', tag='mud_check_comment')
MudLogParameterType.mud_data_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='mud data comment', tag='mud_data_comment')
MudLogParameterType.mudlog_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='mudlog comment', tag='mudlog_comment')
MudLogParameterType.overburden_gradient = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='overburden gradient', tag='overburden_gradient')
MudLogParameterType.overpull_on_connection = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='overpull on connection', tag='overpull_on_connection')
MudLogParameterType.overpull_on_trip = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='overpull on trip', tag='overpull_on_trip')
MudLogParameterType.pore_PG_estimate_most_likely = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='pore PG estimate most likely', tag='pore_PG_estimate_most_likely')
MudLogParameterType.pore_pressure_estimate_while_drilling = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='pore pressure estimate while drilling', tag='pore_pressure_estimate_while_drilling')
MudLogParameterType.pressure_data_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='pressure data comment', tag='pressure_data_comment')
MudLogParameterType.shale_density_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='shale density comment', tag='shale_density_comment')
MudLogParameterType.short_trip_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='short trip comment', tag='short_trip_comment')
MudLogParameterType.show_report_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='show report comment', tag='show_report_comment')
MudLogParameterType.sidewall_core_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='sidewall core comment', tag='sidewall_core_comment')
MudLogParameterType.sliding_Interval = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='sliding Interval', tag='sliding_Interval')
MudLogParameterType.steam_still_results_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='steam still results comment', tag='steam_still_results_comment')
MudLogParameterType.survey_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='survey comment', tag='survey_comment')
MudLogParameterType.temperature_data_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='temperature data comment', tag='temperature_data_comment')
MudLogParameterType.temperature_trend_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='temperature trend comment', tag='temperature_trend_comment')
MudLogParameterType.wireline_log_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='wireline log comment', tag='wireline_log_comment')
MudLogParameterType.unknown = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
MudLogParameterType._InitializeFacetMap(MudLogParameterType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MudLogParameterType', MudLogParameterType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MudSubClass
class MudSubClass (abstractTypeEnum):

    """
        The name of a data extension.
        The list of standard values is contained in the WITSML enumValues.xml file.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MudSubClass')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4319, 2)
    _Documentation = '\n        The name of a data extension.\n        The list of standard values is contained in the WITSML enumValues.xml file.\n      '
MudSubClass._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'MudSubClass', MudSubClass)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NADTypes
class NADTypes (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NADTypes')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4330, 2)
    _Documentation = None
NADTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NADTypes, enum_prefix=None)
NADTypes.NAD27 = NADTypes._CF_enumeration.addEnumeration(unicode_value='NAD27', tag='NAD27')
NADTypes.NAD83 = NADTypes._CF_enumeration.addEnumeration(unicode_value='NAD83', tag='NAD83')
NADTypes.unknown = NADTypes._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
NADTypes._InitializeFacetMap(NADTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NADTypes', NADTypes)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NameTagLocation
class NameTagLocation (abstractTypeEnum):

    """Defines the locations where an equipment tag might be found..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameTagLocation')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4352, 1)
    _Documentation = 'Defines the locations where an equipment tag might be found..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagLocation._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'NameTagLocation', NameTagLocation)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NameTagNumberingScheme
class NameTagNumberingScheme (abstractTypeEnum):

    """Defines the specifications for creating equipment tags..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameTagNumberingScheme')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4361, 1)
    _Documentation = 'Defines the specifications for creating equipment tags..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagNumberingScheme._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'NameTagNumberingScheme', NameTagNumberingScheme)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NameTagTechnology
class NameTagTechnology (abstractTypeEnum):

    """Defines the mechanisms for attaching an equipment tag to an item..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameTagTechnology')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4370, 1)
    _Documentation = 'Defines the mechanisms for attaching an equipment tag to an item..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagTechnology._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'NameTagTechnology', NameTagTechnology)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NorthOrSouth
class NorthOrSouth (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NorthOrSouth')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4379, 1)
    _Documentation = ''
NorthOrSouth._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NorthOrSouth, enum_prefix=None)
NorthOrSouth.north = NorthOrSouth._CF_enumeration.addEnumeration(unicode_value='north', tag='north')
NorthOrSouth.south = NorthOrSouth._CF_enumeration.addEnumeration(unicode_value='south', tag='south')
NorthOrSouth.unknown = NorthOrSouth._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
NorthOrSouth._InitializeFacetMap(NorthOrSouth._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NorthOrSouth', NorthOrSouth)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NozzleType
class NozzleType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NozzleType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4404, 1)
    _Documentation = None
NozzleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NozzleType, enum_prefix=None)
NozzleType.extended = NozzleType._CF_enumeration.addEnumeration(unicode_value='extended', tag='extended')
NozzleType.normal = NozzleType._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
NozzleType.unknown = NozzleType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
NozzleType._InitializeFacetMap(NozzleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NozzleType', NozzleType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}OpsReportVersion
class OpsReportVersion (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OpsReportVersion')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4427, 1)
    _Documentation = ''
OpsReportVersion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OpsReportVersion, enum_prefix=None)
OpsReportVersion.preliminary = OpsReportVersion._CF_enumeration.addEnumeration(unicode_value='preliminary', tag='preliminary')
OpsReportVersion.normal = OpsReportVersion._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
OpsReportVersion.final = OpsReportVersion._CF_enumeration.addEnumeration(unicode_value='final', tag='final')
OpsReportVersion.unknown = OpsReportVersion._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
OpsReportVersion._InitializeFacetMap(OpsReportVersion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OpsReportVersion', OpsReportVersion)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PIDXCommodityCode
class PIDXCommodityCode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The PIDX commodity codes used in a stimulation job."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PIDXCommodityCode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4460, 1)
    _Documentation = 'The PIDX commodity codes used in a stimulation job.'
PIDXCommodityCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PIDXCommodityCode, enum_prefix=None)
PIDXCommodityCode.n71131001 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131001', tag='n71131001')
PIDXCommodityCode.n71131002 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131002', tag='n71131002')
PIDXCommodityCode.n71131003 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131003', tag='n71131003')
PIDXCommodityCode.n71131004 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131004', tag='n71131004')
PIDXCommodityCode.n71131005 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131005', tag='n71131005')
PIDXCommodityCode.n71131006 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131006', tag='n71131006')
PIDXCommodityCode.n71131007 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131007', tag='n71131007')
PIDXCommodityCode.n71131008 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131008', tag='n71131008')
PIDXCommodityCode.n71131009 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131009', tag='n71131009')
PIDXCommodityCode.n71131010 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131010', tag='n71131010')
PIDXCommodityCode.n71131011 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131011', tag='n71131011')
PIDXCommodityCode.n71131012 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131012', tag='n71131012')
PIDXCommodityCode.n71131013 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131013', tag='n71131013')
PIDXCommodityCode.n71131014 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131014', tag='n71131014')
PIDXCommodityCode.n71131015 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131015', tag='n71131015')
PIDXCommodityCode.n71131016 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131016', tag='n71131016')
PIDXCommodityCode.n71131018 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131018', tag='n71131018')
PIDXCommodityCode.n71131019 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value='71131019', tag='n71131019')
PIDXCommodityCode._InitializeFacetMap(PIDXCommodityCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PIDXCommodityCode', PIDXCommodityCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PitType
class PitType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PitType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4559, 1)
    _Documentation = None
PitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PitType, enum_prefix=None)
PitType.bulk = PitType._CF_enumeration.addEnumeration(unicode_value='bulk', tag='bulk')
PitType.chemical = PitType._CF_enumeration.addEnumeration(unicode_value='chemical', tag='chemical')
PitType.drilling = PitType._CF_enumeration.addEnumeration(unicode_value='drilling', tag='drilling')
PitType.mix = PitType._CF_enumeration.addEnumeration(unicode_value='mix', tag='mix')
PitType.mud_cleaning = PitType._CF_enumeration.addEnumeration(unicode_value='mud cleaning', tag='mud_cleaning')
PitType.sand_trap = PitType._CF_enumeration.addEnumeration(unicode_value='sand trap', tag='sand_trap')
PitType.slug = PitType._CF_enumeration.addEnumeration(unicode_value='slug', tag='slug')
PitType.storage = PitType._CF_enumeration.addEnumeration(unicode_value='storage', tag='storage')
PitType.surge_tank = PitType._CF_enumeration.addEnumeration(unicode_value='surge tank', tag='surge_tank')
PitType.trip_tank = PitType._CF_enumeration.addEnumeration(unicode_value='trip tank', tag='trip_tank')
PitType.unknown = PitType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
PitType._InitializeFacetMap(PitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PitType', PitType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PrimitiveType
class PrimitiveType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The underlying XML Schema primitve type
			Does NOT support "decimal", "QName" or "NOTATION". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PrimitiveType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4625, 1)
    _Documentation = 'The underlying XML Schema primitve type\n\t\t\tDoes NOT support "decimal", "QName" or "NOTATION". '
PrimitiveType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PrimitiveType, enum_prefix=None)
PrimitiveType.string = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='string', tag='string')
PrimitiveType.boolean = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='boolean', tag='boolean')
PrimitiveType.float = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='float', tag='float')
PrimitiveType.double = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='double', tag='double')
PrimitiveType.duration = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='duration', tag='duration')
PrimitiveType.dateTime = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='dateTime', tag='dateTime')
PrimitiveType.time = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='time', tag='time')
PrimitiveType.date = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='date', tag='date')
PrimitiveType.gYearMonth = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='gYearMonth', tag='gYearMonth')
PrimitiveType.gYear = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='gYear', tag='gYear')
PrimitiveType.gMonthDay = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='gMonthDay', tag='gMonthDay')
PrimitiveType.gDay = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='gDay', tag='gDay')
PrimitiveType.gMonth = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='gMonth', tag='gMonth')
PrimitiveType.base64Binary = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='base64Binary', tag='base64Binary')
PrimitiveType.anyURI = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='anyURI', tag='anyURI')
PrimitiveType.unknown = PrimitiveType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
PrimitiveType._InitializeFacetMap(PrimitiveType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PrimitiveType', PrimitiveType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}Projection
class Projection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of coordinate system projection method.
			The source (except for "UserDefined") of the values is Geoshare V13. 
			For a detailed description of each value, see the Geoshare documentation of the 
			indicated "217" object at http://w3.posc.org/GeoshareSIG/technical/GDM/v13.0/."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Projection')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4657, 1)
    _Documentation = 'These values represent the type of coordinate system projection method.\n\t\t\tThe source (except for "UserDefined") of the values is Geoshare V13. \n\t\t\tFor a detailed description of each value, see the Geoshare documentation of the \n\t\t\tindicated "217" object at http://w3.posc.org/GeoshareSIG/technical/GDM/v13.0/.'
Projection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Projection, enum_prefix=None)
Projection.Albers_equal_area = Projection._CF_enumeration.addEnumeration(unicode_value='Albers equal area', tag='Albers_equal_area')
Projection.azimuthal_equidistant = Projection._CF_enumeration.addEnumeration(unicode_value='azimuthal equidistant', tag='azimuthal_equidistant')
Projection.Cassini = Projection._CF_enumeration.addEnumeration(unicode_value='Cassini', tag='Cassini')
Projection.equidistant_conic = Projection._CF_enumeration.addEnumeration(unicode_value='equidistant conic', tag='equidistant_conic')
Projection.equirectangular = Projection._CF_enumeration.addEnumeration(unicode_value='equirectangular', tag='equirectangular')
Projection.gnomonic = Projection._CF_enumeration.addEnumeration(unicode_value='gnomonic', tag='gnomonic')
Projection.Lambert_azimuthal = Projection._CF_enumeration.addEnumeration(unicode_value='Lambert azimuthal', tag='Lambert_azimuthal')
Projection.Lambert_conformal_conic = Projection._CF_enumeration.addEnumeration(unicode_value='Lambert conformal conic', tag='Lambert_conformal_conic')
Projection.Mercator = Projection._CF_enumeration.addEnumeration(unicode_value='Mercator', tag='Mercator')
Projection.Miller = Projection._CF_enumeration.addEnumeration(unicode_value='Miller', tag='Miller')
Projection.oblique_Mercator = Projection._CF_enumeration.addEnumeration(unicode_value='oblique Mercator', tag='oblique_Mercator')
Projection.orthographic = Projection._CF_enumeration.addEnumeration(unicode_value='orthographic', tag='orthographic')
Projection.perspective = Projection._CF_enumeration.addEnumeration(unicode_value='perspective', tag='perspective')
Projection.polar_stereographic = Projection._CF_enumeration.addEnumeration(unicode_value='polar stereographic', tag='polar_stereographic')
Projection.polyconic = Projection._CF_enumeration.addEnumeration(unicode_value='polyconic', tag='polyconic')
Projection.sinusoidal = Projection._CF_enumeration.addEnumeration(unicode_value='sinusoidal', tag='sinusoidal')
Projection.state_plane = Projection._CF_enumeration.addEnumeration(unicode_value='state plane', tag='state_plane')
Projection.stereographic = Projection._CF_enumeration.addEnumeration(unicode_value='stereographic', tag='stereographic')
Projection.transverse_Mercator = Projection._CF_enumeration.addEnumeration(unicode_value='transverse Mercator', tag='transverse_Mercator')
Projection.universal_transverse_Mercator = Projection._CF_enumeration.addEnumeration(unicode_value='universal transverse Mercator', tag='universal_transverse_Mercator')
Projection.user_defined = Projection._CF_enumeration.addEnumeration(unicode_value='user defined', tag='user_defined')
Projection.Van_der_Grinten = Projection._CF_enumeration.addEnumeration(unicode_value='Van der Grinten', tag='Van_der_Grinten')
Projection.unknown = Projection._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
Projection._InitializeFacetMap(Projection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Projection', Projection)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ProjectionVariantsObliqueMercator
class ProjectionVariantsObliqueMercator (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProjectionVariantsObliqueMercator')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4785, 1)
    _Documentation = None
ProjectionVariantsObliqueMercator._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProjectionVariantsObliqueMercator, enum_prefix=None)
ProjectionVariantsObliqueMercator.default = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value='default', tag='default')
ProjectionVariantsObliqueMercator.rectified = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value='rectified', tag='rectified')
ProjectionVariantsObliqueMercator.rectified_skew = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value='rectified skew', tag='rectified_skew')
ProjectionVariantsObliqueMercator.rectified_skew_center_origin = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value='rectified skew center origin', tag='rectified_skew_center_origin')
ProjectionVariantsObliqueMercator.unknown = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ProjectionVariantsObliqueMercator._InitializeFacetMap(ProjectionVariantsObliqueMercator._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProjectionVariantsObliqueMercator', ProjectionVariantsObliqueMercator)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PresTestType
class PresTestType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PresTestType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4817, 1)
    _Documentation = ''
PresTestType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PresTestType, enum_prefix=None)
PresTestType.leak_off_test = PresTestType._CF_enumeration.addEnumeration(unicode_value='leak off test', tag='leak_off_test')
PresTestType.formation_integrity_test = PresTestType._CF_enumeration.addEnumeration(unicode_value='formation integrity test', tag='formation_integrity_test')
PresTestType.unknown = PresTestType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
PresTestType._InitializeFacetMap(PresTestType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PresTestType', PresTestType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PrincipalMeridian
class PrincipalMeridian (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Principal Meridians for United States Public Land Surveys."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PrincipalMeridian')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4847, 1)
    _Documentation = 'Principal Meridians for United States Public Land Surveys.'
PrincipalMeridian._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PrincipalMeridian, enum_prefix=None)
PrincipalMeridian.n1st_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='1st Principal Meridian', tag='n1st_Principal_Meridian')
PrincipalMeridian.n2nd_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='2nd Principal Meridian', tag='n2nd_Principal_Meridian')
PrincipalMeridian.n3rd_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='3rd Principal Meridian', tag='n3rd_Principal_Meridian')
PrincipalMeridian.n4th_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='4th Principal Meridian', tag='n4th_Principal_Meridian')
PrincipalMeridian.n5th_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='5th Principal Meridian', tag='n5th_Principal_Meridian')
PrincipalMeridian.n6th_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='6th Principal Meridian', tag='n6th_Principal_Meridian')
PrincipalMeridian.Black_Hills_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Black Hills Meridian', tag='Black_Hills_Meridian')
PrincipalMeridian.Boise_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Boise Meridian', tag='Boise_Meridian')
PrincipalMeridian.Choctaw_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Choctaw Meridian', tag='Choctaw_Meridian')
PrincipalMeridian.Chickasaw_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Chickasaw Meridian', tag='Chickasaw_Meridian')
PrincipalMeridian.Cimarron_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Cimarron Meridian', tag='Cimarron_Meridian')
PrincipalMeridian.Copper_River_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Copper River Meridian', tag='Copper_River_Meridian')
PrincipalMeridian.Fairbanks_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Fairbanks Meridian', tag='Fairbanks_Meridian')
PrincipalMeridian.Gila_and_Salt_River_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Gila and Salt River Meridian', tag='Gila_and_Salt_River_Meridian')
PrincipalMeridian.Humboldt_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Humboldt Meridian', tag='Humboldt_Meridian')
PrincipalMeridian.Huntsville_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Huntsville Meridian', tag='Huntsville_Meridian')
PrincipalMeridian.Indian_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Indian Meridian', tag='Indian_Meridian')
PrincipalMeridian.Kateel_River_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Kateel River Meridian', tag='Kateel_River_Meridian')
PrincipalMeridian.Lousiana_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Lousiana Meridian', tag='Lousiana_Meridian')
PrincipalMeridian.Michigan_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Michigan Meridian', tag='Michigan_Meridian')
PrincipalMeridian.Mount_Diablo_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Mount Diablo Meridian', tag='Mount_Diablo_Meridian')
PrincipalMeridian.New_Mexico_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='New Mexico Meridian', tag='New_Mexico_Meridian')
PrincipalMeridian.Saint_Stephens_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Saint Stephens Meridian', tag='Saint_Stephens_Meridian')
PrincipalMeridian.Saint_Helena_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Saint Helena Meridian', tag='Saint_Helena_Meridian')
PrincipalMeridian.Salt_Lake_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Salt Lake Meridian', tag='Salt_Lake_Meridian')
PrincipalMeridian.San_Bernardo_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='San Bernardo Meridian', tag='San_Bernardo_Meridian')
PrincipalMeridian.Seward_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Seward Meridian', tag='Seward_Meridian')
PrincipalMeridian.Tallahassee_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Tallahassee Meridian', tag='Tallahassee_Meridian')
PrincipalMeridian.Uintah_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Uintah Meridian', tag='Uintah_Meridian')
PrincipalMeridian.Umiat_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Umiat Meridian', tag='Umiat_Meridian')
PrincipalMeridian.Ute_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Ute Meridian', tag='Ute_Meridian')
PrincipalMeridian.Washington_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Washington Meridian', tag='Washington_Meridian')
PrincipalMeridian.Williamette_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Williamette Meridian', tag='Williamette_Meridian')
PrincipalMeridian.Wind_River_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='Wind River Meridian', tag='Wind_River_Meridian')
PrincipalMeridian.unknown = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
PrincipalMeridian._InitializeFacetMap(PrincipalMeridian._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PrincipalMeridian', PrincipalMeridian)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PumpType
class PumpType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a pump. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PumpType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5033, 1)
    _Documentation = 'These values represent the type of a pump. '
PumpType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PumpType, enum_prefix=None)
PumpType.centrifugal = PumpType._CF_enumeration.addEnumeration(unicode_value='centrifugal', tag='centrifugal')
PumpType.duplex = PumpType._CF_enumeration.addEnumeration(unicode_value='duplex', tag='duplex')
PumpType.triplex = PumpType._CF_enumeration.addEnumeration(unicode_value='triplex', tag='triplex')
PumpType.unknown = PumpType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
PumpType._InitializeFacetMap(PumpType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PumpType', PumpType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PumpOpType
class PumpOpType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PumpOpType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5063, 1)
    _Documentation = None
PumpOpType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PumpOpType, enum_prefix=None)
PumpOpType.drilling = PumpOpType._CF_enumeration.addEnumeration(unicode_value='drilling', tag='drilling')
PumpOpType.reaming = PumpOpType._CF_enumeration.addEnumeration(unicode_value='reaming', tag='reaming')
PumpOpType.circulating = PumpOpType._CF_enumeration.addEnumeration(unicode_value='circulating', tag='circulating')
PumpOpType.slow_pump = PumpOpType._CF_enumeration.addEnumeration(unicode_value='slow pump', tag='slow_pump')
PumpOpType.unknown = PumpOpType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
PumpOpType._InitializeFacetMap(PumpOpType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PumpOpType', PumpOpType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}QualifierType
class QualifierType (abstractTypeEnum):

    """The type of qualifier of a lithology.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QualifierType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5095, 1)
    _Documentation = 'The type of qualifier of a lithology.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
QualifierType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'QualifierType', QualifierType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ReadingKind
class ReadingKind (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReadingKind')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5104, 1)
    _Documentation = ''
ReadingKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReadingKind, enum_prefix=None)
ReadingKind.measured = ReadingKind._CF_enumeration.addEnumeration(unicode_value='measured', tag='measured')
ReadingKind.estimated = ReadingKind._CF_enumeration.addEnumeration(unicode_value='estimated', tag='estimated')
ReadingKind.unknown = ReadingKind._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ReadingKind._InitializeFacetMap(ReadingKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReadingKind', ReadingKind)

# Atomic simple type: {http://www.witsml.org/schemas/1series}RigType
class RigType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drilling rig. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RigType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5129, 1)
    _Documentation = 'These values represent the type of drilling rig. '
RigType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RigType, enum_prefix=None)
RigType.barge = RigType._CF_enumeration.addEnumeration(unicode_value='barge', tag='barge')
RigType.coiled_tubing = RigType._CF_enumeration.addEnumeration(unicode_value='coiled tubing', tag='coiled_tubing')
RigType.floater = RigType._CF_enumeration.addEnumeration(unicode_value='floater', tag='floater')
RigType.jackup = RigType._CF_enumeration.addEnumeration(unicode_value='jackup', tag='jackup')
RigType.land = RigType._CF_enumeration.addEnumeration(unicode_value='land', tag='land')
RigType.platform = RigType._CF_enumeration.addEnumeration(unicode_value='platform', tag='platform')
RigType.semi_submersible = RigType._CF_enumeration.addEnumeration(unicode_value='semi-submersible', tag='semi_submersible')
RigType.unknown = RigType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
RigType._InitializeFacetMap(RigType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RigType', RigType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}RiskAffectedPersonnel
class RiskAffectedPersonnel (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Personnel affected by a risk."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RiskAffectedPersonnel')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5179, 1)
    _Documentation = 'Personnel affected by a risk.'
RiskAffectedPersonnel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RiskAffectedPersonnel, enum_prefix=None)
RiskAffectedPersonnel.cementer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='cementer', tag='cementer')
RiskAffectedPersonnel.company_man = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='company man', tag='company_man')
RiskAffectedPersonnel.contractor = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='contractor', tag='contractor')
RiskAffectedPersonnel.directional_driller = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='directional driller', tag='directional_driller')
RiskAffectedPersonnel.driller = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='driller', tag='driller')
RiskAffectedPersonnel.drilling_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='drilling engineer', tag='drilling_engineer')
RiskAffectedPersonnel.drilling_superintendent = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='drilling superintendent', tag='drilling_superintendent')
RiskAffectedPersonnel.drilling_team = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='drilling team', tag='drilling_team')
RiskAffectedPersonnel.facility_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='facility engineer', tag='facility_engineer')
RiskAffectedPersonnel.field_service_manager = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='field service manager', tag='field_service_manager')
RiskAffectedPersonnel.foreman = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='foreman', tag='foreman')
RiskAffectedPersonnel.general_service_supervisor = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='general service supervisor', tag='general_service_supervisor')
RiskAffectedPersonnel.geologist = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='geologist', tag='geologist')
RiskAffectedPersonnel.member = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='member', tag='member')
RiskAffectedPersonnel.mud_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='mud engineer', tag='mud_engineer')
RiskAffectedPersonnel.mud_logger = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='mud logger', tag='mud_logger')
RiskAffectedPersonnel.MWD_or_LWD_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='MWD or LWD engineer', tag='MWD_or_LWD_engineer')
RiskAffectedPersonnel.perform_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='perform engineer', tag='perform_engineer')
RiskAffectedPersonnel.petrophysicist = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='petrophysicist', tag='petrophysicist')
RiskAffectedPersonnel.production_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='production engineer', tag='production_engineer')
RiskAffectedPersonnel.remotely_operated_vehicle_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='remotely operated vehicle engineer', tag='remotely_operated_vehicle_engineer')
RiskAffectedPersonnel.safety_manger = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='safety manger', tag='safety_manger')
RiskAffectedPersonnel.sales_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='sales engineer', tag='sales_engineer')
RiskAffectedPersonnel.service_supervisor = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='service supervisor', tag='service_supervisor')
RiskAffectedPersonnel.technical_support = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='technical support', tag='technical_support')
RiskAffectedPersonnel.tool_pusher = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='tool pusher', tag='tool_pusher')
RiskAffectedPersonnel.wireline_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value='wireline engineer', tag='wireline_engineer')
RiskAffectedPersonnel._InitializeFacetMap(RiskAffectedPersonnel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RiskAffectedPersonnel', RiskAffectedPersonnel)

# Atomic simple type: {http://www.witsml.org/schemas/1series}RiskCategory
class RiskCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of slow circulation rate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RiskCategory')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5322, 1)
    _Documentation = 'Type of slow circulation rate.'
RiskCategory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RiskCategory, enum_prefix=None)
RiskCategory.hydraulics = RiskCategory._CF_enumeration.addEnumeration(unicode_value='hydraulics', tag='hydraulics')
RiskCategory.mechanical = RiskCategory._CF_enumeration.addEnumeration(unicode_value='mechanical', tag='mechanical')
RiskCategory.time_related = RiskCategory._CF_enumeration.addEnumeration(unicode_value='time related', tag='time_related')
RiskCategory.wellbore_stability = RiskCategory._CF_enumeration.addEnumeration(unicode_value='wellbore stability', tag='wellbore_stability')
RiskCategory.directional_drilling = RiskCategory._CF_enumeration.addEnumeration(unicode_value='directional drilling', tag='directional_drilling')
RiskCategory.bit = RiskCategory._CF_enumeration.addEnumeration(unicode_value='bit', tag='bit')
RiskCategory.equipment_failure = RiskCategory._CF_enumeration.addEnumeration(unicode_value='equipment failure', tag='equipment_failure')
RiskCategory.completion = RiskCategory._CF_enumeration.addEnumeration(unicode_value='completion', tag='completion')
RiskCategory.casing = RiskCategory._CF_enumeration.addEnumeration(unicode_value='casing', tag='casing')
RiskCategory.other = RiskCategory._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
RiskCategory.HSE = RiskCategory._CF_enumeration.addEnumeration(unicode_value='HSE', tag='HSE')
RiskCategory.unknown = RiskCategory._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
RiskCategory._InitializeFacetMap(RiskCategory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RiskCategory', RiskCategory)

# Atomic simple type: {http://www.witsml.org/schemas/1series}RiskSubCategory
class RiskSubCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Risk Sub-Categories."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RiskSubCategory')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5392, 1)
    _Documentation = 'Risk Sub-Categories.'
RiskSubCategory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RiskSubCategory, enum_prefix=None)
RiskSubCategory.gas_kick = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='gas kick', tag='gas_kick')
RiskSubCategory.shallow_water_influx = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='shallow water influx', tag='shallow_water_influx')
RiskSubCategory.other_influx_or_kicks = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='other influx or kicks', tag='other_influx_or_kicks')
RiskSubCategory.loss_circulation = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='loss circulation', tag='loss_circulation')
RiskSubCategory.poor_hole_cleaning = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='poor hole cleaning', tag='poor_hole_cleaning')
RiskSubCategory.good_hole_cleaning_at_high_ROP = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='good hole cleaning at high ROP', tag='good_hole_cleaning_at_high_ROP')
RiskSubCategory.high_mud_weight = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='high mud weight', tag='high_mud_weight')
RiskSubCategory.special_additives_needed = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='special additives needed', tag='special_additives_needed')
RiskSubCategory.gumbo_problems = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='gumbo problems', tag='gumbo_problems')
RiskSubCategory.high_ECD___rheology_related = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='high ECD - rheology related', tag='high_ECD___rheology_related')
RiskSubCategory.excessive_circulation = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='excessive circulation', tag='excessive_circulation')
RiskSubCategory.performing_a_kill = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='performing a kill', tag='performing_a_kill')
RiskSubCategory.mud_weight_change = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='mud weight change', tag='mud_weight_change')
RiskSubCategory.excessive_pipe_cement_scaling = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='excessive pipe cement scaling', tag='excessive_pipe_cement_scaling')
RiskSubCategory.pit_gain_or_loss = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='pit gain or loss', tag='pit_gain_or_loss')
RiskSubCategory.mud_stability_problems = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='mud stability problems', tag='mud_stability_problems')
RiskSubCategory.shallow_gas_flow = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='shallow gas flow', tag='shallow_gas_flow')
RiskSubCategory.twist_off = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='twist off', tag='twist_off')
RiskSubCategory.stuck_pipe = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='stuck pipe', tag='stuck_pipe')
RiskSubCategory.wireline_stuck_in_hole = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='wireline stuck in hole', tag='wireline_stuck_in_hole')
RiskSubCategory.stick_and_slip = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='stick and slip', tag='stick_and_slip')
RiskSubCategory.vibration___axial = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='vibration - axial', tag='vibration___axial')
RiskSubCategory.vibration___torsional = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='vibration - torsional', tag='vibration___torsional')
RiskSubCategory.vibration___transverse = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='vibration - transverse', tag='vibration___transverse')
RiskSubCategory.vibration_unknown_or_rough_drilling = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='vibration unknown or rough drilling', tag='vibration_unknown_or_rough_drilling')
RiskSubCategory.uneven_wear_of_BHA = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='uneven wear of BHA', tag='uneven_wear_of_BHA')
RiskSubCategory.uneven_wear_of_drillstring = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='uneven wear of drillstring', tag='uneven_wear_of_drillstring')
RiskSubCategory.excessive_torque = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='excessive torque', tag='excessive_torque')
RiskSubCategory.excessive_drag = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='excessive drag', tag='excessive_drag')
RiskSubCategory.reaming_greater_than_2_hours = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='reaming greater than 2 hours', tag='reaming_greater_than_2_hours')
RiskSubCategory.washouts = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='washouts', tag='washouts')
RiskSubCategory.tight_hole_or_overPull = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='tight hole or overPull', tag='tight_hole_or_overPull')
RiskSubCategory.failed_inspections_or_fatigue_wear = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='failed inspections or fatigue wear', tag='failed_inspections_or_fatigue_wear')
RiskSubCategory.mechanical = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='mechanical', tag='mechanical')
RiskSubCategory.drilling_greater_than_1000_feetday = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='drilling greater than 1000 feet/day', tag='drilling_greater_than_1000_feetday')
RiskSubCategory.drilling_greater_than_2000_feetday = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='drilling greater than 2000 feet/day', tag='drilling_greater_than_2000_feetday')
RiskSubCategory.drilling_less_than_20_feetday = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='drilling less than 20 feet/day', tag='drilling_less_than_20_feetday')
RiskSubCategory.trips_greater_than_24_hours = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='trips greater than 24 hours', tag='trips_greater_than_24_hours')
RiskSubCategory.excessive_time_for_BHA_makeup = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='excessive time for BHA makeup', tag='excessive_time_for_BHA_makeup')
RiskSubCategory.waiting_on_decisions = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='waiting on decisions', tag='waiting_on_decisions')
RiskSubCategory.waiting_on_weather = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='waiting on weather', tag='waiting_on_weather')
RiskSubCategory.waiting_on_tools = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='waiting on tools', tag='waiting_on_tools')
RiskSubCategory.sloughing_or_packoffs = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='sloughing or packoffs', tag='sloughing_or_packoffs')
RiskSubCategory.ballooning = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='ballooning', tag='ballooning')
RiskSubCategory.fracture_problems = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='fracture problems', tag='fracture_problems')
RiskSubCategory.unstable_zones = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='unstable zones', tag='unstable_zones')
RiskSubCategory.formation_integrity_test = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='formation integrity test', tag='formation_integrity_test')
RiskSubCategory.leak_off_test = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='leak-off test', tag='leak_off_test')
RiskSubCategory.tectonics = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='tectonics', tag='tectonics')
RiskSubCategory.pore_pressure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='pore pressure', tag='pore_pressure')
RiskSubCategory.breakouts = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='breakouts', tag='breakouts')
RiskSubCategory.bed_parallel = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='bed parallel', tag='bed_parallel')
RiskSubCategory.wellbore_stability = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='wellbore stability', tag='wellbore_stability')
RiskSubCategory.excessive_doglegs = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='excessive doglegs', tag='excessive_doglegs')
RiskSubCategory.sidetrack = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='sidetrack', tag='sidetrack')
RiskSubCategory.BHA_change_for_directional = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='BHA change for directional', tag='BHA_change_for_directional')
RiskSubCategory.wrong_total_flow_area = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='wrong total flow area', tag='wrong_total_flow_area')
RiskSubCategory.well_collision___actual = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='well collision - actual', tag='well_collision___actual')
RiskSubCategory.well_collision___technical = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='well collision - technical', tag='well_collision___technical')
RiskSubCategory.geosteering = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='geosteering', tag='geosteering')
RiskSubCategory.abnormal_tendency_changes = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='abnormal tendency changes', tag='abnormal_tendency_changes')
RiskSubCategory.resurveying = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='resurveying', tag='resurveying')
RiskSubCategory.in_field_referencing_IFR_actions = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='in-field referencing (IFR) actions', tag='in_field_referencing_IFR_actions')
RiskSubCategory.bit_or_BHA_performance = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='bit or BHA performance', tag='bit_or_BHA_performance')
RiskSubCategory.drilling_optimization = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='drilling optimization', tag='drilling_optimization')
RiskSubCategory.bit_balling = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='bit balling', tag='bit_balling')
RiskSubCategory.lost_cones_or_broken_cutters = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='lost cones or broken cutters', tag='lost_cones_or_broken_cutters')
RiskSubCategory.excessive_bit_wear_or_gauge = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='excessive bit wear or gauge', tag='excessive_bit_wear_or_gauge')
RiskSubCategory.low_rate_of_bit_penetration = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='low rate of bit penetration', tag='low_rate_of_bit_penetration')
RiskSubCategory.high_rate_of_bit_penetration = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='high rate of bit penetration', tag='high_rate_of_bit_penetration')
RiskSubCategory.downhole_tool = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='downhole tool', tag='downhole_tool')
RiskSubCategory.surface_system = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='surface system', tag='surface_system')
RiskSubCategory.motor_or_rotary_steerable_system_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='motor or rotary steerable system failure', tag='motor_or_rotary_steerable_system_failure')
RiskSubCategory.topdrive_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='topdrive failure', tag='topdrive_failure')
RiskSubCategory.hoisting_equipment_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='hoisting equipment failure', tag='hoisting_equipment_failure')
RiskSubCategory.circulating_equipment_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='circulating equipment failure', tag='circulating_equipment_failure')
RiskSubCategory.electrical_system_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='electrical system failure', tag='electrical_system_failure')
RiskSubCategory.blow_out_preventer_events = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='blow out preventer events', tag='blow_out_preventer_events')
RiskSubCategory.surface_instrumentation_problems = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='surface instrumentation problems', tag='surface_instrumentation_problems')
RiskSubCategory.rig_communications = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='rig communications', tag='rig_communications')
RiskSubCategory.completion_equipment_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='completion equipment failure', tag='completion_equipment_failure')
RiskSubCategory.miscellaneous_rig_equipment = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='miscellaneous rig equipment', tag='miscellaneous_rig_equipment')
RiskSubCategory.tool_or_equipment_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='tool or equipment failure', tag='tool_or_equipment_failure')
RiskSubCategory.squeeze_jobs = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='squeeze jobs', tag='squeeze_jobs')
RiskSubCategory.casing_surge_losses = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='casing surge losses', tag='casing_surge_losses')
RiskSubCategory.stuck_casing_or_completion = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='stuck casing or completion', tag='stuck_casing_or_completion')
RiskSubCategory.shoe_failures = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='shoe failures', tag='shoe_failures')
RiskSubCategory.early_cement_setup = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='early cement setup', tag='early_cement_setup')
RiskSubCategory.casing_collapse = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='casing collapse', tag='casing_collapse')
RiskSubCategory.milling = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='milling', tag='milling')
RiskSubCategory.excessive_casing_wear_or_cuttings = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='excessive casing wear or cuttings', tag='excessive_casing_wear_or_cuttings')
RiskSubCategory.excessive_formation_damage_or_skin = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='excessive formation damage or skin', tag='excessive_formation_damage_or_skin')
RiskSubCategory.casing_rotation_or_reciprocation_rqd = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='casing rotation or reciprocation rqd', tag='casing_rotation_or_reciprocation_rqd')
RiskSubCategory.broaching = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='broaching', tag='broaching')
RiskSubCategory.completion_or_casing = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='completion or casing', tag='completion_or_casing')
RiskSubCategory.stratigraphy = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='stratigraphy', tag='stratigraphy')
RiskSubCategory.fishing = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='fishing', tag='fishing')
RiskSubCategory.junk_in_hole = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='junk in hole', tag='junk_in_hole')
RiskSubCategory.delay_due_to_political_unrest = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='delay due to political unrest', tag='delay_due_to_political_unrest')
RiskSubCategory.rig_move = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='rig move', tag='rig_move')
RiskSubCategory.gas_hydrates = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='gas hydrates', tag='gas_hydrates')
RiskSubCategory.pending_analysis = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='pending analysis', tag='pending_analysis')
RiskSubCategory.riser_disconnect = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='riser disconnect', tag='riser_disconnect')
RiskSubCategory.other = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
RiskSubCategory.personnel = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='personnel', tag='personnel')
RiskSubCategory.environmental = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='environmental', tag='environmental')
RiskSubCategory.automotive = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='automotive', tag='automotive')
RiskSubCategory.asset = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='asset', tag='asset')
RiskSubCategory.information = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='information', tag='information')
RiskSubCategory.time = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='time', tag='time')
RiskSubCategory.HSE = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value='HSE', tag='HSE')
RiskSubCategory._InitializeFacetMap(RiskSubCategory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RiskSubCategory', RiskSubCategory)

# Atomic simple type: {http://www.witsml.org/schemas/1series}RiskType
class RiskType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Types of risk."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RiskType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5955, 1)
    _Documentation = 'Types of risk.'
RiskType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RiskType, enum_prefix=None)
RiskType.risk = RiskType._CF_enumeration.addEnumeration(unicode_value='risk', tag='risk')
RiskType.event = RiskType._CF_enumeration.addEnumeration(unicode_value='event', tag='event')
RiskType.near_miss = RiskType._CF_enumeration.addEnumeration(unicode_value='near miss', tag='near_miss')
RiskType.best_practice = RiskType._CF_enumeration.addEnumeration(unicode_value='best practice', tag='best_practice')
RiskType.lessons_learned = RiskType._CF_enumeration.addEnumeration(unicode_value='lessons learned', tag='lessons_learned')
RiskType.other = RiskType._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
RiskType.unknown = RiskType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
RiskType._InitializeFacetMap(RiskType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RiskType', RiskType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ScrType
class ScrType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of slow circulation rate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ScrType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6000, 1)
    _Documentation = 'Type of slow circulation rate.'
ScrType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ScrType, enum_prefix=None)
ScrType.string_annulus = ScrType._CF_enumeration.addEnumeration(unicode_value='string annulus', tag='string_annulus')
ScrType.string_kill_line = ScrType._CF_enumeration.addEnumeration(unicode_value='string kill line', tag='string_kill_line')
ScrType.string_choke_line = ScrType._CF_enumeration.addEnumeration(unicode_value='string choke line', tag='string_choke_line')
ScrType.unknown = ScrType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ScrType._InitializeFacetMap(ScrType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ScrType', ScrType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ShowFluorescence
class ShowFluorescence (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShowFluorescence')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6030, 1)
    _Documentation = None
ShowFluorescence._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowFluorescence, enum_prefix=None)
ShowFluorescence.faint = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value='faint', tag='faint')
ShowFluorescence.bright = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value='bright', tag='bright')
ShowFluorescence.none = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
ShowFluorescence.unknown = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ShowFluorescence._InitializeFacetMap(ShowFluorescence._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ShowFluorescence', ShowFluorescence)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ShowLevel
class ShowLevel (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShowLevel')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6057, 1)
    _Documentation = None
ShowLevel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowLevel, enum_prefix=None)
ShowLevel.blooming = ShowLevel._CF_enumeration.addEnumeration(unicode_value='blooming', tag='blooming')
ShowLevel.streaming = ShowLevel._CF_enumeration.addEnumeration(unicode_value='streaming', tag='streaming')
ShowLevel.unknown = ShowLevel._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ShowLevel._InitializeFacetMap(ShowLevel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ShowLevel', ShowLevel)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ShowRating
class ShowRating (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShowRating')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6079, 1)
    _Documentation = None
ShowRating._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowRating, enum_prefix=None)
ShowRating.none = ShowRating._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
ShowRating.very_poor = ShowRating._CF_enumeration.addEnumeration(unicode_value='very poor', tag='very_poor')
ShowRating.poor = ShowRating._CF_enumeration.addEnumeration(unicode_value='poor', tag='poor')
ShowRating.fair = ShowRating._CF_enumeration.addEnumeration(unicode_value='fair', tag='fair')
ShowRating.good = ShowRating._CF_enumeration.addEnumeration(unicode_value='good', tag='good')
ShowRating.very_good = ShowRating._CF_enumeration.addEnumeration(unicode_value='very good', tag='very_good')
ShowRating.unknown = ShowRating._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ShowRating._InitializeFacetMap(ShowRating._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ShowRating', ShowRating)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ShowSpeed
class ShowSpeed (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShowSpeed')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6121, 1)
    _Documentation = None
ShowSpeed._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowSpeed, enum_prefix=None)
ShowSpeed.slow = ShowSpeed._CF_enumeration.addEnumeration(unicode_value='slow', tag='slow')
ShowSpeed.moderately_fast = ShowSpeed._CF_enumeration.addEnumeration(unicode_value='moderately fast', tag='moderately_fast')
ShowSpeed.fast = ShowSpeed._CF_enumeration.addEnumeration(unicode_value='fast', tag='fast')
ShowSpeed.instantaneous = ShowSpeed._CF_enumeration.addEnumeration(unicode_value='instantaneous', tag='instantaneous')
ShowSpeed.none = ShowSpeed._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
ShowSpeed.unknown = ShowSpeed._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ShowSpeed._InitializeFacetMap(ShowSpeed._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ShowSpeed', ShowSpeed)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StateDetailActivity
class StateDetailActivity (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StateDetailActivity')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6158, 1)
    _Documentation = ''
StateDetailActivity._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StateDetailActivity, enum_prefix=None)
StateDetailActivity.injury = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value='injury', tag='injury')
StateDetailActivity.operation_failed = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value='operation failed', tag='operation_failed')
StateDetailActivity.kick = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value='kick', tag='kick')
StateDetailActivity.circulation_loss = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value='circulation loss', tag='circulation_loss')
StateDetailActivity.mud_loss = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value='mud loss', tag='mud_loss')
StateDetailActivity.stuck_equipment = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value='stuck equipment', tag='stuck_equipment')
StateDetailActivity.equipment_failure = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value='equipment failure', tag='equipment_failure')
StateDetailActivity.equipment_hang = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value='equipment hang', tag='equipment_hang')
StateDetailActivity.success = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value='success', tag='success')
StateDetailActivity.unknown = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
StateDetailActivity._InitializeFacetMap(StateDetailActivity._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StateDetailActivity', StateDetailActivity)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimAdditiveType
class StimAdditiveType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The types of additives used in a stimulation job."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StimAdditiveType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6219, 1)
    _Documentation = 'The types of additives used in a stimulation job.'
StimAdditiveType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimAdditiveType, enum_prefix=None)
StimAdditiveType.abrasive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='abrasive', tag='abrasive')
StimAdditiveType.accelerator = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='accelerator', tag='accelerator')
StimAdditiveType.acid_inhibitorretarder = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='acid inhibitor/retarder', tag='acid_inhibitorretarder')
StimAdditiveType.acid_material = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='acid material', tag='acid_material')
StimAdditiveType.acid_soluble_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='acid soluble additive', tag='acid_soluble_additive')
StimAdditiveType.acid_source = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='acid source', tag='acid_source')
StimAdditiveType.activator = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='activator', tag='activator')
StimAdditiveType.additive_material = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='additive material', tag='additive_material')
StimAdditiveType.alcohol = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='alcohol', tag='alcohol')
StimAdditiveType.anti_Sludge = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='anti-Sludge', tag='anti_Sludge')
StimAdditiveType.anti_sulfide_cracker = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='anti-sulfide cracker', tag='anti_sulfide_cracker')
StimAdditiveType.aromatic_solvent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='aromatic solvent', tag='aromatic_solvent')
StimAdditiveType.biocide = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='biocide', tag='biocide')
StimAdditiveType.borehole_stabilizer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='borehole stabilizer', tag='borehole_stabilizer')
StimAdditiveType.breaker = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='breaker', tag='breaker')
StimAdditiveType.bridging_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='bridging agent', tag='bridging_agent')
StimAdditiveType.buffer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='buffer', tag='buffer')
StimAdditiveType.calcium_remover = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='calcium remover', tag='calcium_remover')
StimAdditiveType.carrying_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='carrying agent', tag='carrying_agent')
StimAdditiveType.catalyst = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='catalyst', tag='catalyst')
StimAdditiveType.clay = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='clay', tag='clay')
StimAdditiveType.clay_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='clay control', tag='clay_control')
StimAdditiveType.conductivity_enhancer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='conductivity enhancer', tag='conductivity_enhancer')
StimAdditiveType.conformance_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='conformance control', tag='conformance_control')
StimAdditiveType.conformance_caterial = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='conformance caterial', tag='conformance_caterial')
StimAdditiveType.corrosion_inhibitor = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='corrosion inhibitor', tag='corrosion_inhibitor')
StimAdditiveType.crosslink_enhancer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='crosslink enhancer', tag='crosslink_enhancer')
StimAdditiveType.crosslinker = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='crosslinker', tag='crosslinker')
StimAdditiveType.curing_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='curing agent', tag='curing_agent')
StimAdditiveType.defoamer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='defoamer', tag='defoamer')
StimAdditiveType.demulsifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='demulsifier', tag='demulsifier')
StimAdditiveType.diluent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='diluent', tag='diluent')
StimAdditiveType.dispersant = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='dispersant', tag='dispersant')
StimAdditiveType.diverter = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='diverter', tag='diverter')
StimAdditiveType.elastomeric_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='elastomeric additive', tag='elastomeric_additive')
StimAdditiveType.emulsifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='emulsifier', tag='emulsifier')
StimAdditiveType.epoxy_resin = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='epoxy resin', tag='epoxy_resin')
StimAdditiveType.expoxy_resin_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='expoxy resin agent', tag='expoxy_resin_agent')
StimAdditiveType.expander = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='expander', tag='expander')
StimAdditiveType.filtration_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='filtration control', tag='filtration_control')
StimAdditiveType.flocculant = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='flocculant', tag='flocculant')
StimAdditiveType.fluid_loss_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='fluid loss control', tag='fluid_loss_control')
StimAdditiveType.flushspacer_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='flush/spacer additive', tag='flushspacer_additive')
StimAdditiveType.foamer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='foamer', tag='foamer')
StimAdditiveType.formation_sealer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='formation sealer', tag='formation_sealer')
StimAdditiveType.free_water_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='free water control', tag='free_water_control')
StimAdditiveType.friction_reducer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='friction reducer', tag='friction_reducer')
StimAdditiveType.gas = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='gas', tag='gas')
StimAdditiveType.gas_migration_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='gas migration control', tag='gas_migration_control')
StimAdditiveType.gel_stabilizer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='gel stabilizer', tag='gel_stabilizer')
StimAdditiveType.gelling_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='gelling agent', tag='gelling_agent')
StimAdditiveType.H2S_scavenger = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='H2S scavenger', tag='H2S_scavenger')
StimAdditiveType.intensifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='intensifier', tag='intensifier')
StimAdditiveType.iron_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='iron control', tag='iron_control')
StimAdditiveType.lost_circulation_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='lost circulation additive', tag='lost_circulation_additive')
StimAdditiveType.low_fluid_loss_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='low fluid loss control', tag='low_fluid_loss_control')
StimAdditiveType.lubricant = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='lubricant', tag='lubricant')
StimAdditiveType.misc_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='misc additive', tag='misc_additive')
StimAdditiveType.mixing_fluid = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='mixing fluid', tag='mixing_fluid')
StimAdditiveType.mud_removal_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='mud removal additive', tag='mud_removal_additive')
StimAdditiveType.mud_thinner = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='mud thinner', tag='mud_thinner')
StimAdditiveType.mutual_solvent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='mutual solvent', tag='mutual_solvent')
StimAdditiveType.oxydizer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='oxydizer', tag='oxydizer')
StimAdditiveType.oxygen_scavenger = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='oxygen scavenger', tag='oxygen_scavenger')
StimAdditiveType.parafin_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='parafin control', tag='parafin_control')
StimAdditiveType.penetrating_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='penetrating agent', tag='penetrating_agent')
StimAdditiveType.polymer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='polymer', tag='polymer')
StimAdditiveType.proppant_stabilizer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='proppant stabilizer', tag='proppant_stabilizer')
StimAdditiveType.radioactive_tracer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='radioactive tracer', tag='radioactive_tracer')
StimAdditiveType.raw_acid = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='raw acid', tag='raw_acid')
StimAdditiveType.relative_perm_modifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='relative perm modifier', tag='relative_perm_modifier')
StimAdditiveType.retarder = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='retarder', tag='retarder')
StimAdditiveType.salt = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='salt', tag='salt')
StimAdditiveType.sand = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='sand', tag='sand')
StimAdditiveType.sand_control_material = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='sand control material', tag='sand_control_material')
StimAdditiveType.scale_control_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='scale control additive', tag='scale_control_additive')
StimAdditiveType.stabilizer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='stabilizer', tag='stabilizer')
StimAdditiveType.strength_retrogression = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='strength retrogression', tag='strength_retrogression')
StimAdditiveType.sulfide_scavenger = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='sulfide scavenger', tag='sulfide_scavenger')
StimAdditiveType.surfactant = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='surfactant', tag='surfactant')
StimAdditiveType.suspension_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='suspension agent', tag='suspension_agent')
StimAdditiveType.tactifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='tactifier', tag='tactifier')
StimAdditiveType.viscosifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='viscosifier', tag='viscosifier')
StimAdditiveType.water_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='water additive', tag='water_additive')
StimAdditiveType.water_management_material = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='water management material', tag='water_management_material')
StimAdditiveType.pH_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='pH control', tag='pH_control')
StimAdditiveType.unknown = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
StimAdditiveType._InitializeFacetMap(StimAdditiveType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StimAdditiveType', StimAdditiveType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimAnalysisMethod
class StimAnalysisMethod (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The analysis method used for the FET test."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StimAnalysisMethod')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6684, 1)
    _Documentation = 'The analysis method used for the FET test.'
StimAnalysisMethod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimAnalysisMethod, enum_prefix=None)
StimAnalysisMethod.average = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='average', tag='average')
StimAnalysisMethod.delta_pressure_over_g_time = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='delta pressure over g-time', tag='delta_pressure_over_g_time')
StimAnalysisMethod.delta_pressure_over_linear_time = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='delta pressure over linear time', tag='delta_pressure_over_linear_time')
StimAnalysisMethod.delta_pressure_over_radial_time = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='delta pressure over radial time', tag='delta_pressure_over_radial_time')
StimAnalysisMethod.gdk_2_d = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='gdk 2-d', tag='gdk_2_d')
StimAnalysisMethod.horner = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='horner', tag='horner')
StimAnalysisMethod.linear = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='linear', tag='linear')
StimAnalysisMethod.log_log = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='log-log', tag='log_log')
StimAnalysisMethod.nolte = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='nolte', tag='nolte')
StimAnalysisMethod.pdl_coefficient = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='pdl coefficient', tag='pdl_coefficient')
StimAnalysisMethod.perkins_and_kern_2_d = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='perkins and kern 2-d', tag='perkins_and_kern_2_d')
StimAnalysisMethod.radial_2_d = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='radial 2-d', tag='radial_2_d')
StimAnalysisMethod.square_root = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='square root', tag='square_root')
StimAnalysisMethod.third_party_software = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='third-party software', tag='third_party_software')
StimAnalysisMethod.other = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
StimAnalysisMethod.unknown = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
StimAnalysisMethod._InitializeFacetMap(StimAnalysisMethod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StimAnalysisMethod', StimAnalysisMethod)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimFluidSubtype
class StimFluidSubtype (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The fluid sub type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StimFluidSubtype')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6848, 1)
    _Documentation = 'The fluid sub type.'
StimFluidSubtype._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimFluidSubtype, enum_prefix=None)
StimFluidSubtype.acid = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='acid', tag='acid')
StimFluidSubtype.base = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='base', tag='base')
StimFluidSubtype.carbon_dioxide = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='carbon dioxide', tag='carbon_dioxide')
StimFluidSubtype.carbon_dioxide_and_nitrogen = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='carbon dioxide and nitrogen', tag='carbon_dioxide_and_nitrogen')
StimFluidSubtype.carbon_dioxide_and_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='carbon dioxide and water', tag='carbon_dioxide_and_water')
StimFluidSubtype.condensate = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='condensate', tag='condensate')
StimFluidSubtype.cross_linked_gel = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='cross-linked gel', tag='cross_linked_gel')
StimFluidSubtype.crude_oil = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='crude oil', tag='crude_oil')
StimFluidSubtype.diesel = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='diesel', tag='diesel')
StimFluidSubtype.foam = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='foam', tag='foam')
StimFluidSubtype.fracturing_oil = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='fracturing oil', tag='fracturing_oil')
StimFluidSubtype.fresh_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='fresh water', tag='fresh_water')
StimFluidSubtype.gelled_acid = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='gelled acid', tag='gelled_acid')
StimFluidSubtype.gelled_condensate = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='gelled condensate', tag='gelled_condensate')
StimFluidSubtype.gelled_crude = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='gelled crude', tag='gelled_crude')
StimFluidSubtype.gelled_diesel = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='gelled diesel', tag='gelled_diesel')
StimFluidSubtype.gelled_oil = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='gelled oil', tag='gelled_oil')
StimFluidSubtype.gelled_salt_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='gelled salt water', tag='gelled_salt_water')
StimFluidSubtype.hot_condensate = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='hot condensate', tag='hot_condensate')
StimFluidSubtype.hot_fresh_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='hot fresh water', tag='hot_fresh_water')
StimFluidSubtype.hot_oil = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='hot oil', tag='hot_oil')
StimFluidSubtype.hot_salt_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='hot salt water', tag='hot_salt_water')
StimFluidSubtype.hybrid = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='hybrid', tag='hybrid')
StimFluidSubtype.linear_gel = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='linear gel', tag='linear_gel')
StimFluidSubtype.liquefied_petroleum_gas = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='liquefied petroleum gas', tag='liquefied_petroleum_gas')
StimFluidSubtype.nitrogen = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='nitrogen', tag='nitrogen')
StimFluidSubtype.oil = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='oil', tag='oil')
StimFluidSubtype.produced_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='produced water', tag='produced_water')
StimFluidSubtype.salt_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='salt water', tag='salt_water')
StimFluidSubtype.slick_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='slick water', tag='slick_water')
StimFluidSubtype.other = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
StimFluidSubtype._InitializeFacetMap(StimFluidSubtype._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StimFluidSubtype', StimFluidSubtype)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimFluidType
class StimFluidType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The fluid type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StimFluidType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7053, 1)
    _Documentation = 'The fluid type.'
StimFluidType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimFluidType, enum_prefix=None)
StimFluidType.acid_based = StimFluidType._CF_enumeration.addEnumeration(unicode_value='acid-based', tag='acid_based')
StimFluidType.gas = StimFluidType._CF_enumeration.addEnumeration(unicode_value='gas', tag='gas')
StimFluidType.oil_based = StimFluidType._CF_enumeration.addEnumeration(unicode_value='oil-based', tag='oil_based')
StimFluidType.water_based = StimFluidType._CF_enumeration.addEnumeration(unicode_value='water-based', tag='water_based')
StimFluidType._InitializeFacetMap(StimFluidType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StimFluidType', StimFluidType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimProppantType
class StimProppantType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """
				Sized particles mixed with treatment fluid to hold fractures open after a hydraulic fracturing treatment.
				In addition to naturally occurring sand grains, man-made or specially engineered
				proppants, such as "resin-coated" sand or "high-strength" ceramic materials, may also be
				used. Proppant materials are carefully sorted for size and sphericity to provide an efficient conduit for
				production of fluid from the reservoir to the wellbore.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StimProppantType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7089, 1)
    _Documentation = '\n\t\t\t\tSized particles mixed with treatment fluid to hold fractures open after a hydraulic fracturing treatment.\n\t\t\t\tIn addition to naturally occurring sand grains, man-made or specially engineered\n\t\t\t\tproppants, such as "resin-coated" sand or "high-strength" ceramic materials, may also be\n\t\t\t\tused. Proppant materials are carefully sorted for size and sphericity to provide an efficient conduit for\n\t\t\t\tproduction of fluid from the reservoir to the wellbore.\n\t\t\t'
StimProppantType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimProppantType, enum_prefix=None)
StimProppantType.sand = StimProppantType._CF_enumeration.addEnumeration(unicode_value='sand', tag='sand')
StimProppantType.manmade_proppant = StimProppantType._CF_enumeration.addEnumeration(unicode_value='manmade proppant', tag='manmade_proppant')
StimProppantType.unknown = StimProppantType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
StimProppantType._InitializeFacetMap(StimProppantType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StimProppantType', StimProppantType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimStageFlowPathType
class StimStageFlowPathType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The types of flow paths used in a stimulation job."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StimStageFlowPathType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7120, 1)
    _Documentation = 'The types of flow paths used in a stimulation job.'
StimStageFlowPathType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimStageFlowPathType, enum_prefix=None)
StimStageFlowPathType.annulus = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value='annulus', tag='annulus')
StimStageFlowPathType.casing = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value='casing', tag='casing')
StimStageFlowPathType.coiled_tubing = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value='coiled tubing', tag='coiled_tubing')
StimStageFlowPathType.drill_pipe = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value='drill pipe', tag='drill_pipe')
StimStageFlowPathType.open_hole = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value='open hole', tag='open_hole')
StimStageFlowPathType.tubing = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value='tubing', tag='tubing')
StimStageFlowPathType.tubing_and_annulus = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value='tubing and annulus', tag='tubing_and_annulus')
StimStageFlowPathType.unknown = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
StimStageFlowPathType._InitializeFacetMap(StimStageFlowPathType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StimStageFlowPathType', StimStageFlowPathType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimStageType
class StimStageType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of stage for a stimulation job."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StimStageType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7175, 1)
    _Documentation = 'Type of stage for a stimulation job.'
StimStageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimStageType, enum_prefix=None)
StimStageType.acid = StimStageType._CF_enumeration.addEnumeration(unicode_value='acid', tag='acid')
StimStageType.acid_spearhead = StimStageType._CF_enumeration.addEnumeration(unicode_value='acid spearhead', tag='acid_spearhead')
StimStageType.acid_ball_out = StimStageType._CF_enumeration.addEnumeration(unicode_value='acid ball out', tag='acid_ball_out')
StimStageType.acid_breakdown = StimStageType._CF_enumeration.addEnumeration(unicode_value='acid breakdown', tag='acid_breakdown')
StimStageType.ball_out = StimStageType._CF_enumeration.addEnumeration(unicode_value='ball out', tag='ball_out')
StimStageType.breakdown = StimStageType._CF_enumeration.addEnumeration(unicode_value='breakdown', tag='breakdown')
StimStageType.chemical_wash = StimStageType._CF_enumeration.addEnumeration(unicode_value='chemical wash', tag='chemical_wash')
StimStageType.circulate = StimStageType._CF_enumeration.addEnumeration(unicode_value='circulate', tag='circulate')
StimStageType.displacement = StimStageType._CF_enumeration.addEnumeration(unicode_value='displacement', tag='displacement')
StimStageType.diverter = StimStageType._CF_enumeration.addEnumeration(unicode_value='diverter', tag='diverter')
StimStageType.fluid_efficiency_test = StimStageType._CF_enumeration.addEnumeration(unicode_value='fluid efficiency test', tag='fluid_efficiency_test')
StimStageType.flowback = StimStageType._CF_enumeration.addEnumeration(unicode_value='flowback', tag='flowback')
StimStageType.flush = StimStageType._CF_enumeration.addEnumeration(unicode_value='flush', tag='flush')
StimStageType.foamed_acid = StimStageType._CF_enumeration.addEnumeration(unicode_value='foamed acid', tag='foamed_acid')
StimStageType.hydrajet = StimStageType._CF_enumeration.addEnumeration(unicode_value='hydrajet', tag='hydrajet')
StimStageType.load_well = StimStageType._CF_enumeration.addEnumeration(unicode_value='load well', tag='load_well')
StimStageType.load_annulus = StimStageType._CF_enumeration.addEnumeration(unicode_value='load annulus', tag='load_annulus')
StimStageType.overflush = StimStageType._CF_enumeration.addEnumeration(unicode_value='overflush', tag='overflush')
StimStageType.pad = StimStageType._CF_enumeration.addEnumeration(unicode_value='pad', tag='pad')
StimStageType.pump_in = StimStageType._CF_enumeration.addEnumeration(unicode_value='pump-in', tag='pump_in')
StimStageType.pre_Job = StimStageType._CF_enumeration.addEnumeration(unicode_value='pre-Job', tag='pre_Job')
StimStageType.pre_flush = StimStageType._CF_enumeration.addEnumeration(unicode_value='pre-flush', tag='pre_flush')
StimStageType.pre_pad = StimStageType._CF_enumeration.addEnumeration(unicode_value='pre-pad', tag='pre_pad')
StimStageType.shut_in = StimStageType._CF_enumeration.addEnumeration(unicode_value='shut-in', tag='shut_in')
StimStageType.shut_in_for_FET_analysis = StimStageType._CF_enumeration.addEnumeration(unicode_value='shut-in for FET analysis', tag='shut_in_for_FET_analysis')
StimStageType.proppant_laden_fluid = StimStageType._CF_enumeration.addEnumeration(unicode_value='proppant laden fluid', tag='proppant_laden_fluid')
StimStageType.slurry = StimStageType._CF_enumeration.addEnumeration(unicode_value='slurry', tag='slurry')
StimStageType.sand_slug = StimStageType._CF_enumeration.addEnumeration(unicode_value='sand slug', tag='sand_slug')
StimStageType.spacer = StimStageType._CF_enumeration.addEnumeration(unicode_value='spacer', tag='spacer')
StimStageType.spot_acid = StimStageType._CF_enumeration.addEnumeration(unicode_value='spot acid', tag='spot_acid')
StimStageType.step_rate_test = StimStageType._CF_enumeration.addEnumeration(unicode_value='step rate test', tag='step_rate_test')
StimStageType.treatment = StimStageType._CF_enumeration.addEnumeration(unicode_value='treatment', tag='treatment')
StimStageType.other = StimStageType._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
StimStageType.unknown = StimStageType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
StimStageType._InitializeFacetMap(StimStageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StimStageType', StimStageType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}SupportCraft
class SupportCraft (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportCraft')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7365, 1)
    _Documentation = None
SupportCraft._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SupportCraft, enum_prefix=None)
SupportCraft.barge = SupportCraft._CF_enumeration.addEnumeration(unicode_value='barge', tag='barge')
SupportCraft.standby_boat = SupportCraft._CF_enumeration.addEnumeration(unicode_value='standby boat', tag='standby_boat')
SupportCraft.helicopter = SupportCraft._CF_enumeration.addEnumeration(unicode_value='helicopter', tag='helicopter')
SupportCraft.supply_boat = SupportCraft._CF_enumeration.addEnumeration(unicode_value='supply boat', tag='supply_boat')
SupportCraft.truck = SupportCraft._CF_enumeration.addEnumeration(unicode_value='truck', tag='truck')
SupportCraft.crew_vehicle = SupportCraft._CF_enumeration.addEnumeration(unicode_value='crew vehicle', tag='crew_vehicle')
SupportCraft.tug_boat = SupportCraft._CF_enumeration.addEnumeration(unicode_value='tug boat', tag='tug_boat')
SupportCraft.unknown = SupportCraft._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
SupportCraft._InitializeFacetMap(SupportCraft._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SupportCraft', SupportCraft)

# Atomic simple type: {http://www.witsml.org/schemas/1series}SurfEquipType
class SurfEquipType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Surface Equipment Type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SurfEquipType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7412, 1)
    _Documentation = 'Surface Equipment Type.'
SurfEquipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SurfEquipType, enum_prefix=None)
SurfEquipType.IADC = SurfEquipType._CF_enumeration.addEnumeration(unicode_value='IADC', tag='IADC')
SurfEquipType.custom = SurfEquipType._CF_enumeration.addEnumeration(unicode_value='custom', tag='custom')
SurfEquipType.coiled_tubing = SurfEquipType._CF_enumeration.addEnumeration(unicode_value='coiled tubing', tag='coiled_tubing')
SurfEquipType.unknown = SurfEquipType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
SurfEquipType._InitializeFacetMap(SurfEquipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SurfEquipType', SurfEquipType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}SurveyToolOperatingMode
class SurveyToolOperatingMode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The codes for the iscwsa survey tool operating modes."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SurveyToolOperatingMode')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7442, 1)
    _Documentation = 'The codes for the iscwsa survey tool operating modes.'
SurveyToolOperatingMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SurveyToolOperatingMode, enum_prefix=None)
SurveyToolOperatingMode.stationary = SurveyToolOperatingMode._CF_enumeration.addEnumeration(unicode_value='stationary', tag='stationary')
SurveyToolOperatingMode.continuous_XY = SurveyToolOperatingMode._CF_enumeration.addEnumeration(unicode_value='continuous XY', tag='continuous_XY')
SurveyToolOperatingMode.continuous_Z = SurveyToolOperatingMode._CF_enumeration.addEnumeration(unicode_value='continuous Z', tag='continuous_Z')
SurveyToolOperatingMode.continuous_XYZ = SurveyToolOperatingMode._CF_enumeration.addEnumeration(unicode_value='continuous XYZ', tag='continuous_XYZ')
SurveyToolOperatingMode.unknown = SurveyToolOperatingMode._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
SurveyToolOperatingMode._InitializeFacetMap(SurveyToolOperatingMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SurveyToolOperatingMode', SurveyToolOperatingMode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TargetCategory
class TargetCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TargetCategory')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7482, 1)
    _Documentation = None
TargetCategory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetCategory, enum_prefix=None)
TargetCategory.geological = TargetCategory._CF_enumeration.addEnumeration(unicode_value='geological', tag='geological')
TargetCategory.unknown = TargetCategory._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TargetCategory._InitializeFacetMap(TargetCategory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TargetCategory', TargetCategory)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TargetScope
class TargetScope (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of scope of the drilling target. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TargetScope')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7499, 1)
    _Documentation = 'These values represent the type of scope of the drilling target. '
TargetScope._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetScope, enum_prefix=None)
TargetScope.n3D_volume = TargetScope._CF_enumeration.addEnumeration(unicode_value='3D volume', tag='n3D_volume')
TargetScope.ellipsoid = TargetScope._CF_enumeration.addEnumeration(unicode_value='ellipsoid', tag='ellipsoid')
TargetScope.elliptical = TargetScope._CF_enumeration.addEnumeration(unicode_value='elliptical', tag='elliptical')
TargetScope.hardLine = TargetScope._CF_enumeration.addEnumeration(unicode_value='hardLine', tag='hardLine')
TargetScope.irregular = TargetScope._CF_enumeration.addEnumeration(unicode_value='irregular', tag='irregular')
TargetScope.lease_line = TargetScope._CF_enumeration.addEnumeration(unicode_value='lease line', tag='lease_line')
TargetScope.line = TargetScope._CF_enumeration.addEnumeration(unicode_value='line', tag='line')
TargetScope.plane = TargetScope._CF_enumeration.addEnumeration(unicode_value='plane', tag='plane')
TargetScope.point = TargetScope._CF_enumeration.addEnumeration(unicode_value='point', tag='point')
TargetScope.rectangular = TargetScope._CF_enumeration.addEnumeration(unicode_value='rectangular', tag='rectangular')
TargetScope.unknown = TargetScope._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TargetScope._InitializeFacetMap(TargetScope._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TargetScope', TargetScope)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TargetSectionScope
class TargetSectionScope (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of scope of a section that describes a target. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TargetSectionScope')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7565, 1)
    _Documentation = 'These values represent the type of scope of a section that describes a target. '
TargetSectionScope._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetSectionScope, enum_prefix=None)
TargetSectionScope.arc = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value='arc', tag='arc')
TargetSectionScope.line = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value='line', tag='line')
TargetSectionScope.unknown = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TargetSectionScope._InitializeFacetMap(TargetSectionScope._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TargetSectionScope', TargetSectionScope)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TrajStnCalcAlgorithm
class TrajStnCalcAlgorithm (abstractTypeEnum):

    """Trajectory Station Calculation Algorithm.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrajStnCalcAlgorithm')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7590, 1)
    _Documentation = 'Trajectory Station Calculation Algorithm.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
TrajStnCalcAlgorithm._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TrajStnCalcAlgorithm', TrajStnCalcAlgorithm)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TrajStationStatus
class TrajStationStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Trajectory Station Status."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrajStationStatus')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7599, 1)
    _Documentation = 'Trajectory Station Status.'
TrajStationStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TrajStationStatus, enum_prefix=None)
TrajStationStatus.open = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value='open', tag='open')
TrajStationStatus.rejected = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value='rejected', tag='rejected')
TrajStationStatus.position = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value='position', tag='position')
TrajStationStatus.unknown = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TrajStationStatus._InitializeFacetMap(TrajStationStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TrajStationStatus', TrajStationStatus)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TrajStationType
class TrajStationType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a directional survey station. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrajStationType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7634, 1)
    _Documentation = 'These values represent the type of a directional survey station. '
TrajStationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TrajStationType, enum_prefix=None)
TrajStationType.azimuth_on_plane = TrajStationType._CF_enumeration.addEnumeration(unicode_value='azimuth on plane', tag='azimuth_on_plane')
TrajStationType.buildrate_to_delta_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='buildrate to delta-MD', tag='buildrate_to_delta_MD')
TrajStationType.buildrate_to_INCL = TrajStationType._CF_enumeration.addEnumeration(unicode_value='buildrate to INCL', tag='buildrate_to_INCL')
TrajStationType.buildrate_to_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='buildrate to MD', tag='buildrate_to_MD')
TrajStationType.buildrate_and_turnrate_to_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value='buildrate and turnrate to AZI', tag='buildrate_and_turnrate_to_AZI')
TrajStationType.buildrate_and_turnrate_to_delta_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='buildrate and turnrate to delta-MD', tag='buildrate_and_turnrate_to_delta_MD')
TrajStationType.buildrate_and_turnrate_to_INCL = TrajStationType._CF_enumeration.addEnumeration(unicode_value='buildrate and turnrate to INCL', tag='buildrate_and_turnrate_to_INCL')
TrajStationType.buildrate_and_turnrate_to_INCL_and_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value='buildrate and turnrate to INCL and AZI', tag='buildrate_and_turnrate_to_INCL_and_AZI')
TrajStationType.buildrate_and_turnrate_to_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='buildrate and turnrate to MD', tag='buildrate_and_turnrate_to_MD')
TrajStationType.buildrate_and_turnrate_to_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='buildrate and turnrate to TVD', tag='buildrate_and_turnrate_to_TVD')
TrajStationType.buildrate_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='buildrate TVD', tag='buildrate_TVD')
TrajStationType.casing_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='casing MD', tag='casing_MD')
TrajStationType.casing_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='casing TVD', tag='casing_TVD')
TrajStationType.DLS = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS', tag='DLS')
TrajStationType.DLS_to_AZI_and_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS to AZI and MD', tag='DLS_to_AZI_and_MD')
TrajStationType.DLS_to_AZI_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS to AZI-TVD', tag='DLS_to_AZI_TVD')
TrajStationType.DLS_to_INCL = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS to INCL', tag='DLS_to_INCL')
TrajStationType.DLS_to_INCL_and_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS to INCL and AZI', tag='DLS_to_INCL_and_AZI')
TrajStationType.DLS_to_INCL_and_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS to INCL and MD', tag='DLS_to_INCL_and_MD')
TrajStationType.DLS_to_INCL_and_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS to INCL and TVD', tag='DLS_to_INCL_and_TVD')
TrajStationType.DLS_to_NS_EW_and_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS to NS, EW and TVD', tag='DLS_to_NS_EW_and_TVD')
TrajStationType.DLS_and_toolface_to_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS and toolface to AZI', tag='DLS_and_toolface_to_AZI')
TrajStationType.DLS_and_toolface_to_delta_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS and toolface to delta-MD', tag='DLS_and_toolface_to_delta_MD')
TrajStationType.DLS_and_toolface_to_INCL = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS and toolface to INCL', tag='DLS_and_toolface_to_INCL')
TrajStationType.DLS_and_toolface_to_INCL_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS and toolface to INCL-AZI', tag='DLS_and_toolface_to_INCL_AZI')
TrajStationType.DLS_and_toolface_to_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS and toolface to MD', tag='DLS_and_toolface_to_MD')
TrajStationType.DLS_and_toolface_to_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='DLS and toolface to TVD', tag='DLS_and_toolface_to_TVD')
TrajStationType.formation_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='formation MD', tag='formation_MD')
TrajStationType.formation_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='formation TVD', tag='formation_TVD')
TrajStationType.gyro_inertial = TrajStationType._CF_enumeration.addEnumeration(unicode_value='gyro inertial', tag='gyro_inertial')
TrajStationType.gyro_MWD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='gyro MWD', tag='gyro_MWD')
TrajStationType.gyro_north_seeking = TrajStationType._CF_enumeration.addEnumeration(unicode_value='gyro north seeking', tag='gyro_north_seeking')
TrajStationType.hold_to_delta_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='hold to delta-MD', tag='hold_to_delta_MD')
TrajStationType.hold_to_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='hold to MD', tag='hold_to_MD')
TrajStationType.hold_to_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='hold to TVD', tag='hold_to_TVD')
TrajStationType.INCL_AZI_and_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='INCL, AZI and TVD', tag='INCL_AZI_and_TVD')
TrajStationType.magnetic_multi_shot = TrajStationType._CF_enumeration.addEnumeration(unicode_value='magnetic multi-shot', tag='magnetic_multi_shot')
TrajStationType.magnetic_MWD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='magnetic MWD', tag='magnetic_MWD')
TrajStationType.magnetic_single_shot = TrajStationType._CF_enumeration.addEnumeration(unicode_value='magnetic single shot', tag='magnetic_single_shot')
TrajStationType.marker_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='marker MD', tag='marker_MD')
TrajStationType.marker_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='marker TVD', tag='marker_TVD')
TrajStationType.NS_EW_and_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='NS, EW and TVD', tag='NS_EW_and_TVD')
TrajStationType.target_center = TrajStationType._CF_enumeration.addEnumeration(unicode_value='target center', tag='target_center')
TrajStationType.target_offset = TrajStationType._CF_enumeration.addEnumeration(unicode_value='target offset', tag='target_offset')
TrajStationType.tie_in_point = TrajStationType._CF_enumeration.addEnumeration(unicode_value='tie in point', tag='tie_in_point')
TrajStationType.turnrate_to_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value='turnrate to AZI', tag='turnrate_to_AZI')
TrajStationType.turnrate_to_delta_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='turnrate to delta-MD', tag='turnrate_to_delta_MD')
TrajStationType.turnrate_to_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='turnrate to MD', tag='turnrate_to_MD')
TrajStationType.turnrate_to_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value='turnrate to TVD', tag='turnrate_to_TVD')
TrajStationType.unknown = TrajStationType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TrajStationType._InitializeFacetMap(TrajStationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TrajStationType', TrajStationType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TubularAssembly
class TubularAssembly (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TubularAssembly')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7900, 1)
    _Documentation = None
TubularAssembly._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TubularAssembly, enum_prefix=None)
TubularAssembly.drilling = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='drilling', tag='drilling')
TubularAssembly.directional_drilling = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='directional drilling', tag='directional_drilling')
TubularAssembly.fishing = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='fishing', tag='fishing')
TubularAssembly.condition_mud = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='condition mud', tag='condition_mud')
TubularAssembly.tubing_conveyed_logging = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='tubing conveyed logging', tag='tubing_conveyed_logging')
TubularAssembly.cementing = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='cementing', tag='cementing')
TubularAssembly.casing = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='casing', tag='casing')
TubularAssembly.clean_out = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='clean out', tag='clean_out')
TubularAssembly.completion_or_testing = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='completion or testing', tag='completion_or_testing')
TubularAssembly.coring = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='coring', tag='coring')
TubularAssembly.hole_opening_or_underreaming = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='hole opening or underreaming', tag='hole_opening_or_underreaming')
TubularAssembly.milling_or_dressing_or_cutting = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='milling or dressing or cutting', tag='milling_or_dressing_or_cutting')
TubularAssembly.wiper_or_check_or_reaming = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='wiper or check or reaming', tag='wiper_or_check_or_reaming')
TubularAssembly.unknown = TubularAssembly._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TubularAssembly._InitializeFacetMap(TubularAssembly._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TubularAssembly', TubularAssembly)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TubularComponent
class TubularComponent (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TubularComponent')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7977, 1)
    _Documentation = None
TubularComponent._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TubularComponent, enum_prefix=None)
TubularComponent.non_magnetic_stabilizer = TubularComponent._CF_enumeration.addEnumeration(unicode_value='non-magnetic stabilizer', tag='non_magnetic_stabilizer')
TubularComponent.non_magnetic_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value='non-magnetic collar', tag='non_magnetic_collar')
TubularComponent.stabilizer = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stabilizer', tag='stabilizer')
TubularComponent.adjustable_kickoff = TubularComponent._CF_enumeration.addEnumeration(unicode_value='adjustable kickoff', tag='adjustable_kickoff')
TubularComponent.accelerator = TubularComponent._CF_enumeration.addEnumeration(unicode_value='accelerator', tag='accelerator')
TubularComponent.rotary_steering_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value='rotary steering tool', tag='rotary_steering_tool')
TubularComponent.sub_bar_catcher = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-bar catcher', tag='sub_bar_catcher')
TubularComponent.sub_bent = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-bent', tag='sub_bent')
TubularComponent.bit_core_diamond = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bit core diamond', tag='bit_core_diamond')
TubularComponent.bit_core_PDC = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bit core PDC', tag='bit_core_PDC')
TubularComponent.bit_diamond_fixed_cut = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bit diamond fixed cut', tag='bit_diamond_fixed_cut')
TubularComponent.bit_insert_roller_cone = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bit insert roller cone', tag='bit_insert_roller_cone')
TubularComponent.bit_mill_tooth_roller_cone = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bit mill tooth roller cone', tag='bit_mill_tooth_roller_cone')
TubularComponent.bit_PDC_fixed_cutter = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bit PDC fixed cutter', tag='bit_PDC_fixed_cutter')
TubularComponent.sub_bit = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-bit', tag='sub_bit')
TubularComponent.bridge_plug = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bridge plug', tag='bridge_plug')
TubularComponent.bullnose = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bullnose', tag='bullnose')
TubularComponent.bull_plug = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bull plug', tag='bull_plug')
TubularComponent.sub_bumper = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-bumper', tag='sub_bumper')
TubularComponent.casing = TubularComponent._CF_enumeration.addEnumeration(unicode_value='casing', tag='casing')
TubularComponent.casing_cutter = TubularComponent._CF_enumeration.addEnumeration(unicode_value='casing cutter', tag='casing_cutter')
TubularComponent.hanger_casing_subsea = TubularComponent._CF_enumeration.addEnumeration(unicode_value='hanger casing subsea', tag='hanger_casing_subsea')
TubularComponent.hanger_casing_surface = TubularComponent._CF_enumeration.addEnumeration(unicode_value='hanger casing surface', tag='hanger_casing_surface')
TubularComponent.casing_head = TubularComponent._CF_enumeration.addEnumeration(unicode_value='casing head', tag='casing_head')
TubularComponent.catch_assembly = TubularComponent._CF_enumeration.addEnumeration(unicode_value='catch assembly', tag='catch_assembly')
TubularComponent.sub_catcher = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-catcher', tag='sub_catcher')
TubularComponent.sub_circulation = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-circulation', tag='sub_circulation')
TubularComponent.coiled_tubing_in_hole = TubularComponent._CF_enumeration.addEnumeration(unicode_value='coiled tubing in hole', tag='coiled_tubing_in_hole')
TubularComponent.coiled_tubing_on_coil = TubularComponent._CF_enumeration.addEnumeration(unicode_value='coiled tubing on coil', tag='coiled_tubing_on_coil')
TubularComponent.drill_pipe_compressive = TubularComponent._CF_enumeration.addEnumeration(unicode_value='drill pipe compressive', tag='drill_pipe_compressive')
TubularComponent.sub_cone = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-cone', tag='sub_cone')
TubularComponent.core_barrel = TubularComponent._CF_enumeration.addEnumeration(unicode_value='core barrel', tag='core_barrel')
TubularComponent.core_orientation_barrel = TubularComponent._CF_enumeration.addEnumeration(unicode_value='core orientation barrel', tag='core_orientation_barrel')
TubularComponent.sub_crossover = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-crossover', tag='sub_crossover')
TubularComponent.casing_crossover = TubularComponent._CF_enumeration.addEnumeration(unicode_value='casing crossover', tag='casing_crossover')
TubularComponent.sub_dart = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-dart', tag='sub_dart')
TubularComponent.die_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value='die collar', tag='die_collar')
TubularComponent.die_collar_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value='die collar LH', tag='die_collar_LH')
TubularComponent.directional_guidance_system = TubularComponent._CF_enumeration.addEnumeration(unicode_value='directional guidance system', tag='directional_guidance_system')
TubularComponent.drill_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value='drill collar', tag='drill_collar')
TubularComponent.drill_pipe = TubularComponent._CF_enumeration.addEnumeration(unicode_value='drill pipe', tag='drill_pipe')
TubularComponent.drill_pipe_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value='drill pipe LH', tag='drill_pipe_LH')
TubularComponent.drill_stem_test_BHA = TubularComponent._CF_enumeration.addEnumeration(unicode_value='drill stem test BHA', tag='drill_stem_test_BHA')
TubularComponent.drive_pipe = TubularComponent._CF_enumeration.addEnumeration(unicode_value='drive pipe', tag='drive_pipe')
TubularComponent.dual_catch_assembly = TubularComponent._CF_enumeration.addEnumeration(unicode_value='dual catch assembly', tag='dual_catch_assembly')
TubularComponent.extension_bowl_overshot = TubularComponent._CF_enumeration.addEnumeration(unicode_value='extension bowl overshot', tag='extension_bowl_overshot')
TubularComponent.extension_sub_overshot = TubularComponent._CF_enumeration.addEnumeration(unicode_value='extension sub-overshot', tag='extension_sub_overshot')
TubularComponent.float_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value='float collar', tag='float_collar')
TubularComponent.float_shoe = TubularComponent._CF_enumeration.addEnumeration(unicode_value='float shoe', tag='float_shoe')
TubularComponent.sub_float = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-float', tag='sub_float')
TubularComponent.flow_head = TubularComponent._CF_enumeration.addEnumeration(unicode_value='flow head', tag='flow_head')
TubularComponent.guide_shoe = TubularComponent._CF_enumeration.addEnumeration(unicode_value='guide shoe', tag='guide_shoe')
TubularComponent.MWD_hang_off_sub = TubularComponent._CF_enumeration.addEnumeration(unicode_value='MWD hang off sub', tag='MWD_hang_off_sub')
TubularComponent.heavy_weight_drill_pipe = TubularComponent._CF_enumeration.addEnumeration(unicode_value='heavy weight drill pipe', tag='heavy_weight_drill_pipe')
TubularComponent.heavy_weight_drill_pipe_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value='heavy weight drill pipe LH', tag='heavy_weight_drill_pipe_LH')
TubularComponent.riser_high_pressure = TubularComponent._CF_enumeration.addEnumeration(unicode_value='riser high pressure', tag='riser_high_pressure')
TubularComponent.bit_hole_opener = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bit hole opener', tag='bit_hole_opener')
TubularComponent.casing_inflatable_packer = TubularComponent._CF_enumeration.addEnumeration(unicode_value='casing inflatable packer', tag='casing_inflatable_packer')
TubularComponent.motor_instrumented = TubularComponent._CF_enumeration.addEnumeration(unicode_value='motor instrumented', tag='motor_instrumented')
TubularComponent.jar = TubularComponent._CF_enumeration.addEnumeration(unicode_value='jar', tag='jar')
TubularComponent.sub_jetting = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-jetting', tag='sub_jetting')
TubularComponent.junk_basket = TubularComponent._CF_enumeration.addEnumeration(unicode_value='junk basket', tag='junk_basket')
TubularComponent.junk_basket_reverse_circulation = TubularComponent._CF_enumeration.addEnumeration(unicode_value='junk basket reverse circulation', tag='junk_basket_reverse_circulation')
TubularComponent.sub_junk = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-junk', tag='sub_junk')
TubularComponent.kelly = TubularComponent._CF_enumeration.addEnumeration(unicode_value='kelly', tag='kelly')
TubularComponent.keyseat_wiper_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value='keyseat wiper tool', tag='keyseat_wiper_tool')
TubularComponent.landing_float_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value='landing float collar', tag='landing_float_collar')
TubularComponent.lead_impression_block = TubularComponent._CF_enumeration.addEnumeration(unicode_value='lead impression block', tag='lead_impression_block')
TubularComponent.liner = TubularComponent._CF_enumeration.addEnumeration(unicode_value='liner', tag='liner')
TubularComponent.hanger_liner = TubularComponent._CF_enumeration.addEnumeration(unicode_value='hanger liner', tag='hanger_liner')
TubularComponent.magnet = TubularComponent._CF_enumeration.addEnumeration(unicode_value='magnet', tag='magnet')
TubularComponent.riser_marine = TubularComponent._CF_enumeration.addEnumeration(unicode_value='riser marine', tag='riser_marine')
TubularComponent.mill_dress = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill dress', tag='mill_dress')
TubularComponent.mill_flat_bottom = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill flat bottom', tag='mill_flat_bottom')
TubularComponent.mill_hollow = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill hollow', tag='mill_hollow')
TubularComponent.mill_polish = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill polish', tag='mill_polish')
TubularComponent.mill_section = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill section', tag='mill_section')
TubularComponent.mill_taper = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill taper', tag='mill_taper')
TubularComponent.mill_washover = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill washover', tag='mill_washover')
TubularComponent.mill_packer_picker_assembly = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill packer picker assembly', tag='mill_packer_picker_assembly')
TubularComponent.millout_extension = TubularComponent._CF_enumeration.addEnumeration(unicode_value='millout extension', tag='millout_extension')
TubularComponent.multilateral_hanger_running_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value='multilateral hanger running tool', tag='multilateral_hanger_running_tool')
TubularComponent.hanger_mud_line = TubularComponent._CF_enumeration.addEnumeration(unicode_value='hanger mud line', tag='hanger_mud_line')
TubularComponent.motor = TubularComponent._CF_enumeration.addEnumeration(unicode_value='motor', tag='motor')
TubularComponent.mule_shoe = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mule shoe', tag='mule_shoe')
TubularComponent.logging_while_drilling_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value='logging while drilling tool', tag='logging_while_drilling_tool')
TubularComponent.stabilizer_near_bit_roller_reamer = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stabilizer near bit roller reamer', tag='stabilizer_near_bit_roller_reamer')
TubularComponent.stabilizer_near_bit = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stabilizer near bit', tag='stabilizer_near_bit')
TubularComponent.stabilizer_non_rotating = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stabilizer non-rotating', tag='stabilizer_non_rotating')
TubularComponent.sub_orienting = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-orienting', tag='sub_orienting')
TubularComponent.other = TubularComponent._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
TubularComponent.overshot = TubularComponent._CF_enumeration.addEnumeration(unicode_value='overshot', tag='overshot')
TubularComponent.overshot_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value='overshot LH', tag='overshot_LH')
TubularComponent.oversize_lip_guide_overshot = TubularComponent._CF_enumeration.addEnumeration(unicode_value='oversize lip guide overshot', tag='oversize_lip_guide_overshot')
TubularComponent.packer = TubularComponent._CF_enumeration.addEnumeration(unicode_value='packer', tag='packer')
TubularComponent.polished_bore_receptacle = TubularComponent._CF_enumeration.addEnumeration(unicode_value='polished bore receptacle', tag='polished_bore_receptacle')
TubularComponent.mill_pilot = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill pilot', tag='mill_pilot')
TubularComponent.pipe_cutter = TubularComponent._CF_enumeration.addEnumeration(unicode_value='pipe cutter', tag='pipe_cutter')
TubularComponent.ported_stinger = TubularComponent._CF_enumeration.addEnumeration(unicode_value='ported stinger', tag='ported_stinger')
TubularComponent.sub_ported = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-ported', tag='sub_ported')
TubularComponent.prepacked_screens = TubularComponent._CF_enumeration.addEnumeration(unicode_value='prepacked screens', tag='prepacked_screens')
TubularComponent.sub_pressure_relief = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-pressure relief', tag='sub_pressure_relief')
TubularComponent.riser_production = TubularComponent._CF_enumeration.addEnumeration(unicode_value='riser production', tag='riser_production')
TubularComponent.MWD_pulser = TubularComponent._CF_enumeration.addEnumeration(unicode_value='MWD pulser', tag='MWD_pulser')
TubularComponent.sub_pump_out = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-pump out', tag='sub_pump_out')
TubularComponent.sub_restrictor = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-restrictor', tag='sub_restrictor')
TubularComponent.packer_retrieve_TT_squeeze = TubularComponent._CF_enumeration.addEnumeration(unicode_value='packer retrieve TT squeeze', tag='packer_retrieve_TT_squeeze')
TubularComponent.reversing_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value='reversing tool', tag='reversing_tool')
TubularComponent.stabilizer_string_roller_reamer = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stabilizer string roller reamer', tag='stabilizer_string_roller_reamer')
TubularComponent.packer_RTTS = TubularComponent._CF_enumeration.addEnumeration(unicode_value='packer RTTS', tag='packer_RTTS')
TubularComponent.running_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value='running tool', tag='running_tool')
TubularComponent.safety_joint = TubularComponent._CF_enumeration.addEnumeration(unicode_value='safety joint', tag='safety_joint')
TubularComponent.safety_joint_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value='safety joint LH', tag='safety_joint_LH')
TubularComponent.sub_saver = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-saver', tag='sub_saver')
TubularComponent.scab_liner_bit_guide = TubularComponent._CF_enumeration.addEnumeration(unicode_value='scab liner bit guide', tag='scab_liner_bit_guide')
TubularComponent.scraper = TubularComponent._CF_enumeration.addEnumeration(unicode_value='scraper', tag='scraper')
TubularComponent.scratchers = TubularComponent._CF_enumeration.addEnumeration(unicode_value='scratchers', tag='scratchers')
TubularComponent.casing_shoe_screw_in = TubularComponent._CF_enumeration.addEnumeration(unicode_value='casing shoe screw-in', tag='casing_shoe_screw_in')
TubularComponent.sub_shock = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-shock', tag='sub_shock')
TubularComponent.drill_collar_short = TubularComponent._CF_enumeration.addEnumeration(unicode_value='drill collar short', tag='drill_collar_short')
TubularComponent.sub_side_entry = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-side entry', tag='sub_side_entry')
TubularComponent.slotted_liner = TubularComponent._CF_enumeration.addEnumeration(unicode_value='slotted liner', tag='slotted_liner')
TubularComponent.spear = TubularComponent._CF_enumeration.addEnumeration(unicode_value='spear', tag='spear')
TubularComponent.stage_cement_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stage cement collar', tag='stage_cement_collar')
TubularComponent.motor_steerable = TubularComponent._CF_enumeration.addEnumeration(unicode_value='motor steerable', tag='motor_steerable')
TubularComponent.packer_storm_valve_RTTS = TubularComponent._CF_enumeration.addEnumeration(unicode_value='packer storm valve RTTS', tag='packer_storm_valve_RTTS')
TubularComponent.stabilizer_string = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stabilizer string', tag='stabilizer_string')
TubularComponent.surface_pipe = TubularComponent._CF_enumeration.addEnumeration(unicode_value='surface pipe', tag='surface_pipe')
TubularComponent.taper_tap = TubularComponent._CF_enumeration.addEnumeration(unicode_value='taper tap', tag='taper_tap')
TubularComponent.taper_tap_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value='taper tap LH', tag='taper_tap_LH')
TubularComponent.tubing_conveyed_perforating_gun = TubularComponent._CF_enumeration.addEnumeration(unicode_value='tubing-conveyed perforating gun', tag='tubing_conveyed_perforating_gun')
TubularComponent.thruster = TubularComponent._CF_enumeration.addEnumeration(unicode_value='thruster', tag='thruster')
TubularComponent.tieback_polished_bore_receptacle = TubularComponent._CF_enumeration.addEnumeration(unicode_value='tieback polished bore receptacle', tag='tieback_polished_bore_receptacle')
TubularComponent.tieback_stinger = TubularComponent._CF_enumeration.addEnumeration(unicode_value='tieback stinger', tag='tieback_stinger')
TubularComponent.tubing = TubularComponent._CF_enumeration.addEnumeration(unicode_value='tubing', tag='tubing')
TubularComponent.hanger_tubing = TubularComponent._CF_enumeration.addEnumeration(unicode_value='hanger tubing', tag='hanger_tubing')
TubularComponent.turbine = TubularComponent._CF_enumeration.addEnumeration(unicode_value='turbine', tag='turbine')
TubularComponent.bit_under_reamer = TubularComponent._CF_enumeration.addEnumeration(unicode_value='bit under reamer', tag='bit_under_reamer')
TubularComponent.stabilizer_variable_blade = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stabilizer variable blade', tag='stabilizer_variable_blade')
TubularComponent.washover_pipe = TubularComponent._CF_enumeration.addEnumeration(unicode_value='washover pipe', tag='washover_pipe')
TubularComponent.mill_watermelon = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill watermelon', tag='mill_watermelon')
TubularComponent.whipstock = TubularComponent._CF_enumeration.addEnumeration(unicode_value='whipstock', tag='whipstock')
TubularComponent.whipstock_anchor = TubularComponent._CF_enumeration.addEnumeration(unicode_value='whipstock anchor', tag='whipstock_anchor')
TubularComponent.stabilizer_turbo_back = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stabilizer turbo back', tag='stabilizer_turbo_back')
TubularComponent.stabilizer_inline = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stabilizer inline', tag='stabilizer_inline')
TubularComponent.stabilizer_steerable = TubularComponent._CF_enumeration.addEnumeration(unicode_value='stabilizer steerable', tag='stabilizer_steerable')
TubularComponent.sub_stop = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-stop', tag='sub_stop')
TubularComponent.sub_filter = TubularComponent._CF_enumeration.addEnumeration(unicode_value='sub-filter', tag='sub_filter')
TubularComponent.mill_casing_cutting = TubularComponent._CF_enumeration.addEnumeration(unicode_value='mill casing cutting', tag='mill_casing_cutting')
TubularComponent.reamer = TubularComponent._CF_enumeration.addEnumeration(unicode_value='reamer', tag='reamer')
TubularComponent.unknown = TubularComponent._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TubularComponent._InitializeFacetMap(TubularComponent._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TubularComponent', TubularComponent)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TypeSurveyTool
class TypeSurveyTool (abstractTypeEnum):

    """Type of direcional survey tool; a very generic classification.
			The list of standard values is contained in the WITSML enumValues.xml file."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TypeSurveyTool')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 8804, 1)
    _Documentation = 'Type of direcional survey tool; a very generic classification.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file.'
TypeSurveyTool._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TypeSurveyTool', TypeSurveyTool)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellControlIncidentType
class WellControlIncidentType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellControlIncidentType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 8813, 1)
    _Documentation = ''
WellControlIncidentType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellControlIncidentType, enum_prefix=None)
WellControlIncidentType.shallow_gas_kick = WellControlIncidentType._CF_enumeration.addEnumeration(unicode_value='shallow gas kick', tag='shallow_gas_kick')
WellControlIncidentType.water_kick = WellControlIncidentType._CF_enumeration.addEnumeration(unicode_value='water kick', tag='water_kick')
WellControlIncidentType.oil_kick = WellControlIncidentType._CF_enumeration.addEnumeration(unicode_value='oil kick', tag='oil_kick')
WellControlIncidentType.gas_kick = WellControlIncidentType._CF_enumeration.addEnumeration(unicode_value='gas kick', tag='gas_kick')
WellControlIncidentType.unknown = WellControlIncidentType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellControlIncidentType._InitializeFacetMap(WellControlIncidentType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellControlIncidentType', WellControlIncidentType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellDirection
class WellDirection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The direction of flow of the fluids in a well facility
			(generally, injected or produced, or some combination)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellDirection')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 8852, 1)
    _Documentation = 'The direction of flow of the fluids in a well facility\n\t\t\t(generally, injected or produced, or some combination).'
WellDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellDirection, enum_prefix=None)
WellDirection.huff_n_puff = WellDirection._CF_enumeration.addEnumeration(unicode_value='huff-n-puff', tag='huff_n_puff')
WellDirection.injector = WellDirection._CF_enumeration.addEnumeration(unicode_value='injector', tag='injector')
WellDirection.producer = WellDirection._CF_enumeration.addEnumeration(unicode_value='producer', tag='producer')
WellDirection.uncertain = WellDirection._CF_enumeration.addEnumeration(unicode_value='uncertain', tag='uncertain')
WellDirection.unknown = WellDirection._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellDirection._InitializeFacetMap(WellDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellDirection', WellDirection)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellFluid
class WellFluid (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The type of fluid being produced from or injected 
			into a well facility."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellFluid')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 8893, 1)
    _Documentation = 'The type of fluid being produced from or injected \n\t\t\tinto a well facility.'
WellFluid._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellFluid, enum_prefix=None)
WellFluid.air = WellFluid._CF_enumeration.addEnumeration(unicode_value='air', tag='air')
WellFluid.condensate = WellFluid._CF_enumeration.addEnumeration(unicode_value='condensate', tag='condensate')
WellFluid.dry = WellFluid._CF_enumeration.addEnumeration(unicode_value='dry', tag='dry')
WellFluid.gas = WellFluid._CF_enumeration.addEnumeration(unicode_value='gas', tag='gas')
WellFluid.gas_water = WellFluid._CF_enumeration.addEnumeration(unicode_value='gas-water', tag='gas_water')
WellFluid.non_HC_gas = WellFluid._CF_enumeration.addEnumeration(unicode_value='non HC gas', tag='non_HC_gas')
WellFluid.non_HC_gas____CO2 = WellFluid._CF_enumeration.addEnumeration(unicode_value='non HC gas -- CO2', tag='non_HC_gas____CO2')
WellFluid.oil = WellFluid._CF_enumeration.addEnumeration(unicode_value='oil', tag='oil')
WellFluid.oil_gas = WellFluid._CF_enumeration.addEnumeration(unicode_value='oil-gas', tag='oil_gas')
WellFluid.oil_water = WellFluid._CF_enumeration.addEnumeration(unicode_value='oil-water', tag='oil_water')
WellFluid.steam = WellFluid._CF_enumeration.addEnumeration(unicode_value='steam', tag='steam')
WellFluid.water = WellFluid._CF_enumeration.addEnumeration(unicode_value='water', tag='water')
WellFluid.water____brine = WellFluid._CF_enumeration.addEnumeration(unicode_value='water -- brine', tag='water____brine')
WellFluid.water____fresh_water = WellFluid._CF_enumeration.addEnumeration(unicode_value='water -- fresh water', tag='water____fresh_water')
WellFluid.unknown = WellFluid._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellFluid._InitializeFacetMap(WellFluid._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellFluid', WellFluid)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellKillingProcedureType
class WellKillingProcedureType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellKillingProcedureType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9010, 1)
    _Documentation = ''
WellKillingProcedureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellKillingProcedureType, enum_prefix=None)
WellKillingProcedureType.drillers_method = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value='drillers method', tag='drillers_method')
WellKillingProcedureType.wait_and_weight = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value='wait and weight', tag='wait_and_weight')
WellKillingProcedureType.bullheading = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value='bullheading', tag='bullheading')
WellKillingProcedureType.lubricate_and_bleed = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value='lubricate and bleed', tag='lubricate_and_bleed')
WellKillingProcedureType.forward_circulation = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value='forward circulation', tag='forward_circulation')
WellKillingProcedureType.reverse_circulation = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value='reverse circulation', tag='reverse_circulation')
WellKillingProcedureType.unknown = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellKillingProcedureType._InitializeFacetMap(WellKillingProcedureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellKillingProcedureType', WellKillingProcedureType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellNamingSystem
class WellNamingSystem (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The types of well/wellbore naming systems."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellNamingSystem')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9070, 1)
    _Documentation = 'The types of well/wellbore naming systems.'
WellNamingSystem._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellNamingSystem, enum_prefix=None)
WellNamingSystem.DTI = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value='DTI', tag='DTI')
WellNamingSystem.API = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value='API', tag='API')
WellNamingSystem.NPD_code = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value='NPD code', tag='NPD_code')
WellNamingSystem.NPD_number = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value='NPD number', tag='NPD_number')
WellNamingSystem.local_field = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value='local field', tag='local_field')
WellNamingSystem.prospect = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value='prospect', tag='prospect')
WellNamingSystem.unknown = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellNamingSystem._InitializeFacetMap(WellNamingSystem._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellNamingSystem', WellNamingSystem)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellTestType
class WellTestType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellTestType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9116, 1)
    _Documentation = ''
WellTestType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellTestType, enum_prefix=None)
WellTestType.drill_stem_test = WellTestType._CF_enumeration.addEnumeration(unicode_value='drill stem test', tag='drill_stem_test')
WellTestType.production_test = WellTestType._CF_enumeration.addEnumeration(unicode_value='production test', tag='production_test')
WellTestType.unknown = WellTestType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellTestType._InitializeFacetMap(WellTestType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellTestType', WellTestType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellboreShape
class WellboreShape (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the classification of a wellbore 
			based on its shape. The source of the values and the descriptions is the 
			POSC V2.2 "facility class" standard instance values in classification system 
			"POSC wellbore trajectory shape". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellboreShape')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9144, 1)
    _Documentation = 'These values represent the classification of a wellbore \n\t\t\tbased on its shape. The source of the values and the descriptions is the \n\t\t\tPOSC V2.2 "facility class" standard instance values in classification system \n\t\t\t"POSC wellbore trajectory shape". '
WellboreShape._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellboreShape, enum_prefix=None)
WellboreShape.build_and_hold = WellboreShape._CF_enumeration.addEnumeration(unicode_value='build and hold', tag='build_and_hold')
WellboreShape.deviated = WellboreShape._CF_enumeration.addEnumeration(unicode_value='deviated', tag='deviated')
WellboreShape.double_kickoff = WellboreShape._CF_enumeration.addEnumeration(unicode_value='double kickoff', tag='double_kickoff')
WellboreShape.horizontal = WellboreShape._CF_enumeration.addEnumeration(unicode_value='horizontal', tag='horizontal')
WellboreShape.S_shaped = WellboreShape._CF_enumeration.addEnumeration(unicode_value='S-shaped', tag='S_shaped')
WellboreShape.vertical = WellboreShape._CF_enumeration.addEnumeration(unicode_value='vertical', tag='vertical')
WellboreShape.unknown = WellboreShape._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellboreShape._InitializeFacetMap(WellboreShape._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellboreShape', WellboreShape)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellboreType
class WellboreType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The classification of a wellbore with respect to its parent 
			well/wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellboreType')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9200, 1)
    _Documentation = 'The classification of a wellbore with respect to its parent \n\t\t\twell/wellbore.'
WellboreType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellboreType, enum_prefix=None)
WellboreType.bypass = WellboreType._CF_enumeration.addEnumeration(unicode_value='bypass', tag='bypass')
WellboreType.initial = WellboreType._CF_enumeration.addEnumeration(unicode_value='initial', tag='initial')
WellboreType.redrill = WellboreType._CF_enumeration.addEnumeration(unicode_value='redrill', tag='redrill')
WellboreType.reentry = WellboreType._CF_enumeration.addEnumeration(unicode_value='reentry', tag='reentry')
WellboreType.respud = WellboreType._CF_enumeration.addEnumeration(unicode_value='respud', tag='respud')
WellboreType.sidetrack = WellboreType._CF_enumeration.addEnumeration(unicode_value='sidetrack', tag='sidetrack')
WellboreType.unknown = WellboreType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellboreType._InitializeFacetMap(WellboreType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellboreType', WellboreType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellPurpose
class WellPurpose (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the classification of a well or 
			wellbore by the purpose for which it was initially drilled."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellPurpose')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9256, 1)
    _Documentation = 'These values represent the classification of a well or \n\t\t\twellbore by the purpose for which it was initially drilled.'
WellPurpose._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellPurpose, enum_prefix=None)
WellPurpose.appraisal = WellPurpose._CF_enumeration.addEnumeration(unicode_value='appraisal', tag='appraisal')
WellPurpose.appraisal____confirmation_appraisal = WellPurpose._CF_enumeration.addEnumeration(unicode_value='appraisal -- confirmation appraisal', tag='appraisal____confirmation_appraisal')
WellPurpose.appraisal____exploratory_appraisal = WellPurpose._CF_enumeration.addEnumeration(unicode_value='appraisal -- exploratory appraisal', tag='appraisal____exploratory_appraisal')
WellPurpose.exploration = WellPurpose._CF_enumeration.addEnumeration(unicode_value='exploration', tag='exploration')
WellPurpose.exploration____deeper_pool_wildcat = WellPurpose._CF_enumeration.addEnumeration(unicode_value='exploration -- deeper-pool wildcat', tag='exploration____deeper_pool_wildcat')
WellPurpose.exploration____new_field_wildcat = WellPurpose._CF_enumeration.addEnumeration(unicode_value='exploration -- new-field wildcat', tag='exploration____new_field_wildcat')
WellPurpose.exploration____new_pool_wildcat = WellPurpose._CF_enumeration.addEnumeration(unicode_value='exploration -- new-pool wildcat', tag='exploration____new_pool_wildcat')
WellPurpose.exploration____outpost_wildcat = WellPurpose._CF_enumeration.addEnumeration(unicode_value='exploration -- outpost wildcat', tag='exploration____outpost_wildcat')
WellPurpose.exploration____shallower_pool_wildcat = WellPurpose._CF_enumeration.addEnumeration(unicode_value='exploration -- shallower-pool wildcat', tag='exploration____shallower_pool_wildcat')
WellPurpose.development = WellPurpose._CF_enumeration.addEnumeration(unicode_value='development', tag='development')
WellPurpose.development____infill_development = WellPurpose._CF_enumeration.addEnumeration(unicode_value='development -- infill development', tag='development____infill_development')
WellPurpose.development____injector = WellPurpose._CF_enumeration.addEnumeration(unicode_value='development -- injector', tag='development____injector')
WellPurpose.development____producer = WellPurpose._CF_enumeration.addEnumeration(unicode_value='development -- producer', tag='development____producer')
WellPurpose.fluid_storage = WellPurpose._CF_enumeration.addEnumeration(unicode_value='fluid storage', tag='fluid_storage')
WellPurpose.fluid_storage____gas_storage = WellPurpose._CF_enumeration.addEnumeration(unicode_value='fluid storage -- gas storage', tag='fluid_storage____gas_storage')
WellPurpose.general_srvc = WellPurpose._CF_enumeration.addEnumeration(unicode_value='general srvc', tag='general_srvc')
WellPurpose.general_srvc____borehole_re_acquisition = WellPurpose._CF_enumeration.addEnumeration(unicode_value='general srvc -- borehole re-acquisition', tag='general_srvc____borehole_re_acquisition')
WellPurpose.general_srvc____observation = WellPurpose._CF_enumeration.addEnumeration(unicode_value='general srvc -- observation', tag='general_srvc____observation')
WellPurpose.general_srvc____relief = WellPurpose._CF_enumeration.addEnumeration(unicode_value='general srvc -- relief', tag='general_srvc____relief')
WellPurpose.general_srvc____research = WellPurpose._CF_enumeration.addEnumeration(unicode_value='general srvc -- research', tag='general_srvc____research')
WellPurpose.general_srvc____research____drill_test = WellPurpose._CF_enumeration.addEnumeration(unicode_value='general srvc -- research -- drill test', tag='general_srvc____research____drill_test')
WellPurpose.general_srvc____research____strat_test = WellPurpose._CF_enumeration.addEnumeration(unicode_value='general srvc -- research -- strat test', tag='general_srvc____research____strat_test')
WellPurpose.general_srvc____waste_disposal = WellPurpose._CF_enumeration.addEnumeration(unicode_value='general srvc -- waste disposal', tag='general_srvc____waste_disposal')
WellPurpose.mineral = WellPurpose._CF_enumeration.addEnumeration(unicode_value='mineral', tag='mineral')
WellPurpose.unknown = WellPurpose._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellPurpose._InitializeFacetMap(WellPurpose._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellPurpose', WellPurpose)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellStatus
class WellStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the status of a well or wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellStatus')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9392, 1)
    _Documentation = 'These values represent the status of a well or wellbore.'
WellStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellStatus, enum_prefix=None)
WellStatus.abandoned = WellStatus._CF_enumeration.addEnumeration(unicode_value='abandoned', tag='abandoned')
WellStatus.active = WellStatus._CF_enumeration.addEnumeration(unicode_value='active', tag='active')
WellStatus.active____injecting = WellStatus._CF_enumeration.addEnumeration(unicode_value='active -- injecting', tag='active____injecting')
WellStatus.active____producing = WellStatus._CF_enumeration.addEnumeration(unicode_value='active -- producing', tag='active____producing')
WellStatus.completed = WellStatus._CF_enumeration.addEnumeration(unicode_value='completed', tag='completed')
WellStatus.drilling = WellStatus._CF_enumeration.addEnumeration(unicode_value='drilling', tag='drilling')
WellStatus.partially_plugged = WellStatus._CF_enumeration.addEnumeration(unicode_value='partially plugged', tag='partially_plugged')
WellStatus.permitted = WellStatus._CF_enumeration.addEnumeration(unicode_value='permitted', tag='permitted')
WellStatus.plugged_and_abandoned = WellStatus._CF_enumeration.addEnumeration(unicode_value='plugged and abandoned', tag='plugged_and_abandoned')
WellStatus.proposed = WellStatus._CF_enumeration.addEnumeration(unicode_value='proposed', tag='proposed')
WellStatus.sold = WellStatus._CF_enumeration.addEnumeration(unicode_value='sold', tag='sold')
WellStatus.suspended = WellStatus._CF_enumeration.addEnumeration(unicode_value='suspended', tag='suspended')
WellStatus.temporarily_abandoned = WellStatus._CF_enumeration.addEnumeration(unicode_value='temporarily abandoned', tag='temporarily_abandoned')
WellStatus.testing = WellStatus._CF_enumeration.addEnumeration(unicode_value='testing', tag='testing')
WellStatus.tight = WellStatus._CF_enumeration.addEnumeration(unicode_value='tight', tag='tight')
WellStatus.working_over = WellStatus._CF_enumeration.addEnumeration(unicode_value='working over', tag='working_over')
WellStatus.unknown = WellStatus._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellStatus._InitializeFacetMap(WellStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellStatus', WellStatus)

# Atomic simple type: {http://www.witsml.org/schemas/1series}timeZone
class timeZone (abstractTimeZone):

    """A time zone conforming to the XSD:dateTime specification."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeZone')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 51, 1)
    _Documentation = 'A time zone conforming to the XSD:dateTime specification.'
timeZone._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'timeZone', timeZone)

# List simple type: {http://www.witsml.org/schemas/1series}listOfString
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfString (pyxb.binding.basis.STD_list):

    """A representation of a list of xsd:string values,
			restricted to strings without embedded whitespace."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'listOfString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 214, 1)
    _Documentation = 'A representation of a list of xsd:string values,\n\t\t\trestricted to strings without embedded whitespace.'

    _ItemType = abstractString32
listOfString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'listOfString', listOfString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}uidString
class uidString (abstractUidString):

    """A locally unique identifier. 
			The value is not intended to convey any semantic content (e.g., it may be computer generated). """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uidString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 226, 1)
    _Documentation = 'A locally unique identifier. \n\t\t\tThe value is not intended to convey any semantic content (e.g., it may be computer generated). '
uidString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'uidString', uidString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}uidParentString
class uidParentString (abstractUidString):

    """A unique identifier of an object parent. 
			This should only be used for the uid of a parent object (i.e., a foreign key to another object). 
			It should not be used for child nodes of an object.
			The value is not intended to convey any semantic content (e.g., it may be computer generated).
			The purpose of this type is to facilitate modifying the optionality of parentage uids in derived schemas."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uidParentString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 235, 1)
    _Documentation = 'A unique identifier of an object parent. \n\t\t\tThis should only be used for the uid of a parent object (i.e., a foreign key to another object). \n\t\t\tIt should not be used for child nodes of an object.\n\t\t\tThe value is not intended to convey any semantic content (e.g., it may be computer generated).\n\t\t\tThe purpose of this type is to facilitate modifying the optionality of parentage uids in derived schemas.'
uidParentString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'uidParentString', uidParentString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}refString
class refString (abstractUidString):

    """A reference to the unique identifier of another element. 
			This value represents a foreign key from one element to another.
			The value should match the value of an attribute of type uidString."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 247, 1)
    _Documentation = 'A reference to the unique identifier of another element. \n\t\t\tThis value represents a foreign key from one element to another.\n\t\t\tThe value should match the value of an attribute of type uidString.'
refString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'refString', refString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}refWellDatum
class refWellDatum (abstractUidString):

    """A reference to a wellDatum in the current well. 
			This value must match the uid value in a WellDatum. 
			This value represents a foreign key from one element to another.
			This is an exception to the convention that a foreign key must utilize both 
			a human contextual name and a uid value. For messages outside the context of
			a server then this value will commonly match the value of the name of the 
			wellDatum (e.g., 'KB') if uids are not not used in that context.
			This was a compromise in order to allow the coordinate structures to be simple
			and still be usable both within the context of a server and outside the context of a server."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refWellDatum')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 316, 1)
    _Documentation = "A reference to a wellDatum in the current well. \n\t\t\tThis value must match the uid value in a WellDatum. \n\t\t\tThis value represents a foreign key from one element to another.\n\t\t\tThis is an exception to the convention that a foreign key must utilize both \n\t\t\ta human contextual name and a uid value. For messages outside the context of\n\t\t\ta server then this value will commonly match the value of the name of the \n\t\t\twellDatum (e.g., 'KB') if uids are not not used in that context.\n\t\t\tThis was a compromise in order to allow the coordinate structures to be simple\n\t\t\tand still be usable both within the context of a server and outside the context of a server."
refWellDatum._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'refWellDatum', refWellDatum)

# Atomic simple type: {http://www.witsml.org/schemas/1series}nameString
class nameString (abstractNameString):

    """A user assigned human recognizable contextual name of something. 
			There should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.
			This type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 333, 1)
    _Documentation = 'A user assigned human recognizable contextual name of something. \n\t\t\tThere should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.\n\t\t\tThis type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration.'
nameString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'nameString', nameString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}descriptionString
class descriptionString (abstractDescriptionString):

    """A textual description of something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'descriptionString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 352, 1)
    _Documentation = 'A textual description of something.'
descriptionString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'descriptionString', descriptionString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}encodedValueString
class encodedValueString (abstractString32):

    """A single value. The encoding may utilize 
			any of several xsd encodings. Something external to the value must
			define the encoding."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'encodedValueString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 381, 1)
    _Documentation = 'A single value. The encoding may utilize \n\t\t\tany of several xsd encodings. Something external to the value must\n\t\t\tdefine the encoding.'
encodedValueString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'encodedValueString', encodedValueString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}kindString
class kindString (abstractTypeEnum):

    """A community assigned human recognizable name. 
			This type of value is intended to be unique and is generally a candidate to be constrained to an enumerated list."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'kindString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 410, 1)
    _Documentation = 'A community assigned human recognizable name. \n\t\t\tThis type of value is intended to be unique and is generally a candidate to be constrained to an enumerated list.'
kindString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'kindString', kindString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}uomString
class uomString (abstractUomEnum):

    """A unit of measure acronym from the POSC unit of measure file."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uomString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 419, 1)
    _Documentation = 'A unit of measure acronym from the POSC unit of measure file.'
uomString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'uomString', uomString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}positiveCount
class positiveCount (abstractPositiveCount):

    """A positive integer (one based count or index)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positiveCount')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 766, 1)
    _Documentation = 'A positive integer (one based count or index).'
positiveCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveCount, value=pyxb.binding.datatypes.short(1))
positiveCount._InitializeFacetMap(positiveCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'positiveCount', positiveCount)

# Atomic simple type: {http://www.witsml.org/schemas/1series}str32
class str32 (abstractString32):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'str32')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 896, 1)
    _Documentation = ''
str32._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'str32', str32)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PercentUom
class PercentUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 31, 1)
    _Documentation = ''
PercentUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PercentUom, enum_prefix=None)
PercentUom.emptyString = PercentUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
PercentUom._InitializeFacetMap(PercentUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PercentUom', PercentUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MeasuredDepthUom
class MeasuredDepthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """The units of measure that are valid for measured depths in a wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasuredDepthUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 40, 1)
    _Documentation = 'The units of measure that are valid for measured depths in a wellbore.'
MeasuredDepthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MeasuredDepthUom, enum_prefix=None)
MeasuredDepthUom.m = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value='m', tag='m')
MeasuredDepthUom.ft = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value='ft', tag='ft')
MeasuredDepthUom.ftUS = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value='ftUS', tag='ftUS')
MeasuredDepthUom._InitializeFacetMap(MeasuredDepthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MeasuredDepthUom', MeasuredDepthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellVerticalCoordinateUom
class WellVerticalCoordinateUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """The units of measure that are valid for vertical gravity based 
			coordinates (i.e., elevation or vertical depth) within the context of a well."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellVerticalCoordinateUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 64, 1)
    _Documentation = 'The units of measure that are valid for vertical gravity based \n\t\t\tcoordinates (i.e., elevation or vertical depth) within the context of a well.'
WellVerticalCoordinateUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellVerticalCoordinateUom, enum_prefix=None)
WellVerticalCoordinateUom.m = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value='m', tag='m')
WellVerticalCoordinateUom.ft = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value='ft', tag='ft')
WellVerticalCoordinateUom.ftUS = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value='ftUS', tag='ftUS')
WellVerticalCoordinateUom.ftBr65 = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value='ftBr(65)', tag='ftBr65')
WellVerticalCoordinateUom._InitializeFacetMap(WellVerticalCoordinateUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellVerticalCoordinateUom', WellVerticalCoordinateUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AccelerationLinearUom
class AccelerationLinearUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AccelerationLinearUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 97, 1)
    _Documentation = ''
AccelerationLinearUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AccelerationLinearUom, enum_prefix=None)
AccelerationLinearUom.ms2 = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='m/s2', tag='ms2')
AccelerationLinearUom.cms2 = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='cm/s2', tag='cms2')
AccelerationLinearUom.fts2 = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='ft/s2', tag='fts2')
AccelerationLinearUom.Gal = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='Gal', tag='Gal')
AccelerationLinearUom.mgn = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='mgn', tag='mgn')
AccelerationLinearUom.gn = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='gn', tag='gn')
AccelerationLinearUom.mGal = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='mGal', tag='mGal')
AccelerationLinearUom._InitializeFacetMap(AccelerationLinearUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AccelerationLinearUom', AccelerationLinearUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AnglePerLengthUom
class AnglePerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnglePerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 112, 1)
    _Documentation = ''
AnglePerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AnglePerLengthUom, enum_prefix=None)
AnglePerLengthUom.radm = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='rad/m', tag='radm')
AnglePerLengthUom.dega30ft = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dega/30ft', tag='dega30ft')
AnglePerLengthUom.degaft = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dega/ft', tag='degaft')
AnglePerLengthUom.dega100ft = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dega/100ft', tag='dega100ft')
AnglePerLengthUom.degam = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dega/m', tag='degam')
AnglePerLengthUom.dega30m = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dega/30m', tag='dega30m')
AnglePerLengthUom.radft = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='rad/ft', tag='radft')
AnglePerLengthUom._InitializeFacetMap(AnglePerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AnglePerLengthUom', AnglePerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AnglePerTimeUom
class AnglePerTimeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnglePerTimeUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 127, 1)
    _Documentation = ''
AnglePerTimeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AnglePerTimeUom, enum_prefix=None)
AnglePerTimeUom.rads = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='rad/s', tag='rads')
AnglePerTimeUom.cs = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='c/s', tag='cs')
AnglePerTimeUom.degah = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='dega/h', tag='degah')
AnglePerTimeUom.degamin = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='dega/min', tag='degamin')
AnglePerTimeUom.degas = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='dega/s', tag='degas')
AnglePerTimeUom.revs = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='rev/s', tag='revs')
AnglePerTimeUom.rpm = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='rpm', tag='rpm')
AnglePerTimeUom._InitializeFacetMap(AnglePerTimeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AnglePerTimeUom', AnglePerTimeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AreaUom
class AreaUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AreaUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 142, 1)
    _Documentation = ''
AreaUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AreaUom, enum_prefix=None)
AreaUom.m2 = AreaUom._CF_enumeration.addEnumeration(unicode_value='m2', tag='m2')
AreaUom.acre = AreaUom._CF_enumeration.addEnumeration(unicode_value='acre', tag='acre')
AreaUom.b = AreaUom._CF_enumeration.addEnumeration(unicode_value='b', tag='b')
AreaUom.cm2 = AreaUom._CF_enumeration.addEnumeration(unicode_value='cm2', tag='cm2')
AreaUom.ft2 = AreaUom._CF_enumeration.addEnumeration(unicode_value='ft2', tag='ft2')
AreaUom.ha = AreaUom._CF_enumeration.addEnumeration(unicode_value='ha', tag='ha')
AreaUom.in2 = AreaUom._CF_enumeration.addEnumeration(unicode_value='in2', tag='in2')
AreaUom.km2 = AreaUom._CF_enumeration.addEnumeration(unicode_value='km2', tag='km2')
AreaUom.mi2 = AreaUom._CF_enumeration.addEnumeration(unicode_value='mi2', tag='mi2')
AreaUom.miUS2 = AreaUom._CF_enumeration.addEnumeration(unicode_value='miUS2', tag='miUS2')
AreaUom.mm2 = AreaUom._CF_enumeration.addEnumeration(unicode_value='mm2', tag='mm2')
AreaUom.um2 = AreaUom._CF_enumeration.addEnumeration(unicode_value='um2', tag='um2')
AreaUom.yd2 = AreaUom._CF_enumeration.addEnumeration(unicode_value='yd2', tag='yd2')
AreaUom._InitializeFacetMap(AreaUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AreaUom', AreaUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AreaPerAreaUom
class AreaPerAreaUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AreaPerAreaUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 163, 1)
    _Documentation = ''
AreaPerAreaUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AreaPerAreaUom, enum_prefix=None)
AreaPerAreaUom.Euc = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='Euc', tag='Euc')
AreaPerAreaUom.emptyString = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
AreaPerAreaUom.in2ft2 = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='in2/ft2', tag='in2ft2')
AreaPerAreaUom.in2in2 = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='in2/in2', tag='in2in2')
AreaPerAreaUom.m2m2 = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='m2/m2', tag='m2m2')
AreaPerAreaUom.mm2mm2 = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='mm2/mm2', tag='mm2mm2')
AreaPerAreaUom._InitializeFacetMap(AreaPerAreaUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AreaPerAreaUom', AreaPerAreaUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}CompressibilityUom
class CompressibilityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompressibilityUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 177, 1)
    _Documentation = ''
CompressibilityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CompressibilityUom, enum_prefix=None)
CompressibilityUom.n1psi = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value='1/psi', tag='n1psi')
CompressibilityUom.n1upsi = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value='1/upsi', tag='n1upsi')
CompressibilityUom.n1Pa = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value='1/Pa', tag='n1Pa')
CompressibilityUom.n1bar = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value='1/bar', tag='n1bar')
CompressibilityUom.n1kPa = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value='1/kPa', tag='n1kPa')
CompressibilityUom.n1pPa = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value='1/pPa', tag='n1pPa')
CompressibilityUom._InitializeFacetMap(CompressibilityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CompressibilityUom', CompressibilityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DensityUom
class DensityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DensityUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 191, 1)
    _Documentation = ''
DensityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DensityUom, enum_prefix=None)
DensityUom.kgm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='kg/m3', tag='kgm3')
DensityUom.n10Mgm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='10Mg/m3', tag='n10Mgm3')
DensityUom.dAPI = DensityUom._CF_enumeration.addEnumeration(unicode_value='dAPI', tag='dAPI')
DensityUom.gcm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='g/cm3', tag='gcm3')
DensityUom.gdm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='g/dm3', tag='gdm3')
DensityUom.ggalUK = DensityUom._CF_enumeration.addEnumeration(unicode_value='g/galUK', tag='ggalUK')
DensityUom.ggalUS = DensityUom._CF_enumeration.addEnumeration(unicode_value='g/galUS', tag='ggalUS')
DensityUom.gL = DensityUom._CF_enumeration.addEnumeration(unicode_value='g/L', tag='gL')
DensityUom.gm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='g/m3', tag='gm3')
DensityUom.grainft3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='grain/ft3', tag='grainft3')
DensityUom.graingalUS = DensityUom._CF_enumeration.addEnumeration(unicode_value='grain/galUS', tag='graingalUS')
DensityUom.grain100ft3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='grain/100ft3', tag='grain100ft3')
DensityUom.kgdm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='kg/dm3', tag='kgdm3')
DensityUom.kgL = DensityUom._CF_enumeration.addEnumeration(unicode_value='kg/L', tag='kgL')
DensityUom.Mgm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='Mg/m3', tag='Mgm3')
DensityUom.lbm10bbl = DensityUom._CF_enumeration.addEnumeration(unicode_value='lbm/10bbl', tag='lbm10bbl')
DensityUom.lbmbbl = DensityUom._CF_enumeration.addEnumeration(unicode_value='lbm/bbl', tag='lbmbbl')
DensityUom.lbmft3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='lbm/ft3', tag='lbmft3')
DensityUom.lbmgalUK = DensityUom._CF_enumeration.addEnumeration(unicode_value='lbm/galUK', tag='lbmgalUK')
DensityUom.lbm1000galUK = DensityUom._CF_enumeration.addEnumeration(unicode_value='lbm/1000galUK', tag='lbm1000galUK')
DensityUom.lbmgalUS = DensityUom._CF_enumeration.addEnumeration(unicode_value='lbm/galUS', tag='lbmgalUS')
DensityUom.lbm1000galUS = DensityUom._CF_enumeration.addEnumeration(unicode_value='lbm/1000galUS', tag='lbm1000galUS')
DensityUom.lbmin3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='lbm/in3', tag='lbmin3')
DensityUom.lbmMbbl = DensityUom._CF_enumeration.addEnumeration(unicode_value='lbm/Mbbl', tag='lbmMbbl')
DensityUom.mgdm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='mg/dm3', tag='mgdm3')
DensityUom.mggalUS = DensityUom._CF_enumeration.addEnumeration(unicode_value='mg/galUS', tag='mggalUS')
DensityUom.mgL = DensityUom._CF_enumeration.addEnumeration(unicode_value='mg/L', tag='mgL')
DensityUom.mgm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='mg/m3', tag='mgm3')
DensityUom.ugcm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value='ug/cm3', tag='ugcm3')
DensityUom._InitializeFacetMap(DensityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DensityUom', DensityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DimensionlessUom
class DimensionlessUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DimensionlessUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 228, 1)
    _Documentation = ''
DimensionlessUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DimensionlessUom, enum_prefix=None)
DimensionlessUom.Euc = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value='Euc', tag='Euc')
DimensionlessUom.emptyString = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
DimensionlessUom.cEuc = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value='cEuc', tag='cEuc')
DimensionlessUom.mEuc = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value='mEuc', tag='mEuc')
DimensionlessUom.nEuc = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value='nEuc', tag='nEuc')
DimensionlessUom.uEuc = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value='uEuc', tag='uEuc')
DimensionlessUom._InitializeFacetMap(DimensionlessUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DimensionlessUom', DimensionlessUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DynamicViscosityUom
class DynamicViscosityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DynamicViscosityUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 242, 1)
    _Documentation = ''
DynamicViscosityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DynamicViscosityUom, enum_prefix=None)
DynamicViscosityUom.Pa_s = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='Pa.s', tag='Pa_s')
DynamicViscosityUom.cP = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='cP', tag='cP')
DynamicViscosityUom.P = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='P', tag='P')
DynamicViscosityUom.psi_s = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='psi.s', tag='psi_s')
DynamicViscosityUom.dyne_scm2 = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='dyne.s/cm2', tag='dyne_scm2')
DynamicViscosityUom.kgf_sm2 = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='kgf.s/m2', tag='kgf_sm2')
DynamicViscosityUom.lbf_sft2 = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='lbf.s/ft2', tag='lbf_sft2')
DynamicViscosityUom.lbf_sin2 = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='lbf.s/in2', tag='lbf_sin2')
DynamicViscosityUom.mPa_s = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='mPa.s', tag='mPa_s')
DynamicViscosityUom.N_sm2 = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='N.s/m2', tag='N_sm2')
DynamicViscosityUom._InitializeFacetMap(DynamicViscosityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DynamicViscosityUom', DynamicViscosityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ElectricCurrentUom
class ElectricCurrentUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElectricCurrentUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 260, 1)
    _Documentation = ''
ElectricCurrentUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ElectricCurrentUom, enum_prefix=None)
ElectricCurrentUom.A = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
ElectricCurrentUom.MA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
ElectricCurrentUom.kA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value='kA', tag='kA')
ElectricCurrentUom.mA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value='mA', tag='mA')
ElectricCurrentUom.nA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value='nA', tag='nA')
ElectricCurrentUom.pA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value='pA', tag='pA')
ElectricCurrentUom.uA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value='uA', tag='uA')
ElectricCurrentUom._InitializeFacetMap(ElectricCurrentUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ElectricCurrentUom', ElectricCurrentUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ElectricPotentialUom
class ElectricPotentialUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElectricPotentialUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 275, 1)
    _Documentation = ''
ElectricPotentialUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ElectricPotentialUom, enum_prefix=None)
ElectricPotentialUom.V = ElectricPotentialUom._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
ElectricPotentialUom.kV = ElectricPotentialUom._CF_enumeration.addEnumeration(unicode_value='kV', tag='kV')
ElectricPotentialUom.mV = ElectricPotentialUom._CF_enumeration.addEnumeration(unicode_value='mV', tag='mV')
ElectricPotentialUom.MV = ElectricPotentialUom._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
ElectricPotentialUom.uV = ElectricPotentialUom._CF_enumeration.addEnumeration(unicode_value='uV', tag='uV')
ElectricPotentialUom._InitializeFacetMap(ElectricPotentialUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ElectricPotentialUom', ElectricPotentialUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}EquivalentPerMassUom
class EquivalentPerMassUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EquivalentPerMassUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 292, 1)
    _Documentation = ''
EquivalentPerMassUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EquivalentPerMassUom, enum_prefix=None)
EquivalentPerMassUom.eqkg = EquivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value='eq/kg', tag='eqkg')
EquivalentPerMassUom.meqg = EquivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value='meq/g', tag='meqg')
EquivalentPerMassUom.meq100g = EquivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value='meq/100g', tag='meq100g')
EquivalentPerMassUom._InitializeFacetMap(EquivalentPerMassUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EquivalentPerMassUom', EquivalentPerMassUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ForceUom
class ForceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ForceUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 303, 1)
    _Documentation = ''
ForceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ForceUom, enum_prefix=None)
ForceUom.N = ForceUom._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
ForceUom.daN = ForceUom._CF_enumeration.addEnumeration(unicode_value='daN', tag='daN')
ForceUom.dyne = ForceUom._CF_enumeration.addEnumeration(unicode_value='dyne', tag='dyne')
ForceUom.gf = ForceUom._CF_enumeration.addEnumeration(unicode_value='gf', tag='gf')
ForceUom.kdyne = ForceUom._CF_enumeration.addEnumeration(unicode_value='kdyne', tag='kdyne')
ForceUom.kgf = ForceUom._CF_enumeration.addEnumeration(unicode_value='kgf', tag='kgf')
ForceUom.klbf = ForceUom._CF_enumeration.addEnumeration(unicode_value='klbf', tag='klbf')
ForceUom.kN = ForceUom._CF_enumeration.addEnumeration(unicode_value='kN', tag='kN')
ForceUom.lbf = ForceUom._CF_enumeration.addEnumeration(unicode_value='lbf', tag='lbf')
ForceUom.Mgf = ForceUom._CF_enumeration.addEnumeration(unicode_value='Mgf', tag='Mgf')
ForceUom.mN = ForceUom._CF_enumeration.addEnumeration(unicode_value='mN', tag='mN')
ForceUom.MN = ForceUom._CF_enumeration.addEnumeration(unicode_value='MN', tag='MN')
ForceUom.ozf = ForceUom._CF_enumeration.addEnumeration(unicode_value='ozf', tag='ozf')
ForceUom.pdl = ForceUom._CF_enumeration.addEnumeration(unicode_value='pdl', tag='pdl')
ForceUom.tonfUK = ForceUom._CF_enumeration.addEnumeration(unicode_value='tonfUK', tag='tonfUK')
ForceUom.tonfUS = ForceUom._CF_enumeration.addEnumeration(unicode_value='tonfUS', tag='tonfUS')
ForceUom.uN = ForceUom._CF_enumeration.addEnumeration(unicode_value='uN', tag='uN')
ForceUom._InitializeFacetMap(ForceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ForceUom', ForceUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ForcePerLengthUom
class ForcePerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ForcePerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 328, 1)
    _Documentation = ''
ForcePerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ForcePerLengthUom, enum_prefix=None)
ForcePerLengthUom.N30m = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='N/30m', tag='N30m')
ForcePerLengthUom.Nm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='N/m', tag='Nm')
ForcePerLengthUom.dynecm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dyne/cm', tag='dynecm')
ForcePerLengthUom.kNm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='kN/m', tag='kNm')
ForcePerLengthUom.kgfcm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='kgf/cm', tag='kgfcm')
ForcePerLengthUom.lbf100ft = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='lbf/100ft', tag='lbf100ft')
ForcePerLengthUom.lbf30m = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='lbf/30m', tag='lbf30m')
ForcePerLengthUom.lbfft = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='lbf/ft', tag='lbfft')
ForcePerLengthUom.lbfin = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='lbf/in', tag='lbfin')
ForcePerLengthUom.mNkm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='mN/km', tag='mNkm')
ForcePerLengthUom.mNm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='mN/m', tag='mNm')
ForcePerLengthUom.pdlcm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='pdl/cm', tag='pdlcm')
ForcePerLengthUom.tonfUKft = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='tonfUK/ft', tag='tonfUKft')
ForcePerLengthUom.tonfUSft = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='tonfUS/ft', tag='tonfUSft')
ForcePerLengthUom._InitializeFacetMap(ForcePerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ForcePerLengthUom', ForcePerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ForcePerVolumeUom
class ForcePerVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ForcePerVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 350, 1)
    _Documentation = ''
ForcePerVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ForcePerVolumeUom, enum_prefix=None)
ForcePerVolumeUom.Nm3 = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='N/m3', tag='Nm3')
ForcePerVolumeUom.atm100m = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='atm/100m', tag='atm100m')
ForcePerVolumeUom.atmm = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='atm/m', tag='atmm')
ForcePerVolumeUom.barkm = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bar/km', tag='barkm')
ForcePerVolumeUom.barm = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bar/m', tag='barm')
ForcePerVolumeUom.GPacm = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='GPa/cm', tag='GPacm')
ForcePerVolumeUom.kPa100m = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='kPa/100m', tag='kPa100m')
ForcePerVolumeUom.kPam = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='kPa/m', tag='kPam')
ForcePerVolumeUom.lbfft3 = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='lbf/ft3', tag='lbfft3')
ForcePerVolumeUom.lbfgalUS = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='lbf/galUS', tag='lbfgalUS')
ForcePerVolumeUom.MPam = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='MPa/m', tag='MPam')
ForcePerVolumeUom.psift = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='psi/ft', tag='psift')
ForcePerVolumeUom.psi100ft = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='psi/100ft', tag='psi100ft')
ForcePerVolumeUom.psikft = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='psi/kft', tag='psikft')
ForcePerVolumeUom.psim = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='psi/m', tag='psim')
ForcePerVolumeUom.Pam = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='Pa/m', tag='Pam')
ForcePerVolumeUom.atmft = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='atm/ft', tag='atmft')
ForcePerVolumeUom._InitializeFacetMap(ForcePerVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ForcePerVolumeUom', ForcePerVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}IlluminanceUom
class IlluminanceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IlluminanceUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 375, 1)
    _Documentation = ''
IlluminanceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IlluminanceUom, enum_prefix=None)
IlluminanceUom.lx = IlluminanceUom._CF_enumeration.addEnumeration(unicode_value='lx', tag='lx')
IlluminanceUom.lmm2 = IlluminanceUom._CF_enumeration.addEnumeration(unicode_value='lm/m2', tag='lmm2')
IlluminanceUom.footcandle = IlluminanceUom._CF_enumeration.addEnumeration(unicode_value='footcandle', tag='footcandle')
IlluminanceUom.klx = IlluminanceUom._CF_enumeration.addEnumeration(unicode_value='klx', tag='klx')
IlluminanceUom._InitializeFacetMap(IlluminanceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IlluminanceUom', IlluminanceUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LengthUom
class LengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LengthUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 387, 1)
    _Documentation = ''
LengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthUom, enum_prefix=None)
LengthUom.m = LengthUom._CF_enumeration.addEnumeration(unicode_value='m', tag='m')
LengthUom.angstrom = LengthUom._CF_enumeration.addEnumeration(unicode_value='angstrom', tag='angstrom')
LengthUom.chBnA = LengthUom._CF_enumeration.addEnumeration(unicode_value='chBnA', tag='chBnA')
LengthUom.chBnB = LengthUom._CF_enumeration.addEnumeration(unicode_value='chBnB', tag='chBnB')
LengthUom.chCla = LengthUom._CF_enumeration.addEnumeration(unicode_value='chCla', tag='chCla')
LengthUom.chSe = LengthUom._CF_enumeration.addEnumeration(unicode_value='chSe', tag='chSe')
LengthUom.chUS = LengthUom._CF_enumeration.addEnumeration(unicode_value='chUS', tag='chUS')
LengthUom.cm = LengthUom._CF_enumeration.addEnumeration(unicode_value='cm', tag='cm')
LengthUom.dm = LengthUom._CF_enumeration.addEnumeration(unicode_value='dm', tag='dm')
LengthUom.fathom = LengthUom._CF_enumeration.addEnumeration(unicode_value='fathom', tag='fathom')
LengthUom.fm = LengthUom._CF_enumeration.addEnumeration(unicode_value='fm', tag='fm')
LengthUom.ft = LengthUom._CF_enumeration.addEnumeration(unicode_value='ft', tag='ft')
LengthUom.ftBnA = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftBnA', tag='ftBnA')
LengthUom.ftBnB = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftBnB', tag='ftBnB')
LengthUom.ftBr65 = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftBr(65)', tag='ftBr65')
LengthUom.ftCla = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftCla', tag='ftCla')
LengthUom.ftGC = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftGC', tag='ftGC')
LengthUom.ftInd = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftInd', tag='ftInd')
LengthUom.ftInd37 = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftInd(37)', tag='ftInd37')
LengthUom.ftInd62 = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftInd(62)', tag='ftInd62')
LengthUom.ftInd75 = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftInd(75)', tag='ftInd75')
LengthUom.ftMA = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftMA', tag='ftMA')
LengthUom.ftSe = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftSe', tag='ftSe')
LengthUom.ftUS = LengthUom._CF_enumeration.addEnumeration(unicode_value='ftUS', tag='ftUS')
LengthUom.in_ = LengthUom._CF_enumeration.addEnumeration(unicode_value='in', tag='in_')
LengthUom.in10 = LengthUom._CF_enumeration.addEnumeration(unicode_value='in/10', tag='in10')
LengthUom.in16 = LengthUom._CF_enumeration.addEnumeration(unicode_value='in/16', tag='in16')
LengthUom.in32 = LengthUom._CF_enumeration.addEnumeration(unicode_value='in/32', tag='in32')
LengthUom.in64 = LengthUom._CF_enumeration.addEnumeration(unicode_value='in/64', tag='in64')
LengthUom.inUS = LengthUom._CF_enumeration.addEnumeration(unicode_value='inUS', tag='inUS')
LengthUom.km = LengthUom._CF_enumeration.addEnumeration(unicode_value='km', tag='km')
LengthUom.lkBnA = LengthUom._CF_enumeration.addEnumeration(unicode_value='lkBnA', tag='lkBnA')
LengthUom.lkBnB = LengthUom._CF_enumeration.addEnumeration(unicode_value='lkBnB', tag='lkBnB')
LengthUom.lkCla = LengthUom._CF_enumeration.addEnumeration(unicode_value='lkCla', tag='lkCla')
LengthUom.lkSe = LengthUom._CF_enumeration.addEnumeration(unicode_value='lkSe', tag='lkSe')
LengthUom.lkUS = LengthUom._CF_enumeration.addEnumeration(unicode_value='lkUS', tag='lkUS')
LengthUom.mGer = LengthUom._CF_enumeration.addEnumeration(unicode_value='mGer', tag='mGer')
LengthUom.mi = LengthUom._CF_enumeration.addEnumeration(unicode_value='mi', tag='mi')
LengthUom.mil = LengthUom._CF_enumeration.addEnumeration(unicode_value='mil', tag='mil')
LengthUom.miUS = LengthUom._CF_enumeration.addEnumeration(unicode_value='miUS', tag='miUS')
LengthUom.mm = LengthUom._CF_enumeration.addEnumeration(unicode_value='mm', tag='mm')
LengthUom.Mm = LengthUom._CF_enumeration.addEnumeration(unicode_value='Mm', tag='Mm')
LengthUom.nautmi = LengthUom._CF_enumeration.addEnumeration(unicode_value='nautmi', tag='nautmi')
LengthUom.nm = LengthUom._CF_enumeration.addEnumeration(unicode_value='nm', tag='nm')
LengthUom.pm = LengthUom._CF_enumeration.addEnumeration(unicode_value='pm', tag='pm')
LengthUom.um = LengthUom._CF_enumeration.addEnumeration(unicode_value='um', tag='um')
LengthUom.yd = LengthUom._CF_enumeration.addEnumeration(unicode_value='yd', tag='yd')
LengthUom.ydBnA = LengthUom._CF_enumeration.addEnumeration(unicode_value='ydBnA', tag='ydBnA')
LengthUom.ydBnB = LengthUom._CF_enumeration.addEnumeration(unicode_value='ydBnB', tag='ydBnB')
LengthUom.ydCla = LengthUom._CF_enumeration.addEnumeration(unicode_value='ydCla', tag='ydCla')
LengthUom.ydIm = LengthUom._CF_enumeration.addEnumeration(unicode_value='ydIm', tag='ydIm')
LengthUom.ydInd = LengthUom._CF_enumeration.addEnumeration(unicode_value='ydInd', tag='ydInd')
LengthUom.ydInd37 = LengthUom._CF_enumeration.addEnumeration(unicode_value='ydInd(37)', tag='ydInd37')
LengthUom.ydInd62 = LengthUom._CF_enumeration.addEnumeration(unicode_value='ydInd(62)', tag='ydInd62')
LengthUom.ydInd75 = LengthUom._CF_enumeration.addEnumeration(unicode_value='ydInd(75)', tag='ydInd75')
LengthUom.ydSe = LengthUom._CF_enumeration.addEnumeration(unicode_value='ydSe', tag='ydSe')
LengthUom._InitializeFacetMap(LengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LengthUom', LengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LengthPerLengthUom
class LengthPerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LengthPerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 451, 1)
    _Documentation = ''
LengthPerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthPerLengthUom, enum_prefix=None)
LengthPerLengthUom.emptyString = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
LengthPerLengthUom.ft100ft = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft/100ft', tag='ft100ft')
LengthPerLengthUom.ftft = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft/ft', tag='ftft')
LengthPerLengthUom.ftin = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft/in', tag='ftin')
LengthPerLengthUom.ftm = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft/m', tag='ftm')
LengthPerLengthUom.ftmi = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft/mi', tag='ftmi')
LengthPerLengthUom.kmcm = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='km/cm', tag='kmcm')
LengthPerLengthUom.m30m = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='m/30m', tag='m30m')
LengthPerLengthUom.mcm = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='m/cm', tag='mcm')
LengthPerLengthUom.mkm = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='m/km', tag='mkm')
LengthPerLengthUom.mm = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='m/m', tag='mm')
LengthPerLengthUom.miin = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='mi/in', tag='miin')
LengthPerLengthUom._InitializeFacetMap(LengthPerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LengthPerLengthUom', LengthPerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MagneticInductionUom
class MagneticInductionUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MagneticInductionUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 475, 1)
    _Documentation = ''
MagneticInductionUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MagneticInductionUom, enum_prefix=None)
MagneticInductionUom.T = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
MagneticInductionUom.gauss = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value='gauss', tag='gauss')
MagneticInductionUom.mT = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value='mT', tag='mT')
MagneticInductionUom.mgauss = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value='mgauss', tag='mgauss')
MagneticInductionUom.nT = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value='nT', tag='nT')
MagneticInductionUom.uT = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value='uT', tag='uT')
MagneticInductionUom._InitializeFacetMap(MagneticInductionUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MagneticInductionUom', MagneticInductionUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MassConcentrationUom
class MassConcentrationUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MassConcentrationUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 489, 1)
    _Documentation = ''
MassConcentrationUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MassConcentrationUom, enum_prefix=None)
MassConcentrationUom.Euc = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value='Euc', tag='Euc')
MassConcentrationUom.emptyString = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
MassConcentrationUom.gkg = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value='g/kg', tag='gkg')
MassConcentrationUom.kgkg = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value='kg/kg', tag='kgkg')
MassConcentrationUom.kgsack94 = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value='kg/sack94', tag='kgsack94')
MassConcentrationUom.mgkg = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value='mg/kg', tag='mgkg')
MassConcentrationUom.permil = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value='permil', tag='permil')
MassConcentrationUom.ppdk = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value='ppdk', tag='ppdk')
MassConcentrationUom.ppk = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value='ppk', tag='ppk')
MassConcentrationUom.ppm = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value='ppm', tag='ppm')
MassConcentrationUom._InitializeFacetMap(MassConcentrationUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MassConcentrationUom', MassConcentrationUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MassUom
class MassUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MassUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 507, 1)
    _Documentation = ''
MassUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MassUom, enum_prefix=None)
MassUom.kg = MassUom._CF_enumeration.addEnumeration(unicode_value='kg', tag='kg')
MassUom.ag = MassUom._CF_enumeration.addEnumeration(unicode_value='ag', tag='ag')
MassUom.ct = MassUom._CF_enumeration.addEnumeration(unicode_value='ct', tag='ct')
MassUom.cwtUK = MassUom._CF_enumeration.addEnumeration(unicode_value='cwtUK', tag='cwtUK')
MassUom.cwtUS = MassUom._CF_enumeration.addEnumeration(unicode_value='cwtUS', tag='cwtUS')
MassUom.g = MassUom._CF_enumeration.addEnumeration(unicode_value='g', tag='g')
MassUom.grain = MassUom._CF_enumeration.addEnumeration(unicode_value='grain', tag='grain')
MassUom.klbm = MassUom._CF_enumeration.addEnumeration(unicode_value='klbm', tag='klbm')
MassUom.lbm = MassUom._CF_enumeration.addEnumeration(unicode_value='lbm', tag='lbm')
MassUom.Mg = MassUom._CF_enumeration.addEnumeration(unicode_value='Mg', tag='Mg')
MassUom.mg = MassUom._CF_enumeration.addEnumeration(unicode_value='mg', tag='mg')
MassUom.ozav = MassUom._CF_enumeration.addEnumeration(unicode_value='oz(av)', tag='ozav')
MassUom.oztroy = MassUom._CF_enumeration.addEnumeration(unicode_value='oz(troy)', tag='oztroy')
MassUom.ozm = MassUom._CF_enumeration.addEnumeration(unicode_value='ozm', tag='ozm')
MassUom.sack94 = MassUom._CF_enumeration.addEnumeration(unicode_value='sack94', tag='sack94')
MassUom.t = MassUom._CF_enumeration.addEnumeration(unicode_value='t', tag='t')
MassUom.tonUK = MassUom._CF_enumeration.addEnumeration(unicode_value='tonUK', tag='tonUK')
MassUom.tonUS = MassUom._CF_enumeration.addEnumeration(unicode_value='tonUS', tag='tonUS')
MassUom.ug = MassUom._CF_enumeration.addEnumeration(unicode_value='ug', tag='ug')
MassUom._InitializeFacetMap(MassUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MassUom', MassUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MassPerLengthUom
class MassPerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MassPerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 534, 1)
    _Documentation = ''
MassPerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MassPerLengthUom, enum_prefix=None)
MassPerLengthUom.kgm = MassPerLengthUom._CF_enumeration.addEnumeration(unicode_value='kg/m', tag='kgm')
MassPerLengthUom.klbmin = MassPerLengthUom._CF_enumeration.addEnumeration(unicode_value='klbm/in', tag='klbmin')
MassPerLengthUom.lbmft = MassPerLengthUom._CF_enumeration.addEnumeration(unicode_value='lbm/ft', tag='lbmft')
MassPerLengthUom.Mgin = MassPerLengthUom._CF_enumeration.addEnumeration(unicode_value='Mg/in', tag='Mgin')
MassPerLengthUom.kg_mcm2 = MassPerLengthUom._CF_enumeration.addEnumeration(unicode_value='kg.m/cm2', tag='kg_mcm2')
MassPerLengthUom._InitializeFacetMap(MassPerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MassPerLengthUom', MassPerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MomentOfForceUom
class MomentOfForceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MomentOfForceUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 547, 1)
    _Documentation = ''
MomentOfForceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MomentOfForceUom, enum_prefix=None)
MomentOfForceUom.J = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
MomentOfForceUom.dN_m = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='dN.m', tag='dN_m')
MomentOfForceUom.daN_m = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='daN.m', tag='daN_m')
MomentOfForceUom.ft_lbf = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='ft.lbf', tag='ft_lbf')
MomentOfForceUom.kft_lbf = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='kft.lbf', tag='kft_lbf')
MomentOfForceUom.kgf_m = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='kgf.m', tag='kgf_m')
MomentOfForceUom.kN_m = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='kN.m', tag='kN_m')
MomentOfForceUom.lbf_ft = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='lbf.ft', tag='lbf_ft')
MomentOfForceUom.lbf_in = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='lbf.in', tag='lbf_in')
MomentOfForceUom.lbm_ft2s2 = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='lbm.ft2/s2', tag='lbm_ft2s2')
MomentOfForceUom.N_m = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='N.m', tag='N_m')
MomentOfForceUom.pdl_ft = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='pdl.ft', tag='pdl_ft')
MomentOfForceUom.tonfUS_ft = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='tonfUS.ft', tag='tonfUS_ft')
MomentOfForceUom.tonfUS_mi = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value='tonfUS.mi', tag='tonfUS_mi')
MomentOfForceUom._InitializeFacetMap(MomentOfForceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MomentOfForceUom', MomentOfForceUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PerLengthUom
class PerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 569, 1)
    _Documentation = ''
PerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PerLengthUom, enum_prefix=None)
PerLengthUom.n1m = PerLengthUom._CF_enumeration.addEnumeration(unicode_value='1/m', tag='n1m')
PerLengthUom.n1angstrom = PerLengthUom._CF_enumeration.addEnumeration(unicode_value='1/angstrom', tag='n1angstrom')
PerLengthUom.n1cm = PerLengthUom._CF_enumeration.addEnumeration(unicode_value='1/cm', tag='n1cm')
PerLengthUom.n1ft = PerLengthUom._CF_enumeration.addEnumeration(unicode_value='1/ft', tag='n1ft')
PerLengthUom.n1in = PerLengthUom._CF_enumeration.addEnumeration(unicode_value='1/in', tag='n1in')
PerLengthUom.n1mi = PerLengthUom._CF_enumeration.addEnumeration(unicode_value='1/mi', tag='n1mi')
PerLengthUom.n1mm = PerLengthUom._CF_enumeration.addEnumeration(unicode_value='1/mm', tag='n1mm')
PerLengthUom.n1nm = PerLengthUom._CF_enumeration.addEnumeration(unicode_value='1/nm', tag='n1nm')
PerLengthUom.n1yd = PerLengthUom._CF_enumeration.addEnumeration(unicode_value='1/yd', tag='n1yd')
PerLengthUom._InitializeFacetMap(PerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PerLengthUom', PerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PermeabilityRockUom
class PermeabilityRockUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PermeabilityRockUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 586, 1)
    _Documentation = ''
PermeabilityRockUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PermeabilityRockUom, enum_prefix=None)
PermeabilityRockUom.D = PermeabilityRockUom._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
PermeabilityRockUom.mD = PermeabilityRockUom._CF_enumeration.addEnumeration(unicode_value='mD', tag='mD')
PermeabilityRockUom._InitializeFacetMap(PermeabilityRockUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PermeabilityRockUom', PermeabilityRockUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PlaneAngleUom
class PlaneAngleUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PlaneAngleUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 596, 1)
    _Documentation = ''
PlaneAngleUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PlaneAngleUom, enum_prefix=None)
PlaneAngleUom.rad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='rad', tag='rad')
PlaneAngleUom.c = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='c', tag='c')
PlaneAngleUom.ccgr = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='ccgr', tag='ccgr')
PlaneAngleUom.cgr = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='cgr', tag='cgr')
PlaneAngleUom.dega = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='dega', tag='dega')
PlaneAngleUom.gon = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='gon', tag='gon')
PlaneAngleUom.gr = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='gr', tag='gr')
PlaneAngleUom.Grad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='Grad', tag='Grad')
PlaneAngleUom.krad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='krad', tag='krad')
PlaneAngleUom.mila = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='mila', tag='mila')
PlaneAngleUom.mina = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='mina', tag='mina')
PlaneAngleUom.mrad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='mrad', tag='mrad')
PlaneAngleUom.Mrad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='Mrad', tag='Mrad')
PlaneAngleUom.mseca = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='mseca', tag='mseca')
PlaneAngleUom.seca = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='seca', tag='seca')
PlaneAngleUom.urad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value='urad', tag='urad')
PlaneAngleUom._InitializeFacetMap(PlaneAngleUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PlaneAngleUom', PlaneAngleUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PowerUom
class PowerUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowerUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 620, 1)
    _Documentation = ''
PowerUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PowerUom, enum_prefix=None)
PowerUom.W = PowerUom._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
PowerUom.ch = PowerUom._CF_enumeration.addEnumeration(unicode_value='ch', tag='ch')
PowerUom.CV = PowerUom._CF_enumeration.addEnumeration(unicode_value='CV', tag='CV')
PowerUom.ehp = PowerUom._CF_enumeration.addEnumeration(unicode_value='ehp', tag='ehp')
PowerUom.GW = PowerUom._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
PowerUom.hhp = PowerUom._CF_enumeration.addEnumeration(unicode_value='hhp', tag='hhp')
PowerUom.hp = PowerUom._CF_enumeration.addEnumeration(unicode_value='hp', tag='hp')
PowerUom.kcalh = PowerUom._CF_enumeration.addEnumeration(unicode_value='kcal/h', tag='kcalh')
PowerUom.kW = PowerUom._CF_enumeration.addEnumeration(unicode_value='kW', tag='kW')
PowerUom.MJa = PowerUom._CF_enumeration.addEnumeration(unicode_value='MJ/a', tag='MJa')
PowerUom.MW = PowerUom._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
PowerUom.mW = PowerUom._CF_enumeration.addEnumeration(unicode_value='mW', tag='mW')
PowerUom.nW = PowerUom._CF_enumeration.addEnumeration(unicode_value='nW', tag='nW')
PowerUom.ton_of_refrig = PowerUom._CF_enumeration.addEnumeration(unicode_value='ton of refrig', tag='ton_of_refrig')
PowerUom.TW = PowerUom._CF_enumeration.addEnumeration(unicode_value='TW', tag='TW')
PowerUom.uW = PowerUom._CF_enumeration.addEnumeration(unicode_value='uW', tag='uW')
PowerUom._InitializeFacetMap(PowerUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PowerUom', PowerUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PressureUom
class PressureUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PressureUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 644, 1)
    _Documentation = ''
PressureUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PressureUom, enum_prefix=None)
PressureUom.Pa = PressureUom._CF_enumeration.addEnumeration(unicode_value='Pa', tag='Pa')
PressureUom.at = PressureUom._CF_enumeration.addEnumeration(unicode_value='at', tag='at')
PressureUom.atm = PressureUom._CF_enumeration.addEnumeration(unicode_value='atm', tag='atm')
PressureUom.bar = PressureUom._CF_enumeration.addEnumeration(unicode_value='bar', tag='bar')
PressureUom.cmH2O4degC = PressureUom._CF_enumeration.addEnumeration(unicode_value='cmH2O(4degC)', tag='cmH2O4degC')
PressureUom.dynecm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='dyne/cm2', tag='dynecm2')
PressureUom.GPa = PressureUom._CF_enumeration.addEnumeration(unicode_value='GPa', tag='GPa')
PressureUom.hbar = PressureUom._CF_enumeration.addEnumeration(unicode_value='hbar', tag='hbar')
PressureUom.inH2O39_2F = PressureUom._CF_enumeration.addEnumeration(unicode_value='inH2O(39.2F)', tag='inH2O39_2F')
PressureUom.inH2O60F = PressureUom._CF_enumeration.addEnumeration(unicode_value='inH2O(60F)', tag='inH2O60F')
PressureUom.inHg32F = PressureUom._CF_enumeration.addEnumeration(unicode_value='inHg(32F)', tag='inHg32F')
PressureUom.inHg60F = PressureUom._CF_enumeration.addEnumeration(unicode_value='inHg(60F)', tag='inHg60F')
PressureUom.kgfcm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='kgf/cm2', tag='kgfcm2')
PressureUom.kgfmm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='kgf/mm2', tag='kgfmm2')
PressureUom.kNm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='kN/m2', tag='kNm2')
PressureUom.kPa = PressureUom._CF_enumeration.addEnumeration(unicode_value='kPa', tag='kPa')
PressureUom.kpsi = PressureUom._CF_enumeration.addEnumeration(unicode_value='kpsi', tag='kpsi')
PressureUom.lbfft2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='lbf/ft2', tag='lbfft2')
PressureUom.lbf100ft2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='lbf/100ft2', tag='lbf100ft2')
PressureUom.lbfin2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='lbf/in2', tag='lbfin2')
PressureUom.mbar = PressureUom._CF_enumeration.addEnumeration(unicode_value='mbar', tag='mbar')
PressureUom.mmHg0C = PressureUom._CF_enumeration.addEnumeration(unicode_value='mmHg(0C)', tag='mmHg0C')
PressureUom.mPa = PressureUom._CF_enumeration.addEnumeration(unicode_value='mPa', tag='mPa')
PressureUom.MPa = PressureUom._CF_enumeration.addEnumeration(unicode_value='MPa', tag='MPa')
PressureUom.Mpsi = PressureUom._CF_enumeration.addEnumeration(unicode_value='Mpsi', tag='Mpsi')
PressureUom.Nm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='N/m2', tag='Nm2')
PressureUom.Nmm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='N/mm2', tag='Nmm2')
PressureUom.Pag = PressureUom._CF_enumeration.addEnumeration(unicode_value='Pa(g)', tag='Pag')
PressureUom.pPa = PressureUom._CF_enumeration.addEnumeration(unicode_value='pPa', tag='pPa')
PressureUom.psi = PressureUom._CF_enumeration.addEnumeration(unicode_value='psi', tag='psi')
PressureUom.psia = PressureUom._CF_enumeration.addEnumeration(unicode_value='psia', tag='psia')
PressureUom.psig = PressureUom._CF_enumeration.addEnumeration(unicode_value='psig', tag='psig')
PressureUom.tonfUSft2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='tonfUS/ft2', tag='tonfUSft2')
PressureUom.tonfUSin2 = PressureUom._CF_enumeration.addEnumeration(unicode_value='tonfUS/in2', tag='tonfUSin2')
PressureUom.torr = PressureUom._CF_enumeration.addEnumeration(unicode_value='torr', tag='torr')
PressureUom.ubar = PressureUom._CF_enumeration.addEnumeration(unicode_value='ubar', tag='ubar')
PressureUom.umHg0C = PressureUom._CF_enumeration.addEnumeration(unicode_value='umHg(0C)', tag='umHg0C')
PressureUom.uPa = PressureUom._CF_enumeration.addEnumeration(unicode_value='uPa', tag='uPa')
PressureUom.upsi = PressureUom._CF_enumeration.addEnumeration(unicode_value='upsi', tag='upsi')
PressureUom._InitializeFacetMap(PressureUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PressureUom', PressureUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}RelativePowerUom
class RelativePowerUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelativePowerUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 691, 1)
    _Documentation = ''
RelativePowerUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RelativePowerUom, enum_prefix=None)
RelativePowerUom.emptyString = RelativePowerUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
RelativePowerUom.Btubhp_hr = RelativePowerUom._CF_enumeration.addEnumeration(unicode_value='Btu/bhp.hr', tag='Btubhp_hr')
RelativePowerUom.WkW = RelativePowerUom._CF_enumeration.addEnumeration(unicode_value='W/kW', tag='WkW')
RelativePowerUom.WW = RelativePowerUom._CF_enumeration.addEnumeration(unicode_value='W/W', tag='WW')
RelativePowerUom._InitializeFacetMap(RelativePowerUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RelativePowerUom', RelativePowerUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}SpecificHeatCapacityUom
class SpecificHeatCapacityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpecificHeatCapacityUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 703, 1)
    _Documentation = ''
SpecificHeatCapacityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpecificHeatCapacityUom, enum_prefix=None)
SpecificHeatCapacityUom.Jkg_K = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value='J/kg.K', tag='Jkg_K')
SpecificHeatCapacityUom.Btulbm_degF = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value='Btu/lbm.degF', tag='Btulbm_degF')
SpecificHeatCapacityUom.Btulbm_degR = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value='Btu/lbm.degR', tag='Btulbm_degR')
SpecificHeatCapacityUom.calg_K = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value='cal/g.K', tag='calg_K')
SpecificHeatCapacityUom.Jg_K = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value='J/g.K', tag='Jg_K')
SpecificHeatCapacityUom.kcalkg_degC = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value='kcal/kg.degC', tag='kcalkg_degC')
SpecificHeatCapacityUom.kJkg_K = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value='kJ/kg.K', tag='kJkg_K')
SpecificHeatCapacityUom.kW_hkg_degC = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value='kW.h/kg.degC', tag='kW_hkg_degC')
SpecificHeatCapacityUom._InitializeFacetMap(SpecificHeatCapacityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SpecificHeatCapacityUom', SpecificHeatCapacityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}SpecificVolumeUom
class SpecificVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpecificVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 719, 1)
    _Documentation = ''
SpecificVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpecificVolumeUom, enum_prefix=None)
SpecificVolumeUom.m3kg = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/kg', tag='m3kg')
SpecificVolumeUom.bbltonUK = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/tonUK', tag='bbltonUK')
SpecificVolumeUom.bbltonUS = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/tonUS', tag='bbltonUS')
SpecificVolumeUom.cm3g = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='cm3/g', tag='cm3g')
SpecificVolumeUom.dm3kg = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='dm3/kg', tag='dm3kg')
SpecificVolumeUom.dm3t = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='dm3/t', tag='dm3t')
SpecificVolumeUom.ft3kg = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3/kg', tag='ft3kg')
SpecificVolumeUom.ft3lbm = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3/lbm', tag='ft3lbm')
SpecificVolumeUom.ft3sack94 = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3/sack94', tag='ft3sack94')
SpecificVolumeUom.galUSsack94 = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/sack94', tag='galUSsack94')
SpecificVolumeUom.galUKlbm = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUK/lbm', tag='galUKlbm')
SpecificVolumeUom.galUSlbm = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/lbm', tag='galUSlbm')
SpecificVolumeUom.galUStonUK = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/tonUK', tag='galUStonUK')
SpecificVolumeUom.galUStonUS = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/tonUS', tag='galUStonUS')
SpecificVolumeUom.L100kg = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/100kg', tag='L100kg')
SpecificVolumeUom.Lkg = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/kg', tag='Lkg')
SpecificVolumeUom.Lt = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/t', tag='Lt')
SpecificVolumeUom.LtonUK = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/tonUK', tag='LtonUK')
SpecificVolumeUom.m3g = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/g', tag='m3g')
SpecificVolumeUom.m3t = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/t', tag='m3t')
SpecificVolumeUom.m3tonUK = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/tonUK', tag='m3tonUK')
SpecificVolumeUom.m3tonUS = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/tonUS', tag='m3tonUS')
SpecificVolumeUom._InitializeFacetMap(SpecificVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SpecificVolumeUom', SpecificVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StandardVolumeUom
class StandardVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StandardVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 749, 1)
    _Documentation = ''
StandardVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StandardVolumeUom, enum_prefix=None)
StandardVolumeUom.scm15C = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='scm(15C)', tag='scm15C')
StandardVolumeUom.scm0C = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='scm(0C)', tag='scm0C')
StandardVolumeUom.Gsm3 = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='Gsm3', tag='Gsm3')
StandardVolumeUom.ksm3 = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='ksm3', tag='ksm3')
StandardVolumeUom.MMscf60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='MMscf(60F)', tag='MMscf60F')
StandardVolumeUom.MMscm15C = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='MMscm(15C)', tag='MMscm15C')
StandardVolumeUom.MMstb60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='MMstb(60F)', tag='MMstb60F')
StandardVolumeUom.Mscf60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='Mscf(60F)', tag='Mscf60F')
StandardVolumeUom.Mstb60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='Mstb(60F)', tag='Mstb60F')
StandardVolumeUom.scf60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='scf(60F)', tag='scf60F')
StandardVolumeUom.stb60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb(60F)', tag='stb60F')
StandardVolumeUom._InitializeFacetMap(StandardVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StandardVolumeUom', StandardVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StandardVolumePerTimeUom
class StandardVolumePerTimeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StandardVolumePerTimeUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 768, 1)
    _Documentation = ''
StandardVolumePerTimeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StandardVolumePerTimeUom, enum_prefix=None)
StandardVolumePerTimeUom.scf60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='scf(60F)/d', tag='scf60Fd')
StandardVolumePerTimeUom.scm15Cs = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='scm(15C)/s', tag='scm15Cs')
StandardVolumePerTimeUom.scm15Cd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='scm(15C)/d', tag='scm15Cd')
StandardVolumePerTimeUom.stb60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='stb(60F)/d', tag='stb60Fd')
StandardVolumePerTimeUom.ksm3d = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='ksm3/d', tag='ksm3d')
StandardVolumePerTimeUom.Mscm15Cd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='Mscm(15C)/d', tag='Mscm15Cd')
StandardVolumePerTimeUom.MMscm15Cd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='MMscm(15C)/d', tag='MMscm15Cd')
StandardVolumePerTimeUom.Mstb60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='Mstb(60F)/d', tag='Mstb60Fd')
StandardVolumePerTimeUom.MMstb60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='MMstb(60F)/d', tag='MMstb60Fd')
StandardVolumePerTimeUom.Mscf60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='Mscf(60F)/d', tag='Mscf60Fd')
StandardVolumePerTimeUom.MMscf60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value='MMscf(60F)/d', tag='MMscf60Fd')
StandardVolumePerTimeUom._InitializeFacetMap(StandardVolumePerTimeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StandardVolumePerTimeUom', StandardVolumePerTimeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ThermalConductivityUom
class ThermalConductivityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThermalConductivityUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 787, 1)
    _Documentation = ''
ThermalConductivityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ThermalConductivityUom, enum_prefix=None)
ThermalConductivityUom.Wm_K = ThermalConductivityUom._CF_enumeration.addEnumeration(unicode_value='W/m.K', tag='Wm_K')
ThermalConductivityUom.Btuhr_ft_degF = ThermalConductivityUom._CF_enumeration.addEnumeration(unicode_value='Btu/hr.ft.degF', tag='Btuhr_ft_degF')
ThermalConductivityUom.calh_cm_degC = ThermalConductivityUom._CF_enumeration.addEnumeration(unicode_value='cal/h.cm.degC', tag='calh_cm_degC')
ThermalConductivityUom.kcalh_m_degC = ThermalConductivityUom._CF_enumeration.addEnumeration(unicode_value='kcal/h.m.degC', tag='kcalh_m_degC')
ThermalConductivityUom.cals_cm_degC = ThermalConductivityUom._CF_enumeration.addEnumeration(unicode_value='cal/s.cm.degC', tag='cals_cm_degC')
ThermalConductivityUom._InitializeFacetMap(ThermalConductivityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ThermalConductivityUom', ThermalConductivityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ThermalVolumetricExpansionUom
class ThermalVolumetricExpansionUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThermalVolumetricExpansionUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 800, 1)
    _Documentation = ''
ThermalVolumetricExpansionUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ThermalVolumetricExpansionUom, enum_prefix=None)
ThermalVolumetricExpansionUom.n1K = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value='1/K', tag='n1K')
ThermalVolumetricExpansionUom.ppmdegC = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value='ppm/degC', tag='ppmdegC')
ThermalVolumetricExpansionUom.ppmdegF = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value='ppm/degF', tag='ppmdegF')
ThermalVolumetricExpansionUom.n1degC = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value='1/degC', tag='n1degC')
ThermalVolumetricExpansionUom.n1degF = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value='1/degF', tag='n1degF')
ThermalVolumetricExpansionUom.n1degR = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value='1/degR', tag='n1degR')
ThermalVolumetricExpansionUom._InitializeFacetMap(ThermalVolumetricExpansionUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ThermalVolumetricExpansionUom', ThermalVolumetricExpansionUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ThermodynamicTemperatureUom
class ThermodynamicTemperatureUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThermodynamicTemperatureUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 814, 1)
    _Documentation = ''
ThermodynamicTemperatureUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ThermodynamicTemperatureUom, enum_prefix=None)
ThermodynamicTemperatureUom.K = ThermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value='K', tag='K')
ThermodynamicTemperatureUom.degC = ThermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value='degC', tag='degC')
ThermodynamicTemperatureUom.degF = ThermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value='degF', tag='degF')
ThermodynamicTemperatureUom.degR = ThermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value='degR', tag='degR')
ThermodynamicTemperatureUom._InitializeFacetMap(ThermodynamicTemperatureUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ThermodynamicTemperatureUom', ThermodynamicTemperatureUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TimeUom
class TimeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 826, 1)
    _Documentation = ''
TimeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TimeUom, enum_prefix=None)
TimeUom.s = TimeUom._CF_enumeration.addEnumeration(unicode_value='s', tag='s')
TimeUom.a = TimeUom._CF_enumeration.addEnumeration(unicode_value='a', tag='a')
TimeUom.cs = TimeUom._CF_enumeration.addEnumeration(unicode_value='cs', tag='cs')
TimeUom.d = TimeUom._CF_enumeration.addEnumeration(unicode_value='d', tag='d')
TimeUom.Ga = TimeUom._CF_enumeration.addEnumeration(unicode_value='Ga', tag='Ga')
TimeUom.h = TimeUom._CF_enumeration.addEnumeration(unicode_value='h', tag='h')
TimeUom.n100s = TimeUom._CF_enumeration.addEnumeration(unicode_value='100s', tag='n100s')
TimeUom.Ma = TimeUom._CF_enumeration.addEnumeration(unicode_value='Ma', tag='Ma')
TimeUom.min = TimeUom._CF_enumeration.addEnumeration(unicode_value='min', tag='min')
TimeUom.ms = TimeUom._CF_enumeration.addEnumeration(unicode_value='ms', tag='ms')
TimeUom.ms2 = TimeUom._CF_enumeration.addEnumeration(unicode_value='ms/2', tag='ms2')
TimeUom.ns = TimeUom._CF_enumeration.addEnumeration(unicode_value='ns', tag='ns')
TimeUom.ps = TimeUom._CF_enumeration.addEnumeration(unicode_value='ps', tag='ps')
TimeUom.us = TimeUom._CF_enumeration.addEnumeration(unicode_value='us', tag='us')
TimeUom.wk = TimeUom._CF_enumeration.addEnumeration(unicode_value='wk', tag='wk')
TimeUom.n100ka = TimeUom._CF_enumeration.addEnumeration(unicode_value='100ka', tag='n100ka')
TimeUom._InitializeFacetMap(TimeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TimeUom', TimeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}VelocityUom
class VelocityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VelocityUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 850, 1)
    _Documentation = ''
VelocityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VelocityUom, enum_prefix=None)
VelocityUom.ms = VelocityUom._CF_enumeration.addEnumeration(unicode_value='m/s', tag='ms')
VelocityUom.cma = VelocityUom._CF_enumeration.addEnumeration(unicode_value='cm/a', tag='cma')
VelocityUom.cms = VelocityUom._CF_enumeration.addEnumeration(unicode_value='cm/s', tag='cms')
VelocityUom.dms = VelocityUom._CF_enumeration.addEnumeration(unicode_value='dm/s', tag='dms')
VelocityUom.ftd = VelocityUom._CF_enumeration.addEnumeration(unicode_value='ft/d', tag='ftd')
VelocityUom.fth = VelocityUom._CF_enumeration.addEnumeration(unicode_value='ft/h', tag='fth')
VelocityUom.ftmin = VelocityUom._CF_enumeration.addEnumeration(unicode_value='ft/min', tag='ftmin')
VelocityUom.ftms = VelocityUom._CF_enumeration.addEnumeration(unicode_value='ft/ms', tag='ftms')
VelocityUom.fts = VelocityUom._CF_enumeration.addEnumeration(unicode_value='ft/s', tag='fts')
VelocityUom.ftus = VelocityUom._CF_enumeration.addEnumeration(unicode_value='ft/us', tag='ftus')
VelocityUom.ina = VelocityUom._CF_enumeration.addEnumeration(unicode_value='in/a', tag='ina')
VelocityUom.inmin = VelocityUom._CF_enumeration.addEnumeration(unicode_value='in/min', tag='inmin')
VelocityUom.ins = VelocityUom._CF_enumeration.addEnumeration(unicode_value='in/s', tag='ins')
VelocityUom.kfth = VelocityUom._CF_enumeration.addEnumeration(unicode_value='kft/h', tag='kfth')
VelocityUom.kfts = VelocityUom._CF_enumeration.addEnumeration(unicode_value='kft/s', tag='kfts')
VelocityUom.kmh = VelocityUom._CF_enumeration.addEnumeration(unicode_value='km/h', tag='kmh')
VelocityUom.kms = VelocityUom._CF_enumeration.addEnumeration(unicode_value='km/s', tag='kms')
VelocityUom.knot = VelocityUom._CF_enumeration.addEnumeration(unicode_value='knot', tag='knot')
VelocityUom.md = VelocityUom._CF_enumeration.addEnumeration(unicode_value='m/d', tag='md')
VelocityUom.mh = VelocityUom._CF_enumeration.addEnumeration(unicode_value='m/h', tag='mh')
VelocityUom.mmin = VelocityUom._CF_enumeration.addEnumeration(unicode_value='m/min', tag='mmin')
VelocityUom.mms = VelocityUom._CF_enumeration.addEnumeration(unicode_value='m/ms', tag='mms')
VelocityUom.mih = VelocityUom._CF_enumeration.addEnumeration(unicode_value='mi/h', tag='mih')
VelocityUom.milyr = VelocityUom._CF_enumeration.addEnumeration(unicode_value='mil/yr', tag='milyr')
VelocityUom.mma = VelocityUom._CF_enumeration.addEnumeration(unicode_value='mm/a', tag='mma')
VelocityUom.mms_ = VelocityUom._CF_enumeration.addEnumeration(unicode_value='mm/s', tag='mms_')
VelocityUom.nms = VelocityUom._CF_enumeration.addEnumeration(unicode_value='nm/s', tag='nms')
VelocityUom.ums = VelocityUom._CF_enumeration.addEnumeration(unicode_value='um/s', tag='ums')
VelocityUom._InitializeFacetMap(VelocityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VelocityUom', VelocityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}VolumeUom
class VolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VolumeUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 886, 1)
    _Documentation = ''
VolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumeUom, enum_prefix=None)
VolumeUom.m3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='m3', tag='m3')
VolumeUom.acre_ft = VolumeUom._CF_enumeration.addEnumeration(unicode_value='acre.ft', tag='acre_ft')
VolumeUom.bbl = VolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl', tag='bbl')
VolumeUom.bcf = VolumeUom._CF_enumeration.addEnumeration(unicode_value='bcf', tag='bcf')
VolumeUom.cm3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='cm3', tag='cm3')
VolumeUom.dm3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='dm3', tag='dm3')
VolumeUom.flozUK = VolumeUom._CF_enumeration.addEnumeration(unicode_value='flozUK', tag='flozUK')
VolumeUom.flozUS = VolumeUom._CF_enumeration.addEnumeration(unicode_value='flozUS', tag='flozUS')
VolumeUom.ft3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3', tag='ft3')
VolumeUom.galUK = VolumeUom._CF_enumeration.addEnumeration(unicode_value='galUK', tag='galUK')
VolumeUom.galUS = VolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS', tag='galUS')
VolumeUom.ha_m = VolumeUom._CF_enumeration.addEnumeration(unicode_value='ha.m', tag='ha_m')
VolumeUom.hL = VolumeUom._CF_enumeration.addEnumeration(unicode_value='hL', tag='hL')
VolumeUom.in3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='in3', tag='in3')
VolumeUom.n1000ft3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='1000ft3', tag='n1000ft3')
VolumeUom.km3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='km3', tag='km3')
VolumeUom.L = VolumeUom._CF_enumeration.addEnumeration(unicode_value='L', tag='L')
VolumeUom.Mbbl = VolumeUom._CF_enumeration.addEnumeration(unicode_value='Mbbl', tag='Mbbl')
VolumeUom.Mcf = VolumeUom._CF_enumeration.addEnumeration(unicode_value='Mcf', tag='Mcf')
VolumeUom.Mft3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='M(ft3)', tag='Mft3')
VolumeUom.mi3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='mi3', tag='mi3')
VolumeUom.mL = VolumeUom._CF_enumeration.addEnumeration(unicode_value='mL', tag='mL')
VolumeUom.Mm3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='M(m3)', tag='Mm3')
VolumeUom.mm3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='mm3', tag='mm3')
VolumeUom.MMbbl = VolumeUom._CF_enumeration.addEnumeration(unicode_value='MMbbl', tag='MMbbl')
VolumeUom.ptUK = VolumeUom._CF_enumeration.addEnumeration(unicode_value='ptUK', tag='ptUK')
VolumeUom.ptUS = VolumeUom._CF_enumeration.addEnumeration(unicode_value='ptUS', tag='ptUS')
VolumeUom.qtUK = VolumeUom._CF_enumeration.addEnumeration(unicode_value='qtUK', tag='qtUK')
VolumeUom.qtUS = VolumeUom._CF_enumeration.addEnumeration(unicode_value='qtUS', tag='qtUS')
VolumeUom.tcf = VolumeUom._CF_enumeration.addEnumeration(unicode_value='tcf', tag='tcf')
VolumeUom.um2_m = VolumeUom._CF_enumeration.addEnumeration(unicode_value='um2.m', tag='um2_m')
VolumeUom.yd3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value='yd3', tag='yd3')
VolumeUom._InitializeFacetMap(VolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VolumeUom', VolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}VolumeFlowRateUom
class VolumeFlowRateUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VolumeFlowRateUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 926, 1)
    _Documentation = ''
VolumeFlowRateUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumeFlowRateUom, enum_prefix=None)
VolumeFlowRateUom.m3s = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='m3/s', tag='m3s')
VolumeFlowRateUom.bbld = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='bbl/d', tag='bbld')
VolumeFlowRateUom.bblhr = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='bbl/hr', tag='bblhr')
VolumeFlowRateUom.bblmin = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='bbl/min', tag='bblmin')
VolumeFlowRateUom.cm330min = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='cm3/30min', tag='cm330min')
VolumeFlowRateUom.cm3h = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='cm3/h', tag='cm3h')
VolumeFlowRateUom.cm3min = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='cm3/min', tag='cm3min')
VolumeFlowRateUom.cm3s = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='cm3/s', tag='cm3s')
VolumeFlowRateUom.dm3s = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='dm3/s', tag='dm3s')
VolumeFlowRateUom.ft3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='ft3/d', tag='ft3d')
VolumeFlowRateUom.ft3h = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='ft3/h', tag='ft3h')
VolumeFlowRateUom.ft3min = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='ft3/min', tag='ft3min')
VolumeFlowRateUom.ft3s = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='ft3/s', tag='ft3s')
VolumeFlowRateUom.galUKd = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUK/d', tag='galUKd')
VolumeFlowRateUom.galUKhr = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUK/hr', tag='galUKhr')
VolumeFlowRateUom.galUKmin = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUK/min', tag='galUKmin')
VolumeFlowRateUom.galUSd = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUS/d', tag='galUSd')
VolumeFlowRateUom.galUShr = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUS/hr', tag='galUShr')
VolumeFlowRateUom.galUSmin = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUS/min', tag='galUSmin')
VolumeFlowRateUom.kbbld = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='kbbl/d', tag='kbbld')
VolumeFlowRateUom.n1000ft3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='1000ft3/d', tag='n1000ft3d')
VolumeFlowRateUom.n1000m3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='1000m3/d', tag='n1000m3d')
VolumeFlowRateUom.n1000m3h = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='1000m3/h', tag='n1000m3h')
VolumeFlowRateUom.Lh = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='L/h', tag='Lh')
VolumeFlowRateUom.Lmin = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='L/min', tag='Lmin')
VolumeFlowRateUom.Ls = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='L/s', tag='Ls')
VolumeFlowRateUom.m3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='m3/d', tag='m3d')
VolumeFlowRateUom.m3h = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='m3/h', tag='m3h')
VolumeFlowRateUom.m3min = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='m3/min', tag='m3min')
VolumeFlowRateUom.Mbbld = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='Mbbl/d', tag='Mbbld')
VolumeFlowRateUom.Mft3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='M(ft3)/d', tag='Mft3d')
VolumeFlowRateUom.Mm3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='M(m3)/d', tag='Mm3d')
VolumeFlowRateUom._InitializeFacetMap(VolumeFlowRateUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VolumeFlowRateUom', VolumeFlowRateUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}VolumePerLengthUom
class VolumePerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VolumePerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 966, 1)
    _Documentation = ''
VolumePerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumePerLengthUom, enum_prefix=None)
VolumePerLengthUom.bblPft = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='bblPft', tag='bblPft')
VolumePerLengthUom.bblPin = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='bblPin', tag='bblPin')
VolumePerLengthUom.bblPmi = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='bblPmi', tag='bblPmi')
VolumePerLengthUom.dm3P100km = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dm3P100km', tag='dm3P100km')
VolumePerLengthUom.dm3Pkm100 = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dm3Pkm(100)', tag='dm3Pkm100')
VolumePerLengthUom.dm3Pm = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dm3Pm', tag='dm3Pm')
VolumePerLengthUom.ft3Pft = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft3Pft', tag='ft3Pft')
VolumePerLengthUom.galUKPmi = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='galUKPmi', tag='galUKPmi')
VolumePerLengthUom.galUSPft = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='galUSPft', tag='galUSPft')
VolumePerLengthUom.galUSPmi = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='galUSPmi', tag='galUSPmi')
VolumePerLengthUom.in3Pft = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='in3Pft', tag='in3Pft')
VolumePerLengthUom.LP100km = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='LP100km', tag='LP100km')
VolumePerLengthUom.LPkm100 = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='LPkm(100)', tag='LPkm100')
VolumePerLengthUom.LPm = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='LPm', tag='LPm')
VolumePerLengthUom.m3Pkm = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='m3Pkm', tag='m3Pkm')
VolumePerLengthUom.m3Pm = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value='m3Pm', tag='m3Pm')
VolumePerLengthUom._InitializeFacetMap(VolumePerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VolumePerLengthUom', VolumePerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}VolumePerVolumeUom
class VolumePerVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VolumePerVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 990, 1)
    _Documentation = ''
VolumePerVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumePerVolumeUom, enum_prefix=None)
VolumePerVolumeUom.Euc = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='Euc', tag='Euc')
VolumePerVolumeUom.emptyString = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
VolumePerVolumeUom.permil = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='permil', tag='permil')
VolumePerVolumeUom.ppdk = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ppdk', tag='ppdk')
VolumePerVolumeUom.ppk = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ppk', tag='ppk')
VolumePerVolumeUom.ppm = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ppm', tag='ppm')
VolumePerVolumeUom.bblacre_ft = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/acre.ft', tag='bblacre_ft')
VolumePerVolumeUom.bblbbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/bbl', tag='bblbbl')
VolumePerVolumeUom.bblft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/ft3', tag='bblft3')
VolumePerVolumeUom.bbl100bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/100bbl', tag='bbl100bbl')
VolumePerVolumeUom.bblkft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/k(ft3)', tag='bblkft3')
VolumePerVolumeUom.bblMft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/M(ft3)', tag='bblMft3')
VolumePerVolumeUom.cm3cm3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='cm3/cm3', tag='cm3cm3')
VolumePerVolumeUom.cm3m3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='cm3/m3', tag='cm3m3')
VolumePerVolumeUom.dm3m3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='dm3/m3', tag='dm3m3')
VolumePerVolumeUom.ft3bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3/bbl', tag='ft3bbl')
VolumePerVolumeUom.ft3ft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3/ft3', tag='ft3ft3')
VolumePerVolumeUom.galUSkgalUS = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/kgalUS', tag='galUSkgalUS')
VolumePerVolumeUom.galUKkgalUK = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUK/kgalUK', tag='galUKkgalUK')
VolumePerVolumeUom.galUKft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUK/ft3', tag='galUKft3')
VolumePerVolumeUom.galUKMbbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUK/Mbbl', tag='galUKMbbl')
VolumePerVolumeUom.galUSbbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/bbl', tag='galUSbbl')
VolumePerVolumeUom.galUS10bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/10bbl', tag='galUS10bbl')
VolumePerVolumeUom.galUSft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/ft3', tag='galUSft3')
VolumePerVolumeUom.galUSMbbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/Mbbl', tag='galUSMbbl')
VolumePerVolumeUom.n1000ft3bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='1000ft3/bbl', tag='n1000ft3bbl')
VolumePerVolumeUom.ksm3sm3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ksm3/sm3', tag='ksm3sm3')
VolumePerVolumeUom.L10bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/10bbl', tag='L10bbl')
VolumePerVolumeUom.Lm3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/m3', tag='Lm3')
VolumePerVolumeUom.m3ha_m = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/ha.m', tag='m3ha_m')
VolumePerVolumeUom.m3m3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/m3', tag='m3m3')
VolumePerVolumeUom.Mft3acre_ft = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='M(ft3)/acre.ft', tag='Mft3acre_ft')
VolumePerVolumeUom.mLgalUK = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='mL/galUK', tag='mLgalUK')
VolumePerVolumeUom.mLgalUS = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='mL/galUS', tag='mLgalUS')
VolumePerVolumeUom.mLmL = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='mL/mL', tag='mLmL')
VolumePerVolumeUom.MMbblacre_ft = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='MMbbl/acre.ft', tag='MMbblacre_ft')
VolumePerVolumeUom.MMscf60stb60 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='MMscf60/stb60', tag='MMscf60stb60')
VolumePerVolumeUom.Mscf60stb60 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='Mscf60/stb60', tag='Mscf60stb60')
VolumePerVolumeUom.ptUKMbbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ptUK/Mbbl', tag='ptUKMbbl')
VolumePerVolumeUom.ptUS10bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ptUS/10bbl', tag='ptUS10bbl')
VolumePerVolumeUom.pu = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='pu', tag='pu')
VolumePerVolumeUom.scm15stb60 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='scm15/stb60', tag='scm15stb60')
VolumePerVolumeUom.sm3ksm3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='sm3/ksm3', tag='sm3ksm3')
VolumePerVolumeUom.sm3sm3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='sm3/sm3', tag='sm3sm3')
VolumePerVolumeUom.stb60MMscf60 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb60/MMscf60', tag='stb60MMscf60')
VolumePerVolumeUom.stb60MMscm15 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb60/MMscm15', tag='stb60MMscm15')
VolumePerVolumeUom.stb60Mscf60 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb60/Mscf60', tag='stb60Mscf60')
VolumePerVolumeUom.stb60Mscm15 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb60/Mscm15', tag='stb60Mscm15')
VolumePerVolumeUom.stb60scm15 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb60/scm15', tag='stb60scm15')
VolumePerVolumeUom._InitializeFacetMap(VolumePerVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VolumePerVolumeUom', VolumePerVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}commentString
class commentString (abstractCommentString):

    """A comment or remark intended for human consumption. 
			There should be no assumption that semantics can be extracted from this field by a computer. 
			Neither should there be an assumption that any two humans will interpret the information 
			in the same way (i.e., it may not be interoperable)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'commentString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 342, 1)
    _Documentation = 'A comment or remark intended for human consumption. \n\t\t\tThere should be no assumption that semantics can be extracted from this field by a computer. \n\t\t\tNeither should there be an assumption that any two humans will interpret the information \n\t\t\tin the same way (i.e., it may not be interoperable).'
commentString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'commentString', commentString)

# Complex type {http://www.witsml.org/schemas/1series}cs_commonData with content type ELEMENT_ONLY
class cs_commonData (pyxb.binding.basis.complexTypeDefinition):
    """ WITSML - Common Data Component Schema """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_commonData')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}sourceName uses Python identifier sourceName
    __sourceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sourceName'), 'sourceName', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriessourceName', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 26, 3), )

    
    sourceName = property(__sourceName.value, __sourceName.set, None, 'An identifier to indicate the data originator.\n\t\t\t\t\tThis identifies the server that originally created \n\t\t\t\t\tthe object and thus most of the uids in the object (but not \n\t\t\t\t\tnecessarily the uids of the parents). This is typically a url. ')

    
    # Element {http://www.witsml.org/schemas/1series}dTimCreation uses Python identifier dTimCreation
    __dTimCreation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dTimCreation'), 'dTimCreation', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesdTimCreation', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 34, 3), )

    
    dTimCreation = property(__dTimCreation.value, __dTimCreation.set, None, 'When the data was created at the persistent data store. \n\t\t\t\t\tThis is an API server parameter releted to the "Special Handling of Change Information" within a server. \n\t\t\t\t\tSee the relevant API specification for the  behavior related to this element.')

    
    # Element {http://www.witsml.org/schemas/1series}dTimLastChange uses Python identifier dTimLastChange
    __dTimLastChange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dTimLastChange'), 'dTimLastChange', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesdTimLastChange', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 43, 3), )

    
    dTimLastChange = property(__dTimLastChange.value, __dTimLastChange.set, None, 'Last change of any element of the data at the persistent data store.\n\t\t\t\t\tThis is an API server parameter releted to the "Special Handling of Change Information" within a server. \n\t\t\t\t\tSee the relevant API specification for the  behavior related to this element.')

    
    # Element {http://www.witsml.org/schemas/1series}itemState uses Python identifier itemState
    __itemState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'itemState'), 'itemState', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesitemState', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 53, 3), )

    
    itemState = property(__itemState.value, __itemState.set, None, 'The item state for the data object.  ')

    
    # Element {http://www.witsml.org/schemas/1series}serviceCategory uses Python identifier serviceCategory
    __serviceCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serviceCategory'), 'serviceCategory', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesserviceCategory', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 58, 3), )

    
    serviceCategory = property(__serviceCategory.value, __serviceCategory.set, None, 'The category of the service related to the creation of the object. \n\t\t\t\t\tFor example, "mud log service", "cement service", "LWD service", "rig service", "drilling service".\n\t\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/1series}comments uses Python identifier comments
    __comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comments'), 'comments', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriescomments', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 67, 3), )

    
    comments = property(__comments.value, __comments.set, None, 'Comments and remarks.  ')

    
    # Element {http://www.witsml.org/schemas/1series}acquisitionTimeZone uses Python identifier acquisitionTimeZone
    __acquisitionTimeZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acquisitionTimeZone'), 'acquisitionTimeZone', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesacquisitionTimeZone', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 72, 3), )

    
    acquisitionTimeZone = property(__acquisitionTimeZone.value, __acquisitionTimeZone.set, None, 'The local time zone of the original acquisition date-time values. \n\t\t\t\t\tIt is the deviation in hours and minutes from UTC.\n\t\t\t\t\tThe first occurrence should be the actual local time zone at the start of acquisition\n\t\t\t\t\tand may represent a seasonally adjusted value such as daylight savings.\n\t\t\t\t\tThe dTim attribute must be populated in the second and subsequent occurrences \n\t\t\t\t\tif the local time zone changes during acquisition.\n\t\t\t\t\tThis knowledge is required because the original time zone in a dateTime\n\t\t\t\t\tvalue may be lost when software converts to a different time zone.')

    
    # Element {http://www.witsml.org/schemas/1series}defaultDatum uses Python identifier defaultDatum
    __defaultDatum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'defaultDatum'), 'defaultDatum', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesdefaultDatum', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 85, 3), )

    
    defaultDatum = property(__defaultDatum.value, __defaultDatum.set, None, 'A pointer to the default wellDatum for measured depth coordinates,\n\t\t\t\t\tvertical depth coordinates and elevation coordinates in this object. \n\t\t\t\t\tDepth coordinates that do not specify a datum attribute shall be \n\t\t\t\t\tassumed to be measured relative to this default vertical datum.\n\t\t\t\t\tThe referenced wellDatum must be defined within the well object associated with this object.')

    
    # Element {http://www.witsml.org/schemas/1series}privateGroupOnly uses Python identifier privateGroupOnly
    __privateGroupOnly = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'privateGroupOnly'), 'privateGroupOnly', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesprivateGroupOnly', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 95, 3), )

    
    privateGroupOnly = property(__privateGroupOnly.value, __privateGroupOnly.set, None, 'This is an API query parameter.\n\t\t\t\t\tSee the API specification for the behavior related to this element.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionAny uses Python identifier extensionAny
    __extensionAny = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionAny'), 'extensionAny', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesextensionAny', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 102, 3), )

    
    extensionAny = property(__extensionAny.value, __extensionAny.set, None, 'Extensions to the schema using an xsd:any construct.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionNameValue uses Python identifier extensionNameValue
    __extensionNameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), 'extensionNameValue', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesextensionNameValue', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 108, 3), )

    
    extensionNameValue = property(__extensionNameValue.value, __extensionNameValue.set, None, 'Extensions to the schema based on a name-value construct.')


    _ElementMap = {
        __sourceName.name() : __sourceName,
        __dTimCreation.name() : __dTimCreation,
        __dTimLastChange.name() : __dTimLastChange,
        __itemState.name() : __itemState,
        __serviceCategory.name() : __serviceCategory,
        __comments.name() : __comments,
        __acquisitionTimeZone.name() : __acquisitionTimeZone,
        __defaultDatum.name() : __defaultDatum,
        __privateGroupOnly.name() : __privateGroupOnly,
        __extensionAny.name() : __extensionAny,
        __extensionNameValue.name() : __extensionNameValue
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_commonData', cs_commonData)


# Complex type {http://www.witsml.org/schemas/1series}cs_customData with content type ELEMENT_ONLY
class cs_customData (pyxb.binding.basis.complexTypeDefinition):
    """ WITSML - Custom or User Defined Element and Attributes Component Schema.
			Specify custom element, attributes, and types in the custom data area."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_customData')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_customData.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_customData', cs_customData)


# Complex type {http://www.witsml.org/schemas/1series}cs_documentAudit with content type ELEMENT_ONLY
class cs_documentAudit (pyxb.binding.basis.complexTypeDefinition):
    """The audit records what happened to the data, to produce 
			the data that is in this file. It consists of one or more events."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_documentAudit')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentAudit.xsd', 20, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}event uses Python identifier event
    __event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'event'), 'event', '__httpwww_witsml_orgschemas1series_cs_documentAudit_httpwww_witsml_orgschemas1seriesevent', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentAudit.xsd', 27, 3), )

    
    event = property(__event.value, __event.set, None, 'One event related to the data.')


    _ElementMap = {
        __event.name() : __event
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_documentAudit', cs_documentAudit)


# Complex type {http://www.witsml.org/schemas/1series}cs_documentFileCreation with content type ELEMENT_ONLY
class cs_documentFileCreation (pyxb.binding.basis.complexTypeDefinition):
    """A block of information about the creation of the XML file. 
			This is different than the creation of the data that is included within the file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_documentFileCreation')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 20, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}fileCreationDate uses Python identifier fileCreationDate
    __fileCreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileCreationDate'), 'fileCreationDate', '__httpwww_witsml_orgschemas1series_cs_documentFileCreation_httpwww_witsml_orgschemas1seriesfileCreationDate', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 27, 3), )

    
    fileCreationDate = property(__fileCreationDate.value, __fileCreationDate.set, None, 'The date and time that the file was created.')

    
    # Element {http://www.witsml.org/schemas/1series}softwareName uses Python identifier softwareName
    __softwareName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'softwareName'), 'softwareName', '__httpwww_witsml_orgschemas1series_cs_documentFileCreation_httpwww_witsml_orgschemas1seriessoftwareName', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 33, 3), )

    
    softwareName = property(__softwareName.value, __softwareName.set, None, 'If appropriate, the software that created the file. \n\t\t\t\t\tThis is a free form string, and may include whatever information \n\t\t\t\t\tis deemed relevant.')

    
    # Element {http://www.witsml.org/schemas/1series}fileCreator uses Python identifier fileCreator
    __fileCreator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileCreator'), 'fileCreator', '__httpwww_witsml_orgschemas1series_cs_documentFileCreation_httpwww_witsml_orgschemas1seriesfileCreator', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 41, 3), )

    
    fileCreator = property(__fileCreator.value, __fileCreator.set, None, 'The person or business associate that created \n\t\t\t\t\tthe file.')

    
    # Element {http://www.witsml.org/schemas/1series}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__httpwww_witsml_orgschemas1series_cs_documentFileCreation_httpwww_witsml_orgschemas1seriescomment', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 48, 3), )

    
    comment = property(__comment.value, __comment.set, None, 'Any comment that would be useful to further \n\t\t\t\t\texplain the creation of this instance document.')


    _ElementMap = {
        __fileCreationDate.name() : __fileCreationDate,
        __softwareName.name() : __softwareName,
        __fileCreator.name() : __fileCreator,
        __comment.name() : __comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_documentFileCreation', cs_documentFileCreation)


# Complex type {http://www.witsml.org/schemas/1series}cs_documentInfo with content type ELEMENT_ONLY
class cs_documentInfo (pyxb.binding.basis.complexTypeDefinition):
    """A  schema to capture a set of data that is 
			relevant for many exchange documents. It includes information about the 
			file that was created, and high-level information about the data that is 
			being exchanged within the file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_documentInfo')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 23, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}documentName uses Python identifier documentName
    __documentName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentName'), 'documentName', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesdocumentName', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 31, 3), )

    
    documentName = property(__documentName.value, __documentName.set, None, 'An identifier for the document. This is \n\t\t\t\t\tintended to be unique within the context of the NamingSystem.')

    
    # Element {http://www.witsml.org/schemas/1series}documentAlias uses Python identifier documentAlias
    __documentAlias = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentAlias'), 'documentAlias', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesdocumentAlias', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 38, 3), )

    
    documentAlias = property(__documentAlias.value, __documentAlias.set, None, 'Zero or more alternate names for the document. \n\t\t\t\t\tThese names do not need to be unique within the naming system.')

    
    # Element {http://www.witsml.org/schemas/1series}documentDate uses Python identifier documentDate
    __documentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentDate'), 'documentDate', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesdocumentDate', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 45, 3), )

    
    documentDate = property(__documentDate.value, __documentDate.set, None, 'The date of the creation of the document. \n\t\t\t\t\tThis is not the same as the date that the file was created. \n\t\t\t\t\tFor this date, the document is considered to be the set of \n\t\t\t\t\tinformation associated with this document information. \n\t\t\t\t\tFor example, the document may be a seismic binset. \n\t\t\t\t\tThis represents the date that the binset was created. \n\t\t\t\t\tThe FileCreation information would capture the date that \n\t\t\t\t\tthe XML file was created to send or exchange the binset.')

    
    # Element {http://www.witsml.org/schemas/1series}documentClass uses Python identifier documentClass
    __documentClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentClass'), 'documentClass', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesdocumentClass', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 58, 3), )

    
    documentClass = property(__documentClass.value, __documentClass.set, None, 'A document class. Examples of classes would be a \n\t\t\t\t\tmetadata classification or a set of keywords. ')

    
    # Element {http://www.witsml.org/schemas/1series}fileCreationInformation uses Python identifier fileCreationInformation
    __fileCreationInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileCreationInformation'), 'fileCreationInformation', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesfileCreationInformation', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 64, 3), )

    
    fileCreationInformation = property(__fileCreationInformation.value, __fileCreationInformation.set, None, 'The information about the creation of the \n\t\t\t\t\texchange file. This is not about the creation of the data within \n\t\t\t\t\tthe file, but the creation of the file itself.')

    
    # Element {http://www.witsml.org/schemas/1series}securityInformation uses Python identifier securityInformation
    __securityInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'securityInformation'), 'securityInformation', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriessecurityInformation', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 72, 3), )

    
    securityInformation = property(__securityInformation.value, __securityInformation.set, None, 'Information about the security to be applied to \n\t\t\t\t\tthis file. More than one classification can be given.')

    
    # Element {http://www.witsml.org/schemas/1series}disclaimer uses Python identifier disclaimer
    __disclaimer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'disclaimer'), 'disclaimer', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesdisclaimer', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 79, 3), )

    
    disclaimer = property(__disclaimer.value, __disclaimer.set, None, 'A free-form string that allows a disclaimer to \n\t\t\t\t\taccompany the information.')

    
    # Element {http://www.witsml.org/schemas/1series}auditTrail uses Python identifier auditTrail
    __auditTrail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'auditTrail'), 'auditTrail', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesauditTrail', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 86, 3), )

    
    auditTrail = property(__auditTrail.value, __auditTrail.set, None, 'A collection of events that can document the \n\t\t\t\t\thistory of the data.')

    
    # Element {http://www.witsml.org/schemas/1series}owner uses Python identifier owner
    __owner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'owner'), 'owner', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesowner', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 93, 3), )

    
    owner = property(__owner.value, __owner.set, None, 'The owner of the data.')

    
    # Element {http://www.witsml.org/schemas/1series}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriescomment', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 99, 3), )

    
    comment = property(__comment.value, __comment.set, None, 'An optional comment about the document.')


    _ElementMap = {
        __documentName.name() : __documentName,
        __documentAlias.name() : __documentAlias,
        __documentDate.name() : __documentDate,
        __documentClass.name() : __documentClass,
        __fileCreationInformation.name() : __fileCreationInformation,
        __securityInformation.name() : __securityInformation,
        __disclaimer.name() : __disclaimer,
        __auditTrail.name() : __auditTrail,
        __owner.name() : __owner,
        __comment.name() : __comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_documentInfo', cs_documentInfo)


# Complex type {http://www.witsml.org/schemas/1series}cs_extensionAny with content type ELEMENT_ONLY
class cs_extensionAny (pyxb.binding.basis.complexTypeDefinition):
    """WITSML - Extension Schema. The intent is to allow standard WITSML schema 
			extensions which will validate in older clients or servers. A client or server can ignore any schema that it 
			does not recognize. New versions will modify specific elements to replace this type with a type that
			adds new elements, including another element with this type."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_extensionAny')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionAny.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_extensionAny', cs_extensionAny)


# Complex type {http://www.witsml.org/schemas/1series}cs_iscwsaAuthorizationData with content type ELEMENT_ONLY
class cs_iscwsaAuthorizationData (pyxb.binding.basis.complexTypeDefinition):
    """Authorization state of some entity."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_iscwsaAuthorizationData')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 20, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'author'), 'author', '__httpwww_witsml_orgschemas1series_cs_iscwsaAuthorizationData_httpwww_witsml_orgschemas1seriesauthor', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 26, 3), )

    
    author = property(__author.value, __author.set, None, 'Person responsible for the information.')

    
    # Element {http://www.witsml.org/schemas/1series}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__httpwww_witsml_orgschemas1series_cs_iscwsaAuthorizationData_httpwww_witsml_orgschemas1seriessource', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 31, 3), )

    
    source = property(__source.value, __source.set, None, 'Source from which the information is derived.')

    
    # Element {http://www.witsml.org/schemas/1series}authority uses Python identifier authority
    __authority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authority'), 'authority', '__httpwww_witsml_orgschemas1series_cs_iscwsaAuthorizationData_httpwww_witsml_orgschemas1seriesauthority', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 36, 3), )

    
    authority = property(__authority.value, __authority.set, None, 'Person or collective body responsible for authorizing the information.')

    
    # Element {http://www.witsml.org/schemas/1series}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__httpwww_witsml_orgschemas1series_cs_iscwsaAuthorizationData_httpwww_witsml_orgschemas1seriesstatus', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 41, 3), )

    
    status = property(__status.value, __status.set, None, 'Authorization state of the information.')

    
    # Element {http://www.witsml.org/schemas/1series}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'version'), 'version', '__httpwww_witsml_orgschemas1series_cs_iscwsaAuthorizationData_httpwww_witsml_orgschemas1seriesversion', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 46, 3), )

    
    version = property(__version.value, __version.set, None, 'Version name or number.')

    
    # Element {http://www.witsml.org/schemas/1series}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__httpwww_witsml_orgschemas1series_cs_iscwsaAuthorizationData_httpwww_witsml_orgschemas1seriescomment', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 51, 3), )

    
    comment = property(__comment.value, __comment.set, None, 'A comment about the object. \n\t\t\t\t\tThis should include information regarding the derivation of the information.')


    _ElementMap = {
        __author.name() : __author,
        __source.name() : __source,
        __authority.name() : __authority,
        __status.name() : __status,
        __version.name() : __version,
        __comment.name() : __comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_iscwsaAuthorizationData', cs_iscwsaAuthorizationData)


# Complex type {http://www.witsml.org/schemas/1series}cs_iscwsaNomenclature with content type ELEMENT_ONLY
class cs_iscwsaNomenclature (pyxb.binding.basis.complexTypeDefinition):
    """A nomenclature for the description of errror terms."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_iscwsaNomenclature')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpwww_witsml_orgschemas1series_cs_iscwsaNomenclature_httpwww_witsml_orgschemas1seriesparameter', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 27, 3), )

    
    parameter = property(__parameter.value, __parameter.set, None, 'Variable names used within a function.\n\t\t\t\t\tEach parameter name must be unique within the context of this nomenclature.')

    
    # Element {http://www.witsml.org/schemas/1series}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'function'), 'function', '__httpwww_witsml_orgschemas1series_cs_iscwsaNomenclature_httpwww_witsml_orgschemas1seriesfunction', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 33, 3), )

    
    function = property(__function.value, __function.set, None, 'Mathmatical function used to generate error term values from parameters.\n\t\t\t\t\tEach function name must be unique within the context of this nomenclature.')

    
    # Element {http://www.witsml.org/schemas/1series}constant uses Python identifier constant
    __constant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'constant'), 'constant', '__httpwww_witsml_orgschemas1series_cs_iscwsaNomenclature_httpwww_witsml_orgschemas1seriesconstant', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 39, 3), )

    
    constant = property(__constant.value, __constant.set, None, 'Numerical constant used by functions.\n\t\t\t\t\tEach constant name must be unique within the context of this nomenclature.')


    _ElementMap = {
        __parameter.name() : __parameter,
        __function.name() : __function,
        __constant.name() : __constant
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_iscwsaNomenclature', cs_iscwsaNomenclature)


# Complex type {http://www.witsml.org/schemas/1series}abstractMeasure with content type SIMPLE
class abstractMeasure (pyxb.binding.basis.complexTypeDefinition):
    """The intended abstract supertype of all quantities that have a value 
			with a unit of measure. The unit of measure is in the uom attribute of the subtypes. 
			This type allows all quantities to be profiled to be a 'float' instead of a 'double'."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 111, 1)
    # Base type is abstractDouble

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'abstractMeasure', abstractMeasure)


# Complex type {http://www.witsml.org/schemas/1series}obj_toolErrorTermSets with content type ELEMENT_ONLY
class obj_toolErrorTermSets (_abs.abstractObject):
    """Complex type {http://www.witsml.org/schemas/1series}obj_toolErrorTermSets with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'obj_toolErrorTermSets')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 41, 1)
    # Base type is _abs.abstractObject
    
    # Element {http://www.witsml.org/schemas/1series}documentInfo uses Python identifier documentInfo
    __documentInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentInfo'), 'documentInfo', '__httpwww_witsml_orgschemas1series_obj_toolErrorTermSets_httpwww_witsml_orgschemas1seriesdocumentInfo', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 45, 5), )

    
    documentInfo = property(__documentInfo.value, __documentInfo.set, None, 'Information about the XML message instance.')

    
    # Element {http://www.witsml.org/schemas/1series}toolErrorTermSet uses Python identifier toolErrorTermSet
    __toolErrorTermSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'toolErrorTermSet'), 'toolErrorTermSet', '__httpwww_witsml_orgschemas1series_obj_toolErrorTermSets_httpwww_witsml_orgschemas1seriestoolErrorTermSet', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 50, 5), )

    
    toolErrorTermSet = property(__toolErrorTermSet.value, __toolErrorTermSet.set, None, 'A single error term set.')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_witsml_orgschemas1series_obj_toolErrorTermSets_version', schemaVersionString, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 56, 4)
    __version._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 56, 4)
    
    version = property(__version.value, __version.set, None, 'Data object schema version.  The fourth level must match the \n\t\t\t\t\t\tversion of the schema constraints (enumerations and XML loader files) that are assumed\n\t\t\t\t\t\tby the document instance.')


    _ElementMap = _abs.abstractObject._ElementMap.copy()
    _ElementMap.update({
        __documentInfo.name() : __documentInfo,
        __toolErrorTermSet.name() : __toolErrorTermSet
    })
    _AttributeMap = _abs.abstractObject._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', 'obj_toolErrorTermSets', obj_toolErrorTermSets)


# Complex type {http://www.witsml.org/schemas/1series}timestampedTimeZone with content type SIMPLE
class timestampedTimeZone (pyxb.binding.basis.complexTypeDefinition):
    """A local time zone conforming to the XSD:dateTime specification.
			The dTim attribute can capture when the local time zone changed.
			The use of this type is generally related to a specific (set of) date and time
			for which the original time zone needs to be captured."""
    _TypeDefinition = abstractTimeZone
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timestampedTimeZone')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 59, 1)
    # Base type is abstractTimeZone
    
    # Attribute dTim uses Python identifier dTim
    __dTim = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dTim'), 'dTim', '__httpwww_witsml_orgschemas1series_timestampedTimeZone_dTim', timestamp)
    __dTim._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 69, 4)
    __dTim._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 69, 4)
    
    dTim = property(__dTim.value, __dTim.set, None, 'The date and time when this local time zone became active.\n\t\t\t\t\t\tThis value must be defined on the second and subsequent occurrences.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __dTim.name() : __dTim
    }
Namespace.addCategoryObject('typeBinding', 'timestampedTimeZone', timestampedTimeZone)


# Complex type {http://www.witsml.org/schemas/1series}cs_documentEvent with content type ELEMENT_ONLY
class cs_documentEvent (pyxb.binding.basis.complexTypeDefinition):
    """An event type captures the basic information about an 
			event that has affected the data."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_documentEvent')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}eventDate uses Python identifier eventDate
    __eventDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eventDate'), 'eventDate', '__httpwww_witsml_orgschemas1series_cs_documentEvent_httpwww_witsml_orgschemas1serieseventDate', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 28, 3), )

    
    eventDate = property(__eventDate.value, __eventDate.set, None, 'The date on which the event took place.')

    
    # Element {http://www.witsml.org/schemas/1series}eventType uses Python identifier eventType
    __eventType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eventType'), 'eventType', '__httpwww_witsml_orgschemas1series_cs_documentEvent_httpwww_witsml_orgschemas1serieseventType', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 34, 3), )

    
    eventType = property(__eventType.value, __eventType.set, None, 'The kind of event event.')

    
    # Element {http://www.witsml.org/schemas/1series}responsibleParty uses Python identifier responsibleParty
    __responsibleParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responsibleParty'), 'responsibleParty', '__httpwww_witsml_orgschemas1series_cs_documentEvent_httpwww_witsml_orgschemas1seriesresponsibleParty', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 40, 3), )

    
    responsibleParty = property(__responsibleParty.value, __responsibleParty.set, None, 'The party responsible for the event.')

    
    # Element {http://www.witsml.org/schemas/1series}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__httpwww_witsml_orgschemas1series_cs_documentEvent_httpwww_witsml_orgschemas1seriescomment', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 46, 3), )

    
    comment = property(__comment.value, __comment.set, None, 'A free form comment that can further \n\t\t\t\t\tdefine the event that occurred.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionNameValue uses Python identifier extensionNameValue
    __extensionNameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), 'extensionNameValue', '__httpwww_witsml_orgschemas1series_cs_documentEvent_httpwww_witsml_orgschemas1seriesextensionNameValue', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 53, 3), )

    
    extensionNameValue = property(__extensionNameValue.value, __extensionNameValue.set, None, 'Extensions to the schema based on a name-value construct.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas1series_cs_documentEvent_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


    _ElementMap = {
        __eventDate.name() : __eventDate,
        __eventType.name() : __eventType,
        __responsibleParty.name() : __responsibleParty,
        __comment.name() : __comment,
        __extensionNameValue.name() : __extensionNameValue
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', 'cs_documentEvent', cs_documentEvent)


# Complex type {http://www.witsml.org/schemas/1series}cs_documentSecurityInfo with content type ELEMENT_ONLY
class cs_documentSecurityInfo (pyxb.binding.basis.complexTypeDefinition):
    """Information about the security classification of the document. 
			This is intended as a documentation of the security so that the file will not 
			inadvertently be sent to someone who is not allowed access to the data. 
			This block also carries a date that the security classification expires.
			For example, a well log is confidential for a period of time, and then
			becomes open.
			All security classes are characterized by their classification systems."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_documentSecurityInfo')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}class uses Python identifier class_
    __class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'class'), 'class_', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_httpwww_witsml_orgschemas1seriesclass', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 33, 3), )

    
    class_ = property(__class.value, __class.set, None, 'The security class in which this document is \n\t\t\t\t\tclassified. Examples would be confidential, partner confidential, \n\t\t\t\t\ttight. The meaning of the class is determined by the System in which \n\t\t\t\t\tit is defined.')

    
    # Element {http://www.witsml.org/schemas/1series}securitySystem uses Python identifier securitySystem
    __securitySystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'securitySystem'), 'securitySystem', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_httpwww_witsml_orgschemas1seriessecuritySystem', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 42, 3), )

    
    securitySystem = property(__securitySystem.value, __securitySystem.set, None, 'The security classification system. \n\t\t\t\t\tThis gives context to the meaning of the Class value.')

    
    # Element {http://www.witsml.org/schemas/1series}endDate uses Python identifier endDate
    __endDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endDate'), 'endDate', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_httpwww_witsml_orgschemas1seriesendDate', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 49, 3), )

    
    endDate = property(__endDate.value, __endDate.set, None, 'The date on which this security class is no \n\t\t\t\t\tlonger applicable.')

    
    # Element {http://www.witsml.org/schemas/1series}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_httpwww_witsml_orgschemas1seriescomment', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 56, 3), )

    
    comment = property(__comment.value, __comment.set, None, 'A general comment to further define the security \n\t\t\t\t\tclass.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionNameValue uses Python identifier extensionNameValue
    __extensionNameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), 'extensionNameValue', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_httpwww_witsml_orgschemas1seriesextensionNameValue', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 63, 3), )

    
    extensionNameValue = property(__extensionNameValue.value, __extensionNameValue.set, None, 'Extensions to the schema based on a name-value construct.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


    _ElementMap = {
        __class.name() : __class,
        __securitySystem.name() : __securitySystem,
        __endDate.name() : __endDate,
        __comment.name() : __comment,
        __extensionNameValue.name() : __extensionNameValue
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', 'cs_documentSecurityInfo', cs_documentSecurityInfo)


# Complex type {http://www.witsml.org/schemas/1series}cs_extensionNameValue with content type ELEMENT_ONLY
class cs_extensionNameValue (pyxb.binding.basis.complexTypeDefinition):
    """WITSML - Extension values Schema. The intent is to allow standard WITSML "named" 
			extensions without having to modify the schema. A client or server can ignore any name that it 
			does not recognize but certain meta data is required in order to allow 
			generic clients or servers to process the value."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_extensionNameValue')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesname', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 29, 3), )

    
    name = property(__name.value, __name.set, None, 'The name of the extension.\n\t\t\t\t\tEach standard name should document the expected measure class.\n\t\t\t\t\tEach standard name should document the expected maximum size. \n\t\t\t\t\tFor numeric values the size should be in terms of xsd types\n\t\t\t\t\tsuch as int, long, short, byte, float or double.\n\t\t\t\t\tFor strings, the maximum length should be defined in number of characters.\n\t\t\t\t\tLocal extensions to the list of standard names are allowed but it is strongly\n\t\t\t\t\trecommended that the names and definitions be approved by the \n\t\t\t\t\tWITSML SIG Technical Team before use.')

    
    # Element {http://www.witsml.org/schemas/1series}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesvalue', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 42, 3), )

    
    value_ = property(__value.value, __value.set, None, 'The value of the extension. \n\t\t\t\t\tThis may also include a uom attribute. \n\t\t\t\t\tThe content should conform to constraints defined by the data type.')

    
    # Element {http://www.witsml.org/schemas/1series}dataType uses Python identifier dataType
    __dataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dataType'), 'dataType', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesdataType', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 49, 3), )

    
    dataType = property(__dataType.value, __dataType.set, None, 'The underlying XML type of the value.')

    
    # Element {http://www.witsml.org/schemas/1series}dTim uses Python identifier dTim
    __dTim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dTim'), 'dTim', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesdTim', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 54, 3), )

    
    dTim = property(__dTim.value, __dTim.set, None, 'The date-time associated with the value.')

    
    # Element {http://www.witsml.org/schemas/1series}md uses Python identifier md
    __md = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'md'), 'md', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesmd', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 59, 3), )

    
    md = property(__md.value, __md.set, None, 'The measured depth associated with the value.')

    
    # Element {http://www.witsml.org/schemas/1series}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'index'), 'index', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesindex', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 64, 3), )

    
    index = property(__index.value, __index.set, None, 'Indexes things with the same name. \n\t\t\t\t\tThat is, 1 indicates the first one, 2 incidates the second one, etc.')

    
    # Element {http://www.witsml.org/schemas/1series}measureClass uses Python identifier measureClass
    __measureClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measureClass'), 'measureClass', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesmeasureClass', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 70, 3), )

    
    measureClass = property(__measureClass.value, __measureClass.set, None, 'The kind of the measure. For example, "length".\n\t\t\t\t\tThis should be specified if the value requires a unit of measure.')

    
    # Element {http://www.witsml.org/schemas/1series}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesdescription', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 76, 3), )

    
    description = property(__description.value, __description.set, None, 'A textual description of the extension.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


    _ElementMap = {
        __name.name() : __name,
        __value.name() : __value,
        __dataType.name() : __dataType,
        __dTim.name() : __dTim,
        __md.name() : __md,
        __index.name() : __index,
        __measureClass.name() : __measureClass,
        __description.name() : __description
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', 'cs_extensionNameValue', cs_extensionNameValue)


# Complex type {http://www.witsml.org/schemas/1series}cs_iscwsaErrorCoefficient with content type ELEMENT_ONLY
class cs_iscwsaErrorCoefficient (pyxb.binding.basis.complexTypeDefinition):
    """Describes what survey measurement or value the error term applies to."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_iscwsaErrorCoefficient')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}azi uses Python identifier azi
    __azi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'azi'), 'azi', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorCoefficient_httpwww_witsml_orgschemas1seriesazi', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 28, 7), )

    
    azi = property(__azi.value, __azi.set, None, 'Measured horizontal azimuth.')

    
    # Element {http://www.witsml.org/schemas/1series}inc uses Python identifier inc
    __inc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inc'), 'inc', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorCoefficient_httpwww_witsml_orgschemas1seriesinc', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 33, 7), )

    
    inc = property(__inc.value, __inc.set, None, 'Measured deviation from vertical.')

    
    # Element {http://www.witsml.org/schemas/1series}depth uses Python identifier depth
    __depth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'depth'), 'depth', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorCoefficient_httpwww_witsml_orgschemas1seriesdepth', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 38, 7), )

    
    depth = property(__depth.value, __depth.set, None, 'Measured depth along the wellbore.')

    
    # Element {http://www.witsml.org/schemas/1series}tvd uses Python identifier tvd
    __tvd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tvd'), 'tvd', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorCoefficient_httpwww_witsml_orgschemas1seriestvd', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 43, 7), )

    
    tvd = property(__tvd.value, __tvd.set, None, 'True Vertical Depth.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionNameValue uses Python identifier extensionNameValue
    __extensionNameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), 'extensionNameValue', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorCoefficient_httpwww_witsml_orgschemas1seriesextensionNameValue', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 49, 3), )

    
    extensionNameValue = property(__extensionNameValue.value, __extensionNameValue.set, None, 'Extensions to the schema based on a name-value construct.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorCoefficient_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


    _ElementMap = {
        __azi.name() : __azi,
        __inc.name() : __inc,
        __depth.name() : __depth,
        __tvd.name() : __tvd,
        __extensionNameValue.name() : __extensionNameValue
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', 'cs_iscwsaErrorCoefficient', cs_iscwsaErrorCoefficient)


# Complex type {http://www.witsml.org/schemas/1series}cs_iscwsaErrorTerm with content type ELEMENT_ONLY
class cs_iscwsaErrorTerm (pyxb.binding.basis.complexTypeDefinition):
    """WITSML - Error Term Component Schema.
			The reference error terms that are included in error models via ErrorTermValues."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_iscwsaErrorTerm')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 22, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorTerm_httpwww_witsml_orgschemas1seriesname', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 29, 3), )

    
    name = property(__name.value, __name.set, None, 'This is the unique mnemonic for this term. \n\t\t\t\t\tFor example, "ABIX" or "DECR".')

    
    # Element {http://www.witsml.org/schemas/1series}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorTerm_httpwww_witsml_orgschemas1seriestype', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 35, 3), )

    
    type = property(__type.value, __type.set, None, 'The class of the error source.')

    
    # Element {http://www.witsml.org/schemas/1series}measureClass uses Python identifier measureClass
    __measureClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measureClass'), 'measureClass', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorTerm_httpwww_witsml_orgschemas1seriesmeasureClass', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 40, 3), )

    
    measureClass = property(__measureClass.value, __measureClass.set, None, 'The kind of quantity that the term represents.\n\t\t\t\t\tThis constrains the unit that can be used for any errorTermValues.')

    
    # Element {http://www.witsml.org/schemas/1series}label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'label'), 'label', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorTerm_httpwww_witsml_orgschemas1serieslabel', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 46, 3), )

    
    label = property(__label.value, __label.set, None, 'Human-readable name for the term, may be presented in \n\t\t\t\t\tapplication software. E.g., "MWD: X-Acceleromter Bias with Z-Axis Corr."')

    
    # Element {http://www.witsml.org/schemas/1series}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorTerm_httpwww_witsml_orgschemas1seriesdescription', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 52, 3), )

    
    description = property(__description.value, __description.set, None, 'Human-readable name for the term, may be presented in \n\t\t\t\t\tapplication software. E.g., "MWD: X-Acceleromter Bias with Z-Axis Corr."')

    
    # Element {http://www.witsml.org/schemas/1series}errorCoefficient uses Python identifier errorCoefficient
    __errorCoefficient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errorCoefficient'), 'errorCoefficient', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorTerm_httpwww_witsml_orgschemas1serieserrorCoefficient', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 58, 3), )

    
    errorCoefficient = property(__errorCoefficient.value, __errorCoefficient.set, None, 'Describes what measurement(s) the error variance(s) apply to.')

    
    # Element {http://www.witsml.org/schemas/1series}operatingMode uses Python identifier operatingMode
    __operatingMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'operatingMode'), 'operatingMode', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorTerm_httpwww_witsml_orgschemas1seriesoperatingMode', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 63, 3), )

    
    operatingMode = property(__operatingMode.value, __operatingMode.set, None, 'Operating mode that is valid for this error term.\n\t\t\t\t\tIn the absence of this element assume Stationary.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionNameValue uses Python identifier extensionNameValue
    __extensionNameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), 'extensionNameValue', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorTerm_httpwww_witsml_orgschemas1seriesextensionNameValue', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 69, 3), )

    
    extensionNameValue = property(__extensionNameValue.value, __extensionNameValue.set, None, 'Extensions to the schema based on a name-value construct.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas1series_cs_iscwsaErrorTerm_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


    _ElementMap = {
        __name.name() : __name,
        __type.name() : __type,
        __measureClass.name() : __measureClass,
        __label.name() : __label,
        __description.name() : __description,
        __errorCoefficient.name() : __errorCoefficient,
        __operatingMode.name() : __operatingMode,
        __extensionNameValue.name() : __extensionNameValue
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', 'cs_iscwsaErrorTerm', cs_iscwsaErrorTerm)


# Complex type {http://www.witsml.org/schemas/1series}cs_iscwsaNameAndDescription with content type ELEMENT_ONLY
class cs_iscwsaNameAndDescription (pyxb.binding.basis.complexTypeDefinition):
    """A generic type which captures a name and a description of something.
			The semantics of the something is defined by the parent element."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_iscwsaNameAndDescription')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_witsml_orgschemas1series_cs_iscwsaNameAndDescription_httpwww_witsml_orgschemas1seriesname', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 28, 3), )

    
    name = property(__name.value, __name.set, None, 'The name of the item.')

    
    # Element {http://www.witsml.org/schemas/1series}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_witsml_orgschemas1series_cs_iscwsaNameAndDescription_httpwww_witsml_orgschemas1seriesdescription', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 33, 3), )

    
    description = property(__description.value, __description.set, None, 'A textual description of the item.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionNameValue uses Python identifier extensionNameValue
    __extensionNameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), 'extensionNameValue', '__httpwww_witsml_orgschemas1series_cs_iscwsaNameAndDescription_httpwww_witsml_orgschemas1seriesextensionNameValue', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 38, 3), )

    
    extensionNameValue = property(__extensionNameValue.value, __extensionNameValue.set, None, 'Extensions to the schema based on a name-value construct.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas1series_cs_iscwsaNameAndDescription_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


    _ElementMap = {
        __name.name() : __name,
        __description.name() : __description,
        __extensionNameValue.name() : __extensionNameValue
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', 'cs_iscwsaNameAndDescription', cs_iscwsaNameAndDescription)


# Complex type {http://www.witsml.org/schemas/1series}cs_iscwsaNomenclatureConstant with content type ELEMENT_ONLY
class cs_iscwsaNomenclatureConstant (pyxb.binding.basis.complexTypeDefinition):
    """A nomenclature constant."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_iscwsaNomenclatureConstant')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_witsml_orgschemas1series_cs_iscwsaNomenclatureConstant_httpwww_witsml_orgschemas1seriesname', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 27, 3), )

    
    name = property(__name.value, __name.set, None, 'The name of the constant.')

    
    # Element {http://www.witsml.org/schemas/1series}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_witsml_orgschemas1series_cs_iscwsaNomenclatureConstant_httpwww_witsml_orgschemas1seriesvalue', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 32, 3), )

    
    value_ = property(__value.value, __value.set, None, 'The value of the constant.')

    
    # Element {http://www.witsml.org/schemas/1series}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unit'), 'unit', '__httpwww_witsml_orgschemas1series_cs_iscwsaNomenclatureConstant_httpwww_witsml_orgschemas1seriesunit', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 37, 3), )

    
    unit = property(__unit.value, __unit.set, None, 'The unit of measure of the constant.\n\t\t\t\t\tThis value must match an acronym from the WITSML unit of measure dictionary.')

    
    # Element {http://www.witsml.org/schemas/1series}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_witsml_orgschemas1series_cs_iscwsaNomenclatureConstant_httpwww_witsml_orgschemas1seriesdescription', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 43, 3), )

    
    description = property(__description.value, __description.set, None, 'A textual description of the constant.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionNameValue uses Python identifier extensionNameValue
    __extensionNameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), 'extensionNameValue', '__httpwww_witsml_orgschemas1series_cs_iscwsaNomenclatureConstant_httpwww_witsml_orgschemas1seriesextensionNameValue', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 48, 3), )

    
    extensionNameValue = property(__extensionNameValue.value, __extensionNameValue.set, None, 'Extensions to the schema based on a name-value construct.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas1series_cs_iscwsaNomenclatureConstant_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


    _ElementMap = {
        __name.name() : __name,
        __value.name() : __value,
        __unit.name() : __unit,
        __description.name() : __description,
        __extensionNameValue.name() : __extensionNameValue
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', 'cs_iscwsaNomenclatureConstant', cs_iscwsaNomenclatureConstant)


# Complex type {http://www.witsml.org/schemas/1series}obj_toolErrorTermSet with content type ELEMENT_ONLY
class obj_toolErrorTermSet (pyxb.binding.basis.complexTypeDefinition):
    """Defines the singular set of error terms."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'obj_toolErrorTermSet')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 67, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}authorization uses Python identifier authorization
    __authorization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authorization'), 'authorization', '__httpwww_witsml_orgschemas1series_obj_toolErrorTermSet_httpwww_witsml_orgschemas1seriesauthorization', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 28, 3), )

    
    authorization = property(__authorization.value, __authorization.set, None, 'The definitive source for this set of error terms.')

    
    # Element {http://www.witsml.org/schemas/1series}nomenclature uses Python identifier nomenclature
    __nomenclature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nomenclature'), 'nomenclature', '__httpwww_witsml_orgschemas1series_obj_toolErrorTermSet_httpwww_witsml_orgschemas1seriesnomenclature', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 33, 3), )

    
    nomenclature = property(__nomenclature.value, __nomenclature.set, None, 'Defines the nomenclature used in the error terms.')

    
    # Element {http://www.witsml.org/schemas/1series}errorTerm uses Python identifier errorTerm
    __errorTerm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errorTerm'), 'errorTerm', '__httpwww_witsml_orgschemas1series_obj_toolErrorTermSet_httpwww_witsml_orgschemas1serieserrorTerm', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 38, 3), )

    
    errorTerm = property(__errorTerm.value, __errorTerm.set, None, 'Defines an error term.')

    
    # Element {http://www.witsml.org/schemas/1series}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_witsml_orgschemas1series_obj_toolErrorTermSet_httpwww_witsml_orgschemas1seriesname', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 72, 3), )

    
    name = property(__name.value, __name.set, None, 'Human-readable name for the set of terms.')

    
    # Element {http://www.witsml.org/schemas/1series}commonData uses Python identifier commonData
    __commonData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'commonData'), 'commonData', '__httpwww_witsml_orgschemas1series_obj_toolErrorTermSet_httpwww_witsml_orgschemas1seriescommonData', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 82, 3), )

    
    commonData = property(__commonData.value, __commonData.set, None, 'A container element that contains elements that are common to all data \n\t\t\t\t\tobjects.  ')

    
    # Element {http://www.witsml.org/schemas/1series}customData uses Python identifier customData
    __customData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customData'), 'customData', '__httpwww_witsml_orgschemas1series_obj_toolErrorTermSet_httpwww_witsml_orgschemas1seriescustomData', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 88, 3), )

    
    customData = property(__customData.value, __customData.set, None, 'A container element that can contain custom or user defined \n\t\t\t\t\tdata elements.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas1series_obj_toolErrorTermSet_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_objectUid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_objectUid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of an object.\n\t\t\t\tThis should not be used for child nodes within an object.\n\t\t\t\tFor an independent object, the value may be globally unique.\n\t\t\t\tFor a dependent object, the value must be unique (for the same object type) within the context of the parent object.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThe purpose of this type is to facilitate modifying the optionality in derived schemas.')


    _ElementMap = {
        __authorization.name() : __authorization,
        __nomenclature.name() : __nomenclature,
        __errorTerm.name() : __errorTerm,
        __name.name() : __name,
        __commonData.name() : __commonData,
        __customData.name() : __customData
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', 'obj_toolErrorTermSet', obj_toolErrorTermSet)


# Complex type {http://www.witsml.org/schemas/1series}yAxisAzimuth with content type SIMPLE
class yAxisAzimuth (abstractMeasure):
    """The angle of a Y axis from North.
			This is a variation of planeAngleMeasure with an 
			attribute defining the direction of north."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'yAxisAzimuth')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 102, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_yAxisAzimuth_uom', PlaneAngleUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 111, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 111, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure of the azimuth value.')

    
    # Attribute northDirection uses Python identifier northDirection
    __northDirection = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'northDirection'), 'northDirection', '__httpwww_witsml_orgschemas1series_yAxisAzimuth_northDirection', AziRef)
    __northDirection._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 117, 4)
    __northDirection._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 117, 4)
    
    northDirection = property(__northDirection.value, __northDirection.set, None, 'Specifies the direction to be considered North for the y axis.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __northDirection.name() : __northDirection
    })
Namespace.addCategoryObject('typeBinding', 'yAxisAzimuth', yAxisAzimuth)


# Complex type {http://www.witsml.org/schemas/1series}volumePerVolumeMeasurePercent with content type SIMPLE
class volumePerVolumeMeasurePercent (abstractMeasure):
    """A volume per volume measure that is constrained to a unit of percent."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumePerVolumeMeasurePercent')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 126, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_volumePerVolumeMeasurePercent_uom', PercentUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 133, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 133, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'volumePerVolumeMeasurePercent', volumePerVolumeMeasurePercent)


# Complex type {http://www.witsml.org/schemas/1series}measureOrQuantity with content type SIMPLE
class measureOrQuantity (abstractMeasure):
    """A measure with a uom or a quantity (without a uom).
			This should not be used except in situations where the underlying class of data is 
			captured elsewhere. For example, via a measure class."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measureOrQuantity')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 146, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_measureOrQuantity_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 154, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 154, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure for the quantity.\n\t\t\t\t\t\tThis value must conform to the values allowed by a measure class. \n\t\t\t\t\t\tIf the value is a measure then the uom must be specified.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'measureOrQuantity', measureOrQuantity)


# Complex type {http://www.witsml.org/schemas/1series}genericMeasure with content type SIMPLE
class genericMeasure (abstractMeasure):
    """A generic measure type.
			This should not be used except in situations where the underlying class of data is 
			captured elsewhere. For example, for a log curve."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genericMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 165, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_genericMeasure_uom', uomString, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 174, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 174, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure for the quantity.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'genericMeasure', genericMeasure)


# Complex type {http://www.witsml.org/schemas/1series}ratioGenericMeasure with content type SIMPLE
class ratioGenericMeasure (abstractMeasure):
    """Representation of a number as a double, possibly qualified as a ratio of doubles.	
			Ratio component attributes 'numerator' and 'denominator' may be both present or both absent.	
			When ratio component attributes are present, the ratio represented is to be used with
			the double representation included for human readability.
			A 'canonical' representation, according to the following rules, is suggested:
			Only use numerator/denominator when the representation of the number as double is not 
			sufficiently precise (i. e. causes errors of accumulation).
			Express both numerator and denominator as integers (doubles with integer values) reduced 
			to 'least common denominator' if possible."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ratioGenericMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 184, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_ratioGenericMeasure_uom', uomString, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 199, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 199, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure for the quantity.\n\t\t\t\t\t\tIf for some reason a uom is not appropriate for the quantity,\n\t\t\t\t\t\ta unit of "Euc" should be used.')

    
    # Attribute numerator uses Python identifier numerator
    __numerator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numerator'), 'numerator', '__httpwww_witsml_orgschemas1series_ratioGenericMeasure_numerator', unitlessQuantity)
    __numerator._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 206, 4)
    __numerator._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 206, 4)
    
    numerator = property(__numerator.value, __numerator.set, None, None)

    
    # Attribute denominator uses Python identifier denominator
    __denominator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'denominator'), 'denominator', '__httpwww_witsml_orgschemas1series_ratioGenericMeasure_denominator', unitlessQuantity)
    __denominator._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 207, 4)
    __denominator._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 207, 4)
    
    denominator = property(__denominator.value, __denominator.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __numerator.name() : __numerator,
        __denominator.name() : __denominator
    })
Namespace.addCategoryObject('typeBinding', 'ratioGenericMeasure', ratioGenericMeasure)


# Complex type {http://www.witsml.org/schemas/1series}refNameString with content type SIMPLE
class refNameString (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a name in another node of the xml hierachy.
			This value represents a foreign key from one element to another."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refNameString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 256, 1)
    # Base type is abstractNameString
    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas1series_refNameString_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 263, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 263, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, 'A reference to the unique identifier (uid attribute) in the node\n\t\t\t\t\t\treferenced by the name value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', 'refNameString', refNameString)


# Complex type {http://www.witsml.org/schemas/1series}refObjectString with content type SIMPLE
class refObjectString (pyxb.binding.basis.complexTypeDefinition):
    """The value of a name element in another data-object.
			The information in this type represents a foreign key to a data-object instance.
			Knowledge of the type of object being referenced is defined by an attribute."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refObjectString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 274, 1)
    # Base type is abstractNameString
    
    # Attribute object uses Python identifier object
    __object = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'object'), 'object', '__httpwww_witsml_orgschemas1series_refObjectString_object', nameString, required=True)
    __object._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 282, 4)
    __object._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 282, 4)
    
    object = property(__object.value, __object.set, None, 'The type of data-object being referenced (e.g., "well", "wellbore").')

    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas1series_refObjectString_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 287, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 287, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, 'A reference to the unique identifier (uid attribute) in the object\n\t\t\t\t\t\treferenced by the name value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __object.name() : __object,
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', 'refObjectString', refObjectString)


# Complex type {http://www.witsml.org/schemas/1series}refPositiveCount with content type SIMPLE
class refPositiveCount (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a index value in another node of the xml hierachy.
			This value represents a foreign key from one element to another."""
    _TypeDefinition = abstractPositiveCount
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refPositiveCount')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 298, 1)
    # Base type is abstractPositiveCount
    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas1series_refPositiveCount_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 305, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 305, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, 'A reference to the unique identifier (uid attribute) in the node\n\t\t\t\t\t\treferenced by the index value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', 'refPositiveCount', refPositiveCount)


# Complex type {http://www.witsml.org/schemas/1series}timestampedCommentString with content type SIMPLE
class timestampedCommentString (pyxb.binding.basis.complexTypeDefinition):
    """A timestamped textual description."""
    _TypeDefinition = abstractCommentString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timestampedCommentString')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 369, 1)
    # Base type is abstractCommentString
    
    # Attribute dTim uses Python identifier dTim
    __dTim = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dTim'), 'dTim', '__httpwww_witsml_orgschemas1series_timestampedCommentString_dTim', timestamp, required=True)
    __dTim._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 376, 4)
    __dTim._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 376, 4)
    
    dTim = property(__dTim.value, __dTim.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __dTim.name() : __dTim
    }
Namespace.addCategoryObject('typeBinding', 'timestampedCommentString', timestampedCommentString)


# Complex type {http://www.witsml.org/schemas/1series}extensionvalue with content type SIMPLE
class extensionvalue (pyxb.binding.basis.complexTypeDefinition):
    """A extension value.
			Each standard name should document the expected maximum size. 
			Knowledge of the semantics must be provided with the context of the usage of this type."""
    _TypeDefinition = abstractMaximumLengthString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extensionvalue')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 391, 1)
    # Base type is abstractMaximumLengthString
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_extensionvalue_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 400, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 400, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure for the value.\n\t\t\t\t\t\tThis value must conform to the values allowed by a measure class.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uom.name() : __uom
    }
Namespace.addCategoryObject('typeBinding', 'extensionvalue', extensionvalue)


# Complex type {http://www.witsml.org/schemas/1series}nameStruct with content type SIMPLE
class nameStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of something within a naming system."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameStruct')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 441, 1)
    # Base type is abstractNameString
    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'namingSystem'), 'namingSystem', '__httpwww_witsml_orgschemas1series_nameStruct_namingSystem', nameString)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 447, 4)
    __namingSystem._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 447, 4)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, 'The naming system within the name is (hopefully) unique.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __namingSystem.name() : __namingSystem
    }
Namespace.addCategoryObject('typeBinding', 'nameStruct', nameStruct)


# Complex type {http://www.witsml.org/schemas/1series}shortNameStruct with content type SIMPLE
class shortNameStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of something within a naming system."""
    _TypeDefinition = abstractString32
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'shortNameStruct')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 456, 1)
    # Base type is abstractString32
    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'namingSystem'), 'namingSystem', '__httpwww_witsml_orgschemas1series_shortNameStruct_namingSystem', nameString)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 462, 4)
    __namingSystem._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 462, 4)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, 'The naming system within the name is (hopefully) unique.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __namingSystem.name() : __namingSystem
    }
Namespace.addCategoryObject('typeBinding', 'shortNameStruct', shortNameStruct)


# Complex type {http://www.witsml.org/schemas/1series}wellKnownNameStruct with content type SIMPLE
class wellKnownNameStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of something within a mandatory naming system 
			with an optional code."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'wellKnownNameStruct')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 471, 1)
    # Base type is abstractNameString
    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'namingSystem'), 'namingSystem', '__httpwww_witsml_orgschemas1series_wellKnownNameStruct_namingSystem', nameString, required=True)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 478, 4)
    __namingSystem._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 478, 4)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, 'The naming system within the name is unique.')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httpwww_witsml_orgschemas1series_wellKnownNameStruct_code', kindString)
    __code._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 483, 4)
    __code._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 483, 4)
    
    code = property(__code.value, __code.set, None, 'A unique (short) code associated with the name.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __namingSystem.name() : __namingSystem,
        __code.name() : __code
    }
Namespace.addCategoryObject('typeBinding', 'wellKnownNameStruct', wellKnownNameStruct)


# Complex type {http://www.witsml.org/schemas/1series}objectSequence with content type SIMPLE
class objectSequence (pyxb.binding.basis.complexTypeDefinition):
    """Defines a sequence number and with an optional description attribute."""
    _TypeDefinition = abstractPositiveCount
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'objectSequence')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 522, 1)
    # Base type is abstractPositiveCount
    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_witsml_orgschemas1series_objectSequence_description', descriptionString)
    __description._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 529, 4)
    __description._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 529, 4)
    
    description = property(__description.value, __description.set, None, 'A description related to the sequence number.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __description.name() : __description
    }
Namespace.addCategoryObject('typeBinding', 'objectSequence', objectSequence)


# Complex type {http://www.witsml.org/schemas/1series}lithostratigraphyStruct with content type SIMPLE
class lithostratigraphyStruct (pyxb.binding.basis.complexTypeDefinition):
    """
				The name of a lithostratigraphy, with the "kind" attribute specifying the lithostratigraphic unit-hierarchy (Group, Formation, Member or Bed).
				The entry at each level is free text for the local lithostratigraphy at that level in the hierarchy.
				If a single hierarchy is defined, it is assumed this is at the Formation level in the hierarchy and kind=formation should be used for the entry.
			"""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lithostratigraphyStruct')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 538, 1)
    # Base type is abstractNameString
    
    # Attribute kind uses Python identifier kind
    __kind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kind'), 'kind', '__httpwww_witsml_orgschemas1series_lithostratigraphyStruct_kind', LithostratigraphyUnit)
    __kind._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 549, 4)
    __kind._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 549, 4)
    
    kind = property(__kind.value, __kind.set, None, 'The unit of lithostratigraphy.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __kind.name() : __kind
    }
Namespace.addCategoryObject('typeBinding', 'lithostratigraphyStruct', lithostratigraphyStruct)


# Complex type {http://www.witsml.org/schemas/1series}chronostratigraphyStruct with content type SIMPLE
class chronostratigraphyStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of a chronostratigraphy, with the "kind" attribute specifying
			the chronostratigraphic unit-hierarchy (Era, Period, Epoch, Stage)."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'chronostratigraphyStruct')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 558, 1)
    # Base type is abstractNameString
    
    # Attribute kind uses Python identifier kind
    __kind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kind'), 'kind', '__httpwww_witsml_orgschemas1series_chronostratigraphyStruct_kind', ChronostratigraphyUnit)
    __kind._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 566, 4)
    __kind._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 566, 4)
    
    kind = property(__kind.value, __kind.set, None, 'The unit of chronostratigraphy.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __kind.name() : __kind
    }
Namespace.addCategoryObject('typeBinding', 'chronostratigraphyStruct', chronostratigraphyStruct)


# Complex type {http://www.witsml.org/schemas/1series}measuredDepthCoord with content type SIMPLE
class measuredDepthCoord (abstractMeasure):
    """A measured depth coordinate in a wellbore. 
			Positive moving from the reference datum toward the bottomhole.
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measuredDepthCoord')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 577, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_measuredDepthCoord_uom', MeasuredDepthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 586, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 586, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure of the quantity value.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datum'), 'datum', '__httpwww_witsml_orgschemas1series_measuredDepthCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 591, 4)
    __datum._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 591, 4)
    
    datum = property(__datum.value, __datum.set, None, 'A pointer to the reference datum for this coordinate \n\t\t\t\t\t\tvalue as defined in WellDatum. This value is assumed to match the uid\n\t\t\t\t\t\tvalue in a WellDatum.\n\t\t\t\t\t\tIf not given then the default WellDatum must be assumed.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __datum.name() : __datum
    })
Namespace.addCategoryObject('typeBinding', 'measuredDepthCoord', measuredDepthCoord)


# Complex type {http://www.witsml.org/schemas/1series}wellVerticalDepthCoord with content type SIMPLE
class wellVerticalDepthCoord (abstractMeasure):
    """A vertical (gravity based) depth coordinate within the context of a well.
			Positive moving downward from the reference datum. 
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'wellVerticalDepthCoord')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 603, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_wellVerticalDepthCoord_uom', WellVerticalCoordinateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 612, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 612, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure of the quantity value.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datum'), 'datum', '__httpwww_witsml_orgschemas1series_wellVerticalDepthCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 617, 4)
    __datum._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 617, 4)
    
    datum = property(__datum.value, __datum.set, None, 'A pointer to the reference datum for this coordinate \n\t\t\t\t\t\tvalue as defined in WellDatum. \n\t\t\t\t\t\tIf not given then the default WellDatum must be assumed.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __datum.name() : __datum
    })
Namespace.addCategoryObject('typeBinding', 'wellVerticalDepthCoord', wellVerticalDepthCoord)


# Complex type {http://www.witsml.org/schemas/1series}wellElevationCoord with content type SIMPLE
class wellElevationCoord (abstractMeasure):
    """A vertical (gravity based) elevation coordinate within the context of a well.
			Positive moving upward from the reference datum.  
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'wellElevationCoord')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 628, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_wellElevationCoord_uom', WellVerticalCoordinateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 637, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 637, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure of the quantity value.\n\t\t\t\t\t\tIf not given then the default unit of measure of the explicitly\n\t\t\t\t\t\tor implicitly given datum must be assumed.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datum'), 'datum', '__httpwww_witsml_orgschemas1series_wellElevationCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 644, 4)
    __datum._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 644, 4)
    
    datum = property(__datum.value, __datum.set, None, 'A pointer to the reference datum for this coordinate \n\t\t\t\t\t\tvalue as defined in WellDatum. \n\t\t\t\t\t\tIf not given then the default WellDatum must be assumed.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __datum.name() : __datum
    })
Namespace.addCategoryObject('typeBinding', 'wellElevationCoord', wellElevationCoord)


# Complex type {http://www.witsml.org/schemas/1series}footageNorthSouth with content type SIMPLE
class footageNorthSouth (abstractMeasure):
    """The distance to a one minute boundary on the north or south of a point.
			USA Public Land Survey System."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'footageNorthSouth')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 693, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_footageNorthSouth_uom', LengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 701, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 701, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure of the distance value.')

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_witsml_orgschemas1series_footageNorthSouth_ref', NorthOrSouth, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 707, 4)
    __ref._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 707, 4)
    
    ref = property(__ref.value, __ref.set, None, 'Specifies the reference line that is the origin of the distance.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', 'footageNorthSouth', footageNorthSouth)


# Complex type {http://www.witsml.org/schemas/1series}footageEastWest with content type SIMPLE
class footageEastWest (abstractMeasure):
    """The distance to a one minute boundary on the east or west of a point.
			USA Public Land Survey System."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'footageEastWest')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 716, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_footageEastWest_uom', LengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 724, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 724, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure of the distance value.')

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_witsml_orgschemas1series_footageEastWest_ref', EastOrWest, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 730, 4)
    __ref._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 730, 4)
    
    ref = property(__ref.value, __ref.set, None, 'Specifies the reference line that is the origin of the distance.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', 'footageEastWest', footageEastWest)


# Complex type {http://www.witsml.org/schemas/1series}cost with content type SIMPLE
class cost (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cost')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 842, 1)
    # Base type is abstractDouble
    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'currency'), 'currency', '__httpwww_witsml_orgschemas1series_cost_currency', kindString)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 848, 4)
    __currency._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 848, 4)
    
    currency = property(__currency.value, __currency.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __currency.name() : __currency
    }
Namespace.addCategoryObject('typeBinding', 'cost', cost)


# Complex type {http://www.witsml.org/schemas/1series}indexedObject with content type SIMPLE
class indexedObject (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = abstractTypeEnum
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'indexedObject')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 853, 1)
    # Base type is abstractTypeEnum
    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas1series_indexedObject_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')

    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'index'), 'index', '__httpwww_witsml_orgschemas1series_indexedObject_index', positiveCount, required=True)
    __index._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 859, 4)
    __index._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 859, 4)
    
    index = property(__index.value, __index.set, None, 'Indexes things with the same name. \n\t\t\t\t\t\tThat is the first one, the second one, etc.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_witsml_orgschemas1series_indexedObject_name', kindString)
    __name._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 865, 4)
    __name._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 865, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_indexedObject_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 866, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 866, 4)
    
    uom = property(__uom.value, __uom.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_witsml_orgschemas1series_indexedObject_description', descriptionString)
    __description._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 867, 4)
    __description._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 867, 4)
    
    description = property(__description.value, __description.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uid.name() : __uid,
        __index.name() : __index,
        __name.name() : __name,
        __uom.name() : __uom,
        __description.name() : __description
    }
Namespace.addCategoryObject('typeBinding', 'indexedObject', indexedObject)


# Complex type {http://www.witsml.org/schemas/1series}accelerationLinearMeasure with content type SIMPLE
class accelerationLinearMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}accelerationLinearMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accelerationLinearMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 26, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_accelerationLinearMeasure_uom', AccelerationLinearUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 29, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 29, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'accelerationLinearMeasure', accelerationLinearMeasure)


# Complex type {http://www.witsml.org/schemas/1series}anglePerLengthMeasure with content type SIMPLE
class anglePerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}anglePerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'anglePerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 38, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_anglePerLengthMeasure_uom', AnglePerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 41, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 41, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'anglePerLengthMeasure', anglePerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}anglePerTimeMeasure with content type SIMPLE
class anglePerTimeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}anglePerTimeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'anglePerTimeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 50, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_anglePerTimeMeasure_uom', AnglePerTimeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 53, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 53, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'anglePerTimeMeasure', anglePerTimeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}areaMeasure with content type SIMPLE
class areaMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}areaMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'areaMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 62, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_areaMeasure_uom', AreaUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 65, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 65, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'areaMeasure', areaMeasure)


# Complex type {http://www.witsml.org/schemas/1series}areaPerAreaMeasure with content type SIMPLE
class areaPerAreaMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}areaPerAreaMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'areaPerAreaMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 74, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_areaPerAreaMeasure_uom', AreaPerAreaUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 77, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 77, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'areaPerAreaMeasure', areaPerAreaMeasure)


# Complex type {http://www.witsml.org/schemas/1series}compressibilityMeasure with content type SIMPLE
class compressibilityMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'compressibilityMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 86, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_compressibilityMeasure_uom', CompressibilityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 92, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 92, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'compressibilityMeasure', compressibilityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}densityMeasure with content type SIMPLE
class densityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}densityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'densityMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 97, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_densityMeasure_uom', DensityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 100, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 100, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'densityMeasure', densityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}dimensionlessMeasure with content type SIMPLE
class dimensionlessMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}dimensionlessMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dimensionlessMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 109, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_dimensionlessMeasure_uom', DimensionlessUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 112, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 112, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'dimensionlessMeasure', dimensionlessMeasure)


# Complex type {http://www.witsml.org/schemas/1series}dynamicViscosityMeasure with content type SIMPLE
class dynamicViscosityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}dynamicViscosityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dynamicViscosityMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 121, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_dynamicViscosityMeasure_uom', DynamicViscosityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 124, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 124, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'dynamicViscosityMeasure', dynamicViscosityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}electricCurrentMeasure with content type SIMPLE
class electricCurrentMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}electricCurrentMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'electricCurrentMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 133, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_electricCurrentMeasure_uom', ElectricCurrentUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 136, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 136, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'electricCurrentMeasure', electricCurrentMeasure)


# Complex type {http://www.witsml.org/schemas/1series}electricPotentialMeasure with content type SIMPLE
class electricPotentialMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}electricPotentialMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'electricPotentialMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 145, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_electricPotentialMeasure_uom', ElectricPotentialUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 148, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 148, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'electricPotentialMeasure', electricPotentialMeasure)


# Complex type {http://www.witsml.org/schemas/1series}equivalentPerMassMeasure with content type SIMPLE
class equivalentPerMassMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}equivalentPerMassMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equivalentPerMassMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 161, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_equivalentPerMassMeasure_uom', EquivalentPerMassUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 164, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 164, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'equivalentPerMassMeasure', equivalentPerMassMeasure)


# Complex type {http://www.witsml.org/schemas/1series}forceMeasure with content type SIMPLE
class forceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}forceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'forceMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 173, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_forceMeasure_uom', ForceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 176, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 176, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'forceMeasure', forceMeasure)


# Complex type {http://www.witsml.org/schemas/1series}forcePerLengthMeasure with content type SIMPLE
class forcePerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}forcePerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'forcePerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 185, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_forcePerLengthMeasure_uom', ForcePerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 188, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 188, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'forcePerLengthMeasure', forcePerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}forcePerVolumeMeasure with content type SIMPLE
class forcePerVolumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}forcePerVolumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'forcePerVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 197, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_forcePerVolumeMeasure_uom', ForcePerVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 200, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 200, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'forcePerVolumeMeasure', forcePerVolumeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}illuminanceMeasure with content type SIMPLE
class illuminanceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}illuminanceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'illuminanceMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 209, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_illuminanceMeasure_uom', IlluminanceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 212, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 212, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'illuminanceMeasure', illuminanceMeasure)


# Complex type {http://www.witsml.org/schemas/1series}lengthMeasure with content type SIMPLE
class lengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}lengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 221, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_lengthMeasure_uom', LengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 224, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 224, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'lengthMeasure', lengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}lengthPerLengthMeasure with content type SIMPLE
class lengthPerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}lengthPerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengthPerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 233, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_lengthPerLengthMeasure_uom', LengthPerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 236, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 236, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'lengthPerLengthMeasure', lengthPerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}magneticInductionMeasure with content type SIMPLE
class magneticInductionMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}magneticInductionMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'magneticInductionMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 249, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_magneticInductionMeasure_uom', MagneticInductionUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 252, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 252, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'magneticInductionMeasure', magneticInductionMeasure)


# Complex type {http://www.witsml.org/schemas/1series}massConcentrationMeasure with content type SIMPLE
class massConcentrationMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}massConcentrationMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'massConcentrationMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 261, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_massConcentrationMeasure_uom', MassConcentrationUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 264, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 264, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'massConcentrationMeasure', massConcentrationMeasure)


# Complex type {http://www.witsml.org/schemas/1series}massMeasure with content type SIMPLE
class massMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}massMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'massMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 273, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_massMeasure_uom', MassUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 276, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 276, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'massMeasure', massMeasure)


# Complex type {http://www.witsml.org/schemas/1series}massPerLengthMeasure with content type SIMPLE
class massPerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}massPerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'massPerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 285, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_massPerLengthMeasure_uom', MassPerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 288, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 288, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'massPerLengthMeasure', massPerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}momentOfForceMeasure with content type SIMPLE
class momentOfForceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}momentOfForceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'momentOfForceMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 297, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_momentOfForceMeasure_uom', MomentOfForceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 300, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 300, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'momentOfForceMeasure', momentOfForceMeasure)


# Complex type {http://www.witsml.org/schemas/1series}perLengthMeasure with content type SIMPLE
class perLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}perLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'perLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 309, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_perLengthMeasure_uom', PerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 312, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 312, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'perLengthMeasure', perLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}permeabilityRockMeasure with content type SIMPLE
class permeabilityRockMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'permeabilityRockMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 321, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_permeabilityRockMeasure_uom', PermeabilityRockUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 327, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 327, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'permeabilityRockMeasure', permeabilityRockMeasure)


# Complex type {http://www.witsml.org/schemas/1series}planeAngleMeasure with content type SIMPLE
class planeAngleMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}planeAngleMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'planeAngleMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 332, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_planeAngleMeasure_uom', PlaneAngleUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 335, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 335, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'planeAngleMeasure', planeAngleMeasure)


# Complex type {http://www.witsml.org/schemas/1series}powerMeasure with content type SIMPLE
class powerMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}powerMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'powerMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 344, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_powerMeasure_uom', PowerUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 347, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 347, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'powerMeasure', powerMeasure)


# Complex type {http://www.witsml.org/schemas/1series}pressureMeasure with content type SIMPLE
class pressureMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}pressureMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pressureMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 356, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_pressureMeasure_uom', PressureUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 359, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 359, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'pressureMeasure', pressureMeasure)


# Complex type {http://www.witsml.org/schemas/1series}relativePowerMeasure with content type SIMPLE
class relativePowerMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}relativePowerMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relativePowerMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 368, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_relativePowerMeasure_uom', RelativePowerUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 371, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 371, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'relativePowerMeasure', relativePowerMeasure)


# Complex type {http://www.witsml.org/schemas/1series}specificHeatCapacityMeasure with content type SIMPLE
class specificHeatCapacityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}specificHeatCapacityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'specificHeatCapacityMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 380, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_specificHeatCapacityMeasure_uom', SpecificHeatCapacityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 383, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 383, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'specificHeatCapacityMeasure', specificHeatCapacityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}specificVolumeMeasure with content type SIMPLE
class specificVolumeMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'specificVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 388, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_specificVolumeMeasure_uom', SpecificVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 394, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 394, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'specificVolumeMeasure', specificVolumeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}standardVolumeMeasure with content type SIMPLE
class standardVolumeMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'standardVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 403, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_standardVolumeMeasure_uom', StandardVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 409, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 409, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'standardVolumeMeasure', standardVolumeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}standardVolumePerTimeMeasure with content type SIMPLE
class standardVolumePerTimeMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'standardVolumePerTimeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 414, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_standardVolumePerTimeMeasure_uom', StandardVolumePerTimeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 420, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 420, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'standardVolumePerTimeMeasure', standardVolumePerTimeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}thermalConductivityMeasure with content type SIMPLE
class thermalConductivityMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermalConductivityMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 425, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_thermalConductivityMeasure_uom', ThermalConductivityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 431, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 431, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'thermalConductivityMeasure', thermalConductivityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}thermalVolumetricExpansionMeasure with content type SIMPLE
class thermalVolumetricExpansionMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermalVolumetricExpansionMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 436, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_thermalVolumetricExpansionMeasure_uom', ThermalVolumetricExpansionUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 442, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 442, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'thermalVolumetricExpansionMeasure', thermalVolumetricExpansionMeasure)


# Complex type {http://www.witsml.org/schemas/1series}thermodynamicTemperatureMeasure with content type SIMPLE
class thermodynamicTemperatureMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}thermodynamicTemperatureMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermodynamicTemperatureMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 447, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_thermodynamicTemperatureMeasure_uom', ThermodynamicTemperatureUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 450, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 450, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'thermodynamicTemperatureMeasure', thermodynamicTemperatureMeasure)


# Complex type {http://www.witsml.org/schemas/1series}timeMeasure with content type SIMPLE
class timeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}timeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 459, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_timeMeasure_uom', TimeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 462, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 462, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'timeMeasure', timeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}velocityMeasure with content type SIMPLE
class velocityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}velocityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'velocityMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 471, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_velocityMeasure_uom', VelocityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 474, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 474, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'velocityMeasure', velocityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}volumeMeasure with content type SIMPLE
class volumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}volumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 483, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_volumeMeasure_uom', VolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 486, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 486, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'volumeMeasure', volumeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}volumeFlowRateMeasure with content type SIMPLE
class volumeFlowRateMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}volumeFlowRateMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumeFlowRateMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 495, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_volumeFlowRateMeasure_uom', VolumeFlowRateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 498, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 498, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'volumeFlowRateMeasure', volumeFlowRateMeasure)


# Complex type {http://www.witsml.org/schemas/1series}volumePerLengthMeasure with content type SIMPLE
class volumePerLengthMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumePerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 507, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_volumePerLengthMeasure_uom', VolumePerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 513, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 513, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'volumePerLengthMeasure', volumePerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}volumePerVolumeMeasure with content type SIMPLE
class volumePerVolumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}volumePerVolumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumePerVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 518, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas1series_volumePerVolumeMeasure_uom', VolumePerVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 521, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 521, 4)
    
    uom = property(__uom.value, __uom.set, None, '')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'volumePerVolumeMeasure', volumePerVolumeMeasure)


toolErrorTermSets = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'toolErrorTermSets'), obj_toolErrorTermSets, documentation='The WITSML API mandated plural root element which allows \n\t\t\tmultiple singular objects to be sent. The plural name is formed by adding\n\t\t\tan "s" to the singular name.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 32, 1))
Namespace.addCategoryObject('elementBinding', toolErrorTermSets.name().localName(), toolErrorTermSets)



cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sourceName'), nameString, scope=cs_commonData, documentation='An identifier to indicate the data originator.\n\t\t\t\t\tThis identifies the server that originally created \n\t\t\t\t\tthe object and thus most of the uids in the object (but not \n\t\t\t\t\tnecessarily the uids of the parents). This is typically a url. ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 26, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dTimCreation'), timestamp, scope=cs_commonData, documentation='When the data was created at the persistent data store. \n\t\t\t\t\tThis is an API server parameter releted to the "Special Handling of Change Information" within a server. \n\t\t\t\t\tSee the relevant API specification for the  behavior related to this element.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 34, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dTimLastChange'), timestamp, scope=cs_commonData, documentation='Last change of any element of the data at the persistent data store.\n\t\t\t\t\tThis is an API server parameter releted to the "Special Handling of Change Information" within a server. \n\t\t\t\t\tSee the relevant API specification for the  behavior related to this element.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 43, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'itemState'), ItemState, scope=cs_commonData, documentation='The item state for the data object.  ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 53, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceCategory'), kindString, scope=cs_commonData, documentation='The category of the service related to the creation of the object. \n\t\t\t\t\tFor example, "mud log service", "cement service", "LWD service", "rig service", "drilling service".\n\t\t\t\t\t', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 58, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comments'), commentString, scope=cs_commonData, documentation='Comments and remarks.  ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 67, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acquisitionTimeZone'), timestampedTimeZone, scope=cs_commonData, documentation='The local time zone of the original acquisition date-time values. \n\t\t\t\t\tIt is the deviation in hours and minutes from UTC.\n\t\t\t\t\tThe first occurrence should be the actual local time zone at the start of acquisition\n\t\t\t\t\tand may represent a seasonally adjusted value such as daylight savings.\n\t\t\t\t\tThe dTim attribute must be populated in the second and subsequent occurrences \n\t\t\t\t\tif the local time zone changes during acquisition.\n\t\t\t\t\tThis knowledge is required because the original time zone in a dateTime\n\t\t\t\t\tvalue may be lost when software converts to a different time zone.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 72, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'defaultDatum'), refNameString, scope=cs_commonData, documentation='A pointer to the default wellDatum for measured depth coordinates,\n\t\t\t\t\tvertical depth coordinates and elevation coordinates in this object. \n\t\t\t\t\tDepth coordinates that do not specify a datum attribute shall be \n\t\t\t\t\tassumed to be measured relative to this default vertical datum.\n\t\t\t\t\tThe referenced wellDatum must be defined within the well object associated with this object.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 85, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'privateGroupOnly'), pyxb.binding.datatypes.boolean, scope=cs_commonData, documentation='This is an API query parameter.\n\t\t\t\t\tSee the API specification for the behavior related to this element.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 95, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionAny'), cs_extensionAny, scope=cs_commonData, documentation='Extensions to the schema using an xsd:any construct.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 102, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), cs_extensionNameValue, scope=cs_commonData, documentation='Extensions to the schema based on a name-value construct.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 108, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 26, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 34, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 43, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 53, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 58, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 67, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 72, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 85, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 95, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 102, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 108, 3))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sourceName')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dTimCreation')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 34, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dTimLastChange')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 43, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'itemState')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 53, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceCategory')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 58, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comments')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 67, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acquisitionTimeZone')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 72, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'defaultDatum')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 85, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'privateGroupOnly')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 95, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionAny')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 102, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 108, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_commonData._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_customData.xsd', 24, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_customData.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_customData._Automaton = _BuildAutomaton_()




cs_documentAudit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'event'), cs_documentEvent, scope=cs_documentAudit, documentation='One event related to the data.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentAudit.xsd', 27, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_documentAudit._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'event')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentAudit.xsd', 27, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_documentAudit._Automaton = _BuildAutomaton_2()




cs_documentFileCreation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileCreationDate'), timestamp, scope=cs_documentFileCreation, documentation='The date and time that the file was created.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 27, 3)))

cs_documentFileCreation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'softwareName'), nameString, scope=cs_documentFileCreation, documentation='If appropriate, the software that created the file. \n\t\t\t\t\tThis is a free form string, and may include whatever information \n\t\t\t\t\tis deemed relevant.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 33, 3)))

cs_documentFileCreation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileCreator'), nameString, scope=cs_documentFileCreation, documentation='The person or business associate that created \n\t\t\t\t\tthe file.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 41, 3)))

cs_documentFileCreation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), commentString, scope=cs_documentFileCreation, documentation='Any comment that would be useful to further \n\t\t\t\t\texplain the creation of this instance document.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 48, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 33, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 41, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 48, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_documentFileCreation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileCreationDate')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 27, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentFileCreation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'softwareName')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentFileCreation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileCreator')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentFileCreation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 48, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_documentFileCreation._Automaton = _BuildAutomaton_3()




cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentName'), nameStruct, scope=cs_documentInfo, documentation='An identifier for the document. This is \n\t\t\t\t\tintended to be unique within the context of the NamingSystem.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 31, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentAlias'), nameStruct, scope=cs_documentInfo, documentation='Zero or more alternate names for the document. \n\t\t\t\t\tThese names do not need to be unique within the naming system.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 38, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentDate'), timestamp, scope=cs_documentInfo, documentation='The date of the creation of the document. \n\t\t\t\t\tThis is not the same as the date that the file was created. \n\t\t\t\t\tFor this date, the document is considered to be the set of \n\t\t\t\t\tinformation associated with this document information. \n\t\t\t\t\tFor example, the document may be a seismic binset. \n\t\t\t\t\tThis represents the date that the binset was created. \n\t\t\t\t\tThe FileCreation information would capture the date that \n\t\t\t\t\tthe XML file was created to send or exchange the binset.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 45, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentClass'), nameStruct, scope=cs_documentInfo, documentation='A document class. Examples of classes would be a \n\t\t\t\t\tmetadata classification or a set of keywords. ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 58, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileCreationInformation'), cs_documentFileCreation, scope=cs_documentInfo, documentation='The information about the creation of the \n\t\t\t\t\texchange file. This is not about the creation of the data within \n\t\t\t\t\tthe file, but the creation of the file itself.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 64, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityInformation'), cs_documentSecurityInfo, scope=cs_documentInfo, documentation='Information about the security to be applied to \n\t\t\t\t\tthis file. More than one classification can be given.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 72, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'disclaimer'), commentString, scope=cs_documentInfo, documentation='A free-form string that allows a disclaimer to \n\t\t\t\t\taccompany the information.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 79, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'auditTrail'), cs_documentAudit, scope=cs_documentInfo, documentation='A collection of events that can document the \n\t\t\t\t\thistory of the data.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 86, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'owner'), nameString, scope=cs_documentInfo, documentation='The owner of the data.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 93, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), commentString, scope=cs_documentInfo, documentation='An optional comment about the document.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 99, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 38, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 45, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 58, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 64, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=5, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 72, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 79, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 86, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 93, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 99, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentName')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 31, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentAlias')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 38, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentDate')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 45, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentClass')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 58, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileCreationInformation')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 64, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'securityInformation')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 72, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'disclaimer')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 79, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'auditTrail')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 86, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'owner')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 93, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 99, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_documentInfo._Automaton = _BuildAutomaton_4()




def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionAny.xsd', 26, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionAny.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_extensionAny._Automaton = _BuildAutomaton_5()




cs_iscwsaAuthorizationData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'author'), nameString, scope=cs_iscwsaAuthorizationData, documentation='Person responsible for the information.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 26, 3)))

cs_iscwsaAuthorizationData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), nameString, scope=cs_iscwsaAuthorizationData, documentation='Source from which the information is derived.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 31, 3)))

cs_iscwsaAuthorizationData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authority'), nameString, scope=cs_iscwsaAuthorizationData, documentation='Person or collective body responsible for authorizing the information.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 36, 3)))

cs_iscwsaAuthorizationData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), AuthorizationStatus, scope=cs_iscwsaAuthorizationData, documentation='Authorization state of the information.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 41, 3)))

cs_iscwsaAuthorizationData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'version'), nameString, scope=cs_iscwsaAuthorizationData, documentation='Version name or number.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 46, 3)))

cs_iscwsaAuthorizationData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), commentString, scope=cs_iscwsaAuthorizationData, documentation='A comment about the object. \n\t\t\t\t\tThis should include information regarding the derivation of the information.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 51, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 26, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 46, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 51, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaAuthorizationData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'author')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaAuthorizationData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaAuthorizationData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authority')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 36, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaAuthorizationData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 41, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaAuthorizationData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'version')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 46, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaAuthorizationData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaAuthorizationData.xsd', 51, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_iscwsaAuthorizationData._Automaton = _BuildAutomaton_6()




cs_iscwsaNomenclature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), cs_iscwsaNameAndDescription, scope=cs_iscwsaNomenclature, documentation='Variable names used within a function.\n\t\t\t\t\tEach parameter name must be unique within the context of this nomenclature.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 27, 3)))

cs_iscwsaNomenclature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'function'), cs_iscwsaNameAndDescription, scope=cs_iscwsaNomenclature, documentation='Mathmatical function used to generate error term values from parameters.\n\t\t\t\t\tEach function name must be unique within the context of this nomenclature.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 33, 3)))

cs_iscwsaNomenclature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'constant'), cs_iscwsaNomenclatureConstant, scope=cs_iscwsaNomenclature, documentation='Numerical constant used by functions.\n\t\t\t\t\tEach constant name must be unique within the context of this nomenclature.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 39, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 27, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 39, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNomenclature._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 27, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNomenclature._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNomenclature._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'constant')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclature.xsd', 39, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_iscwsaNomenclature._Automaton = _BuildAutomaton_7()




obj_toolErrorTermSets._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentInfo'), cs_documentInfo, scope=obj_toolErrorTermSets, documentation='Information about the XML message instance.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 45, 5)))

obj_toolErrorTermSets._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'toolErrorTermSet'), obj_toolErrorTermSet, scope=obj_toolErrorTermSets, documentation='A single error term set.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 50, 5)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 45, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_toolErrorTermSets._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentInfo')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 45, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(obj_toolErrorTermSets._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'toolErrorTermSet')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 50, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
obj_toolErrorTermSets._Automaton = _BuildAutomaton_8()




cs_documentEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eventDate'), timestamp, scope=cs_documentEvent, documentation='The date on which the event took place.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 28, 3)))

cs_documentEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eventType'), nameString, scope=cs_documentEvent, documentation='The kind of event event.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 34, 3)))

cs_documentEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responsibleParty'), nameString, scope=cs_documentEvent, documentation='The party responsible for the event.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 40, 3)))

cs_documentEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), commentString, scope=cs_documentEvent, documentation='A free form comment that can further \n\t\t\t\t\tdefine the event that occurred.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 46, 3)))

cs_documentEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), cs_extensionNameValue, scope=cs_documentEvent, documentation='Extensions to the schema based on a name-value construct.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 53, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 34, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 40, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 46, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 53, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_documentEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eventDate')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 28, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eventType')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 34, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responsibleParty')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 40, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 46, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 53, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_documentEvent._Automaton = _BuildAutomaton_9()




cs_documentSecurityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'class'), kindString, scope=cs_documentSecurityInfo, documentation='The security class in which this document is \n\t\t\t\t\tclassified. Examples would be confidential, partner confidential, \n\t\t\t\t\ttight. The meaning of the class is determined by the System in which \n\t\t\t\t\tit is defined.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 33, 3)))

cs_documentSecurityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securitySystem'), kindString, scope=cs_documentSecurityInfo, documentation='The security classification system. \n\t\t\t\t\tThis gives context to the meaning of the Class value.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 42, 3)))

cs_documentSecurityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endDate'), timestamp, scope=cs_documentSecurityInfo, documentation='The date on which this security class is no \n\t\t\t\t\tlonger applicable.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 49, 3)))

cs_documentSecurityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), commentString, scope=cs_documentSecurityInfo, documentation='A general comment to further define the security \n\t\t\t\t\tclass.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 56, 3)))

cs_documentSecurityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), cs_extensionNameValue, scope=cs_documentSecurityInfo, documentation='Extensions to the schema based on a name-value construct.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 63, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 33, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 42, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 49, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 56, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 63, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentSecurityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 33, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentSecurityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'securitySystem')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 42, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentSecurityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endDate')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 49, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentSecurityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 56, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentSecurityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 63, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_documentSecurityInfo._Automaton = _BuildAutomaton_10()




cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), ExtensionName, scope=cs_extensionNameValue, documentation='The name of the extension.\n\t\t\t\t\tEach standard name should document the expected measure class.\n\t\t\t\t\tEach standard name should document the expected maximum size. \n\t\t\t\t\tFor numeric values the size should be in terms of xsd types\n\t\t\t\t\tsuch as int, long, short, byte, float or double.\n\t\t\t\t\tFor strings, the maximum length should be defined in number of characters.\n\t\t\t\t\tLocal extensions to the list of standard names are allowed but it is strongly\n\t\t\t\t\trecommended that the names and definitions be approved by the \n\t\t\t\t\tWITSML SIG Technical Team before use.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 29, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), extensionvalue, scope=cs_extensionNameValue, documentation='The value of the extension. \n\t\t\t\t\tThis may also include a uom attribute. \n\t\t\t\t\tThe content should conform to constraints defined by the data type.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 42, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dataType'), PrimitiveType, scope=cs_extensionNameValue, documentation='The underlying XML type of the value.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 49, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dTim'), timestamp, scope=cs_extensionNameValue, documentation='The date-time associated with the value.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 54, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'md'), measuredDepthCoord, scope=cs_extensionNameValue, documentation='The measured depth associated with the value.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 59, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'index'), positiveCount, scope=cs_extensionNameValue, documentation='Indexes things with the same name. \n\t\t\t\t\tThat is, 1 indicates the first one, 2 incidates the second one, etc.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 64, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measureClass'), MeasureClass, scope=cs_extensionNameValue, documentation='The kind of the measure. For example, "length".\n\t\t\t\t\tThis should be specified if the value requires a unit of measure.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 70, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), descriptionString, scope=cs_extensionNameValue, documentation='A textual description of the extension.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 76, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 54, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 59, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 64, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 70, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 76, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 29, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 42, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dataType')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 49, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dTim')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 54, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'md')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 59, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'index')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 64, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measureClass')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 70, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 76, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_extensionNameValue._Automaton = _BuildAutomaton_11()




cs_iscwsaErrorCoefficient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'azi'), commentString, scope=cs_iscwsaErrorCoefficient, documentation='Measured horizontal azimuth.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 28, 7)))

cs_iscwsaErrorCoefficient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inc'), commentString, scope=cs_iscwsaErrorCoefficient, documentation='Measured deviation from vertical.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 33, 7)))

cs_iscwsaErrorCoefficient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'depth'), commentString, scope=cs_iscwsaErrorCoefficient, documentation='Measured depth along the wellbore.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 38, 7)))

cs_iscwsaErrorCoefficient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tvd'), commentString, scope=cs_iscwsaErrorCoefficient, documentation='True Vertical Depth.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 43, 7)))

cs_iscwsaErrorCoefficient._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), cs_extensionNameValue, scope=cs_iscwsaErrorCoefficient, documentation='Extensions to the schema based on a name-value construct.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 49, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 49, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'azi')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 28, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inc')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 33, 7))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'depth')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 38, 7))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tvd')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 43, 7))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorCoefficient._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorCoefficient.xsd', 49, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_iscwsaErrorCoefficient._Automaton = _BuildAutomaton_12()




cs_iscwsaErrorTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), nameString, scope=cs_iscwsaErrorTerm, documentation='This is the unique mnemonic for this term. \n\t\t\t\t\tFor example, "ABIX" or "DECR".', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 29, 3)))

cs_iscwsaErrorTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), ErrorTermSource, scope=cs_iscwsaErrorTerm, documentation='The class of the error source.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 35, 3)))

cs_iscwsaErrorTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measureClass'), MeasureClass, scope=cs_iscwsaErrorTerm, documentation='The kind of quantity that the term represents.\n\t\t\t\t\tThis constrains the unit that can be used for any errorTermValues.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 40, 3)))

cs_iscwsaErrorTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'label'), nameString, scope=cs_iscwsaErrorTerm, documentation='Human-readable name for the term, may be presented in \n\t\t\t\t\tapplication software. E.g., "MWD: X-Acceleromter Bias with Z-Axis Corr."', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 46, 3)))

cs_iscwsaErrorTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), commentString, scope=cs_iscwsaErrorTerm, documentation='Human-readable name for the term, may be presented in \n\t\t\t\t\tapplication software. E.g., "MWD: X-Acceleromter Bias with Z-Axis Corr."', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 52, 3)))

cs_iscwsaErrorTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errorCoefficient'), cs_iscwsaErrorCoefficient, scope=cs_iscwsaErrorTerm, documentation='Describes what measurement(s) the error variance(s) apply to.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 58, 3)))

cs_iscwsaErrorTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'operatingMode'), SurveyToolOperatingMode, scope=cs_iscwsaErrorTerm, documentation='Operating mode that is valid for this error term.\n\t\t\t\t\tIn the absence of this element assume Stationary.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 63, 3)))

cs_iscwsaErrorTerm._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), cs_extensionNameValue, scope=cs_iscwsaErrorTerm, documentation='Extensions to the schema based on a name-value construct.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 69, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 35, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 40, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 52, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 63, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 69, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorTerm._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 29, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorTerm._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 35, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorTerm._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measureClass')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 40, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorTerm._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'label')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 46, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorTerm._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 52, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorTerm._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorCoefficient')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 58, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorTerm._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'operatingMode')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 63, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaErrorTerm._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaErrorTerm.xsd', 69, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_iscwsaErrorTerm._Automaton = _BuildAutomaton_13()




cs_iscwsaNameAndDescription._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), nameString, scope=cs_iscwsaNameAndDescription, documentation='The name of the item.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 28, 3)))

cs_iscwsaNameAndDescription._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), commentString, scope=cs_iscwsaNameAndDescription, documentation='A textual description of the item.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 33, 3)))

cs_iscwsaNameAndDescription._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), cs_extensionNameValue, scope=cs_iscwsaNameAndDescription, documentation='Extensions to the schema based on a name-value construct.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 38, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 38, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNameAndDescription._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 28, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNameAndDescription._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNameAndDescription._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNameAndDescription.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_iscwsaNameAndDescription._Automaton = _BuildAutomaton_14()




cs_iscwsaNomenclatureConstant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), nameString, scope=cs_iscwsaNomenclatureConstant, documentation='The name of the constant.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 27, 3)))

cs_iscwsaNomenclatureConstant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.double, scope=cs_iscwsaNomenclatureConstant, documentation='The value of the constant.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 32, 3)))

cs_iscwsaNomenclatureConstant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unit'), uomString, scope=cs_iscwsaNomenclatureConstant, documentation='The unit of measure of the constant.\n\t\t\t\t\tThis value must match an acronym from the WITSML unit of measure dictionary.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 37, 3)))

cs_iscwsaNomenclatureConstant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), commentString, scope=cs_iscwsaNomenclatureConstant, documentation='A textual description of the constant.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 43, 3)))

cs_iscwsaNomenclatureConstant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue'), cs_extensionNameValue, scope=cs_iscwsaNomenclatureConstant, documentation='Extensions to the schema based on a name-value construct.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 48, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 48, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNomenclatureConstant._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 27, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNomenclatureConstant._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 32, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNomenclatureConstant._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unit')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 37, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNomenclatureConstant._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 43, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_iscwsaNomenclatureConstant._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionNameValue')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_iscwsaNomenclatureConstant.xsd', 48, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_iscwsaNomenclatureConstant._Automaton = _BuildAutomaton_15()




obj_toolErrorTermSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authorization'), cs_iscwsaAuthorizationData, scope=obj_toolErrorTermSet, documentation='The definitive source for this set of error terms.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 28, 3)))

obj_toolErrorTermSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nomenclature'), cs_iscwsaNomenclature, scope=obj_toolErrorTermSet, documentation='Defines the nomenclature used in the error terms.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 33, 3)))

obj_toolErrorTermSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errorTerm'), cs_iscwsaErrorTerm, scope=obj_toolErrorTermSet, documentation='Defines an error term.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 38, 3)))

obj_toolErrorTermSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), nameString, scope=obj_toolErrorTermSet, documentation='Human-readable name for the set of terms.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 72, 3)))

obj_toolErrorTermSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'commonData'), cs_commonData, scope=obj_toolErrorTermSet, documentation='A container element that contains elements that are common to all data \n\t\t\t\t\tobjects.  ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 82, 3)))

obj_toolErrorTermSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customData'), cs_customData, scope=obj_toolErrorTermSet, documentation='A container element that can contain custom or user defined \n\t\t\t\t\tdata elements.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 88, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 28, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 38, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 77, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 82, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 88, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(obj_toolErrorTermSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authorization')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 28, 3))
    st_0 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(obj_toolErrorTermSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nomenclature')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(obj_toolErrorTermSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorTerm')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_toolErrorTermSet.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(obj_toolErrorTermSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 72, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(obj_toolErrorTermSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'commonData')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 82, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(obj_toolErrorTermSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customData')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_toolErrorTermSet.xsd', 88, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_3, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
obj_toolErrorTermSet._Automaton = _BuildAutomaton_16()


toolErrorTermSets._setSubstitutionGroup(_abs.abstractDataObject)
