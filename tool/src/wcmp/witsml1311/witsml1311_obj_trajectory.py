# .\witsml1311_obj_trajectory.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:aca2769132b0274e00b9254c973534926b1b1a29
# Generated 2013-06-21 14:47:12.957000 by PyXB version 1.2.1
# Namespace http://www.witsml.org/schemas/131

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:5d6689c0-daab-11e2-9244-08002718187b')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.witsml.org/schemas/131', create_if_missing=True)
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


# Atomic simple type: {http://www.witsml.org/schemas/131}abstractBoolean
class abstractBoolean (pyxb.binding.datatypes.boolean):

    """This type disallows an "empty" boolean value.
			This type should not be used directly except to derive another type.
			All boolean types should be derived from this type rather than using xsd:boolen."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractBoolean')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 20, 1)
    _Documentation = u'This type disallows an "empty" boolean value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll boolean types should be derived from this type rather than using xsd:boolen.'
abstractBoolean._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractBoolean._CF_pattern.addPattern(pattern=u'.+')
abstractBoolean._InitializeFacetMap(abstractBoolean._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractBoolean', abstractBoolean)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractDateTime
class abstractDateTime (pyxb.binding.datatypes.dateTime):

    """This type disallows an "empty" dateTime value.
			This type should not be used directly except to derive another type.
			All dateTime types should be derived from this type rather than using xsd:dateTime."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 31, 1)
    _Documentation = u'This type disallows an "empty" dateTime value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll dateTime types should be derived from this type rather than using xsd:dateTime.'
abstractDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDateTime._CF_pattern.addPattern(pattern=u'.+')
abstractDateTime._InitializeFacetMap(abstractDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractDateTime', abstractDateTime)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractDate
class abstractDate (pyxb.binding.datatypes.date):

    """This type disallows an "empty" date value.
			This type should not be used directly except to derive another type.
			All dateTime types should be derived from this type rather than using xsd:dateTime."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractDate')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 42, 1)
    _Documentation = u'This type disallows an "empty" date value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll dateTime types should be derived from this type rather than using xsd:dateTime.'
abstractDate._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDate._CF_pattern.addPattern(pattern=u'.+')
abstractDate._InitializeFacetMap(abstractDate._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractDate', abstractDate)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractYear
class abstractYear (pyxb.binding.datatypes.gYear):

    """This type disallows an "empty" gYear value.
			This type should not be used directly except to derive another type.
			All year types should be derived from this type rather than using xsd:gYear."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractYear')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 53, 1)
    _Documentation = u'This type disallows an "empty" gYear value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll year types should be derived from this type rather than using xsd:gYear.'
abstractYear._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractYear._CF_pattern.addPattern(pattern=u'.+')
abstractYear._InitializeFacetMap(abstractYear._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractYear', abstractYear)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractDouble
class abstractDouble (pyxb.binding.datatypes.double):

    """This type disallows an "empty" double value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractDouble')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 64, 1)
    _Documentation = u'This type disallows an "empty" double value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractDouble._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDouble._CF_pattern.addPattern(pattern=u'.+')
abstractDouble._InitializeFacetMap(abstractDouble._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractDouble', abstractDouble)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractShort
class abstractShort (pyxb.binding.datatypes.short):

    """This type disallows an "empty" short value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractShort')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 74, 1)
    _Documentation = u'This type disallows an "empty" short value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractShort._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractShort._CF_pattern.addPattern(pattern=u'.+')
abstractShort._InitializeFacetMap(abstractShort._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractShort', abstractShort)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractInt
class abstractInt (pyxb.binding.datatypes.int):

    """This type disallows an "empty" int value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractInt')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 84, 1)
    _Documentation = u'This type disallows an "empty" int value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractInt._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractInt._CF_pattern.addPattern(pattern=u'.+')
abstractInt._InitializeFacetMap(abstractInt._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractInt', abstractInt)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractString
class abstractString (pyxb.binding.datatypes.string):

    """The intended abstract supertype of all strings.
			This abstract type allows the control over whitespace for all strings to be defined at a high level. 
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 94, 1)
    _Documentation = u'The intended abstract supertype of all strings.\n\t\t\tThis abstract type allows the control over whitespace for all strings to be defined at a high level. \n\t\t\tThis type should not be used directly except to derive another type.'
abstractString._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
abstractString._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
abstractString._InitializeFacetMap(abstractString._CF_minLength,
   abstractString._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', u'abstractString', abstractString)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractUncollapsedString
class abstractUncollapsedString (pyxb.binding.datatypes.string):

    """The intended abstract supertype of all strings that must maintain whitespace. 
			The type abstractString should normally be used.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractUncollapsedString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 145, 1)
    _Documentation = u'The intended abstract supertype of all strings that must maintain whitespace. \n\t\t\tThe type abstractString should normally be used.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractUncollapsedString._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
abstractUncollapsedString._InitializeFacetMap(abstractUncollapsedString._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'abstractUncollapsedString', abstractUncollapsedString)

# Union simple type: {http://www.witsml.org/schemas/131}anyDate
# superclasses pyxb.binding.datatypes.anySimpleType
class anyDate (pyxb.binding.basis.STD_union):

    """A union of date and dateTime, so that time is not mandatory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'anyDate')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 20, 1)
    _Documentation = u'A union of date and dateTime, so that time is not mandatory.'

    _MemberTypes = ( pyxb.binding.datatypes.dateTime, pyxb.binding.datatypes.date, pyxb.binding.datatypes.gYearMonth, pyxb.binding.datatypes.gYear, )
anyDate._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=anyDate)
anyDate._CF_pattern = pyxb.binding.facets.CF_pattern()
anyDate._InitializeFacetMap(anyDate._CF_enumeration,
   anyDate._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'anyDate', anyDate)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractMaximumLengthString
class abstractMaximumLengthString (abstractString):

    """This defines the maximum acceptable length of a
			string that can be stored in a data base."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractMaximumLengthString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 129, 1)
    _Documentation = u'This defines the maximum acceptable length of a\n\t\t\tstring that can be stored in a data base.'
abstractMaximumLengthString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000L))
abstractMaximumLengthString._InitializeFacetMap(abstractMaximumLengthString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'abstractMaximumLengthString', abstractMaximumLengthString)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractPositiveCount
class abstractPositiveCount (abstractShort):

    """A positive integer (one based count or index) with a maximum value of 32767 (2-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractPositiveCount')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 162, 1)
    _Documentation = u'A positive integer (one based count or index) with a maximum value of 32767 (2-bytes).'
abstractPositiveCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=abstractPositiveCount, value=pyxb.binding.datatypes.short(1))
abstractPositiveCount._InitializeFacetMap(abstractPositiveCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'abstractPositiveCount', abstractPositiveCount)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractNameString
class abstractNameString (abstractString):

    """The intended abstract supertype of all user assigned human 
			recognizable contextual name types. 
			There should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.
			This type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractNameString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 177, 1)
    _Documentation = u'The intended abstract supertype of all user assigned human \n\t\t\trecognizable contextual name types. \n\t\t\tThere should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.\n\t\t\tThis type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration.'
abstractNameString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
abstractNameString._InitializeFacetMap(abstractNameString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'abstractNameString', abstractNameString)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractUidString
class abstractUidString (abstractString):

    """The intended abstract supertype of all locally unique identifiers. 
			The value is not intended to convey any semantic content (e.g., it may be computer generated). 
			The value is only required to be unique within a context in a document (e.g., defined via key and keyref). 
			There is no guarantee that the same data in multiple documents will utilize the same uid value 
			unless enforced by the source of the document (e.g., a document server).
			Spaces are not allowed."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractUidString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 189, 1)
    _Documentation = u'The intended abstract supertype of all locally unique identifiers. \n\t\t\tThe value is not intended to convey any semantic content (e.g., it may be computer generated). \n\t\t\tThe value is only required to be unique within a context in a document (e.g., defined via key and keyref). \n\t\t\tThere is no guarantee that the same data in multiple documents will utilize the same uid value \n\t\t\tunless enforced by the source of the document (e.g., a document server).\n\t\t\tSpaces are not allowed.'
abstractUidString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
abstractUidString._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractUidString._CF_pattern.addPattern(pattern=u'[^ ]*')
abstractUidString._InitializeFacetMap(abstractUidString._CF_maxLength,
   abstractUidString._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractUidString', abstractUidString)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractTypeEnum
class abstractTypeEnum (abstractString):

    """The intended abstract supertype of all enumerated "types".
			This abstract type allows the maximum length of a type enumeration to be centrally defined.
			This type should not be used directly except to derive another type.
			It should also be used for uncontrolled strings which are candidates to become enumerations at a future date."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 215, 1)
    _Documentation = u'The intended abstract supertype of all enumerated "types".\n\t\t\tThis abstract type allows the maximum length of a type enumeration to be centrally defined.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tIt should also be used for uncontrolled strings which are candidates to become enumerations at a future date.'
abstractTypeEnum._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40L))
abstractTypeEnum._InitializeFacetMap(abstractTypeEnum._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'abstractTypeEnum', abstractTypeEnum)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractUomEnum
class abstractUomEnum (abstractString):

    """The intended abstract supertype of all "units of measure".
			This abstract type allows the maximum length of a UOM enumeration to be centrally defined. 
			This type is abstract in the sense that it should not be used directly 
			except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractUomEnum')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 227, 1)
    _Documentation = u'The intended abstract supertype of all "units of measure".\n\t\t\tThis abstract type allows the maximum length of a UOM enumeration to be centrally defined. \n\t\t\tThis type is abstract in the sense that it should not be used directly \n\t\t\texcept to derive another type.'
abstractUomEnum._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(24L))
abstractUomEnum._InitializeFacetMap(abstractUomEnum._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'abstractUomEnum', abstractUomEnum)

# Atomic simple type: {http://www.witsml.org/schemas/131}logicalBoolean
class logicalBoolean (abstractBoolean):

    """Values of "true" (or "1") and "false" (or "0")."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'logicalBoolean')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 63, 1)
    _Documentation = u'Values of "true" (or "1") and "false" (or "0").'
logicalBoolean._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'logicalBoolean', logicalBoolean)

# Atomic simple type: {http://www.witsml.org/schemas/131}date
class date (abstractDate):

    """A julian date."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'date')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 70, 1)
    _Documentation = u'A julian date.'
date._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'date', date)

# Atomic simple type: {http://www.witsml.org/schemas/131}timestamp
class timestamp (abstractDateTime):

    """A date with the time of day and an optional time zone.
			While the time zone is optional, it is strongly advised that the zone 
			always be specified in each date time value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timestamp')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 77, 1)
    _Documentation = u'A date with the time of day and an optional time zone.\n\t\t\tWhile the time zone is optional, it is strongly advised that the zone \n\t\t\talways be specified in each date time value.'
timestamp._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'timestamp', timestamp)

# Atomic simple type: {http://www.witsml.org/schemas/131}timeZone
class timeZone (abstractString):

    """A time zone conforming to the XSD:dateTime specification.
			It should be of the form "Z" or "shh.mm" where 
				"s" is "+" or "-", 
				"hh" is 00 to 23 and
				"mm" is 00 to 59."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeZone')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 86, 1)
    _Documentation = u'A time zone conforming to the XSD:dateTime specification.\n\t\t\tIt should be of the form "Z" or "shh.mm" where \n\t\t\t\t"s" is "+" or "-", \n\t\t\t\t"hh" is 00 to 23 and\n\t\t\t\t"mm" is 00 to 59.'
timeZone._CF_pattern = pyxb.binding.facets.CF_pattern()
timeZone._CF_pattern.addPattern(pattern=u'[Z]|([-+](([01][0-9])|(2[0-3])):[0-5][0-9])')
timeZone._InitializeFacetMap(timeZone._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'timeZone', timeZone)

# Atomic simple type: {http://www.witsml.org/schemas/131}calendarYear
class calendarYear (abstractYear):

    """A calendar year (CCYY) in the gregorian calendar."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'calendarYear')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 99, 1)
    _Documentation = u'A calendar year (CCYY) in the gregorian calendar.'
calendarYear._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'calendarYear', calendarYear)

# Atomic simple type: {http://www.witsml.org/schemas/131}unitlessQuantity
class unitlessQuantity (abstractDouble):

    """A unitless quantity. This should not 
			be confused with a dimensionless measure."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unitlessQuantity')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 145, 1)
    _Documentation = u'A unitless quantity. This should not \n\t\t\tbe confused with a dimensionless measure.'
unitlessQuantity._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'unitlessQuantity', unitlessQuantity)

# List simple type: {http://www.witsml.org/schemas/131}listOfDouble
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfDouble (pyxb.binding.basis.STD_list):

    """
				A representation of a list of xsd:double values.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfDouble')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 224, 1)
    _Documentation = u'\n\t\t\t\tA representation of a list of xsd:double values.\n\t\t\t'

    _ItemType = abstractDouble
listOfDouble._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfDouble', listOfDouble)

# Atomic simple type: {http://www.witsml.org/schemas/131}descriptionString
class descriptionString (abstractString):

    """A textual description of something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'descriptionString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 331, 1)
    _Documentation = u'A textual description of something.'
descriptionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256L))
descriptionString._InitializeFacetMap(descriptionString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'descriptionString', descriptionString)

# Atomic simple type: {http://www.witsml.org/schemas/131}shortDescriptionString
class shortDescriptionString (abstractString):

    """A short textual description of something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shortDescriptionString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 340, 1)
    _Documentation = u'A short textual description of something.'
shortDescriptionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
shortDescriptionString._InitializeFacetMap(shortDescriptionString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'shortDescriptionString', shortDescriptionString)

# Atomic simple type: {http://www.witsml.org/schemas/131}encodedValueString
class encodedValueString (abstractString):

    """A single value. The encoding may utilize 
			any of several xsd encodings. Something external to the value must
			define the encoding."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'encodedValueString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 364, 1)
    _Documentation = u'A single value. The encoding may utilize \n\t\t\tany of several xsd encodings. Something external to the value must\n\t\t\tdefine the encoding.'
encodedValueString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32L))
encodedValueString._InitializeFacetMap(encodedValueString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'encodedValueString', encodedValueString)

# Atomic simple type: {http://www.witsml.org/schemas/131}schemaVersionString
class schemaVersionString (abstractString):

    """The version of the schema.
			The first three levels are fixed. The fourth level can vary
			to represent on the constraints defined in enumerations and 
			XML loader files. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'schemaVersionString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 411, 1)
    _Documentation = u'The version of the schema.\n\t\t\tThe first three levels are fixed. The fourth level can vary\n\t\t\tto represent on the constraints defined in enumerations and \n\t\t\tXML loader files. '
schemaVersionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16L))
schemaVersionString._CF_pattern = pyxb.binding.facets.CF_pattern()
schemaVersionString._CF_pattern.addPattern(pattern=u'1\\.3\\.1\\.([1-9]|([1-9][0-9]))')
schemaVersionString._InitializeFacetMap(schemaVersionString._CF_maxLength,
   schemaVersionString._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'schemaVersionString', schemaVersionString)

# Atomic simple type: {http://www.witsml.org/schemas/131}uncollapsedString
class uncollapsedString (abstractUncollapsedString):

    """A textual string that retains all whitespace."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'uncollapsedString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 460, 1)
    _Documentation = u'A textual string that retains all whitespace.'
uncollapsedString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256L))
uncollapsedString._InitializeFacetMap(uncollapsedString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'uncollapsedString', uncollapsedString)

# Atomic simple type: {http://www.witsml.org/schemas/131}iadcBearingWearCode
class iadcBearingWearCode (abstractString):

    """IADC bearing wear code: integer 0 - 8 or one of the letters E, F, N or X. ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'iadcBearingWearCode')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 469, 1)
    _Documentation = u'IADC bearing wear code: integer 0 - 8 or one of the letters E, F, N or X. .'
iadcBearingWearCode._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
iadcBearingWearCode._CF_pattern = pyxb.binding.facets.CF_pattern()
iadcBearingWearCode._CF_pattern.addPattern(pattern=u'[0-8EFNX]')
iadcBearingWearCode._InitializeFacetMap(iadcBearingWearCode._CF_maxLength,
   iadcBearingWearCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'iadcBearingWearCode', iadcBearingWearCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}geodeticZoneString
class geodeticZoneString (abstractString):

    """A geodetic zone with values from 1 to 60 and a required direction 
			of "N" (North) or "S" (South). For example, "21N"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'geodeticZoneString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 479, 1)
    _Documentation = u'A geodetic zone with values from 1 to 60 and a required direction \n\t\t\tof "N" (North) or "S" (South). For example, "21N".'
geodeticZoneString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
geodeticZoneString._CF_pattern = pyxb.binding.facets.CF_pattern()
geodeticZoneString._CF_pattern.addPattern(pattern=u'([1-9]|[1-5][0-9]|60)[NS]')
geodeticZoneString._InitializeFacetMap(geodeticZoneString._CF_maxLength,
   geodeticZoneString._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'geodeticZoneString', geodeticZoneString)

# Atomic simple type: {http://www.witsml.org/schemas/131}nonNegativeCount
class nonNegativeCount (abstractShort):

    """A non-negative integer (zero based count or index) with a maximum value of 32767 (2-bytes).
			For items that represent "number of" something or a "sequential" count or index."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nonNegativeCount')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 624, 1)
    _Documentation = u'A non-negative integer (zero based count or index) with a maximum value of 32767 (2-bytes).\n\t\t\tFor items that represent "number of" something or a "sequential" count or index.'
nonNegativeCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=nonNegativeCount, value=pyxb.binding.datatypes.short(0))
nonNegativeCount._InitializeFacetMap(nonNegativeCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'nonNegativeCount', nonNegativeCount)

# Atomic simple type: {http://www.witsml.org/schemas/131}positiveBigCount
class positiveBigCount (abstractInt):

    """A large positive integer (one based count or index) with a maximum value of 2,147,483,647 (4-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positiveBigCount')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 651, 1)
    _Documentation = u'A large positive integer (one based count or index) with a maximum value of 2,147,483,647 (4-bytes).'
positiveBigCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveBigCount, value=pyxb.binding.datatypes.int(1))
positiveBigCount._InitializeFacetMap(positiveBigCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'positiveBigCount', positiveBigCount)

# Atomic simple type: {http://www.witsml.org/schemas/131}integerCount
class integerCount (abstractInt):

    """A positive or negative count with a maximum positive value of 2147483647 (4-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'integerCount')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 664, 1)
    _Documentation = u'A positive or negative count with a maximum positive value of 2147483647 (4-bytes).'
integerCount._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'integerCount', integerCount)

# Atomic simple type: {http://www.witsml.org/schemas/131}beaufortScaleIntegerCode
class beaufortScaleIntegerCode (abstractShort):

    """An estimate wind strength based on the Beaufort Wind Scale. 
			Values range from 0 (calm) to 12 (hurricane). """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'beaufortScaleIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 671, 1)
    _Documentation = u'An estimate wind strength based on the Beaufort Wind Scale. \n\t\t\tValues range from 0 (calm) to 12 (hurricane). '
beaufortScaleIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=beaufortScaleIntegerCode, value=pyxb.binding.datatypes.short(12))
beaufortScaleIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=beaufortScaleIntegerCode, value=pyxb.binding.datatypes.short(0))
beaufortScaleIntegerCode._InitializeFacetMap(beaufortScaleIntegerCode._CF_maxInclusive,
   beaufortScaleIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'beaufortScaleIntegerCode', beaufortScaleIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}pumpActionIntegerCode
class pumpActionIntegerCode (abstractShort):

    """Pump Action: 1 = Single acting, 2 = double acting."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pumpActionIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 682, 1)
    _Documentation = u'Pump Action: 1 = Single acting, 2 = double acting.'
pumpActionIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=pumpActionIntegerCode, value=pyxb.binding.datatypes.short(2))
pumpActionIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=pumpActionIntegerCode, value=pyxb.binding.datatypes.short(1))
pumpActionIntegerCode._InitializeFacetMap(pumpActionIntegerCode._CF_maxInclusive,
   pumpActionIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'pumpActionIntegerCode', pumpActionIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}iadcIntegerCode
class iadcIntegerCode (abstractShort):

    """IADC codes: 0 to 8."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'iadcIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 692, 1)
    _Documentation = u'IADC codes: 0 to 8.'
iadcIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=iadcIntegerCode, value=pyxb.binding.datatypes.short(8))
iadcIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=iadcIntegerCode, value=pyxb.binding.datatypes.short(0))
iadcIntegerCode._InitializeFacetMap(iadcIntegerCode._CF_maxInclusive,
   iadcIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'iadcIntegerCode', iadcIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}levelIntegerCode
class levelIntegerCode (abstractShort):

    """Integer level code from 1 through 5."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'levelIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 702, 1)
    _Documentation = u'Integer level code from 1 through 5.'
levelIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=levelIntegerCode, value=pyxb.binding.datatypes.short(8))
levelIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=levelIntegerCode, value=pyxb.binding.datatypes.short(0))
levelIntegerCode._InitializeFacetMap(levelIntegerCode._CF_maxInclusive,
   levelIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'levelIntegerCode', levelIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}str2
class str2 (abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'str2')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 738, 1)
    _Documentation = None
str2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
str2._InitializeFacetMap(str2._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'str2', str2)

# Atomic simple type: {http://www.witsml.org/schemas/131}str16
class str16 (abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'str16')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 744, 1)
    _Documentation = None
str16._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16L))
str16._InitializeFacetMap(str16._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'str16', str16)

# Atomic simple type: {http://www.witsml.org/schemas/131}str32
class str32 (abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'str32')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 750, 1)
    _Documentation = None
str32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32L))
str32._InitializeFacetMap(str32._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'str32', str32)

# Atomic simple type: {http://www.witsml.org/schemas/131}abstractCommentString
class abstractCommentString (abstractMaximumLengthString):

    """The intended abstract supertype of all comments or remarks 
			intended for human consumption. 
			There should be no assumption that semantics can be extracted from the field by a computer. 
			Neither should there be an assumption that any two humans will interpret the information 
			in the same way (i.e., it may not be interoperable)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractCommentString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 204, 1)
    _Documentation = u'The intended abstract supertype of all comments or remarks \n\t\t\tintended for human consumption. \n\t\t\tThere should be no assumption that semantics can be extracted from the field by a computer. \n\t\t\tNeither should there be an assumption that any two humans will interpret the information \n\t\t\tin the same way (i.e., it may not be interoperable).'
abstractCommentString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'abstractCommentString', abstractCommentString)

# Atomic simple type: {http://www.witsml.org/schemas/131}ActivityClassType
class ActivityClassType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ActivityClassType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 23, 1)
    _Documentation = None
ActivityClassType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ActivityClassType, enum_prefix=None)
ActivityClassType.planned = ActivityClassType._CF_enumeration.addEnumeration(unicode_value=u'planned', tag=u'planned')
ActivityClassType.unplanned = ActivityClassType._CF_enumeration.addEnumeration(unicode_value=u'unplanned', tag=u'unplanned')
ActivityClassType.downtime = ActivityClassType._CF_enumeration.addEnumeration(unicode_value=u'downtime', tag=u'downtime')
ActivityClassType.unknown = ActivityClassType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ActivityClassType._InitializeFacetMap(ActivityClassType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ActivityClassType', ActivityClassType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ActivityCode
class ActivityCode (abstractTypeEnum):

    """Activity codes.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ActivityCode')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 50, 1)
    _Documentation = u'Activity codes.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
ActivityCode._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ActivityCode', ActivityCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}AziRef
class AziRef (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AziRef')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 59, 1)
    _Documentation = None
AziRef._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AziRef, enum_prefix=None)
AziRef.magnetic_north = AziRef._CF_enumeration.addEnumeration(unicode_value=u'magnetic north', tag=u'magnetic_north')
AziRef.grid_north = AziRef._CF_enumeration.addEnumeration(unicode_value=u'grid north', tag=u'grid_north')
AziRef.true_north = AziRef._CF_enumeration.addEnumeration(unicode_value=u'true north', tag=u'true_north')
AziRef.unknown = AziRef._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
AziRef._InitializeFacetMap(AziRef._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AziRef', AziRef)

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

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ArrayElementDataType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 91, 1)
    _Documentation = u'A list of binary representations for elements of \n\t\t\taggregates which may be Base64-encoded\n\t\t\t(e. g. elements of well log array traces, or\n\t\t\tmultiplexed frames of similar-typed well log traces)\n\t\t\tas described in \n\t\t\t"XML Schema Part 2: Datatypes", 3.2.16 base64binary\n\t\t\t[http://www.w3.org/TR/xmlschema-2/#base4Binary]]\n\t\t\tand in\n\t\t\t"Multipurpose Internet Mail Extensions (MIME) Part One:\n\t\t\tFormat of Internet Message Bodies" (IETF RFC 2045)\n\t\t\t[ http://www.ietf.org/rfc/rfc2045.txt ].'
ArrayElementDataType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ArrayElementDataType, enum_prefix=None)
ArrayElementDataType.boolean = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value=u'boolean', tag=u'boolean')
ArrayElementDataType.integer_8_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value=u'integer 8 bit', tag=u'integer_8_bit')
ArrayElementDataType.integer_16_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value=u'integer 16 bit', tag=u'integer_16_bit')
ArrayElementDataType.integer_32_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value=u'integer 32 bit', tag=u'integer_32_bit')
ArrayElementDataType.integer_64_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value=u'integer 64 bit', tag=u'integer_64_bit')
ArrayElementDataType.IEEE_float_32_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value=u'IEEE float 32 bit', tag=u'IEEE_float_32_bit')
ArrayElementDataType.IEEE_float_64_bit = ArrayElementDataType._CF_enumeration.addEnumeration(unicode_value=u'IEEE float 64 bit', tag=u'IEEE_float_64_bit')
ArrayElementDataType._InitializeFacetMap(ArrayElementDataType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ArrayElementDataType', ArrayElementDataType)

# Atomic simple type: {http://www.witsml.org/schemas/131}BearingType
class BearingType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BearingType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 116, 1)
    _Documentation = None
BearingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BearingType, enum_prefix=None)
BearingType.oil_seal = BearingType._CF_enumeration.addEnumeration(unicode_value=u'oil seal', tag=u'oil_seal')
BearingType.mud_lube = BearingType._CF_enumeration.addEnumeration(unicode_value=u'mud lube', tag=u'mud_lube')
BearingType.other = BearingType._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
BearingType.unknown = BearingType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BearingType._InitializeFacetMap(BearingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BearingType', BearingType)

# Atomic simple type: {http://www.witsml.org/schemas/131}BitDullCode
class BitDullCode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent a classification of a drill bit based 
			on its reason for being declared inoperable, as originally defined by the IADC."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BitDullCode')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 143, 1)
    _Documentation = u'These values represent a classification of a drill bit based \n\t\t\ton its reason for being declared inoperable, as originally defined by the IADC.'
BitDullCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BitDullCode, enum_prefix=None)
BitDullCode.BC = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'BC', tag=u'BC')
BitDullCode.BT = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'BT', tag=u'BT')
BitDullCode.BU = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'BU', tag=u'BU')
BitDullCode.CC = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'CC', tag=u'CC')
BitDullCode.CD = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'CD', tag=u'CD')
BitDullCode.CI = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'CI', tag=u'CI')
BitDullCode.CR = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'CR', tag=u'CR')
BitDullCode.CT = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'CT', tag=u'CT')
BitDullCode.ER = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'ER', tag=u'ER')
BitDullCode.FC = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'FC', tag=u'FC')
BitDullCode.HC = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'HC', tag=u'HC')
BitDullCode.JD = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'JD', tag=u'JD')
BitDullCode.LC = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'LC', tag=u'LC')
BitDullCode.LN = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'LN', tag=u'LN')
BitDullCode.LT = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'LT', tag=u'LT')
BitDullCode.NO = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'NO', tag=u'NO')
BitDullCode.OC = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'OC', tag=u'OC')
BitDullCode.PB = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'PB', tag=u'PB')
BitDullCode.PN = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'PN', tag=u'PN')
BitDullCode.RG = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'RG', tag=u'RG')
BitDullCode.RO = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'RO', tag=u'RO')
BitDullCode.SD = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'SD', tag=u'SD')
BitDullCode.SS = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'SS', tag=u'SS')
BitDullCode.TR = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'TR', tag=u'TR')
BitDullCode.WO = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'WO', tag=u'WO')
BitDullCode.WT = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'WT', tag=u'WT')
BitDullCode.unknown = BitDullCode._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BitDullCode._InitializeFacetMap(BitDullCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BitDullCode', BitDullCode)

# Atomic simple type: {http://www.witsml.org/schemas/131}BitReasonPulled
class BitReasonPulled (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the reason for pulling a drill bit 
			from the wellbore, as originally defined by the IADC."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BitReasonPulled')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 289, 1)
    _Documentation = u'These values represent the reason for pulling a drill bit \n\t\t\tfrom the wellbore, as originally defined by the IADC.'
BitReasonPulled._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BitReasonPulled, enum_prefix=None)
BitReasonPulled.BHA = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'BHA', tag=u'BHA')
BitReasonPulled.CM = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'CM', tag=u'CM')
BitReasonPulled.CP = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'CP', tag=u'CP')
BitReasonPulled.DMF = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'DMF', tag=u'DMF')
BitReasonPulled.DP = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'DP', tag=u'DP')
BitReasonPulled.DST = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'DST', tag=u'DST')
BitReasonPulled.DTF = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'DTF', tag=u'DTF')
BitReasonPulled.FM = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'FM', tag=u'FM')
BitReasonPulled.HP = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'HP', tag=u'HP')
BitReasonPulled.HR = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'HR', tag=u'HR')
BitReasonPulled.LOG = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'LOG', tag=u'LOG')
BitReasonPulled.PP = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'PP', tag=u'PP')
BitReasonPulled.PR = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'PR', tag=u'PR')
BitReasonPulled.RIG = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'RIG', tag=u'RIG')
BitReasonPulled.TD = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'TD', tag=u'TD')
BitReasonPulled.TQ = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'TQ', tag=u'TQ')
BitReasonPulled.TW = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'TW', tag=u'TW')
BitReasonPulled.WC = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'WC', tag=u'WC')
BitReasonPulled.unknown = BitReasonPulled._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BitReasonPulled._InitializeFacetMap(BitReasonPulled._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BitReasonPulled', BitReasonPulled)

# Atomic simple type: {http://www.witsml.org/schemas/131}BitType
class BitType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drill/core bit."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BitType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 395, 1)
    _Documentation = u'These values represent the type of drill/core bit.'
BitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BitType, enum_prefix=None)
BitType.diamond = BitType._CF_enumeration.addEnumeration(unicode_value=u'diamond', tag=u'diamond')
BitType.diamond_core = BitType._CF_enumeration.addEnumeration(unicode_value=u'diamond core', tag=u'diamond_core')
BitType.insert_roller_cone = BitType._CF_enumeration.addEnumeration(unicode_value=u'insert roller cone', tag=u'insert_roller_cone')
BitType.PDC = BitType._CF_enumeration.addEnumeration(unicode_value=u'PDC', tag=u'PDC')
BitType.PDC_core = BitType._CF_enumeration.addEnumeration(unicode_value=u'PDC core', tag=u'PDC_core')
BitType.roller_cone = BitType._CF_enumeration.addEnumeration(unicode_value=u'roller cone', tag=u'roller_cone')
BitType.unknown = BitType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BitType._InitializeFacetMap(BitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BitType', BitType)

# Atomic simple type: {http://www.witsml.org/schemas/131}BhaStatus
class BhaStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BhaStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 440, 1)
    _Documentation = None
BhaStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BhaStatus, enum_prefix=None)
BhaStatus.final = BhaStatus._CF_enumeration.addEnumeration(unicode_value=u'final', tag=u'final')
BhaStatus.progress = BhaStatus._CF_enumeration.addEnumeration(unicode_value=u'progress', tag=u'progress')
BhaStatus.plan = BhaStatus._CF_enumeration.addEnumeration(unicode_value=u'plan', tag=u'plan')
BhaStatus.unknown = BhaStatus._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BhaStatus._InitializeFacetMap(BhaStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BhaStatus', BhaStatus)

# Atomic simple type: {http://www.witsml.org/schemas/131}BladeShapeType
class BladeShapeType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BladeShapeType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 467, 1)
    _Documentation = None
BladeShapeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BladeShapeType, enum_prefix=None)
BladeShapeType.dynamic = BladeShapeType._CF_enumeration.addEnumeration(unicode_value=u'dynamic', tag=u'dynamic')
BladeShapeType.melon = BladeShapeType._CF_enumeration.addEnumeration(unicode_value=u'melon', tag=u'melon')
BladeShapeType.spiral = BladeShapeType._CF_enumeration.addEnumeration(unicode_value=u'spiral', tag=u'spiral')
BladeShapeType.straight = BladeShapeType._CF_enumeration.addEnumeration(unicode_value=u'straight', tag=u'straight')
BladeShapeType.variable = BladeShapeType._CF_enumeration.addEnumeration(unicode_value=u'variable', tag=u'variable')
BladeShapeType.unknown = BladeShapeType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BladeShapeType._InitializeFacetMap(BladeShapeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BladeShapeType', BladeShapeType)

# Atomic simple type: {http://www.witsml.org/schemas/131}BladeType
class BladeType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BladeType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 504, 1)
    _Documentation = None
BladeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BladeType, enum_prefix=None)
BladeType.clamp_on = BladeType._CF_enumeration.addEnumeration(unicode_value=u'clamp-on', tag=u'clamp_on')
BladeType.integral = BladeType._CF_enumeration.addEnumeration(unicode_value=u'integral', tag=u'integral')
BladeType.sleeve = BladeType._CF_enumeration.addEnumeration(unicode_value=u'sleeve', tag=u'sleeve')
BladeType.welded = BladeType._CF_enumeration.addEnumeration(unicode_value=u'welded', tag=u'welded')
BladeType.unknown = BladeType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BladeType._InitializeFacetMap(BladeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BladeType', BladeType)

# Atomic simple type: {http://www.witsml.org/schemas/131}BopType
class BopType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BopType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 536, 1)
    _Documentation = None
BopType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BopType, enum_prefix=None)
BopType.annular_preventer = BopType._CF_enumeration.addEnumeration(unicode_value=u'annular preventer', tag=u'annular_preventer')
BopType.shear_ram = BopType._CF_enumeration.addEnumeration(unicode_value=u'shear ram', tag=u'shear_ram')
BopType.blind_ram = BopType._CF_enumeration.addEnumeration(unicode_value=u'blind ram', tag=u'blind_ram')
BopType.pipe_ram = BopType._CF_enumeration.addEnumeration(unicode_value=u'pipe ram', tag=u'pipe_ram')
BopType.drilling_spool = BopType._CF_enumeration.addEnumeration(unicode_value=u'drilling spool', tag=u'drilling_spool')
BopType.flexible_joint = BopType._CF_enumeration.addEnumeration(unicode_value=u'flexible joint', tag=u'flexible_joint')
BopType.connector = BopType._CF_enumeration.addEnumeration(unicode_value=u'connector', tag=u'connector')
BopType.unknown = BopType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BopType._InitializeFacetMap(BopType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BopType', BopType)

# Atomic simple type: {http://www.witsml.org/schemas/131}BoxPinConfig
class BoxPinConfig (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of Box/Pin configuration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BoxPinConfig')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 583, 1)
    _Documentation = u'These values represent the type of Box/Pin configuration.'
BoxPinConfig._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BoxPinConfig, enum_prefix=None)
BoxPinConfig.bottom_box_top_box = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value=u'bottom box, top box', tag=u'bottom_box_top_box')
BoxPinConfig.bottom_box_top_pin = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value=u'bottom box, top pin', tag=u'bottom_box_top_pin')
BoxPinConfig.bottom_pin_top_box = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value=u'bottom pin top box', tag=u'bottom_pin_top_box')
BoxPinConfig.bottom_pin = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value=u'bottom pin', tag=u'bottom_pin')
BoxPinConfig.unknown = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BoxPinConfig._InitializeFacetMap(BoxPinConfig._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BoxPinConfig', BoxPinConfig)

# Atomic simple type: {http://www.witsml.org/schemas/131}CementJobType
class CementJobType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CementJobType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 618, 1)
    _Documentation = None
CementJobType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CementJobType, enum_prefix=None)
CementJobType.primary = CementJobType._CF_enumeration.addEnumeration(unicode_value=u'primary', tag=u'primary')
CementJobType.plug = CementJobType._CF_enumeration.addEnumeration(unicode_value=u'plug', tag=u'plug')
CementJobType.squeeze = CementJobType._CF_enumeration.addEnumeration(unicode_value=u'squeeze', tag=u'squeeze')
CementJobType.unknown = CementJobType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
CementJobType._InitializeFacetMap(CementJobType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CementJobType', CementJobType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ConnectionPosition
class ConnectionPosition (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the position of a connection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ConnectionPosition')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 645, 1)
    _Documentation = u'These values represent the position of a connection.'
ConnectionPosition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ConnectionPosition, enum_prefix=None)
ConnectionPosition.both = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value=u'both', tag=u'both')
ConnectionPosition.bottom = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value=u'bottom', tag=u'bottom')
ConnectionPosition.top = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value=u'top', tag=u'top')
ConnectionPosition.unknown = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ConnectionPosition._InitializeFacetMap(ConnectionPosition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ConnectionPosition', ConnectionPosition)

# Atomic simple type: {http://www.witsml.org/schemas/131}DeflectionMethod
class DeflectionMethod (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent method used to direct the 
			deviation of the trajectory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DeflectionMethod')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 675, 1)
    _Documentation = u'These values represent method used to direct the \n\t\t\tdeviation of the trajectory.'
DeflectionMethod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeflectionMethod, enum_prefix=None)
DeflectionMethod.point_bit = DeflectionMethod._CF_enumeration.addEnumeration(unicode_value=u'point bit', tag=u'point_bit')
DeflectionMethod.push_bit = DeflectionMethod._CF_enumeration.addEnumeration(unicode_value=u'push bit', tag=u'push_bit')
DeflectionMethod._InitializeFacetMap(DeflectionMethod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DeflectionMethod', DeflectionMethod)

# Atomic simple type: {http://www.witsml.org/schemas/131}DerrickType
class DerrickType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drilling derrick."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DerrickType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 698, 1)
    _Documentation = u'These values represent the type of drilling derrick.'
DerrickType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DerrickType, enum_prefix=None)
DerrickType.double = DerrickType._CF_enumeration.addEnumeration(unicode_value=u'double', tag=u'double')
DerrickType.quadruple = DerrickType._CF_enumeration.addEnumeration(unicode_value=u'quadruple', tag=u'quadruple')
DerrickType.slant = DerrickType._CF_enumeration.addEnumeration(unicode_value=u'slant', tag=u'slant')
DerrickType.triple = DerrickType._CF_enumeration.addEnumeration(unicode_value=u'triple', tag=u'triple')
DerrickType.unknown = DerrickType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
DerrickType._InitializeFacetMap(DerrickType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DerrickType', DerrickType)

# Atomic simple type: {http://www.witsml.org/schemas/131}DrawWorksType
class DrawWorksType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DrawWorksType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 733, 1)
    _Documentation = None
DrawWorksType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DrawWorksType, enum_prefix=None)
DrawWorksType.mechanical = DrawWorksType._CF_enumeration.addEnumeration(unicode_value=u'mechanical', tag=u'mechanical')
DrawWorksType.standard_electric = DrawWorksType._CF_enumeration.addEnumeration(unicode_value=u'standard electric', tag=u'standard_electric')
DrawWorksType.diesel_electric = DrawWorksType._CF_enumeration.addEnumeration(unicode_value=u'diesel electric', tag=u'diesel_electric')
DrawWorksType.ram_rig = DrawWorksType._CF_enumeration.addEnumeration(unicode_value=u'ram rig', tag=u'ram_rig')
DrawWorksType.unknown = DrawWorksType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
DrawWorksType._InitializeFacetMap(DrawWorksType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DrawWorksType', DrawWorksType)

# Atomic simple type: {http://www.witsml.org/schemas/131}DriveType
class DriveType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of work string drive (rotary system)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DriveType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 765, 1)
    _Documentation = u'These values represent the type of work string drive (rotary system).'
DriveType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DriveType, enum_prefix=None)
DriveType.coiled_tubing = DriveType._CF_enumeration.addEnumeration(unicode_value=u'coiled tubing', tag=u'coiled_tubing')
DriveType.rotary_kelly_drive = DriveType._CF_enumeration.addEnumeration(unicode_value=u'rotary kelly drive', tag=u'rotary_kelly_drive')
DriveType.top_drive = DriveType._CF_enumeration.addEnumeration(unicode_value=u'top drive', tag=u'top_drive')
DriveType.unknown = DriveType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
DriveType._InitializeFacetMap(DriveType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DriveType', DriveType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ElevCodeEnum
class ElevCodeEnum (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The type of local or permanent reference datum for vertical gravity based 
			(i.e., elevation and vertical depth) and measured depth coordinates within the context of a well.
			This list includes local points (e.g., kelly bushing) used as a datum and 
			vertical reference datums (e.g., mean sea level)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ElevCodeEnum')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 795, 1)
    _Documentation = u'The type of local or permanent reference datum for vertical gravity based \n\t\t\t(i.e., elevation and vertical depth) and measured depth coordinates within the context of a well.\n\t\t\tThis list includes local points (e.g., kelly bushing) used as a datum and \n\t\t\tvertical reference datums (e.g., mean sea level).'
ElevCodeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ElevCodeEnum, enum_prefix=None)
ElevCodeEnum.CF = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'CF', tag=u'CF')
ElevCodeEnum.CV = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'CV', tag=u'CV')
ElevCodeEnum.DF = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'DF', tag=u'DF')
ElevCodeEnum.GL = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'GL', tag=u'GL')
ElevCodeEnum.KB = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'KB', tag=u'KB')
ElevCodeEnum.RB = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'RB', tag=u'RB')
ElevCodeEnum.RT = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'RT', tag=u'RT')
ElevCodeEnum.SF = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'SF', tag=u'SF')
ElevCodeEnum.LAT = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'LAT', tag=u'LAT')
ElevCodeEnum.SL = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'SL', tag=u'SL')
ElevCodeEnum.MHHW = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'MHHW', tag=u'MHHW')
ElevCodeEnum.MHW = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'MHW', tag=u'MHW')
ElevCodeEnum.MLLW = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'MLLW', tag=u'MLLW')
ElevCodeEnum.MLW = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'MLW', tag=u'MLW')
ElevCodeEnum.MTL = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'MTL', tag=u'MTL')
ElevCodeEnum.KO = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'KO', tag=u'KO')
ElevCodeEnum.unknown = ElevCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ElevCodeEnum._InitializeFacetMap(ElevCodeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ElevCodeEnum', ElevCodeEnum)

# Atomic simple type: {http://www.witsml.org/schemas/131}Ellipsoid
class Ellipsoid (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of ellipsoid (spheroid) 
			defining geographic or planar coordinates. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Ellipsoid')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 903, 1)
    _Documentation = u'These values represent the type of ellipsoid (spheroid) \n\t\t\tdefining geographic or planar coordinates. '
Ellipsoid._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Ellipsoid, enum_prefix=None)
Ellipsoid.AGD66 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'AGD66', tag=u'AGD66')
Ellipsoid.AIRY_MOD = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'AIRY_MOD', tag=u'AIRY_MOD')
Ellipsoid.AIRY30 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'AIRY30', tag=u'AIRY30')
Ellipsoid.AIRY49 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'AIRY49', tag=u'AIRY49')
Ellipsoid.AUST_NAT = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'AUST_NAT', tag=u'AUST_NAT')
Ellipsoid.BESL_DHD = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'BESL-DHD', tag=u'BESL_DHD')
Ellipsoid.BESL_NGL = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'BESL-NGL', tag=u'BESL_NGL')
Ellipsoid.BESL_RT9 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'BESL-RT9', tag=u'BESL_RT9')
Ellipsoid.BESS41 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'BESS41', tag=u'BESS41')
Ellipsoid.BESSNAM = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'BESSNAM', tag=u'BESSNAM')
Ellipsoid.BOGOTA = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'BOGOTA', tag=u'BOGOTA')
Ellipsoid.CL58 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL58', tag=u'CL58')
Ellipsoid.CL58_1 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL58-1', tag=u'CL58_1')
Ellipsoid.CL66 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL66', tag=u'CL66')
Ellipsoid.CL66_M = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL66-M', tag=u'CL66_M')
Ellipsoid.CL80 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL80', tag=u'CL80')
Ellipsoid.CL80_A = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL80-A', tag=u'CL80_A')
Ellipsoid.CL80_B = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL80-B', tag=u'CL80_B')
Ellipsoid.CL80_I = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL80-I', tag=u'CL80_I')
Ellipsoid.CL80_J = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL80-J', tag=u'CL80_J')
Ellipsoid.CL80_M = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL80-M', tag=u'CL80_M')
Ellipsoid.CL80_P = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CL80-P', tag=u'CL80_P')
Ellipsoid.CMPOINCH = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'CMPOINCH', tag=u'CMPOINCH')
Ellipsoid.DAN = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'DAN', tag=u'DAN')
Ellipsoid.DELA = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'DELA', tag=u'DELA')
Ellipsoid.ED50 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'ED50', tag=u'ED50')
Ellipsoid.EGYPT07 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'EGYPT07', tag=u'EGYPT07')
Ellipsoid.EVER = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'EVER', tag=u'EVER')
Ellipsoid.EVER48 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'EVER48', tag=u'EVER48')
Ellipsoid.EVER56 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'EVER56', tag=u'EVER56')
Ellipsoid.EVER69 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'EVER69', tag=u'EVER69')
Ellipsoid.EVER_BR = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'EVER-BR', tag=u'EVER_BR')
Ellipsoid.EVERMOD = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'EVERMOD', tag=u'EVERMOD')
Ellipsoid.EVER_P = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'EVER-P', tag=u'EVER_P')
Ellipsoid.EVER_TM = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'EVER-TM', tag=u'EVER_TM')
Ellipsoid.EVTM = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'EVTM', tag=u'EVTM')
Ellipsoid.FISC60 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'FISC60', tag=u'FISC60')
Ellipsoid.FISC60MOD = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'FISC60MOD', tag=u'FISC60MOD')
Ellipsoid.FISC68 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'FISC68', tag=u'FISC68')
Ellipsoid.FISCMOD = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'FISCMOD', tag=u'FISCMOD')
Ellipsoid.GDA94 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'GDA94', tag=u'GDA94')
Ellipsoid.GRS67 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'GRS67', tag=u'GRS67')
Ellipsoid.GRS80 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'GRS80', tag=u'GRS80')
Ellipsoid.HAY09 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'HAY09', tag=u'HAY09')
Ellipsoid.HEIS = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'HEIS', tag=u'HEIS')
Ellipsoid.HEL06 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'HEL06', tag=u'HEL06')
Ellipsoid.HEL07 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'HEL07', tag=u'HEL07')
Ellipsoid.HOUG = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'HOUG', tag=u'HOUG')
Ellipsoid.IAG_75 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'IAG-75', tag=u'IAG_75')
Ellipsoid.INDIAN75 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'INDIAN75', tag=u'INDIAN75')
Ellipsoid.INDO_74 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'INDO-74', tag=u'INDO_74')
Ellipsoid.INT24 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'INT24', tag=u'INT24')
Ellipsoid.IUGG67 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'IUGG67', tag=u'IUGG67')
Ellipsoid.IUGG75 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'IUGG75', tag=u'IUGG75')
Ellipsoid.JEFF48 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'JEFF48', tag=u'JEFF48')
Ellipsoid.KAU63 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'KAU63', tag=u'KAU63')
Ellipsoid.KRSV = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'KRSV', tag=u'KRSV')
Ellipsoid.MERIT83 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'MERIT83', tag=u'MERIT83')
Ellipsoid.NAD27 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'NAD27', tag=u'NAD27')
Ellipsoid.NAHRAN = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'NAHRAN', tag=u'NAHRAN')
Ellipsoid.NEWINT67 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'NEWINT67', tag=u'NEWINT67')
Ellipsoid.NWL_10D = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'NWL-10D', tag=u'NWL_10D')
Ellipsoid.NWL_9D = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'NWL-9D', tag=u'NWL_9D')
Ellipsoid.OSGB36 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'OSGB36', tag=u'OSGB36')
Ellipsoid.OSU86F = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'OSU86F', tag=u'OSU86F')
Ellipsoid.OSU91A = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'OSU91A', tag=u'OSU91A')
Ellipsoid.PLESSIS_1817 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'PLESSIS-1817', tag=u'PLESSIS_1817')
Ellipsoid.PSAD56 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'PSAD56', tag=u'PSAD56')
Ellipsoid.PTNOIRE = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'PTNOIRE', tag=u'PTNOIRE')
Ellipsoid.SA69 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'SA69', tag=u'SA69')
Ellipsoid.SPHR = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'SPHR', tag=u'SPHR')
Ellipsoid.STRU = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'STRU', tag=u'STRU')
Ellipsoid.WALB = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'WALB', tag=u'WALB')
Ellipsoid.WAR24 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'WAR24', tag=u'WAR24')
Ellipsoid.WGS60 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'WGS60', tag=u'WGS60')
Ellipsoid.WGS66 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'WGS66', tag=u'WGS66')
Ellipsoid.WGS72 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'WGS72', tag=u'WGS72')
Ellipsoid.WGS84 = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'WGS84', tag=u'WGS84')
Ellipsoid.unknown = Ellipsoid._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
Ellipsoid._InitializeFacetMap(Ellipsoid._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Ellipsoid', Ellipsoid)

# Atomic simple type: {http://www.witsml.org/schemas/131}FiberMode
class FiberMode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The mode of a Distributed Temperature Survey (DTS) fiber."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FiberMode')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1309, 1)
    _Documentation = u'The mode of a Distributed Temperature Survey (DTS) fiber.'
FiberMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FiberMode, enum_prefix=None)
FiberMode.singlemode = FiberMode._CF_enumeration.addEnumeration(unicode_value=u'singlemode', tag=u'singlemode')
FiberMode.multimode = FiberMode._CF_enumeration.addEnumeration(unicode_value=u'multimode', tag=u'multimode')
FiberMode.other = FiberMode._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
FiberMode.unknown = FiberMode._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
FiberMode._InitializeFacetMap(FiberMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'FiberMode', FiberMode)

# Atomic simple type: {http://www.witsml.org/schemas/131}GasPeakType
class GasPeakType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GasPeakType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1342, 1)
    _Documentation = None
GasPeakType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=GasPeakType, enum_prefix=None)
GasPeakType.circulating_background_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value=u'circulating background gas', tag=u'circulating_background_gas')
GasPeakType.connection_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value=u'connection gas', tag=u'connection_gas')
GasPeakType.drilling_background_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value=u'drilling background gas', tag=u'drilling_background_gas')
GasPeakType.drilling_gas_peak = GasPeakType._CF_enumeration.addEnumeration(unicode_value=u'drilling gas peak', tag=u'drilling_gas_peak')
GasPeakType.flow_check_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value=u'flow check gas', tag=u'flow_check_gas')
GasPeakType.no_readings = GasPeakType._CF_enumeration.addEnumeration(unicode_value=u'no readings', tag=u'no_readings')
GasPeakType.other = GasPeakType._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
GasPeakType.shut_down_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value=u'shut down gas', tag=u'shut_down_gas')
GasPeakType.trip_gas = GasPeakType._CF_enumeration.addEnumeration(unicode_value=u'trip gas', tag=u'trip_gas')
GasPeakType.unknown = GasPeakType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
GasPeakType._InitializeFacetMap(GasPeakType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'GasPeakType', GasPeakType)

# Atomic simple type: {http://www.witsml.org/schemas/131}GeodeticDatum
class GeodeticDatum (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of geodetic datum. 
			The source (except for "none", "unknown" and "UserDefined") of the values 
			and the descriptions is Geoshare V13."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeodeticDatum')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1399, 1)
    _Documentation = u'These values represent the type of geodetic datum. \n\t\t\tThe source (except for "none", "unknown" and "UserDefined") of the values \n\t\t\tand the descriptions is Geoshare V13.'
GeodeticDatum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=GeodeticDatum, enum_prefix=None)
GeodeticDatum.ADND = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'ADND', tag=u'ADND')
GeodeticDatum.ARC50 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'ARC50', tag=u'ARC50')
GeodeticDatum.AUSG = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'AUSG', tag=u'AUSG')
GeodeticDatum.CAA = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'CAA', tag=u'CAA')
GeodeticDatum.CHAS = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'CHAS', tag=u'CHAS')
GeodeticDatum.CORAL = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'CORAL', tag=u'CORAL')
GeodeticDatum.ED50 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'ED50', tag=u'ED50')
GeodeticDatum.ED87 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'ED87', tag=u'ED87')
GeodeticDatum.ERIN65 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'ERIN65', tag=u'ERIN65')
GeodeticDatum.GD49 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'GD49', tag=u'GD49')
GeodeticDatum.GHANA = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'GHANA', tag=u'GHANA')
GeodeticDatum.GUAM63 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'GUAM63', tag=u'GUAM63')
GeodeticDatum.HJRS55 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'HJRS55', tag=u'HJRS55')
GeodeticDatum.HTS = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'HTS', tag=u'HTS')
GeodeticDatum.INCH = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'INCH', tag=u'INCH')
GeodeticDatum.INDIA1 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'INDIA1', tag=u'INDIA1')
GeodeticDatum.INDIA2 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'INDIA2', tag=u'INDIA2')
GeodeticDatum.INDNS74 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'INDNS74', tag=u'INDNS74')
GeodeticDatum.LIB64 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'LIB64', tag=u'LIB64')
GeodeticDatum.LUZON = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'LUZON', tag=u'LUZON')
GeodeticDatum.MRCH = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'MRCH', tag=u'MRCH')
GeodeticDatum.NAD27 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'NAD27', tag=u'NAD27')
GeodeticDatum.NAD83 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'NAD83', tag=u'NAD83')
GeodeticDatum.NGRA = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'NGRA', tag=u'NGRA')
GeodeticDatum.None_ = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'None', tag=u'None_')
GeodeticDatum.NPRM = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'NPRM', tag=u'NPRM')
GeodeticDatum.OSGB36 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'OSGB36', tag=u'OSGB36')
GeodeticDatum.POTS1 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'POTS1', tag=u'POTS1')
GeodeticDatum.PULK1 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'PULK1', tag=u'PULK1')
GeodeticDatum.PULK2 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'PULK2', tag=u'PULK2')
GeodeticDatum.QRNQ = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'QRNQ', tag=u'QRNQ')
GeodeticDatum.SA56 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'SA56', tag=u'SA56')
GeodeticDatum.SRL60 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'SRL60', tag=u'SRL60')
GeodeticDatum.TNRV25 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'TNRV25', tag=u'TNRV25')
GeodeticDatum.TOKYO = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'TOKYO', tag=u'TOKYO')
GeodeticDatum.UserDefined = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'UserDefined', tag=u'UserDefined')
GeodeticDatum.VROL = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'VROL', tag=u'VROL')
GeodeticDatum.WGS72 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'WGS72', tag=u'WGS72')
GeodeticDatum.WGS84 = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'WGS84', tag=u'WGS84')
GeodeticDatum.YACR = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'YACR', tag=u'YACR')
GeodeticDatum.unknown = GeodeticDatum._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
GeodeticDatum._InitializeFacetMap(GeodeticDatum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'GeodeticDatum', GeodeticDatum)

# Atomic simple type: {http://www.witsml.org/schemas/131}Hemispheres
class Hemispheres (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Hemispheres')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1616, 1)
    _Documentation = None
Hemispheres._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Hemispheres, enum_prefix=None)
Hemispheres.northern = Hemispheres._CF_enumeration.addEnumeration(unicode_value=u'northern', tag=u'northern')
Hemispheres.southern = Hemispheres._CF_enumeration.addEnumeration(unicode_value=u'southern', tag=u'southern')
Hemispheres.unknown = Hemispheres._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
Hemispheres._InitializeFacetMap(Hemispheres._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Hemispheres', Hemispheres)

# Atomic simple type: {http://www.witsml.org/schemas/131}HoleCasingType
class HoleCasingType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HoleCasingType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1638, 1)
    _Documentation = None
HoleCasingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HoleCasingType, enum_prefix=None)
HoleCasingType.blow_out_preventer = HoleCasingType._CF_enumeration.addEnumeration(unicode_value=u'blow out preventer', tag=u'blow_out_preventer')
HoleCasingType.casing = HoleCasingType._CF_enumeration.addEnumeration(unicode_value=u'casing', tag=u'casing')
HoleCasingType.conductor = HoleCasingType._CF_enumeration.addEnumeration(unicode_value=u'conductor', tag=u'conductor')
HoleCasingType.curved_conductor = HoleCasingType._CF_enumeration.addEnumeration(unicode_value=u'curved conductor', tag=u'curved_conductor')
HoleCasingType.liner = HoleCasingType._CF_enumeration.addEnumeration(unicode_value=u'liner', tag=u'liner')
HoleCasingType.open_hole = HoleCasingType._CF_enumeration.addEnumeration(unicode_value=u'open hole', tag=u'open_hole')
HoleCasingType.riser = HoleCasingType._CF_enumeration.addEnumeration(unicode_value=u'riser', tag=u'riser')
HoleCasingType.tubing = HoleCasingType._CF_enumeration.addEnumeration(unicode_value=u'tubing', tag=u'tubing')
HoleCasingType.unknown = HoleCasingType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
HoleCasingType._InitializeFacetMap(HoleCasingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'HoleCasingType', HoleCasingType)

# Atomic simple type: {http://www.witsml.org/schemas/131}HoleOpenerType
class HoleOpenerType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HoleOpenerType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1690, 1)
    _Documentation = None
HoleOpenerType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HoleOpenerType, enum_prefix=None)
HoleOpenerType.under_reamer = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value=u'under-reamer', tag=u'under_reamer')
HoleOpenerType.fixed_blade = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value=u'fixed blade', tag=u'fixed_blade')
HoleOpenerType.unknown = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
HoleOpenerType._InitializeFacetMap(HoleOpenerType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'HoleOpenerType', HoleOpenerType)

# Atomic simple type: {http://www.witsml.org/schemas/131}IntervalMethod
class IntervalMethod (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IntervalMethod')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1712, 1)
    _Documentation = None
IntervalMethod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IntervalMethod, enum_prefix=None)
IntervalMethod.average = IntervalMethod._CF_enumeration.addEnumeration(unicode_value=u'average', tag=u'average')
IntervalMethod.maximum = IntervalMethod._CF_enumeration.addEnumeration(unicode_value=u'maximum', tag=u'maximum')
IntervalMethod.minimum = IntervalMethod._CF_enumeration.addEnumeration(unicode_value=u'minimum', tag=u'minimum')
IntervalMethod.other = IntervalMethod._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
IntervalMethod.spot_sample = IntervalMethod._CF_enumeration.addEnumeration(unicode_value=u'spot sample', tag=u'spot_sample')
IntervalMethod.unknown = IntervalMethod._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
IntervalMethod._InitializeFacetMap(IntervalMethod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'IntervalMethod', IntervalMethod)

# Atomic simple type: {http://www.witsml.org/schemas/131}IntervalType
class IntervalType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IntervalType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1749, 1)
    _Documentation = None
IntervalType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IntervalType, enum_prefix=None)
IntervalType.time = IntervalType._CF_enumeration.addEnumeration(unicode_value=u'time', tag=u'time')
IntervalType.depth = IntervalType._CF_enumeration.addEnumeration(unicode_value=u'depth', tag=u'depth')
IntervalType.unknown = IntervalType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
IntervalType._InitializeFacetMap(IntervalType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'IntervalType', IntervalType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ItemState
class ItemState (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the state of a WITSML object. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ItemState')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1771, 1)
    _Documentation = u'These values represent the state of a WITSML object. '
ItemState._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ItemState, enum_prefix=None)
ItemState.actual = ItemState._CF_enumeration.addEnumeration(unicode_value=u'actual', tag=u'actual')
ItemState.model = ItemState._CF_enumeration.addEnumeration(unicode_value=u'model', tag=u'model')
ItemState.plan = ItemState._CF_enumeration.addEnumeration(unicode_value=u'plan', tag=u'plan')
ItemState.unknown = ItemState._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ItemState._InitializeFacetMap(ItemState._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ItemState', ItemState)

# Atomic simple type: {http://www.witsml.org/schemas/131}InstalledFiberPoint
class InstalledFiberPoint (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The type of Distributed Temperature Survey (DTS) fiber point."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'InstalledFiberPoint')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1801, 1)
    _Documentation = u'The type of Distributed Temperature Survey (DTS) fiber point.'
InstalledFiberPoint._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InstalledFiberPoint, enum_prefix=None)
InstalledFiberPoint.splice = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'splice', tag=u'splice')
InstalledFiberPoint.connector = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'connector', tag=u'connector')
InstalledFiberPoint.end_of_fiber = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'end of fiber', tag=u'end_of_fiber')
InstalledFiberPoint.base_of_fiber = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'base of fiber', tag=u'base_of_fiber')
InstalledFiberPoint.turn_around_point = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'turn around point', tag=u'turn_around_point')
InstalledFiberPoint.start_of_fiber = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'start of fiber', tag=u'start_of_fiber')
InstalledFiberPoint.oven_entry_point = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'oven entry point', tag=u'oven_entry_point')
InstalledFiberPoint.oven_exit_point = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'oven exit point', tag=u'oven_exit_point')
InstalledFiberPoint.downhole_gauge = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'downhole gauge', tag=u'downhole_gauge')
InstalledFiberPoint.DTS_laser_head = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'DTS laser head', tag=u'DTS_laser_head')
InstalledFiberPoint.DTS_reference_oven = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'DTS reference oven', tag=u'DTS_reference_oven')
InstalledFiberPoint.splice_box = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'splice box', tag=u'splice_box')
InstalledFiberPoint.wellhead_junction_box = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'wellhead junction box', tag=u'wellhead_junction_box')
InstalledFiberPoint.base_tubing_hanger_flange = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'base tubing hanger flange', tag=u'base_tubing_hanger_flange')
InstalledFiberPoint.PBR_wet_connect = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'PBR wet connect', tag=u'PBR_wet_connect')
InstalledFiberPoint.top_ESP_pump = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'top ESP pump', tag=u'top_ESP_pump')
InstalledFiberPoint.base_ESP_pump = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'base ESP pump', tag=u'base_ESP_pump')
InstalledFiberPoint.wellhead_temperature_gauge = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'wellhead temperature gauge', tag=u'wellhead_temperature_gauge')
InstalledFiberPoint.top_completion_zone = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'top completion zone', tag=u'top_completion_zone')
InstalledFiberPoint.base_completion_zone = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'base completion zone', tag=u'base_completion_zone')
InstalledFiberPoint.unknown = InstalledFiberPoint._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
InstalledFiberPoint._InitializeFacetMap(InstalledFiberPoint._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'InstalledFiberPoint', InstalledFiberPoint)

# Atomic simple type: {http://www.witsml.org/schemas/131}JarType
class JarType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'JarType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1939, 1)
    _Documentation = None
JarType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=JarType, enum_prefix=None)
JarType.mechanical = JarType._CF_enumeration.addEnumeration(unicode_value=u'mechanical', tag=u'mechanical')
JarType.hydraulic = JarType._CF_enumeration.addEnumeration(unicode_value=u'hydraulic', tag=u'hydraulic')
JarType.hydro_mechanical = JarType._CF_enumeration.addEnumeration(unicode_value=u'hydro mechanical', tag=u'hydro_mechanical')
JarType.unknown = JarType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
JarType._InitializeFacetMap(JarType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'JarType', JarType)

# Atomic simple type: {http://www.witsml.org/schemas/131}JarAction
class JarAction (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'JarAction')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1966, 1)
    _Documentation = None
JarAction._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=JarAction, enum_prefix=None)
JarAction.up = JarAction._CF_enumeration.addEnumeration(unicode_value=u'up', tag=u'up')
JarAction.down = JarAction._CF_enumeration.addEnumeration(unicode_value=u'down', tag=u'down')
JarAction.both = JarAction._CF_enumeration.addEnumeration(unicode_value=u'both', tag=u'both')
JarAction.vibrating = JarAction._CF_enumeration.addEnumeration(unicode_value=u'vibrating', tag=u'vibrating')
JarAction.unknown = JarAction._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
JarAction._InitializeFacetMap(JarAction._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'JarAction', JarAction)

# Atomic simple type: {http://www.witsml.org/schemas/131}LithologySource
class LithologySource (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Specifies the source of lithology information."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LithologySource')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 1998, 1)
    _Documentation = u'Specifies the source of lithology information.'
LithologySource._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LithologySource, enum_prefix=None)
LithologySource.interpreted = LithologySource._CF_enumeration.addEnumeration(unicode_value=u'interpreted', tag=u'interpreted')
LithologySource.core = LithologySource._CF_enumeration.addEnumeration(unicode_value=u'core', tag=u'core')
LithologySource.cuttings = LithologySource._CF_enumeration.addEnumeration(unicode_value=u'cuttings', tag=u'cuttings')
LithologySource.unknown = LithologySource._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
LithologySource._InitializeFacetMap(LithologySource._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LithologySource', LithologySource)

# Atomic simple type: {http://www.witsml.org/schemas/131}LithologyType
class LithologyType (abstractTypeEnum):

    """The type of lithology.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LithologyType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2031, 1)
    _Documentation = u'The type of lithology.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
LithologyType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'LithologyType', LithologyType)

# Atomic simple type: {http://www.witsml.org/schemas/131}LogDataType
class LogDataType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The endcoding allowed in a realtime channel value or log curve value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogDataType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2040, 1)
    _Documentation = u'The endcoding allowed in a realtime channel value or log curve value.'
LogDataType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogDataType, enum_prefix=None)
LogDataType.date_time = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'date time', tag=u'date_time')
LogDataType.double = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'double', tag=u'double')
LogDataType.long = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'long', tag=u'long')
LogDataType.string = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'string', tag=u'string')
LogDataType.unknown = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
LogDataType._InitializeFacetMap(LogDataType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LogDataType', LogDataType)

# Atomic simple type: {http://www.witsml.org/schemas/131}LogIndexDirection
class LogIndexDirection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the direction of movement within a wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogIndexDirection')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2075, 1)
    _Documentation = u'These values represent the direction of movement within a wellbore.'
LogIndexDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogIndexDirection, enum_prefix=None)
LogIndexDirection.decreasing = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value=u'decreasing', tag=u'decreasing')
LogIndexDirection.increasing = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value=u'increasing', tag=u'increasing')
LogIndexDirection.unknown = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
LogIndexDirection._InitializeFacetMap(LogIndexDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LogIndexDirection', LogIndexDirection)

# Atomic simple type: {http://www.witsml.org/schemas/131}LogIndexType
class LogIndexType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of data used as an index value for a log. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogIndexType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2102, 1)
    _Documentation = u'These values represent the type of data used as an index value for a log. '
LogIndexType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogIndexType, enum_prefix=None)
LogIndexType.date_time = LogIndexType._CF_enumeration.addEnumeration(unicode_value=u'date time', tag=u'date_time')
LogIndexType.elapsed_time = LogIndexType._CF_enumeration.addEnumeration(unicode_value=u'elapsed time', tag=u'elapsed_time')
LogIndexType.length = LogIndexType._CF_enumeration.addEnumeration(unicode_value=u'length', tag=u'length')
LogIndexType.measured_depth = LogIndexType._CF_enumeration.addEnumeration(unicode_value=u'measured depth', tag=u'measured_depth')
LogIndexType.vertical_depth = LogIndexType._CF_enumeration.addEnumeration(unicode_value=u'vertical depth', tag=u'vertical_depth')
LogIndexType.other = LogIndexType._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
LogIndexType.unknown = LogIndexType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
LogIndexType._InitializeFacetMap(LogIndexType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LogIndexType', LogIndexType)

# Atomic simple type: {http://www.witsml.org/schemas/131}LogTraceOrigin
class LogTraceOrigin (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogTraceOrigin')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2147, 1)
    _Documentation = None
LogTraceOrigin._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogTraceOrigin, enum_prefix=None)
LogTraceOrigin.realtime = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value=u'realtime', tag=u'realtime')
LogTraceOrigin.modeled = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value=u'modeled', tag=u'modeled')
LogTraceOrigin.unknown = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
LogTraceOrigin._InitializeFacetMap(LogTraceOrigin._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LogTraceOrigin', LogTraceOrigin)

# Atomic simple type: {http://www.witsml.org/schemas/131}LogTraceState
class LogTraceState (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogTraceState')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2169, 1)
    _Documentation = None
LogTraceState._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogTraceState, enum_prefix=None)
LogTraceState.depth_adjusted = LogTraceState._CF_enumeration.addEnumeration(unicode_value=u'depth adjusted', tag=u'depth_adjusted')
LogTraceState.edited = LogTraceState._CF_enumeration.addEnumeration(unicode_value=u'edited', tag=u'edited')
LogTraceState.joined = LogTraceState._CF_enumeration.addEnumeration(unicode_value=u'joined', tag=u'joined')
LogTraceState.processed = LogTraceState._CF_enumeration.addEnumeration(unicode_value=u'processed', tag=u'processed')
LogTraceState.raw = LogTraceState._CF_enumeration.addEnumeration(unicode_value=u'raw', tag=u'raw')
LogTraceState.unknown = LogTraceState._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
LogTraceState._InitializeFacetMap(LogTraceState._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LogTraceState', LogTraceState)

# Atomic simple type: {http://www.witsml.org/schemas/131}MaterialType
class MaterialType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MaterialType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2206, 1)
    _Documentation = None
MaterialType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MaterialType, enum_prefix=None)
MaterialType.aluminum = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'aluminum', tag=u'aluminum')
MaterialType.beryllium_copper = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'beryllium copper', tag=u'beryllium_copper')
MaterialType.chrome_alloy = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'chrome alloy', tag=u'chrome_alloy')
MaterialType.composite = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'composite', tag=u'composite')
MaterialType.other = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
MaterialType.non_magnetic_steel = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'non-magnetic steel', tag=u'non_magnetic_steel')
MaterialType.plastic = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'plastic', tag=u'plastic')
MaterialType.steel = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'steel', tag=u'steel')
MaterialType.steel_alloy = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'steel alloy', tag=u'steel_alloy')
MaterialType.titanium = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'titanium', tag=u'titanium')
MaterialType.unknown = MaterialType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
MaterialType._InitializeFacetMap(MaterialType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MaterialType', MaterialType)

# Atomic simple type: {http://www.witsml.org/schemas/131}MeasurementType
class MeasurementType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The source (except for "CH density porosity", "CH neutron porosity", "OH density porosity"
			and "OH neutron porosity") of the values and the descriptions is the POSC V2.2 "well log trace class" 
			standard instance values which are documented as "A classification of well log traces based on 
			specification of a range of characteristics. Traces may be classed according to the type of physical 
			characteristic they are meant to measure." """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MeasurementType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 2268, 1)
    _Documentation = u'The source (except for "CH density porosity", "CH neutron porosity", "OH density porosity"\n\t\t\tand "OH neutron porosity") of the values and the descriptions is the POSC V2.2 "well log trace class" \n\t\t\tstandard instance values which are documented as "A classification of well log traces based on \n\t\t\tspecification of a range of characteristics. Traces may be classed according to the type of physical \n\t\t\tcharacteristic they are meant to measure."'
MeasurementType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MeasurementType, enum_prefix=None)
MeasurementType.acceleration = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'acceleration', tag=u'acceleration')
MeasurementType.acoustic_caliper = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'acoustic caliper', tag=u'acoustic_caliper')
MeasurementType.acoustic_casing_collar_locator = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'acoustic casing collar locator', tag=u'acoustic_casing_collar_locator')
MeasurementType.acoustic_impedance = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'acoustic impedance', tag=u'acoustic_impedance')
MeasurementType.acoustic_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'acoustic porosity', tag=u'acoustic_porosity')
MeasurementType.acoustic_velocity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'acoustic velocity', tag=u'acoustic_velocity')
MeasurementType.acoustic_wave_matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'acoustic wave matrix travel time', tag=u'acoustic_wave_matrix_travel_time')
MeasurementType.acoustic_wave_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'acoustic wave travel time', tag=u'acoustic_wave_travel_time')
MeasurementType.amplitude = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'amplitude', tag=u'amplitude')
MeasurementType.amplitude_of_acoustic_wave = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'amplitude of acoustic wave', tag=u'amplitude_of_acoustic_wave')
MeasurementType.amplitude_of_E_M_wave = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'amplitude of E-M wave', tag=u'amplitude_of_E_M_wave')
MeasurementType.amplitude_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'amplitude ratio', tag=u'amplitude_ratio')
MeasurementType.area = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'area', tag=u'area')
MeasurementType.attenuation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'attenuation', tag=u'attenuation')
MeasurementType.attenuation_of_acoustic_wave = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'attenuation of acoustic wave', tag=u'attenuation_of_acoustic_wave')
MeasurementType.attenuation_of_E_M_wave = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'attenuation of E-M wave', tag=u'attenuation_of_E_M_wave')
MeasurementType.auxiliary = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'auxiliary', tag=u'auxiliary')
MeasurementType.average_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'average porosity', tag=u'average_porosity')
MeasurementType.azimuth = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'azimuth', tag=u'azimuth')
MeasurementType.barite_mud_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'barite mud correction', tag=u'barite_mud_correction')
MeasurementType.bed_thickness_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'bed thickness correction', tag=u'bed_thickness_correction')
MeasurementType.bit_size = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'bit size', tag=u'bit_size')
MeasurementType.blocked = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'blocked', tag=u'blocked')
MeasurementType.borehole_environment_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'borehole environment correction', tag=u'borehole_environment_correction')
MeasurementType.borehole_fluid_composition_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'borehole fluid composition correction', tag=u'borehole_fluid_composition_correction')
MeasurementType.borehole_fluid_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'borehole fluid correction', tag=u'borehole_fluid_correction')
MeasurementType.borehole_size_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'borehole size correction', tag=u'borehole_size_correction')
MeasurementType.bromide_mud_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'bromide mud correction', tag=u'bromide_mud_correction')
MeasurementType.bulk_compressibility = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'bulk compressibility', tag=u'bulk_compressibility')
MeasurementType.bulk_density = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'bulk density', tag=u'bulk_density')
MeasurementType.bulk_volume = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'bulk volume', tag=u'bulk_volume')
MeasurementType.bulk_volume_gas = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'bulk volume gas', tag=u'bulk_volume_gas')
MeasurementType.bulk_volume_hydrocarbon = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'bulk volume hydrocarbon', tag=u'bulk_volume_hydrocarbon')
MeasurementType.bulk_volume_oil = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'bulk volume oil', tag=u'bulk_volume_oil')
MeasurementType.bulk_volume_water = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'bulk volume water', tag=u'bulk_volume_water')
MeasurementType.CO_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'C/O ratio', tag=u'CO_ratio')
MeasurementType.caliper = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'caliper', tag=u'caliper')
MeasurementType.cased_hole_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'cased hole correction', tag=u'cased_hole_correction')
MeasurementType.casing_collar_locator = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'casing collar locator', tag=u'casing_collar_locator')
MeasurementType.casing_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'casing correction', tag=u'casing_correction')
MeasurementType.casing_diameter_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'casing diameter correction', tag=u'casing_diameter_correction')
MeasurementType.casing_inspection = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'casing inspection', tag=u'casing_inspection')
MeasurementType.casing_thickness_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'casing thickness correction', tag=u'casing_thickness_correction')
MeasurementType.casing_weight_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'casing weight correction', tag=u'casing_weight_correction')
MeasurementType.cement_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'cement correction', tag=u'cement_correction')
MeasurementType.cement_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'cement density correction', tag=u'cement_density_correction')
MeasurementType.cement_evaluation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'cement evaluation', tag=u'cement_evaluation')
MeasurementType.cement_thickness_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'cement thickness correction', tag=u'cement_thickness_correction')
MeasurementType.cement_type_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'cement type correction', tag=u'cement_type_correction')
MeasurementType.CH_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'CH density porosity', tag=u'CH_density_porosity')
MeasurementType.CH_dolomite_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'CH dolomite density porosity', tag=u'CH_dolomite_density_porosity')
MeasurementType.CH_dolomite_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'CH dolomite neutron porosity', tag=u'CH_dolomite_neutron_porosity')
MeasurementType.CH_limestone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'CH limestone density porosity', tag=u'CH_limestone_density_porosity')
MeasurementType.CH_limestone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'CH limestone neutron porosity', tag=u'CH_limestone_neutron_porosity')
MeasurementType.CH_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'CH neutron porosity', tag=u'CH_neutron_porosity')
MeasurementType.CH_sandstone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'CH sandstone density porosity', tag=u'CH_sandstone_density_porosity')
MeasurementType.CH_sandstone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'CH sandstone neutron porosity', tag=u'CH_sandstone_neutron_porosity')
MeasurementType.compressional_wave_dolomite_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'compressional wave dolomite porosity', tag=u'compressional_wave_dolomite_porosity')
MeasurementType.compressional_wave_limestone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'compressional wave limestone porosity', tag=u'compressional_wave_limestone_porosity')
MeasurementType.compressional_wave_matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'compressional wave matrix travel time', tag=u'compressional_wave_matrix_travel_time')
MeasurementType.compressional_wave_sandstone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'compressional wave sandstone porosity', tag=u'compressional_wave_sandstone_porosity')
MeasurementType.compressional_wave_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'compressional wave travel time', tag=u'compressional_wave_travel_time')
MeasurementType.conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'conductivity', tag=u'conductivity')
MeasurementType.conductivity_from_attenuation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'conductivity from attenuation', tag=u'conductivity_from_attenuation')
MeasurementType.conductivity_from_phase_shift = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'conductivity from phase shift', tag=u'conductivity_from_phase_shift')
MeasurementType.connate_water_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'connate water conductivity', tag=u'connate_water_conductivity')
MeasurementType.connate_water_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'connate water resistivity', tag=u'connate_water_resistivity')
MeasurementType.conventional_core_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'conventional core porosity', tag=u'conventional_core_porosity')
MeasurementType.core_matrix_density = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'core matrix density', tag=u'core_matrix_density')
MeasurementType.core_permeability = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'core permeability', tag=u'core_permeability')
MeasurementType.core_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'core porosity', tag=u'core_porosity')
MeasurementType.corrected = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'corrected', tag=u'corrected')
MeasurementType.count_rate = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'count rate', tag=u'count_rate')
MeasurementType.count_rate_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'count rate ratio', tag=u'count_rate_ratio')
MeasurementType.cross_plot_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'cross plot porosity', tag=u'cross_plot_porosity')
MeasurementType.decay_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'decay time', tag=u'decay_time')
MeasurementType.deep_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'deep conductivity', tag=u'deep_conductivity')
MeasurementType.deep_induction_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'deep induction conductivity', tag=u'deep_induction_conductivity')
MeasurementType.deep_induction_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'deep induction resistivity', tag=u'deep_induction_resistivity')
MeasurementType.deep_laterolog_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'deep laterolog conductivity', tag=u'deep_laterolog_conductivity')
MeasurementType.deep_laterolog_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'deep laterolog resistivity', tag=u'deep_laterolog_resistivity')
MeasurementType.deep_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'deep resistivity', tag=u'deep_resistivity')
MeasurementType.density = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'density', tag=u'density')
MeasurementType.density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'density porosity', tag=u'density_porosity')
MeasurementType.depth = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'depth', tag=u'depth')
MeasurementType.depth_adjusted = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'depth adjusted', tag=u'depth_adjusted')
MeasurementType.depth_derived_from_velocity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'depth derived from velocity', tag=u'depth_derived_from_velocity')
MeasurementType.deviation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'deviation', tag=u'deviation')
MeasurementType.dielectric = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'dielectric', tag=u'dielectric')
MeasurementType.diffusion_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'diffusion correction', tag=u'diffusion_correction')
MeasurementType.dip = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'dip', tag=u'dip')
MeasurementType.dipmeter = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'dipmeter', tag=u'dipmeter')
MeasurementType.dipmeter_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'dipmeter conductivity', tag=u'dipmeter_conductivity')
MeasurementType.dipmeter_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'dipmeter resistivity', tag=u'dipmeter_resistivity')
MeasurementType.dolomite_acoustic_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'dolomite acoustic porosity', tag=u'dolomite_acoustic_porosity')
MeasurementType.dolomite_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'dolomite density porosity', tag=u'dolomite_density_porosity')
MeasurementType.dolomite_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'dolomite neutron porosity', tag=u'dolomite_neutron_porosity')
MeasurementType.edited = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'edited', tag=u'edited')
MeasurementType.effective_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'effective porosity', tag=u'effective_porosity')
MeasurementType.electric_current = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'electric current', tag=u'electric_current')
MeasurementType.electric_potential = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'electric potential', tag=u'electric_potential')
MeasurementType.electromagnetic_wave_matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'electromagnetic wave matrix travel time', tag=u'electromagnetic_wave_matrix_travel_time')
MeasurementType.electromagnetic_wave_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'electromagnetic wave travel time', tag=u'electromagnetic_wave_travel_time')
MeasurementType.element = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'element', tag=u'element')
MeasurementType.elemental_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'elemental ratio', tag=u'elemental_ratio')
MeasurementType.enhanced = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'enhanced', tag=u'enhanced')
MeasurementType.filtered = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'filtered', tag=u'filtered')
MeasurementType.flowmeter = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'flowmeter', tag=u'flowmeter')
MeasurementType.fluid_density = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'fluid density', tag=u'fluid_density')
MeasurementType.fluid_velocity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'fluid velocity', tag=u'fluid_velocity')
MeasurementType.fluid_viscosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'fluid viscosity', tag=u'fluid_viscosity')
MeasurementType.flushed_zone_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'flushed zone conductivity', tag=u'flushed_zone_conductivity')
MeasurementType.flushed_zone_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'flushed zone resistivity', tag=u'flushed_zone_resistivity')
MeasurementType.flushed_zone_saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'flushed zone saturation', tag=u'flushed_zone_saturation')
MeasurementType.force = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'force', tag=u'force')
MeasurementType.formation_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'formation density correction', tag=u'formation_density_correction')
MeasurementType.formation_properties_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'formation properties correction', tag=u'formation_properties_correction')
MeasurementType.formation_salinity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'formation salinity correction', tag=u'formation_salinity_correction')
MeasurementType.formation_saturation_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'formation saturation correction', tag=u'formation_saturation_correction')
MeasurementType.formation_volume_factor_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'formation volume factor correction', tag=u'formation_volume_factor_correction')
MeasurementType.formation_water_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'formation water density correction', tag=u'formation_water_density_correction')
MeasurementType.formation_water_saturation_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'formation water saturation correction', tag=u'formation_water_saturation_correction')
MeasurementType.free_fluid_index = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'free fluid index', tag=u'free_fluid_index')
MeasurementType.friction_effect_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'friction effect correction', tag=u'friction_effect_correction')
MeasurementType.gamma_ray = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'gamma ray', tag=u'gamma_ray')
MeasurementType.gamma_ray_minus_uranium = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'gamma ray minus uranium', tag=u'gamma_ray_minus_uranium')
MeasurementType.gas_saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'gas saturation', tag=u'gas_saturation')
MeasurementType.gradiomanometer = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'gradiomanometer', tag=u'gradiomanometer')
MeasurementType.high_frequency_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'high frequency conductivity', tag=u'high_frequency_conductivity')
MeasurementType.high_frequency_electromagnetic = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'high frequency electromagnetic', tag=u'high_frequency_electromagnetic')
MeasurementType.high_frequency_electromagnetic_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'high frequency electromagnetic porosity', tag=u'high_frequency_electromagnetic_porosity')
MeasurementType.high_frequency_E_M_phase_shift = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'high frequency E-M phase shift', tag=u'high_frequency_E_M_phase_shift')
MeasurementType.high_frequency_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'high frequency resistivity', tag=u'high_frequency_resistivity')
MeasurementType.hydrocarbon_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'hydrocarbon correction', tag=u'hydrocarbon_correction')
MeasurementType.hydrocarbon_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'hydrocarbon density correction', tag=u'hydrocarbon_density_correction')
MeasurementType.hydrocarbon_gravity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'hydrocarbon gravity correction', tag=u'hydrocarbon_gravity_correction')
MeasurementType.hydrocarbon_saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'hydrocarbon saturation', tag=u'hydrocarbon_saturation')
MeasurementType.hydrocarbon_viscosity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'hydrocarbon viscosity correction', tag=u'hydrocarbon_viscosity_correction')
MeasurementType.image = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'image', tag=u'image')
MeasurementType.interpretation_variable = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'interpretation variable', tag=u'interpretation_variable')
MeasurementType.iron_mud_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'iron mud correction', tag=u'iron_mud_correction')
MeasurementType.joined = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'joined', tag=u'joined')
MeasurementType.KCl_mud_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'KCl mud correction', tag=u'KCl_mud_correction')
MeasurementType.length = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'length', tag=u'length')
MeasurementType.limestone_acoustic_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'limestone acoustic porosity', tag=u'limestone_acoustic_porosity')
MeasurementType.limestone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'limestone density porosity', tag=u'limestone_density_porosity')
MeasurementType.limestone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'limestone neutron porosity', tag=u'limestone_neutron_porosity')
MeasurementType.lithology_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'lithology correction', tag=u'lithology_correction')
MeasurementType.log_derived_permeability = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'log derived permeability', tag=u'log_derived_permeability')
MeasurementType.log_matrix_density = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'log matrix density', tag=u'log_matrix_density')
MeasurementType.magnetic_casing_collar_locator = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'magnetic casing collar locator', tag=u'magnetic_casing_collar_locator')
MeasurementType.matrix_density = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'matrix density', tag=u'matrix_density')
MeasurementType.matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'matrix travel time', tag=u'matrix_travel_time')
MeasurementType.measured_depth = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'measured depth', tag=u'measured_depth')
MeasurementType.mechanical_caliper = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mechanical caliper', tag=u'mechanical_caliper')
MeasurementType.mechanical_casing_collar_locator = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mechanical casing collar locator', tag=u'mechanical_casing_collar_locator')
MeasurementType.medium_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'medium conductivity', tag=u'medium_conductivity')
MeasurementType.medium_induction_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'medium induction conductivity', tag=u'medium_induction_conductivity')
MeasurementType.medium_induction_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'medium induction resistivity', tag=u'medium_induction_resistivity')
MeasurementType.medium_laterolog_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'medium laterolog conductivity', tag=u'medium_laterolog_conductivity')
MeasurementType.medium_laterolog_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'medium laterolog resistivity', tag=u'medium_laterolog_resistivity')
MeasurementType.medium_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'medium resistivity', tag=u'medium_resistivity')
MeasurementType.micro_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'micro conductivity', tag=u'micro_conductivity')
MeasurementType.micro_inverse_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'micro inverse conductivity', tag=u'micro_inverse_conductivity')
MeasurementType.micro_inverse_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'micro inverse resistivity', tag=u'micro_inverse_resistivity')
MeasurementType.micro_laterolog_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'micro laterolog conductivity', tag=u'micro_laterolog_conductivity')
MeasurementType.micro_laterolog_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'micro laterolog resistivity', tag=u'micro_laterolog_resistivity')
MeasurementType.micro_normal_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'micro normal conductivity', tag=u'micro_normal_conductivity')
MeasurementType.micro_normal_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'micro normal resistivity', tag=u'micro_normal_resistivity')
MeasurementType.micro_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'micro resistivity', tag=u'micro_resistivity')
MeasurementType.micro_spherically_focused_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'micro spherically focused conductivity', tag=u'micro_spherically_focused_conductivity')
MeasurementType.micro_spherically_focused_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'micro spherically focused resistivity', tag=u'micro_spherically_focused_resistivity')
MeasurementType.mineral = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mineral', tag=u'mineral')
MeasurementType.mud_cake_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud cake conductivity', tag=u'mud_cake_conductivity')
MeasurementType.mud_cake_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud cake correction', tag=u'mud_cake_correction')
MeasurementType.mud_cake_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud cake density correction', tag=u'mud_cake_density_correction')
MeasurementType.mud_cake_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud cake resistivity', tag=u'mud_cake_resistivity')
MeasurementType.mud_cake_resistivity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud cake resistivity correction', tag=u'mud_cake_resistivity_correction')
MeasurementType.mud_cake_thickness_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud cake thickness correction', tag=u'mud_cake_thickness_correction')
MeasurementType.mud_composition_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud composition correction', tag=u'mud_composition_correction')
MeasurementType.mud_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud conductivity', tag=u'mud_conductivity')
MeasurementType.mud_filtrate_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud filtrate conductivity', tag=u'mud_filtrate_conductivity')
MeasurementType.mud_filtrate_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud filtrate correction', tag=u'mud_filtrate_correction')
MeasurementType.mud_filtrate_density_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud filtrate density correction', tag=u'mud_filtrate_density_correction')
MeasurementType.mud_filtrate_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud filtrate resistivity', tag=u'mud_filtrate_resistivity')
MeasurementType.mud_filtrate_resistivity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud filtrate resistivity correction', tag=u'mud_filtrate_resistivity_correction')
MeasurementType.mud_filtrate_salinity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud filtrate salinity correction', tag=u'mud_filtrate_salinity_correction')
MeasurementType.mud_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud resistivity', tag=u'mud_resistivity')
MeasurementType.mud_salinity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud salinity correction', tag=u'mud_salinity_correction')
MeasurementType.mud_viscosity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud viscosity correction', tag=u'mud_viscosity_correction')
MeasurementType.mud_weight_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'mud weight correction', tag=u'mud_weight_correction')
MeasurementType.neutron_die_away_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'neutron die away time', tag=u'neutron_die_away_time')
MeasurementType.neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'neutron porosity', tag=u'neutron_porosity')
MeasurementType.nuclear_caliper = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'nuclear caliper', tag=u'nuclear_caliper')
MeasurementType.nuclear_magnetic_decay_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'nuclear magnetic decay time', tag=u'nuclear_magnetic_decay_time')
MeasurementType.nuclear_magnetism_log_permeability = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'nuclear magnetism log permeability', tag=u'nuclear_magnetism_log_permeability')
MeasurementType.nuclear_magnetism_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'nuclear magnetism porosity', tag=u'nuclear_magnetism_porosity')
MeasurementType.OH_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'OH density porosity', tag=u'OH_density_porosity')
MeasurementType.OH_dolomite_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'OH dolomite density porosity', tag=u'OH_dolomite_density_porosity')
MeasurementType.OH_dolomite_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'OH dolomite neutron porosity', tag=u'OH_dolomite_neutron_porosity')
MeasurementType.OH_limestone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'OH limestone density porosity', tag=u'OH_limestone_density_porosity')
MeasurementType.OH_limestone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'OH limestone neutron porosity', tag=u'OH_limestone_neutron_porosity')
MeasurementType.OH_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'OH neutron porosity', tag=u'OH_neutron_porosity')
MeasurementType.OH_sandstone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'OH sandstone density porosity', tag=u'OH_sandstone_density_porosity')
MeasurementType.OH_sandstone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'OH sandstone neutron porosity', tag=u'OH_sandstone_neutron_porosity')
MeasurementType.oil_based_mud_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'oil based mud correction', tag=u'oil_based_mud_correction')
MeasurementType.oil_saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'oil saturation', tag=u'oil_saturation')
MeasurementType.perforating = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'perforating', tag=u'perforating')
MeasurementType.permeability = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'permeability', tag=u'permeability')
MeasurementType.phase_shift = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'phase shift', tag=u'phase_shift')
MeasurementType.photoelectric_absorption = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'photoelectric absorption', tag=u'photoelectric_absorption')
MeasurementType.photoelectric_absorption_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'photoelectric absorption correction', tag=u'photoelectric_absorption_correction')
MeasurementType.physical_measurement_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'physical measurement correction', tag=u'physical_measurement_correction')
MeasurementType.plane_angle = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'plane angle', tag=u'plane_angle')
MeasurementType.porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'porosity', tag=u'porosity')
MeasurementType.porosity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'porosity correction', tag=u'porosity_correction')
MeasurementType.potassium = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'potassium', tag=u'potassium')
MeasurementType.pressure = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'pressure', tag=u'pressure')
MeasurementType.pressure_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'pressure correction', tag=u'pressure_correction')
MeasurementType.processed = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'processed', tag=u'processed')
MeasurementType.pulsed_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'pulsed neutron porosity', tag=u'pulsed_neutron_porosity')
MeasurementType.quality = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'quality', tag=u'quality')
MeasurementType.ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'ratio', tag=u'ratio')
MeasurementType.raw = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'raw', tag=u'raw')
MeasurementType.relative_bearing = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'relative bearing', tag=u'relative_bearing')
MeasurementType.resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'resistivity', tag=u'resistivity')
MeasurementType.resistivity_factor_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'resistivity factor correction', tag=u'resistivity_factor_correction')
MeasurementType.resistivity_from_attenuation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'resistivity from attenuation', tag=u'resistivity_from_attenuation')
MeasurementType.resistivity_from_phase_shift = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'resistivity from phase shift', tag=u'resistivity_from_phase_shift')
MeasurementType.resistivity_phase_shift = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'resistivity phase shift', tag=u'resistivity_phase_shift')
MeasurementType.resistivity_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'resistivity ratio', tag=u'resistivity_ratio')
MeasurementType.salinity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'salinity', tag=u'salinity')
MeasurementType.sampling = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sampling', tag=u'sampling')
MeasurementType.sandstone_acoustic_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sandstone acoustic porosity', tag=u'sandstone_acoustic_porosity')
MeasurementType.sandstone_density_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sandstone density porosity', tag=u'sandstone_density_porosity')
MeasurementType.sandstone_neutron_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sandstone neutron porosity', tag=u'sandstone_neutron_porosity')
MeasurementType.saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'saturation', tag=u'saturation')
MeasurementType.shale_volume = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shale volume', tag=u'shale_volume')
MeasurementType.shallow_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shallow conductivity', tag=u'shallow_conductivity')
MeasurementType.shallow_induction_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shallow induction conductivity', tag=u'shallow_induction_conductivity')
MeasurementType.shallow_induction_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shallow induction resistivity', tag=u'shallow_induction_resistivity')
MeasurementType.shallow_laterolog_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shallow laterolog conductivity', tag=u'shallow_laterolog_conductivity')
MeasurementType.shallow_laterolog_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shallow laterolog resistivity', tag=u'shallow_laterolog_resistivity')
MeasurementType.shallow_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shallow resistivity', tag=u'shallow_resistivity')
MeasurementType.shear_wave_dolomite_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shear wave dolomite porosity', tag=u'shear_wave_dolomite_porosity')
MeasurementType.shear_wave_limestone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shear wave limestone porosity', tag=u'shear_wave_limestone_porosity')
MeasurementType.shear_wave_matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shear wave matrix travel time', tag=u'shear_wave_matrix_travel_time')
MeasurementType.shear_wave_sandstone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shear wave sandstone porosity', tag=u'shear_wave_sandstone_porosity')
MeasurementType.shear_wave_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shear wave travel time', tag=u'shear_wave_travel_time')
MeasurementType.shifted = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'shifted', tag=u'shifted')
MeasurementType.sidewall_core_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sidewall core porosity', tag=u'sidewall_core_porosity')
MeasurementType.sigma = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sigma', tag=u'sigma')
MeasurementType.sigma_formation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sigma formation', tag=u'sigma_formation')
MeasurementType.sigma_gas = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sigma gas', tag=u'sigma_gas')
MeasurementType.sigma_hydrocarbon = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sigma hydrocarbon', tag=u'sigma_hydrocarbon')
MeasurementType.sigma_matrix = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sigma matrix', tag=u'sigma_matrix')
MeasurementType.sigma_oil = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sigma oil', tag=u'sigma_oil')
MeasurementType.sigma_water = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'sigma water', tag=u'sigma_water')
MeasurementType.slippage_velocity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'slippage velocity correction', tag=u'slippage_velocity_correction')
MeasurementType.smoothed = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'smoothed', tag=u'smoothed')
MeasurementType.spectral_gamma_ray = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'spectral gamma ray', tag=u'spectral_gamma_ray')
MeasurementType.spherically_focused_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'spherically focused conductivity', tag=u'spherically_focused_conductivity')
MeasurementType.spherically_focused_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'spherically focused resistivity', tag=u'spherically_focused_resistivity')
MeasurementType.spontaneous_potential = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'spontaneous potential', tag=u'spontaneous_potential')
MeasurementType.spreading_loss_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'spreading loss correction', tag=u'spreading_loss_correction')
MeasurementType.synthetic_well_log_trace = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'synthetic well log trace', tag=u'synthetic_well_log_trace')
MeasurementType.temperature = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'temperature', tag=u'temperature')
MeasurementType.temperature_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'temperature correction', tag=u'temperature_correction')
MeasurementType.tension = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'tension', tag=u'tension')
MeasurementType.ThK_ratio = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'Th/K ratio', tag=u'ThK_ratio')
MeasurementType.thorium = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'thorium', tag=u'thorium')
MeasurementType.time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'time', tag=u'time')
MeasurementType.tool_diameter_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'tool diameter correction', tag=u'tool_diameter_correction')
MeasurementType.tool_eccentricity_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'tool eccentricity correction', tag=u'tool_eccentricity_correction')
MeasurementType.total_gamma_ray = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'total gamma ray', tag=u'total_gamma_ray')
MeasurementType.total_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'total porosity', tag=u'total_porosity')
MeasurementType.tracer_survey = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'tracer survey', tag=u'tracer_survey')
MeasurementType.travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'travel time', tag=u'travel_time')
MeasurementType.true_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'true conductivity', tag=u'true_conductivity')
MeasurementType.true_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'true resistivity', tag=u'true_resistivity')
MeasurementType.true_vertical_depth = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'true vertical depth', tag=u'true_vertical_depth')
MeasurementType.tube_wave_dolomite_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'tube wave dolomite porosity', tag=u'tube_wave_dolomite_porosity')
MeasurementType.tube_wave_limestone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'tube wave limestone porosity', tag=u'tube_wave_limestone_porosity')
MeasurementType.tube_wave_matrix_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'tube wave matrix travel time', tag=u'tube_wave_matrix_travel_time')
MeasurementType.tube_wave_sandstone_porosity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'tube wave sandstone porosity', tag=u'tube_wave_sandstone_porosity')
MeasurementType.tube_wave_travel_time = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'tube wave travel time', tag=u'tube_wave_travel_time')
MeasurementType.uranium = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'uranium', tag=u'uranium')
MeasurementType.velocity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'velocity', tag=u'velocity')
MeasurementType.volume = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'volume', tag=u'volume')
MeasurementType.water_based_fluid_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'water based fluid correction', tag=u'water_based_fluid_correction')
MeasurementType.water_holdup_correction = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'water holdup correction', tag=u'water_holdup_correction')
MeasurementType.water_saturated_conductivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'water saturated conductivity', tag=u'water_saturated_conductivity')
MeasurementType.water_saturated_resistivity = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'water saturated resistivity', tag=u'water_saturated_resistivity')
MeasurementType.water_saturation = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'water saturation', tag=u'water_saturation')
MeasurementType.unknown = MeasurementType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
MeasurementType._InitializeFacetMap(MeasurementType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MeasurementType', MeasurementType)

# Atomic simple type: {http://www.witsml.org/schemas/131}MessageProbability
class MessageProbability (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MessageProbability')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 3757, 1)
    _Documentation = None
MessageProbability._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageProbability, enum_prefix=None)
MessageProbability.low = MessageProbability._CF_enumeration.addEnumeration(unicode_value=u'low', tag=u'low')
MessageProbability.medium = MessageProbability._CF_enumeration.addEnumeration(unicode_value=u'medium', tag=u'medium')
MessageProbability.high = MessageProbability._CF_enumeration.addEnumeration(unicode_value=u'high', tag=u'high')
MessageProbability.unknown = MessageProbability._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
MessageProbability._InitializeFacetMap(MessageProbability._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MessageProbability', MessageProbability)

# Atomic simple type: {http://www.witsml.org/schemas/131}MessageSeverity
class MessageSeverity (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MessageSeverity')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 3784, 1)
    _Documentation = None
MessageSeverity._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageSeverity, enum_prefix=None)
MessageSeverity.catastrophic = MessageSeverity._CF_enumeration.addEnumeration(unicode_value=u'catastrophic', tag=u'catastrophic')
MessageSeverity.major = MessageSeverity._CF_enumeration.addEnumeration(unicode_value=u'major', tag=u'major')
MessageSeverity.minor = MessageSeverity._CF_enumeration.addEnumeration(unicode_value=u'minor', tag=u'minor')
MessageSeverity.unknown = MessageSeverity._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
MessageSeverity._InitializeFacetMap(MessageSeverity._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MessageSeverity', MessageSeverity)

# Atomic simple type: {http://www.witsml.org/schemas/131}MessageType
class MessageType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a message. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MessageType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 3811, 1)
    _Documentation = u'These values represent the type of a message. '
MessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageType, enum_prefix=None)
MessageType.alarm = MessageType._CF_enumeration.addEnumeration(unicode_value=u'alarm', tag=u'alarm')
MessageType.event = MessageType._CF_enumeration.addEnumeration(unicode_value=u'event', tag=u'event')
MessageType.informational = MessageType._CF_enumeration.addEnumeration(unicode_value=u'informational', tag=u'informational')
MessageType.warning = MessageType._CF_enumeration.addEnumeration(unicode_value=u'warning', tag=u'warning')
MessageType.unknown = MessageType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
MessageType._InitializeFacetMap(MessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MessageType', MessageType)

# Atomic simple type: {http://www.witsml.org/schemas/131}MudLogParameterType
class MudLogParameterType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """ "Text value" indicates that a text value is expected. 
			"Pressure value" indicates that an equivalentMudWeight value is expected.
			"Pressure gradient value" indicates that an equivalentMudWeight value is 
			  commonly expected but a pressureGradient value may also be specified.
			"Concentration value" indicates that a concentration value is expected.
			"Force value" indicates that a force value is expected.
			"Only" indicates that no other value is expected."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MudLogParameterType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 3846, 1)
    _Documentation = u'"Text value" indicates that a text value is expected. \n\t\t\t"Pressure value" indicates that an equivalentMudWeight value is expected.\n\t\t\t"Pressure gradient value" indicates that an equivalentMudWeight value is \n\t\t\t  commonly expected but a pressureGradient value may also be specified.\n\t\t\t"Concentration value" indicates that a concentration value is expected.\n\t\t\t"Force value" indicates that a force value is expected.\n\t\t\t"Only" indicates that no other value is expected.'
MudLogParameterType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MudLogParameterType, enum_prefix=None)
MudLogParameterType.bit_parameters = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'bit parameters', tag=u'bit_parameters')
MudLogParameterType.bit_type_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'bit type comment', tag=u'bit_type_comment')
MudLogParameterType.casing_point_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'casing point comment', tag=u'casing_point_comment')
MudLogParameterType.chromatograph_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'chromatograph comment', tag=u'chromatograph_comment')
MudLogParameterType.circulation_system_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'circulation system comment', tag=u'circulation_system_comment')
MudLogParameterType.core_interval_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'core interval comment', tag=u'core_interval_comment')
MudLogParameterType.cuttings_gas = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'cuttings gas', tag=u'cuttings_gas')
MudLogParameterType.direct_fracture_pressure = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'direct fracture pressure', tag=u'direct_fracture_pressure')
MudLogParameterType.direct_pore_pressure_measurements = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'direct pore pressure measurements', tag=u'direct_pore_pressure_measurements')
MudLogParameterType.drilling_data_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'drilling data comment', tag=u'drilling_data_comment')
MudLogParameterType.fracture_PG_estimate_most_likely = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'fracture PG estimate most likely', tag=u'fracture_PG_estimate_most_likely')
MudLogParameterType.gas_peaks_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'gas peaks comment', tag=u'gas_peaks_comment')
MudLogParameterType.gas_ratio_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'gas ratio comment', tag=u'gas_ratio_comment')
MudLogParameterType.general_engineering_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'general engineering comment', tag=u'general_engineering_comment')
MudLogParameterType.kicks_and_flows = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'kicks and flows', tag=u'kicks_and_flows')
MudLogParameterType.lithlog_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'lithlog comment', tag=u'lithlog_comment')
MudLogParameterType.lost_returns = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'lost returns', tag=u'lost_returns')
MudLogParameterType.LWD_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'LWD comment', tag=u'LWD_comment')
MudLogParameterType.marker_or_formation_top_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'marker or formation top comment', tag=u'marker_or_formation_top_comment')
MudLogParameterType.midnight_depth_date = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'midnight depth date', tag=u'midnight_depth_date')
MudLogParameterType.mud_check_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'mud check comment', tag=u'mud_check_comment')
MudLogParameterType.mud_data_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'mud data comment', tag=u'mud_data_comment')
MudLogParameterType.mudlog_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'mudlog comment', tag=u'mudlog_comment')
MudLogParameterType.overburden_gradient = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'overburden gradient', tag=u'overburden_gradient')
MudLogParameterType.overpull_on_connection = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'overpull on connection', tag=u'overpull_on_connection')
MudLogParameterType.overpull_on_trip = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'overpull on trip', tag=u'overpull_on_trip')
MudLogParameterType.pore_PG_estimate_most_likely = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'pore PG estimate most likely', tag=u'pore_PG_estimate_most_likely')
MudLogParameterType.pore_pressure_estimate_while_drilling = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'pore pressure estimate while drilling', tag=u'pore_pressure_estimate_while_drilling')
MudLogParameterType.pressure_data_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'pressure data comment', tag=u'pressure_data_comment')
MudLogParameterType.shale_density_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'shale density comment', tag=u'shale_density_comment')
MudLogParameterType.short_trip_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'short trip comment', tag=u'short_trip_comment')
MudLogParameterType.show_report_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'show report comment', tag=u'show_report_comment')
MudLogParameterType.sidewall_core_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'sidewall core comment', tag=u'sidewall_core_comment')
MudLogParameterType.sliding_Interval = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'sliding Interval', tag=u'sliding_Interval')
MudLogParameterType.steam_still_results_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'steam still results comment', tag=u'steam_still_results_comment')
MudLogParameterType.survey_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'survey comment', tag=u'survey_comment')
MudLogParameterType.temperature_data_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'temperature data comment', tag=u'temperature_data_comment')
MudLogParameterType.temperature_trend_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'temperature trend comment', tag=u'temperature_trend_comment')
MudLogParameterType.wireline_log_comment = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'wireline log comment', tag=u'wireline_log_comment')
MudLogParameterType.unknown = MudLogParameterType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
MudLogParameterType._InitializeFacetMap(MudLogParameterType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MudLogParameterType', MudLogParameterType)

# Atomic simple type: {http://www.witsml.org/schemas/131}NADTypes
class NADTypes (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NADTypes')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4108, 1)
    _Documentation = None
NADTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NADTypes, enum_prefix=None)
NADTypes.NAD27 = NADTypes._CF_enumeration.addEnumeration(unicode_value=u'NAD27', tag=u'NAD27')
NADTypes.NAD83 = NADTypes._CF_enumeration.addEnumeration(unicode_value=u'NAD83', tag=u'NAD83')
NADTypes.unknown = NADTypes._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
NADTypes._InitializeFacetMap(NADTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'NADTypes', NADTypes)

# Atomic simple type: {http://www.witsml.org/schemas/131}NameTagLocation
class NameTagLocation (abstractTypeEnum):

    """Defines the locations where an equipment tag might be found..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NameTagLocation')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4130, 1)
    _Documentation = u'Defines the locations where an equipment tag might be found..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagLocation._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'NameTagLocation', NameTagLocation)

# Atomic simple type: {http://www.witsml.org/schemas/131}NameTagNumberingScheme
class NameTagNumberingScheme (abstractTypeEnum):

    """Defines the specifications for creating equipment tags..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NameTagNumberingScheme')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4139, 1)
    _Documentation = u'Defines the specifications for creating equipment tags..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagNumberingScheme._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'NameTagNumberingScheme', NameTagNumberingScheme)

# Atomic simple type: {http://www.witsml.org/schemas/131}NameTagTechnology
class NameTagTechnology (abstractTypeEnum):

    """Defines the mechanisms for attaching an equipment tag to an item..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NameTagTechnology')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4148, 1)
    _Documentation = u'Defines the mechanisms for attaching an equipment tag to an item..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagTechnology._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'NameTagTechnology', NameTagTechnology)

# Atomic simple type: {http://www.witsml.org/schemas/131}NozzleType
class NozzleType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NozzleType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4157, 1)
    _Documentation = None
NozzleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NozzleType, enum_prefix=None)
NozzleType.extended = NozzleType._CF_enumeration.addEnumeration(unicode_value=u'extended', tag=u'extended')
NozzleType.normal = NozzleType._CF_enumeration.addEnumeration(unicode_value=u'normal', tag=u'normal')
NozzleType.unknown = NozzleType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
NozzleType._InitializeFacetMap(NozzleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'NozzleType', NozzleType)

# Atomic simple type: {http://www.witsml.org/schemas/131}OTDRReason
class OTDRReason (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The reason an Optical Time Domain Reflectometry (OTDR) 
			test was run within a  Distributed Temperature Survey (DTS)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OTDRReason')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4179, 1)
    _Documentation = u'The reason an Optical Time Domain Reflectometry (OTDR) \n\t\t\ttest was run within a  Distributed Temperature Survey (DTS).'
OTDRReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OTDRReason, enum_prefix=None)
OTDRReason.pre_installation = OTDRReason._CF_enumeration.addEnumeration(unicode_value=u'pre-installation', tag=u'pre_installation')
OTDRReason.post_installation = OTDRReason._CF_enumeration.addEnumeration(unicode_value=u'post-installation', tag=u'post_installation')
OTDRReason.DTS_run = OTDRReason._CF_enumeration.addEnumeration(unicode_value=u'DTS run', tag=u'DTS_run')
OTDRReason.other = OTDRReason._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
OTDRReason.unknown = OTDRReason._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
OTDRReason._InitializeFacetMap(OTDRReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'OTDRReason', OTDRReason)

# Atomic simple type: {http://www.witsml.org/schemas/131}PitType
class PitType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PitType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4217, 1)
    _Documentation = None
PitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PitType, enum_prefix=None)
PitType.bulk = PitType._CF_enumeration.addEnumeration(unicode_value=u'bulk', tag=u'bulk')
PitType.chemical = PitType._CF_enumeration.addEnumeration(unicode_value=u'chemical', tag=u'chemical')
PitType.drilling = PitType._CF_enumeration.addEnumeration(unicode_value=u'drilling', tag=u'drilling')
PitType.mix = PitType._CF_enumeration.addEnumeration(unicode_value=u'mix', tag=u'mix')
PitType.mud_cleaning = PitType._CF_enumeration.addEnumeration(unicode_value=u'mud cleaning', tag=u'mud_cleaning')
PitType.sand_trap = PitType._CF_enumeration.addEnumeration(unicode_value=u'sand trap', tag=u'sand_trap')
PitType.slug = PitType._CF_enumeration.addEnumeration(unicode_value=u'slug', tag=u'slug')
PitType.storage = PitType._CF_enumeration.addEnumeration(unicode_value=u'storage', tag=u'storage')
PitType.surge_tank = PitType._CF_enumeration.addEnumeration(unicode_value=u'surge tank', tag=u'surge_tank')
PitType.trip_tank = PitType._CF_enumeration.addEnumeration(unicode_value=u'trip tank', tag=u'trip_tank')
PitType.unknown = PitType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
PitType._InitializeFacetMap(PitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PitType', PitType)

# Atomic simple type: {http://www.witsml.org/schemas/131}Projection
class Projection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of coordinate system projection method.
			The source (except for "UserDefined") of the values is Geoshare V13. 
			For a detailed description of each value, see the Geoshare documentation of the 
			indicated "217" object at http://w3.posc.org/GeoshareSIG/technical/GDM/v13.0/."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Projection')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4283, 1)
    _Documentation = u'These values represent the type of coordinate system projection method.\n\t\t\tThe source (except for "UserDefined") of the values is Geoshare V13. \n\t\t\tFor a detailed description of each value, see the Geoshare documentation of the \n\t\t\tindicated "217" object at http://w3.posc.org/GeoshareSIG/technical/GDM/v13.0/.'
Projection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Projection, enum_prefix=None)
Projection.Albers_equal_area = Projection._CF_enumeration.addEnumeration(unicode_value=u'Albers equal area', tag=u'Albers_equal_area')
Projection.azimuthal_equidistant = Projection._CF_enumeration.addEnumeration(unicode_value=u'azimuthal equidistant', tag=u'azimuthal_equidistant')
Projection.Cassini = Projection._CF_enumeration.addEnumeration(unicode_value=u'Cassini', tag=u'Cassini')
Projection.equidistant_conic = Projection._CF_enumeration.addEnumeration(unicode_value=u'equidistant conic', tag=u'equidistant_conic')
Projection.equirectangular = Projection._CF_enumeration.addEnumeration(unicode_value=u'equirectangular', tag=u'equirectangular')
Projection.gnomonic = Projection._CF_enumeration.addEnumeration(unicode_value=u'gnomonic', tag=u'gnomonic')
Projection.Lambert_azimuthal = Projection._CF_enumeration.addEnumeration(unicode_value=u'Lambert azimuthal', tag=u'Lambert_azimuthal')
Projection.Lambert_conformal_conic = Projection._CF_enumeration.addEnumeration(unicode_value=u'Lambert conformal conic', tag=u'Lambert_conformal_conic')
Projection.Mercator = Projection._CF_enumeration.addEnumeration(unicode_value=u'Mercator', tag=u'Mercator')
Projection.Miller = Projection._CF_enumeration.addEnumeration(unicode_value=u'Miller', tag=u'Miller')
Projection.oblique_Mercator = Projection._CF_enumeration.addEnumeration(unicode_value=u'oblique Mercator', tag=u'oblique_Mercator')
Projection.orthographic = Projection._CF_enumeration.addEnumeration(unicode_value=u'orthographic', tag=u'orthographic')
Projection.perspective = Projection._CF_enumeration.addEnumeration(unicode_value=u'perspective', tag=u'perspective')
Projection.polar_stereographic = Projection._CF_enumeration.addEnumeration(unicode_value=u'polar stereographic', tag=u'polar_stereographic')
Projection.polyconic = Projection._CF_enumeration.addEnumeration(unicode_value=u'polyconic', tag=u'polyconic')
Projection.sinusoidal = Projection._CF_enumeration.addEnumeration(unicode_value=u'sinusoidal', tag=u'sinusoidal')
Projection.state_plane = Projection._CF_enumeration.addEnumeration(unicode_value=u'state plane', tag=u'state_plane')
Projection.stereographic = Projection._CF_enumeration.addEnumeration(unicode_value=u'stereographic', tag=u'stereographic')
Projection.transverse_Mercator = Projection._CF_enumeration.addEnumeration(unicode_value=u'transverse Mercator', tag=u'transverse_Mercator')
Projection.universal_transverse_Mercator = Projection._CF_enumeration.addEnumeration(unicode_value=u'universal transverse Mercator', tag=u'universal_transverse_Mercator')
Projection.user_defined = Projection._CF_enumeration.addEnumeration(unicode_value=u'user defined', tag=u'user_defined')
Projection.Van_der_Grinten = Projection._CF_enumeration.addEnumeration(unicode_value=u'Van der Grinten', tag=u'Van_der_Grinten')
Projection.unknown = Projection._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
Projection._InitializeFacetMap(Projection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Projection', Projection)

# Atomic simple type: {http://www.witsml.org/schemas/131}ProjectionVariantsObliqueMercator
class ProjectionVariantsObliqueMercator (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProjectionVariantsObliqueMercator')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4411, 1)
    _Documentation = None
ProjectionVariantsObliqueMercator._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProjectionVariantsObliqueMercator, enum_prefix=None)
ProjectionVariantsObliqueMercator.default = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value=u'default', tag=u'default')
ProjectionVariantsObliqueMercator.rectified = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value=u'rectified', tag=u'rectified')
ProjectionVariantsObliqueMercator.rectified_skew = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value=u'rectified skew', tag=u'rectified_skew')
ProjectionVariantsObliqueMercator.rectified_skew_center_origin = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value=u'rectified skew center origin', tag=u'rectified_skew_center_origin')
ProjectionVariantsObliqueMercator.unknown = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ProjectionVariantsObliqueMercator._InitializeFacetMap(ProjectionVariantsObliqueMercator._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ProjectionVariantsObliqueMercator', ProjectionVariantsObliqueMercator)

# Atomic simple type: {http://www.witsml.org/schemas/131}PumpType
class PumpType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a pump. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PumpType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4443, 1)
    _Documentation = u'These values represent the type of a pump. '
PumpType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PumpType, enum_prefix=None)
PumpType.centrifugal = PumpType._CF_enumeration.addEnumeration(unicode_value=u'centrifugal', tag=u'centrifugal')
PumpType.duplex = PumpType._CF_enumeration.addEnumeration(unicode_value=u'duplex', tag=u'duplex')
PumpType.triplex = PumpType._CF_enumeration.addEnumeration(unicode_value=u'triplex', tag=u'triplex')
PumpType.unknown = PumpType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
PumpType._InitializeFacetMap(PumpType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PumpType', PumpType)

# Atomic simple type: {http://www.witsml.org/schemas/131}PumpOpType
class PumpOpType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PumpOpType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4473, 1)
    _Documentation = None
PumpOpType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PumpOpType, enum_prefix=None)
PumpOpType.drilling = PumpOpType._CF_enumeration.addEnumeration(unicode_value=u'drilling', tag=u'drilling')
PumpOpType.reaming = PumpOpType._CF_enumeration.addEnumeration(unicode_value=u'reaming', tag=u'reaming')
PumpOpType.circulating = PumpOpType._CF_enumeration.addEnumeration(unicode_value=u'circulating', tag=u'circulating')
PumpOpType.slow_pump = PumpOpType._CF_enumeration.addEnumeration(unicode_value=u'slow pump', tag=u'slow_pump')
PumpOpType.unknown = PumpOpType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
PumpOpType._InitializeFacetMap(PumpOpType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PumpOpType', PumpOpType)

# Atomic simple type: {http://www.witsml.org/schemas/131}QualifierType
class QualifierType (abstractTypeEnum):

    """The type of qualifier of a lithology.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QualifierType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4505, 1)
    _Documentation = u'The type of qualifier of a lithology.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
QualifierType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'QualifierType', QualifierType)

# Atomic simple type: {http://www.witsml.org/schemas/131}RealtimeData
class RealtimeData (abstractTypeEnum):

    """These values represent the name of a recording channel.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RealtimeData')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4514, 1)
    _Documentation = u'These values represent the name of a recording channel.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
RealtimeData._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'RealtimeData', RealtimeData)

# Atomic simple type: {http://www.witsml.org/schemas/131}RigType
class RigType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drilling rig. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RigType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4523, 1)
    _Documentation = u'These values represent the type of drilling rig. '
RigType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RigType, enum_prefix=None)
RigType.barge = RigType._CF_enumeration.addEnumeration(unicode_value=u'barge', tag=u'barge')
RigType.coiled_tubing = RigType._CF_enumeration.addEnumeration(unicode_value=u'coiled tubing', tag=u'coiled_tubing')
RigType.floater = RigType._CF_enumeration.addEnumeration(unicode_value=u'floater', tag=u'floater')
RigType.jackup = RigType._CF_enumeration.addEnumeration(unicode_value=u'jackup', tag=u'jackup')
RigType.land = RigType._CF_enumeration.addEnumeration(unicode_value=u'land', tag=u'land')
RigType.platform = RigType._CF_enumeration.addEnumeration(unicode_value=u'platform', tag=u'platform')
RigType.semi_submersible = RigType._CF_enumeration.addEnumeration(unicode_value=u'semi-submersible', tag=u'semi_submersible')
RigType.unknown = RigType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
RigType._InitializeFacetMap(RigType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RigType', RigType)

# Atomic simple type: {http://www.witsml.org/schemas/131}RiskAffectedPersonnel
class RiskAffectedPersonnel (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Personnel affected by a risk."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RiskAffectedPersonnel')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4573, 1)
    _Documentation = u'Personnel affected by a risk.'
RiskAffectedPersonnel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RiskAffectedPersonnel, enum_prefix=None)
RiskAffectedPersonnel.cementer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'cementer', tag=u'cementer')
RiskAffectedPersonnel.company_man = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'company man', tag=u'company_man')
RiskAffectedPersonnel.contractor = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'contractor', tag=u'contractor')
RiskAffectedPersonnel.directional_driller = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'directional driller', tag=u'directional_driller')
RiskAffectedPersonnel.driller = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'driller', tag=u'driller')
RiskAffectedPersonnel.drilling_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'drilling engineer', tag=u'drilling_engineer')
RiskAffectedPersonnel.drilling_superintendent = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'drilling superintendent', tag=u'drilling_superintendent')
RiskAffectedPersonnel.drilling_team = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'drilling team', tag=u'drilling_team')
RiskAffectedPersonnel.facility_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'facility engineer', tag=u'facility_engineer')
RiskAffectedPersonnel.field_service_manager = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'field service manager', tag=u'field_service_manager')
RiskAffectedPersonnel.foreman = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'foreman', tag=u'foreman')
RiskAffectedPersonnel.general_service_supervisor = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'general service supervisor', tag=u'general_service_supervisor')
RiskAffectedPersonnel.geologist = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'geologist', tag=u'geologist')
RiskAffectedPersonnel.member = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'member', tag=u'member')
RiskAffectedPersonnel.mud_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'mud engineer', tag=u'mud_engineer')
RiskAffectedPersonnel.mud_logger = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'mud logger', tag=u'mud_logger')
RiskAffectedPersonnel.MWD_or_LWD_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'MWD or LWD engineer', tag=u'MWD_or_LWD_engineer')
RiskAffectedPersonnel.perform_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'perform engineer', tag=u'perform_engineer')
RiskAffectedPersonnel.petrophysicist = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'petrophysicist', tag=u'petrophysicist')
RiskAffectedPersonnel.production_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'production engineer', tag=u'production_engineer')
RiskAffectedPersonnel.remotely_operated_vehicle_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'remotely operated vehicle engineer', tag=u'remotely_operated_vehicle_engineer')
RiskAffectedPersonnel.safety_manger = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'safety manger', tag=u'safety_manger')
RiskAffectedPersonnel.sales_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'sales engineer', tag=u'sales_engineer')
RiskAffectedPersonnel.service_supervisor = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'service supervisor', tag=u'service_supervisor')
RiskAffectedPersonnel.technical_support = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'technical support', tag=u'technical_support')
RiskAffectedPersonnel.tool_pusher = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'tool pusher', tag=u'tool_pusher')
RiskAffectedPersonnel.wireline_engineer = RiskAffectedPersonnel._CF_enumeration.addEnumeration(unicode_value=u'wireline engineer', tag=u'wireline_engineer')
RiskAffectedPersonnel._InitializeFacetMap(RiskAffectedPersonnel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RiskAffectedPersonnel', RiskAffectedPersonnel)

# Atomic simple type: {http://www.witsml.org/schemas/131}RiskCategory
class RiskCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of slow circulation rate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RiskCategory')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4716, 1)
    _Documentation = u'Type of slow circulation rate.'
RiskCategory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RiskCategory, enum_prefix=None)
RiskCategory.hydraulics = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'hydraulics', tag=u'hydraulics')
RiskCategory.mechanical = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'mechanical', tag=u'mechanical')
RiskCategory.time_related = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'time related', tag=u'time_related')
RiskCategory.wellbore_stability = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'wellbore stability', tag=u'wellbore_stability')
RiskCategory.directional_drilling = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'directional drilling', tag=u'directional_drilling')
RiskCategory.bit = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'bit', tag=u'bit')
RiskCategory.equipment_failure = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'equipment failure', tag=u'equipment_failure')
RiskCategory.completion = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'completion', tag=u'completion')
RiskCategory.casing = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'casing', tag=u'casing')
RiskCategory.other = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
RiskCategory.HSE = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'HSE', tag=u'HSE')
RiskCategory.unknown = RiskCategory._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
RiskCategory._InitializeFacetMap(RiskCategory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RiskCategory', RiskCategory)

# Atomic simple type: {http://www.witsml.org/schemas/131}RiskSubCategory
class RiskSubCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Risk Sub-Categories."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RiskSubCategory')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 4786, 1)
    _Documentation = u'Risk Sub-Categories.'
RiskSubCategory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RiskSubCategory, enum_prefix=None)
RiskSubCategory.gas_kick = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'gas kick', tag=u'gas_kick')
RiskSubCategory.shallow_water_influx = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'shallow water influx', tag=u'shallow_water_influx')
RiskSubCategory.other_influx_or_kicks = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'other influx or kicks', tag=u'other_influx_or_kicks')
RiskSubCategory.loss_circulation = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'loss circulation', tag=u'loss_circulation')
RiskSubCategory.poor_hole_cleaning = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'poor hole cleaning', tag=u'poor_hole_cleaning')
RiskSubCategory.good_hole_cleaning_at_high_ROP = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'good hole cleaning at high ROP', tag=u'good_hole_cleaning_at_high_ROP')
RiskSubCategory.high_mud_weight = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'high mud weight', tag=u'high_mud_weight')
RiskSubCategory.special_additives_needed = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'special additives needed', tag=u'special_additives_needed')
RiskSubCategory.gumbo_problems = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'gumbo problems', tag=u'gumbo_problems')
RiskSubCategory.high_ECD___rheology_related = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'high ECD - rheology related', tag=u'high_ECD___rheology_related')
RiskSubCategory.excessive_circulation = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'excessive circulation', tag=u'excessive_circulation')
RiskSubCategory.performing_a_kill = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'performing a kill', tag=u'performing_a_kill')
RiskSubCategory.mud_weight_change = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'mud weight change', tag=u'mud_weight_change')
RiskSubCategory.excessive_pipe_cement_scaling = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'excessive pipe cement scaling', tag=u'excessive_pipe_cement_scaling')
RiskSubCategory.pit_gain_or_loss = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'pit gain or loss', tag=u'pit_gain_or_loss')
RiskSubCategory.mud_stability_problems = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'mud stability problems', tag=u'mud_stability_problems')
RiskSubCategory.shallow_gas_flow = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'shallow gas flow', tag=u'shallow_gas_flow')
RiskSubCategory.twist_off = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'twist off', tag=u'twist_off')
RiskSubCategory.stuck_pipe = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'stuck pipe', tag=u'stuck_pipe')
RiskSubCategory.wireline_stuck_in_hole = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'wireline stuck in hole', tag=u'wireline_stuck_in_hole')
RiskSubCategory.stick_and_slip = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'stick and slip', tag=u'stick_and_slip')
RiskSubCategory.vibration___axial = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'vibration - axial', tag=u'vibration___axial')
RiskSubCategory.vibration___torsional = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'vibration - torsional', tag=u'vibration___torsional')
RiskSubCategory.vibration___transverse = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'vibration - transverse', tag=u'vibration___transverse')
RiskSubCategory.vibration_unknown_or_rough_drilling = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'vibration unknown or rough drilling', tag=u'vibration_unknown_or_rough_drilling')
RiskSubCategory.uneven_wear_of_BHA = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'uneven wear of BHA', tag=u'uneven_wear_of_BHA')
RiskSubCategory.uneven_wear_of_drillstring = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'uneven wear of drillstring', tag=u'uneven_wear_of_drillstring')
RiskSubCategory.excessive_torque = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'excessive torque', tag=u'excessive_torque')
RiskSubCategory.excessive_drag = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'excessive drag', tag=u'excessive_drag')
RiskSubCategory.reaming_greater_than_2_hours = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'reaming greater than 2 hours', tag=u'reaming_greater_than_2_hours')
RiskSubCategory.washouts = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'washouts', tag=u'washouts')
RiskSubCategory.tight_hole_or_overPull = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'tight hole or overPull', tag=u'tight_hole_or_overPull')
RiskSubCategory.failed_inspections_or_fatigue_wear = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'failed inspections or fatigue wear', tag=u'failed_inspections_or_fatigue_wear')
RiskSubCategory.mechanical = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'mechanical', tag=u'mechanical')
RiskSubCategory.drilling_greater_than_1000_feetday = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'drilling greater than 1000 feet/day', tag=u'drilling_greater_than_1000_feetday')
RiskSubCategory.drilling_greater_than_2000_feetday = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'drilling greater than 2000 feet/day', tag=u'drilling_greater_than_2000_feetday')
RiskSubCategory.drilling_less_than_20_feetday = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'drilling less than 20 feet/day', tag=u'drilling_less_than_20_feetday')
RiskSubCategory.trips_greater_than_24_hours = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'trips greater than 24 hours', tag=u'trips_greater_than_24_hours')
RiskSubCategory.excessive_time_for_BHA_makeup = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'excessive time for BHA makeup', tag=u'excessive_time_for_BHA_makeup')
RiskSubCategory.waiting_on_decisions = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'waiting on decisions', tag=u'waiting_on_decisions')
RiskSubCategory.waiting_on_weather = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'waiting on weather', tag=u'waiting_on_weather')
RiskSubCategory.waiting_on_tools = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'waiting on tools', tag=u'waiting_on_tools')
RiskSubCategory.sloughing_or_packoffs = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'sloughing or packoffs', tag=u'sloughing_or_packoffs')
RiskSubCategory.ballooning = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'ballooning', tag=u'ballooning')
RiskSubCategory.fracture_problems = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'fracture problems', tag=u'fracture_problems')
RiskSubCategory.unstable_zones = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'unstable zones', tag=u'unstable_zones')
RiskSubCategory.formation_integrity_test = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'formation integrity test', tag=u'formation_integrity_test')
RiskSubCategory.leak_off_test = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'leak-off test', tag=u'leak_off_test')
RiskSubCategory.tectonics = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'tectonics', tag=u'tectonics')
RiskSubCategory.pore_pressure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'pore pressure', tag=u'pore_pressure')
RiskSubCategory.breakouts = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'breakouts', tag=u'breakouts')
RiskSubCategory.bed_parallel = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'bed parallel', tag=u'bed_parallel')
RiskSubCategory.wellbore_stability = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'wellbore stability', tag=u'wellbore_stability')
RiskSubCategory.excessive_doglegs = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'excessive doglegs', tag=u'excessive_doglegs')
RiskSubCategory.sidetrack = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'sidetrack', tag=u'sidetrack')
RiskSubCategory.BHA_change_for_directional = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'BHA change for directional', tag=u'BHA_change_for_directional')
RiskSubCategory.wrong_total_flow_area = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'wrong total flow area', tag=u'wrong_total_flow_area')
RiskSubCategory.well_collision___actual = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'well collision - actual', tag=u'well_collision___actual')
RiskSubCategory.well_collision___technical = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'well collision - technical', tag=u'well_collision___technical')
RiskSubCategory.geosteering = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'geosteering', tag=u'geosteering')
RiskSubCategory.abnormal_tendency_changes = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'abnormal tendency changes', tag=u'abnormal_tendency_changes')
RiskSubCategory.resurveying = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'resurveying', tag=u'resurveying')
RiskSubCategory.in_field_referencing_IFR_actions = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'in-field referencing (IFR) actions', tag=u'in_field_referencing_IFR_actions')
RiskSubCategory.bit_or_BHA_performance = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'bit or BHA performance', tag=u'bit_or_BHA_performance')
RiskSubCategory.drilling_optimization = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'drilling optimization', tag=u'drilling_optimization')
RiskSubCategory.bit_balling = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'bit balling', tag=u'bit_balling')
RiskSubCategory.lost_cones_or_broken_cutters = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'lost cones or broken cutters', tag=u'lost_cones_or_broken_cutters')
RiskSubCategory.excessive_bit_wear_or_gauge = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'excessive bit wear or gauge', tag=u'excessive_bit_wear_or_gauge')
RiskSubCategory.low_rate_of_bit_penetration = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'low rate of bit penetration', tag=u'low_rate_of_bit_penetration')
RiskSubCategory.high_rate_of_bit_penetration = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'high rate of bit penetration', tag=u'high_rate_of_bit_penetration')
RiskSubCategory.downhole_tool = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'downhole tool', tag=u'downhole_tool')
RiskSubCategory.surface_system = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'surface system', tag=u'surface_system')
RiskSubCategory.motor_or_rotary_steerable_system_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'motor or rotary steerable system failure', tag=u'motor_or_rotary_steerable_system_failure')
RiskSubCategory.topdrive_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'topdrive failure', tag=u'topdrive_failure')
RiskSubCategory.hoisting_equipment_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'hoisting equipment failure', tag=u'hoisting_equipment_failure')
RiskSubCategory.circulating_equipment_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'circulating equipment failure', tag=u'circulating_equipment_failure')
RiskSubCategory.electrical_system_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'electrical system failure', tag=u'electrical_system_failure')
RiskSubCategory.blow_out_preventer_events = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'blow out preventer events', tag=u'blow_out_preventer_events')
RiskSubCategory.surface_instrumentation_problems = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'surface instrumentation problems', tag=u'surface_instrumentation_problems')
RiskSubCategory.rig_communications = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'rig communications', tag=u'rig_communications')
RiskSubCategory.completion_equipment_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'completion equipment failure', tag=u'completion_equipment_failure')
RiskSubCategory.miscellaneous_rig_equipment = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'miscellaneous rig equipment', tag=u'miscellaneous_rig_equipment')
RiskSubCategory.tool_or_equipment_failure = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'tool or equipment failure', tag=u'tool_or_equipment_failure')
RiskSubCategory.squeeze_jobs = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'squeeze jobs', tag=u'squeeze_jobs')
RiskSubCategory.casing_surge_losses = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'casing surge losses', tag=u'casing_surge_losses')
RiskSubCategory.stuck_casing_or_completion = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'stuck casing or completion', tag=u'stuck_casing_or_completion')
RiskSubCategory.shoe_failures = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'shoe failures', tag=u'shoe_failures')
RiskSubCategory.early_cement_setup = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'early cement setup', tag=u'early_cement_setup')
RiskSubCategory.casing_collapse = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'casing collapse', tag=u'casing_collapse')
RiskSubCategory.milling = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'milling', tag=u'milling')
RiskSubCategory.excessive_casing_wear_or_cuttings = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'excessive casing wear or cuttings', tag=u'excessive_casing_wear_or_cuttings')
RiskSubCategory.excessive_formation_damage_or_skin = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'excessive formation damage or skin', tag=u'excessive_formation_damage_or_skin')
RiskSubCategory.casing_rotation_or_reciprocation_rqd = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'casing rotation or reciprocation rqd', tag=u'casing_rotation_or_reciprocation_rqd')
RiskSubCategory.broaching = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'broaching', tag=u'broaching')
RiskSubCategory.completion_or_casing = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'completion or casing', tag=u'completion_or_casing')
RiskSubCategory.stratigraphy = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'stratigraphy', tag=u'stratigraphy')
RiskSubCategory.fishing = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'fishing', tag=u'fishing')
RiskSubCategory.junk_in_hole = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'junk in hole', tag=u'junk_in_hole')
RiskSubCategory.delay_due_to_political_unrest = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'delay due to political unrest', tag=u'delay_due_to_political_unrest')
RiskSubCategory.rig_move = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'rig move', tag=u'rig_move')
RiskSubCategory.gas_hydrates = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'gas hydrates', tag=u'gas_hydrates')
RiskSubCategory.pending_analysis = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'pending analysis', tag=u'pending_analysis')
RiskSubCategory.riser_disconnect = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'riser disconnect', tag=u'riser_disconnect')
RiskSubCategory.other = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
RiskSubCategory.personnel = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'personnel', tag=u'personnel')
RiskSubCategory.environmental = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'environmental', tag=u'environmental')
RiskSubCategory.automotive = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'automotive', tag=u'automotive')
RiskSubCategory.asset = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'asset', tag=u'asset')
RiskSubCategory.information = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'information', tag=u'information')
RiskSubCategory.time = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'time', tag=u'time')
RiskSubCategory.HSE = RiskSubCategory._CF_enumeration.addEnumeration(unicode_value=u'HSE', tag=u'HSE')
RiskSubCategory._InitializeFacetMap(RiskSubCategory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RiskSubCategory', RiskSubCategory)

# Atomic simple type: {http://www.witsml.org/schemas/131}RiskType
class RiskType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Types of risk."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RiskType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5349, 1)
    _Documentation = u'Types of risk.'
RiskType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RiskType, enum_prefix=None)
RiskType.risk = RiskType._CF_enumeration.addEnumeration(unicode_value=u'risk', tag=u'risk')
RiskType.event = RiskType._CF_enumeration.addEnumeration(unicode_value=u'event', tag=u'event')
RiskType.near_miss = RiskType._CF_enumeration.addEnumeration(unicode_value=u'near miss', tag=u'near_miss')
RiskType.best_practice = RiskType._CF_enumeration.addEnumeration(unicode_value=u'best practice', tag=u'best_practice')
RiskType.lessons_learned = RiskType._CF_enumeration.addEnumeration(unicode_value=u'lessons learned', tag=u'lessons_learned')
RiskType.other = RiskType._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
RiskType.unknown = RiskType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
RiskType._InitializeFacetMap(RiskType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RiskType', RiskType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ScrType
class ScrType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of slow circulation rate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ScrType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5394, 1)
    _Documentation = u'Type of slow circulation rate.'
ScrType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ScrType, enum_prefix=None)
ScrType.string_annulus = ScrType._CF_enumeration.addEnumeration(unicode_value=u'string annulus', tag=u'string_annulus')
ScrType.string_kill_line = ScrType._CF_enumeration.addEnumeration(unicode_value=u'string kill line', tag=u'string_kill_line')
ScrType.string_choke_line = ScrType._CF_enumeration.addEnumeration(unicode_value=u'string choke line', tag=u'string_choke_line')
ScrType.unknown = ScrType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ScrType._InitializeFacetMap(ScrType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ScrType', ScrType)

# Atomic simple type: {http://www.witsml.org/schemas/131}ShowFluorescence
class ShowFluorescence (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ShowFluorescence')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5424, 1)
    _Documentation = None
ShowFluorescence._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowFluorescence, enum_prefix=None)
ShowFluorescence.faint = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value=u'faint', tag=u'faint')
ShowFluorescence.bright = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value=u'bright', tag=u'bright')
ShowFluorescence.none = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
ShowFluorescence.unknown = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ShowFluorescence._InitializeFacetMap(ShowFluorescence._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ShowFluorescence', ShowFluorescence)

# Atomic simple type: {http://www.witsml.org/schemas/131}ShowLevel
class ShowLevel (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ShowLevel')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5451, 1)
    _Documentation = None
ShowLevel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowLevel, enum_prefix=None)
ShowLevel.blooming = ShowLevel._CF_enumeration.addEnumeration(unicode_value=u'blooming', tag=u'blooming')
ShowLevel.streaming = ShowLevel._CF_enumeration.addEnumeration(unicode_value=u'streaming', tag=u'streaming')
ShowLevel.unknown = ShowLevel._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ShowLevel._InitializeFacetMap(ShowLevel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ShowLevel', ShowLevel)

# Atomic simple type: {http://www.witsml.org/schemas/131}ShowRating
class ShowRating (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ShowRating')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5473, 1)
    _Documentation = None
ShowRating._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowRating, enum_prefix=None)
ShowRating.none = ShowRating._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
ShowRating.very_poor = ShowRating._CF_enumeration.addEnumeration(unicode_value=u'very poor', tag=u'very_poor')
ShowRating.poor = ShowRating._CF_enumeration.addEnumeration(unicode_value=u'poor', tag=u'poor')
ShowRating.fair = ShowRating._CF_enumeration.addEnumeration(unicode_value=u'fair', tag=u'fair')
ShowRating.good = ShowRating._CF_enumeration.addEnumeration(unicode_value=u'good', tag=u'good')
ShowRating.very_good = ShowRating._CF_enumeration.addEnumeration(unicode_value=u'very good', tag=u'very_good')
ShowRating.unknown = ShowRating._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ShowRating._InitializeFacetMap(ShowRating._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ShowRating', ShowRating)

# Atomic simple type: {http://www.witsml.org/schemas/131}ShowSpeed
class ShowSpeed (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ShowSpeed')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5515, 1)
    _Documentation = None
ShowSpeed._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowSpeed, enum_prefix=None)
ShowSpeed.slow = ShowSpeed._CF_enumeration.addEnumeration(unicode_value=u'slow', tag=u'slow')
ShowSpeed.moderately_fast = ShowSpeed._CF_enumeration.addEnumeration(unicode_value=u'moderately fast', tag=u'moderately_fast')
ShowSpeed.fast = ShowSpeed._CF_enumeration.addEnumeration(unicode_value=u'fast', tag=u'fast')
ShowSpeed.instantaneous = ShowSpeed._CF_enumeration.addEnumeration(unicode_value=u'instantaneous', tag=u'instantaneous')
ShowSpeed.none = ShowSpeed._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
ShowSpeed.unknown = ShowSpeed._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ShowSpeed._InitializeFacetMap(ShowSpeed._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ShowSpeed', ShowSpeed)

# Atomic simple type: {http://www.witsml.org/schemas/131}SupportCraft
class SupportCraft (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SupportCraft')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5552, 1)
    _Documentation = None
SupportCraft._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SupportCraft, enum_prefix=None)
SupportCraft.barge = SupportCraft._CF_enumeration.addEnumeration(unicode_value=u'barge', tag=u'barge')
SupportCraft.standby_boat = SupportCraft._CF_enumeration.addEnumeration(unicode_value=u'standby boat', tag=u'standby_boat')
SupportCraft.helicopter = SupportCraft._CF_enumeration.addEnumeration(unicode_value=u'helicopter', tag=u'helicopter')
SupportCraft.supply_boat = SupportCraft._CF_enumeration.addEnumeration(unicode_value=u'supply boat', tag=u'supply_boat')
SupportCraft.truck = SupportCraft._CF_enumeration.addEnumeration(unicode_value=u'truck', tag=u'truck')
SupportCraft.crew_vehicle = SupportCraft._CF_enumeration.addEnumeration(unicode_value=u'crew vehicle', tag=u'crew_vehicle')
SupportCraft.tug_boat = SupportCraft._CF_enumeration.addEnumeration(unicode_value=u'tug boat', tag=u'tug_boat')
SupportCraft.unknown = SupportCraft._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
SupportCraft._InitializeFacetMap(SupportCraft._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SupportCraft', SupportCraft)

# Atomic simple type: {http://www.witsml.org/schemas/131}SurfEquipType
class SurfEquipType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SurfEquipType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5600, 1)
    _Documentation = None
SurfEquipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SurfEquipType, enum_prefix=None)
SurfEquipType.IADC = SurfEquipType._CF_enumeration.addEnumeration(unicode_value=u'IADC', tag=u'IADC')
SurfEquipType.custom = SurfEquipType._CF_enumeration.addEnumeration(unicode_value=u'custom', tag=u'custom')
SurfEquipType.coiled_tubing = SurfEquipType._CF_enumeration.addEnumeration(unicode_value=u'coiled tubing', tag=u'coiled_tubing')
SurfEquipType.unknown = SurfEquipType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
SurfEquipType._InitializeFacetMap(SurfEquipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SurfEquipType', SurfEquipType)

# Atomic simple type: {http://www.witsml.org/schemas/131}TargetCategory
class TargetCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TargetCategory')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5627, 1)
    _Documentation = None
TargetCategory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetCategory, enum_prefix=None)
TargetCategory.geological = TargetCategory._CF_enumeration.addEnumeration(unicode_value=u'geological', tag=u'geological')
TargetCategory.unknown = TargetCategory._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TargetCategory._InitializeFacetMap(TargetCategory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TargetCategory', TargetCategory)

# Atomic simple type: {http://www.witsml.org/schemas/131}TargetScope
class TargetScope (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of scope of the drilling target. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TargetScope')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5644, 1)
    _Documentation = u'These values represent the type of scope of the drilling target. '
TargetScope._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetScope, enum_prefix=None)
TargetScope.n3D_volume = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'3D volume', tag=u'n3D_volume')
TargetScope.ellipsoid = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'ellipsoid', tag=u'ellipsoid')
TargetScope.elliptical = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'elliptical', tag=u'elliptical')
TargetScope.hardLine = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'hardLine', tag=u'hardLine')
TargetScope.irregular = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'irregular', tag=u'irregular')
TargetScope.lease_line = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'lease line', tag=u'lease_line')
TargetScope.line = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'line', tag=u'line')
TargetScope.plane = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'plane', tag=u'plane')
TargetScope.point = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'point', tag=u'point')
TargetScope.rectangular = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'rectangular', tag=u'rectangular')
TargetScope.unknown = TargetScope._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TargetScope._InitializeFacetMap(TargetScope._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TargetScope', TargetScope)

# Atomic simple type: {http://www.witsml.org/schemas/131}TargetSectionScope
class TargetSectionScope (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of scope of a section that describes a target. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TargetSectionScope')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5710, 1)
    _Documentation = u'These values represent the type of scope of a section that describes a target. '
TargetSectionScope._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetSectionScope, enum_prefix=None)
TargetSectionScope.arc = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value=u'arc', tag=u'arc')
TargetSectionScope.line = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value=u'line', tag=u'line')
TargetSectionScope.unknown = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TargetSectionScope._InitializeFacetMap(TargetSectionScope._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TargetSectionScope', TargetSectionScope)

# Atomic simple type: {http://www.witsml.org/schemas/131}TrajStationStatus
class TrajStationStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TrajStationStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5736, 1)
    _Documentation = None
TrajStationStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TrajStationStatus, enum_prefix=None)
TrajStationStatus.locked = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value=u'locked', tag=u'locked')
TrajStationStatus.open = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value=u'open', tag=u'open')
TrajStationStatus.rejected = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value=u'rejected', tag=u'rejected')
TrajStationStatus.valid = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value=u'valid', tag=u'valid')
TrajStationStatus.position = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value=u'position', tag=u'position')
TrajStationStatus.unknown = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TrajStationStatus._InitializeFacetMap(TrajStationStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TrajStationStatus', TrajStationStatus)

# Atomic simple type: {http://www.witsml.org/schemas/131}TrajStationType
class TrajStationType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a directional survey station. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TrajStationType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 5773, 1)
    _Documentation = u'These values represent the type of a directional survey station. '
TrajStationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TrajStationType, enum_prefix=None)
TrajStationType.azimuth_on_plane = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'azimuth on plane', tag=u'azimuth_on_plane')
TrajStationType.buildrate_to_delta_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'buildrate to delta-MD', tag=u'buildrate_to_delta_MD')
TrajStationType.buildrate_to_INCL = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'buildrate to INCL', tag=u'buildrate_to_INCL')
TrajStationType.buildrate_to_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'buildrate to MD', tag=u'buildrate_to_MD')
TrajStationType.buildrate_and_turnrate_to_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'buildrate and turnrate to AZI', tag=u'buildrate_and_turnrate_to_AZI')
TrajStationType.buildrate_and_turnrate_to_delta_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'buildrate and turnrate to delta-MD', tag=u'buildrate_and_turnrate_to_delta_MD')
TrajStationType.buildrate_and_turnrate_to_INCL = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'buildrate and turnrate to INCL', tag=u'buildrate_and_turnrate_to_INCL')
TrajStationType.buildrate_and_turnrate_to_INCL_and_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'buildrate and turnrate to INCL and AZI', tag=u'buildrate_and_turnrate_to_INCL_and_AZI')
TrajStationType.buildrate_and_turnrate_to_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'buildrate and turnrate to MD', tag=u'buildrate_and_turnrate_to_MD')
TrajStationType.buildrate_and_turnrate_to_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'buildrate and turnrate to TVD', tag=u'buildrate_and_turnrate_to_TVD')
TrajStationType.buildrate_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'buildrate TVD', tag=u'buildrate_TVD')
TrajStationType.casing_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'casing MD', tag=u'casing_MD')
TrajStationType.casing_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'casing TVD', tag=u'casing_TVD')
TrajStationType.DLS = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS', tag=u'DLS')
TrajStationType.DLS_to_AZI_and_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS to AZI and MD', tag=u'DLS_to_AZI_and_MD')
TrajStationType.DLS_to_AZI_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS to AZI-TVD', tag=u'DLS_to_AZI_TVD')
TrajStationType.DLS_to_INCL = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS to INCL', tag=u'DLS_to_INCL')
TrajStationType.DLS_to_INCL_and_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS to INCL and AZI', tag=u'DLS_to_INCL_and_AZI')
TrajStationType.DLS_to_INCL_and_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS to INCL and MD', tag=u'DLS_to_INCL_and_MD')
TrajStationType.DLS_to_INCL_and_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS to INCL and TVD', tag=u'DLS_to_INCL_and_TVD')
TrajStationType.DLS_to_NS_EW_and_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS to NS, EW and TVD', tag=u'DLS_to_NS_EW_and_TVD')
TrajStationType.DLS_and_toolface_to_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS and toolface to AZI', tag=u'DLS_and_toolface_to_AZI')
TrajStationType.DLS_and_toolface_to_delta_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS and toolface to delta-MD', tag=u'DLS_and_toolface_to_delta_MD')
TrajStationType.DLS_and_toolface_to_INCL = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS and toolface to INCL', tag=u'DLS_and_toolface_to_INCL')
TrajStationType.DLS_and_toolface_to_INCL_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS and toolface to INCL-AZI', tag=u'DLS_and_toolface_to_INCL_AZI')
TrajStationType.DLS_and_toolface_to_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS and toolface to MD', tag=u'DLS_and_toolface_to_MD')
TrajStationType.DLS_and_toolface_to_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'DLS and toolface to TVD', tag=u'DLS_and_toolface_to_TVD')
TrajStationType.formation_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'formation MD', tag=u'formation_MD')
TrajStationType.formation_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'formation TVD', tag=u'formation_TVD')
TrajStationType.gyro_inertial = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'gyro inertial', tag=u'gyro_inertial')
TrajStationType.gyro_MWD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'gyro MWD', tag=u'gyro_MWD')
TrajStationType.gyro_north_seeking = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'gyro north seeking', tag=u'gyro_north_seeking')
TrajStationType.hold_to_delta_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'hold to delta-MD', tag=u'hold_to_delta_MD')
TrajStationType.hold_to_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'hold to MD', tag=u'hold_to_MD')
TrajStationType.hold_to_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'hold to TVD', tag=u'hold_to_TVD')
TrajStationType.INCL_AZI_and_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'INCL, AZI and TVD', tag=u'INCL_AZI_and_TVD')
TrajStationType.magnetic_multi_shot = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'magnetic multi-shot', tag=u'magnetic_multi_shot')
TrajStationType.magnetic_MWD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'magnetic MWD', tag=u'magnetic_MWD')
TrajStationType.magnetic_single_shot = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'magnetic single shot', tag=u'magnetic_single_shot')
TrajStationType.marker_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'marker MD', tag=u'marker_MD')
TrajStationType.marker_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'marker TVD', tag=u'marker_TVD')
TrajStationType.NS_EW_and_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'NS, EW and TVD', tag=u'NS_EW_and_TVD')
TrajStationType.target_center = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'target center', tag=u'target_center')
TrajStationType.target_offset = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'target offset', tag=u'target_offset')
TrajStationType.tie_in_point = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'tie in point', tag=u'tie_in_point')
TrajStationType.turnrate_to_AZI = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'turnrate to AZI', tag=u'turnrate_to_AZI')
TrajStationType.turnrate_to_delta_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'turnrate to delta-MD', tag=u'turnrate_to_delta_MD')
TrajStationType.turnrate_to_MD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'turnrate to MD', tag=u'turnrate_to_MD')
TrajStationType.turnrate_to_TVD = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'turnrate to TVD', tag=u'turnrate_to_TVD')
TrajStationType.unknown = TrajStationType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TrajStationType._InitializeFacetMap(TrajStationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TrajStationType', TrajStationType)

# Atomic simple type: {http://www.witsml.org/schemas/131}TubularAssembly
class TubularAssembly (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TubularAssembly')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 6033, 1)
    _Documentation = None
TubularAssembly._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TubularAssembly, enum_prefix=None)
TubularAssembly.drilling = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'drilling', tag=u'drilling')
TubularAssembly.directional_drilling = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'directional drilling', tag=u'directional_drilling')
TubularAssembly.fishing = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'fishing', tag=u'fishing')
TubularAssembly.condition_mud = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'condition mud', tag=u'condition_mud')
TubularAssembly.tubing_conveyed_logging = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'tubing conveyed logging', tag=u'tubing_conveyed_logging')
TubularAssembly.cementing = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'cementing', tag=u'cementing')
TubularAssembly.casing = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'casing', tag=u'casing')
TubularAssembly.clean_out = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'clean out', tag=u'clean_out')
TubularAssembly.completion_or_testing = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'completion or testing', tag=u'completion_or_testing')
TubularAssembly.coring = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'coring', tag=u'coring')
TubularAssembly.hole_opening_or_underreaming = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'hole opening or underreaming', tag=u'hole_opening_or_underreaming')
TubularAssembly.milling_or_dressing_or_cutting = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'milling or dressing or cutting', tag=u'milling_or_dressing_or_cutting')
TubularAssembly.wiper_or_check_or_reaming = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'wiper or check or reaming', tag=u'wiper_or_check_or_reaming')
TubularAssembly.unknown = TubularAssembly._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TubularAssembly._InitializeFacetMap(TubularAssembly._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TubularAssembly', TubularAssembly)

# Atomic simple type: {http://www.witsml.org/schemas/131}TubularComponent
class TubularComponent (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TubularComponent')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 6110, 1)
    _Documentation = None
TubularComponent._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TubularComponent, enum_prefix=None)
TubularComponent.non_magnetic_stabilizer = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'non-magnetic stabilizer', tag=u'non_magnetic_stabilizer')
TubularComponent.non_magnetic_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'non-magnetic collar', tag=u'non_magnetic_collar')
TubularComponent.stabilizer = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stabilizer', tag=u'stabilizer')
TubularComponent.adjustable_kickoff = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'adjustable kickoff', tag=u'adjustable_kickoff')
TubularComponent.accelerator = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'accelerator', tag=u'accelerator')
TubularComponent.rotary_steering_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'rotary steering tool', tag=u'rotary_steering_tool')
TubularComponent.sub_bar_catcher = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-bar catcher', tag=u'sub_bar_catcher')
TubularComponent.sub_bent = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-bent', tag=u'sub_bent')
TubularComponent.bit_core_diamond = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bit core diamond', tag=u'bit_core_diamond')
TubularComponent.bit_core_PDC = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bit core PDC', tag=u'bit_core_PDC')
TubularComponent.bit_diamond_fixed_cut = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bit diamond fixed cut', tag=u'bit_diamond_fixed_cut')
TubularComponent.bit_insert_roller_cone = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bit insert roller cone', tag=u'bit_insert_roller_cone')
TubularComponent.bit_mill_tooth_roller_cone = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bit mill tooth roller cone', tag=u'bit_mill_tooth_roller_cone')
TubularComponent.bit_PDC_fixed_cutter = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bit PDC fixed cutter', tag=u'bit_PDC_fixed_cutter')
TubularComponent.sub_bit = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-bit', tag=u'sub_bit')
TubularComponent.bridge_plug = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bridge plug', tag=u'bridge_plug')
TubularComponent.bullnose = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bullnose', tag=u'bullnose')
TubularComponent.bull_plug = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bull plug', tag=u'bull_plug')
TubularComponent.sub_bumper = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-bumper', tag=u'sub_bumper')
TubularComponent.casing = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'casing', tag=u'casing')
TubularComponent.casing_cutter = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'casing cutter', tag=u'casing_cutter')
TubularComponent.hanger_casing_subsea = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'hanger casing subsea', tag=u'hanger_casing_subsea')
TubularComponent.hanger_casing_surface = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'hanger casing surface', tag=u'hanger_casing_surface')
TubularComponent.casing_head = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'casing head', tag=u'casing_head')
TubularComponent.catch_assembly = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'catch assembly', tag=u'catch_assembly')
TubularComponent.sub_catcher = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-catcher', tag=u'sub_catcher')
TubularComponent.sub_circulation = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-circulation', tag=u'sub_circulation')
TubularComponent.coiled_tubing_in_hole = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'coiled tubing in hole', tag=u'coiled_tubing_in_hole')
TubularComponent.coiled_tubing_on_coil = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'coiled tubing on coil', tag=u'coiled_tubing_on_coil')
TubularComponent.drill_pipe_compressive = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'drill pipe compressive', tag=u'drill_pipe_compressive')
TubularComponent.sub_cone = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-cone', tag=u'sub_cone')
TubularComponent.core_barrel = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'core barrel', tag=u'core_barrel')
TubularComponent.core_orientation_barrel = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'core orientation barrel', tag=u'core_orientation_barrel')
TubularComponent.sub_crossover = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-crossover', tag=u'sub_crossover')
TubularComponent.casing_crossover = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'casing crossover', tag=u'casing_crossover')
TubularComponent.sub_dart = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-dart', tag=u'sub_dart')
TubularComponent.die_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'die collar', tag=u'die_collar')
TubularComponent.die_collar_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'die collar LH', tag=u'die_collar_LH')
TubularComponent.directional_guidance_system = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'directional guidance system', tag=u'directional_guidance_system')
TubularComponent.drill_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'drill collar', tag=u'drill_collar')
TubularComponent.drill_pipe = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'drill pipe', tag=u'drill_pipe')
TubularComponent.drill_pipe_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'drill pipe LH', tag=u'drill_pipe_LH')
TubularComponent.drill_stem_test_BHA = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'drill stem test BHA', tag=u'drill_stem_test_BHA')
TubularComponent.drive_pipe = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'drive pipe', tag=u'drive_pipe')
TubularComponent.dual_catch_assembly = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'dual catch assembly', tag=u'dual_catch_assembly')
TubularComponent.extension_bowl_overshot = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'extension bowl overshot', tag=u'extension_bowl_overshot')
TubularComponent.extension_sub_overshot = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'extension sub-overshot', tag=u'extension_sub_overshot')
TubularComponent.float_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'float collar', tag=u'float_collar')
TubularComponent.float_shoe = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'float shoe', tag=u'float_shoe')
TubularComponent.sub_float = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-float', tag=u'sub_float')
TubularComponent.flow_head = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'flow head', tag=u'flow_head')
TubularComponent.guide_shoe = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'guide shoe', tag=u'guide_shoe')
TubularComponent.MWD_hang_off_sub = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'MWD hang off sub', tag=u'MWD_hang_off_sub')
TubularComponent.heavy_weight_drill_pipe = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'heavy weight drill pipe', tag=u'heavy_weight_drill_pipe')
TubularComponent.heavy_weight_drill_pipe_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'heavy weight drill pipe LH', tag=u'heavy_weight_drill_pipe_LH')
TubularComponent.riser_high_pressure = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'riser high pressure', tag=u'riser_high_pressure')
TubularComponent.bit_hole_opener = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bit hole opener', tag=u'bit_hole_opener')
TubularComponent.casing_inflatable_packer = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'casing inflatable packer', tag=u'casing_inflatable_packer')
TubularComponent.motor_instrumented = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'motor instrumented', tag=u'motor_instrumented')
TubularComponent.jar = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'jar', tag=u'jar')
TubularComponent.sub_jetting = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-jetting', tag=u'sub_jetting')
TubularComponent.junk_basket = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'junk basket', tag=u'junk_basket')
TubularComponent.junk_basket_reverse_circulation = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'junk basket reverse circulation', tag=u'junk_basket_reverse_circulation')
TubularComponent.sub_junk = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-junk', tag=u'sub_junk')
TubularComponent.kelly = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'kelly', tag=u'kelly')
TubularComponent.keyseat_wiper_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'keyseat wiper tool', tag=u'keyseat_wiper_tool')
TubularComponent.landing_float_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'landing float collar', tag=u'landing_float_collar')
TubularComponent.lead_impression_block = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'lead impression block', tag=u'lead_impression_block')
TubularComponent.liner = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'liner', tag=u'liner')
TubularComponent.hanger_liner = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'hanger liner', tag=u'hanger_liner')
TubularComponent.magnet = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'magnet', tag=u'magnet')
TubularComponent.riser_marine = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'riser marine', tag=u'riser_marine')
TubularComponent.mill_dress = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill dress', tag=u'mill_dress')
TubularComponent.mill_flat_bottom = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill flat bottom', tag=u'mill_flat_bottom')
TubularComponent.mill_hollow = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill hollow', tag=u'mill_hollow')
TubularComponent.mill_polish = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill polish', tag=u'mill_polish')
TubularComponent.mill_section = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill section', tag=u'mill_section')
TubularComponent.mill_taper = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill taper', tag=u'mill_taper')
TubularComponent.mill_washover = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill washover', tag=u'mill_washover')
TubularComponent.mill_packer_picker_assembly = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill packer picker assembly', tag=u'mill_packer_picker_assembly')
TubularComponent.millout_extension = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'millout extension', tag=u'millout_extension')
TubularComponent.multilateral_hanger_running_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'multilateral hanger running tool', tag=u'multilateral_hanger_running_tool')
TubularComponent.hanger_mud_line = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'hanger mud line', tag=u'hanger_mud_line')
TubularComponent.motor = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'motor', tag=u'motor')
TubularComponent.mule_shoe = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mule shoe', tag=u'mule_shoe')
TubularComponent.logging_while_drilling_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'logging while drilling tool', tag=u'logging_while_drilling_tool')
TubularComponent.stabilizer_near_bit_roller_reamer = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stabilizer near bit roller reamer', tag=u'stabilizer_near_bit_roller_reamer')
TubularComponent.stabilizer_near_bit = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stabilizer near bit', tag=u'stabilizer_near_bit')
TubularComponent.stabilizer_non_rotating = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stabilizer non-rotating', tag=u'stabilizer_non_rotating')
TubularComponent.sub_orienting = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-orienting', tag=u'sub_orienting')
TubularComponent.other = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
TubularComponent.overshot = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'overshot', tag=u'overshot')
TubularComponent.overshot_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'overshot LH', tag=u'overshot_LH')
TubularComponent.oversize_lip_guide_overshot = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'oversize lip guide overshot', tag=u'oversize_lip_guide_overshot')
TubularComponent.packer = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'packer', tag=u'packer')
TubularComponent.polished_bore_receptacle = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'polished bore receptacle', tag=u'polished_bore_receptacle')
TubularComponent.mill_pilot = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill pilot', tag=u'mill_pilot')
TubularComponent.pipe_cutter = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'pipe cutter', tag=u'pipe_cutter')
TubularComponent.ported_stinger = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'ported stinger', tag=u'ported_stinger')
TubularComponent.sub_ported = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-ported', tag=u'sub_ported')
TubularComponent.prepacked_screens = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'prepacked screens', tag=u'prepacked_screens')
TubularComponent.sub_pressure_relief = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-pressure relief', tag=u'sub_pressure_relief')
TubularComponent.riser_production = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'riser production', tag=u'riser_production')
TubularComponent.MWD_pulser = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'MWD pulser', tag=u'MWD_pulser')
TubularComponent.sub_pump_out = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-pump out', tag=u'sub_pump_out')
TubularComponent.sub_restrictor = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-restrictor', tag=u'sub_restrictor')
TubularComponent.packer_retrieve_TT_squeeze = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'packer retrieve TT squeeze', tag=u'packer_retrieve_TT_squeeze')
TubularComponent.reversing_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'reversing tool', tag=u'reversing_tool')
TubularComponent.stabilizer_string_roller_reamer = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stabilizer string roller reamer', tag=u'stabilizer_string_roller_reamer')
TubularComponent.packer_RTTS = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'packer RTTS', tag=u'packer_RTTS')
TubularComponent.running_tool = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'running tool', tag=u'running_tool')
TubularComponent.safety_joint = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'safety joint', tag=u'safety_joint')
TubularComponent.safety_joint_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'safety joint LH', tag=u'safety_joint_LH')
TubularComponent.sub_saver = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-saver', tag=u'sub_saver')
TubularComponent.scab_liner_bit_guide = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'scab liner bit guide', tag=u'scab_liner_bit_guide')
TubularComponent.scraper = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'scraper', tag=u'scraper')
TubularComponent.scratchers = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'scratchers', tag=u'scratchers')
TubularComponent.casing_shoe_screw_in = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'casing shoe screw-in', tag=u'casing_shoe_screw_in')
TubularComponent.sub_shock = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-shock', tag=u'sub_shock')
TubularComponent.drill_collar_short = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'drill collar short', tag=u'drill_collar_short')
TubularComponent.sub_side_entry = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-side entry', tag=u'sub_side_entry')
TubularComponent.slotted_liner = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'slotted liner', tag=u'slotted_liner')
TubularComponent.spear = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'spear', tag=u'spear')
TubularComponent.stage_cement_collar = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stage cement collar', tag=u'stage_cement_collar')
TubularComponent.motor_steerable = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'motor steerable', tag=u'motor_steerable')
TubularComponent.packer_storm_valve_RTTS = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'packer storm valve RTTS', tag=u'packer_storm_valve_RTTS')
TubularComponent.stabilizer_string = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stabilizer string', tag=u'stabilizer_string')
TubularComponent.surface_pipe = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'surface pipe', tag=u'surface_pipe')
TubularComponent.taper_tap = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'taper tap', tag=u'taper_tap')
TubularComponent.taper_tap_LH = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'taper tap LH', tag=u'taper_tap_LH')
TubularComponent.tubing_conveyed_perforating_gun = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'tubing-conveyed perforating gun', tag=u'tubing_conveyed_perforating_gun')
TubularComponent.thruster = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'thruster', tag=u'thruster')
TubularComponent.tieback_polished_bore_receptacle = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'tieback polished bore receptacle', tag=u'tieback_polished_bore_receptacle')
TubularComponent.tieback_stinger = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'tieback stinger', tag=u'tieback_stinger')
TubularComponent.tubing = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'tubing', tag=u'tubing')
TubularComponent.hanger_tubing = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'hanger tubing', tag=u'hanger_tubing')
TubularComponent.turbine = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'turbine', tag=u'turbine')
TubularComponent.bit_under_reamer = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'bit under reamer', tag=u'bit_under_reamer')
TubularComponent.stabilizer_variable_blade = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stabilizer variable blade', tag=u'stabilizer_variable_blade')
TubularComponent.washover_pipe = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'washover pipe', tag=u'washover_pipe')
TubularComponent.mill_watermelon = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill watermelon', tag=u'mill_watermelon')
TubularComponent.whipstock = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'whipstock', tag=u'whipstock')
TubularComponent.whipstock_anchor = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'whipstock anchor', tag=u'whipstock_anchor')
TubularComponent.stabilizer_turbo_back = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stabilizer turbo back', tag=u'stabilizer_turbo_back')
TubularComponent.stabilizer_inline = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stabilizer inline', tag=u'stabilizer_inline')
TubularComponent.stabilizer_steerable = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'stabilizer steerable', tag=u'stabilizer_steerable')
TubularComponent.sub_stop = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-stop', tag=u'sub_stop')
TubularComponent.sub_filter = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'sub-filter', tag=u'sub_filter')
TubularComponent.mill_casing_cutting = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'mill casing cutting', tag=u'mill_casing_cutting')
TubularComponent.reamer = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'reamer', tag=u'reamer')
TubularComponent.unknown = TubularComponent._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TubularComponent._InitializeFacetMap(TubularComponent._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TubularComponent', TubularComponent)

# Atomic simple type: {http://www.witsml.org/schemas/131}TypeSurveyTool
class TypeSurveyTool (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of direcional survey tool; very generic classification"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TypeSurveyTool')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 6937, 1)
    _Documentation = u'Type of direcional survey tool; very generic classification'
TypeSurveyTool._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TypeSurveyTool, enum_prefix=None)
TypeSurveyTool.magnetic_MWD = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value=u'magnetic MWD', tag=u'magnetic_MWD')
TypeSurveyTool.gyroscopic__MWD = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value=u'gyroscopic  MWD', tag=u'gyroscopic__MWD')
TypeSurveyTool.gyroscopic_north_seeking = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value=u'gyroscopic north seeking', tag=u'gyroscopic_north_seeking')
TypeSurveyTool.gyroscopic_inertial = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value=u'gyroscopic inertial', tag=u'gyroscopic_inertial')
TypeSurveyTool.magnetic_single_shot = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value=u'magnetic single-shot', tag=u'magnetic_single_shot')
TypeSurveyTool.magnetic_multiple_shot = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value=u'magnetic multiple-shot', tag=u'magnetic_multiple_shot')
TypeSurveyTool.unknown = TypeSurveyTool._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TypeSurveyTool._InitializeFacetMap(TypeSurveyTool._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TypeSurveyTool', TypeSurveyTool)

# Atomic simple type: {http://www.witsml.org/schemas/131}WellDirection
class WellDirection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The direction of flow of the fluids in a well facility
			(generally, injected or produced, or some combination)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellDirection')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 6982, 1)
    _Documentation = u'The direction of flow of the fluids in a well facility\n\t\t\t(generally, injected or produced, or some combination).'
WellDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellDirection, enum_prefix=None)
WellDirection.huff_n_puff = WellDirection._CF_enumeration.addEnumeration(unicode_value=u'huff-n-puff', tag=u'huff_n_puff')
WellDirection.injector = WellDirection._CF_enumeration.addEnumeration(unicode_value=u'injector', tag=u'injector')
WellDirection.producer = WellDirection._CF_enumeration.addEnumeration(unicode_value=u'producer', tag=u'producer')
WellDirection.uncertain = WellDirection._CF_enumeration.addEnumeration(unicode_value=u'uncertain', tag=u'uncertain')
WellDirection.unknown = WellDirection._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellDirection._InitializeFacetMap(WellDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellDirection', WellDirection)

# Atomic simple type: {http://www.witsml.org/schemas/131}WellFluid
class WellFluid (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The type of fluid being produced from or injected 
			into a well facility."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellFluid')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 7023, 1)
    _Documentation = u'The type of fluid being produced from or injected \n\t\t\tinto a well facility.'
WellFluid._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellFluid, enum_prefix=None)
WellFluid.air = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'air', tag=u'air')
WellFluid.condensate = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'condensate', tag=u'condensate')
WellFluid.dry = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'dry', tag=u'dry')
WellFluid.gas = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'gas', tag=u'gas')
WellFluid.gas_water = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'gas-water', tag=u'gas_water')
WellFluid.non_HC_gas = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'non HC gas', tag=u'non_HC_gas')
WellFluid.non_HC_gas____CO2 = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'non HC gas -- CO2', tag=u'non_HC_gas____CO2')
WellFluid.oil = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'oil', tag=u'oil')
WellFluid.oil_gas = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'oil-gas', tag=u'oil_gas')
WellFluid.oil_water = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'oil-water', tag=u'oil_water')
WellFluid.steam = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'steam', tag=u'steam')
WellFluid.water = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'water', tag=u'water')
WellFluid.water____brine = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'water -- brine', tag=u'water____brine')
WellFluid.water____fresh_water = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'water -- fresh water', tag=u'water____fresh_water')
WellFluid.unknown = WellFluid._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellFluid._InitializeFacetMap(WellFluid._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellFluid', WellFluid)

# Atomic simple type: {http://www.witsml.org/schemas/131}WellboreShape
class WellboreShape (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the classification of a wellbore 
			based on its shape. The source of the values and the descriptions is the 
			POSC V2.2 "facility class" standard instance values in classification system 
			"POSC wellbore trajectory shape". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellboreShape')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 7140, 1)
    _Documentation = u'These values represent the classification of a wellbore \n\t\t\tbased on its shape. The source of the values and the descriptions is the \n\t\t\tPOSC V2.2 "facility class" standard instance values in classification system \n\t\t\t"POSC wellbore trajectory shape". '
WellboreShape._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellboreShape, enum_prefix=None)
WellboreShape.build_and_hold = WellboreShape._CF_enumeration.addEnumeration(unicode_value=u'build and hold', tag=u'build_and_hold')
WellboreShape.deviated = WellboreShape._CF_enumeration.addEnumeration(unicode_value=u'deviated', tag=u'deviated')
WellboreShape.double_kickoff = WellboreShape._CF_enumeration.addEnumeration(unicode_value=u'double kickoff', tag=u'double_kickoff')
WellboreShape.horizontal = WellboreShape._CF_enumeration.addEnumeration(unicode_value=u'horizontal', tag=u'horizontal')
WellboreShape.S_shaped = WellboreShape._CF_enumeration.addEnumeration(unicode_value=u'S-shaped', tag=u'S_shaped')
WellboreShape.vertical = WellboreShape._CF_enumeration.addEnumeration(unicode_value=u'vertical', tag=u'vertical')
WellboreShape.unknown = WellboreShape._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellboreShape._InitializeFacetMap(WellboreShape._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellboreShape', WellboreShape)

# Atomic simple type: {http://www.witsml.org/schemas/131}WellboreType
class WellboreType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The classification of a wellbore with respect to its parent 
			well/wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellboreType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 7196, 1)
    _Documentation = u'The classification of a wellbore with respect to its parent \n\t\t\twell/wellbore.'
WellboreType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellboreType, enum_prefix=None)
WellboreType.bypass = WellboreType._CF_enumeration.addEnumeration(unicode_value=u'bypass', tag=u'bypass')
WellboreType.initial = WellboreType._CF_enumeration.addEnumeration(unicode_value=u'initial', tag=u'initial')
WellboreType.redrill = WellboreType._CF_enumeration.addEnumeration(unicode_value=u'redrill', tag=u'redrill')
WellboreType.reentry = WellboreType._CF_enumeration.addEnumeration(unicode_value=u'reentry', tag=u'reentry')
WellboreType.respud = WellboreType._CF_enumeration.addEnumeration(unicode_value=u'respud', tag=u'respud')
WellboreType.sidetrack = WellboreType._CF_enumeration.addEnumeration(unicode_value=u'sidetrack', tag=u'sidetrack')
WellboreType.unknown = WellboreType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellboreType._InitializeFacetMap(WellboreType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellboreType', WellboreType)

# Atomic simple type: {http://www.witsml.org/schemas/131}WellPurpose
class WellPurpose (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the classification of a well or 
			wellbore by the purpose for which it was initially drilled."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellPurpose')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 7252, 1)
    _Documentation = u'These values represent the classification of a well or \n\t\t\twellbore by the purpose for which it was initially drilled.'
WellPurpose._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellPurpose, enum_prefix=None)
WellPurpose.appraisal = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'appraisal', tag=u'appraisal')
WellPurpose.appraisal____confirmation_appraisal = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'appraisal -- confirmation appraisal', tag=u'appraisal____confirmation_appraisal')
WellPurpose.appraisal____exploratory_appraisal = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'appraisal -- exploratory appraisal', tag=u'appraisal____exploratory_appraisal')
WellPurpose.exploration = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'exploration', tag=u'exploration')
WellPurpose.exploration____deeper_pool_wildcat = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'exploration -- deeper-pool wildcat', tag=u'exploration____deeper_pool_wildcat')
WellPurpose.exploration____new_field_wildcat = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'exploration -- new-field wildcat', tag=u'exploration____new_field_wildcat')
WellPurpose.exploration____new_pool_wildcat = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'exploration -- new-pool wildcat', tag=u'exploration____new_pool_wildcat')
WellPurpose.exploration____outpost_wildcat = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'exploration -- outpost wildcat', tag=u'exploration____outpost_wildcat')
WellPurpose.exploration____shallower_pool_wildcat = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'exploration -- shallower-pool wildcat', tag=u'exploration____shallower_pool_wildcat')
WellPurpose.development = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'development', tag=u'development')
WellPurpose.development____infill_development = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'development -- infill development', tag=u'development____infill_development')
WellPurpose.development____injector = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'development -- injector', tag=u'development____injector')
WellPurpose.development____producer = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'development -- producer', tag=u'development____producer')
WellPurpose.fluid_storage = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'fluid storage', tag=u'fluid_storage')
WellPurpose.fluid_storage____gas_storage = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'fluid storage -- gas storage', tag=u'fluid_storage____gas_storage')
WellPurpose.general_srvc = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'general srvc', tag=u'general_srvc')
WellPurpose.general_srvc____borehole_re_acquisition = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'general srvc -- borehole re-acquisition', tag=u'general_srvc____borehole_re_acquisition')
WellPurpose.general_srvc____observation = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'general srvc -- observation', tag=u'general_srvc____observation')
WellPurpose.general_srvc____relief = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'general srvc -- relief', tag=u'general_srvc____relief')
WellPurpose.general_srvc____research = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'general srvc -- research', tag=u'general_srvc____research')
WellPurpose.general_srvc____research____drill_test = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'general srvc -- research -- drill test', tag=u'general_srvc____research____drill_test')
WellPurpose.general_srvc____research____strat_test = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'general srvc -- research -- strat test', tag=u'general_srvc____research____strat_test')
WellPurpose.general_srvc____waste_disposal = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'general srvc -- waste disposal', tag=u'general_srvc____waste_disposal')
WellPurpose.mineral = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'mineral', tag=u'mineral')
WellPurpose.unknown = WellPurpose._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellPurpose._InitializeFacetMap(WellPurpose._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellPurpose', WellPurpose)

# Atomic simple type: {http://www.witsml.org/schemas/131}WellStatus
class WellStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the status of a well or wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_catalog.xsd', 7388, 1)
    _Documentation = u'These values represent the status of a well or wellbore.'
WellStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellStatus, enum_prefix=None)
WellStatus.abandoned = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'abandoned', tag=u'abandoned')
WellStatus.active = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'active', tag=u'active')
WellStatus.active____injecting = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'active -- injecting', tag=u'active____injecting')
WellStatus.active____producing = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'active -- producing', tag=u'active____producing')
WellStatus.completed = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'completed', tag=u'completed')
WellStatus.drilling = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'drilling', tag=u'drilling')
WellStatus.partially_plugged = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'partially plugged', tag=u'partially_plugged')
WellStatus.permitted = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'permitted', tag=u'permitted')
WellStatus.plugged_and_abandoned = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'plugged and abandoned', tag=u'plugged_and_abandoned')
WellStatus.proposed = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'proposed', tag=u'proposed')
WellStatus.sold = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'sold', tag=u'sold')
WellStatus.suspended = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'suspended', tag=u'suspended')
WellStatus.temporarily_abandoned = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'temporarily abandoned', tag=u'temporarily_abandoned')
WellStatus.testing = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'testing', tag=u'testing')
WellStatus.tight = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'tight', tag=u'tight')
WellStatus.working_over = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'working over', tag=u'working_over')
WellStatus.unknown = WellStatus._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellStatus._InitializeFacetMap(WellStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellStatus', WellStatus)

# Atomic simple type: {http://www.witsml.org/schemas/131}PercentUom
class PercentUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PercentUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 139, 1)
    _Documentation = None
PercentUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PercentUom, enum_prefix=None)
PercentUom.emptyString = PercentUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
PercentUom._InitializeFacetMap(PercentUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PercentUom', PercentUom)

# List simple type: {http://www.witsml.org/schemas/131}listOfString
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfString (pyxb.binding.basis.STD_list):

    """A representation of a list of xsd:string values,
			restricted to strings without embedded whitespace."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 216, 1)
    _Documentation = u'A representation of a list of xsd:string values,\n\t\t\trestricted to strings without embedded whitespace.'

    _ItemType = str32
listOfString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfString', listOfString)

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

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'refWellDatum')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 295, 1)
    _Documentation = u"A reference to a wellDatum in the current well. \n\t\t\tThis value must match the uid value in a WellDatum. \n\t\t\tThis value represents a foreign key from one element to another.\n\t\t\tThis is an exception to the convention that a foreign key must utilize both \n\t\t\ta human contextual name and a uid value. For messages outside the context of\n\t\t\ta server then this value will commonly match the value of the name of the \n\t\t\twellDatum (e.g., 'KB') if uids are not not used in that context.\n\t\t\tThis was a compromise in order to allow the coordinate structures to be simple\n\t\t\tand still be usable both within the context of a server and outside the context of a server."
refWellDatum._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'refWellDatum', refWellDatum)

# Atomic simple type: {http://www.witsml.org/schemas/131}nameString
class nameString (abstractNameString):

    """A user assigned human recognizable contextual name of something. 
			There should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.
			This type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 312, 1)
    _Documentation = u'A user assigned human recognizable contextual name of something. \n\t\t\tThere should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.\n\t\t\tThis type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration.'
nameString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'nameString', nameString)

# Atomic simple type: {http://www.witsml.org/schemas/131}kindString
class kindString (abstractTypeEnum):

    """A community assigned human recognizable name. 
			This type of value is intended to be unique and is generally a candidate to be constrained to an enumerated list."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'kindString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 375, 1)
    _Documentation = u'A community assigned human recognizable name. \n\t\t\tThis type of value is intended to be unique and is generally a candidate to be constrained to an enumerated list.'
kindString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'kindString', kindString)

# Atomic simple type: {http://www.witsml.org/schemas/131}uomString
class uomString (abstractUomEnum):

    """A unit of measure acronym from the POSC unit of measure file."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'uomString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 384, 1)
    _Documentation = u'A unit of measure acronym from the POSC unit of measure file.'
uomString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'uomString', uomString)

# Atomic simple type: {http://www.witsml.org/schemas/131}uidString
class uidString (abstractUidString):

    """A locally unique identifier. 
			The value is not intended to convey any semantic content (e.g., it may be computer generated). 
			The value is only required to be unique within a context in a document (e.g., defined via key and keyref). 
			There is no guarantee that the same data in multiple documents will utilize the same uid value 
			unless enforced by the source of the document (e.g., a document server)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'uidString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 391, 1)
    _Documentation = u'A locally unique identifier. \n\t\t\tThe value is not intended to convey any semantic content (e.g., it may be computer generated). \n\t\t\tThe value is only required to be unique within a context in a document (e.g., defined via key and keyref). \n\t\t\tThere is no guarantee that the same data in multiple documents will utilize the same uid value \n\t\t\tunless enforced by the source of the document (e.g., a document server).'
uidString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'uidString', uidString)

# Atomic simple type: {http://www.witsml.org/schemas/131}refString
class refString (abstractUidString):

    """A reference to the unique identifier of another element. 
			This value represents a foreign key from one element to another.
			The value should match the value of an attribute of type uidString."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'refString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 402, 1)
    _Documentation = u'A reference to the unique identifier of another element. \n\t\t\tThis value represents a foreign key from one element to another.\n\t\t\tThe value should match the value of an attribute of type uidString.'
refString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'refString', refString)

# Atomic simple type: {http://www.witsml.org/schemas/131}MeasuredDepthUom
class MeasuredDepthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """The units of measure that are valid for measured depths in a wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MeasuredDepthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 518, 1)
    _Documentation = u'The units of measure that are valid for measured depths in a wellbore.'
MeasuredDepthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MeasuredDepthUom, enum_prefix=None)
MeasuredDepthUom.m = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value=u'm', tag=u'm')
MeasuredDepthUom.ft = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value=u'ft', tag=u'ft')
MeasuredDepthUom.ftUS = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value=u'ftUS', tag=u'ftUS')
MeasuredDepthUom._InitializeFacetMap(MeasuredDepthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MeasuredDepthUom', MeasuredDepthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}WellVerticalCoordinateUom
class WellVerticalCoordinateUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """The units of measure that are valid for vertical gravity based 
			coordinates (i.e., elevation or vertical depth) within the context of a well."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellVerticalCoordinateUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 593, 1)
    _Documentation = u'The units of measure that are valid for vertical gravity based \n\t\t\tcoordinates (i.e., elevation or vertical depth) within the context of a well.'
WellVerticalCoordinateUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellVerticalCoordinateUom, enum_prefix=None)
WellVerticalCoordinateUom.m = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value=u'm', tag=u'm')
WellVerticalCoordinateUom.ft = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value=u'ft', tag=u'ft')
WellVerticalCoordinateUom.ftUS = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value=u'ftUS', tag=u'ftUS')
WellVerticalCoordinateUom.ftBr65 = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value=u'ftBr(65)', tag=u'ftBr65')
WellVerticalCoordinateUom._InitializeFacetMap(WellVerticalCoordinateUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellVerticalCoordinateUom', WellVerticalCoordinateUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}positiveCount
class positiveCount (abstractPositiveCount):

    """A positive integer (one based count or index)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positiveCount')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 638, 1)
    _Documentation = u'A positive integer (one based count or index).'
positiveCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveCount, value=pyxb.binding.datatypes.short(1))
positiveCount._InitializeFacetMap(positiveCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'positiveCount', positiveCount)

# Atomic simple type: {http://www.witsml.org/schemas/131}accelerationLinearUom
class accelerationLinearUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accelerationLinearUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 25, 1)
    _Documentation = None
accelerationLinearUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=accelerationLinearUom, enum_prefix=None)
accelerationLinearUom.ms2 = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'm/s2', tag=u'ms2')
accelerationLinearUom.cms2 = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'cm/s2', tag=u'cms2')
accelerationLinearUom.fts2 = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'ft/s2', tag=u'fts2')
accelerationLinearUom.Gal = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'Gal', tag=u'Gal')
accelerationLinearUom.mgn = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'mgn', tag=u'mgn')
accelerationLinearUom.gn = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'gn', tag=u'gn')
accelerationLinearUom.mGal = accelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'mGal', tag=u'mGal')
accelerationLinearUom._InitializeFacetMap(accelerationLinearUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'accelerationLinearUom', accelerationLinearUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}anglePerLengthUom
class anglePerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'anglePerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 37, 1)
    _Documentation = None
anglePerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=anglePerLengthUom, enum_prefix=None)
anglePerLengthUom.radm = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'rad/m', tag=u'radm')
anglePerLengthUom.dega30ft = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dega/30ft', tag=u'dega30ft')
anglePerLengthUom.degaft = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dega/ft', tag=u'degaft')
anglePerLengthUom.dega100ft = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dega/100ft', tag=u'dega100ft')
anglePerLengthUom.degam = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dega/m', tag=u'degam')
anglePerLengthUom.dega30m = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dega/30m', tag=u'dega30m')
anglePerLengthUom.radft = anglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'rad/ft', tag=u'radft')
anglePerLengthUom._InitializeFacetMap(anglePerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'anglePerLengthUom', anglePerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}anglePerTimeUom
class anglePerTimeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'anglePerTimeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 49, 1)
    _Documentation = None
anglePerTimeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=anglePerTimeUom, enum_prefix=None)
anglePerTimeUom.rads = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'rad/s', tag=u'rads')
anglePerTimeUom.cs = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'c/s', tag=u'cs')
anglePerTimeUom.degah = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'dega/h', tag=u'degah')
anglePerTimeUom.degamin = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'dega/min', tag=u'degamin')
anglePerTimeUom.degas = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'dega/s', tag=u'degas')
anglePerTimeUom.revs = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'rev/s', tag=u'revs')
anglePerTimeUom.rpm = anglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'rpm', tag=u'rpm')
anglePerTimeUom._InitializeFacetMap(anglePerTimeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'anglePerTimeUom', anglePerTimeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}areaUom
class areaUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'areaUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 61, 1)
    _Documentation = None
areaUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=areaUom, enum_prefix=None)
areaUom.m2 = areaUom._CF_enumeration.addEnumeration(unicode_value=u'm2', tag=u'm2')
areaUom.acre = areaUom._CF_enumeration.addEnumeration(unicode_value=u'acre', tag=u'acre')
areaUom.b = areaUom._CF_enumeration.addEnumeration(unicode_value=u'b', tag=u'b')
areaUom.cm2 = areaUom._CF_enumeration.addEnumeration(unicode_value=u'cm2', tag=u'cm2')
areaUom.ft2 = areaUom._CF_enumeration.addEnumeration(unicode_value=u'ft2', tag=u'ft2')
areaUom.ha = areaUom._CF_enumeration.addEnumeration(unicode_value=u'ha', tag=u'ha')
areaUom.in2 = areaUom._CF_enumeration.addEnumeration(unicode_value=u'in2', tag=u'in2')
areaUom.km2 = areaUom._CF_enumeration.addEnumeration(unicode_value=u'km2', tag=u'km2')
areaUom.mi2 = areaUom._CF_enumeration.addEnumeration(unicode_value=u'mi2', tag=u'mi2')
areaUom.miUS2 = areaUom._CF_enumeration.addEnumeration(unicode_value=u'miUS2', tag=u'miUS2')
areaUom.mm2 = areaUom._CF_enumeration.addEnumeration(unicode_value=u'mm2', tag=u'mm2')
areaUom.um2 = areaUom._CF_enumeration.addEnumeration(unicode_value=u'um2', tag=u'um2')
areaUom.yd2 = areaUom._CF_enumeration.addEnumeration(unicode_value=u'yd2', tag=u'yd2')
areaUom._InitializeFacetMap(areaUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'areaUom', areaUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}areaPerAreaUom
class areaPerAreaUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'areaPerAreaUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 79, 1)
    _Documentation = None
areaPerAreaUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=areaPerAreaUom, enum_prefix=None)
areaPerAreaUom.Euc = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'Euc', tag=u'Euc')
areaPerAreaUom.emptyString = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
areaPerAreaUom.in2ft2 = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'in2/ft2', tag=u'in2ft2')
areaPerAreaUom.in2in2 = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'in2/in2', tag=u'in2in2')
areaPerAreaUom.m2m2 = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'm2/m2', tag=u'm2m2')
areaPerAreaUom.mm2mm2 = areaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'mm2/mm2', tag=u'mm2mm2')
areaPerAreaUom._InitializeFacetMap(areaPerAreaUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'areaPerAreaUom', areaPerAreaUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}densityUom
class densityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'densityUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 90, 1)
    _Documentation = None
densityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=densityUom, enum_prefix=None)
densityUom.kgm3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'kg/m3', tag=u'kgm3')
densityUom.n10Mgm3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'10Mg/m3', tag=u'n10Mgm3')
densityUom.dAPI = densityUom._CF_enumeration.addEnumeration(unicode_value=u'dAPI', tag=u'dAPI')
densityUom.gcm3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'g/cm3', tag=u'gcm3')
densityUom.gdm3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'g/dm3', tag=u'gdm3')
densityUom.ggalUK = densityUom._CF_enumeration.addEnumeration(unicode_value=u'g/galUK', tag=u'ggalUK')
densityUom.ggalUS = densityUom._CF_enumeration.addEnumeration(unicode_value=u'g/galUS', tag=u'ggalUS')
densityUom.gL = densityUom._CF_enumeration.addEnumeration(unicode_value=u'g/L', tag=u'gL')
densityUom.gm3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'g/m3', tag=u'gm3')
densityUom.grainft3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'grain/ft3', tag=u'grainft3')
densityUom.graingalUS = densityUom._CF_enumeration.addEnumeration(unicode_value=u'grain/galUS', tag=u'graingalUS')
densityUom.grain100ft3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'grain/100ft3', tag=u'grain100ft3')
densityUom.kgdm3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'kg/dm3', tag=u'kgdm3')
densityUom.kgL = densityUom._CF_enumeration.addEnumeration(unicode_value=u'kg/L', tag=u'kgL')
densityUom.Mgm3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'Mg/m3', tag=u'Mgm3')
densityUom.lbm10bbl = densityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/10bbl', tag=u'lbm10bbl')
densityUom.lbmbbl = densityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/bbl', tag=u'lbmbbl')
densityUom.lbmft3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/ft3', tag=u'lbmft3')
densityUom.lbmgalUK = densityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/galUK', tag=u'lbmgalUK')
densityUom.lbm1000galUK = densityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/1000galUK', tag=u'lbm1000galUK')
densityUom.lbmgalUS = densityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/galUS', tag=u'lbmgalUS')
densityUom.lbm1000galUS = densityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/1000galUS', tag=u'lbm1000galUS')
densityUom.lbmin3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/in3', tag=u'lbmin3')
densityUom.lbmMbbl = densityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/Mbbl', tag=u'lbmMbbl')
densityUom.mgdm3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'mg/dm3', tag=u'mgdm3')
densityUom.mggalUS = densityUom._CF_enumeration.addEnumeration(unicode_value=u'mg/galUS', tag=u'mggalUS')
densityUom.mgL = densityUom._CF_enumeration.addEnumeration(unicode_value=u'mg/L', tag=u'mgL')
densityUom.mgm3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'mg/m3', tag=u'mgm3')
densityUom.ugcm3 = densityUom._CF_enumeration.addEnumeration(unicode_value=u'ug/cm3', tag=u'ugcm3')
densityUom._InitializeFacetMap(densityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'densityUom', densityUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}dimensionlessUom
class dimensionlessUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dimensionlessUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 124, 1)
    _Documentation = None
dimensionlessUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dimensionlessUom, enum_prefix=None)
dimensionlessUom.Euc = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'Euc', tag=u'Euc')
dimensionlessUom.emptyString = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
dimensionlessUom.cEuc = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'cEuc', tag=u'cEuc')
dimensionlessUom.mEuc = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'mEuc', tag=u'mEuc')
dimensionlessUom.nEuc = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'nEuc', tag=u'nEuc')
dimensionlessUom.uEuc = dimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'uEuc', tag=u'uEuc')
dimensionlessUom._InitializeFacetMap(dimensionlessUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dimensionlessUom', dimensionlessUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}dynamicViscosityUom
class dynamicViscosityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dynamicViscosityUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 135, 1)
    _Documentation = None
dynamicViscosityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dynamicViscosityUom, enum_prefix=None)
dynamicViscosityUom.Pa_s = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'Pa.s', tag=u'Pa_s')
dynamicViscosityUom.cP = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'cP', tag=u'cP')
dynamicViscosityUom.P = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'P', tag=u'P')
dynamicViscosityUom.psi_s = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'psi.s', tag=u'psi_s')
dynamicViscosityUom.dyne_scm2 = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'dyne.s/cm2', tag=u'dyne_scm2')
dynamicViscosityUom.kgf_sm2 = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'kgf.s/m2', tag=u'kgf_sm2')
dynamicViscosityUom.lbf_sft2 = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'lbf.s/ft2', tag=u'lbf_sft2')
dynamicViscosityUom.lbf_sin2 = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'lbf.s/in2', tag=u'lbf_sin2')
dynamicViscosityUom.mPa_s = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'mPa.s', tag=u'mPa_s')
dynamicViscosityUom.N_sm2 = dynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'N.s/m2', tag=u'N_sm2')
dynamicViscosityUom._InitializeFacetMap(dynamicViscosityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dynamicViscosityUom', dynamicViscosityUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}electricCurrentUom
class electricCurrentUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'electricCurrentUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 150, 1)
    _Documentation = None
electricCurrentUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=electricCurrentUom, enum_prefix=None)
electricCurrentUom.A = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'A', tag=u'A')
electricCurrentUom.MA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'MA', tag=u'MA')
electricCurrentUom.kA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'kA', tag=u'kA')
electricCurrentUom.mA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'mA', tag=u'mA')
electricCurrentUom.nA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'nA', tag=u'nA')
electricCurrentUom.pA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'pA', tag=u'pA')
electricCurrentUom.uA = electricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'uA', tag=u'uA')
electricCurrentUom._InitializeFacetMap(electricCurrentUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'electricCurrentUom', electricCurrentUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}electricPotentialUom
class electricPotentialUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'electricPotentialUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 162, 1)
    _Documentation = None
electricPotentialUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=electricPotentialUom, enum_prefix=None)
electricPotentialUom.V = electricPotentialUom._CF_enumeration.addEnumeration(unicode_value=u'V', tag=u'V')
electricPotentialUom.kV = electricPotentialUom._CF_enumeration.addEnumeration(unicode_value=u'kV', tag=u'kV')
electricPotentialUom.mV = electricPotentialUom._CF_enumeration.addEnumeration(unicode_value=u'mV', tag=u'mV')
electricPotentialUom.MV = electricPotentialUom._CF_enumeration.addEnumeration(unicode_value=u'MV', tag=u'MV')
electricPotentialUom.uV = electricPotentialUom._CF_enumeration.addEnumeration(unicode_value=u'uV', tag=u'uV')
electricPotentialUom._InitializeFacetMap(electricPotentialUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'electricPotentialUom', electricPotentialUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}energyPerAreaUom
class energyPerAreaUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'energyPerAreaUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 172, 1)
    _Documentation = None
energyPerAreaUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=energyPerAreaUom, enum_prefix=None)
energyPerAreaUom.Nm = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'N/m', tag=u'Nm')
energyPerAreaUom.ergcm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'erg/cm2', tag=u'ergcm2')
energyPerAreaUom.Jcm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'J/cm2', tag=u'Jcm2')
energyPerAreaUom.Jm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'J/m2', tag=u'Jm2')
energyPerAreaUom.kgf_mcm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'kgf.m/cm2', tag=u'kgf_mcm2')
energyPerAreaUom.lbf_ftin2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'lbf.ft/in2', tag=u'lbf_ftin2')
energyPerAreaUom.mJcm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'mJ/cm2', tag=u'mJcm2')
energyPerAreaUom.mJm2 = energyPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'mJ/m2', tag=u'mJm2')
energyPerAreaUom._InitializeFacetMap(energyPerAreaUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'energyPerAreaUom', energyPerAreaUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}equivalentPerMassUom
class equivalentPerMassUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'equivalentPerMassUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 185, 1)
    _Documentation = None
equivalentPerMassUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=equivalentPerMassUom, enum_prefix=None)
equivalentPerMassUom.eqkg = equivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value=u'eq/kg', tag=u'eqkg')
equivalentPerMassUom.meqg = equivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value=u'meq/g', tag=u'meqg')
equivalentPerMassUom.meq100g = equivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value=u'meq/100g', tag=u'meq100g')
equivalentPerMassUom._InitializeFacetMap(equivalentPerMassUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'equivalentPerMassUom', equivalentPerMassUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}forceUom
class forceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'forceUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 193, 1)
    _Documentation = None
forceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=forceUom, enum_prefix=None)
forceUom.N = forceUom._CF_enumeration.addEnumeration(unicode_value=u'N', tag=u'N')
forceUom.daN = forceUom._CF_enumeration.addEnumeration(unicode_value=u'daN', tag=u'daN')
forceUom.dyne = forceUom._CF_enumeration.addEnumeration(unicode_value=u'dyne', tag=u'dyne')
forceUom.gf = forceUom._CF_enumeration.addEnumeration(unicode_value=u'gf', tag=u'gf')
forceUom.kdyne = forceUom._CF_enumeration.addEnumeration(unicode_value=u'kdyne', tag=u'kdyne')
forceUom.kgf = forceUom._CF_enumeration.addEnumeration(unicode_value=u'kgf', tag=u'kgf')
forceUom.klbf = forceUom._CF_enumeration.addEnumeration(unicode_value=u'klbf', tag=u'klbf')
forceUom.kN = forceUom._CF_enumeration.addEnumeration(unicode_value=u'kN', tag=u'kN')
forceUom.lbf = forceUom._CF_enumeration.addEnumeration(unicode_value=u'lbf', tag=u'lbf')
forceUom.Mgf = forceUom._CF_enumeration.addEnumeration(unicode_value=u'Mgf', tag=u'Mgf')
forceUom.mN = forceUom._CF_enumeration.addEnumeration(unicode_value=u'mN', tag=u'mN')
forceUom.MN = forceUom._CF_enumeration.addEnumeration(unicode_value=u'MN', tag=u'MN')
forceUom.ozf = forceUom._CF_enumeration.addEnumeration(unicode_value=u'ozf', tag=u'ozf')
forceUom.pdl = forceUom._CF_enumeration.addEnumeration(unicode_value=u'pdl', tag=u'pdl')
forceUom.tonfUK = forceUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUK', tag=u'tonfUK')
forceUom.tonfUS = forceUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS', tag=u'tonfUS')
forceUom.uN = forceUom._CF_enumeration.addEnumeration(unicode_value=u'uN', tag=u'uN')
forceUom._InitializeFacetMap(forceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'forceUom', forceUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}forcePerLengthUom
class forcePerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'forcePerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 215, 1)
    _Documentation = None
forcePerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=forcePerLengthUom, enum_prefix=None)
forcePerLengthUom.N30m = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'N/30m', tag=u'N30m')
forcePerLengthUom.Nm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'N/m', tag=u'Nm')
forcePerLengthUom.dynecm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dyne/cm', tag=u'dynecm')
forcePerLengthUom.kNm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'kN/m', tag=u'kNm')
forcePerLengthUom.kgfcm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'kgf/cm', tag=u'kgfcm')
forcePerLengthUom.lbf100ft = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/100ft', tag=u'lbf100ft')
forcePerLengthUom.lbf30m = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/30m', tag=u'lbf30m')
forcePerLengthUom.lbfft = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/ft', tag=u'lbfft')
forcePerLengthUom.lbfin = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/in', tag=u'lbfin')
forcePerLengthUom.mNkm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'mN/km', tag=u'mNkm')
forcePerLengthUom.mNm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'mN/m', tag=u'mNm')
forcePerLengthUom.pdlcm = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'pdl/cm', tag=u'pdlcm')
forcePerLengthUom.tonfUKft = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUK/ft', tag=u'tonfUKft')
forcePerLengthUom.tonfUSft = forcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS/ft', tag=u'tonfUSft')
forcePerLengthUom._InitializeFacetMap(forcePerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'forcePerLengthUom', forcePerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}forcePerVolumeUom
class forcePerVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'forcePerVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 234, 1)
    _Documentation = None
forcePerVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=forcePerVolumeUom, enum_prefix=None)
forcePerVolumeUom.Nm3 = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'N/m3', tag=u'Nm3')
forcePerVolumeUom.atm100m = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'atm/100m', tag=u'atm100m')
forcePerVolumeUom.atmm = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'atm/m', tag=u'atmm')
forcePerVolumeUom.barkm = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bar/km', tag=u'barkm')
forcePerVolumeUom.barm = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bar/m', tag=u'barm')
forcePerVolumeUom.GPacm = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'GPa/cm', tag=u'GPacm')
forcePerVolumeUom.kPa100m = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'kPa/100m', tag=u'kPa100m')
forcePerVolumeUom.kPam = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'kPa/m', tag=u'kPam')
forcePerVolumeUom.lbfft3 = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/ft3', tag=u'lbfft3')
forcePerVolumeUom.lbfgalUS = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/galUS', tag=u'lbfgalUS')
forcePerVolumeUom.MPam = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'MPa/m', tag=u'MPam')
forcePerVolumeUom.psift = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'psi/ft', tag=u'psift')
forcePerVolumeUom.psi100ft = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'psi/100ft', tag=u'psi100ft')
forcePerVolumeUom.psikft = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'psi/kft', tag=u'psikft')
forcePerVolumeUom.psim = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'psi/m', tag=u'psim')
forcePerVolumeUom.Pam = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Pa/m', tag=u'Pam')
forcePerVolumeUom.atmft = forcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'atm/ft', tag=u'atmft')
forcePerVolumeUom._InitializeFacetMap(forcePerVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'forcePerVolumeUom', forcePerVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}frequencyUom
class frequencyUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'frequencyUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 256, 1)
    _Documentation = None
frequencyUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=frequencyUom, enum_prefix=None)
frequencyUom.Hz = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'Hz', tag=u'Hz')
frequencyUom.cs = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'c/s', tag=u'cs')
frequencyUom.GHz = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'GHz', tag=u'GHz')
frequencyUom.kHz = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'kHz', tag=u'kHz')
frequencyUom.mHz = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'mHz', tag=u'mHz')
frequencyUom.MHz = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'MHz', tag=u'MHz')
frequencyUom.uHz = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'uHz', tag=u'uHz')
frequencyUom.n1s = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'1/s', tag=u'n1s')
frequencyUom.n1a = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'1/a', tag=u'n1a')
frequencyUom.n1d = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'1/d', tag=u'n1d')
frequencyUom.n1h = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'1/h', tag=u'n1h')
frequencyUom.n1min = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'1/min', tag=u'n1min')
frequencyUom.n1wk = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'1/wk', tag=u'n1wk')
frequencyUom.kEucs = frequencyUom._CF_enumeration.addEnumeration(unicode_value=u'kEuc/s', tag=u'kEucs')
frequencyUom._InitializeFacetMap(frequencyUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'frequencyUom', frequencyUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}illuminanceUom
class illuminanceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminanceUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 275, 1)
    _Documentation = None
illuminanceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=illuminanceUom, enum_prefix=None)
illuminanceUom.lx = illuminanceUom._CF_enumeration.addEnumeration(unicode_value=u'lx', tag=u'lx')
illuminanceUom.lmm2 = illuminanceUom._CF_enumeration.addEnumeration(unicode_value=u'lm/m2', tag=u'lmm2')
illuminanceUom.footcandle = illuminanceUom._CF_enumeration.addEnumeration(unicode_value=u'footcandle', tag=u'footcandle')
illuminanceUom.klx = illuminanceUom._CF_enumeration.addEnumeration(unicode_value=u'klx', tag=u'klx')
illuminanceUom._InitializeFacetMap(illuminanceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'illuminanceUom', illuminanceUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}lengthUom
class lengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 284, 1)
    _Documentation = None
lengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lengthUom, enum_prefix=None)
lengthUom.m = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'm', tag=u'm')
lengthUom.angstrom = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'angstrom', tag=u'angstrom')
lengthUom.chBnA = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'chBnA', tag=u'chBnA')
lengthUom.chBnB = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'chBnB', tag=u'chBnB')
lengthUom.chCla = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'chCla', tag=u'chCla')
lengthUom.chSe = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'chSe', tag=u'chSe')
lengthUom.chUS = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'chUS', tag=u'chUS')
lengthUom.cm = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'cm', tag=u'cm')
lengthUom.dm = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'dm', tag=u'dm')
lengthUom.fathom = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'fathom', tag=u'fathom')
lengthUom.fm = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'fm', tag=u'fm')
lengthUom.ft = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft', tag=u'ft')
lengthUom.ftBnA = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftBnA', tag=u'ftBnA')
lengthUom.ftBnB = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftBnB', tag=u'ftBnB')
lengthUom.ftBr65 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftBr(65)', tag=u'ftBr65')
lengthUom.ftCla = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftCla', tag=u'ftCla')
lengthUom.ftGC = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftGC', tag=u'ftGC')
lengthUom.ftInd = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftInd', tag=u'ftInd')
lengthUom.ftInd37 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftInd(37)', tag=u'ftInd37')
lengthUom.ftInd62 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftInd(62)', tag=u'ftInd62')
lengthUom.ftInd75 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftInd(75)', tag=u'ftInd75')
lengthUom.ftMA = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftMA', tag=u'ftMA')
lengthUom.ftSe = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftSe', tag=u'ftSe')
lengthUom.ftUS = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftUS', tag=u'ftUS')
lengthUom.in_ = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'in', tag=u'in_')
lengthUom.in10 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'in/10', tag=u'in10')
lengthUom.in16 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'in/16', tag=u'in16')
lengthUom.in32 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'in/32', tag=u'in32')
lengthUom.in64 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'in/64', tag=u'in64')
lengthUom.inUS = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'inUS', tag=u'inUS')
lengthUom.km = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'km', tag=u'km')
lengthUom.lkBnA = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'lkBnA', tag=u'lkBnA')
lengthUom.lkBnB = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'lkBnB', tag=u'lkBnB')
lengthUom.lkCla = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'lkCla', tag=u'lkCla')
lengthUom.lkSe = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'lkSe', tag=u'lkSe')
lengthUom.lkUS = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'lkUS', tag=u'lkUS')
lengthUom.mGer = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'mGer', tag=u'mGer')
lengthUom.mi = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'mi', tag=u'mi')
lengthUom.mil = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'mil', tag=u'mil')
lengthUom.miUS = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'miUS', tag=u'miUS')
lengthUom.mm = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'mm', tag=u'mm')
lengthUom.Mm = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'Mm', tag=u'Mm')
lengthUom.nautmi = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'nautmi', tag=u'nautmi')
lengthUom.nm = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'nm', tag=u'nm')
lengthUom.pm = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'pm', tag=u'pm')
lengthUom.um = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'um', tag=u'um')
lengthUom.yd = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'yd', tag=u'yd')
lengthUom.ydBnA = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydBnA', tag=u'ydBnA')
lengthUom.ydBnB = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydBnB', tag=u'ydBnB')
lengthUom.ydCla = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydCla', tag=u'ydCla')
lengthUom.ydIm = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydIm', tag=u'ydIm')
lengthUom.ydInd = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydInd', tag=u'ydInd')
lengthUom.ydInd37 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydInd(37)', tag=u'ydInd37')
lengthUom.ydInd62 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydInd(62)', tag=u'ydInd62')
lengthUom.ydInd75 = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydInd(75)', tag=u'ydInd75')
lengthUom.ydSe = lengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydSe', tag=u'ydSe')
lengthUom._InitializeFacetMap(lengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'lengthUom', lengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}lengthPerLengthUom
class lengthPerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lengthPerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 345, 1)
    _Documentation = None
lengthPerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lengthPerLengthUom, enum_prefix=None)
lengthPerLengthUom.emptyString = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
lengthPerLengthUom.ft100ft = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft/100ft', tag=u'ft100ft')
lengthPerLengthUom.ftft = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft/ft', tag=u'ftft')
lengthPerLengthUom.ftin = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft/in', tag=u'ftin')
lengthPerLengthUom.ftm = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft/m', tag=u'ftm')
lengthPerLengthUom.ftmi = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft/mi', tag=u'ftmi')
lengthPerLengthUom.kmcm = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'km/cm', tag=u'kmcm')
lengthPerLengthUom.m30m = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'm/30m', tag=u'm30m')
lengthPerLengthUom.mcm = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'm/cm', tag=u'mcm')
lengthPerLengthUom.mkm = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'm/km', tag=u'mkm')
lengthPerLengthUom.mm = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'm/m', tag=u'mm')
lengthPerLengthUom.miin = lengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'mi/in', tag=u'miin')
lengthPerLengthUom._InitializeFacetMap(lengthPerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'lengthPerLengthUom', lengthPerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}magneticFieldStrengthUom
class magneticFieldStrengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'magneticFieldStrengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 362, 1)
    _Documentation = None
magneticFieldStrengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=magneticFieldStrengthUom, enum_prefix=None)
magneticFieldStrengthUom.Am = magneticFieldStrengthUom._CF_enumeration.addEnumeration(unicode_value=u'A/m', tag=u'Am')
magneticFieldStrengthUom.Amm = magneticFieldStrengthUom._CF_enumeration.addEnumeration(unicode_value=u'A/mm', tag=u'Amm')
magneticFieldStrengthUom.gamma = magneticFieldStrengthUom._CF_enumeration.addEnumeration(unicode_value=u'gamma', tag=u'gamma')
magneticFieldStrengthUom.Oe = magneticFieldStrengthUom._CF_enumeration.addEnumeration(unicode_value=u'Oe', tag=u'Oe')
magneticFieldStrengthUom._InitializeFacetMap(magneticFieldStrengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'magneticFieldStrengthUom', magneticFieldStrengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}magneticInductionUom
class magneticInductionUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'magneticInductionUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 371, 1)
    _Documentation = None
magneticInductionUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=magneticInductionUom, enum_prefix=None)
magneticInductionUom.T = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'T', tag=u'T')
magneticInductionUom.gauss = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'gauss', tag=u'gauss')
magneticInductionUom.mT = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'mT', tag=u'mT')
magneticInductionUom.mgauss = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'mgauss', tag=u'mgauss')
magneticInductionUom.nT = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'nT', tag=u'nT')
magneticInductionUom.uT = magneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'uT', tag=u'uT')
magneticInductionUom._InitializeFacetMap(magneticInductionUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'magneticInductionUom', magneticInductionUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}massConcentrationUom
class massConcentrationUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'massConcentrationUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 382, 1)
    _Documentation = None
massConcentrationUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=massConcentrationUom, enum_prefix=None)
massConcentrationUom.Euc = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'Euc', tag=u'Euc')
massConcentrationUom.emptyString = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
massConcentrationUom.gkg = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'g/kg', tag=u'gkg')
massConcentrationUom.kgkg = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'kg/kg', tag=u'kgkg')
massConcentrationUom.kgsack94 = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'kg/sack94', tag=u'kgsack94')
massConcentrationUom.mgkg = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'mg/kg', tag=u'mgkg')
massConcentrationUom.permil = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'permil', tag=u'permil')
massConcentrationUom.ppdk = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'ppdk', tag=u'ppdk')
massConcentrationUom.ppk = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'ppk', tag=u'ppk')
massConcentrationUom.ppm = massConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'ppm', tag=u'ppm')
massConcentrationUom._InitializeFacetMap(massConcentrationUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'massConcentrationUom', massConcentrationUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}massUom
class massUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'massUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 397, 1)
    _Documentation = None
massUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=massUom, enum_prefix=None)
massUom.kg = massUom._CF_enumeration.addEnumeration(unicode_value=u'kg', tag=u'kg')
massUom.ag = massUom._CF_enumeration.addEnumeration(unicode_value=u'ag', tag=u'ag')
massUom.ct = massUom._CF_enumeration.addEnumeration(unicode_value=u'ct', tag=u'ct')
massUom.cwtUK = massUom._CF_enumeration.addEnumeration(unicode_value=u'cwtUK', tag=u'cwtUK')
massUom.cwtUS = massUom._CF_enumeration.addEnumeration(unicode_value=u'cwtUS', tag=u'cwtUS')
massUom.g = massUom._CF_enumeration.addEnumeration(unicode_value=u'g', tag=u'g')
massUom.grain = massUom._CF_enumeration.addEnumeration(unicode_value=u'grain', tag=u'grain')
massUom.klbm = massUom._CF_enumeration.addEnumeration(unicode_value=u'klbm', tag=u'klbm')
massUom.lbm = massUom._CF_enumeration.addEnumeration(unicode_value=u'lbm', tag=u'lbm')
massUom.Mg = massUom._CF_enumeration.addEnumeration(unicode_value=u'Mg', tag=u'Mg')
massUom.mg = massUom._CF_enumeration.addEnumeration(unicode_value=u'mg', tag=u'mg')
massUom.ozav = massUom._CF_enumeration.addEnumeration(unicode_value=u'oz(av)', tag=u'ozav')
massUom.oztroy = massUom._CF_enumeration.addEnumeration(unicode_value=u'oz(troy)', tag=u'oztroy')
massUom.ozm = massUom._CF_enumeration.addEnumeration(unicode_value=u'ozm', tag=u'ozm')
massUom.sack94 = massUom._CF_enumeration.addEnumeration(unicode_value=u'sack94', tag=u'sack94')
massUom.t = massUom._CF_enumeration.addEnumeration(unicode_value=u't', tag=u't')
massUom.tonUK = massUom._CF_enumeration.addEnumeration(unicode_value=u'tonUK', tag=u'tonUK')
massUom.tonUS = massUom._CF_enumeration.addEnumeration(unicode_value=u'tonUS', tag=u'tonUS')
massUom.ug = massUom._CF_enumeration.addEnumeration(unicode_value=u'ug', tag=u'ug')
massUom._InitializeFacetMap(massUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'massUom', massUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}massPerLengthUom
class massPerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'massPerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 421, 1)
    _Documentation = None
massPerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=massPerLengthUom, enum_prefix=None)
massPerLengthUom.kgm = massPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'kg/m', tag=u'kgm')
massPerLengthUom.klbmin = massPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'klbm/in', tag=u'klbmin')
massPerLengthUom.lbmft = massPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/ft', tag=u'lbmft')
massPerLengthUom.Mgin = massPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'Mg/in', tag=u'Mgin')
massPerLengthUom.kg_mcm2 = massPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'kg.m/cm2', tag=u'kg_mcm2')
massPerLengthUom._InitializeFacetMap(massPerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'massPerLengthUom', massPerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}momentOfForceUom
class momentOfForceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'momentOfForceUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 431, 1)
    _Documentation = None
momentOfForceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=momentOfForceUom, enum_prefix=None)
momentOfForceUom.J = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'J', tag=u'J')
momentOfForceUom.dN_m = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'dN.m', tag=u'dN_m')
momentOfForceUom.daN_m = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'daN.m', tag=u'daN_m')
momentOfForceUom.ft_lbf = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'ft.lbf', tag=u'ft_lbf')
momentOfForceUom.kft_lbf = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'kft.lbf', tag=u'kft_lbf')
momentOfForceUom.kgf_m = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'kgf.m', tag=u'kgf_m')
momentOfForceUom.kN_m = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'kN.m', tag=u'kN_m')
momentOfForceUom.lbf_ft = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'lbf.ft', tag=u'lbf_ft')
momentOfForceUom.lbf_in = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'lbf.in', tag=u'lbf_in')
momentOfForceUom.lbm_ft2s2 = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'lbm.ft2/s2', tag=u'lbm_ft2s2')
momentOfForceUom.N_m = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'N.m', tag=u'N_m')
momentOfForceUom.pdl_ft = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'pdl.ft', tag=u'pdl_ft')
momentOfForceUom.tonfUS_ft = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS.ft', tag=u'tonfUS_ft')
momentOfForceUom.tonfUS_mi = momentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS.mi', tag=u'tonfUS_mi')
momentOfForceUom._InitializeFacetMap(momentOfForceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'momentOfForceUom', momentOfForceUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}perLengthUom
class perLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'perLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 450, 1)
    _Documentation = None
perLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=perLengthUom, enum_prefix=None)
perLengthUom.n1m = perLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/m', tag=u'n1m')
perLengthUom.n1angstrom = perLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/angstrom', tag=u'n1angstrom')
perLengthUom.n1cm = perLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/cm', tag=u'n1cm')
perLengthUom.n1ft = perLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/ft', tag=u'n1ft')
perLengthUom.n1in = perLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/in', tag=u'n1in')
perLengthUom.n1mi = perLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/mi', tag=u'n1mi')
perLengthUom.n1mm = perLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/mm', tag=u'n1mm')
perLengthUom.n1nm = perLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/nm', tag=u'n1nm')
perLengthUom.n1yd = perLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/yd', tag=u'n1yd')
perLengthUom._InitializeFacetMap(perLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'perLengthUom', perLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}planeAngleUom
class planeAngleUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'planeAngleUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 464, 1)
    _Documentation = None
planeAngleUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=planeAngleUom, enum_prefix=None)
planeAngleUom.rad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'rad', tag=u'rad')
planeAngleUom.c = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'c', tag=u'c')
planeAngleUom.ccgr = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'ccgr', tag=u'ccgr')
planeAngleUom.cgr = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'cgr', tag=u'cgr')
planeAngleUom.dega = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'dega', tag=u'dega')
planeAngleUom.gon = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'gon', tag=u'gon')
planeAngleUom.gr = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'gr', tag=u'gr')
planeAngleUom.Grad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'Grad', tag=u'Grad')
planeAngleUom.krad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'krad', tag=u'krad')
planeAngleUom.mila = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'mila', tag=u'mila')
planeAngleUom.mina = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'mina', tag=u'mina')
planeAngleUom.mrad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'mrad', tag=u'mrad')
planeAngleUom.Mrad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'Mrad', tag=u'Mrad')
planeAngleUom.mseca = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'mseca', tag=u'mseca')
planeAngleUom.seca = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'seca', tag=u'seca')
planeAngleUom.urad = planeAngleUom._CF_enumeration.addEnumeration(unicode_value=u'urad', tag=u'urad')
planeAngleUom._InitializeFacetMap(planeAngleUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'planeAngleUom', planeAngleUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}powerUom
class powerUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'powerUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 485, 1)
    _Documentation = None
powerUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=powerUom, enum_prefix=None)
powerUom.W = powerUom._CF_enumeration.addEnumeration(unicode_value=u'W', tag=u'W')
powerUom.ch = powerUom._CF_enumeration.addEnumeration(unicode_value=u'ch', tag=u'ch')
powerUom.CV = powerUom._CF_enumeration.addEnumeration(unicode_value=u'CV', tag=u'CV')
powerUom.ehp = powerUom._CF_enumeration.addEnumeration(unicode_value=u'ehp', tag=u'ehp')
powerUom.GW = powerUom._CF_enumeration.addEnumeration(unicode_value=u'GW', tag=u'GW')
powerUom.hhp = powerUom._CF_enumeration.addEnumeration(unicode_value=u'hhp', tag=u'hhp')
powerUom.hp = powerUom._CF_enumeration.addEnumeration(unicode_value=u'hp', tag=u'hp')
powerUom.kcalh = powerUom._CF_enumeration.addEnumeration(unicode_value=u'kcal/h', tag=u'kcalh')
powerUom.kW = powerUom._CF_enumeration.addEnumeration(unicode_value=u'kW', tag=u'kW')
powerUom.MJa = powerUom._CF_enumeration.addEnumeration(unicode_value=u'MJ/a', tag=u'MJa')
powerUom.MW = powerUom._CF_enumeration.addEnumeration(unicode_value=u'MW', tag=u'MW')
powerUom.mW = powerUom._CF_enumeration.addEnumeration(unicode_value=u'mW', tag=u'mW')
powerUom.nW = powerUom._CF_enumeration.addEnumeration(unicode_value=u'nW', tag=u'nW')
powerUom.ton_of_refrig = powerUom._CF_enumeration.addEnumeration(unicode_value=u'ton of refrig', tag=u'ton_of_refrig')
powerUom.TW = powerUom._CF_enumeration.addEnumeration(unicode_value=u'TW', tag=u'TW')
powerUom.uW = powerUom._CF_enumeration.addEnumeration(unicode_value=u'uW', tag=u'uW')
powerUom._InitializeFacetMap(powerUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'powerUom', powerUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}pressureUom
class pressureUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pressureUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 506, 1)
    _Documentation = None
pressureUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=pressureUom, enum_prefix=None)
pressureUom.Pa = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'Pa', tag=u'Pa')
pressureUom.at = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'at', tag=u'at')
pressureUom.atm = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'atm', tag=u'atm')
pressureUom.bar = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'bar', tag=u'bar')
pressureUom.cmH2O4degC = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'cmH2O(4degC)', tag=u'cmH2O4degC')
pressureUom.dynecm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'dyne/cm2', tag=u'dynecm2')
pressureUom.GPa = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'GPa', tag=u'GPa')
pressureUom.hbar = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'hbar', tag=u'hbar')
pressureUom.inH2O39_2F = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'inH2O(39.2F)', tag=u'inH2O39_2F')
pressureUom.inH2O60F = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'inH2O(60F)', tag=u'inH2O60F')
pressureUom.inHg32F = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'inHg(32F)', tag=u'inHg32F')
pressureUom.inHg60F = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'inHg(60F)', tag=u'inHg60F')
pressureUom.kgfcm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'kgf/cm2', tag=u'kgfcm2')
pressureUom.kgfmm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'kgf/mm2', tag=u'kgfmm2')
pressureUom.kNm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'kN/m2', tag=u'kNm2')
pressureUom.kPa = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'kPa', tag=u'kPa')
pressureUom.kpsi = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'kpsi', tag=u'kpsi')
pressureUom.lbfft2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/ft2', tag=u'lbfft2')
pressureUom.lbf100ft2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/100ft2', tag=u'lbf100ft2')
pressureUom.lbfin2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/in2', tag=u'lbfin2')
pressureUom.mbar = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'mbar', tag=u'mbar')
pressureUom.mmHg0C = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'mmHg(0C)', tag=u'mmHg0C')
pressureUom.mPa = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'mPa', tag=u'mPa')
pressureUom.MPa = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'MPa', tag=u'MPa')
pressureUom.Mpsi = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'Mpsi', tag=u'Mpsi')
pressureUom.Nm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'N/m2', tag=u'Nm2')
pressureUom.Nmm2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'N/mm2', tag=u'Nmm2')
pressureUom.Pag = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'Pa(g)', tag=u'Pag')
pressureUom.pPa = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'pPa', tag=u'pPa')
pressureUom.psi = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'psi', tag=u'psi')
pressureUom.psia = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'psia', tag=u'psia')
pressureUom.psig = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'psig', tag=u'psig')
pressureUom.tonfUSft2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS/ft2', tag=u'tonfUSft2')
pressureUom.tonfUSin2 = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS/in2', tag=u'tonfUSin2')
pressureUom.torr = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'torr', tag=u'torr')
pressureUom.ubar = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'ubar', tag=u'ubar')
pressureUom.umHg0C = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'umHg(0C)', tag=u'umHg0C')
pressureUom.uPa = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'uPa', tag=u'uPa')
pressureUom.upsi = pressureUom._CF_enumeration.addEnumeration(unicode_value=u'upsi', tag=u'upsi')
pressureUom._InitializeFacetMap(pressureUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'pressureUom', pressureUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}relativePowerUom
class relativePowerUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'relativePowerUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 550, 1)
    _Documentation = None
relativePowerUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=relativePowerUom, enum_prefix=None)
relativePowerUom.emptyString = relativePowerUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
relativePowerUom.Btubhp_hr = relativePowerUom._CF_enumeration.addEnumeration(unicode_value=u'Btu/bhp.hr', tag=u'Btubhp_hr')
relativePowerUom.WkW = relativePowerUom._CF_enumeration.addEnumeration(unicode_value=u'W/kW', tag=u'WkW')
relativePowerUom.WW = relativePowerUom._CF_enumeration.addEnumeration(unicode_value=u'W/W', tag=u'WW')
relativePowerUom._InitializeFacetMap(relativePowerUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'relativePowerUom', relativePowerUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}specificVolumeUom
class specificVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'specificVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 559, 1)
    _Documentation = None
specificVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=specificVolumeUom, enum_prefix=None)
specificVolumeUom.m3kg = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/kg', tag=u'm3kg')
specificVolumeUom.bbltonUK = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/tonUK', tag=u'bbltonUK')
specificVolumeUom.bbltonUS = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/tonUS', tag=u'bbltonUS')
specificVolumeUom.cm3g = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/g', tag=u'cm3g')
specificVolumeUom.dm3kg = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'dm3/kg', tag=u'dm3kg')
specificVolumeUom.dm3t = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'dm3/t', tag=u'dm3t')
specificVolumeUom.ft3kg = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/kg', tag=u'ft3kg')
specificVolumeUom.ft3lbm = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/lbm', tag=u'ft3lbm')
specificVolumeUom.ft3sack94 = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/sack94', tag=u'ft3sack94')
specificVolumeUom.galUSsack94 = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/sack94', tag=u'galUSsack94')
specificVolumeUom.galUKlbm = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/lbm', tag=u'galUKlbm')
specificVolumeUom.galUSlbm = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/lbm', tag=u'galUSlbm')
specificVolumeUom.galUStonUK = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/tonUK', tag=u'galUStonUK')
specificVolumeUom.galUStonUS = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/tonUS', tag=u'galUStonUS')
specificVolumeUom.L100kg = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/100kg', tag=u'L100kg')
specificVolumeUom.Lkg = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/kg', tag=u'Lkg')
specificVolumeUom.Lt = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/t', tag=u'Lt')
specificVolumeUom.LtonUK = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/tonUK', tag=u'LtonUK')
specificVolumeUom.m3g = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/g', tag=u'm3g')
specificVolumeUom.m3t = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/t', tag=u'm3t')
specificVolumeUom.m3tonUK = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/tonUK', tag=u'm3tonUK')
specificVolumeUom.m3tonUS = specificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/tonUS', tag=u'm3tonUS')
specificVolumeUom._InitializeFacetMap(specificVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'specificVolumeUom', specificVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}thermodynamicTemperatureUom
class thermodynamicTemperatureUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'thermodynamicTemperatureUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 586, 1)
    _Documentation = None
thermodynamicTemperatureUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=thermodynamicTemperatureUom, enum_prefix=None)
thermodynamicTemperatureUom.K = thermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value=u'K', tag=u'K')
thermodynamicTemperatureUom.degC = thermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value=u'degC', tag=u'degC')
thermodynamicTemperatureUom.degF = thermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value=u'degF', tag=u'degF')
thermodynamicTemperatureUom.degR = thermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value=u'degR', tag=u'degR')
thermodynamicTemperatureUom._InitializeFacetMap(thermodynamicTemperatureUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'thermodynamicTemperatureUom', thermodynamicTemperatureUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}timeUom
class timeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 595, 1)
    _Documentation = None
timeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=timeUom, enum_prefix=None)
timeUom.s = timeUom._CF_enumeration.addEnumeration(unicode_value=u's', tag=u's')
timeUom.a = timeUom._CF_enumeration.addEnumeration(unicode_value=u'a', tag=u'a')
timeUom.cs = timeUom._CF_enumeration.addEnumeration(unicode_value=u'cs', tag=u'cs')
timeUom.d = timeUom._CF_enumeration.addEnumeration(unicode_value=u'd', tag=u'd')
timeUom.Ga = timeUom._CF_enumeration.addEnumeration(unicode_value=u'Ga', tag=u'Ga')
timeUom.h = timeUom._CF_enumeration.addEnumeration(unicode_value=u'h', tag=u'h')
timeUom.n100s = timeUom._CF_enumeration.addEnumeration(unicode_value=u'100s', tag=u'n100s')
timeUom.Ma = timeUom._CF_enumeration.addEnumeration(unicode_value=u'Ma', tag=u'Ma')
timeUom.min = timeUom._CF_enumeration.addEnumeration(unicode_value=u'min', tag=u'min')
timeUom.ms = timeUom._CF_enumeration.addEnumeration(unicode_value=u'ms', tag=u'ms')
timeUom.ms2 = timeUom._CF_enumeration.addEnumeration(unicode_value=u'ms/2', tag=u'ms2')
timeUom.ns = timeUom._CF_enumeration.addEnumeration(unicode_value=u'ns', tag=u'ns')
timeUom.ps = timeUom._CF_enumeration.addEnumeration(unicode_value=u'ps', tag=u'ps')
timeUom.us = timeUom._CF_enumeration.addEnumeration(unicode_value=u'us', tag=u'us')
timeUom.wk = timeUom._CF_enumeration.addEnumeration(unicode_value=u'wk', tag=u'wk')
timeUom.n100ka = timeUom._CF_enumeration.addEnumeration(unicode_value=u'100ka', tag=u'n100ka')
timeUom._InitializeFacetMap(timeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'timeUom', timeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}velocityUom
class velocityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'velocityUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 616, 1)
    _Documentation = None
velocityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=velocityUom, enum_prefix=None)
velocityUom.ms = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'm/s', tag=u'ms')
velocityUom.cma = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'cm/a', tag=u'cma')
velocityUom.cms = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'cm/s', tag=u'cms')
velocityUom.dms = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'dm/s', tag=u'dms')
velocityUom.ftd = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/d', tag=u'ftd')
velocityUom.fth = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/h', tag=u'fth')
velocityUom.ftmin = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/min', tag=u'ftmin')
velocityUom.ftms = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/ms', tag=u'ftms')
velocityUom.fts = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/s', tag=u'fts')
velocityUom.ftus = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/us', tag=u'ftus')
velocityUom.ina = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'in/a', tag=u'ina')
velocityUom.inmin = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'in/min', tag=u'inmin')
velocityUom.ins = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'in/s', tag=u'ins')
velocityUom.kfth = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'kft/h', tag=u'kfth')
velocityUom.kfts = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'kft/s', tag=u'kfts')
velocityUom.kmh = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'km/h', tag=u'kmh')
velocityUom.kms = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'km/s', tag=u'kms')
velocityUom.knot = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'knot', tag=u'knot')
velocityUom.md = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'm/d', tag=u'md')
velocityUom.mh = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'm/h', tag=u'mh')
velocityUom.mmin = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'm/min', tag=u'mmin')
velocityUom.mms = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'm/ms', tag=u'mms')
velocityUom.mih = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'mi/h', tag=u'mih')
velocityUom.milyr = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'mil/yr', tag=u'milyr')
velocityUom.mma = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'mm/a', tag=u'mma')
velocityUom.mms_ = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'mm/s', tag=u'mms_')
velocityUom.nms = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'nm/s', tag=u'nms')
velocityUom.ums = velocityUom._CF_enumeration.addEnumeration(unicode_value=u'um/s', tag=u'ums')
velocityUom._InitializeFacetMap(velocityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'velocityUom', velocityUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}volumeUom
class volumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 649, 1)
    _Documentation = None
volumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=volumeUom, enum_prefix=None)
volumeUom.m3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3', tag=u'm3')
volumeUom.acre_ft = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'acre.ft', tag=u'acre_ft')
volumeUom.bbl = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl', tag=u'bbl')
volumeUom.bcf = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'bcf', tag=u'bcf')
volumeUom.cm3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'cm3', tag=u'cm3')
volumeUom.dm3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'dm3', tag=u'dm3')
volumeUom.flozUK = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'flozUK', tag=u'flozUK')
volumeUom.flozUS = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'flozUS', tag=u'flozUS')
volumeUom.ft3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3', tag=u'ft3')
volumeUom.galUK = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUK', tag=u'galUK')
volumeUom.galUS = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS', tag=u'galUS')
volumeUom.ha_m = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'ha.m', tag=u'ha_m')
volumeUom.hL = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'hL', tag=u'hL')
volumeUom.in3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'in3', tag=u'in3')
volumeUom.n1000ft3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'1000ft3', tag=u'n1000ft3')
volumeUom.km3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'km3', tag=u'km3')
volumeUom.L = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'L', tag=u'L')
volumeUom.Mbbl = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'Mbbl', tag=u'Mbbl')
volumeUom.Mcf = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'Mcf', tag=u'Mcf')
volumeUom.Mft3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'M(ft3)', tag=u'Mft3')
volumeUom.mi3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'mi3', tag=u'mi3')
volumeUom.mL = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'mL', tag=u'mL')
volumeUom.Mm3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'M(m3)', tag=u'Mm3')
volumeUom.mm3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'mm3', tag=u'mm3')
volumeUom.MMbbl = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'MMbbl', tag=u'MMbbl')
volumeUom.ptUK = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'ptUK', tag=u'ptUK')
volumeUom.ptUS = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'ptUS', tag=u'ptUS')
volumeUom.qtUK = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'qtUK', tag=u'qtUK')
volumeUom.qtUS = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'qtUS', tag=u'qtUS')
volumeUom.tcf = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'tcf', tag=u'tcf')
volumeUom.um2_m = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'um2.m', tag=u'um2_m')
volumeUom.yd3 = volumeUom._CF_enumeration.addEnumeration(unicode_value=u'yd3', tag=u'yd3')
volumeUom._InitializeFacetMap(volumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'volumeUom', volumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}volumeFlowRateUom
class volumeFlowRateUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumeFlowRateUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 686, 1)
    _Documentation = None
volumeFlowRateUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=volumeFlowRateUom, enum_prefix=None)
volumeFlowRateUom.m3s = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'm3/s', tag=u'm3s')
volumeFlowRateUom.bbld = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/d', tag=u'bbld')
volumeFlowRateUom.bblhr = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/hr', tag=u'bblhr')
volumeFlowRateUom.bblmin = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/min', tag=u'bblmin')
volumeFlowRateUom.cm330min = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/30min', tag=u'cm330min')
volumeFlowRateUom.cm3h = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/h', tag=u'cm3h')
volumeFlowRateUom.cm3min = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/min', tag=u'cm3min')
volumeFlowRateUom.cm3s = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/s', tag=u'cm3s')
volumeFlowRateUom.dm3s = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'dm3/s', tag=u'dm3s')
volumeFlowRateUom.ft3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/d', tag=u'ft3d')
volumeFlowRateUom.ft3h = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/h', tag=u'ft3h')
volumeFlowRateUom.ft3min = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/min', tag=u'ft3min')
volumeFlowRateUom.ft3s = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/s', tag=u'ft3s')
volumeFlowRateUom.galUKd = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/d', tag=u'galUKd')
volumeFlowRateUom.galUKhr = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/hr', tag=u'galUKhr')
volumeFlowRateUom.galUKmin = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/min', tag=u'galUKmin')
volumeFlowRateUom.galUSd = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/d', tag=u'galUSd')
volumeFlowRateUom.galUShr = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/hr', tag=u'galUShr')
volumeFlowRateUom.galUSmin = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/min', tag=u'galUSmin')
volumeFlowRateUom.kbbld = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'kbbl/d', tag=u'kbbld')
volumeFlowRateUom.n1000ft3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'1000ft3/d', tag=u'n1000ft3d')
volumeFlowRateUom.n1000m3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'1000m3/d', tag=u'n1000m3d')
volumeFlowRateUom.n1000m3h = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'1000m3/h', tag=u'n1000m3h')
volumeFlowRateUom.Lh = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'L/h', tag=u'Lh')
volumeFlowRateUom.Lmin = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'L/min', tag=u'Lmin')
volumeFlowRateUom.Ls = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'L/s', tag=u'Ls')
volumeFlowRateUom.m3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'm3/d', tag=u'm3d')
volumeFlowRateUom.m3h = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'm3/h', tag=u'm3h')
volumeFlowRateUom.m3min = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'm3/min', tag=u'm3min')
volumeFlowRateUom.Mbbld = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'Mbbl/d', tag=u'Mbbld')
volumeFlowRateUom.Mft3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'M(ft3)/d', tag=u'Mft3d')
volumeFlowRateUom.Mm3d = volumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'M(m3)/d', tag=u'Mm3d')
volumeFlowRateUom._InitializeFacetMap(volumeFlowRateUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'volumeFlowRateUom', volumeFlowRateUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}volumePerVolumeUom
class volumePerVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumePerVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_quantityClass.xsd', 723, 1)
    _Documentation = None
volumePerVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=volumePerVolumeUom, enum_prefix=None)
volumePerVolumeUom.Euc = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Euc', tag=u'Euc')
volumePerVolumeUom.emptyString = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
volumePerVolumeUom.permil = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'permil', tag=u'permil')
volumePerVolumeUom.ppdk = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ppdk', tag=u'ppdk')
volumePerVolumeUom.ppk = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ppk', tag=u'ppk')
volumePerVolumeUom.ppm = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ppm', tag=u'ppm')
volumePerVolumeUom.bblacre_ft = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/acre.ft', tag=u'bblacre_ft')
volumePerVolumeUom.bblbbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/bbl', tag=u'bblbbl')
volumePerVolumeUom.bblft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/ft3', tag=u'bblft3')
volumePerVolumeUom.bbl100bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/100bbl', tag=u'bbl100bbl')
volumePerVolumeUom.bblkft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/k(ft3)', tag=u'bblkft3')
volumePerVolumeUom.bblMft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/M(ft3)', tag=u'bblMft3')
volumePerVolumeUom.cm3cm3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/cm3', tag=u'cm3cm3')
volumePerVolumeUom.cm3m3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/m3', tag=u'cm3m3')
volumePerVolumeUom.dm3m3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'dm3/m3', tag=u'dm3m3')
volumePerVolumeUom.ft3bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/bbl', tag=u'ft3bbl')
volumePerVolumeUom.ft3ft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/ft3', tag=u'ft3ft3')
volumePerVolumeUom.galUSkgalUS = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/kgalUS', tag=u'galUSkgalUS')
volumePerVolumeUom.galUKkgalUK = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/kgalUK', tag=u'galUKkgalUK')
volumePerVolumeUom.galUKft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/ft3', tag=u'galUKft3')
volumePerVolumeUom.galUKMbbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/Mbbl', tag=u'galUKMbbl')
volumePerVolumeUom.galUSbbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/bbl', tag=u'galUSbbl')
volumePerVolumeUom.galUS10bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/10bbl', tag=u'galUS10bbl')
volumePerVolumeUom.galUSft3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/ft3', tag=u'galUSft3')
volumePerVolumeUom.galUSMbbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/Mbbl', tag=u'galUSMbbl')
volumePerVolumeUom.n1000ft3bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'1000ft3/bbl', tag=u'n1000ft3bbl')
volumePerVolumeUom.ksm3sm3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ksm3/sm3', tag=u'ksm3sm3')
volumePerVolumeUom.L10bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/10bbl', tag=u'L10bbl')
volumePerVolumeUom.Lm3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/m3', tag=u'Lm3')
volumePerVolumeUom.m3ha_m = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/ha.m', tag=u'm3ha_m')
volumePerVolumeUom.m3m3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/m3', tag=u'm3m3')
volumePerVolumeUom.Mft3acre_ft = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'M(ft3)/acre.ft', tag=u'Mft3acre_ft')
volumePerVolumeUom.mLgalUK = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'mL/galUK', tag=u'mLgalUK')
volumePerVolumeUom.mLgalUS = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'mL/galUS', tag=u'mLgalUS')
volumePerVolumeUom.mLmL = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'mL/mL', tag=u'mLmL')
volumePerVolumeUom.MMbblacre_ft = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'MMbbl/acre.ft', tag=u'MMbblacre_ft')
volumePerVolumeUom.MMscf60stb60 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'MMscf60/stb60', tag=u'MMscf60stb60')
volumePerVolumeUom.Mscf60stb60 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Mscf60/stb60', tag=u'Mscf60stb60')
volumePerVolumeUom.ptUKMbbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ptUK/Mbbl', tag=u'ptUKMbbl')
volumePerVolumeUom.ptUS10bbl = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ptUS/10bbl', tag=u'ptUS10bbl')
volumePerVolumeUom.pu = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'pu', tag=u'pu')
volumePerVolumeUom.scm15stb60 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'scm15/stb60', tag=u'scm15stb60')
volumePerVolumeUom.sm3ksm3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'sm3/ksm3', tag=u'sm3ksm3')
volumePerVolumeUom.sm3sm3 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'sm3/sm3', tag=u'sm3sm3')
volumePerVolumeUom.stb60MMscf60 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb60/MMscf60', tag=u'stb60MMscf60')
volumePerVolumeUom.stb60MMscm15 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb60/MMscm15', tag=u'stb60MMscm15')
volumePerVolumeUom.stb60Mscf60 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb60/Mscf60', tag=u'stb60Mscf60')
volumePerVolumeUom.stb60Mscm15 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb60/Mscm15', tag=u'stb60Mscm15')
volumePerVolumeUom.stb60scm15 = volumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb60/scm15', tag=u'stb60scm15')
volumePerVolumeUom._InitializeFacetMap(volumePerVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'volumePerVolumeUom', volumePerVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/131}commentString
class commentString (abstractCommentString):

    """A comment or remark intended for human consumption. 
			There should be no assumption that semantics can be extracted from this field by a computer. 
			Neither should there be an assumption that any two humans will interpret the information 
			in the same way (i.e., it may not be interoperable)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'commentString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 321, 1)
    _Documentation = u'A comment or remark intended for human consumption. \n\t\t\tThere should be no assumption that semantics can be extracted from this field by a computer. \n\t\t\tNeither should there be an assumption that any two humans will interpret the information \n\t\t\tin the same way (i.e., it may not be interoperable).'
commentString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'commentString', commentString)

# Complex type {http://www.witsml.org/schemas/131}cs_commonData with content type ELEMENT_ONLY
class cs_commonData (pyxb.binding.basis.complexTypeDefinition):
    """ WITSML - Common Data Component Schema """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_commonData')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}sourceName uses Python identifier sourceName
    __sourceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sourceName'), 'sourceName', '__httpwww_witsml_orgschemas131_cs_commonData_httpwww_witsml_orgschemas131sourceName', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 23, 3), )

    
    sourceName = property(__sourceName.value, __sourceName.set, None, u'An identifier to indicate the data originator.\n\t\t\t\t\tThis identifies the server that originally created \n\t\t\t\t\tthe object and thus most of the uids in the object (but not \n\t\t\t\t\tnecessarily the uids of the parents). This is typically a url. ')

    
    # Element {http://www.witsml.org/schemas/131}dTimCreation uses Python identifier dTimCreation
    __dTimCreation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dTimCreation'), 'dTimCreation', '__httpwww_witsml_orgschemas131_cs_commonData_httpwww_witsml_orgschemas131dTimCreation', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 31, 3), )

    
    dTimCreation = property(__dTimCreation.value, __dTimCreation.set, None, u'When the data was created at the persistent data store.  ')

    
    # Element {http://www.witsml.org/schemas/131}dTimLastChange uses Python identifier dTimLastChange
    __dTimLastChange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dTimLastChange'), 'dTimLastChange', '__httpwww_witsml_orgschemas131_cs_commonData_httpwww_witsml_orgschemas131dTimLastChange', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 36, 3), )

    
    dTimLastChange = property(__dTimLastChange.value, __dTimLastChange.set, None, u'Last change of any element of the data at the persistent data store.\n\t\t\t\t\tThe change time is not updated for a growing object while it is growing.  ')

    
    # Element {http://www.witsml.org/schemas/131}itemState uses Python identifier itemState
    __itemState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'itemState'), 'itemState', '__httpwww_witsml_orgschemas131_cs_commonData_httpwww_witsml_orgschemas131itemState', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 42, 3), )

    
    itemState = property(__itemState.value, __itemState.set, None, u'The item state for the data object.  ')

    
    # Element {http://www.witsml.org/schemas/131}comments uses Python identifier comments
    __comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comments'), 'comments', '__httpwww_witsml_orgschemas131_cs_commonData_httpwww_witsml_orgschemas131comments', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 47, 3), )

    
    comments = property(__comments.value, __comments.set, None, u'Comments and remarks.  ')


    _ElementMap = {
        __sourceName.name() : __sourceName,
        __dTimCreation.name() : __dTimCreation,
        __dTimLastChange.name() : __dTimLastChange,
        __itemState.name() : __itemState,
        __comments.name() : __comments
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_commonData', cs_commonData)


# Complex type {http://www.witsml.org/schemas/131}cs_customData with content type ELEMENT_ONLY
class cs_customData (pyxb.binding.basis.complexTypeDefinition):
    """ WITSML - Custom or User Defined Element and Attributes Component Schema.
			Specify custom element, attributes, and types in the custom data area."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_customData')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_customData.xsd', 16, 1)
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_customData', cs_customData)


# Complex type {http://www.witsml.org/schemas/131}cs_documentInfo with content type ELEMENT_ONLY
class cs_documentInfo (pyxb.binding.basis.complexTypeDefinition):
    """A  schema to capture a set of data that is 
			relevant for many exchange documents. It includes information about the 
			file that was created, and high-level information about the data that is 
			being exchanged within the file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_documentInfo')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}DocumentName uses Python identifier DocumentName
    __DocumentName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DocumentName'), 'DocumentName', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131DocumentName', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 26, 3), )

    
    DocumentName = property(__DocumentName.value, __DocumentName.set, None, u'An identifier for the document. This is \n\t\t\t\t\tintended to be unique within the context of the NamingSystem.')

    
    # Element {http://www.witsml.org/schemas/131}DocumentAlias uses Python identifier DocumentAlias
    __DocumentAlias = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DocumentAlias'), 'DocumentAlias', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131DocumentAlias', True, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 32, 3), )

    
    DocumentAlias = property(__DocumentAlias.value, __DocumentAlias.set, None, u'Zero or more alternate names for the document. \n\t\t\t\t\tThese names do not need to be unique within the naming system.')

    
    # Element {http://www.witsml.org/schemas/131}DocumentDate uses Python identifier DocumentDate
    __DocumentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DocumentDate'), 'DocumentDate', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131DocumentDate', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 38, 3), )

    
    DocumentDate = property(__DocumentDate.value, __DocumentDate.set, None, u'The date of the creation of the document. \n\t\t\t\t\tThis is not the same as the date that the file was created. \n\t\t\t\t\tFor this date, the document is considered to be the set of \n\t\t\t\t\tinformation associated with this document information. \n\t\t\t\t\tFor example, the document may be a seismic binset. \n\t\t\t\t\tThis represents the date that the binset was created. \n\t\t\t\t\tThe FileCreation information would capture the date that \n\t\t\t\t\tthe XML file was created to send or exchange the binset.')

    
    # Element {http://www.witsml.org/schemas/131}documentClass uses Python identifier documentClass
    __documentClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'documentClass'), 'documentClass', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131documentClass', True, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 50, 3), )

    
    documentClass = property(__documentClass.value, __documentClass.set, None, u'A document class. Examples of classes would be a \n\t\t\t\t\tmetadata classification or a set of keywords. ')

    
    # Element {http://www.witsml.org/schemas/131}FileCreationInformation uses Python identifier FileCreationInformation
    __FileCreationInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileCreationInformation'), 'FileCreationInformation', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131FileCreationInformation', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 56, 3), )

    
    FileCreationInformation = property(__FileCreationInformation.value, __FileCreationInformation.set, None, u'The information about the creation of the \n\t\t\t\t\texchange file. This is not about the creation of the data within \n\t\t\t\t\tthe file, but the creation of the file itself.')

    
    # Element {http://www.witsml.org/schemas/131}SecurityInformation uses Python identifier SecurityInformation
    __SecurityInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SecurityInformation'), 'SecurityInformation', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131SecurityInformation', True, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 63, 3), )

    
    SecurityInformation = property(__SecurityInformation.value, __SecurityInformation.set, None, u'Information about the security to be applied to \n\t\t\t\t\tthis file. More than one classification can be given.')

    
    # Element {http://www.witsml.org/schemas/131}Disclaimer uses Python identifier Disclaimer
    __Disclaimer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Disclaimer'), 'Disclaimer', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131Disclaimer', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 69, 3), )

    
    Disclaimer = property(__Disclaimer.value, __Disclaimer.set, None, u'A free-form string that allows a disclaimer to \n\t\t\t\t\taccompany the information.')

    
    # Element {http://www.witsml.org/schemas/131}AuditTrail uses Python identifier AuditTrail
    __AuditTrail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AuditTrail'), 'AuditTrail', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131AuditTrail', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 75, 3), )

    
    AuditTrail = property(__AuditTrail.value, __AuditTrail.set, None, u'A collection of events that can document the \n\t\t\t\t\thistory of the data.')

    
    # Element {http://www.witsml.org/schemas/131}Owner uses Python identifier Owner
    __Owner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Owner'), 'Owner', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131Owner', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 81, 3), )

    
    Owner = property(__Owner.value, __Owner.set, None, u'The owner of the data.')

    
    # Element {http://www.witsml.org/schemas/131}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Comment'), 'Comment', '__httpwww_witsml_orgschemas131_cs_documentInfo_httpwww_witsml_orgschemas131Comment', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 86, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, u'An optional comment about the document.')


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
Namespace.addCategoryObject('typeBinding', u'cs_documentInfo', cs_documentInfo)


# Complex type {http://www.witsml.org/schemas/131}fileCreationType with content type ELEMENT_ONLY
class fileCreationType (pyxb.binding.basis.complexTypeDefinition):
    """A block of information about the creation of the XML file. 
			This is different than the creation of the data that is included within the file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fileCreationType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 94, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}FileCreationDate uses Python identifier FileCreationDate
    __FileCreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileCreationDate'), 'FileCreationDate', '__httpwww_witsml_orgschemas131_fileCreationType_httpwww_witsml_orgschemas131FileCreationDate', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 100, 3), )

    
    FileCreationDate = property(__FileCreationDate.value, __FileCreationDate.set, None, u'The date and time that the file was created.')

    
    # Element {http://www.witsml.org/schemas/131}SoftwareName uses Python identifier SoftwareName
    __SoftwareName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SoftwareName'), 'SoftwareName', '__httpwww_witsml_orgschemas131_fileCreationType_httpwww_witsml_orgschemas131SoftwareName', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 105, 3), )

    
    SoftwareName = property(__SoftwareName.value, __SoftwareName.set, None, u'If appropriate, the software that created the file. \n\t\t\t\t\tThis is a free form string, and may include whatever information \n\t\t\t\t\tis deemed relevant.')

    
    # Element {http://www.witsml.org/schemas/131}FileCreator uses Python identifier FileCreator
    __FileCreator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileCreator'), 'FileCreator', '__httpwww_witsml_orgschemas131_fileCreationType_httpwww_witsml_orgschemas131FileCreator', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 112, 3), )

    
    FileCreator = property(__FileCreator.value, __FileCreator.set, None, u'The person or business associate that created \n\t\t\t\t\tthe file.')

    
    # Element {http://www.witsml.org/schemas/131}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Comment'), 'Comment', '__httpwww_witsml_orgschemas131_fileCreationType_httpwww_witsml_orgschemas131Comment', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 118, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, u'Any comment that would be useful to further \n\t\t\t\t\texplain the creation of this instance document.')


    _ElementMap = {
        __FileCreationDate.name() : __FileCreationDate,
        __SoftwareName.name() : __SoftwareName,
        __FileCreator.name() : __FileCreator,
        __Comment.name() : __Comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'fileCreationType', fileCreationType)


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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'securityInfoType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 127, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Class'), 'Class', '__httpwww_witsml_orgschemas131_securityInfoType_httpwww_witsml_orgschemas131Class', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 138, 3), )

    
    Class = property(__Class.value, __Class.set, None, u'The security class in which this document is \n\t\t\t\t\tclassified. Examples would be confidential, partner confidential, \n\t\t\t\t\ttight. The meaning of the class is determined by the System in which \n\t\t\t\t\tit is defined.')

    
    # Element {http://www.witsml.org/schemas/131}System uses Python identifier System
    __System = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'System'), 'System', '__httpwww_witsml_orgschemas131_securityInfoType_httpwww_witsml_orgschemas131System', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 146, 3), )

    
    System = property(__System.value, __System.set, None, u'The security classification system. \n\t\t\t\t\tThis gives context to the meaning of the Class value.')

    
    # Element {http://www.witsml.org/schemas/131}EndDate uses Python identifier EndDate
    __EndDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndDate'), 'EndDate', '__httpwww_witsml_orgschemas131_securityInfoType_httpwww_witsml_orgschemas131EndDate', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 152, 3), )

    
    EndDate = property(__EndDate.value, __EndDate.set, None, u'The date on which this security class is no \n\t\t\t\t\tlonger applicable.')

    
    # Element {http://www.witsml.org/schemas/131}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Comment'), 'Comment', '__httpwww_witsml_orgschemas131_securityInfoType_httpwww_witsml_orgschemas131Comment', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 158, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, u'A general comment to further define the security \n\t\t\t\t\tclass.')


    _ElementMap = {
        __Class.name() : __Class,
        __System.name() : __System,
        __EndDate.name() : __EndDate,
        __Comment.name() : __Comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'securityInfoType', securityInfoType)


# Complex type {http://www.witsml.org/schemas/131}auditType with content type ELEMENT_ONLY
class auditType (pyxb.binding.basis.complexTypeDefinition):
    """The audit records what happened to the data, to produce 
			the data that is in this file. It consists of one or more events."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'auditType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 167, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}Event uses Python identifier Event
    __Event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Event'), 'Event', '__httpwww_witsml_orgschemas131_auditType_httpwww_witsml_orgschemas131Event', True, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 173, 3), )

    
    Event = property(__Event.value, __Event.set, None, None)


    _ElementMap = {
        __Event.name() : __Event
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'auditType', auditType)


# Complex type {http://www.witsml.org/schemas/131}eventType with content type ELEMENT_ONLY
class eventType (pyxb.binding.basis.complexTypeDefinition):
    """An event type captures the basic information about an 
			event that has affected the data."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'eventType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 177, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}EventDate uses Python identifier EventDate
    __EventDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EventDate'), 'EventDate', '__httpwww_witsml_orgschemas131_eventType_httpwww_witsml_orgschemas131EventDate', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 183, 3), )

    
    EventDate = property(__EventDate.value, __EventDate.set, None, u'The date on which the event took place.')

    
    # Element {http://www.witsml.org/schemas/131}ResponsibleParty uses Python identifier ResponsibleParty
    __ResponsibleParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ResponsibleParty'), 'ResponsibleParty', '__httpwww_witsml_orgschemas131_eventType_httpwww_witsml_orgschemas131ResponsibleParty', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 188, 3), )

    
    ResponsibleParty = property(__ResponsibleParty.value, __ResponsibleParty.set, None, u'The party responsible for the event.')

    
    # Element {http://www.witsml.org/schemas/131}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Comment'), 'Comment', '__httpwww_witsml_orgschemas131_eventType_httpwww_witsml_orgschemas131Comment', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 193, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, u'A free form comment that can further \n\t\t\t\t\tdefine the event that occurred.')


    _ElementMap = {
        __EventDate.name() : __EventDate,
        __ResponsibleParty.name() : __ResponsibleParty,
        __Comment.name() : __Comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'eventType', eventType)


# Complex type {http://www.witsml.org/schemas/131}cs_refWellboreTrajectory with content type ELEMENT_ONLY
class cs_refWellboreTrajectory (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a trajectory in a wellbore.
			The trajectory may be defined within the context of another wellbore.
			This value represents a foreign key from one element to another."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_refWellboreTrajectory')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectory.xsd', 19, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}trajectoryReference uses Python identifier trajectoryReference
    __trajectoryReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'trajectoryReference'), 'trajectoryReference', '__httpwww_witsml_orgschemas131_cs_refWellboreTrajectory_httpwww_witsml_orgschemas131trajectoryReference', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectory.xsd', 26, 3), )

    
    trajectoryReference = property(__trajectoryReference.value, __trajectoryReference.set, None, u'A pointer to the trajectory within the wellbore.')

    
    # Element {http://www.witsml.org/schemas/131}wellboreParent uses Python identifier wellboreParent
    __wellboreParent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'wellboreParent'), 'wellboreParent', '__httpwww_witsml_orgschemas131_cs_refWellboreTrajectory_httpwww_witsml_orgschemas131wellboreParent', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectory.xsd', 31, 3), )

    
    wellboreParent = property(__wellboreParent.value, __wellboreParent.set, None, u'A pointer to the wellbore that contains the trajectoryReference.\n\t\t\t\t\tThis is not needed unless the trajectory is outside the \n\t\t\t\t\tcontext of a common parent wellbore.')


    _ElementMap = {
        __trajectoryReference.name() : __trajectoryReference,
        __wellboreParent.name() : __wellboreParent
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_refWellboreTrajectory', cs_refWellboreTrajectory)


# Complex type {http://www.witsml.org/schemas/131}cs_refWellboreTrajectoryStation with content type ELEMENT_ONLY
class cs_refWellboreTrajectoryStation (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a trajectoryStation in a wellbore.
			The trajectoryStation may be defined within the context of another wellbore.
			This value represents a foreign key from one element to another."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_refWellboreTrajectoryStation')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 19, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}stationReference uses Python identifier stationReference
    __stationReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'stationReference'), 'stationReference', '__httpwww_witsml_orgschemas131_cs_refWellboreTrajectoryStation_httpwww_witsml_orgschemas131stationReference', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 26, 3), )

    
    stationReference = property(__stationReference.value, __stationReference.set, None, u'A pointer to the trajectoryStation within the parent trajectory.\n\t\t\t\t\tThis is a special case where we only use a uid for the pointer.\n\t\t\t\t\tThe natural identity of a station is its physical characteristics (e.g., md).')

    
    # Element {http://www.witsml.org/schemas/131}trajectoryParent uses Python identifier trajectoryParent
    __trajectoryParent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'trajectoryParent'), 'trajectoryParent', '__httpwww_witsml_orgschemas131_cs_refWellboreTrajectoryStation_httpwww_witsml_orgschemas131trajectoryParent', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 33, 3), )

    
    trajectoryParent = property(__trajectoryParent.value, __trajectoryParent.set, None, u'A pointer to the trajectory within the parent wellbore.\n\t\t\t\t\tThis trajectory contains the trajectoryStation.')

    
    # Element {http://www.witsml.org/schemas/131}wellboreParent uses Python identifier wellboreParent
    __wellboreParent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'wellboreParent'), 'wellboreParent', '__httpwww_witsml_orgschemas131_cs_refWellboreTrajectoryStation_httpwww_witsml_orgschemas131wellboreParent', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 39, 3), )

    
    wellboreParent = property(__wellboreParent.value, __wellboreParent.set, None, u'A pointer to the wellbore that contains the trajectory.\n\t\t\t\t\tThis is not needed unless the trajectory is outside the \n\t\t\t\t\tcontext of a common parent wellbore.')


    _ElementMap = {
        __stationReference.name() : __stationReference,
        __trajectoryParent.name() : __trajectoryParent,
        __wellboreParent.name() : __wellboreParent
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_refWellboreTrajectoryStation', cs_refWellboreTrajectoryStation)


# Complex type {http://www.witsml.org/schemas/131}cs_stnTrajCorUsed with content type ELEMENT_ONLY
class cs_stnTrajCorUsed (pyxb.binding.basis.complexTypeDefinition):
    """WITSML Trajectory Station Corrections Applied"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_stnTrajCorUsed')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}gravAxialAccelCor uses Python identifier gravAxialAccelCor
    __gravAxialAccelCor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gravAxialAccelCor'), 'gravAxialAccelCor', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131gravAxialAccelCor', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 23, 3), )

    
    gravAxialAccelCor = property(__gravAxialAccelCor.value, __gravAxialAccelCor.set, None, u'Calculated gravitational field strength correction.  ')

    
    # Element {http://www.witsml.org/schemas/131}gravTran1AccelCor uses Python identifier gravTran1AccelCor
    __gravTran1AccelCor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gravTran1AccelCor'), 'gravTran1AccelCor', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131gravTran1AccelCor', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 28, 3), )

    
    gravTran1AccelCor = property(__gravTran1AccelCor.value, __gravTran1AccelCor.set, None, u'The correction applied to the X cross-axial component of the earths magnetic field.\n\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/131}gravTran2AccelCor uses Python identifier gravTran2AccelCor
    __gravTran2AccelCor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gravTran2AccelCor'), 'gravTran2AccelCor', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131gravTran2AccelCor', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 34, 3), )

    
    gravTran2AccelCor = property(__gravTran2AccelCor.value, __gravTran2AccelCor.set, None, u'The correction applied to the Y cross-axial component of the earths magnetic field.\n\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/131}magAxialDrlstrCor uses Python identifier magAxialDrlstrCor
    __magAxialDrlstrCor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magAxialDrlstrCor'), 'magAxialDrlstrCor', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131magAxialDrlstrCor', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 40, 3), )

    
    magAxialDrlstrCor = property(__magAxialDrlstrCor.value, __magAxialDrlstrCor.set, None, u'Axial magnetic drillstring correction.  ')

    
    # Element {http://www.witsml.org/schemas/131}magTran1DrlstrCor uses Python identifier magTran1DrlstrCor
    __magTran1DrlstrCor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magTran1DrlstrCor'), 'magTran1DrlstrCor', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131magTran1DrlstrCor', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 45, 3), )

    
    magTran1DrlstrCor = property(__magTran1DrlstrCor.value, __magTran1DrlstrCor.set, None, u'Cross-axial magnetic correction.  ')

    
    # Element {http://www.witsml.org/schemas/131}magTran2DrlstrCor uses Python identifier magTran2DrlstrCor
    __magTran2DrlstrCor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magTran2DrlstrCor'), 'magTran2DrlstrCor', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131magTran2DrlstrCor', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 50, 3), )

    
    magTran2DrlstrCor = property(__magTran2DrlstrCor.value, __magTran2DrlstrCor.set, None, u'Cross-axial magnetic correction.  ')

    
    # Element {http://www.witsml.org/schemas/131}sagIncCor uses Python identifier sagIncCor
    __sagIncCor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sagIncCor'), 'sagIncCor', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131sagIncCor', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 55, 3), )

    
    sagIncCor = property(__sagIncCor.value, __sagIncCor.set, None, u'Calculated sag correction to inclination.  ')

    
    # Element {http://www.witsml.org/schemas/131}sagAziCor uses Python identifier sagAziCor
    __sagAziCor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sagAziCor'), 'sagAziCor', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131sagAziCor', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 60, 3), )

    
    sagAziCor = property(__sagAziCor.value, __sagAziCor.set, None, u'Calculated sag correction to azimuth.  ')

    
    # Element {http://www.witsml.org/schemas/131}stnMagDeclUsed uses Python identifier stnMagDeclUsed
    __stnMagDeclUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'stnMagDeclUsed'), 'stnMagDeclUsed', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131stnMagDeclUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 65, 3), )

    
    stnMagDeclUsed = property(__stnMagDeclUsed.value, __stnMagDeclUsed.set, None, u'Magnetic declination used to correct a magnetic survey station.  ')

    
    # Element {http://www.witsml.org/schemas/131}stnGridCorUsed uses Python identifier stnGridCorUsed
    __stnGridCorUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'stnGridCorUsed'), 'stnGridCorUsed', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131stnGridCorUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 70, 3), )

    
    stnGridCorUsed = property(__stnGridCorUsed.value, __stnGridCorUsed.set, None, u'Grid Correction (Meridian convergence). The angle between \n\t\t\t\t\tTrue North and Grid North. Grid Correction is positive when True North \n\t\t\t\t\tis west of Grid North. The correction is added to the raw observation, \n\t\t\t\t\tthus yielding a reduced or corrected observation that can go into \n\t\t\t\t\tthe subsequent calculations.')

    
    # Element {http://www.witsml.org/schemas/131}dirSensorOffset uses Python identifier dirSensorOffset
    __dirSensorOffset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dirSensorOffset'), 'dirSensorOffset', '__httpwww_witsml_orgschemas131_cs_stnTrajCorUsed_httpwww_witsml_orgschemas131dirSensorOffset', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 79, 3), )

    
    dirSensorOffset = property(__dirSensorOffset.value, __dirSensorOffset.set, None, u'Offset relative to bit.  ')


    _ElementMap = {
        __gravAxialAccelCor.name() : __gravAxialAccelCor,
        __gravTran1AccelCor.name() : __gravTran1AccelCor,
        __gravTran2AccelCor.name() : __gravTran2AccelCor,
        __magAxialDrlstrCor.name() : __magAxialDrlstrCor,
        __magTran1DrlstrCor.name() : __magTran1DrlstrCor,
        __magTran2DrlstrCor.name() : __magTran2DrlstrCor,
        __sagIncCor.name() : __sagIncCor,
        __sagAziCor.name() : __sagAziCor,
        __stnMagDeclUsed.name() : __stnMagDeclUsed,
        __stnGridCorUsed.name() : __stnGridCorUsed,
        __dirSensorOffset.name() : __dirSensorOffset
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_stnTrajCorUsed', cs_stnTrajCorUsed)


# Complex type {http://www.witsml.org/schemas/131}cs_stnTrajMatrixCov with content type ELEMENT_ONLY
class cs_stnTrajMatrixCov (pyxb.binding.basis.complexTypeDefinition):
    """WITSML Validation Information for Covariance Matrix"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_stnTrajMatrixCov')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}varianceNN uses Python identifier varianceNN
    __varianceNN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'varianceNN'), 'varianceNN', '__httpwww_witsml_orgschemas131_cs_stnTrajMatrixCov_httpwww_witsml_orgschemas131varianceNN', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 23, 3), )

    
    varianceNN = property(__varianceNN.value, __varianceNN.set, None, u'Covariance north north.  ')

    
    # Element {http://www.witsml.org/schemas/131}varianceNE uses Python identifier varianceNE
    __varianceNE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'varianceNE'), 'varianceNE', '__httpwww_witsml_orgschemas131_cs_stnTrajMatrixCov_httpwww_witsml_orgschemas131varianceNE', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 28, 3), )

    
    varianceNE = property(__varianceNE.value, __varianceNE.set, None, u'Crossvariance north east.  ')

    
    # Element {http://www.witsml.org/schemas/131}varianceNVert uses Python identifier varianceNVert
    __varianceNVert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'varianceNVert'), 'varianceNVert', '__httpwww_witsml_orgschemas131_cs_stnTrajMatrixCov_httpwww_witsml_orgschemas131varianceNVert', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 33, 3), )

    
    varianceNVert = property(__varianceNVert.value, __varianceNVert.set, None, u'Crossvariance north vertical.  ')

    
    # Element {http://www.witsml.org/schemas/131}varianceEE uses Python identifier varianceEE
    __varianceEE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'varianceEE'), 'varianceEE', '__httpwww_witsml_orgschemas131_cs_stnTrajMatrixCov_httpwww_witsml_orgschemas131varianceEE', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 38, 3), )

    
    varianceEE = property(__varianceEE.value, __varianceEE.set, None, u'Covariance east east.  ')

    
    # Element {http://www.witsml.org/schemas/131}varianceEVert uses Python identifier varianceEVert
    __varianceEVert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'varianceEVert'), 'varianceEVert', '__httpwww_witsml_orgschemas131_cs_stnTrajMatrixCov_httpwww_witsml_orgschemas131varianceEVert', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 43, 3), )

    
    varianceEVert = property(__varianceEVert.value, __varianceEVert.set, None, u'Crossvariance east vertical.  ')

    
    # Element {http://www.witsml.org/schemas/131}varianceVertVert uses Python identifier varianceVertVert
    __varianceVertVert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'varianceVertVert'), 'varianceVertVert', '__httpwww_witsml_orgschemas131_cs_stnTrajMatrixCov_httpwww_witsml_orgschemas131varianceVertVert', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 48, 3), )

    
    varianceVertVert = property(__varianceVertVert.value, __varianceVertVert.set, None, u'Covariance vertical vertical.  ')

    
    # Element {http://www.witsml.org/schemas/131}biasN uses Python identifier biasN
    __biasN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'biasN'), 'biasN', '__httpwww_witsml_orgschemas131_cs_stnTrajMatrixCov_httpwww_witsml_orgschemas131biasN', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 53, 3), )

    
    biasN = property(__biasN.value, __biasN.set, None, u'Bias north.  ')

    
    # Element {http://www.witsml.org/schemas/131}biasE uses Python identifier biasE
    __biasE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'biasE'), 'biasE', '__httpwww_witsml_orgschemas131_cs_stnTrajMatrixCov_httpwww_witsml_orgschemas131biasE', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 58, 3), )

    
    biasE = property(__biasE.value, __biasE.set, None, u'Bias east.  ')

    
    # Element {http://www.witsml.org/schemas/131}biasVert uses Python identifier biasVert
    __biasVert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'biasVert'), 'biasVert', '__httpwww_witsml_orgschemas131_cs_stnTrajMatrixCov_httpwww_witsml_orgschemas131biasVert', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 63, 3), )

    
    biasVert = property(__biasVert.value, __biasVert.set, None, u'Bias vertical.  ')


    _ElementMap = {
        __varianceNN.name() : __varianceNN,
        __varianceNE.name() : __varianceNE,
        __varianceNVert.name() : __varianceNVert,
        __varianceEE.name() : __varianceEE,
        __varianceEVert.name() : __varianceEVert,
        __varianceVertVert.name() : __varianceVertVert,
        __biasN.name() : __biasN,
        __biasE.name() : __biasE,
        __biasVert.name() : __biasVert
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_stnTrajMatrixCov', cs_stnTrajMatrixCov)


# Complex type {http://www.witsml.org/schemas/131}cs_stnTrajRawData with content type ELEMENT_ONLY
class cs_stnTrajRawData (pyxb.binding.basis.complexTypeDefinition):
    """WITSML Trajectory Station Raw Data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_stnTrajRawData')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}gravAxialRaw uses Python identifier gravAxialRaw
    __gravAxialRaw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gravAxialRaw'), 'gravAxialRaw', '__httpwww_witsml_orgschemas131_cs_stnTrajRawData_httpwww_witsml_orgschemas131gravAxialRaw', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 23, 3), )

    
    gravAxialRaw = property(__gravAxialRaw.value, __gravAxialRaw.set, None, u'Uncorrected gravitational field strength measured in axial direction.  ')

    
    # Element {http://www.witsml.org/schemas/131}gravTran1Raw uses Python identifier gravTran1Raw
    __gravTran1Raw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gravTran1Raw'), 'gravTran1Raw', '__httpwww_witsml_orgschemas131_cs_stnTrajRawData_httpwww_witsml_orgschemas131gravTran1Raw', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 28, 3), )

    
    gravTran1Raw = property(__gravTran1Raw.value, __gravTran1Raw.set, None, u'Uncorrected gravitational field strength measured in transverse direction.\n\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/131}gravTran2Raw uses Python identifier gravTran2Raw
    __gravTran2Raw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gravTran2Raw'), 'gravTran2Raw', '__httpwww_witsml_orgschemas131_cs_stnTrajRawData_httpwww_witsml_orgschemas131gravTran2Raw', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 34, 3), )

    
    gravTran2Raw = property(__gravTran2Raw.value, __gravTran2Raw.set, None, u'Uncorrected gravitational field strength measured in transverse direction, \n\t\t\t\tapproximately normal to tran1.  ')

    
    # Element {http://www.witsml.org/schemas/131}magAxialRaw uses Python identifier magAxialRaw
    __magAxialRaw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magAxialRaw'), 'magAxialRaw', '__httpwww_witsml_orgschemas131_cs_stnTrajRawData_httpwww_witsml_orgschemas131magAxialRaw', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 40, 3), )

    
    magAxialRaw = property(__magAxialRaw.value, __magAxialRaw.set, None, u'Uncorrected magnetic field strength measured in axial direction.  ')

    
    # Element {http://www.witsml.org/schemas/131}magTran1Raw uses Python identifier magTran1Raw
    __magTran1Raw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magTran1Raw'), 'magTran1Raw', '__httpwww_witsml_orgschemas131_cs_stnTrajRawData_httpwww_witsml_orgschemas131magTran1Raw', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 45, 3), )

    
    magTran1Raw = property(__magTran1Raw.value, __magTran1Raw.set, None, u'Uncorrected magnetic field strength measured in transverse direction.  ')

    
    # Element {http://www.witsml.org/schemas/131}magTran2Raw uses Python identifier magTran2Raw
    __magTran2Raw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magTran2Raw'), 'magTran2Raw', '__httpwww_witsml_orgschemas131_cs_stnTrajRawData_httpwww_witsml_orgschemas131magTran2Raw', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 50, 3), )

    
    magTran2Raw = property(__magTran2Raw.value, __magTran2Raw.set, None, u'Uncorrected magnetic field strength measured in transverse direction, \n\t\t\t\t\tapproximately normal to tran1.  ')


    _ElementMap = {
        __gravAxialRaw.name() : __gravAxialRaw,
        __gravTran1Raw.name() : __gravTran1Raw,
        __gravTran2Raw.name() : __gravTran2Raw,
        __magAxialRaw.name() : __magAxialRaw,
        __magTran1Raw.name() : __magTran1Raw,
        __magTran2Raw.name() : __magTran2Raw
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_stnTrajRawData', cs_stnTrajRawData)


# Complex type {http://www.witsml.org/schemas/131}cs_stnTrajValid with content type ELEMENT_ONLY
class cs_stnTrajValid (pyxb.binding.basis.complexTypeDefinition):
    """WITSML Validation Information for Survey"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_stnTrajValid')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}magTotalFieldCalc uses Python identifier magTotalFieldCalc
    __magTotalFieldCalc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magTotalFieldCalc'), 'magTotalFieldCalc', '__httpwww_witsml_orgschemas131_cs_stnTrajValid_httpwww_witsml_orgschemas131magTotalFieldCalc', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 23, 3), )

    
    magTotalFieldCalc = property(__magTotalFieldCalc.value, __magTotalFieldCalc.set, None, u'Calculated total intensity of the geomagnetic field as sum of BGGM, \n\t\t\t\t\tIFR and local field. ')

    
    # Element {http://www.witsml.org/schemas/131}magDipAngleCalc uses Python identifier magDipAngleCalc
    __magDipAngleCalc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magDipAngleCalc'), 'magDipAngleCalc', '__httpwww_witsml_orgschemas131_cs_stnTrajValid_httpwww_witsml_orgschemas131magDipAngleCalc', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 29, 3), )

    
    magDipAngleCalc = property(__magDipAngleCalc.value, __magDipAngleCalc.set, None, u'Calculated magnetic dip (inclination), the angle between the horizontal \n\t\t\t\t\tand the geomagnetic field (positive down, res .001).  ')

    
    # Element {http://www.witsml.org/schemas/131}gravTotalFieldCalc uses Python identifier gravTotalFieldCalc
    __gravTotalFieldCalc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gravTotalFieldCalc'), 'gravTotalFieldCalc', '__httpwww_witsml_orgschemas131_cs_stnTrajValid_httpwww_witsml_orgschemas131gravTotalFieldCalc', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 35, 3), )

    
    gravTotalFieldCalc = property(__gravTotalFieldCalc.value, __gravTotalFieldCalc.set, None, u'Calculated total gravitational field.  ')


    _ElementMap = {
        __magTotalFieldCalc.name() : __magTotalFieldCalc,
        __magDipAngleCalc.name() : __magDipAngleCalc,
        __gravTotalFieldCalc.name() : __gravTotalFieldCalc
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_stnTrajValid', cs_stnTrajValid)


# Complex type {http://www.witsml.org/schemas/131}abstractMeasure with content type SIMPLE
class abstractMeasure (pyxb.binding.basis.complexTypeDefinition):
    """The intended abstract supertype of all quantities that have a value 
			with a unit of measure. The unit of measure is in the uom attribute of the subtypes. 
			This type allows all quantities to be profiled to be a 'float' instead of a 'double'."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_baseType.xsd', 118, 1)
    # Base type is abstractDouble

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'abstractMeasure', abstractMeasure)


# Complex type {http://www.witsml.org/schemas/131}obj_trajectorys with content type ELEMENT_ONLY
class obj_trajectorys (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/schemas/131}obj_trajectorys with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'obj_trajectorys')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 34, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}documentInfo uses Python identifier documentInfo
    __documentInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'documentInfo'), 'documentInfo', '__httpwww_witsml_orgschemas131_obj_trajectorys_httpwww_witsml_orgschemas131documentInfo', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 36, 3), )

    
    documentInfo = property(__documentInfo.value, __documentInfo.set, None, u'Information about the XML message instance.  ')

    
    # Element {http://www.witsml.org/schemas/131}trajectory uses Python identifier trajectory
    __trajectory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'trajectory'), 'trajectory', '__httpwww_witsml_orgschemas131_obj_trajectorys_httpwww_witsml_orgschemas131trajectory', True, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 41, 3), )

    
    trajectory = property(__trajectory.value, __trajectory.set, None, u'A single trajectory.  ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_witsml_orgschemas131_obj_trajectorys_version', schemaVersionString, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 47, 2)
    __version._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 47, 2)
    
    version = property(__version.value, __version.set, None, u'Data object schema version.  The fourth level must match the \n\t\t\t\tversion of the schema constraints (enumerations and XML loader files) that are assumed\n\t\t\t\tby the document instance.')


    _ElementMap = {
        __documentInfo.name() : __documentInfo,
        __trajectory.name() : __trajectory
    }
    _AttributeMap = {
        __version.name() : __version
    }
Namespace.addCategoryObject('typeBinding', u'obj_trajectorys', obj_trajectorys)


# Complex type {http://www.witsml.org/schemas/131}indexCurve with content type SIMPLE
class indexCurve (pyxb.binding.basis.complexTypeDefinition):
    """The mnemonic of a log index curve plus 
			the column index of the curve."""
    _TypeDefinition = str32
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'indexCurve')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 171, 1)
    # Base type is str32
    
    # Attribute columnIndex uses Python identifier columnIndex
    __columnIndex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'columnIndex'), 'columnIndex', '__httpwww_witsml_orgschemas131_indexCurve_columnIndex', nonNegativeCount, required=True)
    __columnIndex._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 178, 4)
    __columnIndex._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 178, 4)
    
    columnIndex = property(__columnIndex.value, __columnIndex.set, None, u'The column index of the curve.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __columnIndex.name() : __columnIndex
    }
Namespace.addCategoryObject('typeBinding', u'indexCurve', indexCurve)


# Complex type {http://www.witsml.org/schemas/131}cs_location with content type ELEMENT_ONLY
class cs_location (pyxb.binding.basis.complexTypeDefinition):
    """WITSML Location Component Schema
			This is a location that is expressed in terms of 2D coordinates. 
			In order that the location be understood, the coordinate reference system (CRS) 
			must be known."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_location')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 19, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}wellCRS uses Python identifier wellCRS
    __wellCRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'wellCRS'), 'wellCRS', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131wellCRS', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 27, 3), )

    
    wellCRS = property(__wellCRS.value, __wellCRS.set, None, u'A pointer to the wellCRS that defines the CRS for the coordinates. \n\t\t\t\t\tWhile optional, it is strongly recommended that this be specified.')

    
    # Element {http://www.witsml.org/schemas/131}latitude uses Python identifier latitude
    __latitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'latitude'), 'latitude', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131latitude', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 45, 5), )

    
    latitude = property(__latitude.value, __latitude.set, None, u'The latitude with north being positive.')

    
    # Element {http://www.witsml.org/schemas/131}longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'longitude'), 'longitude', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131longitude', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 50, 5), )

    
    longitude = property(__longitude.value, __longitude.set, None, u'The longitude with east being positive.')

    
    # Element {http://www.witsml.org/schemas/131}easting uses Python identifier easting
    __easting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'easting'), 'easting', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131easting', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 57, 5), )

    
    easting = property(__easting.value, __easting.set, None, u'The projected coordinate with east being positive. \n\t\t\t\t\t\t\tThis is the most common type of projected coordinates. \n\t\t\t\t\t\t\tUTM coordinates are expressed in Easting and Northing.')

    
    # Element {http://www.witsml.org/schemas/131}northing uses Python identifier northing
    __northing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'northing'), 'northing', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131northing', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 64, 5), )

    
    northing = property(__northing.value, __northing.set, None, u'The projected coordinate with north being positive. \n\t\t\t\t\t\t\tThis is the most common type of projected coordinates. \n\t\t\t\t\t\t\tUTM coordinates are expressed in Easting and Northing.')

    
    # Element {http://www.witsml.org/schemas/131}westing uses Python identifier westing
    __westing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'westing'), 'westing', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131westing', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 73, 5), )

    
    westing = property(__westing.value, __westing.set, None, u'The projected coordinate with west being positive. \n\t\t\t\t\t\t\tThe positive directions are reversed from the usual Easting and Northing values. \n\t\t\t\t\t\t\tThese values are generally located in the southern hemisphere, \n\t\t\t\t\t\t\tmost notably in South Africa and Australia.')

    
    # Element {http://www.witsml.org/schemas/131}southing uses Python identifier southing
    __southing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'southing'), 'southing', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131southing', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 81, 5), )

    
    southing = property(__southing.value, __southing.set, None, u'The projected coordinate with south being positive. \n\t\t\t\t\t\t\tThe positive directions are reversed from the usual Easting and Northing values. \n\t\t\t\t\t\t\tThese values are generally located in the southern hemisphere, \n\t\t\t\t\t\t\tmost notably in South Africa and Australia.')

    
    # Element {http://www.witsml.org/schemas/131}projectedX uses Python identifier projectedX
    __projectedX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'projectedX'), 'projectedX', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131projectedX', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 91, 5), )

    
    projectedX = property(__projectedX.value, __projectedX.set, None, u'The projected X coordinate with the positive direction unknown.\n\t\t\t\t\t\t\tProjectedX and ProjectedY are used when it is not \n\t\t\t\t\t\t\tknown what the meaning of the coordinates is. If the meaning is known, \n\t\t\t\t\t\t\tthe Easting/Northing or Westing/Southing should be used. Use of this pair \n\t\t\t\t\t\t\timplies a lack of knowledge on the part of the sender.')

    
    # Element {http://www.witsml.org/schemas/131}projectedY uses Python identifier projectedY
    __projectedY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'projectedY'), 'projectedY', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131projectedY', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 100, 5), )

    
    projectedY = property(__projectedY.value, __projectedY.set, None, u'The projected Y coordinate with the positive direction unknown.\n\t\t\t\t\t\t\tProjectedX and ProjectedY are used when it is not \n\t\t\t\t\t\t\tknown what the meaning of the coordinates is. If the meaning is known, \n\t\t\t\t\t\t\tthe Easting/Northing or Westing/Southing should be used. Use of this pair \n\t\t\t\t\t\t\timplies a lack of knowledge on the part of the sender.')

    
    # Element {http://www.witsml.org/schemas/131}localX uses Python identifier localX
    __localX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'localX'), 'localX', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131localX', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 111, 5), )

    
    localX = property(__localX.value, __localX.set, None, u'The local (engineering) X coordinate. \n\t\t\t\t\t\t\tThe CRS will define the orientation of the axis.')

    
    # Element {http://www.witsml.org/schemas/131}localY uses Python identifier localY
    __localY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'localY'), 'localY', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131localY', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 117, 5), )

    
    localY = property(__localY.value, __localY.set, None, u'The local (engineering) Y coordinate. \n\t\t\t\t\t\t\tThe CRS will define the orientation of the axis.')

    
    # Element {http://www.witsml.org/schemas/131}original uses Python identifier original
    __original = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'original'), 'original', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131original', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 125, 3), )

    
    original = property(__original.value, __original.set, None, u'Flag indicating (if "true" or "1") that this pair of values was \n\t\t\t\t\tthe original data given for the location. If the pair of values was \n\t\t\t\t\tcalculated from an original pair of values, this flag should be "false" (or "0"), \n\t\t\t\t\tor not present.')

    
    # Element {http://www.witsml.org/schemas/131}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpwww_witsml_orgschemas131_cs_location_httpwww_witsml_orgschemas131description', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 133, 3), )

    
    description = property(__description.value, __description.set, None, u'A Comment, generally given to help the reader \n\t\t\t\t\tinterpret the coordinates if the CRS and the chosen pair do not make them clear.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uid'), 'uid', '__httpwww_witsml_orgschemas131_cs_location_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\attgrp_uid.xsd', 20, 2)
    __uid._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\attgrp_uid.xsd', 20, 2)
    
    uid = property(__uid.value, __uid.set, None, u'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


    _ElementMap = {
        __wellCRS.name() : __wellCRS,
        __latitude.name() : __latitude,
        __longitude.name() : __longitude,
        __easting.name() : __easting,
        __northing.name() : __northing,
        __westing.name() : __westing,
        __southing.name() : __southing,
        __projectedX.name() : __projectedX,
        __projectedY.name() : __projectedY,
        __localX.name() : __localX,
        __localY.name() : __localY,
        __original.name() : __original,
        __description.name() : __description
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', u'cs_location', cs_location)


# Complex type {http://www.witsml.org/schemas/131}cs_trajectoryStation with content type ELEMENT_ONLY
class cs_trajectoryStation (pyxb.binding.basis.complexTypeDefinition):
    """WITSML - Trajectory Station Component Schema"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_trajectoryStation')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_trajectoryStation.xsd', 20, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}commonData uses Python identifier commonData
    __commonData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'commonData'), 'commonData', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131commonData', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_trajectoryStation.xsd', 30, 3), )

    
    commonData = property(__commonData.value, __commonData.set, None, u'A container element that contains elements that are common to all data \n\t\t\t\t\tobjects.  ')

    
    # Element {http://www.witsml.org/schemas/131}target uses Python identifier target
    __target = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'target'), 'target', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131target', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 28, 3), )

    
    target = property(__target.value, __target.set, None, u'A pointer to the intended target of this station.  ')

    
    # Element {http://www.witsml.org/schemas/131}dTimStn uses Python identifier dTimStn
    __dTimStn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dTimStn'), 'dTimStn', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131dTimStn', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 33, 3), )

    
    dTimStn = property(__dTimStn.value, __dTimStn.set, None, u'Date and time the station was measured or created.  ')

    
    # Element {http://www.witsml.org/schemas/131}typeTrajStation uses Python identifier typeTrajStation
    __typeTrajStation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'typeTrajStation'), 'typeTrajStation', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131typeTrajStation', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 38, 3), )

    
    typeTrajStation = property(__typeTrajStation.value, __typeTrajStation.set, None, u'Type of survey station.  ')

    
    # Element {http://www.witsml.org/schemas/131}typeSurveyTool uses Python identifier typeSurveyTool
    __typeSurveyTool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'typeSurveyTool'), 'typeSurveyTool', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131typeSurveyTool', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 43, 3), )

    
    typeSurveyTool = property(__typeSurveyTool.value, __typeSurveyTool.set, None, u'The type of tool used for the measurements.')

    
    # Element {http://www.witsml.org/schemas/131}md uses Python identifier md
    __md = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'md'), 'md', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131md', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 48, 3), )

    
    md = property(__md.value, __md.set, None, u'Measured depth of measurement from the drill datum.  ')

    
    # Element {http://www.witsml.org/schemas/131}tvd uses Python identifier tvd
    __tvd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tvd'), 'tvd', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131tvd', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 53, 3), )

    
    tvd = property(__tvd.value, __tvd.set, None, u'Vertical depth of the measurements.  ')

    
    # Element {http://www.witsml.org/schemas/131}incl uses Python identifier incl
    __incl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'incl'), 'incl', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131incl', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 58, 3), )

    
    incl = property(__incl.value, __incl.set, None, u'Hole inclination, measured from vertical.  ')

    
    # Element {http://www.witsml.org/schemas/131}azi uses Python identifier azi
    __azi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'azi'), 'azi', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131azi', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 63, 3), )

    
    azi = property(__azi.value, __azi.set, None, u'Hole azimuth. Corrected to wells azimuth reference.  ')

    
    # Element {http://www.witsml.org/schemas/131}mtf uses Python identifier mtf
    __mtf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mtf'), 'mtf', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131mtf', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 68, 3), )

    
    mtf = property(__mtf.value, __mtf.set, None, u'Toolface angle (magnetic).  ')

    
    # Element {http://www.witsml.org/schemas/131}gtf uses Python identifier gtf
    __gtf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gtf'), 'gtf', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131gtf', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 73, 3), )

    
    gtf = property(__gtf.value, __gtf.set, None, u'Toolface angle (gravity).  ')

    
    # Element {http://www.witsml.org/schemas/131}dispNs uses Python identifier dispNs
    __dispNs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dispNs'), 'dispNs', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131dispNs', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 78, 3), )

    
    dispNs = property(__dispNs.value, __dispNs.set, None, u'North-south offset, positive to the North. \n\t\t\t\t\tThis is relative to wellLocation with a North axis orientation of aziRef.\n\t\t\t\t\tIf a displacement with respect to a different point is desired then\n\t\t\t\t\tdefine a localCRS and specify local coordinates in location.')

    
    # Element {http://www.witsml.org/schemas/131}dispEw uses Python identifier dispEw
    __dispEw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dispEw'), 'dispEw', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131dispEw', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 86, 3), )

    
    dispEw = property(__dispEw.value, __dispEw.set, None, u'East-west offset, positive to the East.\n\t\t\t\t\tThis is relative to wellLocation with a North axis orientation of aziRef. \n\t\t\t\t\tIf a displacement with respect to a different point is desired then\n\t\t\t\t\tdefine a localCRS and specify local coordinates in location. ')

    
    # Element {http://www.witsml.org/schemas/131}vertSect uses Python identifier vertSect
    __vertSect = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'vertSect'), 'vertSect', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131vertSect', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 94, 3), )

    
    vertSect = property(__vertSect.value, __vertSect.set, None, u'Distance along vertical section azimuth plane.  ')

    
    # Element {http://www.witsml.org/schemas/131}dls uses Python identifier dls
    __dls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dls'), 'dls', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131dls', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 99, 3), )

    
    dls = property(__dls.value, __dls.set, None, u'Dogleg severity.  ')

    
    # Element {http://www.witsml.org/schemas/131}rateTurn uses Python identifier rateTurn
    __rateTurn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'rateTurn'), 'rateTurn', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131rateTurn', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 104, 3), )

    
    rateTurn = property(__rateTurn.value, __rateTurn.set, None, u'Turn rate, radius of curvature computation.  ')

    
    # Element {http://www.witsml.org/schemas/131}rateBuild uses Python identifier rateBuild
    __rateBuild = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'rateBuild'), 'rateBuild', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131rateBuild', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 109, 3), )

    
    rateBuild = property(__rateBuild.value, __rateBuild.set, None, u'Build Rate, radius of curvature computation.  ')

    
    # Element {http://www.witsml.org/schemas/131}mdDelta uses Python identifier mdDelta
    __mdDelta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mdDelta'), 'mdDelta', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131mdDelta', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 114, 3), )

    
    mdDelta = property(__mdDelta.value, __mdDelta.set, None, u'Delta measured depth from previous station.  ')

    
    # Element {http://www.witsml.org/schemas/131}tvdDelta uses Python identifier tvdDelta
    __tvdDelta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tvdDelta'), 'tvdDelta', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131tvdDelta', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 119, 3), )

    
    tvdDelta = property(__tvdDelta.value, __tvdDelta.set, None, u'Delta true vertical depth from previous station.  ')

    
    # Element {http://www.witsml.org/schemas/131}modelToolError uses Python identifier modelToolError
    __modelToolError = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'modelToolError'), 'modelToolError', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131modelToolError', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 124, 3), )

    
    modelToolError = property(__modelToolError.value, __modelToolError.set, None, u'Tool error model used to compute covariance matrix.  ')

    
    # Element {http://www.witsml.org/schemas/131}gravTotalUncert uses Python identifier gravTotalUncert
    __gravTotalUncert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gravTotalUncert'), 'gravTotalUncert', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131gravTotalUncert', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 129, 3), )

    
    gravTotalUncert = property(__gravTotalUncert.value, __gravTotalUncert.set, None, u'Survey tool gravity uncertainty.  ')

    
    # Element {http://www.witsml.org/schemas/131}dipAngleUncert uses Python identifier dipAngleUncert
    __dipAngleUncert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dipAngleUncert'), 'dipAngleUncert', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131dipAngleUncert', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 134, 3), )

    
    dipAngleUncert = property(__dipAngleUncert.value, __dipAngleUncert.set, None, u'Survey tool dip uncertainty.  ')

    
    # Element {http://www.witsml.org/schemas/131}magTotalUncert uses Python identifier magTotalUncert
    __magTotalUncert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magTotalUncert'), 'magTotalUncert', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131magTotalUncert', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 139, 3), )

    
    magTotalUncert = property(__magTotalUncert.value, __magTotalUncert.set, None, u'Survey tool magnetic uncertainty.  ')

    
    # Element {http://www.witsml.org/schemas/131}gravAccelCorUsed uses Python identifier gravAccelCorUsed
    __gravAccelCorUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gravAccelCorUsed'), 'gravAccelCorUsed', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131gravAccelCorUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 144, 3), )

    
    gravAccelCorUsed = property(__gravAccelCorUsed.value, __gravAccelCorUsed.set, None, u'Was an accelerometer alignment correction applied to survey computation?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").\n\t\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/131}magXAxialCorUsed uses Python identifier magXAxialCorUsed
    __magXAxialCorUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magXAxialCorUsed'), 'magXAxialCorUsed', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131magXAxialCorUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 151, 3), )

    
    magXAxialCorUsed = property(__magXAxialCorUsed.value, __magXAxialCorUsed.set, None, u'Was a magnetometer alignment correction applied to survey computation?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").')

    
    # Element {http://www.witsml.org/schemas/131}sagCorUsed uses Python identifier sagCorUsed
    __sagCorUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sagCorUsed'), 'sagCorUsed', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131sagCorUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 157, 3), )

    
    sagCorUsed = property(__sagCorUsed.value, __sagCorUsed.set, None, u'Was a bottom hole assembly sag correction applied to the survey computation?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").')

    
    # Element {http://www.witsml.org/schemas/131}magDrlstrCorUsed uses Python identifier magDrlstrCorUsed
    __magDrlstrCorUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magDrlstrCorUsed'), 'magDrlstrCorUsed', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131magDrlstrCorUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 163, 3), )

    
    magDrlstrCorUsed = property(__magDrlstrCorUsed.value, __magDrlstrCorUsed.set, None, u'Was a drillstring magnetism correction applied to survey computation?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").')

    
    # Element {http://www.witsml.org/schemas/131}gravTotalFieldReference uses Python identifier gravTotalFieldReference
    __gravTotalFieldReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gravTotalFieldReference'), 'gravTotalFieldReference', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131gravTotalFieldReference', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 169, 3), )

    
    gravTotalFieldReference = property(__gravTotalFieldReference.value, __gravTotalFieldReference.set, None, u'Gravitational field theoretical/reference value.\n\t\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/131}magTotalFieldReference uses Python identifier magTotalFieldReference
    __magTotalFieldReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magTotalFieldReference'), 'magTotalFieldReference', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131magTotalFieldReference', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 175, 3), )

    
    magTotalFieldReference = property(__magTotalFieldReference.value, __magTotalFieldReference.set, None, u'Geomagnetic field theoretical/reference value.\n\t\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/131}magDipAngleReference uses Python identifier magDipAngleReference
    __magDipAngleReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magDipAngleReference'), 'magDipAngleReference', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131magDipAngleReference', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 181, 3), )

    
    magDipAngleReference = property(__magDipAngleReference.value, __magDipAngleReference.set, None, u'Magnetic dip angle theoretical/reference value.\n\t\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/131}magModelUsed uses Python identifier magModelUsed
    __magModelUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magModelUsed'), 'magModelUsed', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131magModelUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 187, 3), )

    
    magModelUsed = property(__magModelUsed.value, __magModelUsed.set, None, u'Geomagnetic model used.\n\t\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/131}magModelValid uses Python identifier magModelValid
    __magModelValid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magModelValid'), 'magModelValid', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131magModelValid', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 193, 3), )

    
    magModelValid = property(__magModelValid.value, __magModelValid.set, None, u'Current valid interval for the geomagnetic model used.\n\t\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/131}geoModelUsed uses Python identifier geoModelUsed
    __geoModelUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'geoModelUsed'), 'geoModelUsed', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131geoModelUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 199, 3), )

    
    geoModelUsed = property(__geoModelUsed.value, __geoModelUsed.set, None, u'Gravitational model used.\n\t\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/131}statusTrajStation uses Python identifier statusTrajStation
    __statusTrajStation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'statusTrajStation'), 'statusTrajStation', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131statusTrajStation', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 205, 3), )

    
    statusTrajStation = property(__statusTrajStation.value, __statusTrajStation.set, None, u'Status of the station.  ')

    
    # Element {http://www.witsml.org/schemas/131}rawData uses Python identifier rawData
    __rawData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'rawData'), 'rawData', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131rawData', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 210, 3), )

    
    rawData = property(__rawData.value, __rawData.set, None, u'Applies only to measured magnetic stations.  ')

    
    # Element {http://www.witsml.org/schemas/131}corUsed uses Python identifier corUsed
    __corUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'corUsed'), 'corUsed', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131corUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 215, 3), )

    
    corUsed = property(__corUsed.value, __corUsed.set, None, u'Applies only to measured magnetic stations.  ')

    
    # Element {http://www.witsml.org/schemas/131}valid uses Python identifier valid
    __valid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'valid'), 'valid', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131valid', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 220, 3), )

    
    valid = property(__valid.value, __valid.set, None, u'Applies only to measured magnetic stations.  ')

    
    # Element {http://www.witsml.org/schemas/131}matrixCov uses Python identifier matrixCov
    __matrixCov = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'matrixCov'), 'matrixCov', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131matrixCov', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 225, 3), )

    
    matrixCov = property(__matrixCov.value, __matrixCov.set, None, u'Covariance matrix for error model.  ')

    
    # Element {http://www.witsml.org/schemas/131}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'location'), 'location', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131location', True, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 230, 3), )

    
    location = property(__location.value, __location.set, None, u'The 2D coordinates of the item. \n\t\t\t\t\tNote that within the context of trajectory, the "original" coordinates are\n\t\t\t\t\tinherently local coordinates as defined above.')

    
    # Element {http://www.witsml.org/schemas/131}sourceStation uses Python identifier sourceStation
    __sourceStation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sourceStation'), 'sourceStation', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_httpwww_witsml_orgschemas131sourceStation', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 237, 3), )

    
    sourceStation = property(__sourceStation.value, __sourceStation.set, None, u'A pointer to the trajectoryStation from which this station was derived.\n\t\t\t\t\tThe trajectoryStation may be in another wellbore.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uid'), 'uid', '__httpwww_witsml_orgschemas131_cs_trajectoryStation_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\attgrp_uid.xsd', 20, 2)
    __uid._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\attgrp_uid.xsd', 20, 2)
    
    uid = property(__uid.value, __uid.set, None, u'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


    _ElementMap = {
        __commonData.name() : __commonData,
        __target.name() : __target,
        __dTimStn.name() : __dTimStn,
        __typeTrajStation.name() : __typeTrajStation,
        __typeSurveyTool.name() : __typeSurveyTool,
        __md.name() : __md,
        __tvd.name() : __tvd,
        __incl.name() : __incl,
        __azi.name() : __azi,
        __mtf.name() : __mtf,
        __gtf.name() : __gtf,
        __dispNs.name() : __dispNs,
        __dispEw.name() : __dispEw,
        __vertSect.name() : __vertSect,
        __dls.name() : __dls,
        __rateTurn.name() : __rateTurn,
        __rateBuild.name() : __rateBuild,
        __mdDelta.name() : __mdDelta,
        __tvdDelta.name() : __tvdDelta,
        __modelToolError.name() : __modelToolError,
        __gravTotalUncert.name() : __gravTotalUncert,
        __dipAngleUncert.name() : __dipAngleUncert,
        __magTotalUncert.name() : __magTotalUncert,
        __gravAccelCorUsed.name() : __gravAccelCorUsed,
        __magXAxialCorUsed.name() : __magXAxialCorUsed,
        __sagCorUsed.name() : __sagCorUsed,
        __magDrlstrCorUsed.name() : __magDrlstrCorUsed,
        __gravTotalFieldReference.name() : __gravTotalFieldReference,
        __magTotalFieldReference.name() : __magTotalFieldReference,
        __magDipAngleReference.name() : __magDipAngleReference,
        __magModelUsed.name() : __magModelUsed,
        __magModelValid.name() : __magModelValid,
        __geoModelUsed.name() : __geoModelUsed,
        __statusTrajStation.name() : __statusTrajStation,
        __rawData.name() : __rawData,
        __corUsed.name() : __corUsed,
        __valid.name() : __valid,
        __matrixCov.name() : __matrixCov,
        __location.name() : __location,
        __sourceStation.name() : __sourceStation
    }
    _AttributeMap = {
        __uid.name() : __uid
    }
Namespace.addCategoryObject('typeBinding', u'cs_trajectoryStation', cs_trajectoryStation)


# Complex type {http://www.witsml.org/schemas/131}obj_trajectory with content type ELEMENT_ONLY
class obj_trajectory (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/schemas/131}obj_trajectory with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'obj_trajectory')
    _XSDLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 56, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/131}objectGrowing uses Python identifier objectGrowing
    __objectGrowing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'objectGrowing'), 'objectGrowing', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131objectGrowing', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 24, 3), )

    
    objectGrowing = property(__objectGrowing.value, __objectGrowing.set, None, u'Whether or not the trajectory is growing. \n\t\t\t\t\tTrue ("true" or "1") indicates the that the trajectory is still growing \n\t\t\t\t\tin size (that is, trajectoryStation values are still being added).\n\t\t\t\t\tFor example, it may be connected to a realtime stream.\n\t\t\t\t\tFalse ("false" or "0") indicates that the trajectory is \n\t\t\t\t\tclosed (that is, no further trajectoryStation values will be added).\n\t\t\t\t\tNot given indicates that the status of the trajectory is not known.\n\t\t\t\t\tThis value is only relevant within the context of a server.')

    
    # Element {http://www.witsml.org/schemas/131}parentTrajectory uses Python identifier parentTrajectory
    __parentTrajectory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'parentTrajectory'), 'parentTrajectory', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131parentTrajectory', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 36, 3), )

    
    parentTrajectory = property(__parentTrajectory.value, __parentTrajectory.set, None, u'If a trajectory is tied into another trajectory, \n\t\t\t\t\ta pointer to the parent trajectory.  \n\t\t\t\t\tThe trajectory may be in another wellbore.')

    
    # Element {http://www.witsml.org/schemas/131}dTimTrajStart uses Python identifier dTimTrajStart
    __dTimTrajStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dTimTrajStart'), 'dTimTrajStart', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131dTimTrajStart', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 43, 3), )

    
    dTimTrajStart = property(__dTimTrajStart.value, __dTimTrajStart.set, None, u'Start date and time of trajectory station measurements.\n\t\t\t\t\tNote that this is NOT a server query parameter.')

    
    # Element {http://www.witsml.org/schemas/131}dTimTrajEnd uses Python identifier dTimTrajEnd
    __dTimTrajEnd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dTimTrajEnd'), 'dTimTrajEnd', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131dTimTrajEnd', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 49, 3), )

    
    dTimTrajEnd = property(__dTimTrajEnd.value, __dTimTrajEnd.set, None, u'End date and time of trajectory station measurements.\n\t\t\t\t\tNote that this is NOT a server query parameter.')

    
    # Element {http://www.witsml.org/schemas/131}mdMn uses Python identifier mdMn
    __mdMn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mdMn'), 'mdMn', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131mdMn', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 55, 3), )

    
    mdMn = property(__mdMn.value, __mdMn.set, None, u"Minimum measured depth of trajectory.\n\t\t\t\t\tThis is a query parameter. It's value will be populated by the server\n\t\t\t\t\tto reflect the values of md in the returned trajectoryStations.")

    
    # Element {http://www.witsml.org/schemas/131}mdMx uses Python identifier mdMx
    __mdMx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mdMx'), 'mdMx', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131mdMx', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 62, 3), )

    
    mdMx = property(__mdMx.value, __mdMx.set, None, u"Maximum measured depth of trajectory.\n\t\t\t\t\tThis is a query parameter. It's value will be populated by the server\n\t\t\t\t\tto reflect the values of md in the returned trajectoryStations.")

    
    # Element {http://www.witsml.org/schemas/131}serviceCompany uses Python identifier serviceCompany
    __serviceCompany = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'serviceCompany'), 'serviceCompany', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131serviceCompany', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 69, 3), )

    
    serviceCompany = property(__serviceCompany.value, __serviceCompany.set, None, u'Name of contractor who provided the service.')

    
    # Element {http://www.witsml.org/schemas/131}magDeclUsed uses Python identifier magDeclUsed
    __magDeclUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'magDeclUsed'), 'magDeclUsed', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131magDeclUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 74, 3), )

    
    magDeclUsed = property(__magDeclUsed.value, __magDeclUsed.set, None, u'Magnetic declination used to correct a magnetic survey. \n\t\t\t\t\tStarting value if stations have individual values. ')

    
    # Element {http://www.witsml.org/schemas/131}gridCorUsed uses Python identifier gridCorUsed
    __gridCorUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gridCorUsed'), 'gridCorUsed', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131gridCorUsed', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 80, 3), )

    
    gridCorUsed = property(__gridCorUsed.value, __gridCorUsed.set, None, u'Grid correction used to correct a survey. \n\t\t\t\t\tStarting value if stations have individual values.')

    
    # Element {http://www.witsml.org/schemas/131}aziVertSect uses Python identifier aziVertSect
    __aziVertSect = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'aziVertSect'), 'aziVertSect', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131aziVertSect', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 86, 3), )

    
    aziVertSect = property(__aziVertSect.value, __aziVertSect.set, None, u'Azimuth used for vertical section plot/computations.')

    
    # Element {http://www.witsml.org/schemas/131}dispNsVertSectOrig uses Python identifier dispNsVertSectOrig
    __dispNsVertSectOrig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dispNsVertSectOrig'), 'dispNsVertSectOrig', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131dispNsVertSectOrig', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 91, 3), )

    
    dispNsVertSectOrig = property(__dispNsVertSectOrig.value, __dispNsVertSectOrig.set, None, u'Origin north-south used for vertical section plot/computations.')

    
    # Element {http://www.witsml.org/schemas/131}dispEwVertSectOrig uses Python identifier dispEwVertSectOrig
    __dispEwVertSectOrig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dispEwVertSectOrig'), 'dispEwVertSectOrig', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131dispEwVertSectOrig', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 96, 3), )

    
    dispEwVertSectOrig = property(__dispEwVertSectOrig.value, __dispEwVertSectOrig.set, None, u'Origin east-west used for vertical section plot/computations.')

    
    # Element {http://www.witsml.org/schemas/131}definitive uses Python identifier definitive
    __definitive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'definitive'), 'definitive', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131definitive', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 101, 3), )

    
    definitive = property(__definitive.value, __definitive.set, None, u'True ("true" or "1") indicates that this trajectory is definitive for \n\t\t\t\t\tthis wellbore. False ("false" or "0") or not given indicates otherwise.\n\t\t\t\t\tThere can only be one trajectory per wellbore with definitive=true and it\n\t\t\t\t\tmust define the geometry of the whole wellbore (surface to bottom).\n\t\t\t\t\tThe definitive trajectory may represent a composite of information in many\n\t\t\t\t\tother trajectories. A query requesting a subset of the possible information can\n\t\t\t\t\tprovide a simplistic view of the geometry of the wellbore.')

    
    # Element {http://www.witsml.org/schemas/131}memory uses Python identifier memory
    __memory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'memory'), 'memory', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131memory', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 112, 3), )

    
    memory = property(__memory.value, __memory.set, None, u'Is trajectory a result of a memory dump from a tool?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").')

    
    # Element {http://www.witsml.org/schemas/131}finalTraj uses Python identifier finalTraj
    __finalTraj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'finalTraj'), 'finalTraj', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131finalTraj', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 118, 3), )

    
    finalTraj = property(__finalTraj.value, __finalTraj.set, None, u'Is trajectory a final or intermediate/preliminary?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").')

    
    # Element {http://www.witsml.org/schemas/131}aziRef uses Python identifier aziRef
    __aziRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'aziRef'), 'aziRef', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131aziRef', False, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 124, 3), )

    
    aziRef = property(__aziRef.value, __aziRef.set, None, u'Specifies the definition of north.\n\t\t\t\t\tWhile this is optional because of legacy data, it is strongly recommended \n\t\t\t\t\tthat this always be specified.')

    
    # Element {http://www.witsml.org/schemas/131}trajectoryStation uses Python identifier trajectoryStation
    __trajectoryStation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'trajectoryStation'), 'trajectoryStation', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131trajectoryStation', True, pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 131, 3), )

    
    trajectoryStation = property(__trajectoryStation.value, __trajectoryStation.set, None, u'Container element for trajectory station elements.')

    
    # Element {http://www.witsml.org/schemas/131}nameWell uses Python identifier nameWell
    __nameWell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'nameWell'), 'nameWell', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131nameWell', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 58, 3), )

    
    nameWell = property(__nameWell.value, __nameWell.set, None, u'Human recognizable context for the well that contains the wellbore.  ')

    
    # Element {http://www.witsml.org/schemas/131}nameWellbore uses Python identifier nameWellbore
    __nameWellbore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'nameWellbore'), 'nameWellbore', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131nameWellbore', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 63, 3), )

    
    nameWellbore = property(__nameWellbore.value, __nameWellbore.set, None, u'Human recognizable context for the wellbore that contains the trajectory.  ')

    
    # Element {http://www.witsml.org/schemas/131}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131name', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 68, 3), )

    
    name = property(__name.value, __name.set, None, u'Human recognizable context for the trajectory.  ')

    
    # Element {http://www.witsml.org/schemas/131}commonData uses Python identifier commonData
    __commonData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'commonData'), 'commonData', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131commonData', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 78, 3), )

    
    commonData = property(__commonData.value, __commonData.set, None, u'A container element that contains elements that are common to all data \n\t\t\t\t\tobjects.  ')

    
    # Element {http://www.witsml.org/schemas/131}customData uses Python identifier customData
    __customData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'customData'), 'customData', '__httpwww_witsml_orgschemas131_obj_trajectory_httpwww_witsml_orgschemas131customData', False, pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 84, 3), )

    
    customData = property(__customData.value, __customData.set, None, u'A container element that can contain custom or user defined \n\t\t\t\t\tdata elements.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uid'), 'uid', '__httpwww_witsml_orgschemas131_obj_trajectory_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\attgrp_uid.xsd', 20, 2)
    __uid._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\attgrp_uid.xsd', 20, 2)
    
    uid = property(__uid.value, __uid.set, None, u'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')

    
    # Attribute uidWell uses Python identifier uidWell
    __uidWell = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uidWell'), 'uidWell', '__httpwww_witsml_orgschemas131_obj_trajectory_uidWell', uidString)
    __uidWell._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 91, 2)
    __uidWell._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 91, 2)
    
    uidWell = property(__uidWell.value, __uidWell.set, None, u'Unique identifier for the well. This uniquely represents \n\t\t\t\tthe well referenced by the (possibly non-unique) nameWell. ')

    
    # Attribute uidWellbore uses Python identifier uidWellbore
    __uidWellbore = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uidWellbore'), 'uidWellbore', '__httpwww_witsml_orgschemas131_obj_trajectory_uidWellbore', uidString)
    __uidWellbore._DeclarationLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 97, 2)
    __uidWellbore._UseLocation = pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 97, 2)
    
    uidWellbore = property(__uidWellbore.value, __uidWellbore.set, None, u'Unique identifier for the wellbore. This uniquely represents \n\t\t\t\tthe wellbore referenced by the (possibly non-unique) nameWellbore. ')


    _ElementMap = {
        __objectGrowing.name() : __objectGrowing,
        __parentTrajectory.name() : __parentTrajectory,
        __dTimTrajStart.name() : __dTimTrajStart,
        __dTimTrajEnd.name() : __dTimTrajEnd,
        __mdMn.name() : __mdMn,
        __mdMx.name() : __mdMx,
        __serviceCompany.name() : __serviceCompany,
        __magDeclUsed.name() : __magDeclUsed,
        __gridCorUsed.name() : __gridCorUsed,
        __aziVertSect.name() : __aziVertSect,
        __dispNsVertSectOrig.name() : __dispNsVertSectOrig,
        __dispEwVertSectOrig.name() : __dispEwVertSectOrig,
        __definitive.name() : __definitive,
        __memory.name() : __memory,
        __finalTraj.name() : __finalTraj,
        __aziRef.name() : __aziRef,
        __trajectoryStation.name() : __trajectoryStation,
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
Namespace.addCategoryObject('typeBinding', u'obj_trajectory', obj_trajectory)


# Complex type {http://www.witsml.org/schemas/131}generalMeasureType with content type SIMPLE
class generalMeasureType (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}generalMeasureType with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'generalMeasureType')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 27, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_generalMeasureType_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 30, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 30, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'generalMeasureType', generalMeasureType)


# Complex type {http://www.witsml.org/schemas/131}temperatureSlopeMeasure with content type SIMPLE
class temperatureSlopeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}temperatureSlopeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'temperatureSlopeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 35, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_temperatureSlopeMeasure_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 38, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 38, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'temperatureSlopeMeasure', temperatureSlopeMeasure)


# Complex type {http://www.witsml.org/schemas/131}typeOptionalClassString with content type SIMPLE
class typeOptionalClassString (pyxb.binding.basis.complexTypeDefinition):
    """A type with a classType attribute. This allows a user to give a 
			classification of something, and to specify the type of classification that it is. 
			There is no control over the class values, or the class types."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'typeOptionalClassString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 43, 1)
    # Base type is abstractNameString
    
    # Attribute classType uses Python identifier classType
    __classType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'classType'), 'classType', '__httpwww_witsml_orgschemas131_typeOptionalClassString_classType', kindString)
    __classType._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 51, 4)
    __classType._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 51, 4)
    
    classType = property(__classType.value, __classType.set, None, u'This identifies the classification system to \n\t\t\t\t\t\twhich the class belongs. ')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __classType.name() : __classType
    }
Namespace.addCategoryObject('typeBinding', u'typeOptionalClassString', typeOptionalClassString)


# Complex type {http://www.witsml.org/schemas/131}yAxisAzimuth with content type SIMPLE
class yAxisAzimuth (abstractMeasure):
    """The angle of a Y axis from North.
			This is a variation of planeAngleMeasure with an 
			attribute defining the direction of north."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'yAxisAzimuth')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 106, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_yAxisAzimuth_uom', planeAngleUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 114, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 114, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure of the azimuth value.')

    
    # Attribute northDirection uses Python identifier northDirection
    __northDirection = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'northDirection'), 'northDirection', '__httpwww_witsml_orgschemas131_yAxisAzimuth_northDirection', AziRef)
    __northDirection._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 119, 4)
    __northDirection._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 119, 4)
    
    northDirection = property(__northDirection.value, __northDirection.set, None, u'Specifies the direction to be considered North for the y axis.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __northDirection.name() : __northDirection
    })
Namespace.addCategoryObject('typeBinding', u'yAxisAzimuth', yAxisAzimuth)


# Complex type {http://www.witsml.org/schemas/131}volumePerVolumeMeasurePercent with content type SIMPLE
class volumePerVolumeMeasurePercent (abstractMeasure):
    """A volume per volume measure that is constrained to a unit of percent."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumePerVolumeMeasurePercent')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 128, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_volumePerVolumeMeasurePercent_uom', PercentUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 134, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 134, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'volumePerVolumeMeasurePercent', volumePerVolumeMeasurePercent)


# Complex type {http://www.witsml.org/schemas/131}genericMeasure with content type SIMPLE
class genericMeasure (abstractMeasure):
    """A generic measure type.
			This should not be used except in situations where the underlying class of data is 
			captured elsewhere. For example, for a log curve."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'genericMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 153, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_genericMeasure_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 161, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 161, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure for the quantity.\n\t\t\t\t\t\tThe uom is mandatory unless the value represents a unitless quantity.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'genericMeasure', genericMeasure)


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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ratioGenericMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 187, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_ratioGenericMeasure_uom', uomString, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 201, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 201, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure for the quantity.\n\t\t\t\t\t\tIf for some reason a uom is not appropriate for the quantity,\n\t\t\t\t\t\ta unit of "Euc" should be used.')

    
    # Attribute numerator uses Python identifier numerator
    __numerator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numerator'), 'numerator', '__httpwww_witsml_orgschemas131_ratioGenericMeasure_numerator', unitlessQuantity)
    __numerator._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 208, 4)
    __numerator._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 208, 4)
    
    numerator = property(__numerator.value, __numerator.set, None, None)

    
    # Attribute denominator uses Python identifier denominator
    __denominator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'denominator'), 'denominator', '__httpwww_witsml_orgschemas131_ratioGenericMeasure_denominator', unitlessQuantity)
    __denominator._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 209, 4)
    __denominator._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 209, 4)
    
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
Namespace.addCategoryObject('typeBinding', u'ratioGenericMeasure', ratioGenericMeasure)


# Complex type {http://www.witsml.org/schemas/131}refNameString with content type SIMPLE
class refNameString (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a name in another node of the xml hierachy.
			This value represents a foreign key from one element to another."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'refNameString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 235, 1)
    # Base type is abstractNameString
    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas131_refNameString_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 242, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 242, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, u'A reference to the unique identifier (uid attribute) in the node\n\t\t\t\t\t\treferenced by the name value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', u'refNameString', refNameString)


# Complex type {http://www.witsml.org/schemas/131}refObjectString with content type SIMPLE
class refObjectString (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a name in another object.
			This value represents a foreign key from one object to another.
			Knowledge of the object being referenced is defined by an attribute."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'refObjectString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 253, 1)
    # Base type is abstractNameString
    
    # Attribute object uses Python identifier object
    __object = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'object'), 'object', '__httpwww_witsml_orgschemas131_refObjectString_object', nameString, required=True)
    __object._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 261, 4)
    __object._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 261, 4)
    
    object = property(__object.value, __object.set, None, u'The name of the singular object being referenced.')

    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas131_refObjectString_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 266, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 266, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, u'A reference to the unique identifier (uid attribute) in the object\n\t\t\t\t\t\treferenced by the name value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __object.name() : __object,
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', u'refObjectString', refObjectString)


# Complex type {http://www.witsml.org/schemas/131}refPositiveCount with content type SIMPLE
class refPositiveCount (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a index value in another node of the xml hierachy.
			This value represents a foreign key from one element to another."""
    _TypeDefinition = abstractPositiveCount
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'refPositiveCount')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 277, 1)
    # Base type is abstractPositiveCount
    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas131_refPositiveCount_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 284, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 284, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, u'A reference to the unique identifier (uid attribute) in the node\n\t\t\t\t\t\treferenced by the index value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', u'refPositiveCount', refPositiveCount)


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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'encodedArrayString')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 349, 1)
    # Base type is abstractMaximumLengthString
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_encodedArrayString_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 359, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 359, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uom.name() : __uom
    }
Namespace.addCategoryObject('typeBinding', u'encodedArrayString', encodedArrayString)


# Complex type {http://www.witsml.org/schemas/131}nameStruct with content type SIMPLE
class nameStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of something within a naming system."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameStruct')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 424, 1)
    # Base type is abstractNameString
    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'namingSystem'), 'namingSystem', '__httpwww_witsml_orgschemas131_nameStruct_namingSystem', nameString)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 430, 4)
    __namingSystem._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 430, 4)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, u'The naming system within the name is (hopefully) unique.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __namingSystem.name() : __namingSystem
    }
Namespace.addCategoryObject('typeBinding', u'nameStruct', nameStruct)


# Complex type {http://www.witsml.org/schemas/131}wellKnownNameStruct with content type SIMPLE
class wellKnownNameStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of something within a mandatory naming system 
			with an optional code."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wellKnownNameStruct')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 439, 1)
    # Base type is abstractNameString
    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'namingSystem'), 'namingSystem', '__httpwww_witsml_orgschemas131_wellKnownNameStruct_namingSystem', nameString, required=True)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 446, 4)
    __namingSystem._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 446, 4)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, u'The naming system within the name is unique.')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'code'), 'code', '__httpwww_witsml_orgschemas131_wellKnownNameStruct_code', kindString)
    __code._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 451, 4)
    __code._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 451, 4)
    
    code = property(__code.value, __code.set, None, u'A unique (short) code associated with the name.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __namingSystem.name() : __namingSystem,
        __code.name() : __code
    }
Namespace.addCategoryObject('typeBinding', u'wellKnownNameStruct', wellKnownNameStruct)


# Complex type {http://www.witsml.org/schemas/131}measuredDepthCoord with content type SIMPLE
class measuredDepthCoord (abstractMeasure):
    """A measured depth coordinate in a wellbore. 
			Positive moving from the reference datum toward the bottomhole.
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'measuredDepthCoord')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 492, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_measuredDepthCoord_uom', MeasuredDepthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 501, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 501, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure of the quantity value.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'datum'), 'datum', '__httpwww_witsml_orgschemas131_measuredDepthCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 506, 4)
    __datum._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 506, 4)
    
    datum = property(__datum.value, __datum.set, None, u'A pointer to the reference datum for this coordinate \n\t\t\t\t\t\tvalue as defined in WellDatum. This value is assumed to match the uid\n\t\t\t\t\t\tvalue in a WellDatum.\n\t\t\t\t\t\tIf not given then the default WellDatum must be assumed.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __datum.name() : __datum
    })
Namespace.addCategoryObject('typeBinding', u'measuredDepthCoord', measuredDepthCoord)


# Complex type {http://www.witsml.org/schemas/131}wellVerticalDepthCoord with content type SIMPLE
class wellVerticalDepthCoord (abstractMeasure):
    """A vertical (gravity based) depth coordinate within the context of a well.
			Positive moving downward from the reference datum. 
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wellVerticalDepthCoord')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 541, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_wellVerticalDepthCoord_uom', WellVerticalCoordinateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 550, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 550, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure of the quantity value.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'datum'), 'datum', '__httpwww_witsml_orgschemas131_wellVerticalDepthCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 555, 4)
    __datum._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 555, 4)
    
    datum = property(__datum.value, __datum.set, None, u'A pointer to the reference datum for this coordinate \n\t\t\t\t\t\tvalue as defined in WellDatum. \n\t\t\t\t\t\tIf not given then the default WellDatum must be assumed.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __datum.name() : __datum
    })
Namespace.addCategoryObject('typeBinding', u'wellVerticalDepthCoord', wellVerticalDepthCoord)


# Complex type {http://www.witsml.org/schemas/131}wellElevationCoord with content type SIMPLE
class wellElevationCoord (abstractMeasure):
    """A vertical (gravity based) elevation coordinate within the context of a well.
			Positive moving upward from the reference datum.  
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wellElevationCoord')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 566, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_wellElevationCoord_uom', WellVerticalCoordinateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 575, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 575, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure of the quantity value.\n\t\t\t\t\t\tIf not given then the default unit of measure of the explicitly\n\t\t\t\t\t\tor implicitly given datum must be assumed.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'datum'), 'datum', '__httpwww_witsml_orgschemas131_wellElevationCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 582, 4)
    __datum._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 582, 4)
    
    datum = property(__datum.value, __datum.set, None, u'A pointer to the reference datum for this coordinate \n\t\t\t\t\t\tvalue as defined in WellDatum. \n\t\t\t\t\t\tIf not given then the default WellDatum must be assumed.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __datum.name() : __datum
    })
Namespace.addCategoryObject('typeBinding', u'wellElevationCoord', wellElevationCoord)


# Complex type {http://www.witsml.org/schemas/131}cost with content type SIMPLE
class cost (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/schemas/131}cost with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cost')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 714, 1)
    # Base type is abstractDouble
    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'currency'), 'currency', '__httpwww_witsml_orgschemas131_cost_currency', kindString)
    __currency._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 717, 4)
    __currency._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 717, 4)
    
    currency = property(__currency.value, __currency.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __currency.name() : __currency
    }
Namespace.addCategoryObject('typeBinding', u'cost', cost)


# Complex type {http://www.witsml.org/schemas/131}indexedObject with content type SIMPLE
class indexedObject (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/schemas/131}indexedObject with content type SIMPLE"""
    _TypeDefinition = abstractTypeEnum
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'indexedObject')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 722, 1)
    # Base type is abstractTypeEnum
    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'index'), 'index', '__httpwww_witsml_orgschemas131_indexedObject_index', positiveCount, required=True)
    __index._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 725, 4)
    __index._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 725, 4)
    
    index = property(__index.value, __index.set, None, u'Indexes things with the same name. \n\t\t\t\t\t\tThat is the first one, the second one, etc.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_witsml_orgschemas131_indexedObject_name', kindString)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 731, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 731, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_indexedObject_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 732, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 732, 4)
    
    uom = property(__uom.value, __uom.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpwww_witsml_orgschemas131_indexedObject_description', descriptionString)
    __description._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 733, 4)
    __description._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_dataTypes.xsd', 733, 4)
    
    description = property(__description.value, __description.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __index.name() : __index,
        __name.name() : __name,
        __uom.name() : __uom,
        __description.name() : __description
    }
Namespace.addCategoryObject('typeBinding', u'indexedObject', indexedObject)


# Complex type {http://www.witsml.org/schemas/131}accelerationLinearMeasure with content type SIMPLE
class accelerationLinearMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}accelerationLinearMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accelerationLinearMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 24, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_accelerationLinearMeasure_uom', accelerationLinearUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 27, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 27, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'accelerationLinearMeasure', accelerationLinearMeasure)


# Complex type {http://www.witsml.org/schemas/131}anglePerLengthMeasure with content type SIMPLE
class anglePerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}anglePerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'anglePerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 32, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_anglePerLengthMeasure_uom', anglePerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 35, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 35, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'anglePerLengthMeasure', anglePerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}anglePerTimeMeasure with content type SIMPLE
class anglePerTimeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}anglePerTimeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'anglePerTimeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 40, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_anglePerTimeMeasure_uom', anglePerTimeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 43, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 43, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'anglePerTimeMeasure', anglePerTimeMeasure)


# Complex type {http://www.witsml.org/schemas/131}areaMeasure with content type SIMPLE
class areaMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}areaMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'areaMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 48, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_areaMeasure_uom', areaUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 51, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 51, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'areaMeasure', areaMeasure)


# Complex type {http://www.witsml.org/schemas/131}areaPerAreaMeasure with content type SIMPLE
class areaPerAreaMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}areaPerAreaMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'areaPerAreaMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 56, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_areaPerAreaMeasure_uom', areaPerAreaUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 59, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 59, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'areaPerAreaMeasure', areaPerAreaMeasure)


# Complex type {http://www.witsml.org/schemas/131}densityMeasure with content type SIMPLE
class densityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}densityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'densityMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 64, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_densityMeasure_uom', densityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 67, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 67, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'densityMeasure', densityMeasure)


# Complex type {http://www.witsml.org/schemas/131}dimensionlessMeasure with content type SIMPLE
class dimensionlessMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}dimensionlessMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dimensionlessMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 72, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_dimensionlessMeasure_uom', dimensionlessUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 75, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 75, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'dimensionlessMeasure', dimensionlessMeasure)


# Complex type {http://www.witsml.org/schemas/131}dynamicViscosityMeasure with content type SIMPLE
class dynamicViscosityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}dynamicViscosityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dynamicViscosityMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 80, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_dynamicViscosityMeasure_uom', dynamicViscosityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 83, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 83, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'dynamicViscosityMeasure', dynamicViscosityMeasure)


# Complex type {http://www.witsml.org/schemas/131}electricCurrentMeasure with content type SIMPLE
class electricCurrentMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}electricCurrentMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'electricCurrentMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 88, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_electricCurrentMeasure_uom', electricCurrentUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 91, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 91, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'electricCurrentMeasure', electricCurrentMeasure)


# Complex type {http://www.witsml.org/schemas/131}electricPotentialMeasure with content type SIMPLE
class electricPotentialMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}electricPotentialMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'electricPotentialMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 96, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_electricPotentialMeasure_uom', electricPotentialUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 99, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 99, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'electricPotentialMeasure', electricPotentialMeasure)


# Complex type {http://www.witsml.org/schemas/131}energyPerAreaMeasure with content type SIMPLE
class energyPerAreaMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}energyPerAreaMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'energyPerAreaMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 104, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_energyPerAreaMeasure_uom', energyPerAreaUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 107, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 107, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'energyPerAreaMeasure', energyPerAreaMeasure)


# Complex type {http://www.witsml.org/schemas/131}equivalentPerMassMeasure with content type SIMPLE
class equivalentPerMassMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}equivalentPerMassMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'equivalentPerMassMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 112, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_equivalentPerMassMeasure_uom', equivalentPerMassUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 115, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 115, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'equivalentPerMassMeasure', equivalentPerMassMeasure)


# Complex type {http://www.witsml.org/schemas/131}forceMeasure with content type SIMPLE
class forceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}forceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'forceMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 120, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_forceMeasure_uom', forceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 123, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 123, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'forceMeasure', forceMeasure)


# Complex type {http://www.witsml.org/schemas/131}forcePerLengthMeasure with content type SIMPLE
class forcePerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}forcePerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'forcePerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 128, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_forcePerLengthMeasure_uom', forcePerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 131, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 131, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'forcePerLengthMeasure', forcePerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}forcePerVolumeMeasure with content type SIMPLE
class forcePerVolumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}forcePerVolumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'forcePerVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 136, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_forcePerVolumeMeasure_uom', forcePerVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 139, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 139, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'forcePerVolumeMeasure', forcePerVolumeMeasure)


# Complex type {http://www.witsml.org/schemas/131}frequencyMeasure with content type SIMPLE
class frequencyMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}frequencyMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'frequencyMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 144, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_frequencyMeasure_uom', frequencyUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 147, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 147, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'frequencyMeasure', frequencyMeasure)


# Complex type {http://www.witsml.org/schemas/131}illuminanceMeasure with content type SIMPLE
class illuminanceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}illuminanceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminanceMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 152, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_illuminanceMeasure_uom', illuminanceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 155, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 155, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'illuminanceMeasure', illuminanceMeasure)


# Complex type {http://www.witsml.org/schemas/131}lengthMeasure with content type SIMPLE
class lengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}lengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 160, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_lengthMeasure_uom', lengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 163, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 163, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'lengthMeasure', lengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}lengthPerLengthMeasure with content type SIMPLE
class lengthPerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}lengthPerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lengthPerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 168, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_lengthPerLengthMeasure_uom', lengthPerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 171, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 171, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'lengthPerLengthMeasure', lengthPerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}magneticFieldStrengthMeasure with content type SIMPLE
class magneticFieldStrengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}magneticFieldStrengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'magneticFieldStrengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 176, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_magneticFieldStrengthMeasure_uom', magneticFieldStrengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 179, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 179, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'magneticFieldStrengthMeasure', magneticFieldStrengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}magneticInductionMeasure with content type SIMPLE
class magneticInductionMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}magneticInductionMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'magneticInductionMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 184, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_magneticInductionMeasure_uom', magneticInductionUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 187, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 187, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'magneticInductionMeasure', magneticInductionMeasure)


# Complex type {http://www.witsml.org/schemas/131}massConcentrationMeasure with content type SIMPLE
class massConcentrationMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}massConcentrationMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'massConcentrationMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 192, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_massConcentrationMeasure_uom', massConcentrationUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 195, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 195, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'massConcentrationMeasure', massConcentrationMeasure)


# Complex type {http://www.witsml.org/schemas/131}massMeasure with content type SIMPLE
class massMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}massMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'massMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 200, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_massMeasure_uom', massUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 203, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 203, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'massMeasure', massMeasure)


# Complex type {http://www.witsml.org/schemas/131}massPerLengthMeasure with content type SIMPLE
class massPerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}massPerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'massPerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 208, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_massPerLengthMeasure_uom', massPerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 211, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 211, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'massPerLengthMeasure', massPerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}momentOfForceMeasure with content type SIMPLE
class momentOfForceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}momentOfForceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'momentOfForceMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 216, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_momentOfForceMeasure_uom', momentOfForceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 219, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 219, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'momentOfForceMeasure', momentOfForceMeasure)


# Complex type {http://www.witsml.org/schemas/131}perLengthMeasure with content type SIMPLE
class perLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}perLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'perLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 224, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_perLengthMeasure_uom', perLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 227, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 227, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'perLengthMeasure', perLengthMeasure)


# Complex type {http://www.witsml.org/schemas/131}planeAngleMeasure with content type SIMPLE
class planeAngleMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}planeAngleMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'planeAngleMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 232, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_planeAngleMeasure_uom', planeAngleUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 235, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 235, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'planeAngleMeasure', planeAngleMeasure)


# Complex type {http://www.witsml.org/schemas/131}powerMeasure with content type SIMPLE
class powerMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}powerMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'powerMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 240, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_powerMeasure_uom', powerUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 243, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 243, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'powerMeasure', powerMeasure)


# Complex type {http://www.witsml.org/schemas/131}pressureMeasure with content type SIMPLE
class pressureMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}pressureMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pressureMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 248, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_pressureMeasure_uom', pressureUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 251, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 251, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'pressureMeasure', pressureMeasure)


# Complex type {http://www.witsml.org/schemas/131}relativePowerMeasure with content type SIMPLE
class relativePowerMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}relativePowerMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'relativePowerMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 256, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_relativePowerMeasure_uom', relativePowerUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 259, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 259, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'relativePowerMeasure', relativePowerMeasure)


# Complex type {http://www.witsml.org/schemas/131}specificVolumeMeasure with content type SIMPLE
class specificVolumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}specificVolumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'specificVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 264, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_specificVolumeMeasure_uom', specificVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 267, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 267, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'specificVolumeMeasure', specificVolumeMeasure)


# Complex type {http://www.witsml.org/schemas/131}thermodynamicTemperatureMeasure with content type SIMPLE
class thermodynamicTemperatureMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}thermodynamicTemperatureMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'thermodynamicTemperatureMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 272, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_thermodynamicTemperatureMeasure_uom', thermodynamicTemperatureUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 275, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 275, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'thermodynamicTemperatureMeasure', thermodynamicTemperatureMeasure)


# Complex type {http://www.witsml.org/schemas/131}timeMeasure with content type SIMPLE
class timeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}timeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 280, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_timeMeasure_uom', timeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 283, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 283, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'timeMeasure', timeMeasure)


# Complex type {http://www.witsml.org/schemas/131}velocityMeasure with content type SIMPLE
class velocityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}velocityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'velocityMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 288, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_velocityMeasure_uom', velocityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 291, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 291, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'velocityMeasure', velocityMeasure)


# Complex type {http://www.witsml.org/schemas/131}volumeMeasure with content type SIMPLE
class volumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}volumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 296, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_volumeMeasure_uom', volumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 299, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 299, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'volumeMeasure', volumeMeasure)


# Complex type {http://www.witsml.org/schemas/131}volumeFlowRateMeasure with content type SIMPLE
class volumeFlowRateMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}volumeFlowRateMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumeFlowRateMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 304, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_volumeFlowRateMeasure_uom', volumeFlowRateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 307, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 307, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'volumeFlowRateMeasure', volumeFlowRateMeasure)


# Complex type {http://www.witsml.org/schemas/131}volumePerVolumeMeasure with content type SIMPLE
class volumePerVolumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/131}volumePerVolumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumePerVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 312, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas131_volumePerVolumeMeasure_uom', volumePerVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 315, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\typ_measureType.xsd', 315, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'volumePerVolumeMeasure', volumePerVolumeMeasure)


trajectorys = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trajectorys'), obj_trajectorys, documentation=u'The WITSML API mandated plural root element which allows \n\t\t\tmultiple singular objects to be sent. The plural name is formed by adding\n\t\t\tan "s" to the singular name.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', trajectorys.name().localName(), trajectorys)



cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sourceName'), nameString, scope=cs_commonData, documentation=u'An identifier to indicate the data originator.\n\t\t\t\t\tThis identifies the server that originally created \n\t\t\t\t\tthe object and thus most of the uids in the object (but not \n\t\t\t\t\tnecessarily the uids of the parents). This is typically a url. ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 23, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dTimCreation'), timestamp, scope=cs_commonData, documentation=u'When the data was created at the persistent data store.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 31, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dTimLastChange'), timestamp, scope=cs_commonData, documentation=u'Last change of any element of the data at the persistent data store.\n\t\t\t\t\tThe change time is not updated for a growing object while it is growing.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 36, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'itemState'), ItemState, scope=cs_commonData, documentation=u'The item state for the data object.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 42, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comments'), commentString, scope=cs_commonData, documentation=u'Comments and remarks.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 47, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 23, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 36, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 42, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 47, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sourceName')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 23, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dTimCreation')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dTimLastChange')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 36, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'itemState')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comments')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_commonData.xsd', 47, 3))
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
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_customData.xsd', 22, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_customData.xsd', 22, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_customData._Automaton = _BuildAutomaton_()




cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DocumentName'), nameStruct, scope=cs_documentInfo, documentation=u'An identifier for the document. This is \n\t\t\t\t\tintended to be unique within the context of the NamingSystem.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 26, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DocumentAlias'), nameStruct, scope=cs_documentInfo, documentation=u'Zero or more alternate names for the document. \n\t\t\t\t\tThese names do not need to be unique within the naming system.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 32, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DocumentDate'), timestamp, scope=cs_documentInfo, documentation=u'The date of the creation of the document. \n\t\t\t\t\tThis is not the same as the date that the file was created. \n\t\t\t\t\tFor this date, the document is considered to be the set of \n\t\t\t\t\tinformation associated with this document information. \n\t\t\t\t\tFor example, the document may be a seismic binset. \n\t\t\t\t\tThis represents the date that the binset was created. \n\t\t\t\t\tThe FileCreation information would capture the date that \n\t\t\t\t\tthe XML file was created to send or exchange the binset.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 38, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'documentClass'), nameStruct, scope=cs_documentInfo, documentation=u'A document class. Examples of classes would be a \n\t\t\t\t\tmetadata classification or a set of keywords. ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 50, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileCreationInformation'), fileCreationType, scope=cs_documentInfo, documentation=u'The information about the creation of the \n\t\t\t\t\texchange file. This is not about the creation of the data within \n\t\t\t\t\tthe file, but the creation of the file itself.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 56, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SecurityInformation'), securityInfoType, scope=cs_documentInfo, documentation=u'Information about the security to be applied to \n\t\t\t\t\tthis file. More than one classification can be given.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 63, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Disclaimer'), commentString, scope=cs_documentInfo, documentation=u'A free-form string that allows a disclaimer to \n\t\t\t\t\taccompany the information.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 69, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AuditTrail'), auditType, scope=cs_documentInfo, documentation=u'A collection of events that can document the \n\t\t\t\t\thistory of the data.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 75, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Owner'), nameString, scope=cs_documentInfo, documentation=u'The owner of the data.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 81, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Comment'), commentString, scope=cs_documentInfo, documentation=u'An optional comment about the document.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 86, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 32, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 38, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 50, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 56, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=5L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 63, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 69, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 75, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 81, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 86, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DocumentName')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DocumentAlias')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 32, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DocumentDate')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'documentClass')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 50, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileCreationInformation')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 56, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SecurityInformation')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 63, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Disclaimer')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 69, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AuditTrail')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 75, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Owner')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 81, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Comment')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 86, 3))
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




fileCreationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileCreationDate'), timestamp, scope=fileCreationType, documentation=u'The date and time that the file was created.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 100, 3)))

fileCreationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SoftwareName'), nameString, scope=fileCreationType, documentation=u'If appropriate, the software that created the file. \n\t\t\t\t\tThis is a free form string, and may include whatever information \n\t\t\t\t\tis deemed relevant.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 105, 3)))

fileCreationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileCreator'), nameString, scope=fileCreationType, documentation=u'The person or business associate that created \n\t\t\t\t\tthe file.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 112, 3)))

fileCreationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Comment'), commentString, scope=fileCreationType, documentation=u'Any comment that would be useful to further \n\t\t\t\t\texplain the creation of this instance document.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 118, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 105, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 112, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 118, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fileCreationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileCreationDate')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 100, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(fileCreationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SoftwareName')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 105, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(fileCreationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileCreator')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 112, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(fileCreationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Comment')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 118, 3))
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




securityInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Class'), kindString, scope=securityInfoType, documentation=u'The security class in which this document is \n\t\t\t\t\tclassified. Examples would be confidential, partner confidential, \n\t\t\t\t\ttight. The meaning of the class is determined by the System in which \n\t\t\t\t\tit is defined.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 138, 3)))

securityInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'System'), kindString, scope=securityInfoType, documentation=u'The security classification system. \n\t\t\t\t\tThis gives context to the meaning of the Class value.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 146, 3)))

securityInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndDate'), timestamp, scope=securityInfoType, documentation=u'The date on which this security class is no \n\t\t\t\t\tlonger applicable.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 152, 3)))

securityInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Comment'), commentString, scope=securityInfoType, documentation=u'A general comment to further define the security \n\t\t\t\t\tclass.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 158, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 138, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 146, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 152, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 158, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Class')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 138, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'System')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 146, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndDate')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 152, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(securityInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Comment')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 158, 3))
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




auditType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Event'), eventType, scope=auditType, location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 173, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(auditType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Event')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 173, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
auditType._Automaton = _BuildAutomaton_5()




eventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EventDate'), timestamp, scope=eventType, documentation=u'The date on which the event took place.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 183, 3)))

eventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ResponsibleParty'), nameString, scope=eventType, documentation=u'The party responsible for the event.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 188, 3)))

eventType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Comment'), commentString, scope=eventType, documentation=u'A free form comment that can further \n\t\t\t\t\tdefine the event that occurred.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 193, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 188, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 193, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(eventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EventDate')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 183, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(eventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ResponsibleParty')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 188, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(eventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Comment')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_documentInfo.xsd', 193, 3))
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




cs_refWellboreTrajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trajectoryReference'), refNameString, scope=cs_refWellboreTrajectory, documentation=u'A pointer to the trajectory within the wellbore.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectory.xsd', 26, 3)))

cs_refWellboreTrajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wellboreParent'), refNameString, scope=cs_refWellboreTrajectory, documentation=u'A pointer to the wellbore that contains the trajectoryReference.\n\t\t\t\t\tThis is not needed unless the trajectory is outside the \n\t\t\t\t\tcontext of a common parent wellbore.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectory.xsd', 31, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectory.xsd', 31, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_refWellboreTrajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trajectoryReference')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectory.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_refWellboreTrajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wellboreParent')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectory.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_refWellboreTrajectory._Automaton = _BuildAutomaton_7()




cs_refWellboreTrajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stationReference'), refString, scope=cs_refWellboreTrajectoryStation, documentation=u'A pointer to the trajectoryStation within the parent trajectory.\n\t\t\t\t\tThis is a special case where we only use a uid for the pointer.\n\t\t\t\t\tThe natural identity of a station is its physical characteristics (e.g., md).', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 26, 3)))

cs_refWellboreTrajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trajectoryParent'), refNameString, scope=cs_refWellboreTrajectoryStation, documentation=u'A pointer to the trajectory within the parent wellbore.\n\t\t\t\t\tThis trajectory contains the trajectoryStation.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 33, 3)))

cs_refWellboreTrajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wellboreParent'), refNameString, scope=cs_refWellboreTrajectoryStation, documentation=u'A pointer to the wellbore that contains the trajectory.\n\t\t\t\t\tThis is not needed unless the trajectory is outside the \n\t\t\t\t\tcontext of a common parent wellbore.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 39, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 39, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_refWellboreTrajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stationReference')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_refWellboreTrajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trajectoryParent')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_refWellboreTrajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wellboreParent')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_refWellboreTrajectoryStation.xsd', 39, 3))
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
cs_refWellboreTrajectoryStation._Automaton = _BuildAutomaton_8()




cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gravAxialAccelCor'), accelerationLinearMeasure, scope=cs_stnTrajCorUsed, documentation=u'Calculated gravitational field strength correction.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 23, 3)))

cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gravTran1AccelCor'), accelerationLinearMeasure, scope=cs_stnTrajCorUsed, documentation=u'The correction applied to the X cross-axial component of the earths magnetic field.\n\t\t\t\t', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 28, 3)))

cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gravTran2AccelCor'), accelerationLinearMeasure, scope=cs_stnTrajCorUsed, documentation=u'The correction applied to the Y cross-axial component of the earths magnetic field.\n\t\t\t\t', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 34, 3)))

cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magAxialDrlstrCor'), magneticInductionMeasure, scope=cs_stnTrajCorUsed, documentation=u'Axial magnetic drillstring correction.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 40, 3)))

cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magTran1DrlstrCor'), magneticInductionMeasure, scope=cs_stnTrajCorUsed, documentation=u'Cross-axial magnetic correction.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 45, 3)))

cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magTran2DrlstrCor'), magneticInductionMeasure, scope=cs_stnTrajCorUsed, documentation=u'Cross-axial magnetic correction.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 50, 3)))

cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sagIncCor'), planeAngleMeasure, scope=cs_stnTrajCorUsed, documentation=u'Calculated sag correction to inclination.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 55, 3)))

cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sagAziCor'), planeAngleMeasure, scope=cs_stnTrajCorUsed, documentation=u'Calculated sag correction to azimuth.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 60, 3)))

cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stnMagDeclUsed'), planeAngleMeasure, scope=cs_stnTrajCorUsed, documentation=u'Magnetic declination used to correct a magnetic survey station.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 65, 3)))

cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stnGridCorUsed'), planeAngleMeasure, scope=cs_stnTrajCorUsed, documentation=u'Grid Correction (Meridian convergence). The angle between \n\t\t\t\t\tTrue North and Grid North. Grid Correction is positive when True North \n\t\t\t\t\tis west of Grid North. The correction is added to the raw observation, \n\t\t\t\t\tthus yielding a reduced or corrected observation that can go into \n\t\t\t\t\tthe subsequent calculations.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 70, 3)))

cs_stnTrajCorUsed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dirSensorOffset'), lengthMeasure, scope=cs_stnTrajCorUsed, documentation=u'Offset relative to bit.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 79, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 23, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 28, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 40, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 45, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 50, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 55, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 60, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 65, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 70, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 79, 3))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gravAxialAccelCor')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 23, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gravTran1AccelCor')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 28, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gravTran2AccelCor')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magAxialDrlstrCor')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 40, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magTran1DrlstrCor')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 45, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magTran2DrlstrCor')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 50, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sagIncCor')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 55, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sagAziCor')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 60, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stnMagDeclUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 65, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stnGridCorUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 70, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajCorUsed._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dirSensorOffset')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajCorUsed.xsd', 79, 3))
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
cs_stnTrajCorUsed._Automaton = _BuildAutomaton_9()




cs_stnTrajMatrixCov._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varianceNN'), areaMeasure, scope=cs_stnTrajMatrixCov, documentation=u'Covariance north north.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 23, 3)))

cs_stnTrajMatrixCov._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varianceNE'), areaMeasure, scope=cs_stnTrajMatrixCov, documentation=u'Crossvariance north east.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 28, 3)))

cs_stnTrajMatrixCov._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varianceNVert'), areaMeasure, scope=cs_stnTrajMatrixCov, documentation=u'Crossvariance north vertical.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 33, 3)))

cs_stnTrajMatrixCov._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varianceEE'), areaMeasure, scope=cs_stnTrajMatrixCov, documentation=u'Covariance east east.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 38, 3)))

cs_stnTrajMatrixCov._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varianceEVert'), areaMeasure, scope=cs_stnTrajMatrixCov, documentation=u'Crossvariance east vertical.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 43, 3)))

cs_stnTrajMatrixCov._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varianceVertVert'), areaMeasure, scope=cs_stnTrajMatrixCov, documentation=u'Covariance vertical vertical.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 48, 3)))

cs_stnTrajMatrixCov._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'biasN'), lengthMeasure, scope=cs_stnTrajMatrixCov, documentation=u'Bias north.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 53, 3)))

cs_stnTrajMatrixCov._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'biasE'), lengthMeasure, scope=cs_stnTrajMatrixCov, documentation=u'Bias east.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 58, 3)))

cs_stnTrajMatrixCov._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'biasVert'), lengthMeasure, scope=cs_stnTrajMatrixCov, documentation=u'Bias vertical.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 63, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 23, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 28, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 33, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 38, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 43, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 48, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 53, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 58, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 63, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajMatrixCov._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varianceNN')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 23, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajMatrixCov._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varianceNE')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 28, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajMatrixCov._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varianceNVert')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 33, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajMatrixCov._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varianceEE')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 38, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajMatrixCov._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varianceEVert')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajMatrixCov._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varianceVertVert')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 48, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajMatrixCov._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'biasN')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 53, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajMatrixCov._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'biasE')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 58, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajMatrixCov._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'biasVert')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajMatrixCov.xsd', 63, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_stnTrajMatrixCov._Automaton = _BuildAutomaton_10()




cs_stnTrajRawData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gravAxialRaw'), accelerationLinearMeasure, scope=cs_stnTrajRawData, documentation=u'Uncorrected gravitational field strength measured in axial direction.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 23, 3)))

cs_stnTrajRawData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gravTran1Raw'), accelerationLinearMeasure, scope=cs_stnTrajRawData, documentation=u'Uncorrected gravitational field strength measured in transverse direction.\n\t\t\t\t', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 28, 3)))

cs_stnTrajRawData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gravTran2Raw'), accelerationLinearMeasure, scope=cs_stnTrajRawData, documentation=u'Uncorrected gravitational field strength measured in transverse direction, \n\t\t\t\tapproximately normal to tran1.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 34, 3)))

cs_stnTrajRawData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magAxialRaw'), magneticInductionMeasure, scope=cs_stnTrajRawData, documentation=u'Uncorrected magnetic field strength measured in axial direction.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 40, 3)))

cs_stnTrajRawData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magTran1Raw'), magneticInductionMeasure, scope=cs_stnTrajRawData, documentation=u'Uncorrected magnetic field strength measured in transverse direction.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 45, 3)))

cs_stnTrajRawData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magTran2Raw'), magneticInductionMeasure, scope=cs_stnTrajRawData, documentation=u'Uncorrected magnetic field strength measured in transverse direction, \n\t\t\t\t\tapproximately normal to tran1.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 50, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 23, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 28, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 34, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 40, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 45, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 50, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajRawData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gravAxialRaw')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 23, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajRawData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gravTran1Raw')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 28, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajRawData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gravTran2Raw')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 34, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajRawData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magAxialRaw')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 40, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajRawData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magTran1Raw')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 45, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajRawData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magTran2Raw')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajRawData.xsd', 50, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
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
    return fac.Automaton(states, counters, True, containing_state=None)
cs_stnTrajRawData._Automaton = _BuildAutomaton_11()




cs_stnTrajValid._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magTotalFieldCalc'), magneticInductionMeasure, scope=cs_stnTrajValid, documentation=u'Calculated total intensity of the geomagnetic field as sum of BGGM, \n\t\t\t\t\tIFR and local field. ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 23, 3)))

cs_stnTrajValid._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magDipAngleCalc'), planeAngleMeasure, scope=cs_stnTrajValid, documentation=u'Calculated magnetic dip (inclination), the angle between the horizontal \n\t\t\t\t\tand the geomagnetic field (positive down, res .001).  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 29, 3)))

cs_stnTrajValid._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gravTotalFieldCalc'), accelerationLinearMeasure, scope=cs_stnTrajValid, documentation=u'Calculated total gravitational field.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 35, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 23, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 29, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 35, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajValid._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magTotalFieldCalc')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 23, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajValid._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magDipAngleCalc')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 29, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_stnTrajValid._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gravTotalFieldCalc')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_stnTrajValid.xsd', 35, 3))
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
cs_stnTrajValid._Automaton = _BuildAutomaton_12()




obj_trajectorys._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'documentInfo'), cs_documentInfo, scope=obj_trajectorys, documentation=u'Information about the XML message instance.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 36, 3)))

obj_trajectorys._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trajectory'), obj_trajectory, scope=obj_trajectorys, documentation=u'A single trajectory.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 41, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 36, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_trajectorys._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'documentInfo')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(obj_trajectorys._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trajectory')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 41, 3))
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
obj_trajectorys._Automaton = _BuildAutomaton_13()




cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wellCRS'), refNameString, scope=cs_location, documentation=u'A pointer to the wellCRS that defines the CRS for the coordinates. \n\t\t\t\t\tWhile optional, it is strongly recommended that this be specified.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 27, 3)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'latitude'), planeAngleMeasure, scope=cs_location, documentation=u'The latitude with north being positive.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 45, 5)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'longitude'), planeAngleMeasure, scope=cs_location, documentation=u'The longitude with east being positive.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 50, 5)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'easting'), lengthMeasure, scope=cs_location, documentation=u'The projected coordinate with east being positive. \n\t\t\t\t\t\t\tThis is the most common type of projected coordinates. \n\t\t\t\t\t\t\tUTM coordinates are expressed in Easting and Northing.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 57, 5)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'northing'), lengthMeasure, scope=cs_location, documentation=u'The projected coordinate with north being positive. \n\t\t\t\t\t\t\tThis is the most common type of projected coordinates. \n\t\t\t\t\t\t\tUTM coordinates are expressed in Easting and Northing.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 64, 5)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'westing'), lengthMeasure, scope=cs_location, documentation=u'The projected coordinate with west being positive. \n\t\t\t\t\t\t\tThe positive directions are reversed from the usual Easting and Northing values. \n\t\t\t\t\t\t\tThese values are generally located in the southern hemisphere, \n\t\t\t\t\t\t\tmost notably in South Africa and Australia.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 73, 5)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'southing'), lengthMeasure, scope=cs_location, documentation=u'The projected coordinate with south being positive. \n\t\t\t\t\t\t\tThe positive directions are reversed from the usual Easting and Northing values. \n\t\t\t\t\t\t\tThese values are generally located in the southern hemisphere, \n\t\t\t\t\t\t\tmost notably in South Africa and Australia.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 81, 5)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'projectedX'), lengthMeasure, scope=cs_location, documentation=u'The projected X coordinate with the positive direction unknown.\n\t\t\t\t\t\t\tProjectedX and ProjectedY are used when it is not \n\t\t\t\t\t\t\tknown what the meaning of the coordinates is. If the meaning is known, \n\t\t\t\t\t\t\tthe Easting/Northing or Westing/Southing should be used. Use of this pair \n\t\t\t\t\t\t\timplies a lack of knowledge on the part of the sender.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 91, 5)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'projectedY'), lengthMeasure, scope=cs_location, documentation=u'The projected Y coordinate with the positive direction unknown.\n\t\t\t\t\t\t\tProjectedX and ProjectedY are used when it is not \n\t\t\t\t\t\t\tknown what the meaning of the coordinates is. If the meaning is known, \n\t\t\t\t\t\t\tthe Easting/Northing or Westing/Southing should be used. Use of this pair \n\t\t\t\t\t\t\timplies a lack of knowledge on the part of the sender.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 100, 5)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'localX'), lengthMeasure, scope=cs_location, documentation=u'The local (engineering) X coordinate. \n\t\t\t\t\t\t\tThe CRS will define the orientation of the axis.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 111, 5)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'localY'), lengthMeasure, scope=cs_location, documentation=u'The local (engineering) Y coordinate. \n\t\t\t\t\t\t\tThe CRS will define the orientation of the axis.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 117, 5)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'original'), logicalBoolean, scope=cs_location, documentation=u'Flag indicating (if "true" or "1") that this pair of values was \n\t\t\t\t\tthe original data given for the location. If the pair of values was \n\t\t\t\t\tcalculated from an original pair of values, this flag should be "false" (or "0"), \n\t\t\t\t\tor not present.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 125, 3)))

cs_location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), descriptionString, scope=cs_location, documentation=u'A Comment, generally given to help the reader \n\t\t\t\t\tinterpret the coordinates if the CRS and the chosen pair do not make them clear.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 133, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 27, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 33, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 44, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 56, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 72, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 90, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 110, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 125, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 133, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wellCRS')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 27, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'latitude')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 45, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'longitude')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 50, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'easting')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 57, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'northing')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 64, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'westing')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 73, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'southing')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 81, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'projectedX')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 91, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'projectedY')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 100, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'localX')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 111, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'localY')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 117, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'original')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 125, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_location._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_location.xsd', 133, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_location._Automaton = _BuildAutomaton_14()




cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'commonData'), cs_commonData, scope=cs_trajectoryStation, documentation=u'A container element that contains elements that are common to all data \n\t\t\t\t\tobjects.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_trajectoryStation.xsd', 30, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'target'), refNameString, scope=cs_trajectoryStation, documentation=u'A pointer to the intended target of this station.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 28, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dTimStn'), timestamp, scope=cs_trajectoryStation, documentation=u'Date and time the station was measured or created.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 33, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'typeTrajStation'), TrajStationType, scope=cs_trajectoryStation, documentation=u'Type of survey station.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 38, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'typeSurveyTool'), TypeSurveyTool, scope=cs_trajectoryStation, documentation=u'The type of tool used for the measurements.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 43, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'md'), measuredDepthCoord, scope=cs_trajectoryStation, documentation=u'Measured depth of measurement from the drill datum.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 48, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tvd'), wellVerticalDepthCoord, scope=cs_trajectoryStation, documentation=u'Vertical depth of the measurements.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 53, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'incl'), planeAngleMeasure, scope=cs_trajectoryStation, documentation=u'Hole inclination, measured from vertical.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 58, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'azi'), planeAngleMeasure, scope=cs_trajectoryStation, documentation=u'Hole azimuth. Corrected to wells azimuth reference.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 63, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mtf'), planeAngleMeasure, scope=cs_trajectoryStation, documentation=u'Toolface angle (magnetic).  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 68, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gtf'), planeAngleMeasure, scope=cs_trajectoryStation, documentation=u'Toolface angle (gravity).  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 73, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dispNs'), lengthMeasure, scope=cs_trajectoryStation, documentation=u'North-south offset, positive to the North. \n\t\t\t\t\tThis is relative to wellLocation with a North axis orientation of aziRef.\n\t\t\t\t\tIf a displacement with respect to a different point is desired then\n\t\t\t\t\tdefine a localCRS and specify local coordinates in location.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 78, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dispEw'), lengthMeasure, scope=cs_trajectoryStation, documentation=u'East-west offset, positive to the East.\n\t\t\t\t\tThis is relative to wellLocation with a North axis orientation of aziRef. \n\t\t\t\t\tIf a displacement with respect to a different point is desired then\n\t\t\t\t\tdefine a localCRS and specify local coordinates in location. ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 86, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'vertSect'), lengthMeasure, scope=cs_trajectoryStation, documentation=u'Distance along vertical section azimuth plane.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 94, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dls'), anglePerLengthMeasure, scope=cs_trajectoryStation, documentation=u'Dogleg severity.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 99, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rateTurn'), anglePerLengthMeasure, scope=cs_trajectoryStation, documentation=u'Turn rate, radius of curvature computation.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 104, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rateBuild'), anglePerLengthMeasure, scope=cs_trajectoryStation, documentation=u'Build Rate, radius of curvature computation.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 109, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mdDelta'), measuredDepthCoord, scope=cs_trajectoryStation, documentation=u'Delta measured depth from previous station.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 114, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tvdDelta'), wellVerticalDepthCoord, scope=cs_trajectoryStation, documentation=u'Delta true vertical depth from previous station.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 119, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'modelToolError'), commentString, scope=cs_trajectoryStation, documentation=u'Tool error model used to compute covariance matrix.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 124, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gravTotalUncert'), accelerationLinearMeasure, scope=cs_trajectoryStation, documentation=u'Survey tool gravity uncertainty.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 129, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dipAngleUncert'), planeAngleMeasure, scope=cs_trajectoryStation, documentation=u'Survey tool dip uncertainty.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 134, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magTotalUncert'), magneticInductionMeasure, scope=cs_trajectoryStation, documentation=u'Survey tool magnetic uncertainty.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 139, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gravAccelCorUsed'), logicalBoolean, scope=cs_trajectoryStation, documentation=u'Was an accelerometer alignment correction applied to survey computation?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").\n\t\t\t\t\t', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 144, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magXAxialCorUsed'), logicalBoolean, scope=cs_trajectoryStation, documentation=u'Was a magnetometer alignment correction applied to survey computation?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 151, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sagCorUsed'), logicalBoolean, scope=cs_trajectoryStation, documentation=u'Was a bottom hole assembly sag correction applied to the survey computation?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 157, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magDrlstrCorUsed'), logicalBoolean, scope=cs_trajectoryStation, documentation=u'Was a drillstring magnetism correction applied to survey computation?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 163, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gravTotalFieldReference'), accelerationLinearMeasure, scope=cs_trajectoryStation, documentation=u'Gravitational field theoretical/reference value.\n\t\t\t\t\t', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 169, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magTotalFieldReference'), magneticInductionMeasure, scope=cs_trajectoryStation, documentation=u'Geomagnetic field theoretical/reference value.\n\t\t\t\t\t', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 175, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magDipAngleReference'), planeAngleMeasure, scope=cs_trajectoryStation, documentation=u'Magnetic dip angle theoretical/reference value.\n\t\t\t\t\t', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 181, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magModelUsed'), nameString, scope=cs_trajectoryStation, documentation=u'Geomagnetic model used.\n\t\t\t\t\t', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 187, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magModelValid'), nameString, scope=cs_trajectoryStation, documentation=u'Current valid interval for the geomagnetic model used.\n\t\t\t\t\t', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 193, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'geoModelUsed'), nameString, scope=cs_trajectoryStation, documentation=u'Gravitational model used.\n\t\t\t\t\t', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 199, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'statusTrajStation'), TrajStationStatus, scope=cs_trajectoryStation, documentation=u'Status of the station.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 205, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rawData'), cs_stnTrajRawData, scope=cs_trajectoryStation, documentation=u'Applies only to measured magnetic stations.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 210, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'corUsed'), cs_stnTrajCorUsed, scope=cs_trajectoryStation, documentation=u'Applies only to measured magnetic stations.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 215, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'valid'), cs_stnTrajValid, scope=cs_trajectoryStation, documentation=u'Applies only to measured magnetic stations.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 220, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'matrixCov'), cs_stnTrajMatrixCov, scope=cs_trajectoryStation, documentation=u'Covariance matrix for error model.  ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 225, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'location'), cs_location, scope=cs_trajectoryStation, documentation=u'The 2D coordinates of the item. \n\t\t\t\t\tNote that within the context of trajectory, the "original" coordinates are\n\t\t\t\t\tinherently local coordinates as defined above.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 230, 3)))

cs_trajectoryStation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sourceStation'), cs_refWellboreTrajectoryStation, scope=cs_trajectoryStation, documentation=u'A pointer to the trajectoryStation from which this station was derived.\n\t\t\t\t\tThe trajectoryStation may be in another wellbore.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 237, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_trajectoryStation.xsd', 25, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_trajectoryStation.xsd', 30, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 28, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 33, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 43, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 53, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 58, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 63, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 68, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 73, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 78, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 86, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 94, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 99, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 104, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 109, 3))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 114, 3))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 119, 3))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 124, 3))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 129, 3))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 134, 3))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 139, 3))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 144, 3))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 151, 3))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 157, 3))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 163, 3))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 169, 3))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 175, 3))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 181, 3))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 187, 3))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 193, 3))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 199, 3))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 205, 3))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 210, 3))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 215, 3))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 220, 3))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 225, 3))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 230, 3))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 237, 3))
    counters.add(cc_38)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'commonData')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\cs_trajectoryStation.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'target')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 28, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dTimStn')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 33, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'typeTrajStation')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 38, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'typeSurveyTool')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'md')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 48, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tvd')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 53, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'incl')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 58, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'azi')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 63, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mtf')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 68, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gtf')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 73, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dispNs')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 78, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dispEw')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 86, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'vertSect')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 94, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dls')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 99, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rateTurn')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 104, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rateBuild')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 109, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mdDelta')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 114, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tvdDelta')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 119, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'modelToolError')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 124, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gravTotalUncert')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 129, 3))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dipAngleUncert')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 134, 3))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magTotalUncert')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 139, 3))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gravAccelCorUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 144, 3))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magXAxialCorUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 151, 3))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sagCorUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 157, 3))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magDrlstrCorUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 163, 3))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gravTotalFieldReference')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 169, 3))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magTotalFieldReference')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 175, 3))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magDipAngleReference')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 181, 3))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magModelUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 187, 3))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magModelValid')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 193, 3))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'geoModelUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 199, 3))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'statusTrajStation')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 205, 3))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rawData')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 210, 3))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'corUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 215, 3))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'valid')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 220, 3))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'matrixCov')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 225, 3))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'location')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 230, 3))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(cs_trajectoryStation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sourceStation')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectoryStation.xsd', 237, 3))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
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
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
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
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
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
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
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
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
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
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
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
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
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
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
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
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
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
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
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
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
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
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
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
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
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
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
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
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
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
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
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
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False) ]))
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
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
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
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False) ]))
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
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
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
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, False) ]))
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
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, False) ]))
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
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, False) ]))
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
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, False) ]))
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
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_32, False) ]))
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
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_38, True) ]))
    st_39._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_trajectoryStation._Automaton = _BuildAutomaton_15()




obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'objectGrowing'), logicalBoolean, scope=obj_trajectory, documentation=u'Whether or not the trajectory is growing. \n\t\t\t\t\tTrue ("true" or "1") indicates the that the trajectory is still growing \n\t\t\t\t\tin size (that is, trajectoryStation values are still being added).\n\t\t\t\t\tFor example, it may be connected to a realtime stream.\n\t\t\t\t\tFalse ("false" or "0") indicates that the trajectory is \n\t\t\t\t\tclosed (that is, no further trajectoryStation values will be added).\n\t\t\t\t\tNot given indicates that the status of the trajectory is not known.\n\t\t\t\t\tThis value is only relevant within the context of a server.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 24, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'parentTrajectory'), cs_refWellboreTrajectory, scope=obj_trajectory, documentation=u'If a trajectory is tied into another trajectory, \n\t\t\t\t\ta pointer to the parent trajectory.  \n\t\t\t\t\tThe trajectory may be in another wellbore.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 36, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dTimTrajStart'), timestamp, scope=obj_trajectory, documentation=u'Start date and time of trajectory station measurements.\n\t\t\t\t\tNote that this is NOT a server query parameter.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 43, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dTimTrajEnd'), timestamp, scope=obj_trajectory, documentation=u'End date and time of trajectory station measurements.\n\t\t\t\t\tNote that this is NOT a server query parameter.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 49, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mdMn'), measuredDepthCoord, scope=obj_trajectory, documentation=u"Minimum measured depth of trajectory.\n\t\t\t\t\tThis is a query parameter. It's value will be populated by the server\n\t\t\t\t\tto reflect the values of md in the returned trajectoryStations.", location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 55, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mdMx'), measuredDepthCoord, scope=obj_trajectory, documentation=u"Maximum measured depth of trajectory.\n\t\t\t\t\tThis is a query parameter. It's value will be populated by the server\n\t\t\t\t\tto reflect the values of md in the returned trajectoryStations.", location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 62, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serviceCompany'), nameString, scope=obj_trajectory, documentation=u'Name of contractor who provided the service.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 69, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'magDeclUsed'), planeAngleMeasure, scope=obj_trajectory, documentation=u'Magnetic declination used to correct a magnetic survey. \n\t\t\t\t\tStarting value if stations have individual values. ', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 74, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gridCorUsed'), planeAngleMeasure, scope=obj_trajectory, documentation=u'Grid correction used to correct a survey. \n\t\t\t\t\tStarting value if stations have individual values.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 80, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'aziVertSect'), planeAngleMeasure, scope=obj_trajectory, documentation=u'Azimuth used for vertical section plot/computations.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 86, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dispNsVertSectOrig'), lengthMeasure, scope=obj_trajectory, documentation=u'Origin north-south used for vertical section plot/computations.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 91, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dispEwVertSectOrig'), lengthMeasure, scope=obj_trajectory, documentation=u'Origin east-west used for vertical section plot/computations.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 96, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'definitive'), logicalBoolean, scope=obj_trajectory, documentation=u'True ("true" or "1") indicates that this trajectory is definitive for \n\t\t\t\t\tthis wellbore. False ("false" or "0") or not given indicates otherwise.\n\t\t\t\t\tThere can only be one trajectory per wellbore with definitive=true and it\n\t\t\t\t\tmust define the geometry of the whole wellbore (surface to bottom).\n\t\t\t\t\tThe definitive trajectory may represent a composite of information in many\n\t\t\t\t\tother trajectories. A query requesting a subset of the possible information can\n\t\t\t\t\tprovide a simplistic view of the geometry of the wellbore.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 101, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'memory'), logicalBoolean, scope=obj_trajectory, documentation=u'Is trajectory a result of a memory dump from a tool?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 112, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'finalTraj'), logicalBoolean, scope=obj_trajectory, documentation=u'Is trajectory a final or intermediate/preliminary?  \n\t\t\t\t\tValues are "true" (or "1") and "false" (or "0").', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 118, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'aziRef'), AziRef, scope=obj_trajectory, documentation=u'Specifies the definition of north.\n\t\t\t\t\tWhile this is optional because of legacy data, it is strongly recommended \n\t\t\t\t\tthat this always be specified.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 124, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trajectoryStation'), cs_trajectoryStation, scope=obj_trajectory, documentation=u'Container element for trajectory station elements.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 131, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameWell'), nameString, scope=obj_trajectory, documentation=u'Human recognizable context for the well that contains the wellbore.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 58, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameWellbore'), nameString, scope=obj_trajectory, documentation=u'Human recognizable context for the wellbore that contains the trajectory.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 63, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), nameString, scope=obj_trajectory, documentation=u'Human recognizable context for the trajectory.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 68, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'commonData'), cs_commonData, scope=obj_trajectory, documentation=u'A container element that contains elements that are common to all data \n\t\t\t\t\tobjects.  ', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 78, 3)))

obj_trajectory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customData'), cs_customData, scope=obj_trajectory, documentation=u'A container element that can contain custom or user defined \n\t\t\t\t\tdata elements.', location=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 84, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 24, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 36, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 43, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 49, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 55, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 62, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 69, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 74, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 80, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 86, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 91, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 96, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 101, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 112, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 118, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 124, 3))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 131, 3))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 73, 3))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 78, 3))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 84, 3))
    counters.add(cc_19)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'objectGrowing')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'parentTrajectory')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 36, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dTimTrajStart')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 43, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dTimTrajEnd')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 49, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mdMn')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 55, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mdMx')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 62, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceCompany')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 69, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'magDeclUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 74, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gridCorUsed')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 80, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'aziVertSect')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 86, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dispNsVertSectOrig')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 91, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dispEwVertSectOrig')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 96, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'definitive')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 101, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'memory')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 112, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'finalTraj')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 118, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'aziRef')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 124, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trajectoryStation')), pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\grp_trajectory.xsd', 131, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameWell')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 58, 3))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameWellbore')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 63, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 68, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'commonData')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 78, 3))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(obj_trajectory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customData')), pyxb.utils.utility.Location('o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.3.1.1_Data_Schema\\obj_trajectory.xsd', 84, 3))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False),
        fac.UpdateInstruction(cc_17, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
         ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
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
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    st_21._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
obj_trajectory._Automaton = _BuildAutomaton_16()

