# .\witsml1311_obj_bhaRun.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:aca2769132b0274e00b9254c973534926b1b1a29
# Generated 2013-06-21 14:46:34.591000 by PyXB version 1.2.1
# Namespace http://www.witsml.org/schemas/131

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:464f6f91-daab-11e2-991a-08002718187b')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI('http://www.witsml.org/schemas/131', create_if_missing=True)
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


# Atomic simple type: {http://www.witsml.org/schemas/131}abstractBoolean
class abstractBoolean (pyxb.binding.datatypes.boolean):

    """This type disallows an "empty" boolean value.
			This type should not be used directly except to derive another type.
			All boolean types should be derived from this type rather than using xsd:boolen."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractBoolean')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 20, 1)
    _Documentation = 'This type disallows an "empty" boolean value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll boolean types should be derived from this type rather than using xsd:boolen.'
abstractBoolean._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractBoolean._CF_pattern.addPattern(pattern='.+')
abstractBoolean._InitializeFacetMap(abstractBoolean._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractBoolean', abstractBoolean)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractDateTime
class abstractDateTime (pyxb.binding.datatypes.dateTime):

    """This type disallows an "empty" dateTime value.
			This type should not be used directly except to derive another type.
			All dateTime types should be derived from this type rather than using xsd:dateTime."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractDateTime')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 31, 1)
    _Documentation = 'This type disallows an "empty" dateTime value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll dateTime types should be derived from this type rather than using xsd:dateTime.'
abstractDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDateTime._CF_pattern.addPattern(pattern='.+')
abstractDateTime._InitializeFacetMap(abstractDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractDateTime', abstractDateTime)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractDate
class abstractDate (pyxb.binding.datatypes.date):

    """This type disallows an "empty" date value.
			This type should not be used directly except to derive another type.
			All dateTime types should be derived from this type rather than using xsd:dateTime."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractDate')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 42, 1)
    _Documentation = 'This type disallows an "empty" date value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll dateTime types should be derived from this type rather than using xsd:dateTime.'
abstractDate._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDate._CF_pattern.addPattern(pattern='.+')
abstractDate._InitializeFacetMap(abstractDate._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractDate', abstractDate)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractYear
class abstractYear (pyxb.binding.datatypes.gYear):

    """This type disallows an "empty" gYear value.
			This type should not be used directly except to derive another type.
			All year types should be derived from this type rather than using xsd:gYear."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractYear')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 53, 1)
    _Documentation = 'This type disallows an "empty" gYear value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll year types should be derived from this type rather than using xsd:gYear.'
abstractYear._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractYear._CF_pattern.addPattern(pattern='.+')
abstractYear._InitializeFacetMap(abstractYear._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractYear', abstractYear)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractDouble
class abstractDouble (pyxb.binding.datatypes.double):

    """This type disallows an "empty" double value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractDouble')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 64, 1)
    _Documentation = 'This type disallows an "empty" double value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractDouble._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDouble._CF_pattern.addPattern(pattern='.+')
abstractDouble._InitializeFacetMap(abstractDouble._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractDouble', abstractDouble)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractShort
class abstractShort (pyxb.binding.datatypes.short):

    """This type disallows an "empty" short value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractShort')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 74, 1)
    _Documentation = 'This type disallows an "empty" short value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractShort._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractShort._CF_pattern.addPattern(pattern='.+')
abstractShort._InitializeFacetMap(abstractShort._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractShort', abstractShort)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractInt
class abstractInt (pyxb.binding.datatypes.int):

    """This type disallows an "empty" int value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractInt')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 84, 1)
    _Documentation = 'This type disallows an "empty" int value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractInt._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractInt._CF_pattern.addPattern(pattern='.+')
abstractInt._InitializeFacetMap(abstractInt._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractInt', abstractInt)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractString
class abstractString (pyxb.binding.datatypes.string):

    """The intended abstract supertype of all strings.
			This abstract type allows the control over whitespace for all strings to be defined at a high level. 
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 94, 1)
    _Documentation = 'The intended abstract supertype of all strings.\n\t\t\tThis abstract type allows the control over whitespace for all strings to be defined at a high level. \n\t\t\tThis type should not be used directly except to derive another type.'
abstractString._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
abstractString._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
abstractString._InitializeFacetMap(abstractString._CF_minLength,
   abstractString._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'abstractString', abstractString)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractUncollapsedString
class abstractUncollapsedString (pyxb.binding.datatypes.string):

    """The intended abstract supertype of all strings that must maintain whitespace. 
			The type abstractString should normally be used.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractUncollapsedString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 145, 1)
    _Documentation = 'The intended abstract supertype of all strings that must maintain whitespace. \n\t\t\tThe type abstractString should normally be used.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractUncollapsedString._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
abstractUncollapsedString._InitializeFacetMap(abstractUncollapsedString._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'abstractUncollapsedString', abstractUncollapsedString)

# Union simple type: {http://www.witsml.org/schemas/131}anyDate
# superclasses pyxb.binding.datatypes.anySimpleType
class anyDate (pyxb.binding.basis.STD_union):

    """A union of date and dateTime, so that time is not mandatory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'anyDate')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 20, 1)
    _Documentation = 'A union of date and dateTime, so that time is not mandatory.'

    _MemberTypes = ( pyxb.binding.datatypes.dateTime, pyxb.binding.datatypes.date, pyxb.binding.datatypes.gYearMonth, pyxb.binding.datatypes.gYear, )
anyDate._CF_pattern = pyxb.binding.facets.CF_pattern()
anyDate._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=anyDate)
anyDate._InitializeFacetMap(anyDate._CF_pattern,
   anyDate._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'anyDate', anyDate)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractMaximumLengthString
class abstractMaximumLengthString (abstractString):

    """This defines the maximum acceptable length of a
			string that can be stored in a data base."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractMaximumLengthString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 129, 1)
    _Documentation = 'This defines the maximum acceptable length of a\n\t\t\tstring that can be stored in a data base.'
abstractMaximumLengthString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000))
abstractMaximumLengthString._InitializeFacetMap(abstractMaximumLengthString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractMaximumLengthString', abstractMaximumLengthString)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractPositiveCount
class abstractPositiveCount (abstractShort):

    """A positive integer (one based count or index) with a maximum value of 32767 (2-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractPositiveCount')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 162, 1)
    _Documentation = 'A positive integer (one based count or index) with a maximum value of 32767 (2-bytes).'
abstractPositiveCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=abstractPositiveCount, value=pyxb.binding.datatypes.short(1))
abstractPositiveCount._InitializeFacetMap(abstractPositiveCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'abstractPositiveCount', abstractPositiveCount)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractNameString
class abstractNameString (abstractString):

    """The intended abstract supertype of all user assigned human 
			recognizable contextual name types. 
			There should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.
			This type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractNameString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 177, 1)
    _Documentation = 'The intended abstract supertype of all user assigned human \n\t\t\trecognizable contextual name types. \n\t\t\tThere should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.\n\t\t\tThis type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration.'
abstractNameString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
abstractNameString._InitializeFacetMap(abstractNameString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractNameString', abstractNameString)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractUidString
class abstractUidString (abstractString):

    """The intended abstract supertype of all locally unique identifiers. 
			The value is not intended to convey any semantic content (e.g., it may be computer generated). 
			The value is only required to be unique within a context in a document (e.g., defined via key and keyref). 
			There is no guarantee that the same data in multiple documents will utilize the same uid value 
			unless enforced by the source of the document (e.g., a document server).
			Spaces are not allowed."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractUidString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 189, 1)
    _Documentation = 'The intended abstract supertype of all locally unique identifiers. \n\t\t\tThe value is not intended to convey any semantic content (e.g., it may be computer generated). \n\t\t\tThe value is only required to be unique within a context in a document (e.g., defined via key and keyref). \n\t\t\tThere is no guarantee that the same data in multiple documents will utilize the same uid value \n\t\t\tunless enforced by the source of the document (e.g., a document server).\n\t\t\tSpaces are not allowed.'
abstractUidString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
abstractUidString._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractUidString._CF_pattern.addPattern(pattern='[^ ]*')
abstractUidString._InitializeFacetMap(abstractUidString._CF_maxLength,
   abstractUidString._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'abstractUidString', abstractUidString)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractTypeEnum
class abstractTypeEnum (abstractString):

    """The intended abstract supertype of all enumerated "types".
			This abstract type allows the maximum length of a type enumeration to be centrally defined.
			This type should not be used directly except to derive another type.
			It should also be used for uncontrolled strings which are candidates to become enumerations at a future date."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 215, 1)
    _Documentation = 'The intended abstract supertype of all enumerated "types".\n\t\t\tThis abstract type allows the maximum length of a type enumeration to be centrally defined.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tIt should also be used for uncontrolled strings which are candidates to become enumerations at a future date.'
abstractTypeEnum._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
abstractTypeEnum._InitializeFacetMap(abstractTypeEnum._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractTypeEnum', abstractTypeEnum)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractUomEnum
class abstractUomEnum (abstractString):

    """The intended abstract supertype of all "units of measure".
			This abstract type allows the maximum length of a UOM enumeration to be centrally defined. 
			This type is abstract in the sense that it should not be used directly 
			except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractUomEnum')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 227, 1)
    _Documentation = 'The intended abstract supertype of all "units of measure".\n\t\t\tThis abstract type allows the maximum length of a UOM enumeration to be centrally defined. \n\t\t\tThis type is abstract in the sense that it should not be used directly \n\t\t\texcept to derive another type.'
abstractUomEnum._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(24))
abstractUomEnum._InitializeFacetMap(abstractUomEnum._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'abstractUomEnum', abstractUomEnum)

# Atomic simple type: {http://www.witsml.org/schemas/131}logicalBoolean
class logicalBoolean (abstractBoolean):

    """Values of "true" (or "1") and "false" (or "0")."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'logicalBoolean')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 63, 1)
    _Documentation = 'Values of "true" (or "1") and "false" (or "0").'
logicalBoolean._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'logicalBoolean', logicalBoolean)

# Atomic simple type: {http://www.witsml.org/schemas/131}date
class date (abstractDate):

    """A julian date."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'date')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 70, 1)
    _Documentation = 'A julian date.'
date._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'date', date)

# Atomic simple type: {http://www.witsml.org/schemas/131}timestamp
class timestamp (abstractDateTime):

    """A date with the time of day and an optional time zone.
			While the time zone is optional, it is strongly advised that the zone 
			always be specified in each date time value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timestamp')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 77, 1)
    _Documentation = 'A date with the time of day and an optional time zone.\n\t\t\tWhile the time zone is optional, it is strongly advised that the zone \n\t\t\talways be specified in each date time value.'
timestamp._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'timestamp', timestamp)

# Atomic simple type: {http://www.witsml.org/schemas/131}timeZone
class timeZone (abstractString):

    """A time zone conforming to the XSD:dateTime specification.
			It should be of the form "Z" or "shh.mm" where 
				"s" is "+" or "-", 
				"hh" is 00 to 23 and
				"mm" is 00 to 59."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeZone')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 86, 1)
    _Documentation = 'A time zone conforming to the XSD:dateTime specification.\n\t\t\tIt should be of the form "Z" or "shh.mm" where \n\t\t\t\t"s" is "+" or "-", \n\t\t\t\t"hh" is 00 to 23 and\n\t\t\t\t"mm" is 00 to 59.'
timeZone._CF_pattern = pyxb.binding.facets.CF_pattern()
timeZone._CF_pattern.addPattern(pattern='[Z]|([-+](([01][0-9])|(2[0-3])):[0-5][0-9])')
timeZone._InitializeFacetMap(timeZone._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'timeZone', timeZone)

# Atomic simple type: {http://www.witsml.org/schemas/131}calendarYear
class calendarYear (abstractYear):

    """A calendar year (CCYY) in the gregorian calendar."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'calendarYear')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 99, 1)
    _Documentation = 'A calendar year (CCYY) in the gregorian calendar.'
calendarYear._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'calendarYear', calendarYear)

# Atomic simple type: {http://www.witsml.org/schemas/131}unitlessQuantity
class unitlessQuantity (abstractDouble):

    """A unitless quantity. This should not 
			be confused with a dimensionless measure."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unitlessQuantity')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 145, 1)
    _Documentation = 'A unitless quantity. This should not \n\t\t\tbe confused with a dimensionless measure.'
unitlessQuantity._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'unitlessQuantity', unitlessQuantity)

# List simple type: {http://www.witsml.org/schemas/131}listOfDouble
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfDouble (pyxb.binding.basis.STD_list):

    """
				A representation of a list of xsd:double values.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'listOfDouble')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 224, 1)
    _Documentation = '\n\t\t\t\tA representation of a list of xsd:double values.\n\t\t\t'

    _ItemType = abstractDouble
listOfDouble._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'listOfDouble', listOfDouble)

# Atomic simple type: {http://www.witsml.org/schemas/131}descriptionString
class descriptionString (abstractString):

    """A textual description of something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'descriptionString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 331, 1)
    _Documentation = 'A textual description of something.'
descriptionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
descriptionString._InitializeFacetMap(descriptionString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'descriptionString', descriptionString)

# Atomic simple type: {http://www.witsml.org/schemas/131}shortDescriptionString
class shortDescriptionString (abstractString):

    """A short textual description of something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'shortDescriptionString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 340, 1)
    _Documentation = 'A short textual description of something.'
shortDescriptionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
shortDescriptionString._InitializeFacetMap(shortDescriptionString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'shortDescriptionString', shortDescriptionString)

# Atomic simple type: {http://www.witsml.org/schemas/131}encodedValueString
class encodedValueString (abstractString):

    """A single value. The encoding may utilize 
			any of several xsd encodings. Something external to the value must
			define the encoding."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'encodedValueString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 364, 1)
    _Documentation = 'A single value. The encoding may utilize \n\t\t\tany of several xsd encodings. Something external to the value must\n\t\t\tdefine the encoding.'
encodedValueString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
encodedValueString._InitializeFacetMap(encodedValueString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'encodedValueString', encodedValueString)

# Atomic simple type: {http://www.witsml.org/schemas/131}schemaVersionString
class schemaVersionString (abstractString):

    """The version of the schema.
			The first three levels are fixed. The fourth level can vary
			to represent on the constraints defined in enumerations and 
			XML loader files. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'schemaVersionString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 411, 1)
    _Documentation = 'The version of the schema.\n\t\t\tThe first three levels are fixed. The fourth level can vary\n\t\t\tto represent on the constraints defined in enumerations and \n\t\t\tXML loader files. '
schemaVersionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
schemaVersionString._CF_pattern = pyxb.binding.facets.CF_pattern()
schemaVersionString._CF_pattern.addPattern(pattern='1\\.3\\.1\\.([1-9]|([1-9][0-9]))')
schemaVersionString._InitializeFacetMap(schemaVersionString._CF_maxLength,
   schemaVersionString._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'schemaVersionString', schemaVersionString)

# Atomic simple type: {http://www.witsml.org/schemas/131}uncollapsedString
class uncollapsedString (abstractUncollapsedString):

    """A textual string that retains all whitespace."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uncollapsedString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 460, 1)
    _Documentation = 'A textual string that retains all whitespace.'
uncollapsedString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
uncollapsedString._InitializeFacetMap(uncollapsedString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'uncollapsedString', uncollapsedString)

# Atomic simple type: {http://www.witsml.org/schemas/131}iadcBearingWearCode
class iadcBearingWearCode (abstractString):

    """IADC bearing wear code: integer 0 - 8 or one of the letters E, F, N or X. ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'iadcBearingWearCode')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 469, 1)
    _Documentation = 'IADC bearing wear code: integer 0 - 8 or one of the letters E, F, N or X. .'
iadcBearingWearCode._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
iadcBearingWearCode._CF_pattern = pyxb.binding.facets.CF_pattern()
iadcBearingWearCode._CF_pattern.addPattern(pattern='[0-8EFNX]')
iadcBearingWearCode._InitializeFacetMap(iadcBearingWearCode._CF_maxLength,
   iadcBearingWearCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'iadcBearingWearCode', iadcBearingWearCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}geodeticZoneString
class geodeticZoneString (abstractString):

    """A geodetic zone with values from 1 to 60 and a required direction 
			of "N" (North) or "S" (South). For example, "21N"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geodeticZoneString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 479, 1)
    _Documentation = 'A geodetic zone with values from 1 to 60 and a required direction \n\t\t\tof "N" (North) or "S" (South). For example, "21N".'
geodeticZoneString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
geodeticZoneString._CF_pattern = pyxb.binding.facets.CF_pattern()
geodeticZoneString._CF_pattern.addPattern(pattern='([1-9]|[1-5][0-9]|60)[NS]')
geodeticZoneString._InitializeFacetMap(geodeticZoneString._CF_maxLength,
   geodeticZoneString._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'geodeticZoneString', geodeticZoneString)

# Atomic simple type: {http://www.witsml.org/schemas/131}nonNegativeCount
class nonNegativeCount (abstractShort):

    """A non-negative integer (zero based count or index) with a maximum value of 32767 (2-bytes).
			For items that represent "number of" something or a "sequential" count or index."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nonNegativeCount')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 624, 1)
    _Documentation = 'A non-negative integer (zero based count or index) with a maximum value of 32767 (2-bytes).\n\t\t\tFor items that represent "number of" something or a "sequential" count or index.'
nonNegativeCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=nonNegativeCount, value=pyxb.binding.datatypes.short(0))
nonNegativeCount._InitializeFacetMap(nonNegativeCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'nonNegativeCount', nonNegativeCount)

# Atomic simple type: {http://www.witsml.org/schemas/131}positiveBigCount
class positiveBigCount (abstractInt):

    """A large positive integer (one based count or index) with a maximum value of 2,147,483,647 (4-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positiveBigCount')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 651, 1)
    _Documentation = 'A large positive integer (one based count or index) with a maximum value of 2,147,483,647 (4-bytes).'
positiveBigCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveBigCount, value=pyxb.binding.datatypes.int(1))
positiveBigCount._InitializeFacetMap(positiveBigCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'positiveBigCount', positiveBigCount)

# Atomic simple type: {http://www.witsml.org/schemas/131}integerCount
class integerCount (abstractInt):

    """A positive or negative count with a maximum positive value of 2147483647 (4-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerCount')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 664, 1)
    _Documentation = 'A positive or negative count with a maximum positive value of 2147483647 (4-bytes).'
integerCount._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'integerCount', integerCount)

# Atomic simple type: {http://www.witsml.org/schemas/131}beaufortScaleIntegerCode
class beaufortScaleIntegerCode (abstractShort):

    """An estimate wind strength based on the Beaufort Wind Scale. 
			Values range from 0 (calm) to 12 (hurricane). """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'beaufortScaleIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 671, 1)
    _Documentation = 'An estimate wind strength based on the Beaufort Wind Scale. \n\t\t\tValues range from 0 (calm) to 12 (hurricane). '
beaufortScaleIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=beaufortScaleIntegerCode, value=pyxb.binding.datatypes.short(0))
beaufortScaleIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=beaufortScaleIntegerCode, value=pyxb.binding.datatypes.short(12))
beaufortScaleIntegerCode._InitializeFacetMap(beaufortScaleIntegerCode._CF_minInclusive,
   beaufortScaleIntegerCode._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'beaufortScaleIntegerCode', beaufortScaleIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}pumpActionIntegerCode
class pumpActionIntegerCode (abstractShort):

    """Pump Action: 1 = Single acting, 2 = double acting."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pumpActionIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 682, 1)
    _Documentation = 'Pump Action: 1 = Single acting, 2 = double acting.'
pumpActionIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=pumpActionIntegerCode, value=pyxb.binding.datatypes.short(1))
pumpActionIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=pumpActionIntegerCode, value=pyxb.binding.datatypes.short(2))
pumpActionIntegerCode._InitializeFacetMap(pumpActionIntegerCode._CF_minInclusive,
   pumpActionIntegerCode._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'pumpActionIntegerCode', pumpActionIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}iadcIntegerCode
class iadcIntegerCode (abstractShort):

    """IADC codes: 0 to 8."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'iadcIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 692, 1)
    _Documentation = 'IADC codes: 0 to 8.'
iadcIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=iadcIntegerCode, value=pyxb.binding.datatypes.short(0))
iadcIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=iadcIntegerCode, value=pyxb.binding.datatypes.short(8))
iadcIntegerCode._InitializeFacetMap(iadcIntegerCode._CF_minInclusive,
   iadcIntegerCode._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'iadcIntegerCode', iadcIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}levelIntegerCode
class levelIntegerCode (abstractShort):

    """Integer level code from 1 through 5."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'levelIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 702, 1)
    _Documentation = 'Integer level code from 1 through 5.'
levelIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=levelIntegerCode, value=pyxb.binding.datatypes.short(0))
levelIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=levelIntegerCode, value=pyxb.binding.datatypes.short(8))
levelIntegerCode._InitializeFacetMap(levelIntegerCode._CF_minInclusive,
   levelIntegerCode._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'levelIntegerCode', levelIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}str2
class str2 (abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'str2')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 738, 1)
    _Documentation = None
str2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
str2._InitializeFacetMap(str2._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'str2', str2)

# Atomic simple type: {http://www.witsml.org/schemas/131}str16
class str16 (abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'str16')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 744, 1)
    _Documentation = None
str16._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
str16._InitializeFacetMap(str16._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'str16', str16)

# Atomic simple type: {http://www.witsml.org/schemas/131}str32
class str32 (abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'str32')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 750, 1)
    _Documentation = None
str32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
str32._InitializeFacetMap(str32._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'str32', str32)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractCommentString
class abstractCommentString (abstractMaximumLengthString):

    """The intended abstract supertype of all comments or remarks 
			intended for human consumption. 
			There should be no assumption that semantics can be extracted from the field by a computer. 
			Neither should there be an assumption that any two humans will interpret the information 
			in the same way (i.e., it may not be interoperable)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractCommentString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 204, 1)
    _Documentation = 'The intended abstract supertype of all comments or remarks \n\t\t\tintended for human consumption. \n\t\t\tThere should be no assumption that semantics can be extracted from the field by a computer. \n\t\t\tNeither should there be an assumption that any two humans will interpret the information \n\t\t\tin the same way (i.e., it may not be interoperable).'
abstractCommentString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'abstractCommentString', abstractCommentString)

# Atomic simple type: {http://www.witsml.org/schemas/131}ActivityClassType
class ActivityClassType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActivityClassType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 23, 1)
    _Documentation = None
ActivityClassType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ActivityClassType, enum_prefix=None)
ActivityClassType.planned = ActivityClassType._CF_enumeration.addEnumeration(unicode_value='planned', tag='planned')
ActivityClassType.unplanned = ActivityClassType._CF_enumeration.addEnumeration(unicode_value='unplanned', tag='unplanned')
ActivityClassType.downtime = ActivityClassType._CF_enumeration.addEnumeration(unicode_value='downtime', tag='downtime')
ActivityClassType.unknown = ActivityClassType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ActivityClassType._InitializeFacetMap(ActivityClassType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ActivityClassType', ActivityClassType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ActivityCode
class ActivityCode (abstractTypeEnum):

    """Activity codes.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActivityCode')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 50, 1)
    _Documentation = 'Activity codes.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
ActivityCode._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ActivityCode', ActivityCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}AziRef
class AziRef (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AziRef')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 59, 1)
    _Documentation = None
AziRef._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AziRef, enum_prefix=None)
AziRef.magnetic_north = AziRef._CF_enumeration.addEnumeration(unicode_value='magnetic north', tag='magnetic_north')
AziRef.grid_north = AziRef._CF_enumeration.addEnumeration(unicode_value='grid north', tag='grid_north')
AziRef.true_north = AziRef._CF_enumeration.addEnumeration(unicode_value='true north', tag='true_north')
AziRef.unknown = AziRef._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
AziRef._InitializeFacetMap(AziRef._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AziRef', AziRef)

# Atomic simple type: {http://www.witsml.org/schemas/131}ArrayElementDataType
class ArrayElementDataType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """A list of binary representations for elements of 
			aggregates which may be Base64-encoded
			(e. g. elements of well log array traces, or
			multiplexed frames of similar-typed well log traces)
			as described in 
			"XML Schema Part 2: Datatypes", 3.2.16 base64binary
			[http://www.w3.org/TR/xmlschema-2/#base4Binary]]
			and in
			"Multipurpose Internet Mail Extensions (MIME) Part One:
			Format of Internet Message Bodies" (IETF RFC 2045)
			[ http://www.ietf.org/rfc/rfc2045.txt ]."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArrayElementDataType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 91, 1)
    _Documentation = 'A list of binary representations for elements of \n\t\t\taggregates which may be Base64-encoded\n\t\t\t(e. g. elements of well log array traces, or\n\t\t\tmultiplexed frames of similar-typed well log traces)\n\t\t\tas described in \n\t\t\t"XML Schema Part 2: Datatypes", 3.2.16 base64binary\n\t\t\t[http://www.w3.org/TR/xmlschema-2/#base4Binary]]\n\t\t\tand in\n\t\t\t"Multipurpose Internet Mail Extensions (MIME) Part One:\n\t\t\tFormat of Internet Message Bodies" (IETF RFC 2045)\n\t\t\t[ http://www.ietf.org/rfc/rfc2045.txt ].'
ArrayElementDataType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ArrayElementDataType, enum_prefix=None)
ArrayElementDataType.boolean = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value='boolean', tag='boolean')
ArrayElementDataType.integer_8_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value='integer 8 bit', tag='integer_8_bit')
ArrayElementDataType.integer_16_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value='integer 16 bit', tag='integer_16_bit')
ArrayElementDataType.integer_32_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value='integer 32 bit', tag='integer_32_bit')
ArrayElementDataType.integer_64_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value='integer 64 bit', tag='integer_64_bit')
ArrayElementDataType.IEEE_float_32_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value='IEEE float 32 bit', tag='IEEE_float_32_bit')
ArrayElementDataType.IEEE_float_64_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value='IEEE float 64 bit', tag='IEEE_float_64_bit')
ArrayElementDataType._InitializeFacetMap(ArrayElementDataType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ArrayElementDataType', ArrayElementDataType)

# Atomic simple type: {http://www.witsml.org/schemas/131}BearingType
class BearingType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BearingType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 116, 1)
    _Documentation = None
BearingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BearingType, enum_prefix=None)
BearingType.oil_seal = BearingType._CF_enumeration.addEnumeration(unicode_value='oil seal', tag='oil_seal')
BearingType.mud_lube = BearingType._CF_enumeration.addEnumeration(unicode_value='mud lube', tag='mud_lube')
BearingType.other = BearingType._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
BearingType.unknown = BearingType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BearingType._InitializeFacetMap(BearingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BearingType', BearingType)

# Atomic simple type: {http://www.witsml.org/schemas/131}BitDullCode
class BitDullCode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent a classification of a drill bit based 
			on its reason for being declared inoperable, as originally defined by the IADC."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BitDullCode')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 143, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}BitReasonPulled
class BitReasonPulled (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the reason for pulling a drill bit 
			from the wellbore, as originally defined by the IADC."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BitReasonPulled')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 289, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}BitType
class BitType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drill/core bit."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BitType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 395, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}BhaStatus
class BhaStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BhaStatus')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 440, 1)
    _Documentation = None
BhaStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BhaStatus, enum_prefix=None)
BhaStatus.final = BhaStatus._CF_enumeration.addEnumeration(unicode_value='final', tag='final')
BhaStatus.progress = BhaStatus._CF_enumeration.addEnumeration(unicode_value='progress', tag='progress')
BhaStatus.plan = BhaStatus._CF_enumeration.addEnumeration(unicode_value='plan', tag='plan')
BhaStatus.unknown = BhaStatus._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BhaStatus._InitializeFacetMap(BhaStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BhaStatus', BhaStatus)

# Atomic simple type: {http://www.witsml.org/schemas/131}BladeShapeType
class BladeShapeType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BladeShapeType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 467, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}BladeType
class BladeType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BladeType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 504, 1)
    _Documentation = None
BladeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BladeType, enum_prefix=None)
BladeType.clamp_on = BladeType._CF_enumeration.addEnumeration(unicode_value='clamp-on', tag='clamp_on')
BladeType.integral = BladeType._CF_enumeration.addEnumeration(unicode_value='integral', tag='integral')
BladeType.sleeve = BladeType._CF_enumeration.addEnumeration(unicode_value='sleeve', tag='sleeve')
BladeType.welded = BladeType._CF_enumeration.addEnumeration(unicode_value='welded', tag='welded')
BladeType.unknown = BladeType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BladeType._InitializeFacetMap(BladeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BladeType', BladeType)

# Atomic simple type: {http://www.witsml.org/schemas/131}BopType
class BopType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BopType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 536, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}BoxPinConfig
class BoxPinConfig (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of Box/Pin configuration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoxPinConfig')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 583, 1)
    _Documentation = 'These values represent the type of Box/Pin configuration.'
BoxPinConfig._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BoxPinConfig, enum_prefix=None)
BoxPinConfig.bottom_box_top_box = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value='bottom box, top box', tag='bottom_box_top_box')
BoxPinConfig.bottom_box_top_pin = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value='bottom box, top pin', tag='bottom_box_top_pin')
BoxPinConfig.bottom_pin_top_box = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value='bottom pin top box', tag='bottom_pin_top_box')
BoxPinConfig.bottom_pin = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value='bottom pin', tag='bottom_pin')
BoxPinConfig.unknown = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
BoxPinConfig._InitializeFacetMap(BoxPinConfig._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BoxPinConfig', BoxPinConfig)

# Atomic simple type: {http://www.witsml.org/schemas/131}CementJobType
class CementJobType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CementJobType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 618, 1)
    _Documentation = None
CementJobType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CementJobType, enum_prefix=None)
CementJobType.primary = CementJobType._CF_enumeration.addEnumeration(unicode_value='primary', tag='primary')
CementJobType.plug = CementJobType._CF_enumeration.addEnumeration(unicode_value='plug', tag='plug')
CementJobType.squeeze = CementJobType._CF_enumeration.addEnumeration(unicode_value='squeeze', tag='squeeze')
CementJobType.unknown = CementJobType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
CementJobType._InitializeFacetMap(CementJobType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CementJobType', CementJobType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ConnectionPosition
class ConnectionPosition (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the position of a connection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConnectionPosition')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 645, 1)
    _Documentation = 'These values represent the position of a connection.'
ConnectionPosition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ConnectionPosition, enum_prefix=None)
ConnectionPosition.both = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value='both', tag='both')
ConnectionPosition.bottom = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value='bottom', tag='bottom')
ConnectionPosition.top = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value='top', tag='top')
ConnectionPosition.unknown = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ConnectionPosition._InitializeFacetMap(ConnectionPosition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ConnectionPosition', ConnectionPosition)

# Atomic simple type: {http://www.witsml.org/schemas/131}DeflectionMethod
class DeflectionMethod (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent method used to direct the 
			deviation of the trajectory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeflectionMethod')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 675, 1)
    _Documentation = 'These values represent method used to direct the \n\t\t\tdeviation of the trajectory.'
DeflectionMethod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeflectionMethod, enum_prefix=None)
DeflectionMethod.point_bit = DeflectionMethod._CF_enumeration.addEnumeration(unicode_value='point bit', tag='point_bit')
DeflectionMethod.push_bit = DeflectionMethod._CF_enumeration.addEnumeration(unicode_value='push bit', tag='push_bit')
DeflectionMethod._InitializeFacetMap(DeflectionMethod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeflectionMethod', DeflectionMethod)

# Atomic simple type: {http://www.witsml.org/schemas/131}DerrickType
class DerrickType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drilling derrick."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DerrickType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 698, 1)
    _Documentation = 'These values represent the type of drilling derrick.'
DerrickType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DerrickType, enum_prefix=None)
DerrickType.double = DerrickType._CF_enumeration.addEnumeration(unicode_value='double', tag='double')
DerrickType.quadruple = DerrickType._CF_enumeration.addEnumeration(unicode_value='quadruple', tag='quadruple')
DerrickType.slant = DerrickType._CF_enumeration.addEnumeration(unicode_value='slant', tag='slant')
DerrickType.triple = DerrickType._CF_enumeration.addEnumeration(unicode_value='triple', tag='triple')
DerrickType.unknown = DerrickType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
DerrickType._InitializeFacetMap(DerrickType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DerrickType', DerrickType)

# Atomic simple type: {http://www.witsml.org/schemas/131}DrawWorksType
class DrawWorksType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DrawWorksType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 733, 1)
    _Documentation = None
DrawWorksType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DrawWorksType, enum_prefix=None)
DrawWorksType.mechanical = DrawWorksType._CF_enumeration.addEnumeration(unicode_value='mechanical', tag='mechanical')
DrawWorksType.standard_electric = DrawWorksType._CF_enumeration.addEnumeration(unicode_value='standard electric', tag='standard_electric')
DrawWorksType.diesel_electric = DrawWorksType._CF_enumeration.addEnumeration(unicode_value='diesel electric', tag='diesel_electric')
DrawWorksType.ram_rig = DrawWorksType._CF_enumeration.addEnumeration(unicode_value='ram rig', tag='ram_rig')
DrawWorksType.unknown = DrawWorksType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
DrawWorksType._InitializeFacetMap(DrawWorksType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DrawWorksType', DrawWorksType)

# Atomic simple type: {http://www.witsml.org/schemas/131}DriveType
class DriveType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of work string drive (rotary system)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DriveType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 765, 1)
    _Documentation = 'These values represent the type of work string drive (rotary system).'
DriveType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DriveType, enum_prefix=None)
DriveType.coiled_tubing = DriveType._CF_enumeration.addEnumeration(unicode_value='coiled tubing', tag='coiled_tubing')
DriveType.rotary_kelly_drive = DriveType._CF_enumeration.addEnumeration(unicode_value='rotary kelly drive', tag='rotary_kelly_drive')
DriveType.top_drive = DriveType._CF_enumeration.addEnumeration(unicode_value='top drive', tag='top_drive')
DriveType.unknown = DriveType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
DriveType._InitializeFacetMap(DriveType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DriveType', DriveType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ElevCodeEnum
class ElevCodeEnum (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The type of local or permanent reference datum for vertical gravity based 
			(i.e., elevation and vertical depth) and measured depth coordinates within the context of a well.
			This list includes local points (e.g., kelly bushing) used as a datum and 
			vertical reference datums (e.g., mean sea level)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElevCodeEnum')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 795, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}Ellipsoid
class Ellipsoid (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of ellipsoid (spheroid) 
			defining geographic or planar coordinates. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Ellipsoid')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 903, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}FiberMode
class FiberMode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The mode of a Distributed Temperature Survey (DTS) fiber."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FiberMode')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1309, 1)
    _Documentation = 'The mode of a Distributed Temperature Survey (DTS) fiber.'
FiberMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FiberMode, enum_prefix=None)
FiberMode.singlemode = FiberMode._CF_enumeration.addEnumeration(unicode_value='singlemode', tag='singlemode')
FiberMode.multimode = FiberMode._CF_enumeration.addEnumeration(unicode_value='multimode', tag='multimode')
FiberMode.other = FiberMode._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
FiberMode.unknown = FiberMode._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
FiberMode._InitializeFacetMap(FiberMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FiberMode', FiberMode)

# Atomic simple type: {http://www.witsml.org/schemas/131}GasPeakType
class GasPeakType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GasPeakType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1342, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}GeodeticDatum
class GeodeticDatum (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of geodetic datum. 
			The source (except for "none", "unknown" and "UserDefined") of the values 
			and the descriptions is Geoshare V13."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeodeticDatum')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1399, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}Hemispheres
class Hemispheres (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Hemispheres')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1616, 1)
    _Documentation = None
Hemispheres._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Hemispheres, enum_prefix=None)
Hemispheres.northern = Hemispheres._CF_enumeration.addEnumeration(unicode_value='northern', tag='northern')
Hemispheres.southern = Hemispheres._CF_enumeration.addEnumeration(unicode_value='southern', tag='southern')
Hemispheres.unknown = Hemispheres._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
Hemispheres._InitializeFacetMap(Hemispheres._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Hemispheres', Hemispheres)

# Atomic simple type: {http://www.witsml.org/schemas/131}HoleCasingType
class HoleCasingType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HoleCasingType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1638, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}HoleOpenerType
class HoleOpenerType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HoleOpenerType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1690, 1)
    _Documentation = None
HoleOpenerType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HoleOpenerType, enum_prefix=None)
HoleOpenerType.under_reamer = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value='under-reamer', tag='under_reamer')
HoleOpenerType.fixed_blade = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value='fixed blade', tag='fixed_blade')
HoleOpenerType.unknown = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
HoleOpenerType._InitializeFacetMap(HoleOpenerType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HoleOpenerType', HoleOpenerType)

# Atomic simple type: {http://www.witsml.org/schemas/131}IntervalMethod
class IntervalMethod (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IntervalMethod')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1712, 1)
    _Documentation = None
IntervalMethod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IntervalMethod, enum_prefix=None)
IntervalMethod.average = IntervalMethod._CF_enumeration.addEnumeration(unicode_value='average', tag='average')
IntervalMethod.maximum = IntervalMethod._CF_enumeration.addEnumeration(unicode_value='maximum', tag='maximum')
IntervalMethod.minimum = IntervalMethod._CF_enumeration.addEnumeration(unicode_value='minimum', tag='minimum')
IntervalMethod.other = IntervalMethod._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
IntervalMethod.spot_sample = IntervalMethod._CF_enumeration.addEnumeration(unicode_value='spot sample', tag='spot_sample')
IntervalMethod.unknown = IntervalMethod._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
IntervalMethod._InitializeFacetMap(IntervalMethod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IntervalMethod', IntervalMethod)

# Atomic simple type: {http://www.witsml.org/schemas/131}IntervalType
class IntervalType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IntervalType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1749, 1)
    _Documentation = None
IntervalType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IntervalType, enum_prefix=None)
IntervalType.time = IntervalType._CF_enumeration.addEnumeration(unicode_value='time', tag='time')
IntervalType.depth = IntervalType._CF_enumeration.addEnumeration(unicode_value='depth', tag='depth')
IntervalType.unknown = IntervalType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
IntervalType._InitializeFacetMap(IntervalType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IntervalType', IntervalType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ItemState
class ItemState (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the state of a WITSML object. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ItemState')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1771, 1)
    _Documentation = 'These values represent the state of a WITSML object. '
ItemState._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ItemState, enum_prefix=None)
ItemState.actual = ItemState._CF_enumeration.addEnumeration(unicode_value='actual', tag='actual')
ItemState.model = ItemState._CF_enumeration.addEnumeration(unicode_value='model', tag='model')
ItemState.plan = ItemState._CF_enumeration.addEnumeration(unicode_value='plan', tag='plan')
ItemState.unknown = ItemState._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ItemState._InitializeFacetMap(ItemState._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ItemState', ItemState)

# Atomic simple type: {http://www.witsml.org/schemas/131}InstalledFiberPoint
class InstalledFiberPoint (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The type of Distributed Temperature Survey (DTS) fiber point."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstalledFiberPoint')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1801, 1)
    _Documentation = 'The type of Distributed Temperature Survey (DTS) fiber point.'
InstalledFiberPoint._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InstalledFiberPoint, enum_prefix=None)
InstalledFiberPoint.splice = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='splice', tag='splice')
InstalledFiberPoint.connector = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='connector', tag='connector')
InstalledFiberPoint.end_of_fiber = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='end of fiber', tag='end_of_fiber')
InstalledFiberPoint.base_of_fiber = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='base of fiber', tag='base_of_fiber')
InstalledFiberPoint.turn_around_point = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='turn around point', tag='turn_around_point')
InstalledFiberPoint.start_of_fiber = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='start of fiber', tag='start_of_fiber')
InstalledFiberPoint.oven_entry_point = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='oven entry point', tag='oven_entry_point')
InstalledFiberPoint.oven_exit_point = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='oven exit point', tag='oven_exit_point')
InstalledFiberPoint.downhole_gauge = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='downhole gauge', tag='downhole_gauge')
InstalledFiberPoint.DTS_laser_head = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='DTS laser head', tag='DTS_laser_head')
InstalledFiberPoint.DTS_reference_oven = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='DTS reference oven', tag='DTS_reference_oven')
InstalledFiberPoint.splice_box = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='splice box', tag='splice_box')
InstalledFiberPoint.wellhead_junction_box = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='wellhead junction box', tag='wellhead_junction_box')
InstalledFiberPoint.base_tubing_hanger_flange = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='base tubing hanger flange', tag='base_tubing_hanger_flange')
InstalledFiberPoint.PBR_wet_connect = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='PBR wet connect', tag='PBR_wet_connect')
InstalledFiberPoint.top_ESP_pump = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='top ESP pump', tag='top_ESP_pump')
InstalledFiberPoint.base_ESP_pump = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='base ESP pump', tag='base_ESP_pump')
InstalledFiberPoint.wellhead_temperature_gauge = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='wellhead temperature gauge', tag='wellhead_temperature_gauge')
InstalledFiberPoint.top_completion_zone = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='top completion zone', tag='top_completion_zone')
InstalledFiberPoint.base_completion_zone = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='base completion zone', tag='base_completion_zone')
InstalledFiberPoint.unknown = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
InstalledFiberPoint._InitializeFacetMap(InstalledFiberPoint._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InstalledFiberPoint', InstalledFiberPoint)

# Atomic simple type: {http://www.witsml.org/schemas/131}JarType
class JarType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JarType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1939, 1)
    _Documentation = None
JarType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=JarType, enum_prefix=None)
JarType.mechanical = JarType._CF_enumeration.addEnumeration(unicode_value='mechanical', tag='mechanical')
JarType.hydraulic = JarType._CF_enumeration.addEnumeration(unicode_value='hydraulic', tag='hydraulic')
JarType.hydro_mechanical = JarType._CF_enumeration.addEnumeration(unicode_value='hydro mechanical', tag='hydro_mechanical')
JarType.unknown = JarType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
JarType._InitializeFacetMap(JarType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'JarType', JarType)

# Atomic simple type: {http://www.witsml.org/schemas/131}JarAction
class JarAction (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JarAction')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1966, 1)
    _Documentation = None
JarAction._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=JarAction, enum_prefix=None)
JarAction.up = JarAction._CF_enumeration.addEnumeration(unicode_value='up', tag='up')
JarAction.down = JarAction._CF_enumeration.addEnumeration(unicode_value='down', tag='down')
JarAction.both = JarAction._CF_enumeration.addEnumeration(unicode_value='both', tag='both')
JarAction.vibrating = JarAction._CF_enumeration.addEnumeration(unicode_value='vibrating', tag='vibrating')
JarAction.unknown = JarAction._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
JarAction._InitializeFacetMap(JarAction._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'JarAction', JarAction)

# Atomic simple type: {http://www.witsml.org/schemas/131}LithologySource
class LithologySource (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Specifies the source of lithology information."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LithologySource')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1998, 1)
    _Documentation = 'Specifies the source of lithology information.'
LithologySource._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LithologySource, enum_prefix=None)
LithologySource.interpreted = LithologySource._CF_enumeration.addEnumeration(unicode_value='interpreted', tag='interpreted')
LithologySource.core = LithologySource._CF_enumeration.addEnumeration(unicode_value='core', tag='core')
LithologySource.cuttings = LithologySource._CF_enumeration.addEnumeration(unicode_value='cuttings', tag='cuttings')
LithologySource.unknown = LithologySource._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
LithologySource._InitializeFacetMap(LithologySource._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LithologySource', LithologySource)

# Atomic simple type: {http://www.witsml.org/schemas/131}LithologyType
class LithologyType (abstractTypeEnum):

    """The type of lithology.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LithologyType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2031, 1)
    _Documentation = 'The type of lithology.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
LithologyType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'LithologyType', LithologyType)

# Atomic simple type: {http://www.witsml.org/schemas/131}LogDataType
class LogDataType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The endcoding allowed in a realtime channel value or log curve value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogDataType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2040, 1)
    _Documentation = 'The endcoding allowed in a realtime channel value or log curve value.'
LogDataType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogDataType, enum_prefix=None)
LogDataType.date_time = LogDataType._CF_enumeration.addEnumeration(unicode_value='date time', tag='date_time')
LogDataType.double = LogDataType._CF_enumeration.addEnumeration(unicode_value='double', tag='double')
LogDataType.long = LogDataType._CF_enumeration.addEnumeration(unicode_value='long', tag='long')
LogDataType.string = LogDataType._CF_enumeration.addEnumeration(unicode_value='string', tag='string')
LogDataType.unknown = LogDataType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
LogDataType._InitializeFacetMap(LogDataType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogDataType', LogDataType)

# Atomic simple type: {http://www.witsml.org/schemas/131}LogIndexDirection
class LogIndexDirection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the direction of movement within a wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogIndexDirection')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2075, 1)
    _Documentation = 'These values represent the direction of movement within a wellbore.'
LogIndexDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogIndexDirection, enum_prefix=None)
LogIndexDirection.decreasing = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value='decreasing', tag='decreasing')
LogIndexDirection.increasing = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value='increasing', tag='increasing')
LogIndexDirection.unknown = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
LogIndexDirection._InitializeFacetMap(LogIndexDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogIndexDirection', LogIndexDirection)

# Atomic simple type: {http://www.witsml.org/schemas/131}LogIndexType
class LogIndexType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of data used as an index value for a log. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogIndexType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2102, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}LogTraceOrigin
class LogTraceOrigin (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogTraceOrigin')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2147, 1)
    _Documentation = None
LogTraceOrigin._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogTraceOrigin, enum_prefix=None)
LogTraceOrigin.realtime = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value='realtime', tag='realtime')
LogTraceOrigin.modeled = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value='modeled', tag='modeled')
LogTraceOrigin.unknown = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
LogTraceOrigin._InitializeFacetMap(LogTraceOrigin._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogTraceOrigin', LogTraceOrigin)

# Atomic simple type: {http://www.witsml.org/schemas/131}LogTraceState
class LogTraceState (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogTraceState')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2169, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}MaterialType
class MaterialType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2206, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}MeasurementType
class MeasurementType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The source (except for "CH density porosity", "CH neutron porosity", "OH density porosity"
			and "OH neutron porosity") of the values and the descriptions is the POSC V2.2 "well log trace class" 
			standard instance values which are documented as "A classification of well log traces based on 
			specification of a range of characteristics. Traces may be classed according to the type of physical 
			characteristic they are meant to measure." """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasurementType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2268, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}MessageProbability
class MessageProbability (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageProbability')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 3757, 1)
    _Documentation = None
MessageProbability._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageProbability, enum_prefix=None)
MessageProbability.low = MessageProbability._CF_enumeration.addEnumeration(unicode_value='low', tag='low')
MessageProbability.medium = MessageProbability._CF_enumeration.addEnumeration(unicode_value='medium', tag='medium')
MessageProbability.high = MessageProbability._CF_enumeration.addEnumeration(unicode_value='high', tag='high')
MessageProbability.unknown = MessageProbability._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
MessageProbability._InitializeFacetMap(MessageProbability._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageProbability', MessageProbability)

# Atomic simple type: {http://www.witsml.org/schemas/131}MessageSeverity
class MessageSeverity (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageSeverity')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 3784, 1)
    _Documentation = None
MessageSeverity._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageSeverity, enum_prefix=None)
MessageSeverity.catastrophic = MessageSeverity._CF_enumeration.addEnumeration(unicode_value='catastrophic', tag='catastrophic')
MessageSeverity.major = MessageSeverity._CF_enumeration.addEnumeration(unicode_value='major', tag='major')
MessageSeverity.minor = MessageSeverity._CF_enumeration.addEnumeration(unicode_value='minor', tag='minor')
MessageSeverity.unknown = MessageSeverity._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
MessageSeverity._InitializeFacetMap(MessageSeverity._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageSeverity', MessageSeverity)

# Atomic simple type: {http://www.witsml.org/schemas/131}MessageType
class MessageType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a message. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 3811, 1)
    _Documentation = 'These values represent the type of a message. '
MessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageType, enum_prefix=None)
MessageType.alarm = MessageType._CF_enumeration.addEnumeration(unicode_value='alarm', tag='alarm')
MessageType.event = MessageType._CF_enumeration.addEnumeration(unicode_value='event', tag='event')
MessageType.informational = MessageType._CF_enumeration.addEnumeration(unicode_value='informational', tag='informational')
MessageType.warning = MessageType._CF_enumeration.addEnumeration(unicode_value='warning', tag='warning')
MessageType.unknown = MessageType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
MessageType._InitializeFacetMap(MessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageType', MessageType)

# Atomic simple type: {http://www.witsml.org/schemas/131}MudLogParameterType
class MudLogParameterType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """ "Text value" indicates that a text value is expected. 
			"Pressure value" indicates that an equivalentMudWeight value is expected.
			"Pressure gradient value" indicates that an equivalentMudWeight value is 
			  commonly expected but a pressureGradient value may also be specified.
			"Concentration value" indicates that a concentration value is expected.
			"Force value" indicates that a force value is expected.
			"Only" indicates that no other value is expected."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MudLogParameterType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 3846, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}NADTypes
class NADTypes (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NADTypes')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4108, 1)
    _Documentation = None
NADTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NADTypes, enum_prefix=None)
NADTypes.NAD27 = NADTypes._CF_enumeration.addEnumeration(unicode_value='NAD27', tag='NAD27')
NADTypes.NAD83 = NADTypes._CF_enumeration.addEnumeration(unicode_value='NAD83', tag='NAD83')
NADTypes.unknown = NADTypes._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
NADTypes._InitializeFacetMap(NADTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NADTypes', NADTypes)

# Atomic simple type: {http://www.witsml.org/schemas/131}NameTagLocation
class NameTagLocation (abstractTypeEnum):

    """Defines the locations where an equipment tag might be found..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameTagLocation')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4130, 1)
    _Documentation = 'Defines the locations where an equipment tag might be found..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagLocation._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'NameTagLocation', NameTagLocation)

# Atomic simple type: {http://www.witsml.org/schemas/131}NameTagNumberingScheme
class NameTagNumberingScheme (abstractTypeEnum):

    """Defines the specifications for creating equipment tags..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameTagNumberingScheme')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4139, 1)
    _Documentation = 'Defines the specifications for creating equipment tags..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagNumberingScheme._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'NameTagNumberingScheme', NameTagNumberingScheme)

# Atomic simple type: {http://www.witsml.org/schemas/131}NameTagTechnology
class NameTagTechnology (abstractTypeEnum):

    """Defines the mechanisms for attaching an equipment tag to an item..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameTagTechnology')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4148, 1)
    _Documentation = 'Defines the mechanisms for attaching an equipment tag to an item..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagTechnology._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'NameTagTechnology', NameTagTechnology)

# Atomic simple type: {http://www.witsml.org/schemas/131}NozzleType
class NozzleType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NozzleType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4157, 1)
    _Documentation = None
NozzleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NozzleType, enum_prefix=None)
NozzleType.extended = NozzleType._CF_enumeration.addEnumeration(unicode_value='extended', tag='extended')
NozzleType.normal = NozzleType._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
NozzleType.unknown = NozzleType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
NozzleType._InitializeFacetMap(NozzleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NozzleType', NozzleType)

# Atomic simple type: {http://www.witsml.org/schemas/131}OTDRReason
class OTDRReason (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The reason an Optical Time Domain Reflectometry (OTDR) 
			test was run within a  Distributed Temperature Survey (DTS)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OTDRReason')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4179, 1)
    _Documentation = 'The reason an Optical Time Domain Reflectometry (OTDR) \n\t\t\ttest was run within a  Distributed Temperature Survey (DTS).'
OTDRReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OTDRReason, enum_prefix=None)
OTDRReason.pre_installation = OTDRReason._CF_enumeration.addEnumeration(unicode_value='pre-installation', tag='pre_installation')
OTDRReason.post_installation = OTDRReason._CF_enumeration.addEnumeration(unicode_value='post-installation', tag='post_installation')
OTDRReason.DTS_run = OTDRReason._CF_enumeration.addEnumeration(unicode_value='DTS run', tag='DTS_run')
OTDRReason.other = OTDRReason._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
OTDRReason.unknown = OTDRReason._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
OTDRReason._InitializeFacetMap(OTDRReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OTDRReason', OTDRReason)

# Atomic simple type: {http://www.witsml.org/schemas/131}PitType
class PitType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PitType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4217, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}Projection
class Projection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of coordinate system projection method.
			The source (except for "UserDefined") of the values is Geoshare V13. 
			For a detailed description of each value, see the Geoshare documentation of the 
			indicated "217" object at http://w3.posc.org/GeoshareSIG/technical/GDM/v13.0/."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Projection')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4283, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}ProjectionVariantsObliqueMercator
class ProjectionVariantsObliqueMercator (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProjectionVariantsObliqueMercator')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4411, 1)
    _Documentation = None
ProjectionVariantsObliqueMercator._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProjectionVariantsObliqueMercator, enum_prefix=None)
ProjectionVariantsObliqueMercator.default = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value='default', tag='default')
ProjectionVariantsObliqueMercator.rectified = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value='rectified', tag='rectified')
ProjectionVariantsObliqueMercator.rectified_skew = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value='rectified skew', tag='rectified_skew')
ProjectionVariantsObliqueMercator.rectified_skew_center_origin = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value='rectified skew center origin', tag='rectified_skew_center_origin')
ProjectionVariantsObliqueMercator.unknown = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ProjectionVariantsObliqueMercator._InitializeFacetMap(ProjectionVariantsObliqueMercator._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProjectionVariantsObliqueMercator', ProjectionVariantsObliqueMercator)

# Atomic simple type: {http://www.witsml.org/schemas/131}PumpType
class PumpType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a pump. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PumpType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4443, 1)
    _Documentation = 'These values represent the type of a pump. '
PumpType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PumpType, enum_prefix=None)
PumpType.centrifugal = PumpType._CF_enumeration.addEnumeration(unicode_value='centrifugal', tag='centrifugal')
PumpType.duplex = PumpType._CF_enumeration.addEnumeration(unicode_value='duplex', tag='duplex')
PumpType.triplex = PumpType._CF_enumeration.addEnumeration(unicode_value='triplex', tag='triplex')
PumpType.unknown = PumpType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
PumpType._InitializeFacetMap(PumpType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PumpType', PumpType)

# Atomic simple type: {http://www.witsml.org/schemas/131}PumpOpType
class PumpOpType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PumpOpType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4473, 1)
    _Documentation = None
PumpOpType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PumpOpType, enum_prefix=None)
PumpOpType.drilling = PumpOpType._CF_enumeration.addEnumeration(unicode_value='drilling', tag='drilling')
PumpOpType.reaming = PumpOpType._CF_enumeration.addEnumeration(unicode_value='reaming', tag='reaming')
PumpOpType.circulating = PumpOpType._CF_enumeration.addEnumeration(unicode_value='circulating', tag='circulating')
PumpOpType.slow_pump = PumpOpType._CF_enumeration.addEnumeration(unicode_value='slow pump', tag='slow_pump')
PumpOpType.unknown = PumpOpType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
PumpOpType._InitializeFacetMap(PumpOpType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PumpOpType', PumpOpType)

# Atomic simple type: {http://www.witsml.org/schemas/131}QualifierType
class QualifierType (abstractTypeEnum):

    """The type of qualifier of a lithology.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QualifierType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4505, 1)
    _Documentation = 'The type of qualifier of a lithology.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
QualifierType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'QualifierType', QualifierType)

# Atomic simple type: {http://www.witsml.org/schemas/131}RealtimeData
class RealtimeData (abstractTypeEnum):

    """These values represent the name of a recording channel.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RealtimeData')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4514, 1)
    _Documentation = 'These values represent the name of a recording channel.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
RealtimeData._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'RealtimeData', RealtimeData)

# Atomic simple type: {http://www.witsml.org/schemas/131}RigType
class RigType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drilling rig. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RigType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4523, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}RiskAffectedPersonnel
class RiskAffectedPersonnel (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Personnel affected by a risk."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RiskAffectedPersonnel')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4573, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}RiskCategory
class RiskCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of slow circulation rate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RiskCategory')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4716, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}RiskSubCategory
class RiskSubCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Risk Sub-Categories."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RiskSubCategory')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4786, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}RiskType
class RiskType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Types of risk."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RiskType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5349, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}ScrType
class ScrType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of slow circulation rate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ScrType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5394, 1)
    _Documentation = 'Type of slow circulation rate.'
ScrType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ScrType, enum_prefix=None)
ScrType.string_annulus = ScrType._CF_enumeration.addEnumeration(unicode_value='string annulus', tag='string_annulus')
ScrType.string_kill_line = ScrType._CF_enumeration.addEnumeration(unicode_value='string kill line', tag='string_kill_line')
ScrType.string_choke_line = ScrType._CF_enumeration.addEnumeration(unicode_value='string choke line', tag='string_choke_line')
ScrType.unknown = ScrType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ScrType._InitializeFacetMap(ScrType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ScrType', ScrType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ShowFluorescence
class ShowFluorescence (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShowFluorescence')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5424, 1)
    _Documentation = None
ShowFluorescence._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowFluorescence, enum_prefix=None)
ShowFluorescence.faint = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value='faint', tag='faint')
ShowFluorescence.bright = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value='bright', tag='bright')
ShowFluorescence.none = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
ShowFluorescence.unknown = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ShowFluorescence._InitializeFacetMap(ShowFluorescence._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ShowFluorescence', ShowFluorescence)

# Atomic simple type: {http://www.witsml.org/schemas/131}ShowLevel
class ShowLevel (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShowLevel')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5451, 1)
    _Documentation = None
ShowLevel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowLevel, enum_prefix=None)
ShowLevel.blooming = ShowLevel._CF_enumeration.addEnumeration(unicode_value='blooming', tag='blooming')
ShowLevel.streaming = ShowLevel._CF_enumeration.addEnumeration(unicode_value='streaming', tag='streaming')
ShowLevel.unknown = ShowLevel._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ShowLevel._InitializeFacetMap(ShowLevel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ShowLevel', ShowLevel)

# Atomic simple type: {http://www.witsml.org/schemas/131}ShowRating
class ShowRating (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShowRating')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5473, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}ShowSpeed
class ShowSpeed (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShowSpeed')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5515, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}SupportCraft
class SupportCraft (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportCraft')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5552, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}SurfEquipType
class SurfEquipType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SurfEquipType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5600, 1)
    _Documentation = None
SurfEquipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SurfEquipType, enum_prefix=None)
SurfEquipType.IADC = SurfEquipType._CF_enumeration.addEnumeration(unicode_value='IADC', tag='IADC')
SurfEquipType.custom = SurfEquipType._CF_enumeration.addEnumeration(unicode_value='custom', tag='custom')
SurfEquipType.coiled_tubing = SurfEquipType._CF_enumeration.addEnumeration(unicode_value='coiled tubing', tag='coiled_tubing')
SurfEquipType.unknown = SurfEquipType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
SurfEquipType._InitializeFacetMap(SurfEquipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SurfEquipType', SurfEquipType)

# Atomic simple type: {http://www.witsml.org/schemas/131}TargetCategory
class TargetCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TargetCategory')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5627, 1)
    _Documentation = None
TargetCategory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetCategory, enum_prefix=None)
TargetCategory.geological = TargetCategory._CF_enumeration.addEnumeration(unicode_value='geological', tag='geological')
TargetCategory.unknown = TargetCategory._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TargetCategory._InitializeFacetMap(TargetCategory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TargetCategory', TargetCategory)

# Atomic simple type: {http://www.witsml.org/schemas/131}TargetScope
class TargetScope (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of scope of the drilling target. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TargetScope')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5644, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}TargetSectionScope
class TargetSectionScope (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of scope of a section that describes a target. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TargetSectionScope')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5710, 1)
    _Documentation = 'These values represent the type of scope of a section that describes a target. '
TargetSectionScope._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetSectionScope, enum_prefix=None)
TargetSectionScope.arc = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value='arc', tag='arc')
TargetSectionScope.line = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value='line', tag='line')
TargetSectionScope.unknown = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TargetSectionScope._InitializeFacetMap(TargetSectionScope._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TargetSectionScope', TargetSectionScope)

# Atomic simple type: {http://www.witsml.org/schemas/131}TrajStationStatus
class TrajStationStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrajStationStatus')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5736, 1)
    _Documentation = None
TrajStationStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TrajStationStatus, enum_prefix=None)
TrajStationStatus.locked = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value='locked', tag='locked')
TrajStationStatus.open = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value='open', tag='open')
TrajStationStatus.rejected = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value='rejected', tag='rejected')
TrajStationStatus.valid = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value='valid', tag='valid')
TrajStationStatus.position = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value='position', tag='position')
TrajStationStatus.unknown = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TrajStationStatus._InitializeFacetMap(TrajStationStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TrajStationStatus', TrajStationStatus)

# Atomic simple type: {http://www.witsml.org/schemas/131}TrajStationType
class TrajStationType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a directional survey station. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrajStationType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5773, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}TubularAssembly
class TubularAssembly (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TubularAssembly')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 6033, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}TubularComponent
class TubularComponent (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TubularComponent')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 6110, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}TypeSurveyTool
class TypeSurveyTool (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of direcional survey tool; very generic classification"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TypeSurveyTool')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 6937, 1)
    _Documentation = 'Type of direcional survey tool; very generic classification'
TypeSurveyTool._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TypeSurveyTool, enum_prefix=None)
TypeSurveyTool.magnetic_MWD = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value='magnetic MWD', tag='magnetic_MWD')
TypeSurveyTool.gyroscopic__MWD = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value='gyroscopic  MWD', tag='gyroscopic__MWD')
TypeSurveyTool.gyroscopic_north_seeking = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value='gyroscopic north seeking', tag='gyroscopic_north_seeking')
TypeSurveyTool.gyroscopic_inertial = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value='gyroscopic inertial', tag='gyroscopic_inertial')
TypeSurveyTool.magnetic_single_shot = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value='magnetic single-shot', tag='magnetic_single_shot')
TypeSurveyTool.magnetic_multiple_shot = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value='magnetic multiple-shot', tag='magnetic_multiple_shot')
TypeSurveyTool.unknown = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
TypeSurveyTool._InitializeFacetMap(TypeSurveyTool._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TypeSurveyTool', TypeSurveyTool)

# Atomic simple type: {http://www.witsml.org/schemas/131}WellDirection
class WellDirection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The direction of flow of the fluids in a well facility
			(generally, injected or produced, or some combination)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellDirection')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 6982, 1)
    _Documentation = 'The direction of flow of the fluids in a well facility\n\t\t\t(generally, injected or produced, or some combination).'
WellDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellDirection, enum_prefix=None)
WellDirection.huff_n_puff = WellDirection._CF_enumeration.addEnumeration(unicode_value='huff-n-puff', tag='huff_n_puff')
WellDirection.injector = WellDirection._CF_enumeration.addEnumeration(unicode_value='injector', tag='injector')
WellDirection.producer = WellDirection._CF_enumeration.addEnumeration(unicode_value='producer', tag='producer')
WellDirection.uncertain = WellDirection._CF_enumeration.addEnumeration(unicode_value='uncertain', tag='uncertain')
WellDirection.unknown = WellDirection._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
WellDirection._InitializeFacetMap(WellDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellDirection', WellDirection)

# Atomic simple type: {http://www.witsml.org/schemas/131}WellFluid
class WellFluid (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The type of fluid being produced from or injected 
			into a well facility."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellFluid')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 7023, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}WellboreShape
class WellboreShape (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the classification of a wellbore 
			based on its shape. The source of the values and the descriptions is the 
			POSC V2.2 "facility class" standard instance values in classification system 
			"POSC wellbore trajectory shape". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellboreShape')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 7140, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}WellboreType
class WellboreType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The classification of a wellbore with respect to its parent 
			well/wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellboreType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 7196, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}WellPurpose
class WellPurpose (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the classification of a well or 
			wellbore by the purpose for which it was initially drilled."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellPurpose')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 7252, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}WellStatus
class WellStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the status of a well or wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellStatus')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 7388, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/131}PercentUom
class PercentUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 139, 1)
    _Documentation = None
PercentUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PercentUom, enum_prefix=None)
PercentUom.emptyString = PercentUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
PercentUom._InitializeFacetMap(PercentUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PercentUom', PercentUom)

# List simple type: {http://www.witsml.org/schemas/131}listOfString
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfString (pyxb.binding.basis.STD_list):

    """A representation of a list of xsd:string values,
			restricted to strings without embedded whitespace."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'listOfString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 216, 1)
    _Documentation = 'A representation of a list of xsd:string values,\n\t\t\trestricted to strings without embedded whitespace.'

    _ItemType = str32
listOfString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'listOfString', listOfString)

# Atomic simple type: {http://www.witsml.org/schemas/131}refWellDatum
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
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 295, 1)
    _Documentation = "A reference to a wellDatum in the current well. \n\t\t\tThis value must match the uid value in a WellDatum. \n\t\t\tThis value represents a foreign key from one element to another.\n\t\t\tThis is an exception to the convention that a foreign key must utilize both \n\t\t\ta human contextual name and a uid value. For messages outside the context of\n\t\t\ta server then this value will commonly match the value of the name of the \n\t\t\twellDatum (e.g., 'KB') if uids are not not used in that context.\n\t\t\tThis was a compromise in order to allow the coordinate structures to be simple\n\t\t\tand still be usable both within the context of a server and outside the context of a server."
refWellDatum._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'refWellDatum', refWellDatum)

# Atomic simple type: {http://www.witsml.org/schemas/131}nameString
class nameString (abstractNameString):

    """A user assigned human recognizable contextual name of something. 
			There should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.
			This type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 312, 1)
    _Documentation = 'A user assigned human recognizable contextual name of something. \n\t\t\tThere should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.\n\t\t\tThis type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration.'
nameString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'nameString', nameString)

# Atomic simple type: {http://www.witsml.org/schemas/131}kindString
class kindString (abstractTypeEnum):

    """A community assigned human recognizable name. 
			This type of value is intended to be unique and is generally a candidate to be constrained to an enumerated list."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'kindString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 375, 1)
    _Documentation = 'A community assigned human recognizable name. \n\t\t\tThis type of value is intended to be unique and is generally a candidate to be constrained to an enumerated list.'
kindString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'kindString', kindString)

# Atomic simple type: {http://www.witsml.org/schemas/131}uomString
class uomString (abstractUomEnum):

    """A unit of measure acronym from the POSC unit of measure file."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uomString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 384, 1)
    _Documentation = 'A unit of measure acronym from the POSC unit of measure file.'
uomString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'uomString', uomString)

# Atomic simple type: {http://www.witsml.org/schemas/131}uidString
class uidString (abstractUidString):

    """A locally unique identifier. 
			The value is not intended to convey any semantic content (e.g., it may be computer generated). 
			The value is only required to be unique within a context in a document (e.g., defined via key and keyref). 
			There is no guarantee that the same data in multiple documents will utilize the same uid value 
			unless enforced by the source of the document (e.g., a document server)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uidString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 391, 1)
    _Documentation = 'A locally unique identifier. \n\t\t\tThe value is not intended to convey any semantic content (e.g., it may be computer generated). \n\t\t\tThe value is only required to be unique within a context in a document (e.g., defined via key and keyref). \n\t\t\tThere is no guarantee that the same data in multiple documents will utilize the same uid value \n\t\t\tunless enforced by the source of the document (e.g., a document server).'
uidString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'uidString', uidString)

# Atomic simple type: {http://www.witsml.org/schemas/131}refString
class refString (abstractUidString):

    """A reference to the unique identifier of another element. 
			This value represents a foreign key from one element to another.
			The value should match the value of an attribute of type uidString."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 402, 1)
    _Documentation = 'A reference to the unique identifier of another element. \n\t\t\tThis value represents a foreign key from one element to another.\n\t\t\tThe value should match the value of an attribute of type uidString.'
refString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'refString', refString)

# Atomic simple type: {http://www.witsml.org/schemas/131}MeasuredDepthUom
class MeasuredDepthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """The units of measure that are valid for measured depths in a wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeasuredDepthUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 518, 1)
    _Documentation = 'The units of measure that are valid for measured depths in a wellbore.'
MeasuredDepthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MeasuredDepthUom, enum_prefix=None)
MeasuredDepthUom.m = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value='m', tag='m')
MeasuredDepthUom.ft = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value='ft', tag='ft')
MeasuredDepthUom.ftUS = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value='ftUS', tag='ftUS')
MeasuredDepthUom._InitializeFacetMap(MeasuredDepthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MeasuredDepthUom', MeasuredDepthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}WellVerticalCoordinateUom
class WellVerticalCoordinateUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """The units of measure that are valid for vertical gravity based 
			coordinates (i.e., elevation or vertical depth) within the context of a well."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WellVerticalCoordinateUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 593, 1)
    _Documentation = 'The units of measure that are valid for vertical gravity based \n\t\t\tcoordinates (i.e., elevation or vertical depth) within the context of a well.'
WellVerticalCoordinateUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellVerticalCoordinateUom, enum_prefix=None)
WellVerticalCoordinateUom.m = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value='m', tag='m')
WellVerticalCoordinateUom.ft = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value='ft', tag='ft')
WellVerticalCoordinateUom.ftUS = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value='ftUS', tag='ftUS')
WellVerticalCoordinateUom.ftBr65 = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value='ftBr(65)', tag='ftBr65')
WellVerticalCoordinateUom._InitializeFacetMap(WellVerticalCoordinateUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WellVerticalCoordinateUom', WellVerticalCoordinateUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}positiveCount
class positiveCount (abstractPositiveCount):

    """A positive integer (one based count or index)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positiveCount')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 638, 1)
    _Documentation = 'A positive integer (one based count or index).'
positiveCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveCount, value=pyxb.binding.datatypes.short(1))
positiveCount._InitializeFacetMap(positiveCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'positiveCount', positiveCount)

# Atomic simple type: {http://www.witsml.org/schemas/131}accelerationLinearUom
class accelerationLinearUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accelerationLinearUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 25, 1)
    _Documentation = None
accelerationLinearUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=accelerationLinearUom, enum_prefix=None)
accelerationLinearUom.ms2 = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='m/s2', tag='ms2')
accelerationLinearUom.cms2 = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='cm/s2', tag='cms2')
accelerationLinearUom.fts2 = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='ft/s2', tag='fts2')
accelerationLinearUom.Gal = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='Gal', tag='Gal')
accelerationLinearUom.mgn = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='mgn', tag='mgn')
accelerationLinearUom.gn = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='gn', tag='gn')
accelerationLinearUom.mGal = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value='mGal', tag='mGal')
accelerationLinearUom._InitializeFacetMap(accelerationLinearUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'accelerationLinearUom', accelerationLinearUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}anglePerLengthUom
class anglePerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'anglePerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 37, 1)
    _Documentation = None
anglePerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=anglePerLengthUom, enum_prefix=None)
anglePerLengthUom.radm = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='rad/m', tag='radm')
anglePerLengthUom.dega30ft = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dega/30ft', tag='dega30ft')
anglePerLengthUom.degaft = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dega/ft', tag='degaft')
anglePerLengthUom.dega100ft = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dega/100ft', tag='dega100ft')
anglePerLengthUom.degam = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dega/m', tag='degam')
anglePerLengthUom.dega30m = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dega/30m', tag='dega30m')
anglePerLengthUom.radft = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value='rad/ft', tag='radft')
anglePerLengthUom._InitializeFacetMap(anglePerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'anglePerLengthUom', anglePerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}anglePerTimeUom
class anglePerTimeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'anglePerTimeUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 49, 1)
    _Documentation = None
anglePerTimeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=anglePerTimeUom, enum_prefix=None)
anglePerTimeUom.rads = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='rad/s', tag='rads')
anglePerTimeUom.cs = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='c/s', tag='cs')
anglePerTimeUom.degah = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='dega/h', tag='degah')
anglePerTimeUom.degamin = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='dega/min', tag='degamin')
anglePerTimeUom.degas = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='dega/s', tag='degas')
anglePerTimeUom.revs = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='rev/s', tag='revs')
anglePerTimeUom.rpm = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value='rpm', tag='rpm')
anglePerTimeUom._InitializeFacetMap(anglePerTimeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'anglePerTimeUom', anglePerTimeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}areaUom
class areaUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'areaUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 61, 1)
    _Documentation = None
areaUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=areaUom, enum_prefix=None)
areaUom.m2 = areaUom._CF_enumeration.addEnumeration(unicode_value='m2', tag='m2')
areaUom.acre = areaUom._CF_enumeration.addEnumeration(unicode_value='acre', tag='acre')
areaUom.b = areaUom._CF_enumeration.addEnumeration(unicode_value='b', tag='b')
areaUom.cm2 = areaUom._CF_enumeration.addEnumeration(unicode_value='cm2', tag='cm2')
areaUom.ft2 = areaUom._CF_enumeration.addEnumeration(unicode_value='ft2', tag='ft2')
areaUom.ha = areaUom._CF_enumeration.addEnumeration(unicode_value='ha', tag='ha')
areaUom.in2 = areaUom._CF_enumeration.addEnumeration(unicode_value='in2', tag='in2')
areaUom.km2 = areaUom._CF_enumeration.addEnumeration(unicode_value='km2', tag='km2')
areaUom.mi2 = areaUom._CF_enumeration.addEnumeration(unicode_value='mi2', tag='mi2')
areaUom.miUS2 = areaUom._CF_enumeration.addEnumeration(unicode_value='miUS2', tag='miUS2')
areaUom.mm2 = areaUom._CF_enumeration.addEnumeration(unicode_value='mm2', tag='mm2')
areaUom.um2 = areaUom._CF_enumeration.addEnumeration(unicode_value='um2', tag='um2')
areaUom.yd2 = areaUom._CF_enumeration.addEnumeration(unicode_value='yd2', tag='yd2')
areaUom._InitializeFacetMap(areaUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'areaUom', areaUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}areaPerAreaUom
class areaPerAreaUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'areaPerAreaUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 79, 1)
    _Documentation = None
areaPerAreaUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=areaPerAreaUom, enum_prefix=None)
areaPerAreaUom.Euc = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='Euc', tag='Euc')
areaPerAreaUom.emptyString = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
areaPerAreaUom.in2ft2 = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='in2/ft2', tag='in2ft2')
areaPerAreaUom.in2in2 = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='in2/in2', tag='in2in2')
areaPerAreaUom.m2m2 = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='m2/m2', tag='m2m2')
areaPerAreaUom.mm2mm2 = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value='mm2/mm2', tag='mm2mm2')
areaPerAreaUom._InitializeFacetMap(areaPerAreaUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'areaPerAreaUom', areaPerAreaUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}densityUom
class densityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'densityUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 90, 1)
    _Documentation = None
densityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=densityUom, enum_prefix=None)
densityUom.kgm3 = densityUom._CF_enumeration.addEnumeration(unicode_value='kg/m3', tag='kgm3')
densityUom.n10Mgm3 = densityUom._CF_enumeration.addEnumeration(unicode_value='10Mg/m3', tag='n10Mgm3')
densityUom.dAPI = densityUom._CF_enumeration.addEnumeration(unicode_value='dAPI', tag='dAPI')
densityUom.gcm3 = densityUom._CF_enumeration.addEnumeration(unicode_value='g/cm3', tag='gcm3')
densityUom.gdm3 = densityUom._CF_enumeration.addEnumeration(unicode_value='g/dm3', tag='gdm3')
densityUom.ggalUK = densityUom._CF_enumeration.addEnumeration(unicode_value='g/galUK', tag='ggalUK')
densityUom.ggalUS = densityUom._CF_enumeration.addEnumeration(unicode_value='g/galUS', tag='ggalUS')
densityUom.gL = densityUom._CF_enumeration.addEnumeration(unicode_value='g/L', tag='gL')
densityUom.gm3 = densityUom._CF_enumeration.addEnumeration(unicode_value='g/m3', tag='gm3')
densityUom.grainft3 = densityUom._CF_enumeration.addEnumeration(unicode_value='grain/ft3', tag='grainft3')
densityUom.graingalUS = densityUom._CF_enumeration.addEnumeration(unicode_value='grain/galUS', tag='graingalUS')
densityUom.grain100ft3 = densityUom._CF_enumeration.addEnumeration(unicode_value='grain/100ft3', tag='grain100ft3')
densityUom.kgdm3 = densityUom._CF_enumeration.addEnumeration(unicode_value='kg/dm3', tag='kgdm3')
densityUom.kgL = densityUom._CF_enumeration.addEnumeration(unicode_value='kg/L', tag='kgL')
densityUom.Mgm3 = densityUom._CF_enumeration.addEnumeration(unicode_value='Mg/m3', tag='Mgm3')
densityUom.lbm10bbl = densityUom._CF_enumeration.addEnumeration(unicode_value='lbm/10bbl', tag='lbm10bbl')
densityUom.lbmbbl = densityUom._CF_enumeration.addEnumeration(unicode_value='lbm/bbl', tag='lbmbbl')
densityUom.lbmft3 = densityUom._CF_enumeration.addEnumeration(unicode_value='lbm/ft3', tag='lbmft3')
densityUom.lbmgalUK = densityUom._CF_enumeration.addEnumeration(unicode_value='lbm/galUK', tag='lbmgalUK')
densityUom.lbm1000galUK = densityUom._CF_enumeration.addEnumeration(unicode_value='lbm/1000galUK', tag='lbm1000galUK')
densityUom.lbmgalUS = densityUom._CF_enumeration.addEnumeration(unicode_value='lbm/galUS', tag='lbmgalUS')
densityUom.lbm1000galUS = densityUom._CF_enumeration.addEnumeration(unicode_value='lbm/1000galUS', tag='lbm1000galUS')
densityUom.lbmin3 = densityUom._CF_enumeration.addEnumeration(unicode_value='lbm/in3', tag='lbmin3')
densityUom.lbmMbbl = densityUom._CF_enumeration.addEnumeration(unicode_value='lbm/Mbbl', tag='lbmMbbl')
densityUom.mgdm3 = densityUom._CF_enumeration.addEnumeration(unicode_value='mg/dm3', tag='mgdm3')
densityUom.mggalUS = densityUom._CF_enumeration.addEnumeration(unicode_value='mg/galUS', tag='mggalUS')
densityUom.mgL = densityUom._CF_enumeration.addEnumeration(unicode_value='mg/L', tag='mgL')
densityUom.mgm3 = densityUom._CF_enumeration.addEnumeration(unicode_value='mg/m3', tag='mgm3')
densityUom.ugcm3 = densityUom._CF_enumeration.addEnumeration(unicode_value='ug/cm3', tag='ugcm3')
densityUom._InitializeFacetMap(densityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'densityUom', densityUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}dimensionlessUom
class dimensionlessUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dimensionlessUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 124, 1)
    _Documentation = None
dimensionlessUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dimensionlessUom, enum_prefix=None)
dimensionlessUom.Euc = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value='Euc', tag='Euc')
dimensionlessUom.emptyString = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
dimensionlessUom.cEuc = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value='cEuc', tag='cEuc')
dimensionlessUom.mEuc = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value='mEuc', tag='mEuc')
dimensionlessUom.nEuc = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value='nEuc', tag='nEuc')
dimensionlessUom.uEuc = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value='uEuc', tag='uEuc')
dimensionlessUom._InitializeFacetMap(dimensionlessUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'dimensionlessUom', dimensionlessUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}dynamicViscosityUom
class dynamicViscosityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dynamicViscosityUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 135, 1)
    _Documentation = None
dynamicViscosityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dynamicViscosityUom, enum_prefix=None)
dynamicViscosityUom.Pa_s = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='Pa.s', tag='Pa_s')
dynamicViscosityUom.cP = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='cP', tag='cP')
dynamicViscosityUom.P = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='P', tag='P')
dynamicViscosityUom.psi_s = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='psi.s', tag='psi_s')
dynamicViscosityUom.dyne_scm2 = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='dyne.s/cm2', tag='dyne_scm2')
dynamicViscosityUom.kgf_sm2 = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='kgf.s/m2', tag='kgf_sm2')
dynamicViscosityUom.lbf_sft2 = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='lbf.s/ft2', tag='lbf_sft2')
dynamicViscosityUom.lbf_sin2 = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='lbf.s/in2', tag='lbf_sin2')
dynamicViscosityUom.mPa_s = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='mPa.s', tag='mPa_s')
dynamicViscosityUom.N_sm2 = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value='N.s/m2', tag='N_sm2')
dynamicViscosityUom._InitializeFacetMap(dynamicViscosityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'dynamicViscosityUom', dynamicViscosityUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}electricCurrentUom
class electricCurrentUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'electricCurrentUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 150, 1)
    _Documentation = None
electricCurrentUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=electricCurrentUom, enum_prefix=None)
electricCurrentUom.A = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
electricCurrentUom.MA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
electricCurrentUom.kA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value='kA', tag='kA')
electricCurrentUom.mA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value='mA', tag='mA')
electricCurrentUom.nA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value='nA', tag='nA')
electricCurrentUom.pA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value='pA', tag='pA')
electricCurrentUom.uA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value='uA', tag='uA')
electricCurrentUom._InitializeFacetMap(electricCurrentUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'electricCurrentUom', electricCurrentUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}electricPotentialUom
class electricPotentialUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'electricPotentialUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 162, 1)
    _Documentation = None
electricPotentialUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=electricPotentialUom, enum_prefix=None)
electricPotentialUom.V = electricPotentialUom._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
electricPotentialUom.kV = electricPotentialUom._CF_enumeration.addEnumeration(unicode_value='kV', tag='kV')
electricPotentialUom.mV = electricPotentialUom._CF_enumeration.addEnumeration(unicode_value='mV', tag='mV')
electricPotentialUom.MV = electricPotentialUom._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
electricPotentialUom.uV = electricPotentialUom._CF_enumeration.addEnumeration(unicode_value='uV', tag='uV')
electricPotentialUom._InitializeFacetMap(electricPotentialUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'electricPotentialUom', electricPotentialUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}energyPerAreaUom
class energyPerAreaUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'energyPerAreaUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 172, 1)
    _Documentation = None
energyPerAreaUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=energyPerAreaUom, enum_prefix=None)
energyPerAreaUom.Nm = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value='N/m', tag='Nm')
energyPerAreaUom.ergcm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value='erg/cm2', tag='ergcm2')
energyPerAreaUom.Jcm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value='J/cm2', tag='Jcm2')
energyPerAreaUom.Jm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value='J/m2', tag='Jm2')
energyPerAreaUom.kgf_mcm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value='kgf.m/cm2', tag='kgf_mcm2')
energyPerAreaUom.lbf_ftin2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value='lbf.ft/in2', tag='lbf_ftin2')
energyPerAreaUom.mJcm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value='mJ/cm2', tag='mJcm2')
energyPerAreaUom.mJm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value='mJ/m2', tag='mJm2')
energyPerAreaUom._InitializeFacetMap(energyPerAreaUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'energyPerAreaUom', energyPerAreaUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}equivalentPerMassUom
class equivalentPerMassUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equivalentPerMassUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 185, 1)
    _Documentation = None
equivalentPerMassUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=equivalentPerMassUom, enum_prefix=None)
equivalentPerMassUom.eqkg = equivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value='eq/kg', tag='eqkg')
equivalentPerMassUom.meqg = equivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value='meq/g', tag='meqg')
equivalentPerMassUom.meq100g = equivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value='meq/100g', tag='meq100g')
equivalentPerMassUom._InitializeFacetMap(equivalentPerMassUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'equivalentPerMassUom', equivalentPerMassUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}forceUom
class forceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'forceUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 193, 1)
    _Documentation = None
forceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=forceUom, enum_prefix=None)
forceUom.N = forceUom._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
forceUom.daN = forceUom._CF_enumeration.addEnumeration(unicode_value='daN', tag='daN')
forceUom.dyne = forceUom._CF_enumeration.addEnumeration(unicode_value='dyne', tag='dyne')
forceUom.gf = forceUom._CF_enumeration.addEnumeration(unicode_value='gf', tag='gf')
forceUom.kdyne = forceUom._CF_enumeration.addEnumeration(unicode_value='kdyne', tag='kdyne')
forceUom.kgf = forceUom._CF_enumeration.addEnumeration(unicode_value='kgf', tag='kgf')
forceUom.klbf = forceUom._CF_enumeration.addEnumeration(unicode_value='klbf', tag='klbf')
forceUom.kN = forceUom._CF_enumeration.addEnumeration(unicode_value='kN', tag='kN')
forceUom.lbf = forceUom._CF_enumeration.addEnumeration(unicode_value='lbf', tag='lbf')
forceUom.Mgf = forceUom._CF_enumeration.addEnumeration(unicode_value='Mgf', tag='Mgf')
forceUom.mN = forceUom._CF_enumeration.addEnumeration(unicode_value='mN', tag='mN')
forceUom.MN = forceUom._CF_enumeration.addEnumeration(unicode_value='MN', tag='MN')
forceUom.ozf = forceUom._CF_enumeration.addEnumeration(unicode_value='ozf', tag='ozf')
forceUom.pdl = forceUom._CF_enumeration.addEnumeration(unicode_value='pdl', tag='pdl')
forceUom.tonfUK = forceUom._CF_enumeration.addEnumeration(unicode_value='tonfUK', tag='tonfUK')
forceUom.tonfUS = forceUom._CF_enumeration.addEnumeration(unicode_value='tonfUS', tag='tonfUS')
forceUom.uN = forceUom._CF_enumeration.addEnumeration(unicode_value='uN', tag='uN')
forceUom._InitializeFacetMap(forceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'forceUom', forceUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}forcePerLengthUom
class forcePerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'forcePerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 215, 1)
    _Documentation = None
forcePerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=forcePerLengthUom, enum_prefix=None)
forcePerLengthUom.N30m = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='N/30m', tag='N30m')
forcePerLengthUom.Nm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='N/m', tag='Nm')
forcePerLengthUom.dynecm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='dyne/cm', tag='dynecm')
forcePerLengthUom.kNm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='kN/m', tag='kNm')
forcePerLengthUom.kgfcm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='kgf/cm', tag='kgfcm')
forcePerLengthUom.lbf100ft = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='lbf/100ft', tag='lbf100ft')
forcePerLengthUom.lbf30m = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='lbf/30m', tag='lbf30m')
forcePerLengthUom.lbfft = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='lbf/ft', tag='lbfft')
forcePerLengthUom.lbfin = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='lbf/in', tag='lbfin')
forcePerLengthUom.mNkm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='mN/km', tag='mNkm')
forcePerLengthUom.mNm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='mN/m', tag='mNm')
forcePerLengthUom.pdlcm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='pdl/cm', tag='pdlcm')
forcePerLengthUom.tonfUKft = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='tonfUK/ft', tag='tonfUKft')
forcePerLengthUom.tonfUSft = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value='tonfUS/ft', tag='tonfUSft')
forcePerLengthUom._InitializeFacetMap(forcePerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'forcePerLengthUom', forcePerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}forcePerVolumeUom
class forcePerVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'forcePerVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 234, 1)
    _Documentation = None
forcePerVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=forcePerVolumeUom, enum_prefix=None)
forcePerVolumeUom.Nm3 = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='N/m3', tag='Nm3')
forcePerVolumeUom.atm100m = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='atm/100m', tag='atm100m')
forcePerVolumeUom.atmm = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='atm/m', tag='atmm')
forcePerVolumeUom.barkm = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bar/km', tag='barkm')
forcePerVolumeUom.barm = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bar/m', tag='barm')
forcePerVolumeUom.GPacm = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='GPa/cm', tag='GPacm')
forcePerVolumeUom.kPa100m = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='kPa/100m', tag='kPa100m')
forcePerVolumeUom.kPam = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='kPa/m', tag='kPam')
forcePerVolumeUom.lbfft3 = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='lbf/ft3', tag='lbfft3')
forcePerVolumeUom.lbfgalUS = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='lbf/galUS', tag='lbfgalUS')
forcePerVolumeUom.MPam = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='MPa/m', tag='MPam')
forcePerVolumeUom.psift = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='psi/ft', tag='psift')
forcePerVolumeUom.psi100ft = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='psi/100ft', tag='psi100ft')
forcePerVolumeUom.psikft = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='psi/kft', tag='psikft')
forcePerVolumeUom.psim = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='psi/m', tag='psim')
forcePerVolumeUom.Pam = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='Pa/m', tag='Pam')
forcePerVolumeUom.atmft = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='atm/ft', tag='atmft')
forcePerVolumeUom._InitializeFacetMap(forcePerVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'forcePerVolumeUom', forcePerVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}frequencyUom
class frequencyUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'frequencyUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 256, 1)
    _Documentation = None
frequencyUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=frequencyUom, enum_prefix=None)
frequencyUom.Hz = frequencyUom._CF_enumeration.addEnumeration(unicode_value='Hz', tag='Hz')
frequencyUom.cs = frequencyUom._CF_enumeration.addEnumeration(unicode_value='c/s', tag='cs')
frequencyUom.GHz = frequencyUom._CF_enumeration.addEnumeration(unicode_value='GHz', tag='GHz')
frequencyUom.kHz = frequencyUom._CF_enumeration.addEnumeration(unicode_value='kHz', tag='kHz')
frequencyUom.mHz = frequencyUom._CF_enumeration.addEnumeration(unicode_value='mHz', tag='mHz')
frequencyUom.MHz = frequencyUom._CF_enumeration.addEnumeration(unicode_value='MHz', tag='MHz')
frequencyUom.uHz = frequencyUom._CF_enumeration.addEnumeration(unicode_value='uHz', tag='uHz')
frequencyUom.n1s = frequencyUom._CF_enumeration.addEnumeration(unicode_value='1/s', tag='n1s')
frequencyUom.n1a = frequencyUom._CF_enumeration.addEnumeration(unicode_value='1/a', tag='n1a')
frequencyUom.n1d = frequencyUom._CF_enumeration.addEnumeration(unicode_value='1/d', tag='n1d')
frequencyUom.n1h = frequencyUom._CF_enumeration.addEnumeration(unicode_value='1/h', tag='n1h')
frequencyUom.n1min = frequencyUom._CF_enumeration.addEnumeration(unicode_value='1/min', tag='n1min')
frequencyUom.n1wk = frequencyUom._CF_enumeration.addEnumeration(unicode_value='1/wk', tag='n1wk')
frequencyUom.kEucs = frequencyUom._CF_enumeration.addEnumeration(unicode_value='kEuc/s', tag='kEucs')
frequencyUom._InitializeFacetMap(frequencyUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'frequencyUom', frequencyUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}illuminanceUom
class illuminanceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'illuminanceUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 275, 1)
    _Documentation = None
illuminanceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=illuminanceUom, enum_prefix=None)
illuminanceUom.lx = illuminanceUom._CF_enumeration.addEnumeration(unicode_value='lx', tag='lx')
illuminanceUom.lmm2 = illuminanceUom._CF_enumeration.addEnumeration(unicode_value='lm/m2', tag='lmm2')
illuminanceUom.footcandle = illuminanceUom._CF_enumeration.addEnumeration(unicode_value='footcandle', tag='footcandle')
illuminanceUom.klx = illuminanceUom._CF_enumeration.addEnumeration(unicode_value='klx', tag='klx')
illuminanceUom._InitializeFacetMap(illuminanceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'illuminanceUom', illuminanceUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}lengthUom
class lengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengthUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 284, 1)
    _Documentation = None
lengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lengthUom, enum_prefix=None)
lengthUom.m = lengthUom._CF_enumeration.addEnumeration(unicode_value='m', tag='m')
lengthUom.angstrom = lengthUom._CF_enumeration.addEnumeration(unicode_value='angstrom', tag='angstrom')
lengthUom.chBnA = lengthUom._CF_enumeration.addEnumeration(unicode_value='chBnA', tag='chBnA')
lengthUom.chBnB = lengthUom._CF_enumeration.addEnumeration(unicode_value='chBnB', tag='chBnB')
lengthUom.chCla = lengthUom._CF_enumeration.addEnumeration(unicode_value='chCla', tag='chCla')
lengthUom.chSe = lengthUom._CF_enumeration.addEnumeration(unicode_value='chSe', tag='chSe')
lengthUom.chUS = lengthUom._CF_enumeration.addEnumeration(unicode_value='chUS', tag='chUS')
lengthUom.cm = lengthUom._CF_enumeration.addEnumeration(unicode_value='cm', tag='cm')
lengthUom.dm = lengthUom._CF_enumeration.addEnumeration(unicode_value='dm', tag='dm')
lengthUom.fathom = lengthUom._CF_enumeration.addEnumeration(unicode_value='fathom', tag='fathom')
lengthUom.fm = lengthUom._CF_enumeration.addEnumeration(unicode_value='fm', tag='fm')
lengthUom.ft = lengthUom._CF_enumeration.addEnumeration(unicode_value='ft', tag='ft')
lengthUom.ftBnA = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftBnA', tag='ftBnA')
lengthUom.ftBnB = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftBnB', tag='ftBnB')
lengthUom.ftBr65 = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftBr(65)', tag='ftBr65')
lengthUom.ftCla = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftCla', tag='ftCla')
lengthUom.ftGC = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftGC', tag='ftGC')
lengthUom.ftInd = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftInd', tag='ftInd')
lengthUom.ftInd37 = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftInd(37)', tag='ftInd37')
lengthUom.ftInd62 = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftInd(62)', tag='ftInd62')
lengthUom.ftInd75 = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftInd(75)', tag='ftInd75')
lengthUom.ftMA = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftMA', tag='ftMA')
lengthUom.ftSe = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftSe', tag='ftSe')
lengthUom.ftUS = lengthUom._CF_enumeration.addEnumeration(unicode_value='ftUS', tag='ftUS')
lengthUom.in_ = lengthUom._CF_enumeration.addEnumeration(unicode_value='in', tag='in_')
lengthUom.in10 = lengthUom._CF_enumeration.addEnumeration(unicode_value='in/10', tag='in10')
lengthUom.in16 = lengthUom._CF_enumeration.addEnumeration(unicode_value='in/16', tag='in16')
lengthUom.in32 = lengthUom._CF_enumeration.addEnumeration(unicode_value='in/32', tag='in32')
lengthUom.in64 = lengthUom._CF_enumeration.addEnumeration(unicode_value='in/64', tag='in64')
lengthUom.inUS = lengthUom._CF_enumeration.addEnumeration(unicode_value='inUS', tag='inUS')
lengthUom.km = lengthUom._CF_enumeration.addEnumeration(unicode_value='km', tag='km')
lengthUom.lkBnA = lengthUom._CF_enumeration.addEnumeration(unicode_value='lkBnA', tag='lkBnA')
lengthUom.lkBnB = lengthUom._CF_enumeration.addEnumeration(unicode_value='lkBnB', tag='lkBnB')
lengthUom.lkCla = lengthUom._CF_enumeration.addEnumeration(unicode_value='lkCla', tag='lkCla')
lengthUom.lkSe = lengthUom._CF_enumeration.addEnumeration(unicode_value='lkSe', tag='lkSe')
lengthUom.lkUS = lengthUom._CF_enumeration.addEnumeration(unicode_value='lkUS', tag='lkUS')
lengthUom.mGer = lengthUom._CF_enumeration.addEnumeration(unicode_value='mGer', tag='mGer')
lengthUom.mi = lengthUom._CF_enumeration.addEnumeration(unicode_value='mi', tag='mi')
lengthUom.mil = lengthUom._CF_enumeration.addEnumeration(unicode_value='mil', tag='mil')
lengthUom.miUS = lengthUom._CF_enumeration.addEnumeration(unicode_value='miUS', tag='miUS')
lengthUom.mm = lengthUom._CF_enumeration.addEnumeration(unicode_value='mm', tag='mm')
lengthUom.Mm = lengthUom._CF_enumeration.addEnumeration(unicode_value='Mm', tag='Mm')
lengthUom.nautmi = lengthUom._CF_enumeration.addEnumeration(unicode_value='nautmi', tag='nautmi')
lengthUom.nm = lengthUom._CF_enumeration.addEnumeration(unicode_value='nm', tag='nm')
lengthUom.pm = lengthUom._CF_enumeration.addEnumeration(unicode_value='pm', tag='pm')
lengthUom.um = lengthUom._CF_enumeration.addEnumeration(unicode_value='um', tag='um')
lengthUom.yd = lengthUom._CF_enumeration.addEnumeration(unicode_value='yd', tag='yd')
lengthUom.ydBnA = lengthUom._CF_enumeration.addEnumeration(unicode_value='ydBnA', tag='ydBnA')
lengthUom.ydBnB = lengthUom._CF_enumeration.addEnumeration(unicode_value='ydBnB', tag='ydBnB')
lengthUom.ydCla = lengthUom._CF_enumeration.addEnumeration(unicode_value='ydCla', tag='ydCla')
lengthUom.ydIm = lengthUom._CF_enumeration.addEnumeration(unicode_value='ydIm', tag='ydIm')
lengthUom.ydInd = lengthUom._CF_enumeration.addEnumeration(unicode_value='ydInd', tag='ydInd')
lengthUom.ydInd37 = lengthUom._CF_enumeration.addEnumeration(unicode_value='ydInd(37)', tag='ydInd37')
lengthUom.ydInd62 = lengthUom._CF_enumeration.addEnumeration(unicode_value='ydInd(62)', tag='ydInd62')
lengthUom.ydInd75 = lengthUom._CF_enumeration.addEnumeration(unicode_value='ydInd(75)', tag='ydInd75')
lengthUom.ydSe = lengthUom._CF_enumeration.addEnumeration(unicode_value='ydSe', tag='ydSe')
lengthUom._InitializeFacetMap(lengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'lengthUom', lengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}lengthPerLengthUom
class lengthPerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengthPerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 345, 1)
    _Documentation = None
lengthPerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lengthPerLengthUom, enum_prefix=None)
lengthPerLengthUom.emptyString = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
lengthPerLengthUom.ft100ft = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft/100ft', tag='ft100ft')
lengthPerLengthUom.ftft = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft/ft', tag='ftft')
lengthPerLengthUom.ftin = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft/in', tag='ftin')
lengthPerLengthUom.ftm = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft/m', tag='ftm')
lengthPerLengthUom.ftmi = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='ft/mi', tag='ftmi')
lengthPerLengthUom.kmcm = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='km/cm', tag='kmcm')
lengthPerLengthUom.m30m = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='m/30m', tag='m30m')
lengthPerLengthUom.mcm = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='m/cm', tag='mcm')
lengthPerLengthUom.mkm = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='m/km', tag='mkm')
lengthPerLengthUom.mm = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='m/m', tag='mm')
lengthPerLengthUom.miin = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value='mi/in', tag='miin')
lengthPerLengthUom._InitializeFacetMap(lengthPerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'lengthPerLengthUom', lengthPerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}magneticFieldStrengthUom
class magneticFieldStrengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'magneticFieldStrengthUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 362, 1)
    _Documentation = None
magneticFieldStrengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=magneticFieldStrengthUom, enum_prefix=None)
magneticFieldStrengthUom.Am = magneticFieldStrengthUom._CF_enumeration.addEnumeration(unicode_value='A/m', tag='Am')
magneticFieldStrengthUom.Amm = magneticFieldStrengthUom._CF_enumeration.addEnumeration(unicode_value='A/mm', tag='Amm')
magneticFieldStrengthUom.gamma = magneticFieldStrengthUom._CF_enumeration.addEnumeration(unicode_value='gamma', tag='gamma')
magneticFieldStrengthUom.Oe = magneticFieldStrengthUom._CF_enumeration.addEnumeration(unicode_value='Oe', tag='Oe')
magneticFieldStrengthUom._InitializeFacetMap(magneticFieldStrengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'magneticFieldStrengthUom', magneticFieldStrengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}magneticInductionUom
class magneticInductionUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'magneticInductionUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 371, 1)
    _Documentation = None
magneticInductionUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=magneticInductionUom, enum_prefix=None)
magneticInductionUom.T = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
magneticInductionUom.gauss = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value='gauss', tag='gauss')
magneticInductionUom.mT = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value='mT', tag='mT')
magneticInductionUom.mgauss = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value='mgauss', tag='mgauss')
magneticInductionUom.nT = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value='nT', tag='nT')
magneticInductionUom.uT = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value='uT', tag='uT')
magneticInductionUom._InitializeFacetMap(magneticInductionUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'magneticInductionUom', magneticInductionUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}massConcentrationUom
class massConcentrationUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'massConcentrationUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 382, 1)
    _Documentation = None
massConcentrationUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=massConcentrationUom, enum_prefix=None)
massConcentrationUom.Euc = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value='Euc', tag='Euc')
massConcentrationUom.emptyString = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
massConcentrationUom.gkg = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value='g/kg', tag='gkg')
massConcentrationUom.kgkg = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value='kg/kg', tag='kgkg')
massConcentrationUom.kgsack94 = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value='kg/sack94', tag='kgsack94')
massConcentrationUom.mgkg = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value='mg/kg', tag='mgkg')
massConcentrationUom.permil = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value='permil', tag='permil')
massConcentrationUom.ppdk = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value='ppdk', tag='ppdk')
massConcentrationUom.ppk = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value='ppk', tag='ppk')
massConcentrationUom.ppm = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value='ppm', tag='ppm')
massConcentrationUom._InitializeFacetMap(massConcentrationUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'massConcentrationUom', massConcentrationUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}massUom
class massUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'massUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 397, 1)
    _Documentation = None
massUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=massUom, enum_prefix=None)
massUom.kg = massUom._CF_enumeration.addEnumeration(unicode_value='kg', tag='kg')
massUom.ag = massUom._CF_enumeration.addEnumeration(unicode_value='ag', tag='ag')
massUom.ct = massUom._CF_enumeration.addEnumeration(unicode_value='ct', tag='ct')
massUom.cwtUK = massUom._CF_enumeration.addEnumeration(unicode_value='cwtUK', tag='cwtUK')
massUom.cwtUS = massUom._CF_enumeration.addEnumeration(unicode_value='cwtUS', tag='cwtUS')
massUom.g = massUom._CF_enumeration.addEnumeration(unicode_value='g', tag='g')
massUom.grain = massUom._CF_enumeration.addEnumeration(unicode_value='grain', tag='grain')
massUom.klbm = massUom._CF_enumeration.addEnumeration(unicode_value='klbm', tag='klbm')
massUom.lbm = massUom._CF_enumeration.addEnumeration(unicode_value='lbm', tag='lbm')
massUom.Mg = massUom._CF_enumeration.addEnumeration(unicode_value='Mg', tag='Mg')
massUom.mg = massUom._CF_enumeration.addEnumeration(unicode_value='mg', tag='mg')
massUom.ozav = massUom._CF_enumeration.addEnumeration(unicode_value='oz(av)', tag='ozav')
massUom.oztroy = massUom._CF_enumeration.addEnumeration(unicode_value='oz(troy)', tag='oztroy')
massUom.ozm = massUom._CF_enumeration.addEnumeration(unicode_value='ozm', tag='ozm')
massUom.sack94 = massUom._CF_enumeration.addEnumeration(unicode_value='sack94', tag='sack94')
massUom.t = massUom._CF_enumeration.addEnumeration(unicode_value='t', tag='t')
massUom.tonUK = massUom._CF_enumeration.addEnumeration(unicode_value='tonUK', tag='tonUK')
massUom.tonUS = massUom._CF_enumeration.addEnumeration(unicode_value='tonUS', tag='tonUS')
massUom.ug = massUom._CF_enumeration.addEnumeration(unicode_value='ug', tag='ug')
massUom._InitializeFacetMap(massUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'massUom', massUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}massPerLengthUom
class massPerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'massPerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 421, 1)
    _Documentation = None
massPerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=massPerLengthUom, enum_prefix=None)
massPerLengthUom.kgm = massPerLengthUom._CF_enumeration.addEnumeration(unicode_value='kg/m', tag='kgm')
massPerLengthUom.klbmin = massPerLengthUom._CF_enumeration.addEnumeration(unicode_value='klbm/in', tag='klbmin')
massPerLengthUom.lbmft = massPerLengthUom._CF_enumeration.addEnumeration(unicode_value='lbm/ft', tag='lbmft')
massPerLengthUom.Mgin = massPerLengthUom._CF_enumeration.addEnumeration(unicode_value='Mg/in', tag='Mgin')
massPerLengthUom.kg_mcm2 = massPerLengthUom._CF_enumeration.addEnumeration(unicode_value='kg.m/cm2', tag='kg_mcm2')
massPerLengthUom._InitializeFacetMap(massPerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'massPerLengthUom', massPerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}momentOfForceUom
class momentOfForceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'momentOfForceUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 431, 1)
    _Documentation = None
momentOfForceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=momentOfForceUom, enum_prefix=None)
momentOfForceUom.J = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
momentOfForceUom.dN_m = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='dN.m', tag='dN_m')
momentOfForceUom.daN_m = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='daN.m', tag='daN_m')
momentOfForceUom.ft_lbf = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='ft.lbf', tag='ft_lbf')
momentOfForceUom.kft_lbf = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='kft.lbf', tag='kft_lbf')
momentOfForceUom.kgf_m = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='kgf.m', tag='kgf_m')
momentOfForceUom.kN_m = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='kN.m', tag='kN_m')
momentOfForceUom.lbf_ft = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='lbf.ft', tag='lbf_ft')
momentOfForceUom.lbf_in = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='lbf.in', tag='lbf_in')
momentOfForceUom.lbm_ft2s2 = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='lbm.ft2/s2', tag='lbm_ft2s2')
momentOfForceUom.N_m = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='N.m', tag='N_m')
momentOfForceUom.pdl_ft = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='pdl.ft', tag='pdl_ft')
momentOfForceUom.tonfUS_ft = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='tonfUS.ft', tag='tonfUS_ft')
momentOfForceUom.tonfUS_mi = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value='tonfUS.mi', tag='tonfUS_mi')
momentOfForceUom._InitializeFacetMap(momentOfForceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'momentOfForceUom', momentOfForceUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}perLengthUom
class perLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'perLengthUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 450, 1)
    _Documentation = None
perLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=perLengthUom, enum_prefix=None)
perLengthUom.n1m = perLengthUom._CF_enumeration.addEnumeration(unicode_value='1/m', tag='n1m')
perLengthUom.n1angstrom = perLengthUom._CF_enumeration.addEnumeration(unicode_value='1/angstrom', tag='n1angstrom')
perLengthUom.n1cm = perLengthUom._CF_enumeration.addEnumeration(unicode_value='1/cm', tag='n1cm')
perLengthUom.n1ft = perLengthUom._CF_enumeration.addEnumeration(unicode_value='1/ft', tag='n1ft')
perLengthUom.n1in = perLengthUom._CF_enumeration.addEnumeration(unicode_value='1/in', tag='n1in')
perLengthUom.n1mi = perLengthUom._CF_enumeration.addEnumeration(unicode_value='1/mi', tag='n1mi')
perLengthUom.n1mm = perLengthUom._CF_enumeration.addEnumeration(unicode_value='1/mm', tag='n1mm')
perLengthUom.n1nm = perLengthUom._CF_enumeration.addEnumeration(unicode_value='1/nm', tag='n1nm')
perLengthUom.n1yd = perLengthUom._CF_enumeration.addEnumeration(unicode_value='1/yd', tag='n1yd')
perLengthUom._InitializeFacetMap(perLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'perLengthUom', perLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}planeAngleUom
class planeAngleUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'planeAngleUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 464, 1)
    _Documentation = None
planeAngleUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=planeAngleUom, enum_prefix=None)
planeAngleUom.rad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='rad', tag='rad')
planeAngleUom.c = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='c', tag='c')
planeAngleUom.ccgr = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='ccgr', tag='ccgr')
planeAngleUom.cgr = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='cgr', tag='cgr')
planeAngleUom.dega = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='dega', tag='dega')
planeAngleUom.gon = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='gon', tag='gon')
planeAngleUom.gr = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='gr', tag='gr')
planeAngleUom.Grad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='Grad', tag='Grad')
planeAngleUom.krad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='krad', tag='krad')
planeAngleUom.mila = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='mila', tag='mila')
planeAngleUom.mina = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='mina', tag='mina')
planeAngleUom.mrad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='mrad', tag='mrad')
planeAngleUom.Mrad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='Mrad', tag='Mrad')
planeAngleUom.mseca = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='mseca', tag='mseca')
planeAngleUom.seca = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='seca', tag='seca')
planeAngleUom.urad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value='urad', tag='urad')
planeAngleUom._InitializeFacetMap(planeAngleUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'planeAngleUom', planeAngleUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}powerUom
class powerUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'powerUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 485, 1)
    _Documentation = None
powerUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=powerUom, enum_prefix=None)
powerUom.W = powerUom._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
powerUom.ch = powerUom._CF_enumeration.addEnumeration(unicode_value='ch', tag='ch')
powerUom.CV = powerUom._CF_enumeration.addEnumeration(unicode_value='CV', tag='CV')
powerUom.ehp = powerUom._CF_enumeration.addEnumeration(unicode_value='ehp', tag='ehp')
powerUom.GW = powerUom._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
powerUom.hhp = powerUom._CF_enumeration.addEnumeration(unicode_value='hhp', tag='hhp')
powerUom.hp = powerUom._CF_enumeration.addEnumeration(unicode_value='hp', tag='hp')
powerUom.kcalh = powerUom._CF_enumeration.addEnumeration(unicode_value='kcal/h', tag='kcalh')
powerUom.kW = powerUom._CF_enumeration.addEnumeration(unicode_value='kW', tag='kW')
powerUom.MJa = powerUom._CF_enumeration.addEnumeration(unicode_value='MJ/a', tag='MJa')
powerUom.MW = powerUom._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
powerUom.mW = powerUom._CF_enumeration.addEnumeration(unicode_value='mW', tag='mW')
powerUom.nW = powerUom._CF_enumeration.addEnumeration(unicode_value='nW', tag='nW')
powerUom.ton_of_refrig = powerUom._CF_enumeration.addEnumeration(unicode_value='ton of refrig', tag='ton_of_refrig')
powerUom.TW = powerUom._CF_enumeration.addEnumeration(unicode_value='TW', tag='TW')
powerUom.uW = powerUom._CF_enumeration.addEnumeration(unicode_value='uW', tag='uW')
powerUom._InitializeFacetMap(powerUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'powerUom', powerUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}pressureUom
class pressureUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pressureUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 506, 1)
    _Documentation = None
pressureUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=pressureUom, enum_prefix=None)
pressureUom.Pa = pressureUom._CF_enumeration.addEnumeration(unicode_value='Pa', tag='Pa')
pressureUom.at = pressureUom._CF_enumeration.addEnumeration(unicode_value='at', tag='at')
pressureUom.atm = pressureUom._CF_enumeration.addEnumeration(unicode_value='atm', tag='atm')
pressureUom.bar = pressureUom._CF_enumeration.addEnumeration(unicode_value='bar', tag='bar')
pressureUom.cmH2O4degC = pressureUom._CF_enumeration.addEnumeration(unicode_value='cmH2O(4degC)', tag='cmH2O4degC')
pressureUom.dynecm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='dyne/cm2', tag='dynecm2')
pressureUom.GPa = pressureUom._CF_enumeration.addEnumeration(unicode_value='GPa', tag='GPa')
pressureUom.hbar = pressureUom._CF_enumeration.addEnumeration(unicode_value='hbar', tag='hbar')
pressureUom.inH2O39_2F = pressureUom._CF_enumeration.addEnumeration(unicode_value='inH2O(39.2F)', tag='inH2O39_2F')
pressureUom.inH2O60F = pressureUom._CF_enumeration.addEnumeration(unicode_value='inH2O(60F)', tag='inH2O60F')
pressureUom.inHg32F = pressureUom._CF_enumeration.addEnumeration(unicode_value='inHg(32F)', tag='inHg32F')
pressureUom.inHg60F = pressureUom._CF_enumeration.addEnumeration(unicode_value='inHg(60F)', tag='inHg60F')
pressureUom.kgfcm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='kgf/cm2', tag='kgfcm2')
pressureUom.kgfmm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='kgf/mm2', tag='kgfmm2')
pressureUom.kNm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='kN/m2', tag='kNm2')
pressureUom.kPa = pressureUom._CF_enumeration.addEnumeration(unicode_value='kPa', tag='kPa')
pressureUom.kpsi = pressureUom._CF_enumeration.addEnumeration(unicode_value='kpsi', tag='kpsi')
pressureUom.lbfft2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='lbf/ft2', tag='lbfft2')
pressureUom.lbf100ft2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='lbf/100ft2', tag='lbf100ft2')
pressureUom.lbfin2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='lbf/in2', tag='lbfin2')
pressureUom.mbar = pressureUom._CF_enumeration.addEnumeration(unicode_value='mbar', tag='mbar')
pressureUom.mmHg0C = pressureUom._CF_enumeration.addEnumeration(unicode_value='mmHg(0C)', tag='mmHg0C')
pressureUom.mPa = pressureUom._CF_enumeration.addEnumeration(unicode_value='mPa', tag='mPa')
pressureUom.MPa = pressureUom._CF_enumeration.addEnumeration(unicode_value='MPa', tag='MPa')
pressureUom.Mpsi = pressureUom._CF_enumeration.addEnumeration(unicode_value='Mpsi', tag='Mpsi')
pressureUom.Nm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='N/m2', tag='Nm2')
pressureUom.Nmm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='N/mm2', tag='Nmm2')
pressureUom.Pag = pressureUom._CF_enumeration.addEnumeration(unicode_value='Pa(g)', tag='Pag')
pressureUom.pPa = pressureUom._CF_enumeration.addEnumeration(unicode_value='pPa', tag='pPa')
pressureUom.psi = pressureUom._CF_enumeration.addEnumeration(unicode_value='psi', tag='psi')
pressureUom.psia = pressureUom._CF_enumeration.addEnumeration(unicode_value='psia', tag='psia')
pressureUom.psig = pressureUom._CF_enumeration.addEnumeration(unicode_value='psig', tag='psig')
pressureUom.tonfUSft2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='tonfUS/ft2', tag='tonfUSft2')
pressureUom.tonfUSin2 = pressureUom._CF_enumeration.addEnumeration(unicode_value='tonfUS/in2', tag='tonfUSin2')
pressureUom.torr = pressureUom._CF_enumeration.addEnumeration(unicode_value='torr', tag='torr')
pressureUom.ubar = pressureUom._CF_enumeration.addEnumeration(unicode_value='ubar', tag='ubar')
pressureUom.umHg0C = pressureUom._CF_enumeration.addEnumeration(unicode_value='umHg(0C)', tag='umHg0C')
pressureUom.uPa = pressureUom._CF_enumeration.addEnumeration(unicode_value='uPa', tag='uPa')
pressureUom.upsi = pressureUom._CF_enumeration.addEnumeration(unicode_value='upsi', tag='upsi')
pressureUom._InitializeFacetMap(pressureUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'pressureUom', pressureUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}relativePowerUom
class relativePowerUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relativePowerUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 550, 1)
    _Documentation = None
relativePowerUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=relativePowerUom, enum_prefix=None)
relativePowerUom.emptyString = relativePowerUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
relativePowerUom.Btubhp_hr = relativePowerUom._CF_enumeration.addEnumeration(unicode_value='Btu/bhp.hr', tag='Btubhp_hr')
relativePowerUom.WkW = relativePowerUom._CF_enumeration.addEnumeration(unicode_value='W/kW', tag='WkW')
relativePowerUom.WW = relativePowerUom._CF_enumeration.addEnumeration(unicode_value='W/W', tag='WW')
relativePowerUom._InitializeFacetMap(relativePowerUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'relativePowerUom', relativePowerUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}specificVolumeUom
class specificVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'specificVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 559, 1)
    _Documentation = None
specificVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=specificVolumeUom, enum_prefix=None)
specificVolumeUom.m3kg = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/kg', tag='m3kg')
specificVolumeUom.bbltonUK = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/tonUK', tag='bbltonUK')
specificVolumeUom.bbltonUS = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/tonUS', tag='bbltonUS')
specificVolumeUom.cm3g = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='cm3/g', tag='cm3g')
specificVolumeUom.dm3kg = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='dm3/kg', tag='dm3kg')
specificVolumeUom.dm3t = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='dm3/t', tag='dm3t')
specificVolumeUom.ft3kg = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3/kg', tag='ft3kg')
specificVolumeUom.ft3lbm = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3/lbm', tag='ft3lbm')
specificVolumeUom.ft3sack94 = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3/sack94', tag='ft3sack94')
specificVolumeUom.galUSsack94 = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/sack94', tag='galUSsack94')
specificVolumeUom.galUKlbm = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUK/lbm', tag='galUKlbm')
specificVolumeUom.galUSlbm = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/lbm', tag='galUSlbm')
specificVolumeUom.galUStonUK = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/tonUK', tag='galUStonUK')
specificVolumeUom.galUStonUS = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/tonUS', tag='galUStonUS')
specificVolumeUom.L100kg = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/100kg', tag='L100kg')
specificVolumeUom.Lkg = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/kg', tag='Lkg')
specificVolumeUom.Lt = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/t', tag='Lt')
specificVolumeUom.LtonUK = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/tonUK', tag='LtonUK')
specificVolumeUom.m3g = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/g', tag='m3g')
specificVolumeUom.m3t = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/t', tag='m3t')
specificVolumeUom.m3tonUK = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/tonUK', tag='m3tonUK')
specificVolumeUom.m3tonUS = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/tonUS', tag='m3tonUS')
specificVolumeUom._InitializeFacetMap(specificVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'specificVolumeUom', specificVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}thermodynamicTemperatureUom
class thermodynamicTemperatureUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermodynamicTemperatureUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 586, 1)
    _Documentation = None
thermodynamicTemperatureUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=thermodynamicTemperatureUom, enum_prefix=None)
thermodynamicTemperatureUom.K = thermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value='K', tag='K')
thermodynamicTemperatureUom.degC = thermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value='degC', tag='degC')
thermodynamicTemperatureUom.degF = thermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value='degF', tag='degF')
thermodynamicTemperatureUom.degR = thermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value='degR', tag='degR')
thermodynamicTemperatureUom._InitializeFacetMap(thermodynamicTemperatureUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'thermodynamicTemperatureUom', thermodynamicTemperatureUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}timeUom
class timeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 595, 1)
    _Documentation = None
timeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=timeUom, enum_prefix=None)
timeUom.s = timeUom._CF_enumeration.addEnumeration(unicode_value='s', tag='s')
timeUom.a = timeUom._CF_enumeration.addEnumeration(unicode_value='a', tag='a')
timeUom.cs = timeUom._CF_enumeration.addEnumeration(unicode_value='cs', tag='cs')
timeUom.d = timeUom._CF_enumeration.addEnumeration(unicode_value='d', tag='d')
timeUom.Ga = timeUom._CF_enumeration.addEnumeration(unicode_value='Ga', tag='Ga')
timeUom.h = timeUom._CF_enumeration.addEnumeration(unicode_value='h', tag='h')
timeUom.n100s = timeUom._CF_enumeration.addEnumeration(unicode_value='100s', tag='n100s')
timeUom.Ma = timeUom._CF_enumeration.addEnumeration(unicode_value='Ma', tag='Ma')
timeUom.min = timeUom._CF_enumeration.addEnumeration(unicode_value='min', tag='min')
timeUom.ms = timeUom._CF_enumeration.addEnumeration(unicode_value='ms', tag='ms')
timeUom.ms2 = timeUom._CF_enumeration.addEnumeration(unicode_value='ms/2', tag='ms2')
timeUom.ns = timeUom._CF_enumeration.addEnumeration(unicode_value='ns', tag='ns')
timeUom.ps = timeUom._CF_enumeration.addEnumeration(unicode_value='ps', tag='ps')
timeUom.us = timeUom._CF_enumeration.addEnumeration(unicode_value='us', tag='us')
timeUom.wk = timeUom._CF_enumeration.addEnumeration(unicode_value='wk', tag='wk')
timeUom.n100ka = timeUom._CF_enumeration.addEnumeration(unicode_value='100ka', tag='n100ka')
timeUom._InitializeFacetMap(timeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'timeUom', timeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}velocityUom
class velocityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'velocityUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 616, 1)
    _Documentation = None
velocityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=velocityUom, enum_prefix=None)
velocityUom.ms = velocityUom._CF_enumeration.addEnumeration(unicode_value='m/s', tag='ms')
velocityUom.cma = velocityUom._CF_enumeration.addEnumeration(unicode_value='cm/a', tag='cma')
velocityUom.cms = velocityUom._CF_enumeration.addEnumeration(unicode_value='cm/s', tag='cms')
velocityUom.dms = velocityUom._CF_enumeration.addEnumeration(unicode_value='dm/s', tag='dms')
velocityUom.ftd = velocityUom._CF_enumeration.addEnumeration(unicode_value='ft/d', tag='ftd')
velocityUom.fth = velocityUom._CF_enumeration.addEnumeration(unicode_value='ft/h', tag='fth')
velocityUom.ftmin = velocityUom._CF_enumeration.addEnumeration(unicode_value='ft/min', tag='ftmin')
velocityUom.ftms = velocityUom._CF_enumeration.addEnumeration(unicode_value='ft/ms', tag='ftms')
velocityUom.fts = velocityUom._CF_enumeration.addEnumeration(unicode_value='ft/s', tag='fts')
velocityUom.ftus = velocityUom._CF_enumeration.addEnumeration(unicode_value='ft/us', tag='ftus')
velocityUom.ina = velocityUom._CF_enumeration.addEnumeration(unicode_value='in/a', tag='ina')
velocityUom.inmin = velocityUom._CF_enumeration.addEnumeration(unicode_value='in/min', tag='inmin')
velocityUom.ins = velocityUom._CF_enumeration.addEnumeration(unicode_value='in/s', tag='ins')
velocityUom.kfth = velocityUom._CF_enumeration.addEnumeration(unicode_value='kft/h', tag='kfth')
velocityUom.kfts = velocityUom._CF_enumeration.addEnumeration(unicode_value='kft/s', tag='kfts')
velocityUom.kmh = velocityUom._CF_enumeration.addEnumeration(unicode_value='km/h', tag='kmh')
velocityUom.kms = velocityUom._CF_enumeration.addEnumeration(unicode_value='km/s', tag='kms')
velocityUom.knot = velocityUom._CF_enumeration.addEnumeration(unicode_value='knot', tag='knot')
velocityUom.md = velocityUom._CF_enumeration.addEnumeration(unicode_value='m/d', tag='md')
velocityUom.mh = velocityUom._CF_enumeration.addEnumeration(unicode_value='m/h', tag='mh')
velocityUom.mmin = velocityUom._CF_enumeration.addEnumeration(unicode_value='m/min', tag='mmin')
velocityUom.mms = velocityUom._CF_enumeration.addEnumeration(unicode_value='m/ms', tag='mms')
velocityUom.mih = velocityUom._CF_enumeration.addEnumeration(unicode_value='mi/h', tag='mih')
velocityUom.milyr = velocityUom._CF_enumeration.addEnumeration(unicode_value='mil/yr', tag='milyr')
velocityUom.mma = velocityUom._CF_enumeration.addEnumeration(unicode_value='mm/a', tag='mma')
velocityUom.mms_ = velocityUom._CF_enumeration.addEnumeration(unicode_value='mm/s', tag='mms_')
velocityUom.nms = velocityUom._CF_enumeration.addEnumeration(unicode_value='nm/s', tag='nms')
velocityUom.ums = velocityUom._CF_enumeration.addEnumeration(unicode_value='um/s', tag='ums')
velocityUom._InitializeFacetMap(velocityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'velocityUom', velocityUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}volumeUom
class volumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumeUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 649, 1)
    _Documentation = None
volumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=volumeUom, enum_prefix=None)
volumeUom.m3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='m3', tag='m3')
volumeUom.acre_ft = volumeUom._CF_enumeration.addEnumeration(unicode_value='acre.ft', tag='acre_ft')
volumeUom.bbl = volumeUom._CF_enumeration.addEnumeration(unicode_value='bbl', tag='bbl')
volumeUom.bcf = volumeUom._CF_enumeration.addEnumeration(unicode_value='bcf', tag='bcf')
volumeUom.cm3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='cm3', tag='cm3')
volumeUom.dm3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='dm3', tag='dm3')
volumeUom.flozUK = volumeUom._CF_enumeration.addEnumeration(unicode_value='flozUK', tag='flozUK')
volumeUom.flozUS = volumeUom._CF_enumeration.addEnumeration(unicode_value='flozUS', tag='flozUS')
volumeUom.ft3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='ft3', tag='ft3')
volumeUom.galUK = volumeUom._CF_enumeration.addEnumeration(unicode_value='galUK', tag='galUK')
volumeUom.galUS = volumeUom._CF_enumeration.addEnumeration(unicode_value='galUS', tag='galUS')
volumeUom.ha_m = volumeUom._CF_enumeration.addEnumeration(unicode_value='ha.m', tag='ha_m')
volumeUom.hL = volumeUom._CF_enumeration.addEnumeration(unicode_value='hL', tag='hL')
volumeUom.in3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='in3', tag='in3')
volumeUom.n1000ft3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='1000ft3', tag='n1000ft3')
volumeUom.km3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='km3', tag='km3')
volumeUom.L = volumeUom._CF_enumeration.addEnumeration(unicode_value='L', tag='L')
volumeUom.Mbbl = volumeUom._CF_enumeration.addEnumeration(unicode_value='Mbbl', tag='Mbbl')
volumeUom.Mcf = volumeUom._CF_enumeration.addEnumeration(unicode_value='Mcf', tag='Mcf')
volumeUom.Mft3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='M(ft3)', tag='Mft3')
volumeUom.mi3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='mi3', tag='mi3')
volumeUom.mL = volumeUom._CF_enumeration.addEnumeration(unicode_value='mL', tag='mL')
volumeUom.Mm3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='M(m3)', tag='Mm3')
volumeUom.mm3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='mm3', tag='mm3')
volumeUom.MMbbl = volumeUom._CF_enumeration.addEnumeration(unicode_value='MMbbl', tag='MMbbl')
volumeUom.ptUK = volumeUom._CF_enumeration.addEnumeration(unicode_value='ptUK', tag='ptUK')
volumeUom.ptUS = volumeUom._CF_enumeration.addEnumeration(unicode_value='ptUS', tag='ptUS')
volumeUom.qtUK = volumeUom._CF_enumeration.addEnumeration(unicode_value='qtUK', tag='qtUK')
volumeUom.qtUS = volumeUom._CF_enumeration.addEnumeration(unicode_value='qtUS', tag='qtUS')
volumeUom.tcf = volumeUom._CF_enumeration.addEnumeration(unicode_value='tcf', tag='tcf')
volumeUom.um2_m = volumeUom._CF_enumeration.addEnumeration(unicode_value='um2.m', tag='um2_m')
volumeUom.yd3 = volumeUom._CF_enumeration.addEnumeration(unicode_value='yd3', tag='yd3')
volumeUom._InitializeFacetMap(volumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'volumeUom', volumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}volumeFlowRateUom
class volumeFlowRateUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumeFlowRateUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 686, 1)
    _Documentation = None
volumeFlowRateUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=volumeFlowRateUom, enum_prefix=None)
volumeFlowRateUom.m3s = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='m3/s', tag='m3s')
volumeFlowRateUom.bbld = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='bbl/d', tag='bbld')
volumeFlowRateUom.bblhr = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='bbl/hr', tag='bblhr')
volumeFlowRateUom.bblmin = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='bbl/min', tag='bblmin')
volumeFlowRateUom.cm330min = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='cm3/30min', tag='cm330min')
volumeFlowRateUom.cm3h = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='cm3/h', tag='cm3h')
volumeFlowRateUom.cm3min = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='cm3/min', tag='cm3min')
volumeFlowRateUom.cm3s = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='cm3/s', tag='cm3s')
volumeFlowRateUom.dm3s = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='dm3/s', tag='dm3s')
volumeFlowRateUom.ft3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='ft3/d', tag='ft3d')
volumeFlowRateUom.ft3h = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='ft3/h', tag='ft3h')
volumeFlowRateUom.ft3min = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='ft3/min', tag='ft3min')
volumeFlowRateUom.ft3s = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='ft3/s', tag='ft3s')
volumeFlowRateUom.galUKd = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUK/d', tag='galUKd')
volumeFlowRateUom.galUKhr = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUK/hr', tag='galUKhr')
volumeFlowRateUom.galUKmin = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUK/min', tag='galUKmin')
volumeFlowRateUom.galUSd = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUS/d', tag='galUSd')
volumeFlowRateUom.galUShr = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUS/hr', tag='galUShr')
volumeFlowRateUom.galUSmin = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='galUS/min', tag='galUSmin')
volumeFlowRateUom.kbbld = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='kbbl/d', tag='kbbld')
volumeFlowRateUom.n1000ft3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='1000ft3/d', tag='n1000ft3d')
volumeFlowRateUom.n1000m3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='1000m3/d', tag='n1000m3d')
volumeFlowRateUom.n1000m3h = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='1000m3/h', tag='n1000m3h')
volumeFlowRateUom.Lh = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='L/h', tag='Lh')
volumeFlowRateUom.Lmin = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='L/min', tag='Lmin')
volumeFlowRateUom.Ls = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='L/s', tag='Ls')
volumeFlowRateUom.m3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='m3/d', tag='m3d')
volumeFlowRateUom.m3h = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='m3/h', tag='m3h')
volumeFlowRateUom.m3min = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='m3/min', tag='m3min')
volumeFlowRateUom.Mbbld = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='Mbbl/d', tag='Mbbld')
volumeFlowRateUom.Mft3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='M(ft3)/d', tag='Mft3d')
volumeFlowRateUom.Mm3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value='M(m3)/d', tag='Mm3d')
volumeFlowRateUom._InitializeFacetMap(volumeFlowRateUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'volumeFlowRateUom', volumeFlowRateUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}volumePerVolumeUom
class volumePerVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumePerVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 723, 1)
    _Documentation = None
volumePerVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=volumePerVolumeUom, enum_prefix=None)
volumePerVolumeUom.Euc = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='Euc', tag='Euc')
volumePerVolumeUom.emptyString = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString')
volumePerVolumeUom.permil = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='permil', tag='permil')
volumePerVolumeUom.ppdk = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ppdk', tag='ppdk')
volumePerVolumeUom.ppk = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ppk', tag='ppk')
volumePerVolumeUom.ppm = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ppm', tag='ppm')
volumePerVolumeUom.bblacre_ft = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/acre.ft', tag='bblacre_ft')
volumePerVolumeUom.bblbbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/bbl', tag='bblbbl')
volumePerVolumeUom.bblft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/ft3', tag='bblft3')
volumePerVolumeUom.bbl100bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/100bbl', tag='bbl100bbl')
volumePerVolumeUom.bblkft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/k(ft3)', tag='bblkft3')
volumePerVolumeUom.bblMft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='bbl/M(ft3)', tag='bblMft3')
volumePerVolumeUom.cm3cm3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='cm3/cm3', tag='cm3cm3')
volumePerVolumeUom.cm3m3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='cm3/m3', tag='cm3m3')
volumePerVolumeUom.dm3m3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='dm3/m3', tag='dm3m3')
volumePerVolumeUom.ft3bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3/bbl', tag='ft3bbl')
volumePerVolumeUom.ft3ft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ft3/ft3', tag='ft3ft3')
volumePerVolumeUom.galUSkgalUS = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/kgalUS', tag='galUSkgalUS')
volumePerVolumeUom.galUKkgalUK = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUK/kgalUK', tag='galUKkgalUK')
volumePerVolumeUom.galUKft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUK/ft3', tag='galUKft3')
volumePerVolumeUom.galUKMbbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUK/Mbbl', tag='galUKMbbl')
volumePerVolumeUom.galUSbbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/bbl', tag='galUSbbl')
volumePerVolumeUom.galUS10bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/10bbl', tag='galUS10bbl')
volumePerVolumeUom.galUSft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/ft3', tag='galUSft3')
volumePerVolumeUom.galUSMbbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='galUS/Mbbl', tag='galUSMbbl')
volumePerVolumeUom.n1000ft3bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='1000ft3/bbl', tag='n1000ft3bbl')
volumePerVolumeUom.ksm3sm3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ksm3/sm3', tag='ksm3sm3')
volumePerVolumeUom.L10bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/10bbl', tag='L10bbl')
volumePerVolumeUom.Lm3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='L/m3', tag='Lm3')
volumePerVolumeUom.m3ha_m = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/ha.m', tag='m3ha_m')
volumePerVolumeUom.m3m3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='m3/m3', tag='m3m3')
volumePerVolumeUom.Mft3acre_ft = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='M(ft3)/acre.ft', tag='Mft3acre_ft')
volumePerVolumeUom.mLgalUK = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='mL/galUK', tag='mLgalUK')
volumePerVolumeUom.mLgalUS = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='mL/galUS', tag='mLgalUS')
volumePerVolumeUom.mLmL = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='mL/mL', tag='mLmL')
volumePerVolumeUom.MMbblacre_ft = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='MMbbl/acre.ft', tag='MMbblacre_ft')
volumePerVolumeUom.MMscf60stb60 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='MMscf60/stb60', tag='MMscf60stb60')
volumePerVolumeUom.Mscf60stb60 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='Mscf60/stb60', tag='Mscf60stb60')
volumePerVolumeUom.ptUKMbbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ptUK/Mbbl', tag='ptUKMbbl')
volumePerVolumeUom.ptUS10bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='ptUS/10bbl', tag='ptUS10bbl')
volumePerVolumeUom.pu = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='pu', tag='pu')
volumePerVolumeUom.scm15stb60 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='scm15/stb60', tag='scm15stb60')
volumePerVolumeUom.sm3ksm3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='sm3/ksm3', tag='sm3ksm3')
volumePerVolumeUom.sm3sm3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='sm3/sm3', tag='sm3sm3')
volumePerVolumeUom.stb60MMscf60 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb60/MMscf60', tag='stb60MMscf60')
volumePerVolumeUom.stb60MMscm15 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb60/MMscm15', tag='stb60MMscm15')
volumePerVolumeUom.stb60Mscf60 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb60/Mscf60', tag='stb60Mscf60')
volumePerVolumeUom.stb60Mscm15 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb60/Mscm15', tag='stb60Mscm15')
volumePerVolumeUom.stb60scm15 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value='stb60/scm15', tag='stb60scm15')
volumePerVolumeUom._InitializeFacetMap(volumePerVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'volumePerVolumeUom', volumePerVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}commentString
class commentString (abstractCommentString):

    """A comment or remark intended for human consumption. 
			There should be no assumption that semantics can be extracted from this field by a computer. 
			Neither should there be an assumption that any two humans will interpret the information 
			in the same way (i.e., it may not be interoperable)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'commentString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 321, 1)
    _Documentation = 'A comment or remark intended for human consumption. \n\t\t\tThere should be no assumption that semantics can be extracted from this field by a computer. \n\t\t\tNeither should there be an assumption that any two humans will interpret the information \n\t\t\tin the same way (i.e., it may not be interoperable).'
commentString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'commentString', commentString)

# Complex type {http://www.witsml.org/schemas/131}cs_commonData with content type ELEMENT_ONLY
class cs_commonData (pyxb.binding.basis.complexTypeDefinition):
    """ WITSML - Common Data Component Schema """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_commonData')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}sourceName uses Python identifier sourceName
    __sourceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sourceName'), 'sourceName', '__httpwww_witsml_orgschemas131_cs_commonData_httpwww_witsml_orgschemas131sourceName', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 23, 3), )

    
    sourceName = property(__sourceName.value, __sourceName.set, None, 'An identifier to indicate the data originator.\n\t\t\t\t\tThis identifies the server that originally created \n\t\t\t\t\tthe object and thus most of the uids in the object (but not \n\t\t\t\t\tnecessarily the uids of the parents). This is typically a url. ')

    
    # Element {http://www.witsml.org/schemas/131}dTimCreation uses Python identifier dTimCreation
    __dTimCreation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dTimCreation'), 'dTimCreation', '__httpwww_witsml_orgschemas131_cs_commonData_httpwww_witsml_orgschemas131dTimCreation', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 31, 3), )

    
    dTimCreation = property(__dTimCreation.value, __dTimCreation.set, None, 'When the data was created at the persistent data store.  ')

    
    # Element {http://www.witsml.org/schemas/131}dTimLastChange uses Python identifier dTimLastChange
    __dTimLastChange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dTimLastChange'), 'dTimLastChange', '__httpwww_witsml_orgschemas131_cs_commonData_httpwww_witsml_orgschemas131dTimLastChange', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 36, 3), )

    
    dTimLastChange = property(__dTimLastChange.value, __dTimLastChange.set, None, 'Last change of any element of the data at the persistent data store.\n\t\t\t\t\tThe change time is not updated for a growing object while it is growing.  ')

    
    # Element {http://www.witsml.org/schemas/131}itemState uses Python identifier itemState
    __itemState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'itemState'), 'itemState', '__httpwww_witsml_orgschemas131_cs_commonData_httpwww_witsml_orgschemas131itemState', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 42, 3), )

    
    itemState = property(__itemState.value, __itemState.set, None, 'The item state for the data object.  ')

    
    # Element {http://www.witsml.org/schemas/131}comments uses Python identifier comments
    __comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comments'), 'comments', '__httpwww_witsml_orgschemas131_cs_commonData_httpwww_witsml_orgschemas131comments', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 47, 3), )

    
    comments = property(__comments.value, __comments.set, None, 'Comments and remarks.  ')


    _ElementMap = {
        __sourceName.name() : __sourceName,
        __dTimCreation.name() : __dTimCreation,
        __dTimLastChange.name() : __dTimLastChange,
        __itemState.name() : __itemState,
        __comments.name() : __comments
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_commonData', cs_commonData)


# Complex type {http://www.witsml.org/schemas/131}cs_customData with content type ELEMENT_ONLY
class cs_customData (pyxb.binding.basis.complexTypeDefinition):
    """ WITSML - Custom or User Defined Element and Attributes Component Schema.
			Specify custom element, attributes, and types in the custom data area."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_customData')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_customData.xsd', 16, 1)
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_customData', cs_customData)


# Complex type {http://www.witsml.org/schemas/131}cs_documentInfo with content type ELEMENT_ONLY
class cs_documentInfo (pyxb.binding.basis.complexTypeDefinition):
    """A  schema to capture a set of data that is 
			relevant for many exchange documents. It includes information about the 
			file that was created, and high-level information about the data that is 
			being exchanged within the file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_documentInfo')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}DocumentName uses Python identifier DocumentName
    __DocumentName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DocumentName'), 'DocumentName', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131DocumentName', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 26, 3), )

    
    DocumentName = property(__DocumentName.value, __DocumentName.set, None, 'An identifier for the document. This is \n\t\t\t\t\tintended to be unique within the context of the NamingSystem.')

    
    # Element {http://www.witsml.org/schemas/131}DocumentAlias uses Python identifier DocumentAlias
    __DocumentAlias = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DocumentAlias'), 'DocumentAlias', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131DocumentAlias', True, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 32, 3), )

    
    DocumentAlias = property(__DocumentAlias.value, __DocumentAlias.set, None, 'Zero or more alternate names for the document. \n\t\t\t\t\tThese names do not need to be unique within the naming system.')

    
    # Element {http://www.witsml.org/schemas/131}DocumentDate uses Python identifier DocumentDate
    __DocumentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DocumentDate'), 'DocumentDate', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131DocumentDate', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 38, 3), )

    
    DocumentDate = property(__DocumentDate.value, __DocumentDate.set, None, 'The date of the creation of the document. \n\t\t\t\t\tThis is not the same as the date that the file was created. \n\t\t\t\t\tFor this date, the document is considered to be the set of \n\t\t\t\t\tinformation associated with this document information. \n\t\t\t\t\tFor example, the document may be a seismic binset. \n\t\t\t\t\tThis represents the date that the binset was created. \n\t\t\t\t\tThe FileCreation information would capture the date that \n\t\t\t\t\tthe XML file was created to send or exchange the binset.')

    
    # Element {http://www.witsml.org/schemas/131}documentClass uses Python identifier documentClass
    __documentClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentClass'), 'documentClass', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131documentClass', True, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 50, 3), )

    
    documentClass = property(__documentClass.value, __documentClass.set, None, 'A document class. Examples of classes would be a \n\t\t\t\t\tmetadata classification or a set of keywords. ')

    
    # Element {http://www.witsml.org/schemas/131}FileCreationInformation uses Python identifier FileCreationInformation
    __FileCreationInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FileCreationInformation'), 'FileCreationInformation', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131FileCreationInformation', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 56, 3), )

    
    FileCreationInformation = property(__FileCreationInformation.value, __FileCreationInformation.set, None, 'The information about the creation of the \n\t\t\t\t\texchange file. This is not about the creation of the data within \n\t\t\t\t\tthe file, but the creation of the file itself.')

    
    # Element {http://www.witsml.org/schemas/131}SecurityInformation uses Python identifier SecurityInformation
    __SecurityInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SecurityInformation'), 'SecurityInformation', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131SecurityInformation', True, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 63, 3), )

    
    SecurityInformation = property(__SecurityInformation.value, __SecurityInformation.set, None, 'Information about the security to be applied to \n\t\t\t\t\tthis file. More than one classification can be given.')

    
    # Element {http://www.witsml.org/schemas/131}Disclaimer uses Python identifier Disclaimer
    __Disclaimer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Disclaimer'), 'Disclaimer', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131Disclaimer', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 69, 3), )

    
    Disclaimer = property(__Disclaimer.value, __Disclaimer.set, None, 'A free-form string that allows a disclaimer to \n\t\t\t\t\taccompany the information.')

    
    # Element {http://www.witsml.org/schemas/131}AuditTrail uses Python identifier AuditTrail
    __AuditTrail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AuditTrail'), 'AuditTrail', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131AuditTrail', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 75, 3), )

    
    AuditTrail = property(__AuditTrail.value, __AuditTrail.set, None, 'A collection of events that can document the \n\t\t\t\t\thistory of the data.')

    
    # Element {http://www.witsml.org/schemas/131}Owner uses Python identifier Owner
    __Owner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Owner'), 'Owner', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131Owner', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 81, 3), )

    
    Owner = property(__Owner.value, __Owner.set, None, 'The owner of the data.')

    
    # Element {http://www.witsml.org/schemas/131}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Comment'), 'Comment', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131Comment', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 86, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, 'An optional comment about the document.')


    _ElementMap = {
        __DocumentName.name() : __DocumentName,
        __DocumentAlias.name() : __DocumentAlias,
        __DocumentDate.name() : __DocumentDate,
        __documentClass.name() : __documentClass,
        __FileCreationInformation.name() : __FileCreationInformation,
        __SecurityInformation.name() : __SecurityInformation,
        __Disclaimer.name() : __Disclaimer,
        __AuditTrail.name() : __AuditTrail,
        __Owner.name() : __Owner,
        __Comment.name() : __Comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'cs_documentInfo', cs_documentInfo)


# Complex type {http://www.witsml.org/schemas/131}fileCreationType with content type ELEMENT_ONLY
class fileCreationType (pyxb.binding.basis.complexTypeDefinition):
    """A block of information about the creation of the XML file. 
			This is different than the creation of the data that is included within the file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fileCreationType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 94, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}FileCreationDate uses Python identifier FileCreationDate
    __FileCreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FileCreationDate'), 'FileCreationDate', '__httpwww_witsml_orgschemas131_fileCreationType_httpwww_witsml_orgschemas131FileCreationDate', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 100, 3), )

    
    FileCreationDate = property(__FileCreationDate.value, __FileCreationDate.set, None, 'The date and time that the file was created.')

    
    # Element {http://www.witsml.org/schemas/131}SoftwareName uses Python identifier SoftwareName
    __SoftwareName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SoftwareName'), 'SoftwareName', '__httpwww_witsml_orgschemas131_fileCreationType_httpwww_witsml_orgschemas131SoftwareName', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 105, 3), )

    
    SoftwareName = property(__SoftwareName.value, __SoftwareName.set, None, 'If appropriate, the software that created the file. \n\t\t\t\t\tThis is a free form string, and may include whatever information \n\t\t\t\t\tis deemed relevant.')

    
    # Element {http://www.witsml.org/schemas/131}FileCreator uses Python identifier FileCreator
    __FileCreator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FileCreator'), 'FileCreator', '__httpwww_witsml_orgschemas131_fileCreationType_httpwww_witsml_orgschemas131FileCreator', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 112, 3), )

    
    FileCreator = property(__FileCreator.value, __FileCreator.set, None, 'The person or business associate that created \n\t\t\t\t\tthe file.')

    
    # Element {http://www.witsml.org/schemas/131}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Comment'), 'Comment', '__httpwww_witsml_orgschemas131_fileCreationType_httpwww_witsml_orgschemas131Comment', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 118, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, 'Any comment that would be useful to further \n\t\t\t\t\texplain the creation of this instance document.')


    _ElementMap = {
        __FileCreationDate.name() : __FileCreationDate,
        __SoftwareName.name() : __SoftwareName,
        __FileCreator.name() : __FileCreator,
        __Comment.name() : __Comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'fileCreationType', fileCreationType)


# Complex type {http://www.witsml.org/schemas/131}securityInfoType with content type ELEMENT_ONLY
class securityInfoType (pyxb.binding.basis.complexTypeDefinition):
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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'securityInfoType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 127, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Class'), 'Class', '__httpwww_witsml_orgschemas131_securityInfoType_httpwww_witsml_orgschemas131Class', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 138, 3), )

    
    Class = property(__Class.value, __Class.set, None, 'The security class in which this document is \n\t\t\t\t\tclassified. Examples would be confidential, partner confidential, \n\t\t\t\t\ttight. The meaning of the class is determined by the System in which \n\t\t\t\t\tit is defined.')

    
    # Element {http://www.witsml.org/schemas/131}System uses Python identifier System
    __System = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'System'), 'System', '__httpwww_witsml_orgschemas131_securityInfoType_httpwww_witsml_orgschemas131System', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 146, 3), )

    
    System = property(__System.value, __System.set, None, 'The security classification system. \n\t\t\t\t\tThis gives context to the meaning of the Class value.')

    
    # Element {http://www.witsml.org/schemas/131}EndDate uses Python identifier EndDate
    __EndDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndDate'), 'EndDate', '__httpwww_witsml_orgschemas131_securityInfoType_httpwww_witsml_orgschemas131EndDate', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 152, 3), )

    
    EndDate = property(__EndDate.value, __EndDate.set, None, 'The date on which this security class is no \n\t\t\t\t\tlonger applicable.')

    
    # Element {http://www.witsml.org/schemas/131}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Comment'), 'Comment', '__httpwww_witsml_orgschemas131_securityInfoType_httpwww_witsml_orgschemas131Comment', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 158, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, 'A general comment to further define the security \n\t\t\t\t\tclass.')


    _ElementMap = {
        __Class.name() : __Class,
        __System.name() : __System,
        __EndDate.name() : __EndDate,
        __Comment.name() : __Comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'securityInfoType', securityInfoType)


# Complex type {http://www.witsml.org/schemas/131}auditType with content type ELEMENT_ONLY
class auditType (pyxb.binding.basis.complexTypeDefinition):
    """The audit records what happened to the data, to produce 
			the data that is in this file. It consists of one or more events."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'auditType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 167, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}Event uses Python identifier Event
    __Event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Event'), 'Event', '__httpwww_witsml_orgschemas131_auditType_httpwww_witsml_orgschemas131Event', True, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 173, 3), )

    
    Event = property(__Event.value, __Event.set, None, None)


    _ElementMap = {
        __Event.name() : __Event
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'auditType', auditType)


# Complex type {http://www.witsml.org/schemas/131}eventType with content type ELEMENT_ONLY
class eventType (pyxb.binding.basis.complexTypeDefinition):
    """An event type captures the basic information about an 
			event that has affected the data."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'eventType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 177, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}EventDate uses Python identifier EventDate
    __EventDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EventDate'), 'EventDate', '__httpwww_witsml_orgschemas131_eventType_httpwww_witsml_orgschemas131EventDate', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 183, 3), )

    
    EventDate = property(__EventDate.value, __EventDate.set, None, 'The date on which the event took place.')

    
    # Element {http://www.witsml.org/schemas/131}ResponsibleParty uses Python identifier ResponsibleParty
    __ResponsibleParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponsibleParty'), 'ResponsibleParty', '__httpwww_witsml_orgschemas131_eventType_httpwww_witsml_orgschemas131ResponsibleParty', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 188, 3), )

    
    ResponsibleParty = property(__ResponsibleParty.value, __ResponsibleParty.set, None, 'The party responsible for the event.')

    
    # Element {http://www.witsml.org/schemas/131}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Comment'), 'Comment', '__httpwww_witsml_orgschemas131_eventType_httpwww_witsml_orgschemas131Comment', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 193, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, 'A free form comment that can further \n\t\t\t\t\tdefine the event that occurred.')


    _ElementMap = {
        __EventDate.name() : __EventDate,
        __ResponsibleParty.name() : __ResponsibleParty,
        __Comment.name() : __Comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'eventType', eventType)


# Complex type {http://www.witsml.org/schemas/131}abstractMeasure with content type SIMPLE
class abstractMeasure (pyxb.binding.basis.complexTypeDefinition):
    """The intended abstract supertype of all quantities that have a value 
			with a unit of measure. The unit of measure is in the uom attribute of the subtypes. 
			This type allows all quantities to be profiled to be a 'float' instead of a 'double'."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 118, 1)
    # Base type is abstractDouble

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', 'abstractMeasure', abstractMeasure)


# Complex type {http://www.witsml.org/schemas/131}obj_bhaRuns with content type ELEMENT_ONLY
class obj_bhaRuns (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/schemas/131}obj_bhaRuns with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'obj_bhaRuns')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 33, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}documentInfo uses Python identifier documentInfo
    __documentInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentInfo'), 'documentInfo', '__httpwww_witsml_orgschemas131_obj_bhaRuns_httpwww_witsml_orgschemas131documentInfo', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 35, 3), )

    
    documentInfo = property(__documentInfo.value, __documentInfo.set, None, 'Information about the XML message instance.  ')

    
    # Element {http://www.witsml.org/schemas/131}bhaRun uses Python identifier bhaRun
    __bhaRun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bhaRun'), 'bhaRun', '__httpwww_witsml_orgschemas131_obj_bhaRuns_httpwww_witsml_orgschemas131bhaRun', True, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 40, 3), )

    
    bhaRun = property(__bhaRun.value, __bhaRun.set, None, 'A single bottom hole assembly run.  ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_witsml_orgschemas131_obj_bhaRuns_version', schemaVersionString, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 46, 2)
    __version._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 46, 2)
    
    version = property(__version.value, __version.set, None, 'Data object schema version.  The fourth level must match the \n\t\t\t\tversion of the schema constraints (enumerations and XML loader files) that are assumed\n\t\t\t\tby the document instance.')


    _ElementMap = {
        __documentInfo.name() : __documentInfo,
        __bhaRun.name() : __bhaRun
    }
    _AttributeMap = {
        __version.name() : __version
    }
Namespace.addCategoryObject('typeBinding', 'obj_bhaRuns', obj_bhaRuns)


# Complex type {http://www.witsml.org/schemas/131}indexCurve with content type SIMPLE
class indexCurve (pyxb.binding.basis.complexTypeDefinition):
    """The mnemonic of a log index curve plus 
			the column index of the curve."""
    _TypeDefinition = str32
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'indexCurve')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 171, 1)
    # Base type is str32
    
    # Attribute columnIndex uses Python identifier columnIndex
    __columnIndex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'columnIndex'), 'columnIndex', '__httpwww_witsml_orgschemas131_indexCurve_columnIndex', nonNegativeCount, required=True)
    __columnIndex._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 178, 4)
    __columnIndex._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 178, 4)
    
    columnIndex = property(__columnIndex.value, __columnIndex.set, None, 'The column index of the curve.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __columnIndex.name() : __columnIndex
    }
Namespace.addCategoryObject('typeBinding', 'indexCurve', indexCurve)


# Complex type {http://www.witsml.org/schemas/131}cs_drillingParams with content type ELEMENT_ONLY
class cs_drillingParams (pyxb.binding.basis.complexTypeDefinition):
    """ WITSML - Bottom hole assembly drilling parameters component schema """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cs_drillingParams')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 19, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}eTimOpBit uses Python identifier eTimOpBit
    __eTimOpBit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eTimOpBit'), 'eTimOpBit', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131eTimOpBit', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 24, 3), )

    
    eTimOpBit = property(__eTimOpBit.value, __eTimOpBit.set, None, 'Operating time spent by bit for run.  ')

    
    # Element {http://www.witsml.org/schemas/131}mdHoleStart uses Python identifier mdHoleStart
    __mdHoleStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mdHoleStart'), 'mdHoleStart', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131mdHoleStart', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 29, 3), )

    
    mdHoleStart = property(__mdHoleStart.value, __mdHoleStart.set, None, 'Measured depth at start.  ')

    
    # Element {http://www.witsml.org/schemas/131}mdHoleStop uses Python identifier mdHoleStop
    __mdHoleStop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mdHoleStop'), 'mdHoleStop', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131mdHoleStop', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 34, 3), )

    
    mdHoleStop = property(__mdHoleStop.value, __mdHoleStop.set, None, 'Measured depth at stop.  ')

    
    # Element {http://www.witsml.org/schemas/131}tubular uses Python identifier tubular
    __tubular = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tubular'), 'tubular', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131tubular', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 39, 3), )

    
    tubular = property(__tubular.value, __tubular.set, None, 'A pointer to the tubular assembly.  ')

    
    # Element {http://www.witsml.org/schemas/131}hkldRot uses Python identifier hkldRot
    __hkldRot = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hkldRot'), 'hkldRot', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131hkldRot', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 44, 3), )

    
    hkldRot = property(__hkldRot.value, __hkldRot.set, None, 'Hookload - rotating.  ')

    
    # Element {http://www.witsml.org/schemas/131}overPull uses Python identifier overPull
    __overPull = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'overPull'), 'overPull', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131overPull', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 49, 3), )

    
    overPull = property(__overPull.value, __overPull.set, None, 'hkldUp-hkldRot.  ')

    
    # Element {http://www.witsml.org/schemas/131}slackOff uses Python identifier slackOff
    __slackOff = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'slackOff'), 'slackOff', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131slackOff', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 54, 3), )

    
    slackOff = property(__slackOff.value, __slackOff.set, None, 'hkldRot-hkldDown.  ')

    
    # Element {http://www.witsml.org/schemas/131}hkldUp uses Python identifier hkldUp
    __hkldUp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hkldUp'), 'hkldUp', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131hkldUp', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 59, 3), )

    
    hkldUp = property(__hkldUp.value, __hkldUp.set, None, 'Hookload - string moving up.  ')

    
    # Element {http://www.witsml.org/schemas/131}hkldDn uses Python identifier hkldDn
    __hkldDn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hkldDn'), 'hkldDn', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131hkldDn', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 64, 3), )

    
    hkldDn = property(__hkldDn.value, __hkldDn.set, None, 'Hookload - string moving down.  ')

    
    # Element {http://www.witsml.org/schemas/131}tqOnBotAv uses Python identifier tqOnBotAv
    __tqOnBotAv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tqOnBotAv'), 'tqOnBotAv', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131tqOnBotAv', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 69, 3), )

    
    tqOnBotAv = property(__tqOnBotAv.value, __tqOnBotAv.set, None, 'Average Torque - on bottom.  ')

    
    # Element {http://www.witsml.org/schemas/131}tqOnBotMx uses Python identifier tqOnBotMx
    __tqOnBotMx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tqOnBotMx'), 'tqOnBotMx', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131tqOnBotMx', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 74, 3), )

    
    tqOnBotMx = property(__tqOnBotMx.value, __tqOnBotMx.set, None, 'Maximum torque - on bottom.  ')

    
    # Element {http://www.witsml.org/schemas/131}tqOnBotMn uses Python identifier tqOnBotMn
    __tqOnBotMn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tqOnBotMn'), 'tqOnBotMn', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131tqOnBotMn', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 79, 3), )

    
    tqOnBotMn = property(__tqOnBotMn.value, __tqOnBotMn.set, None, 'Minimum torque - on bottom.  ')

    
    # Element {http://www.witsml.org/schemas/131}tqOffBotAv uses Python identifier tqOffBotAv
    __tqOffBotAv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tqOffBotAv'), 'tqOffBotAv', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131tqOffBotAv', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 84, 3), )

    
    tqOffBotAv = property(__tqOffBotAv.value, __tqOffBotAv.set, None, 'Average torque - off bottom.  ')

    
    # Element {http://www.witsml.org/schemas/131}tqDhAv uses Python identifier tqDhAv
    __tqDhAv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tqDhAv'), 'tqDhAv', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131tqDhAv', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 89, 3), )

    
    tqDhAv = property(__tqDhAv.value, __tqDhAv.set, None, 'Average torque - downhole.  ')

    
    # Element {http://www.witsml.org/schemas/131}wtAboveJar uses Python identifier wtAboveJar
    __wtAboveJar = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wtAboveJar'), 'wtAboveJar', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131wtAboveJar', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 94, 3), )

    
    wtAboveJar = property(__wtAboveJar.value, __wtAboveJar.set, None, 'Weight above jars.  ')

    
    # Element {http://www.witsml.org/schemas/131}wtBelowJar uses Python identifier wtBelowJar
    __wtBelowJar = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wtBelowJar'), 'wtBelowJar', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131wtBelowJar', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 99, 3), )

    
    wtBelowJar = property(__wtBelowJar.value, __wtBelowJar.set, None, 'Weight below jars.  ')

    
    # Element {http://www.witsml.org/schemas/131}wtMud uses Python identifier wtMud
    __wtMud = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wtMud'), 'wtMud', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131wtMud', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 104, 3), )

    
    wtMud = property(__wtMud.value, __wtMud.set, None, 'Mud density.  ')

    
    # Element {http://www.witsml.org/schemas/131}flowratePump uses Python identifier flowratePump
    __flowratePump = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flowratePump'), 'flowratePump', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131flowratePump', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 109, 3), )

    
    flowratePump = property(__flowratePump.value, __flowratePump.set, None, 'Pump flow rate.  ')

    
    # Element {http://www.witsml.org/schemas/131}powBit uses Python identifier powBit
    __powBit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'powBit'), 'powBit', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131powBit', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 114, 3), )

    
    powBit = property(__powBit.value, __powBit.set, None, 'Bit hydraulic.  ')

    
    # Element {http://www.witsml.org/schemas/131}velNozzleAv uses Python identifier velNozzleAv
    __velNozzleAv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'velNozzleAv'), 'velNozzleAv', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131velNozzleAv', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 119, 3), )

    
    velNozzleAv = property(__velNozzleAv.value, __velNozzleAv.set, None, 'Bit nozzle average velocity.  ')

    
    # Element {http://www.witsml.org/schemas/131}presDropBit uses Python identifier presDropBit
    __presDropBit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'presDropBit'), 'presDropBit', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131presDropBit', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 124, 3), )

    
    presDropBit = property(__presDropBit.value, __presDropBit.set, None, 'Pressure drop in bit.  ')

    
    # Element {http://www.witsml.org/schemas/131}cTimHold uses Python identifier cTimHold
    __cTimHold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cTimHold'), 'cTimHold', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131cTimHold', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 129, 3), )

    
    cTimHold = property(__cTimHold.value, __cTimHold.set, None, 'Time spent on hold from start of bit run.  ')

    
    # Element {http://www.witsml.org/schemas/131}cTimSteering uses Python identifier cTimSteering
    __cTimSteering = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cTimSteering'), 'cTimSteering', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131cTimSteering', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 134, 3), )

    
    cTimSteering = property(__cTimSteering.value, __cTimSteering.set, None, 'Time spent steering from start of bit run.  ')

    
    # Element {http://www.witsml.org/schemas/131}cTimDrillRot uses Python identifier cTimDrillRot
    __cTimDrillRot = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cTimDrillRot'), 'cTimDrillRot', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131cTimDrillRot', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 139, 3), )

    
    cTimDrillRot = property(__cTimDrillRot.value, __cTimDrillRot.set, None, 'Time spent rotary drilling from start of bit run.  ')

    
    # Element {http://www.witsml.org/schemas/131}cTimDrillSlid uses Python identifier cTimDrillSlid
    __cTimDrillSlid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cTimDrillSlid'), 'cTimDrillSlid', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131cTimDrillSlid', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 144, 3), )

    
    cTimDrillSlid = property(__cTimDrillSlid.value, __cTimDrillSlid.set, None, 'Time spent slide drilling from start of bit run.  ')

    
    # Element {http://www.witsml.org/schemas/131}cTimCirc uses Python identifier cTimCirc
    __cTimCirc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cTimCirc'), 'cTimCirc', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131cTimCirc', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 149, 3), )

    
    cTimCirc = property(__cTimCirc.value, __cTimCirc.set, None, 'Time spent circulating from start of bit run.  ')

    
    # Element {http://www.witsml.org/schemas/131}cTimReam uses Python identifier cTimReam
    __cTimReam = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cTimReam'), 'cTimReam', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131cTimReam', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 154, 3), )

    
    cTimReam = property(__cTimReam.value, __cTimReam.set, None, 'Time spent reaming from start of bit run.  ')

    
    # Element {http://www.witsml.org/schemas/131}distDrillRot uses Python identifier distDrillRot
    __distDrillRot = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'distDrillRot'), 'distDrillRot', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131distDrillRot', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 159, 3), )

    
    distDrillRot = property(__distDrillRot.value, __distDrillRot.set, None, 'Distance drilled - rotating.  ')

    
    # Element {http://www.witsml.org/schemas/131}distDrillSlid uses Python identifier distDrillSlid
    __distDrillSlid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'distDrillSlid'), 'distDrillSlid', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131distDrillSlid', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 164, 3), )

    
    distDrillSlid = property(__distDrillSlid.value, __distDrillSlid.set, None, 'Distance drilled - sliding  ')

    
    # Element {http://www.witsml.org/schemas/131}distReam uses Python identifier distReam
    __distReam = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'distReam'), 'distReam', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131distReam', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 169, 3), )

    
    distReam = property(__distReam.value, __distReam.set, None, 'Distance reamed.  ')

    
    # Element {http://www.witsml.org/schemas/131}distHold uses Python identifier distHold
    __distHold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'distHold'), 'distHold', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131distHold', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 174, 3), )

    
    distHold = property(__distHold.value, __distHold.set, None, 'Distance covered while holding angle with a steerable drilling assembly.  ')

    
    # Element {http://www.witsml.org/schemas/131}distSteering uses Python identifier distSteering
    __distSteering = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'distSteering'), 'distSteering', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131distSteering', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 179, 3), )

    
    distSteering = property(__distSteering.value, __distSteering.set, None, 'Distance covered while actively steering with a steerable drilling assembly.  ')

    
    # Element {http://www.witsml.org/schemas/131}rpmAv uses Python identifier rpmAv
    __rpmAv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rpmAv'), 'rpmAv', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131rpmAv', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 184, 3), )

    
    rpmAv = property(__rpmAv.value, __rpmAv.set, None, 'Average turn rate (commonly in rpm) through Interval.  ')

    
    # Element {http://www.witsml.org/schemas/131}rpmMx uses Python identifier rpmMx
    __rpmMx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rpmMx'), 'rpmMx', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131rpmMx', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 189, 3), )

    
    rpmMx = property(__rpmMx.value, __rpmMx.set, None, 'Maximum turn rate (commonly in rpm).  ')

    
    # Element {http://www.witsml.org/schemas/131}rpmMn uses Python identifier rpmMn
    __rpmMn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rpmMn'), 'rpmMn', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131rpmMn', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 194, 3), )

    
    rpmMn = property(__rpmMn.value, __rpmMn.set, None, 'Minimum turn rate (commonly in rpm).  ')

    
    # Element {http://www.witsml.org/schemas/131}rpmAvDh uses Python identifier rpmAvDh
    __rpmAvDh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rpmAvDh'), 'rpmAvDh', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131rpmAvDh', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 199, 3), )

    
    rpmAvDh = property(__rpmAvDh.value, __rpmAvDh.set, None, 'Average turn rate (commonly in rpm) downhole.  ')

    
    # Element {http://www.witsml.org/schemas/131}ropAv uses Python identifier ropAv
    __ropAv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ropAv'), 'ropAv', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131ropAv', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 204, 3), )

    
    ropAv = property(__ropAv.value, __ropAv.set, None, 'Average rate of penetration through Interval.  ')

    
    # Element {http://www.witsml.org/schemas/131}ropMx uses Python identifier ropMx
    __ropMx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ropMx'), 'ropMx', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131ropMx', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 209, 3), )

    
    ropMx = property(__ropMx.value, __ropMx.set, None, 'Maximum rate of penetration through Interval.  ')

    
    # Element {http://www.witsml.org/schemas/131}ropMn uses Python identifier ropMn
    __ropMn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ropMn'), 'ropMn', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131ropMn', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 214, 3), )

    
    ropMn = property(__ropMn.value, __ropMn.set, None, 'Minimum rate of penetration through Interval.  ')

    
    # Element {http://www.witsml.org/schemas/131}wobAv uses Python identifier wobAv
    __wobAv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wobAv'), 'wobAv', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131wobAv', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 219, 3), )

    
    wobAv = property(__wobAv.value, __wobAv.set, None, 'Surface weight on bit - average through interval.  ')

    
    # Element {http://www.witsml.org/schemas/131}wobMx uses Python identifier wobMx
    __wobMx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wobMx'), 'wobMx', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131wobMx', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 224, 3), )

    
    wobMx = property(__wobMx.value, __wobMx.set, None, 'Weight on bit - maximum.  ')

    
    # Element {http://www.witsml.org/schemas/131}wobMn uses Python identifier wobMn
    __wobMn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wobMn'), 'wobMn', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131wobMn', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 229, 3), )

    
    wobMn = property(__wobMn.value, __wobMn.set, None, 'Weight on bit - minimum.  ')

    
    # Element {http://www.witsml.org/schemas/131}wobAvDh uses Python identifier wobAvDh
    __wobAvDh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wobAvDh'), 'wobAvDh', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131wobAvDh', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 234, 3), )

    
    wobAvDh = property(__wobAvDh.value, __wobAvDh.set, None, 'Weight on bit - average downhole.  ')

    
    # Element {http://www.witsml.org/schemas/131}reasonTrip uses Python identifier reasonTrip
    __reasonTrip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reasonTrip'), 'reasonTrip', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131reasonTrip', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 239, 3), )

    
    reasonTrip = property(__reasonTrip.value, __reasonTrip.set, None, 'Reason for trip.  ')

    
    # Element {http://www.witsml.org/schemas/131}objectiveBha uses Python identifier objectiveBha
    __objectiveBha = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectiveBha'), 'objectiveBha', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131objectiveBha', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 244, 3), )

    
    objectiveBha = property(__objectiveBha.value, __objectiveBha.set, None, 'Objective of bottom hole assembly.  ')

    
    # Element {http://www.witsml.org/schemas/131}aziTop uses Python identifier aziTop
    __aziTop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aziTop'), 'aziTop', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131aziTop', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 249, 3), )

    
    aziTop = property(__aziTop.value, __aziTop.set, None, 'Azimuth at start measured depth.  ')

    
    # Element {http://www.witsml.org/schemas/131}aziBottom uses Python identifier aziBottom
    __aziBottom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aziBottom'), 'aziBottom', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131aziBottom', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 254, 3), )

    
    aziBottom = property(__aziBottom.value, __aziBottom.set, None, 'Azimuth at stop measured depth.  ')

    
    # Element {http://www.witsml.org/schemas/131}inclStart uses Python identifier inclStart
    __inclStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inclStart'), 'inclStart', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131inclStart', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 259, 3), )

    
    inclStart = property(__inclStart.value, __inclStart.set, None, 'Inclination at start measured depth.  ')

    
    # Element {http://www.witsml.org/schemas/131}inclMx uses Python identifier inclMx
    __inclMx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inclMx'), 'inclMx', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131inclMx', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 264, 3), )

    
    inclMx = property(__inclMx.value, __inclMx.set, None, 'Maximum inclination.  ')

    
    # Element {http://www.witsml.org/schemas/131}inclMn uses Python identifier inclMn
    __inclMn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inclMn'), 'inclMn', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131inclMn', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 269, 3), )

    
    inclMn = property(__inclMn.value, __inclMn.set, None, 'Minimum inclination.  ')

    
    # Element {http://www.witsml.org/schemas/131}inclStop uses Python identifier inclStop
    __inclStop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inclStop'), 'inclStop', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131inclStop', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 274, 3), )

    
    inclStop = property(__inclStop.value, __inclStop.set, None, 'Inclination at stop measured depth.  ')

    
    # Element {http://www.witsml.org/schemas/131}tempMudDhMx uses Python identifier tempMudDhMx
    __tempMudDhMx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tempMudDhMx'), 'tempMudDhMx', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131tempMudDhMx', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 279, 3), )

    
    tempMudDhMx = property(__tempMudDhMx.value, __tempMudDhMx.set, None, 'Maximum mud temperature downhole during run.  ')

    
    # Element {http://www.witsml.org/schemas/131}presPumpAv uses Python identifier presPumpAv
    __presPumpAv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'presPumpAv'), 'presPumpAv', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131presPumpAv', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 284, 3), )

    
    presPumpAv = property(__presPumpAv.value, __presPumpAv.set, None, 'Average pump pressure.  ')

    
    # Element {http://www.witsml.org/schemas/131}flowrateBit uses Python identifier flowrateBit
    __flowrateBit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flowrateBit'), 'flowrateBit', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131flowrateBit', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 289, 3), )

    
    flowrateBit = property(__flowrateBit.value, __flowrateBit.set, None, 'Flow rate at bit.  ')

    
    # Element {http://www.witsml.org/schemas/131}comments uses Python identifier comments
    __comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comments'), 'comments', '__httpwww_witsml_orgschemas131_cs_drillingParams_httpwww_witsml_orgschemas131comments', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 294, 3), )

    
    comments = property(__comments.value, __comments.set, None, 'Comments and remarks.  ')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas131_cs_drillingParams_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\attgrp_uid.xsd', 20, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\attgrp_uid.xsd', 20, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


    _ElementMap = {
        __eTimOpBit.name() : __eTimOpBit,
        __mdHoleStart.name() : __mdHoleStart,
        __mdHoleStop.name() : __mdHoleStop,
        __tubular.name() : __tubular,
        __hkldRot.name() : __hkldRot,
        __overPull.name() : __overPull,
        __slackOff.name() : __slackOff,
        __hkldUp.name() : __hkldUp,
        __hkldDn.name() : __hkldDn,
        __tqOnBotAv.name() : __tqOnBotAv,
        __tqOnBotMx.name() : __tqOnBotMx,
        __tqOnBotMn.name() : __tqOnBotMn,
        __tqOffBotAv.name() : __tqOffBotAv,
        __tqDhAv.name() : __tqDhAv,
        __wtAboveJar.name() : __wtAboveJar,
        __wtBelowJar.name() : __wtBelowJar,
        __wtMud.name() : __wtMud,
        __flowratePump.name() : __flowratePump,
        __powBit.name() : __powBit,
        __velNozzleAv.name() : __velNozzleAv,
        __presDropBit.name() : __presDropBit,
        __cTimHold.name() : __cTimHold,
        __cTimSteering.name() : __cTimSteering,
        __cTimDrillRot.name() : __cTimDrillRot,
        __cTimDrillSlid.name() : __cTimDrillSlid,
        __cTimCirc.name() : __cTimCirc,
        __cTimReam.name() : __cTimReam,
        __distDrillRot.name() : __distDrillRot,
        __distDrillSlid.name() : __distDrillSlid,
        __distReam.name() : __distReam,
        __distHold.name() : __distHold,
        __distSteering.name() : __distSteering,
        __rpmAv.name() : __rpmAv,
        __rpmMx.name() : __rpmMx,
        __rpmMn.name() : __rpmMn,
        __rpmAvDh.name() : __rpmAvDh,
        __ropAv.name() : __ropAv,
        __ropMx.name() : __ropMx,
        __ropMn.name() : __ropMn,
        __wobAv.name() : __wobAv,
        __wobMx.name() : __wobMx,
        __wobMn.name() : __wobMn,
        __wobAvDh.name() : __wobAvDh,
        __reasonTrip.name() : __reasonTrip,
        __objectiveBha.name() : __objectiveBha,
        __aziTop.name() : __aziTop,
        __aziBottom.name() : __aziBottom,
        __inclStart.name() : __inclStart,
        __inclMx.name() : __inclMx,
        __inclMn.name() : __inclMn,
        __inclStop.name() : __inclStop,
        __tempMudDhMx.name() : __tempMudDhMx,
        __presPumpAv.name() : __presPumpAv,
        __flowrateBit.name() : __flowrateBit,
        __comments.name() : __comments
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', 'cs_drillingParams', cs_drillingParams)


# Complex type {http://www.witsml.org/schemas/131}obj_bhaRun with content type ELEMENT_ONLY
class obj_bhaRun (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/schemas/131}obj_bhaRun with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'obj_bhaRun')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 55, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}tubular uses Python identifier tubular
    __tubular = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tubular'), 'tubular', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131tubular', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 24, 3), )

    
    tubular = property(__tubular.value, __tubular.set, None, 'This represents a foreign key to the tubular (assembly) \n\t\t\t\t\tthat was utilized in this run.')

    
    # Element {http://www.witsml.org/schemas/131}dTimStart uses Python identifier dTimStart
    __dTimStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dTimStart'), 'dTimStart', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131dTimStart', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 30, 3), )

    
    dTimStart = property(__dTimStart.value, __dTimStart.set, None, 'Date and time that activities started.  ')

    
    # Element {http://www.witsml.org/schemas/131}dTimStop uses Python identifier dTimStop
    __dTimStop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dTimStop'), 'dTimStop', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131dTimStop', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 35, 3), )

    
    dTimStop = property(__dTimStop.value, __dTimStop.set, None, 'Date and time that activities stopped.  ')

    
    # Element {http://www.witsml.org/schemas/131}dTimStartDrilling uses Python identifier dTimStartDrilling
    __dTimStartDrilling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dTimStartDrilling'), 'dTimStartDrilling', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131dTimStartDrilling', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 40, 3), )

    
    dTimStartDrilling = property(__dTimStartDrilling.value, __dTimStartDrilling.set, None, 'Start on bottom - date and time.  ')

    
    # Element {http://www.witsml.org/schemas/131}dTimStopDrilling uses Python identifier dTimStopDrilling
    __dTimStopDrilling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dTimStopDrilling'), 'dTimStopDrilling', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131dTimStopDrilling', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 45, 3), )

    
    dTimStopDrilling = property(__dTimStopDrilling.value, __dTimStopDrilling.set, None, 'Start off bottom - date and time.  ')

    
    # Element {http://www.witsml.org/schemas/131}planDogleg uses Python identifier planDogleg
    __planDogleg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'planDogleg'), 'planDogleg', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131planDogleg', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 50, 3), )

    
    planDogleg = property(__planDogleg.value, __planDogleg.set, None, 'Planned dogleg severity.  ')

    
    # Element {http://www.witsml.org/schemas/131}actDogleg uses Python identifier actDogleg
    __actDogleg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actDogleg'), 'actDogleg', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131actDogleg', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 55, 3), )

    
    actDogleg = property(__actDogleg.value, __actDogleg.set, None, 'Actual dogleg severity.  ')

    
    # Element {http://www.witsml.org/schemas/131}actDoglegMx uses Python identifier actDoglegMx
    __actDoglegMx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actDoglegMx'), 'actDoglegMx', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131actDoglegMx', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 60, 3), )

    
    actDoglegMx = property(__actDoglegMx.value, __actDoglegMx.set, None, 'Actual dogleg severity - Maximum.  ')

    
    # Element {http://www.witsml.org/schemas/131}statusBha uses Python identifier statusBha
    __statusBha = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'statusBha'), 'statusBha', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131statusBha', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 65, 3), )

    
    statusBha = property(__statusBha.value, __statusBha.set, None, 'Bottom hole assembly status.')

    
    # Element {http://www.witsml.org/schemas/131}numBitRun uses Python identifier numBitRun
    __numBitRun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'numBitRun'), 'numBitRun', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131numBitRun', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 70, 3), )

    
    numBitRun = property(__numBitRun.value, __numBitRun.set, None, 'Bit run number.  ')

    
    # Element {http://www.witsml.org/schemas/131}numStringRun uses Python identifier numStringRun
    __numStringRun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'numStringRun'), 'numStringRun', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131numStringRun', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 75, 3), )

    
    numStringRun = property(__numStringRun.value, __numStringRun.set, None, 'The BHA (drilling string) run number. ')

    
    # Element {http://www.witsml.org/schemas/131}reasonTrip uses Python identifier reasonTrip
    __reasonTrip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reasonTrip'), 'reasonTrip', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131reasonTrip', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 80, 3), )

    
    reasonTrip = property(__reasonTrip.value, __reasonTrip.set, None, 'Reason for trip.  ')

    
    # Element {http://www.witsml.org/schemas/131}objectiveBha uses Python identifier objectiveBha
    __objectiveBha = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectiveBha'), 'objectiveBha', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131objectiveBha', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 85, 3), )

    
    objectiveBha = property(__objectiveBha.value, __objectiveBha.set, None, 'Objective of bottom hole assembly.  ')

    
    # Element {http://www.witsml.org/schemas/131}drillingParams uses Python identifier drillingParams
    __drillingParams = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'drillingParams'), 'drillingParams', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131drillingParams', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 90, 3), )

    
    drillingParams = property(__drillingParams.value, __drillingParams.set, None, 'Drilling parameters.  ')

    
    # Element {http://www.witsml.org/schemas/131}nameWell uses Python identifier nameWell
    __nameWell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameWell'), 'nameWell', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131nameWell', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 57, 3), )

    
    nameWell = property(__nameWell.value, __nameWell.set, None, 'Human recognizable context for the well that contains the wellbore.  ')

    
    # Element {http://www.witsml.org/schemas/131}nameWellbore uses Python identifier nameWellbore
    __nameWellbore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameWellbore'), 'nameWellbore', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131nameWellbore', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 62, 3), )

    
    nameWellbore = property(__nameWellbore.value, __nameWellbore.set, None, 'Human recognizable context for the wellbore that contains the bottom hole assembly. ')

    
    # Element {http://www.witsml.org/schemas/131}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131name', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 67, 3), )

    
    name = property(__name.value, __name.set, None, 'Human recognizable context for the run.  ')

    
    # Element {http://www.witsml.org/schemas/131}commonData uses Python identifier commonData
    __commonData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'commonData'), 'commonData', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131commonData', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 77, 3), )

    
    commonData = property(__commonData.value, __commonData.set, None, 'A container element that contains elements that are common to all data \n\t\t\t\t\tobjects.  ')

    
    # Element {http://www.witsml.org/schemas/131}customData uses Python identifier customData
    __customData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customData'), 'customData', '__httpwww_witsml_orgschemas131_obj_bhaRun_httpwww_witsml_orgschemas131customData', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 83, 3), )

    
    customData = property(__customData.value, __customData.set, None, 'A container element that can contain custom or user defined \n\t\t\t\t\tdata elements.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_witsml_orgschemas131_obj_bhaRun_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\attgrp_uid.xsd', 20, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\attgrp_uid.xsd', 20, 2)
    
    uid = property(__uid.value, __uid.set, None, 'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')

    
    # Attribute uidWell uses Python identifier uidWell
    __uidWell = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uidWell'), 'uidWell', '__httpwww_witsml_orgschemas131_obj_bhaRun_uidWell', uidString)
    __uidWell._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 90, 2)
    __uidWell._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 90, 2)
    
    uidWell = property(__uidWell.value, __uidWell.set, None, 'Unique identifier for the well. This uniquely represents \n\t\t\t\tthe well referenced by the (possibly non-unique) nameWell. ')

    
    # Attribute uidWellbore uses Python identifier uidWellbore
    __uidWellbore = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uidWellbore'), 'uidWellbore', '__httpwww_witsml_orgschemas131_obj_bhaRun_uidWellbore', uidString)
    __uidWellbore._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 96, 2)
    __uidWellbore._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 96, 2)
    
    uidWellbore = property(__uidWellbore.value, __uidWellbore.set, None, 'Unique identifier for the wellbore.  This uniquely represents \n\t\t\t\tthe wellbore referenced by the (possibly non-unique) nameWellbore.  ')


    _ElementMap = {
        __tubular.name() : __tubular,
        __dTimStart.name() : __dTimStart,
        __dTimStop.name() : __dTimStop,
        __dTimStartDrilling.name() : __dTimStartDrilling,
        __dTimStopDrilling.name() : __dTimStopDrilling,
        __planDogleg.name() : __planDogleg,
        __actDogleg.name() : __actDogleg,
        __actDoglegMx.name() : __actDoglegMx,
        __statusBha.name() : __statusBha,
        __numBitRun.name() : __numBitRun,
        __numStringRun.name() : __numStringRun,
        __reasonTrip.name() : __reasonTrip,
        __objectiveBha.name() : __objectiveBha,
        __drillingParams.name() : __drillingParams,
        __nameWell.name() : __nameWell,
        __nameWellbore.name() : __nameWellbore,
        __name.name() : __name,
        __commonData.name() : __commonData,
        __customData.name() : __customData
    }
    _AttributeMap = {
        __uid.name() : __uid,
        __uidWell.name() : __uidWell,
        __uidWellbore.name() : __uidWellbore
    }
Namespace.addCategoryObject('typeBinding', 'obj_bhaRun', obj_bhaRun)


# Complex type {http://www.witsml.org/schemas/131}generalMeasureType with content type SIMPLE
class generalMeasureType (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}generalMeasureType with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'generalMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 27, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_generalMeasureType_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 30, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 30, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'generalMeasureType', generalMeasureType)


# Complex type {http://www.witsml.org/schemas/131}temperatureSlopeMeasure with content type SIMPLE
class temperatureSlopeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}temperatureSlopeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'temperatureSlopeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 35, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_temperatureSlopeMeasure_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 38, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 38, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'temperatureSlopeMeasure', temperatureSlopeMeasure)


# Complex type {http://www.witsml.org/schemas/131}typeOptionalClassString with content type SIMPLE
class typeOptionalClassString (pyxb.binding.basis.complexTypeDefinition):
    """A type with a classType attribute. This allows a user to give a 
			classification of something, and to specify the type of classification that it is. 
			There is no control over the class values, or the class types."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeOptionalClassString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 43, 1)
    # Base type is abstractNameString
    
    # Attribute classType uses Python identifier classType
    __classType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'classType'), 'classType', '__httpwww_witsml_orgschemas131_typeOptionalClassString_classType', kindString)
    __classType._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 51, 4)
    __classType._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 51, 4)
    
    classType = property(__classType.value, __classType.set, None, 'This identifies the classification system to \n\t\t\t\t\t\twhich the class belongs. ')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __classType.name() : __classType
    }
Namespace.addCategoryObject('typeBinding', 'typeOptionalClassString', typeOptionalClassString)


# Complex type {http://www.witsml.org/schemas/131}yAxisAzimuth with content type SIMPLE
class yAxisAzimuth (abstractMeasure):
    """The angle of a Y axis from North.
			This is a variation of planeAngleMeasure with an 
			attribute defining the direction of north."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'yAxisAzimuth')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 106, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_yAxisAzimuth_uom', planeAngleUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 114, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 114, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure of the azimuth value.')

    
    # Attribute northDirection uses Python identifier northDirection
    __northDirection = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'northDirection'), 'northDirection', '__httpwww_witsml_orgschemas131_yAxisAzimuth_northDirection', AziRef)
    __northDirection._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 119, 4)
    __northDirection._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 119, 4)
    
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


# Complex type {http://www.witsml.org/schemas/131}volumePerVolumeMeasurePercent with content type SIMPLE
class volumePerVolumeMeasurePercent (abstractMeasure):
    """A volume per volume measure that is constrained to a unit of percent."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumePerVolumeMeasurePercent')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 128, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_volumePerVolumeMeasurePercent_uom', PercentUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 134, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 134, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'volumePerVolumeMeasurePercent', volumePerVolumeMeasurePercent)


# Complex type {http://www.witsml.org/schemas/131}genericMeasure with content type SIMPLE
class genericMeasure (abstractMeasure):
    """A generic measure type.
			This should not be used except in situations where the underlying class of data is 
			captured elsewhere. For example, for a log curve."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genericMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 153, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_genericMeasure_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 161, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 161, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure for the quantity.\n\t\t\t\t\t\tThe uom is mandatory unless the value represents a unitless quantity.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'genericMeasure', genericMeasure)


# Complex type {http://www.witsml.org/schemas/131}ratioGenericMeasure with content type SIMPLE
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
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 187, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_ratioGenericMeasure_uom', uomString, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 201, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 201, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure for the quantity.\n\t\t\t\t\t\tIf for some reason a uom is not appropriate for the quantity,\n\t\t\t\t\t\ta unit of "Euc" should be used.')

    
    # Attribute numerator uses Python identifier numerator
    __numerator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numerator'), 'numerator', '__httpwww_witsml_orgschemas131_ratioGenericMeasure_numerator', unitlessQuantity)
    __numerator._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 208, 4)
    __numerator._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 208, 4)
    
    numerator = property(__numerator.value, __numerator.set, None, None)

    
    # Attribute denominator uses Python identifier denominator
    __denominator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'denominator'), 'denominator', '__httpwww_witsml_orgschemas131_ratioGenericMeasure_denominator', unitlessQuantity)
    __denominator._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 209, 4)
    __denominator._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 209, 4)
    
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


# Complex type {http://www.witsml.org/schemas/131}refNameString with content type SIMPLE
class refNameString (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a name in another node of the xml hierachy.
			This value represents a foreign key from one element to another."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refNameString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 235, 1)
    # Base type is abstractNameString
    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas131_refNameString_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 242, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 242, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, 'A reference to the unique identifier (uid attribute) in the node\n\t\t\t\t\t\treferenced by the name value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', 'refNameString', refNameString)


# Complex type {http://www.witsml.org/schemas/131}refObjectString with content type SIMPLE
class refObjectString (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a name in another object.
			This value represents a foreign key from one object to another.
			Knowledge of the object being referenced is defined by an attribute."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refObjectString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 253, 1)
    # Base type is abstractNameString
    
    # Attribute object uses Python identifier object
    __object = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'object'), 'object', '__httpwww_witsml_orgschemas131_refObjectString_object', nameString, required=True)
    __object._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 261, 4)
    __object._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 261, 4)
    
    object = property(__object.value, __object.set, None, 'The name of the singular object being referenced.')

    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas131_refObjectString_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 266, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 266, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, 'A reference to the unique identifier (uid attribute) in the object\n\t\t\t\t\t\treferenced by the name value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __object.name() : __object,
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', 'refObjectString', refObjectString)


# Complex type {http://www.witsml.org/schemas/131}refPositiveCount with content type SIMPLE
class refPositiveCount (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a index value in another node of the xml hierachy.
			This value represents a foreign key from one element to another."""
    _TypeDefinition = abstractPositiveCount
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refPositiveCount')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 277, 1)
    # Base type is abstractPositiveCount
    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas131_refPositiveCount_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 284, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 284, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, 'A reference to the unique identifier (uid attribute) in the node\n\t\t\t\t\t\treferenced by the index value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', 'refPositiveCount', refPositiveCount)


# Complex type {http://www.witsml.org/schemas/131}encodedArrayString with content type SIMPLE
class encodedArrayString (pyxb.binding.basis.complexTypeDefinition):
    """An encoded value or values. The encoding may utilize 
			any of several xsd encodings. Something external to the value must
			define the encoding. The uom attribute is optional because the value may 
			be a string or unitless quantity. If the value is a measure then
			the uom must be specified."""
    _TypeDefinition = abstractMaximumLengthString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'encodedArrayString')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 349, 1)
    # Base type is abstractMaximumLengthString
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_encodedArrayString_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 359, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 359, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uom.name() : __uom
    }
Namespace.addCategoryObject('typeBinding', 'encodedArrayString', encodedArrayString)


# Complex type {http://www.witsml.org/schemas/131}nameStruct with content type SIMPLE
class nameStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of something within a naming system."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameStruct')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 424, 1)
    # Base type is abstractNameString
    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'namingSystem'), 'namingSystem', '__httpwww_witsml_orgschemas131_nameStruct_namingSystem', nameString)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 430, 4)
    __namingSystem._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 430, 4)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, 'The naming system within the name is (hopefully) unique.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __namingSystem.name() : __namingSystem
    }
Namespace.addCategoryObject('typeBinding', 'nameStruct', nameStruct)


# Complex type {http://www.witsml.org/schemas/131}wellKnownNameStruct with content type SIMPLE
class wellKnownNameStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of something within a mandatory naming system 
			with an optional code."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'wellKnownNameStruct')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 439, 1)
    # Base type is abstractNameString
    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'namingSystem'), 'namingSystem', '__httpwww_witsml_orgschemas131_wellKnownNameStruct_namingSystem', nameString, required=True)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 446, 4)
    __namingSystem._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 446, 4)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, 'The naming system within the name is unique.')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httpwww_witsml_orgschemas131_wellKnownNameStruct_code', kindString)
    __code._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 451, 4)
    __code._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 451, 4)
    
    code = property(__code.value, __code.set, None, 'A unique (short) code associated with the name.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __namingSystem.name() : __namingSystem,
        __code.name() : __code
    }
Namespace.addCategoryObject('typeBinding', 'wellKnownNameStruct', wellKnownNameStruct)


# Complex type {http://www.witsml.org/schemas/131}measuredDepthCoord with content type SIMPLE
class measuredDepthCoord (abstractMeasure):
    """A measured depth coordinate in a wellbore. 
			Positive moving from the reference datum toward the bottomhole.
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measuredDepthCoord')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 492, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_measuredDepthCoord_uom', MeasuredDepthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 501, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 501, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure of the quantity value.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datum'), 'datum', '__httpwww_witsml_orgschemas131_measuredDepthCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 506, 4)
    __datum._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 506, 4)
    
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


# Complex type {http://www.witsml.org/schemas/131}wellVerticalDepthCoord with content type SIMPLE
class wellVerticalDepthCoord (abstractMeasure):
    """A vertical (gravity based) depth coordinate within the context of a well.
			Positive moving downward from the reference datum. 
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'wellVerticalDepthCoord')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 541, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_wellVerticalDepthCoord_uom', WellVerticalCoordinateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 550, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 550, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure of the quantity value.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datum'), 'datum', '__httpwww_witsml_orgschemas131_wellVerticalDepthCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 555, 4)
    __datum._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 555, 4)
    
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


# Complex type {http://www.witsml.org/schemas/131}wellElevationCoord with content type SIMPLE
class wellElevationCoord (abstractMeasure):
    """A vertical (gravity based) elevation coordinate within the context of a well.
			Positive moving upward from the reference datum.  
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'wellElevationCoord')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 566, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_wellElevationCoord_uom', WellVerticalCoordinateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 575, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 575, 4)
    
    uom = property(__uom.value, __uom.set, None, 'The unit of measure of the quantity value.\n\t\t\t\t\t\tIf not given then the default unit of measure of the explicitly\n\t\t\t\t\t\tor implicitly given datum must be assumed.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datum'), 'datum', '__httpwww_witsml_orgschemas131_wellElevationCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 582, 4)
    __datum._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 582, 4)
    
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


# Complex type {http://www.witsml.org/schemas/131}cost with content type SIMPLE
class cost (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/schemas/131}cost with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cost')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 714, 1)
    # Base type is abstractDouble
    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'currency'), 'currency', '__httpwww_witsml_orgschemas131_cost_currency', kindString)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 717, 4)
    __currency._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 717, 4)
    
    currency = property(__currency.value, __currency.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __currency.name() : __currency
    }
Namespace.addCategoryObject('typeBinding', 'cost', cost)


# Complex type {http://www.witsml.org/schemas/131}indexedObject with content type SIMPLE
class indexedObject (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/schemas/131}indexedObject with content type SIMPLE"""
    _TypeDefinition = abstractTypeEnum
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'indexedObject')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 722, 1)
    # Base type is abstractTypeEnum
    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'index'), 'index', '__httpwww_witsml_orgschemas131_indexedObject_index', positiveCount, required=True)
    __index._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 725, 4)
    __index._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 725, 4)
    
    index = property(__index.value, __index.set, None, 'Indexes things with the same name. \n\t\t\t\t\t\tThat is the first one, the second one, etc.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_witsml_orgschemas131_indexedObject_name', kindString)
    __name._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 731, 4)
    __name._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 731, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_indexedObject_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 732, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 732, 4)
    
    uom = property(__uom.value, __uom.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpwww_witsml_orgschemas131_indexedObject_description', descriptionString)
    __description._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 733, 4)
    __description._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 733, 4)
    
    description = property(__description.value, __description.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __index.name() : __index,
        __name.name() : __name,
        __uom.name() : __uom,
        __description.name() : __description
    }
Namespace.addCategoryObject('typeBinding', 'indexedObject', indexedObject)


# Complex type {http://www.witsml.org/schemas/131}accelerationLinearMeasure with content type SIMPLE
class accelerationLinearMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}accelerationLinearMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accelerationLinearMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 24, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_accelerationLinearMeasure_uom', accelerationLinearUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 27, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 27, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'accelerationLinearMeasure', accelerationLinearMeasure)


# Complex type {http://www.witsml.org/schemas/131}anglePerLengthMeasure with content type SIMPLE
class anglePerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}anglePerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'anglePerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 32, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_anglePerLengthMeasure_uom', anglePerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 35, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 35, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'anglePerLengthMeasure', anglePerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}anglePerTimeMeasure with content type SIMPLE
class anglePerTimeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}anglePerTimeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'anglePerTimeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 40, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_anglePerTimeMeasure_uom', anglePerTimeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 43, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 43, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'anglePerTimeMeasure', anglePerTimeMeasure)


# Complex type {http://www.witsml.org/schemas/131}areaMeasure with content type SIMPLE
class areaMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}areaMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'areaMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 48, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_areaMeasure_uom', areaUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 51, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 51, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'areaMeasure', areaMeasure)


# Complex type {http://www.witsml.org/schemas/131}areaPerAreaMeasure with content type SIMPLE
class areaPerAreaMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}areaPerAreaMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'areaPerAreaMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 56, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_areaPerAreaMeasure_uom', areaPerAreaUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 59, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 59, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'areaPerAreaMeasure', areaPerAreaMeasure)


# Complex type {http://www.witsml.org/schemas/131}densityMeasure with content type SIMPLE
class densityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}densityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'densityMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 64, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_densityMeasure_uom', densityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 67, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 67, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'densityMeasure', densityMeasure)


# Complex type {http://www.witsml.org/schemas/131}dimensionlessMeasure with content type SIMPLE
class dimensionlessMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}dimensionlessMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dimensionlessMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 72, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_dimensionlessMeasure_uom', dimensionlessUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 75, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 75, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'dimensionlessMeasure', dimensionlessMeasure)


# Complex type {http://www.witsml.org/schemas/131}dynamicViscosityMeasure with content type SIMPLE
class dynamicViscosityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}dynamicViscosityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dynamicViscosityMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 80, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_dynamicViscosityMeasure_uom', dynamicViscosityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 83, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 83, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'dynamicViscosityMeasure', dynamicViscosityMeasure)


# Complex type {http://www.witsml.org/schemas/131}electricCurrentMeasure with content type SIMPLE
class electricCurrentMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}electricCurrentMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'electricCurrentMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 88, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_electricCurrentMeasure_uom', electricCurrentUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 91, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 91, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'electricCurrentMeasure', electricCurrentMeasure)


# Complex type {http://www.witsml.org/schemas/131}electricPotentialMeasure with content type SIMPLE
class electricPotentialMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}electricPotentialMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'electricPotentialMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 96, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_electricPotentialMeasure_uom', electricPotentialUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 99, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 99, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'electricPotentialMeasure', electricPotentialMeasure)


# Complex type {http://www.witsml.org/schemas/131}energyPerAreaMeasure with content type SIMPLE
class energyPerAreaMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}energyPerAreaMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'energyPerAreaMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 104, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_energyPerAreaMeasure_uom', energyPerAreaUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 107, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 107, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'energyPerAreaMeasure', energyPerAreaMeasure)


# Complex type {http://www.witsml.org/schemas/131}equivalentPerMassMeasure with content type SIMPLE
class equivalentPerMassMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}equivalentPerMassMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equivalentPerMassMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 112, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_equivalentPerMassMeasure_uom', equivalentPerMassUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 115, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 115, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'equivalentPerMassMeasure', equivalentPerMassMeasure)


# Complex type {http://www.witsml.org/schemas/131}forceMeasure with content type SIMPLE
class forceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}forceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'forceMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 120, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_forceMeasure_uom', forceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 123, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 123, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'forceMeasure', forceMeasure)


# Complex type {http://www.witsml.org/schemas/131}forcePerLengthMeasure with content type SIMPLE
class forcePerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}forcePerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'forcePerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 128, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_forcePerLengthMeasure_uom', forcePerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 131, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 131, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'forcePerLengthMeasure', forcePerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}forcePerVolumeMeasure with content type SIMPLE
class forcePerVolumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}forcePerVolumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'forcePerVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 136, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_forcePerVolumeMeasure_uom', forcePerVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 139, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 139, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'forcePerVolumeMeasure', forcePerVolumeMeasure)


# Complex type {http://www.witsml.org/schemas/131}frequencyMeasure with content type SIMPLE
class frequencyMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}frequencyMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'frequencyMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 144, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_frequencyMeasure_uom', frequencyUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 147, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 147, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'frequencyMeasure', frequencyMeasure)


# Complex type {http://www.witsml.org/schemas/131}illuminanceMeasure with content type SIMPLE
class illuminanceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}illuminanceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'illuminanceMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 152, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_illuminanceMeasure_uom', illuminanceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 155, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 155, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'illuminanceMeasure', illuminanceMeasure)


# Complex type {http://www.witsml.org/schemas/131}lengthMeasure with content type SIMPLE
class lengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}lengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 160, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_lengthMeasure_uom', lengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 163, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 163, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'lengthMeasure', lengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}lengthPerLengthMeasure with content type SIMPLE
class lengthPerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}lengthPerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengthPerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 168, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_lengthPerLengthMeasure_uom', lengthPerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 171, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 171, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'lengthPerLengthMeasure', lengthPerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}magneticFieldStrengthMeasure with content type SIMPLE
class magneticFieldStrengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}magneticFieldStrengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'magneticFieldStrengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 176, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_magneticFieldStrengthMeasure_uom', magneticFieldStrengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 179, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 179, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'magneticFieldStrengthMeasure', magneticFieldStrengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}magneticInductionMeasure with content type SIMPLE
class magneticInductionMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}magneticInductionMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'magneticInductionMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 184, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_magneticInductionMeasure_uom', magneticInductionUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 187, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 187, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'magneticInductionMeasure', magneticInductionMeasure)


# Complex type {http://www.witsml.org/schemas/131}massConcentrationMeasure with content type SIMPLE
class massConcentrationMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}massConcentrationMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'massConcentrationMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 192, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_massConcentrationMeasure_uom', massConcentrationUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 195, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 195, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'massConcentrationMeasure', massConcentrationMeasure)


# Complex type {http://www.witsml.org/schemas/131}massMeasure with content type SIMPLE
class massMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}massMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'massMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 200, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_massMeasure_uom', massUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 203, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 203, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'massMeasure', massMeasure)


# Complex type {http://www.witsml.org/schemas/131}massPerLengthMeasure with content type SIMPLE
class massPerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}massPerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'massPerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 208, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_massPerLengthMeasure_uom', massPerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 211, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 211, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'massPerLengthMeasure', massPerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}momentOfForceMeasure with content type SIMPLE
class momentOfForceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}momentOfForceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'momentOfForceMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 216, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_momentOfForceMeasure_uom', momentOfForceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 219, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 219, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'momentOfForceMeasure', momentOfForceMeasure)


# Complex type {http://www.witsml.org/schemas/131}perLengthMeasure with content type SIMPLE
class perLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}perLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'perLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 224, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_perLengthMeasure_uom', perLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 227, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 227, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'perLengthMeasure', perLengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}planeAngleMeasure with content type SIMPLE
class planeAngleMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}planeAngleMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'planeAngleMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 232, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_planeAngleMeasure_uom', planeAngleUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 235, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 235, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'planeAngleMeasure', planeAngleMeasure)


# Complex type {http://www.witsml.org/schemas/131}powerMeasure with content type SIMPLE
class powerMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}powerMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'powerMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 240, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_powerMeasure_uom', powerUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 243, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 243, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'powerMeasure', powerMeasure)


# Complex type {http://www.witsml.org/schemas/131}pressureMeasure with content type SIMPLE
class pressureMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}pressureMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pressureMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 248, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_pressureMeasure_uom', pressureUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 251, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 251, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'pressureMeasure', pressureMeasure)


# Complex type {http://www.witsml.org/schemas/131}relativePowerMeasure with content type SIMPLE
class relativePowerMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}relativePowerMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relativePowerMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 256, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_relativePowerMeasure_uom', relativePowerUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 259, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 259, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'relativePowerMeasure', relativePowerMeasure)


# Complex type {http://www.witsml.org/schemas/131}specificVolumeMeasure with content type SIMPLE
class specificVolumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}specificVolumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'specificVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 264, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_specificVolumeMeasure_uom', specificVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 267, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 267, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'specificVolumeMeasure', specificVolumeMeasure)


# Complex type {http://www.witsml.org/schemas/131}thermodynamicTemperatureMeasure with content type SIMPLE
class thermodynamicTemperatureMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}thermodynamicTemperatureMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermodynamicTemperatureMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 272, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_thermodynamicTemperatureMeasure_uom', thermodynamicTemperatureUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 275, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 275, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'thermodynamicTemperatureMeasure', thermodynamicTemperatureMeasure)


# Complex type {http://www.witsml.org/schemas/131}timeMeasure with content type SIMPLE
class timeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}timeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 280, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_timeMeasure_uom', timeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 283, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 283, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'timeMeasure', timeMeasure)


# Complex type {http://www.witsml.org/schemas/131}velocityMeasure with content type SIMPLE
class velocityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}velocityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'velocityMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 288, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_velocityMeasure_uom', velocityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 291, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 291, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'velocityMeasure', velocityMeasure)


# Complex type {http://www.witsml.org/schemas/131}volumeMeasure with content type SIMPLE
class volumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}volumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 296, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_volumeMeasure_uom', volumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 299, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 299, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'volumeMeasure', volumeMeasure)


# Complex type {http://www.witsml.org/schemas/131}volumeFlowRateMeasure with content type SIMPLE
class volumeFlowRateMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}volumeFlowRateMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumeFlowRateMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 304, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_volumeFlowRateMeasure_uom', volumeFlowRateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 307, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 307, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'volumeFlowRateMeasure', volumeFlowRateMeasure)


# Complex type {http://www.witsml.org/schemas/131}volumePerVolumeMeasure with content type SIMPLE
class volumePerVolumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}volumePerVolumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'volumePerVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 312, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_witsml_orgschemas131_volumePerVolumeMeasure_uom', volumePerVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 315, 4)
    __uom._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 315, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', 'volumePerVolumeMeasure', volumePerVolumeMeasure)


bhaRuns = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bhaRuns'), obj_bhaRuns, documentation='The WITSML API mandated plural root element which allows \n\t\t\tmultiple singular objects to be sent. The plural name is formed by adding\n\t\t\tan "s" to the singular name.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', bhaRuns.name().localName(), bhaRuns)



cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sourceName'), nameString, scope=cs_commonData, documentation='An identifier to indicate the data originator.\n\t\t\t\t\tThis identifies the server that originally created \n\t\t\t\t\tthe object and thus most of the uids in the object (but not \n\t\t\t\t\tnecessarily the uids of the parents). This is typically a url. ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 23, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dTimCreation'), timestamp, scope=cs_commonData, documentation='When the data was created at the persistent data store.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 31, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dTimLastChange'), timestamp, scope=cs_commonData, documentation='Last change of any element of the data at the persistent data store.\n\t\t\t\t\tThe change time is not updated for a growing object while it is growing.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 36, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'itemState'), ItemState, scope=cs_commonData, documentation='The item state for the data object.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 42, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comments'), commentString, scope=cs_commonData, documentation='Comments and remarks.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 47, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 23, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 36, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 42, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 47, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sourceName')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 23, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dTimCreation')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dTimLastChange')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 36, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'itemState')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comments')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 47, 3))
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
cs_commonData._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_customData.xsd', 22, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_customData.xsd', 22, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_customData._Automaton = _BuildAutomaton_()




cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DocumentName'), nameStruct, scope=cs_documentInfo, documentation='An identifier for the document. This is \n\t\t\t\t\tintended to be unique within the context of the NamingSystem.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 26, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DocumentAlias'), nameStruct, scope=cs_documentInfo, documentation='Zero or more alternate names for the document. \n\t\t\t\t\tThese names do not need to be unique within the naming system.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 32, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DocumentDate'), timestamp, scope=cs_documentInfo, documentation='The date of the creation of the document. \n\t\t\t\t\tThis is not the same as the date that the file was created. \n\t\t\t\t\tFor this date, the document is considered to be the set of \n\t\t\t\t\tinformation associated with this document information. \n\t\t\t\t\tFor example, the document may be a seismic binset. \n\t\t\t\t\tThis represents the date that the binset was created. \n\t\t\t\t\tThe FileCreation information would capture the date that \n\t\t\t\t\tthe XML file was created to send or exchange the binset.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 38, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentClass'), nameStruct, scope=cs_documentInfo, documentation='A document class. Examples of classes would be a \n\t\t\t\t\tmetadata classification or a set of keywords. ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 50, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FileCreationInformation'), fileCreationType, scope=cs_documentInfo, documentation='The information about the creation of the \n\t\t\t\t\texchange file. This is not about the creation of the data within \n\t\t\t\t\tthe file, but the creation of the file itself.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 56, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SecurityInformation'), securityInfoType, scope=cs_documentInfo, documentation='Information about the security to be applied to \n\t\t\t\t\tthis file. More than one classification can be given.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 63, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Disclaimer'), commentString, scope=cs_documentInfo, documentation='A free-form string that allows a disclaimer to \n\t\t\t\t\taccompany the information.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 69, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AuditTrail'), auditType, scope=cs_documentInfo, documentation='A collection of events that can document the \n\t\t\t\t\thistory of the data.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 75, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Owner'), nameString, scope=cs_documentInfo, documentation='The owner of the data.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 81, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Comment'), commentString, scope=cs_documentInfo, documentation='An optional comment about the document.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 86, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 38, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 50, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 56, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=5, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 63, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 69, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 75, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 81, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 86, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DocumentName')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DocumentAlias')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 32, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DocumentDate')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentClass')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 50, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileCreationInformation')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 56, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SecurityInformation')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 63, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Disclaimer')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 69, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AuditTrail')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 75, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Owner')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 81, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Comment')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 86, 3))
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
cs_documentInfo._Automaton = _BuildAutomaton_2()




fileCreationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FileCreationDate'), timestamp, scope=fileCreationType, documentation='The date and time that the file was created.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 100, 3)))

fileCreationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SoftwareName'), nameString, scope=fileCreationType, documentation='If appropriate, the software that created the file. \n\t\t\t\t\tThis is a free form string, and may include whatever information \n\t\t\t\t\tis deemed relevant.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 105, 3)))

fileCreationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FileCreator'), nameString, scope=fileCreationType, documentation='The person or business associate that created \n\t\t\t\t\tthe file.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 112, 3)))

fileCreationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Comment'), commentString, scope=fileCreationType, documentation='Any comment that would be useful to further \n\t\t\t\t\texplain the creation of this instance document.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 118, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 105, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 112, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 118, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fileCreationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileCreationDate')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 100, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(fileCreationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SoftwareName')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 105, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(fileCreationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileCreator')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 112, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(fileCreationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Comment')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 118, 3))
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
fileCreationType._Automaton = _BuildAutomaton_3()




securityInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), kindString, scope=securityInfoType, documentation='The security class in which this document is \n\t\t\t\t\tclassified. Examples would be confidential, partner confidential, \n\t\t\t\t\ttight. The meaning of the class is determined by the System in which \n\t\t\t\t\tit is defined.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 138, 3)))

securityInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'System'), kindString, scope=securityInfoType, documentation='The security classification system. \n\t\t\t\t\tThis gives context to the meaning of the Class value.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 146, 3)))

securityInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndDate'), timestamp, scope=securityInfoType, documentation='The date on which this security class is no \n\t\t\t\t\tlonger applicable.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 152, 3)))

securityInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Comment'), commentString, scope=securityInfoType, documentation='A general comment to further define the security \n\t\t\t\t\tclass.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 158, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 138, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 146, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 152, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 158, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Class')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 138, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'System')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 146, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndDate')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 152, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Comment')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 158, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
securityInfoType._Automaton = _BuildAutomaton_4()




auditType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Event'), eventType, scope=auditType, location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 173, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(auditType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Event')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 173, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
auditType._Automaton = _BuildAutomaton_5()




eventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EventDate'), timestamp, scope=eventType, documentation='The date on which the event took place.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 183, 3)))

eventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponsibleParty'), nameString, scope=eventType, documentation='The party responsible for the event.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 188, 3)))

eventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Comment'), commentString, scope=eventType, documentation='A free form comment that can further \n\t\t\t\t\tdefine the event that occurred.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 193, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 188, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 193, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(eventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EventDate')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 183, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(eventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponsibleParty')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 188, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(eventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Comment')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 193, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
eventType._Automaton = _BuildAutomaton_6()




obj_bhaRuns._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentInfo'), cs_documentInfo, scope=obj_bhaRuns, documentation='Information about the XML message instance.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 35, 3)))

obj_bhaRuns._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bhaRun'), obj_bhaRun, scope=obj_bhaRuns, documentation='A single bottom hole assembly run.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 40, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 35, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_bhaRuns._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentInfo')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 35, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(obj_bhaRuns._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bhaRun')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 40, 3))
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
obj_bhaRuns._Automaton = _BuildAutomaton_7()




cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eTimOpBit'), timeMeasure, scope=cs_drillingParams, documentation='Operating time spent by bit for run.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 24, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mdHoleStart'), measuredDepthCoord, scope=cs_drillingParams, documentation='Measured depth at start.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 29, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mdHoleStop'), measuredDepthCoord, scope=cs_drillingParams, documentation='Measured depth at stop.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 34, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tubular'), refNameString, scope=cs_drillingParams, documentation='A pointer to the tubular assembly.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 39, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hkldRot'), forceMeasure, scope=cs_drillingParams, documentation='Hookload - rotating.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 44, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'overPull'), forceMeasure, scope=cs_drillingParams, documentation='hkldUp-hkldRot.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 49, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'slackOff'), forceMeasure, scope=cs_drillingParams, documentation='hkldRot-hkldDown.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 54, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hkldUp'), forceMeasure, scope=cs_drillingParams, documentation='Hookload - string moving up.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 59, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hkldDn'), forceMeasure, scope=cs_drillingParams, documentation='Hookload - string moving down.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 64, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tqOnBotAv'), momentOfForceMeasure, scope=cs_drillingParams, documentation='Average Torque - on bottom.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 69, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tqOnBotMx'), momentOfForceMeasure, scope=cs_drillingParams, documentation='Maximum torque - on bottom.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 74, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tqOnBotMn'), momentOfForceMeasure, scope=cs_drillingParams, documentation='Minimum torque - on bottom.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 79, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tqOffBotAv'), momentOfForceMeasure, scope=cs_drillingParams, documentation='Average torque - off bottom.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 84, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tqDhAv'), momentOfForceMeasure, scope=cs_drillingParams, documentation='Average torque - downhole.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 89, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wtAboveJar'), forceMeasure, scope=cs_drillingParams, documentation='Weight above jars.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 94, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wtBelowJar'), forceMeasure, scope=cs_drillingParams, documentation='Weight below jars.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 99, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wtMud'), densityMeasure, scope=cs_drillingParams, documentation='Mud density.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 104, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flowratePump'), volumeFlowRateMeasure, scope=cs_drillingParams, documentation='Pump flow rate.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 109, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'powBit'), powerMeasure, scope=cs_drillingParams, documentation='Bit hydraulic.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 114, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'velNozzleAv'), velocityMeasure, scope=cs_drillingParams, documentation='Bit nozzle average velocity.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 119, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'presDropBit'), pressureMeasure, scope=cs_drillingParams, documentation='Pressure drop in bit.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 124, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cTimHold'), timeMeasure, scope=cs_drillingParams, documentation='Time spent on hold from start of bit run.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 129, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cTimSteering'), timeMeasure, scope=cs_drillingParams, documentation='Time spent steering from start of bit run.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 134, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cTimDrillRot'), timeMeasure, scope=cs_drillingParams, documentation='Time spent rotary drilling from start of bit run.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 139, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cTimDrillSlid'), timeMeasure, scope=cs_drillingParams, documentation='Time spent slide drilling from start of bit run.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 144, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cTimCirc'), timeMeasure, scope=cs_drillingParams, documentation='Time spent circulating from start of bit run.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 149, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cTimReam'), timeMeasure, scope=cs_drillingParams, documentation='Time spent reaming from start of bit run.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 154, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'distDrillRot'), lengthMeasure, scope=cs_drillingParams, documentation='Distance drilled - rotating.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 159, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'distDrillSlid'), lengthMeasure, scope=cs_drillingParams, documentation='Distance drilled - sliding  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 164, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'distReam'), lengthMeasure, scope=cs_drillingParams, documentation='Distance reamed.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 169, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'distHold'), lengthMeasure, scope=cs_drillingParams, documentation='Distance covered while holding angle with a steerable drilling assembly.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 174, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'distSteering'), lengthMeasure, scope=cs_drillingParams, documentation='Distance covered while actively steering with a steerable drilling assembly.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 179, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rpmAv'), anglePerTimeMeasure, scope=cs_drillingParams, documentation='Average turn rate (commonly in rpm) through Interval.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 184, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rpmMx'), anglePerTimeMeasure, scope=cs_drillingParams, documentation='Maximum turn rate (commonly in rpm).  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 189, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rpmMn'), anglePerTimeMeasure, scope=cs_drillingParams, documentation='Minimum turn rate (commonly in rpm).  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 194, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rpmAvDh'), anglePerTimeMeasure, scope=cs_drillingParams, documentation='Average turn rate (commonly in rpm) downhole.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 199, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ropAv'), velocityMeasure, scope=cs_drillingParams, documentation='Average rate of penetration through Interval.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 204, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ropMx'), velocityMeasure, scope=cs_drillingParams, documentation='Maximum rate of penetration through Interval.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 209, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ropMn'), velocityMeasure, scope=cs_drillingParams, documentation='Minimum rate of penetration through Interval.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 214, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wobAv'), forceMeasure, scope=cs_drillingParams, documentation='Surface weight on bit - average through interval.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 219, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wobMx'), forceMeasure, scope=cs_drillingParams, documentation='Weight on bit - maximum.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 224, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wobMn'), forceMeasure, scope=cs_drillingParams, documentation='Weight on bit - minimum.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 229, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wobAvDh'), forceMeasure, scope=cs_drillingParams, documentation='Weight on bit - average downhole.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 234, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reasonTrip'), commentString, scope=cs_drillingParams, documentation='Reason for trip.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 239, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectiveBha'), commentString, scope=cs_drillingParams, documentation='Objective of bottom hole assembly.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 244, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aziTop'), planeAngleMeasure, scope=cs_drillingParams, documentation='Azimuth at start measured depth.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 249, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aziBottom'), planeAngleMeasure, scope=cs_drillingParams, documentation='Azimuth at stop measured depth.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 254, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inclStart'), planeAngleMeasure, scope=cs_drillingParams, documentation='Inclination at start measured depth.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 259, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inclMx'), planeAngleMeasure, scope=cs_drillingParams, documentation='Maximum inclination.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 264, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inclMn'), planeAngleMeasure, scope=cs_drillingParams, documentation='Minimum inclination.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 269, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inclStop'), planeAngleMeasure, scope=cs_drillingParams, documentation='Inclination at stop measured depth.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 274, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tempMudDhMx'), thermodynamicTemperatureMeasure, scope=cs_drillingParams, documentation='Maximum mud temperature downhole during run.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 279, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'presPumpAv'), pressureMeasure, scope=cs_drillingParams, documentation='Average pump pressure.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 284, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flowrateBit'), volumeFlowRateMeasure, scope=cs_drillingParams, documentation='Flow rate at bit.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 289, 3)))

cs_drillingParams._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comments'), commentString, scope=cs_drillingParams, documentation='Comments and remarks.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 294, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 29, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 39, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 44, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 49, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 54, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 59, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 64, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 69, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 74, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 79, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 84, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 89, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 94, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 99, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 104, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 109, 3))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 114, 3))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 119, 3))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 124, 3))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 129, 3))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 134, 3))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 139, 3))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 144, 3))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 149, 3))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 154, 3))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 159, 3))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 164, 3))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 169, 3))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 174, 3))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 179, 3))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 184, 3))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 189, 3))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 194, 3))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 199, 3))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 204, 3))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 209, 3))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 214, 3))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 219, 3))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 224, 3))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 229, 3))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 234, 3))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 239, 3))
    counters.add(cc_41)
    cc_42 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 244, 3))
    counters.add(cc_42)
    cc_43 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 249, 3))
    counters.add(cc_43)
    cc_44 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 254, 3))
    counters.add(cc_44)
    cc_45 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 259, 3))
    counters.add(cc_45)
    cc_46 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 264, 3))
    counters.add(cc_46)
    cc_47 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 269, 3))
    counters.add(cc_47)
    cc_48 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 274, 3))
    counters.add(cc_48)
    cc_49 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 279, 3))
    counters.add(cc_49)
    cc_50 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 284, 3))
    counters.add(cc_50)
    cc_51 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 289, 3))
    counters.add(cc_51)
    cc_52 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 294, 3))
    counters.add(cc_52)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eTimOpBit')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mdHoleStart')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 29, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mdHoleStop')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tubular')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 39, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hkldRot')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 44, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'overPull')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 49, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'slackOff')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 54, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hkldUp')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 59, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hkldDn')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 64, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tqOnBotAv')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 69, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tqOnBotMx')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 74, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tqOnBotMn')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 79, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tqOffBotAv')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 84, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tqDhAv')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 89, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wtAboveJar')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 94, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wtBelowJar')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 99, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wtMud')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 104, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flowratePump')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 109, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'powBit')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 114, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'velNozzleAv')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 119, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'presDropBit')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 124, 3))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cTimHold')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 129, 3))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cTimSteering')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 134, 3))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cTimDrillRot')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 139, 3))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cTimDrillSlid')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 144, 3))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cTimCirc')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 149, 3))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cTimReam')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 154, 3))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'distDrillRot')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 159, 3))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'distDrillSlid')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 164, 3))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'distReam')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 169, 3))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'distHold')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 174, 3))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'distSteering')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 179, 3))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rpmAv')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 184, 3))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rpmMx')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 189, 3))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rpmMn')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 194, 3))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rpmAvDh')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 199, 3))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ropAv')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 204, 3))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ropMx')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 209, 3))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ropMn')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 214, 3))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wobAv')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 219, 3))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wobMx')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 224, 3))
    st_40 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wobMn')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 229, 3))
    st_41 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_40, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wobAvDh')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 234, 3))
    st_42 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_41, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reasonTrip')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 239, 3))
    st_43 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_42, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectiveBha')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 244, 3))
    st_44 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_43, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aziTop')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 249, 3))
    st_45 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_45)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_44, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aziBottom')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 254, 3))
    st_46 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_46)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_45, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inclStart')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 259, 3))
    st_47 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_47)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_46, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inclMx')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 264, 3))
    st_48 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_48)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_47, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inclMn')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 269, 3))
    st_49 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_49)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_48, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inclStop')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 274, 3))
    st_50 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_50)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_49, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tempMudDhMx')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 279, 3))
    st_51 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_51)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_50, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'presPumpAv')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 284, 3))
    st_52 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_52)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_51, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flowrateBit')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 289, 3))
    st_53 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_53)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_52, False))
    symbol = pyxb.binding.content.ElementUse(cs_drillingParams._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comments')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_drillingParams.xsd', 294, 3))
    st_54 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_54)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    transitions.append(fac.Transition(st_34, [
         ]))
    transitions.append(fac.Transition(st_35, [
         ]))
    transitions.append(fac.Transition(st_36, [
         ]))
    transitions.append(fac.Transition(st_37, [
         ]))
    transitions.append(fac.Transition(st_38, [
         ]))
    transitions.append(fac.Transition(st_39, [
         ]))
    transitions.append(fac.Transition(st_40, [
         ]))
    transitions.append(fac.Transition(st_41, [
         ]))
    transitions.append(fac.Transition(st_42, [
         ]))
    transitions.append(fac.Transition(st_43, [
         ]))
    transitions.append(fac.Transition(st_44, [
         ]))
    transitions.append(fac.Transition(st_45, [
         ]))
    transitions.append(fac.Transition(st_46, [
         ]))
    transitions.append(fac.Transition(st_47, [
         ]))
    transitions.append(fac.Transition(st_48, [
         ]))
    transitions.append(fac.Transition(st_49, [
         ]))
    transitions.append(fac.Transition(st_50, [
         ]))
    transitions.append(fac.Transition(st_51, [
         ]))
    transitions.append(fac.Transition(st_52, [
         ]))
    transitions.append(fac.Transition(st_53, [
         ]))
    transitions.append(fac.Transition(st_54, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_40, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_40, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_41, True) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_41, False) ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_42, True) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_42, False) ]))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_43, True) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_43, False) ]))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_44, True) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_44, False) ]))
    st_46._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_45, True) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_45, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_45, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_45, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_45, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_45, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_45, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_45, False) ]))
    st_47._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_46, True) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_46, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_46, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_46, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_46, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_46, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_46, False) ]))
    st_48._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_47, True) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_47, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_47, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_47, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_47, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_47, False) ]))
    st_49._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_48, True) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_48, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_48, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_48, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_48, False) ]))
    st_50._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_49, True) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_49, False) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_49, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_49, False) ]))
    st_51._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_50, True) ]))
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_50, False) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_50, False) ]))
    st_52._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_53, [
        fac.UpdateInstruction(cc_51, True) ]))
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_51, False) ]))
    st_53._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_54, [
        fac.UpdateInstruction(cc_52, True) ]))
    st_54._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_drillingParams._Automaton = _BuildAutomaton_8()




obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tubular'), refNameString, scope=obj_bhaRun, documentation='This represents a foreign key to the tubular (assembly) \n\t\t\t\t\tthat was utilized in this run.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 24, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dTimStart'), timestamp, scope=obj_bhaRun, documentation='Date and time that activities started.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 30, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dTimStop'), timestamp, scope=obj_bhaRun, documentation='Date and time that activities stopped.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 35, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dTimStartDrilling'), timestamp, scope=obj_bhaRun, documentation='Start on bottom - date and time.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 40, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dTimStopDrilling'), timestamp, scope=obj_bhaRun, documentation='Start off bottom - date and time.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 45, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'planDogleg'), anglePerLengthMeasure, scope=obj_bhaRun, documentation='Planned dogleg severity.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 50, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actDogleg'), anglePerLengthMeasure, scope=obj_bhaRun, documentation='Actual dogleg severity.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 55, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actDoglegMx'), anglePerLengthMeasure, scope=obj_bhaRun, documentation='Actual dogleg severity - Maximum.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 60, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'statusBha'), BhaStatus, scope=obj_bhaRun, documentation='Bottom hole assembly status.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 65, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numBitRun'), nameString, scope=obj_bhaRun, documentation='Bit run number.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 70, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numStringRun'), positiveCount, scope=obj_bhaRun, documentation='The BHA (drilling string) run number. ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 75, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reasonTrip'), commentString, scope=obj_bhaRun, documentation='Reason for trip.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 80, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectiveBha'), commentString, scope=obj_bhaRun, documentation='Objective of bottom hole assembly.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 85, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'drillingParams'), cs_drillingParams, scope=obj_bhaRun, documentation='Drilling parameters.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 90, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameWell'), nameString, scope=obj_bhaRun, documentation='Human recognizable context for the well that contains the wellbore.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 57, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameWellbore'), nameString, scope=obj_bhaRun, documentation='Human recognizable context for the wellbore that contains the bottom hole assembly. ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 62, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), nameString, scope=obj_bhaRun, documentation='Human recognizable context for the run.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 67, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'commonData'), cs_commonData, scope=obj_bhaRun, documentation='A container element that contains elements that are common to all data \n\t\t\t\t\tobjects.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 77, 3)))

obj_bhaRun._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customData'), cs_customData, scope=obj_bhaRun, documentation='A container element that can contain custom or user defined \n\t\t\t\t\tdata elements.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 83, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 30, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 35, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 40, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 45, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 50, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 55, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 60, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 65, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 70, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 75, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 80, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 85, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 90, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 72, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 77, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 83, 3))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tubular')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dTimStart')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 30, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dTimStop')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 35, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dTimStartDrilling')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 40, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dTimStopDrilling')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 45, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'planDogleg')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 50, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actDogleg')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 55, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actDoglegMx')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 60, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'statusBha')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 65, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'numBitRun')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 70, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'numStringRun')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 75, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reasonTrip')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 80, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectiveBha')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 85, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'drillingParams')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_bhaRun.xsd', 90, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameWell')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 57, 3))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameWellbore')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 62, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 67, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'commonData')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 77, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(obj_bhaRun._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customData')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_bhaRun.xsd', 83, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_13, True) ]))
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
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_13, True) ]))
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_13, True) ]))
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_13, True) ]))
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_13, True) ]))
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_13, True) ]))
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
obj_bhaRun._Automaton = _BuildAutomaton_9()

