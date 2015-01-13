# .\witsml1411_obj_message.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:bff9e1cadb696f69d77e8e135b7b2cb67426d3a5
# Generated 2013-03-20 17:54:01.535000 by PyXB version 1.2.1
# Namespace http://www.witsml.org/schemas/1series

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0db71f40-91b1-11e2-a997-08002712d133')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _abs

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.witsml.org/schemas/1series', create_if_missing=True)
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


# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractBoolean
class abstractBoolean (pyxb.binding.datatypes.boolean):

    """This type disallows an "empty" boolean value.
			This type should not be used directly except to derive another type.
			All boolean types should be derived from this type rather than using xsd:boolen."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractBoolean')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 24, 1)
    _Documentation = u'This type disallows an "empty" boolean value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll boolean types should be derived from this type rather than using xsd:boolen.'
abstractBoolean._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractBoolean._CF_pattern.addPattern(pattern=u'.+')
abstractBoolean._InitializeFacetMap(abstractBoolean._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractBoolean', abstractBoolean)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractDateTime
class abstractDateTime (pyxb.binding.datatypes.dateTime):

    """This type disallows an "empty" dateTime value.
			This type should not be used directly except to derive another type.
			All dateTime types should be derived from this type rather than using xsd:dateTime."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractDateTime')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 35, 1)
    _Documentation = u'This type disallows an "empty" dateTime value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll dateTime types should be derived from this type rather than using xsd:dateTime.'
abstractDateTime._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDateTime._CF_pattern.addPattern(pattern=u'.+')
abstractDateTime._InitializeFacetMap(abstractDateTime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractDateTime', abstractDateTime)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractDate
class abstractDate (pyxb.binding.datatypes.date):

    """This type disallows an "empty" date value.
			This type should not be used directly except to derive another type.
			All dateTime types should be derived from this type rather than using xsd:dateTime."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractDate')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 46, 1)
    _Documentation = u'This type disallows an "empty" date value.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tAll dateTime types should be derived from this type rather than using xsd:dateTime.'
abstractDate._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDate._CF_pattern.addPattern(pattern=u'.+')
abstractDate._InitializeFacetMap(abstractDate._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractDate', abstractDate)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractDouble
class abstractDouble (pyxb.binding.datatypes.double):

    """This type disallows an "empty" double value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractDouble')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 57, 1)
    _Documentation = u'This type disallows an "empty" double value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractDouble._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractDouble._CF_pattern.addPattern(pattern=u'.+')
abstractDouble._InitializeFacetMap(abstractDouble._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractDouble', abstractDouble)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractShort
class abstractShort (pyxb.binding.datatypes.short):

    """This type disallows an "empty" short value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractShort')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 67, 1)
    _Documentation = u'This type disallows an "empty" short value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractShort._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractShort._CF_pattern.addPattern(pattern=u'.+')
abstractShort._InitializeFacetMap(abstractShort._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractShort', abstractShort)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractInt
class abstractInt (pyxb.binding.datatypes.int):

    """This type disallows an "empty" int value.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractInt')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 77, 1)
    _Documentation = u'This type disallows an "empty" int value.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractInt._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractInt._CF_pattern.addPattern(pattern=u'.+')
abstractInt._InitializeFacetMap(abstractInt._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractInt', abstractInt)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractString
class abstractString (pyxb.binding.datatypes.string):

    """The intended abstract supertype of all strings.
			This abstract type allows the control over whitespace for all strings to be defined at a high level. 
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 87, 1)
    _Documentation = u'The intended abstract supertype of all strings.\n\t\t\tThis abstract type allows the control over whitespace for all strings to be defined at a high level. \n\t\t\tThis type should not be used directly except to derive another type.'
abstractString._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
abstractString._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
abstractString._InitializeFacetMap(abstractString._CF_whiteSpace,
   abstractString._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'abstractString', abstractString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractUncollapsedString
class abstractUncollapsedString (pyxb.binding.datatypes.string):

    """The intended abstract supertype of all strings that must maintain whitespace. 
			The type abstractString should normally be used.
			This type should not be used directly except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractUncollapsedString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 138, 1)
    _Documentation = u'The intended abstract supertype of all strings that must maintain whitespace. \n\t\t\tThe type abstractString should normally be used.\n\t\t\tThis type should not be used directly except to derive another type.'
abstractUncollapsedString._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
abstractUncollapsedString._InitializeFacetMap(abstractUncollapsedString._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'abstractUncollapsedString', abstractUncollapsedString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractMaximumLengthString
class abstractMaximumLengthString (abstractString):

    """This defines the maximum acceptable length of a
			string that can be stored in a data base."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractMaximumLengthString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 122, 1)
    _Documentation = u'This defines the maximum acceptable length of a\n\t\t\tstring that can be stored in a data base.'
abstractMaximumLengthString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4000L))
abstractMaximumLengthString._InitializeFacetMap(abstractMaximumLengthString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'abstractMaximumLengthString', abstractMaximumLengthString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractPositiveCount
class abstractPositiveCount (abstractShort):

    """A positive integer (one based count or index) with a maximum value of 32767 (2-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractPositiveCount')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 155, 1)
    _Documentation = u'A positive integer (one based count or index) with a maximum value of 32767 (2-bytes).'
abstractPositiveCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=abstractPositiveCount, value=pyxb.binding.datatypes.short(1))
abstractPositiveCount._InitializeFacetMap(abstractPositiveCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'abstractPositiveCount', abstractPositiveCount)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractTimeZone
class abstractTimeZone (abstractString):

    """A time zone conforming to the XSD:dateTime specification.
			It should be of the form "Z" or "shh.mm" where 
				"s" is "+" or "-", 
				"hh" is 00 to 23 and
				"mm" is 00 to 59."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractTimeZone')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 170, 1)
    _Documentation = u'A time zone conforming to the XSD:dateTime specification.\n\t\t\tIt should be of the form "Z" or "shh.mm" where \n\t\t\t\t"s" is "+" or "-", \n\t\t\t\t"hh" is 00 to 23 and\n\t\t\t\t"mm" is 00 to 59.'
abstractTimeZone._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractTimeZone._CF_pattern.addPattern(pattern=u'[Z]|([\\-+](([01][0-9])|(2[0-3])):[0-5][0-9])')
abstractTimeZone._InitializeFacetMap(abstractTimeZone._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractTimeZone', abstractTimeZone)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractNameString
class abstractNameString (abstractString):

    """The intended abstract supertype of all user assigned human 
			recognizable contextual name types. 
			There should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.
			This type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractNameString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 184, 1)
    _Documentation = u'The intended abstract supertype of all user assigned human \n\t\t\trecognizable contextual name types. \n\t\t\tThere should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.\n\t\t\tThis type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration.'
abstractNameString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
abstractNameString._InitializeFacetMap(abstractNameString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'abstractNameString', abstractNameString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractUidString
class abstractUidString (abstractString):

    """The intended abstract supertype of all locally unique identifiers. 
			The value is not intended to convey any semantic content (e.g., it may be computer generated). 
			The value is only required to be unique within a context in a document (e.g., defined via key and keyref). 
			There is no guarantee that the same data in multiple documents will utilize the same uid value 
			unless enforced by the source of the document (e.g., a document server).
			Spaces are not allowed."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractUidString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 196, 1)
    _Documentation = u'The intended abstract supertype of all locally unique identifiers. \n\t\t\tThe value is not intended to convey any semantic content (e.g., it may be computer generated). \n\t\t\tThe value is only required to be unique within a context in a document (e.g., defined via key and keyref). \n\t\t\tThere is no guarantee that the same data in multiple documents will utilize the same uid value \n\t\t\tunless enforced by the source of the document (e.g., a document server).\n\t\t\tSpaces are not allowed.'
abstractUidString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
abstractUidString._CF_pattern = pyxb.binding.facets.CF_pattern()
abstractUidString._CF_pattern.addPattern(pattern=u'[^ ]*')
abstractUidString._InitializeFacetMap(abstractUidString._CF_maxLength,
   abstractUidString._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'abstractUidString', abstractUidString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractDescriptionString
class abstractDescriptionString (abstractString):

    """A textual description of something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractDescriptionString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 222, 1)
    _Documentation = u'A textual description of something.'
abstractDescriptionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256L))
abstractDescriptionString._InitializeFacetMap(abstractDescriptionString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'abstractDescriptionString', abstractDescriptionString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractString32
class abstractString32 (abstractString):

    """A 32 character string."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractString32')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 232, 1)
    _Documentation = u'A 32 character string.'
abstractString32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32L))
abstractString32._InitializeFacetMap(abstractString32._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'abstractString32', abstractString32)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractTypeEnum
class abstractTypeEnum (abstractString):

    """The intended abstract supertype of all enumerated "types".
			This abstract type allows the maximum length of a type enumeration to be centrally defined.
			This type should not be used directly except to derive another type.
			It should also be used for uncontrolled strings which are candidates to become enumerations at a future date."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 242, 1)
    _Documentation = u'The intended abstract supertype of all enumerated "types".\n\t\t\tThis abstract type allows the maximum length of a type enumeration to be centrally defined.\n\t\t\tThis type should not be used directly except to derive another type.\n\t\t\tIt should also be used for uncontrolled strings which are candidates to become enumerations at a future date.'
abstractTypeEnum._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40L))
abstractTypeEnum._InitializeFacetMap(abstractTypeEnum._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'abstractTypeEnum', abstractTypeEnum)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractUomEnum
class abstractUomEnum (abstractString):

    """The intended abstract supertype of all "units of measure".
			This abstract type allows the maximum length of a UOM enumeration to be centrally defined. 
			This type is abstract in the sense that it should not be used directly 
			except to derive another type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractUomEnum')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 254, 1)
    _Documentation = u'The intended abstract supertype of all "units of measure".\n\t\t\tThis abstract type allows the maximum length of a UOM enumeration to be centrally defined. \n\t\t\tThis type is abstract in the sense that it should not be used directly \n\t\t\texcept to derive another type.'
abstractUomEnum._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(24L))
abstractUomEnum._InitializeFacetMap(abstractUomEnum._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'abstractUomEnum', abstractUomEnum)

# Atomic simple type: {http://www.witsml.org/schemas/1series}date
class date (abstractDate):

    """A julian date."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'date')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 29, 1)
    _Documentation = u'A julian date.'
date._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'date', date)

# Atomic simple type: {http://www.witsml.org/schemas/1series}timestamp
class timestamp (abstractDateTime):

    """A date with a time of day and a mandatory time zone offset.
			This must captute the correct date-time relative to UTC. It is not necessary to 
			use a local time zone because software may convert the date-time to a different 
			local time zone (while retaining correct date-time relative to UTC).
			See acquisitionTmeZone in commonData for the original time zone of times in an object."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timestamp')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 36, 1)
    _Documentation = u'A date with a time of day and a mandatory time zone offset.\n\t\t\tThis must captute the correct date-time relative to UTC. It is not necessary to \n\t\t\tuse a local time zone because software may convert the date-time to a different \n\t\t\tlocal time zone (while retaining correct date-time relative to UTC).\n\t\t\tSee acquisitionTmeZone in commonData for the original time zone of times in an object.'
timestamp._CF_pattern = pyxb.binding.facets.CF_pattern()
timestamp._CF_pattern.addPattern(pattern=u'.+T.+[Z+\\-].*')
timestamp._InitializeFacetMap(timestamp._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'timestamp', timestamp)

# Atomic simple type: {http://www.witsml.org/schemas/1series}calendarYear
class calendarYear (abstractInt):

    """A calendar year (CCYY) in the gregorian calendar.
			This type is meant to captute original invariant values. 
			It is not intended to be used in "time math" where knowledge of the time zone is needed."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'calendarYear')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 79, 1)
    _Documentation = u'A calendar year (CCYY) in the gregorian calendar.\n\t\t\tThis type is meant to captute original invariant values. \n\t\t\tIt is not intended to be used in "time math" where knowledge of the time zone is needed.'
calendarYear._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=calendarYear, value=pyxb.binding.datatypes.int(9999))
calendarYear._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=calendarYear, value=pyxb.binding.datatypes.int(1000))
calendarYear._InitializeFacetMap(calendarYear._CF_maxInclusive,
   calendarYear._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'calendarYear', calendarYear)

# Atomic simple type: {http://www.witsml.org/schemas/1series}logicalBoolean
class logicalBoolean (abstractBoolean):

    """Values of "true" (or "1") and "false" (or "0")."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'logicalBoolean')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 95, 1)
    _Documentation = u'Values of "true" (or "1") and "false" (or "0").'
logicalBoolean._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'logicalBoolean', logicalBoolean)

# Atomic simple type: {http://www.witsml.org/schemas/1series}unitlessQuantity
class unitlessQuantity (abstractDouble):

    """A unitless quantity. This should not 
			be confused with a dimensionless measure."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unitlessQuantity')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 138, 1)
    _Documentation = u'A unitless quantity. This should not \n\t\t\tbe confused with a dimensionless measure.'
unitlessQuantity._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'unitlessQuantity', unitlessQuantity)

# Atomic simple type: {http://www.witsml.org/schemas/1series}shortDescriptionString
class shortDescriptionString (abstractString):

    """A short textual description of something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shortDescriptionString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 360, 1)
    _Documentation = u'A short textual description of something.'
shortDescriptionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64L))
shortDescriptionString._InitializeFacetMap(shortDescriptionString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'shortDescriptionString', shortDescriptionString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}schemaVersionString
class schemaVersionString (abstractString):

    """The version of the schema.
			The first level is fixed. The fourth level can vary
			to represent on the constraints defined in enumerations and 
			XML loader files. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'schemaVersionString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 426, 1)
    _Documentation = u'The version of the schema.\n\t\t\tThe first level is fixed. The fourth level can vary\n\t\t\tto represent on the constraints defined in enumerations and \n\t\t\tXML loader files. '
schemaVersionString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16L))
schemaVersionString._CF_pattern = pyxb.binding.facets.CF_pattern()
schemaVersionString._CF_pattern.addPattern(pattern=u'1\\.[4-9]\\.[0-9]\\.([0-9]|([1-9][0-9]))')
schemaVersionString._InitializeFacetMap(schemaVersionString._CF_maxLength,
   schemaVersionString._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'schemaVersionString', schemaVersionString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}uncollapsedString
class uncollapsedString (abstractUncollapsedString):

    """A textual string that retains all whitespace."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'uncollapsedString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 492, 1)
    _Documentation = u'A textual string that retains all whitespace.'
uncollapsedString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256L))
uncollapsedString._InitializeFacetMap(uncollapsedString._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'uncollapsedString', uncollapsedString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}iadcBearingWearCode
class iadcBearingWearCode (abstractString):

    """IADC bearing wear code: integer 0 - 8 or one of the letters E, F, N or X. ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'iadcBearingWearCode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 501, 1)
    _Documentation = u'IADC bearing wear code: integer 0 - 8 or one of the letters E, F, N or X. .'
iadcBearingWearCode._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
iadcBearingWearCode._CF_pattern = pyxb.binding.facets.CF_pattern()
iadcBearingWearCode._CF_pattern.addPattern(pattern=u'[0-8EFNX]')
iadcBearingWearCode._InitializeFacetMap(iadcBearingWearCode._CF_maxLength,
   iadcBearingWearCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'iadcBearingWearCode', iadcBearingWearCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}geodeticZoneString
class geodeticZoneString (abstractString):

    """A geodetic zone with values from 1 to 60 and a required direction 
			of "N" (North) or "S" (South). For example, "21N"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'geodeticZoneString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 511, 1)
    _Documentation = u'A geodetic zone with values from 1 to 60 and a required direction \n\t\t\tof "N" (North) or "S" (South). For example, "21N".'
geodeticZoneString._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
geodeticZoneString._CF_pattern = pyxb.binding.facets.CF_pattern()
geodeticZoneString._CF_pattern.addPattern(pattern=u'([1-9]|[1-5][0-9]|60)[NS]')
geodeticZoneString._InitializeFacetMap(geodeticZoneString._CF_maxLength,
   geodeticZoneString._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'geodeticZoneString', geodeticZoneString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}sectionNumber
class sectionNumber (abstractString):

    """Sections are numbered "1" through "36." 
			Irregular sections may be designated with a single value after a decimal point.
			USA Public Land Survey System."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sectionNumber')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 657, 1)
    _Documentation = u'Sections are numbered "1" through "36." \n\t\t\tIrregular sections may be designated with a single value after a decimal point.\n\t\t\tUSA Public Land Survey System.'
sectionNumber._CF_pattern = pyxb.binding.facets.CF_pattern()
sectionNumber._CF_pattern.addPattern(pattern=u'[+]?([1-9]|[1-2][0-9]|3[0-6])\\.?[0-9]?')
sectionNumber._InitializeFacetMap(sectionNumber._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'sectionNumber', sectionNumber)

# Atomic simple type: {http://www.witsml.org/schemas/1series}publicLandSurveySystemQuarterTownship
class publicLandSurveySystemQuarterTownship (abstractString):

    """Designates a particular quarter of a township.
			USA Public Land Survey System."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'publicLandSurveySystemQuarterTownship')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 669, 1)
    _Documentation = u'Designates a particular quarter of a township.\n\t\t\tUSA Public Land Survey System.'
publicLandSurveySystemQuarterTownship._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12L))
publicLandSurveySystemQuarterTownship._CF_pattern = pyxb.binding.facets.CF_pattern()
publicLandSurveySystemQuarterTownship._CF_pattern.addPattern(pattern=u'NE|NW|SW|SE')
publicLandSurveySystemQuarterTownship._InitializeFacetMap(publicLandSurveySystemQuarterTownship._CF_maxLength,
   publicLandSurveySystemQuarterTownship._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'publicLandSurveySystemQuarterTownship', publicLandSurveySystemQuarterTownship)

# Atomic simple type: {http://www.witsml.org/schemas/1series}publicLandSurveySystemQuarterSection
class publicLandSurveySystemQuarterSection (abstractString):

    """Some combination of NE,NW,SW,SE,N2,S2,E2,W2,C,TRxx,LTnn.
			USA Public Land Survey System."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'publicLandSurveySystemQuarterSection')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 681, 1)
    _Documentation = u'Some combination of NE,NW,SW,SE,N2,S2,E2,W2,C,TRxx,LTnn.\n\t\t\tUSA Public Land Survey System.'
publicLandSurveySystemQuarterSection._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12L))
publicLandSurveySystemQuarterSection._CF_pattern = pyxb.binding.facets.CF_pattern()
publicLandSurveySystemQuarterSection._CF_pattern.addPattern(pattern=u'(NE|NW|SW|SE|N2|S2|E2|W2|C|LT[0-9]{2,2}|TR[a-zA-Z0-9]{1,2}){1,3}')
publicLandSurveySystemQuarterSection._InitializeFacetMap(publicLandSurveySystemQuarterSection._CF_maxLength,
   publicLandSurveySystemQuarterSection._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'publicLandSurveySystemQuarterSection', publicLandSurveySystemQuarterSection)

# Atomic simple type: {http://www.witsml.org/schemas/1series}gtZeroAndLeOne
class gtZeroAndLeOne (abstractDouble):

    """A floating point value which is greater than zero and 
			less than or equal to one."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'gtZeroAndLeOne')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 741, 1)
    _Documentation = u'A floating point value which is greater than zero and \n\t\t\tless than or equal to one.'
gtZeroAndLeOne._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=gtZeroAndLeOne, value=pyxb.binding.datatypes.double(1.0))
gtZeroAndLeOne._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=abstractDouble, value=pyxb.binding.datatypes.anySimpleType(u'0'))
gtZeroAndLeOne._InitializeFacetMap(gtZeroAndLeOne._CF_maxInclusive,
   gtZeroAndLeOne._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', u'gtZeroAndLeOne', gtZeroAndLeOne)

# Atomic simple type: {http://www.witsml.org/schemas/1series}nonNegativeCount
class nonNegativeCount (abstractShort):

    """A non-negative integer (zero based count or index) with a maximum value of 32767 (2-bytes).
			For items that represent "number of" something or a "sequential" count or index."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nonNegativeCount')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 752, 1)
    _Documentation = u'A non-negative integer (zero based count or index) with a maximum value of 32767 (2-bytes).\n\t\t\tFor items that represent "number of" something or a "sequential" count or index.'
nonNegativeCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=nonNegativeCount, value=pyxb.binding.datatypes.short(0))
nonNegativeCount._InitializeFacetMap(nonNegativeCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'nonNegativeCount', nonNegativeCount)

# Atomic simple type: {http://www.witsml.org/schemas/1series}positiveBigCount
class positiveBigCount (abstractInt):

    """A large positive integer (one based count or index) with a maximum value of 2,147,483,647 (4-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positiveBigCount')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 779, 1)
    _Documentation = u'A large positive integer (one based count or index) with a maximum value of 2,147,483,647 (4-bytes).'
positiveBigCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveBigCount, value=pyxb.binding.datatypes.int(1))
positiveBigCount._InitializeFacetMap(positiveBigCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'positiveBigCount', positiveBigCount)

# Atomic simple type: {http://www.witsml.org/schemas/1series}integerCount
class integerCount (abstractInt):

    """A positive or negative count with a maximum positive value of 2147483647 (4-bytes)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'integerCount')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 792, 1)
    _Documentation = u'A positive or negative count with a maximum positive value of 2147483647 (4-bytes).'
integerCount._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'integerCount', integerCount)

# Atomic simple type: {http://www.witsml.org/schemas/1series}beaufortScaleIntegerCode
class beaufortScaleIntegerCode (abstractShort):

    """An estimate wind strength based on the Beaufort Wind Scale. 
			Values range from 0 (calm) to 12 (hurricane). """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'beaufortScaleIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 799, 1)
    _Documentation = u'An estimate wind strength based on the Beaufort Wind Scale. \n\t\t\tValues range from 0 (calm) to 12 (hurricane). '
beaufortScaleIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=beaufortScaleIntegerCode, value=pyxb.binding.datatypes.short(12))
beaufortScaleIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=beaufortScaleIntegerCode, value=pyxb.binding.datatypes.short(0))
beaufortScaleIntegerCode._InitializeFacetMap(beaufortScaleIntegerCode._CF_maxInclusive,
   beaufortScaleIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'beaufortScaleIntegerCode', beaufortScaleIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}pumpActionIntegerCode
class pumpActionIntegerCode (abstractShort):

    """Pump Action: 1 = Single acting, 2 = double acting."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pumpActionIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 810, 1)
    _Documentation = u'Pump Action: 1 = Single acting, 2 = double acting.'
pumpActionIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=pumpActionIntegerCode, value=pyxb.binding.datatypes.short(2))
pumpActionIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=pumpActionIntegerCode, value=pyxb.binding.datatypes.short(1))
pumpActionIntegerCode._InitializeFacetMap(pumpActionIntegerCode._CF_maxInclusive,
   pumpActionIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'pumpActionIntegerCode', pumpActionIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}iadcIntegerCode
class iadcIntegerCode (abstractShort):

    """IADC codes: 0 to 8."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'iadcIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 820, 1)
    _Documentation = u'IADC codes: 0 to 8.'
iadcIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=iadcIntegerCode, value=pyxb.binding.datatypes.short(8))
iadcIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=iadcIntegerCode, value=pyxb.binding.datatypes.short(0))
iadcIntegerCode._InitializeFacetMap(iadcIntegerCode._CF_maxInclusive,
   iadcIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'iadcIntegerCode', iadcIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}levelIntegerCode
class levelIntegerCode (abstractShort):

    """Integer level code from 1 through 5."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'levelIntegerCode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 830, 1)
    _Documentation = u'Integer level code from 1 through 5.'
levelIntegerCode._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=levelIntegerCode, value=pyxb.binding.datatypes.short(8))
levelIntegerCode._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=levelIntegerCode, value=pyxb.binding.datatypes.short(0))
levelIntegerCode._InitializeFacetMap(levelIntegerCode._CF_maxInclusive,
   levelIntegerCode._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'levelIntegerCode', levelIntegerCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}str2
class str2 (abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'str2')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 878, 1)
    _Documentation = ''
str2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
str2._InitializeFacetMap(str2._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'str2', str2)

# Atomic simple type: {http://www.witsml.org/schemas/1series}str16
class str16 (abstractString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'str16')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 887, 1)
    _Documentation = ''
str16._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16L))
str16._InitializeFacetMap(str16._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'str16', str16)

# Atomic simple type: {http://www.witsml.org/schemas/1series}abstractCommentString
class abstractCommentString (abstractMaximumLengthString):

    """The intended abstract supertype of all comments or remarks 
			intended for human consumption. 
			There should be no assumption that semantics can be extracted from the field by a computer. 
			Neither should there be an assumption that any two humans will interpret the information 
			in the same way (i.e., it may not be interoperable)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractCommentString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 211, 1)
    _Documentation = u'The intended abstract supertype of all comments or remarks \n\t\t\tintended for human consumption. \n\t\t\tThere should be no assumption that semantics can be extracted from the field by a computer. \n\t\t\tNeither should there be an assumption that any two humans will interpret the information \n\t\t\tin the same way (i.e., it may not be interoperable).'
abstractCommentString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'abstractCommentString', abstractCommentString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ActivityClassType
class ActivityClassType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ActivityClassType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 26, 1)
    _Documentation = None
ActivityClassType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ActivityClassType, enum_prefix=None)
ActivityClassType.planned = ActivityClassType._CF_enumeration.addEnumeration(unicode_value=u'planned', tag=u'planned')
ActivityClassType.unplanned = ActivityClassType._CF_enumeration.addEnumeration(unicode_value=u'unplanned', tag=u'unplanned')
ActivityClassType.downtime = ActivityClassType._CF_enumeration.addEnumeration(unicode_value=u'downtime', tag=u'downtime')
ActivityClassType.unknown = ActivityClassType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ActivityClassType._InitializeFacetMap(ActivityClassType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ActivityClassType', ActivityClassType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ActivityCode
class ActivityCode (abstractTypeEnum):

    """Activity codes.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ActivityCode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 53, 1)
    _Documentation = u'Activity codes.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
ActivityCode._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ActivityCode', ActivityCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AuthorizationStatus
class AuthorizationStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AuthorizationStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 62, 1)
    _Documentation = ''
AuthorizationStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AuthorizationStatus, enum_prefix=None)
AuthorizationStatus.draft = AuthorizationStatus._CF_enumeration.addEnumeration(unicode_value=u'draft', tag=u'draft')
AuthorizationStatus.authorized = AuthorizationStatus._CF_enumeration.addEnumeration(unicode_value=u'authorized', tag=u'authorized')
AuthorizationStatus.superceded = AuthorizationStatus._CF_enumeration.addEnumeration(unicode_value=u'superceded', tag=u'superceded')
AuthorizationStatus.withdrawn = AuthorizationStatus._CF_enumeration.addEnumeration(unicode_value=u'withdrawn', tag=u'withdrawn')
AuthorizationStatus.unknown = AuthorizationStatus._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
AuthorizationStatus._InitializeFacetMap(AuthorizationStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AuthorizationStatus', AuthorizationStatus)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AziRef
class AziRef (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AziRef')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 97, 1)
    _Documentation = None
AziRef._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AziRef, enum_prefix=None)
AziRef.magnetic_north = AziRef._CF_enumeration.addEnumeration(unicode_value=u'magnetic north', tag=u'magnetic_north')
AziRef.grid_north = AziRef._CF_enumeration.addEnumeration(unicode_value=u'grid north', tag=u'grid_north')
AziRef.true_north = AziRef._CF_enumeration.addEnumeration(unicode_value=u'true north', tag=u'true_north')
AziRef.unknown = AziRef._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
AziRef._InitializeFacetMap(AziRef._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AziRef', AziRef)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BearingType
class BearingType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BearingType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 129, 1)
    _Documentation = None
BearingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BearingType, enum_prefix=None)
BearingType.oil_seal = BearingType._CF_enumeration.addEnumeration(unicode_value=u'oil seal', tag=u'oil_seal')
BearingType.mud_lube = BearingType._CF_enumeration.addEnumeration(unicode_value=u'mud lube', tag=u'mud_lube')
BearingType.other = BearingType._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
BearingType.unknown = BearingType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BearingType._InitializeFacetMap(BearingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BearingType', BearingType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BitDullCode
class BitDullCode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent a classification of a drill bit based 
			on its reason for being declared inoperable, as originally defined by the IADC."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BitDullCode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 156, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}BitReasonPulled
class BitReasonPulled (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the reason for pulling a drill bit 
			from the wellbore, as originally defined by the IADC."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BitReasonPulled')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 302, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}BitType
class BitType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drill/core bit."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BitType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 408, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}BhaStatus
class BhaStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BhaStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 453, 1)
    _Documentation = None
BhaStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BhaStatus, enum_prefix=None)
BhaStatus.final = BhaStatus._CF_enumeration.addEnumeration(unicode_value=u'final', tag=u'final')
BhaStatus.progress = BhaStatus._CF_enumeration.addEnumeration(unicode_value=u'progress', tag=u'progress')
BhaStatus.plan = BhaStatus._CF_enumeration.addEnumeration(unicode_value=u'plan', tag=u'plan')
BhaStatus.unknown = BhaStatus._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BhaStatus._InitializeFacetMap(BhaStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BhaStatus', BhaStatus)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BladeShapeType
class BladeShapeType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BladeShapeType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 480, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}BladeType
class BladeType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BladeType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 517, 1)
    _Documentation = None
BladeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BladeType, enum_prefix=None)
BladeType.clamp_on = BladeType._CF_enumeration.addEnumeration(unicode_value=u'clamp-on', tag=u'clamp_on')
BladeType.integral = BladeType._CF_enumeration.addEnumeration(unicode_value=u'integral', tag=u'integral')
BladeType.sleeve = BladeType._CF_enumeration.addEnumeration(unicode_value=u'sleeve', tag=u'sleeve')
BladeType.welded = BladeType._CF_enumeration.addEnumeration(unicode_value=u'welded', tag=u'welded')
BladeType.unknown = BladeType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BladeType._InitializeFacetMap(BladeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BladeType', BladeType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}BopType
class BopType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BopType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 549, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}BoxPinConfig
class BoxPinConfig (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of Box/Pin configuration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BoxPinConfig')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 596, 1)
    _Documentation = u'These values represent the type of Box/Pin configuration.'
BoxPinConfig._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BoxPinConfig, enum_prefix=None)
BoxPinConfig.bottom_box_top_box = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value=u'bottom box, top box', tag=u'bottom_box_top_box')
BoxPinConfig.bottom_box_top_pin = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value=u'bottom box, top pin', tag=u'bottom_box_top_pin')
BoxPinConfig.bottom_pin_top_box = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value=u'bottom pin top box', tag=u'bottom_pin_top_box')
BoxPinConfig.bottom_pin = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value=u'bottom pin', tag=u'bottom_pin')
BoxPinConfig.unknown = BoxPinConfig._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
BoxPinConfig._InitializeFacetMap(BoxPinConfig._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BoxPinConfig', BoxPinConfig)

# Atomic simple type: {http://www.witsml.org/schemas/1series}CementJobType
class CementJobType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CementJobType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 631, 1)
    _Documentation = None
CementJobType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CementJobType, enum_prefix=None)
CementJobType.primary = CementJobType._CF_enumeration.addEnumeration(unicode_value=u'primary', tag=u'primary')
CementJobType.plug = CementJobType._CF_enumeration.addEnumeration(unicode_value=u'plug', tag=u'plug')
CementJobType.squeeze = CementJobType._CF_enumeration.addEnumeration(unicode_value=u'squeeze', tag=u'squeeze')
CementJobType.unknown = CementJobType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
CementJobType._InitializeFacetMap(CementJobType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CementJobType', CementJobType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ChangeInfoType
class ChangeInfoType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ChangeInfoType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 658, 1)
    _Documentation = ''
ChangeInfoType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ChangeInfoType, enum_prefix=None)
ChangeInfoType.add = ChangeInfoType._CF_enumeration.addEnumeration(unicode_value=u'add', tag=u'add')
ChangeInfoType.update = ChangeInfoType._CF_enumeration.addEnumeration(unicode_value=u'update', tag=u'update')
ChangeInfoType.delete = ChangeInfoType._CF_enumeration.addEnumeration(unicode_value=u'delete', tag=u'delete')
ChangeInfoType._InitializeFacetMap(ChangeInfoType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ChangeInfoType', ChangeInfoType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ChronostratigraphyUnit
class ChronostratigraphyUnit (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Specifies the unit of chronostratigraphy."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ChronostratigraphyUnit')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 681, 1)
    _Documentation = u'Specifies the unit of chronostratigraphy.'
ChronostratigraphyUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ChronostratigraphyUnit, enum_prefix=None)
ChronostratigraphyUnit.era = ChronostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value=u'era', tag=u'era')
ChronostratigraphyUnit.period = ChronostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value=u'period', tag=u'period')
ChronostratigraphyUnit.epoch = ChronostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value=u'epoch', tag=u'epoch')
ChronostratigraphyUnit.stage = ChronostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value=u'stage', tag=u'stage')
ChronostratigraphyUnit._InitializeFacetMap(ChronostratigraphyUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ChronostratigraphyUnit', ChronostratigraphyUnit)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ConnectionPosition
class ConnectionPosition (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the position of a connection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ConnectionPosition')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 727, 1)
    _Documentation = u'These values represent the position of a connection.'
ConnectionPosition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ConnectionPosition, enum_prefix=None)
ConnectionPosition.both = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value=u'both', tag=u'both')
ConnectionPosition.bottom = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value=u'bottom', tag=u'bottom')
ConnectionPosition.top = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value=u'top', tag=u'top')
ConnectionPosition.unknown = ConnectionPosition._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ConnectionPosition._InitializeFacetMap(ConnectionPosition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ConnectionPosition', ConnectionPosition)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DeflectionMethod
class DeflectionMethod (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent method used to direct the 
			deviation of the trajectory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DeflectionMethod')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 757, 1)
    _Documentation = u'These values represent method used to direct the \n\t\t\tdeviation of the trajectory.'
DeflectionMethod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeflectionMethod, enum_prefix=None)
DeflectionMethod.point_bit = DeflectionMethod._CF_enumeration.addEnumeration(unicode_value=u'point bit', tag=u'point_bit')
DeflectionMethod.push_bit = DeflectionMethod._CF_enumeration.addEnumeration(unicode_value=u'push bit', tag=u'push_bit')
DeflectionMethod._InitializeFacetMap(DeflectionMethod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DeflectionMethod', DeflectionMethod)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DerrickType
class DerrickType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drilling derrick."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DerrickType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 780, 1)
    _Documentation = u'These values represent the type of drilling derrick.'
DerrickType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DerrickType, enum_prefix=None)
DerrickType.double = DerrickType._CF_enumeration.addEnumeration(unicode_value=u'double', tag=u'double')
DerrickType.quadruple = DerrickType._CF_enumeration.addEnumeration(unicode_value=u'quadruple', tag=u'quadruple')
DerrickType.slant = DerrickType._CF_enumeration.addEnumeration(unicode_value=u'slant', tag=u'slant')
DerrickType.triple = DerrickType._CF_enumeration.addEnumeration(unicode_value=u'triple', tag=u'triple')
DerrickType.unknown = DerrickType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
DerrickType._InitializeFacetMap(DerrickType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DerrickType', DerrickType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DrawWorksType
class DrawWorksType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DrawWorksType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 815, 1)
    _Documentation = None
DrawWorksType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DrawWorksType, enum_prefix=None)
DrawWorksType.mechanical = DrawWorksType._CF_enumeration.addEnumeration(unicode_value=u'mechanical', tag=u'mechanical')
DrawWorksType.standard_electric = DrawWorksType._CF_enumeration.addEnumeration(unicode_value=u'standard electric', tag=u'standard_electric')
DrawWorksType.diesel_electric = DrawWorksType._CF_enumeration.addEnumeration(unicode_value=u'diesel electric', tag=u'diesel_electric')
DrawWorksType.ram_rig = DrawWorksType._CF_enumeration.addEnumeration(unicode_value=u'ram rig', tag=u'ram_rig')
DrawWorksType.unknown = DrawWorksType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
DrawWorksType._InitializeFacetMap(DrawWorksType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DrawWorksType', DrawWorksType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DriveType
class DriveType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of work string drive (rotary system)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DriveType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 847, 1)
    _Documentation = u'These values represent the type of work string drive (rotary system).'
DriveType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DriveType, enum_prefix=None)
DriveType.coiled_tubing = DriveType._CF_enumeration.addEnumeration(unicode_value=u'coiled tubing', tag=u'coiled_tubing')
DriveType.rotary_kelly_drive = DriveType._CF_enumeration.addEnumeration(unicode_value=u'rotary kelly drive', tag=u'rotary_kelly_drive')
DriveType.top_drive = DriveType._CF_enumeration.addEnumeration(unicode_value=u'top drive', tag=u'top_drive')
DriveType.unknown = DriveType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
DriveType._InitializeFacetMap(DriveType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DriveType', DriveType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}EastOrWest
class EastOrWest (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EastOrWest')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 877, 1)
    _Documentation = ''
EastOrWest._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EastOrWest, enum_prefix=None)
EastOrWest.east = EastOrWest._CF_enumeration.addEnumeration(unicode_value=u'east', tag=u'east')
EastOrWest.west = EastOrWest._CF_enumeration.addEnumeration(unicode_value=u'west', tag=u'west')
EastOrWest.unknown = EastOrWest._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
EastOrWest._InitializeFacetMap(EastOrWest._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'EastOrWest', EastOrWest)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ElevCodeEnum
class ElevCodeEnum (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The type of local or permanent reference datum for vertical gravity based 
			(i.e., elevation and vertical depth) and measured depth coordinates within the context of a well.
			This list includes local points (e.g., kelly bushing) used as a datum and 
			vertical reference datums (e.g., mean sea level)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ElevCodeEnum')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 902, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}Ellipsoid
class Ellipsoid (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of ellipsoid (spheroid) 
			defining geographic or planar coordinates. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Ellipsoid')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1010, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}ErrorTermSource
class ErrorTermSource (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The codes for the various classes of error source."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ErrorTermSource')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1416, 1)
    _Documentation = u'The codes for the various classes of error source.'
ErrorTermSource._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErrorTermSource, enum_prefix=None)
ErrorTermSource.sensor = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value=u'sensor', tag=u'sensor')
ErrorTermSource.azimuth_reference = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value=u'azimuth reference', tag=u'azimuth_reference')
ErrorTermSource.magnetic = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value=u'magnetic', tag=u'magnetic')
ErrorTermSource.alignment = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value=u'alignment', tag=u'alignment')
ErrorTermSource.misalignment = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value=u'misalignment', tag=u'misalignment')
ErrorTermSource.depth = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value=u'depth', tag=u'depth')
ErrorTermSource.reference = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value=u'reference', tag=u'reference')
ErrorTermSource.unknown = ErrorTermSource._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ErrorTermSource._InitializeFacetMap(ErrorTermSource._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ErrorTermSource', ErrorTermSource)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ErrorPropagationMode
class ErrorPropagationMode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The codes for the various propagation modes."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ErrorPropagationMode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1473, 1)
    _Documentation = u'The codes for the various propagation modes.'
ErrorPropagationMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErrorPropagationMode, enum_prefix=None)
ErrorPropagationMode.B = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value=u'B', tag=u'B')
ErrorPropagationMode.R = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value=u'R', tag=u'R')
ErrorPropagationMode.S = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value=u'S', tag=u'S')
ErrorPropagationMode.W = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value=u'W', tag=u'W')
ErrorPropagationMode.G = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value=u'G', tag=u'G')
ErrorPropagationMode.unknown = ErrorPropagationMode._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ErrorPropagationMode._InitializeFacetMap(ErrorPropagationMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ErrorPropagationMode', ErrorPropagationMode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ErrorModelMisalignmentMode
class ErrorModelMisalignmentMode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The enums for the various misalignment maths."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ErrorModelMisalignmentMode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1514, 1)
    _Documentation = u'The enums for the various misalignment maths.'
ErrorModelMisalignmentMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErrorModelMisalignmentMode, enum_prefix=None)
ErrorModelMisalignmentMode.n1 = ErrorModelMisalignmentMode._CF_enumeration.addEnumeration(unicode_value=u'1', tag=u'n1')
ErrorModelMisalignmentMode.n2 = ErrorModelMisalignmentMode._CF_enumeration.addEnumeration(unicode_value=u'2', tag=u'n2')
ErrorModelMisalignmentMode.n3 = ErrorModelMisalignmentMode._CF_enumeration.addEnumeration(unicode_value=u'3', tag=u'n3')
ErrorModelMisalignmentMode.unknown = ErrorModelMisalignmentMode._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ErrorModelMisalignmentMode._InitializeFacetMap(ErrorModelMisalignmentMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ErrorModelMisalignmentMode', ErrorModelMisalignmentMode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ExtensionName
class ExtensionName (abstractTypeEnum):

    """The name of a data extension.
			The list of standard values is contained in the WITSML enumValues.xml file."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExtensionName')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1545, 1)
    _Documentation = u'The name of a data extension.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file.'
ExtensionName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ExtensionName', ExtensionName)

# Atomic simple type: {http://www.witsml.org/schemas/1series}GasPeakType
class GasPeakType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GasPeakType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1554, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}GeodeticDatum
class GeodeticDatum (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of geodetic datum. 
			The source (except for "none", "unknown" and "UserDefined") of the values 
			and the descriptions is Geoshare V13."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeodeticDatum')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1611, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}Hemispheres
class Hemispheres (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Hemispheres')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1828, 1)
    _Documentation = None
Hemispheres._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Hemispheres, enum_prefix=None)
Hemispheres.northern = Hemispheres._CF_enumeration.addEnumeration(unicode_value=u'northern', tag=u'northern')
Hemispheres.southern = Hemispheres._CF_enumeration.addEnumeration(unicode_value=u'southern', tag=u'southern')
Hemispheres.unknown = Hemispheres._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
Hemispheres._InitializeFacetMap(Hemispheres._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Hemispheres', Hemispheres)

# Atomic simple type: {http://www.witsml.org/schemas/1series}HoleCasingType
class HoleCasingType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HoleCasingType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1850, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}HoleOpenerType
class HoleOpenerType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HoleOpenerType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1902, 1)
    _Documentation = None
HoleOpenerType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HoleOpenerType, enum_prefix=None)
HoleOpenerType.under_reamer = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value=u'under-reamer', tag=u'under_reamer')
HoleOpenerType.fixed_blade = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value=u'fixed blade', tag=u'fixed_blade')
HoleOpenerType.unknown = HoleOpenerType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
HoleOpenerType._InitializeFacetMap(HoleOpenerType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'HoleOpenerType', HoleOpenerType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}InnerBarrelType
class InnerBarrelType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'InnerBarrelType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1924, 1)
    _Documentation = ''
InnerBarrelType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InnerBarrelType, enum_prefix=None)
InnerBarrelType.undifferented = InnerBarrelType._CF_enumeration.addEnumeration(unicode_value=u'undifferented', tag=u'undifferented')
InnerBarrelType.aluminum = InnerBarrelType._CF_enumeration.addEnumeration(unicode_value=u'aluminum', tag=u'aluminum')
InnerBarrelType.gel = InnerBarrelType._CF_enumeration.addEnumeration(unicode_value=u'gel', tag=u'gel')
InnerBarrelType.fiberglass = InnerBarrelType._CF_enumeration.addEnumeration(unicode_value=u'fiberglass', tag=u'fiberglass')
InnerBarrelType.unknown = InnerBarrelType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
InnerBarrelType._InitializeFacetMap(InnerBarrelType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'InnerBarrelType', InnerBarrelType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ItemState
class ItemState (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the state of a WITSML object. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ItemState')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1960, 1)
    _Documentation = u'These values represent the state of a WITSML object. '
ItemState._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ItemState, enum_prefix=None)
ItemState.actual = ItemState._CF_enumeration.addEnumeration(unicode_value=u'actual', tag=u'actual')
ItemState.model = ItemState._CF_enumeration.addEnumeration(unicode_value=u'model', tag=u'model')
ItemState.plan = ItemState._CF_enumeration.addEnumeration(unicode_value=u'plan', tag=u'plan')
ItemState.unknown = ItemState._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ItemState._InitializeFacetMap(ItemState._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ItemState', ItemState)

# Atomic simple type: {http://www.witsml.org/schemas/1series}JarType
class JarType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'JarType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 1990, 1)
    _Documentation = None
JarType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=JarType, enum_prefix=None)
JarType.mechanical = JarType._CF_enumeration.addEnumeration(unicode_value=u'mechanical', tag=u'mechanical')
JarType.hydraulic = JarType._CF_enumeration.addEnumeration(unicode_value=u'hydraulic', tag=u'hydraulic')
JarType.hydro_mechanical = JarType._CF_enumeration.addEnumeration(unicode_value=u'hydro mechanical', tag=u'hydro_mechanical')
JarType.unknown = JarType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
JarType._InitializeFacetMap(JarType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'JarType', JarType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}JarAction
class JarAction (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'JarAction')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2017, 1)
    _Documentation = None
JarAction._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=JarAction, enum_prefix=None)
JarAction.up = JarAction._CF_enumeration.addEnumeration(unicode_value=u'up', tag=u'up')
JarAction.down = JarAction._CF_enumeration.addEnumeration(unicode_value=u'down', tag=u'down')
JarAction.both = JarAction._CF_enumeration.addEnumeration(unicode_value=u'both', tag=u'both')
JarAction.vibrating = JarAction._CF_enumeration.addEnumeration(unicode_value=u'vibrating', tag=u'vibrating')
JarAction.unknown = JarAction._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
JarAction._InitializeFacetMap(JarAction._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'JarAction', JarAction)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LithologySource
class LithologySource (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Specifies the source of lithology information."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LithologySource')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2049, 1)
    _Documentation = u'Specifies the source of lithology information.'
LithologySource._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LithologySource, enum_prefix=None)
LithologySource.interpreted = LithologySource._CF_enumeration.addEnumeration(unicode_value=u'interpreted', tag=u'interpreted')
LithologySource.core = LithologySource._CF_enumeration.addEnumeration(unicode_value=u'core', tag=u'core')
LithologySource.cuttings = LithologySource._CF_enumeration.addEnumeration(unicode_value=u'cuttings', tag=u'cuttings')
LithologySource.unknown = LithologySource._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
LithologySource._InitializeFacetMap(LithologySource._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LithologySource', LithologySource)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LithologyType
class LithologyType (abstractTypeEnum):

    """The type of lithology.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LithologyType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2082, 1)
    _Documentation = u'The type of lithology.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
LithologyType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'LithologyType', LithologyType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LithostratigraphyUnit
class LithostratigraphyUnit (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Specifies the unit of lithostratigraphy."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LithostratigraphyUnit')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2091, 1)
    _Documentation = u'Specifies the unit of lithostratigraphy.'
LithostratigraphyUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LithostratigraphyUnit, enum_prefix=None)
LithostratigraphyUnit.group = LithostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value=u'group', tag=u'group')
LithostratigraphyUnit.formation = LithostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value=u'formation', tag=u'formation')
LithostratigraphyUnit.member = LithostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value=u'member', tag=u'member')
LithostratigraphyUnit.bed = LithostratigraphyUnit._CF_enumeration.addEnumeration(unicode_value=u'bed', tag=u'bed')
LithostratigraphyUnit._InitializeFacetMap(LithostratigraphyUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LithostratigraphyUnit', LithostratigraphyUnit)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LogDataType
class LogDataType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The endcoding allowed in a log curve value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogDataType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2146, 1)
    _Documentation = u'The endcoding allowed in a log curve value.'
LogDataType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogDataType, enum_prefix=None)
LogDataType.byte = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'byte', tag=u'byte')
LogDataType.date_time = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'date time', tag=u'date_time')
LogDataType.double = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'double', tag=u'double')
LogDataType.float = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'float', tag=u'float')
LogDataType.int = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'int', tag=u'int')
LogDataType.long = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'long', tag=u'long')
LogDataType.short = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'short', tag=u'short')
LogDataType.string = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'string', tag=u'string')
LogDataType.string40 = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'string40', tag=u'string40')
LogDataType.string16 = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'string16', tag=u'string16')
LogDataType.unknown = LogDataType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
LogDataType._InitializeFacetMap(LogDataType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LogDataType', LogDataType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LogIndexDirection
class LogIndexDirection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the direction of movement within a wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogIndexDirection')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2229, 1)
    _Documentation = u'These values represent the direction of movement within a wellbore.'
LogIndexDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogIndexDirection, enum_prefix=None)
LogIndexDirection.decreasing = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value=u'decreasing', tag=u'decreasing')
LogIndexDirection.increasing = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value=u'increasing', tag=u'increasing')
LogIndexDirection.unknown = LogIndexDirection._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
LogIndexDirection._InitializeFacetMap(LogIndexDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LogIndexDirection', LogIndexDirection)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LogIndexType
class LogIndexType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of data used as an index value for a log. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogIndexType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2256, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}LogTraceOrigin
class LogTraceOrigin (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogTraceOrigin')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2301, 1)
    _Documentation = None
LogTraceOrigin._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogTraceOrigin, enum_prefix=None)
LogTraceOrigin.realtime = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value=u'realtime', tag=u'realtime')
LogTraceOrigin.modeled = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value=u'modeled', tag=u'modeled')
LogTraceOrigin.unknown = LogTraceOrigin._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
LogTraceOrigin._InitializeFacetMap(LogTraceOrigin._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LogTraceOrigin', LogTraceOrigin)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LogTraceState
class LogTraceState (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogTraceState')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2323, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}MaterialType
class MaterialType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MaterialType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2360, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}MatrixCementType
class MatrixCementType (abstractTypeEnum):

    """Lithology matrix/cement description.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MatrixCementType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2422, 1)
    _Documentation = u'Lithology matrix/cement description.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
MatrixCementType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'MatrixCementType', MatrixCementType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MeasureClass
class MeasureClass (abstractTypeEnum):

    """Measure class values.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MeasureClass')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2432, 1)
    _Documentation = u'Measure class values.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
MeasureClass._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'MeasureClass', MeasureClass)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MeasurementType
class MeasurementType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The source (except for "CH density porosity", "CH neutron porosity", "OH density porosity"
			and "OH neutron porosity") of the values and the descriptions is the POSC V2.2 "well log trace class" 
			standard instance values which are documented as "A classification of well log traces based on 
			specification of a range of characteristics. Traces may be classed according to the type of physical 
			characteristic they are meant to measure." """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MeasurementType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 2442, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}MessageProbability
class MessageProbability (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MessageProbability')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 3931, 1)
    _Documentation = None
MessageProbability._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageProbability, enum_prefix=None)
MessageProbability.low = MessageProbability._CF_enumeration.addEnumeration(unicode_value=u'low', tag=u'low')
MessageProbability.medium = MessageProbability._CF_enumeration.addEnumeration(unicode_value=u'medium', tag=u'medium')
MessageProbability.high = MessageProbability._CF_enumeration.addEnumeration(unicode_value=u'high', tag=u'high')
MessageProbability.unknown = MessageProbability._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
MessageProbability._InitializeFacetMap(MessageProbability._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MessageProbability', MessageProbability)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MessageSeverity
class MessageSeverity (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MessageSeverity')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 3958, 1)
    _Documentation = None
MessageSeverity._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageSeverity, enum_prefix=None)
MessageSeverity.catastrophic = MessageSeverity._CF_enumeration.addEnumeration(unicode_value=u'catastrophic', tag=u'catastrophic')
MessageSeverity.major = MessageSeverity._CF_enumeration.addEnumeration(unicode_value=u'major', tag=u'major')
MessageSeverity.minor = MessageSeverity._CF_enumeration.addEnumeration(unicode_value=u'minor', tag=u'minor')
MessageSeverity.unknown = MessageSeverity._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
MessageSeverity._InitializeFacetMap(MessageSeverity._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MessageSeverity', MessageSeverity)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MessageType
class MessageType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a message. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MessageType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 3985, 1)
    _Documentation = u'These values represent the type of a message. '
MessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageType, enum_prefix=None)
MessageType.alarm = MessageType._CF_enumeration.addEnumeration(unicode_value=u'alarm', tag=u'alarm')
MessageType.event = MessageType._CF_enumeration.addEnumeration(unicode_value=u'event', tag=u'event')
MessageType.informational = MessageType._CF_enumeration.addEnumeration(unicode_value=u'informational', tag=u'informational')
MessageType.warning = MessageType._CF_enumeration.addEnumeration(unicode_value=u'warning', tag=u'warning')
MessageType.unknown = MessageType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
MessageType._InitializeFacetMap(MessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MessageType', MessageType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MudClass
class MudClass (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Defines the class of a drilling fluid."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MudClass')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4020, 1)
    _Documentation = u'Defines the class of a drilling fluid.'
MudClass._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MudClass, enum_prefix=None)
MudClass.water_based = MudClass._CF_enumeration.addEnumeration(unicode_value=u'water based', tag=u'water_based')
MudClass.oil_based = MudClass._CF_enumeration.addEnumeration(unicode_value=u'oil based', tag=u'oil_based')
MudClass.other = MudClass._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
MudClass.pneumatic = MudClass._CF_enumeration.addEnumeration(unicode_value=u'pneumatic', tag=u'pneumatic')
MudClass.unknown = MudClass._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
MudClass._InitializeFacetMap(MudClass._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MudClass', MudClass)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MudLogParameterType
class MudLogParameterType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """ "Text value" indicates that a text value is expected. 
			"Pressure value" indicates that an equivalentMudWeight value is expected.
			"Pressure gradient value" indicates that an equivalentMudWeight value is 
			  commonly expected but a pressureGradient value may also be specified.
			"Concentration value" indicates that a concentration value is expected.
			"Force value" indicates that a force value is expected.
			"Only" indicates that no other value is expected."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MudLogParameterType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4057, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}MudSubClass
class MudSubClass (abstractTypeEnum):

    """
        The name of a data extension.
        The list of standard values is contained in the WITSML enumValues.xml file.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MudSubClass')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4319, 2)
    _Documentation = u'\n        The name of a data extension.\n        The list of standard values is contained in the WITSML enumValues.xml file.\n      '
MudSubClass._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'MudSubClass', MudSubClass)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NADTypes
class NADTypes (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NADTypes')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4330, 2)
    _Documentation = None
NADTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NADTypes, enum_prefix=None)
NADTypes.NAD27 = NADTypes._CF_enumeration.addEnumeration(unicode_value=u'NAD27', tag=u'NAD27')
NADTypes.NAD83 = NADTypes._CF_enumeration.addEnumeration(unicode_value=u'NAD83', tag=u'NAD83')
NADTypes.unknown = NADTypes._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
NADTypes._InitializeFacetMap(NADTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'NADTypes', NADTypes)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NameTagLocation
class NameTagLocation (abstractTypeEnum):

    """Defines the locations where an equipment tag might be found..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NameTagLocation')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4352, 1)
    _Documentation = u'Defines the locations where an equipment tag might be found..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagLocation._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'NameTagLocation', NameTagLocation)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NameTagNumberingScheme
class NameTagNumberingScheme (abstractTypeEnum):

    """Defines the specifications for creating equipment tags..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NameTagNumberingScheme')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4361, 1)
    _Documentation = u'Defines the specifications for creating equipment tags..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagNumberingScheme._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'NameTagNumberingScheme', NameTagNumberingScheme)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NameTagTechnology
class NameTagTechnology (abstractTypeEnum):

    """Defines the mechanisms for attaching an equipment tag to an item..
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NameTagTechnology')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4370, 1)
    _Documentation = u'Defines the mechanisms for attaching an equipment tag to an item..\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
NameTagTechnology._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'NameTagTechnology', NameTagTechnology)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NorthOrSouth
class NorthOrSouth (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NorthOrSouth')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4379, 1)
    _Documentation = ''
NorthOrSouth._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NorthOrSouth, enum_prefix=None)
NorthOrSouth.north = NorthOrSouth._CF_enumeration.addEnumeration(unicode_value=u'north', tag=u'north')
NorthOrSouth.south = NorthOrSouth._CF_enumeration.addEnumeration(unicode_value=u'south', tag=u'south')
NorthOrSouth.unknown = NorthOrSouth._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
NorthOrSouth._InitializeFacetMap(NorthOrSouth._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'NorthOrSouth', NorthOrSouth)

# Atomic simple type: {http://www.witsml.org/schemas/1series}NozzleType
class NozzleType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NozzleType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4404, 1)
    _Documentation = None
NozzleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NozzleType, enum_prefix=None)
NozzleType.extended = NozzleType._CF_enumeration.addEnumeration(unicode_value=u'extended', tag=u'extended')
NozzleType.normal = NozzleType._CF_enumeration.addEnumeration(unicode_value=u'normal', tag=u'normal')
NozzleType.unknown = NozzleType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
NozzleType._InitializeFacetMap(NozzleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'NozzleType', NozzleType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}OpsReportVersion
class OpsReportVersion (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OpsReportVersion')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4427, 1)
    _Documentation = ''
OpsReportVersion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OpsReportVersion, enum_prefix=None)
OpsReportVersion.preliminary = OpsReportVersion._CF_enumeration.addEnumeration(unicode_value=u'preliminary', tag=u'preliminary')
OpsReportVersion.normal = OpsReportVersion._CF_enumeration.addEnumeration(unicode_value=u'normal', tag=u'normal')
OpsReportVersion.final = OpsReportVersion._CF_enumeration.addEnumeration(unicode_value=u'final', tag=u'final')
OpsReportVersion.unknown = OpsReportVersion._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
OpsReportVersion._InitializeFacetMap(OpsReportVersion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'OpsReportVersion', OpsReportVersion)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PIDXCommodityCode
class PIDXCommodityCode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The PIDX commodity codes used in a stimulation job."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PIDXCommodityCode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4460, 1)
    _Documentation = u'The PIDX commodity codes used in a stimulation job.'
PIDXCommodityCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PIDXCommodityCode, enum_prefix=None)
PIDXCommodityCode.n71131001 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131001', tag=u'n71131001')
PIDXCommodityCode.n71131002 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131002', tag=u'n71131002')
PIDXCommodityCode.n71131003 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131003', tag=u'n71131003')
PIDXCommodityCode.n71131004 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131004', tag=u'n71131004')
PIDXCommodityCode.n71131005 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131005', tag=u'n71131005')
PIDXCommodityCode.n71131006 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131006', tag=u'n71131006')
PIDXCommodityCode.n71131007 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131007', tag=u'n71131007')
PIDXCommodityCode.n71131008 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131008', tag=u'n71131008')
PIDXCommodityCode.n71131009 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131009', tag=u'n71131009')
PIDXCommodityCode.n71131010 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131010', tag=u'n71131010')
PIDXCommodityCode.n71131011 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131011', tag=u'n71131011')
PIDXCommodityCode.n71131012 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131012', tag=u'n71131012')
PIDXCommodityCode.n71131013 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131013', tag=u'n71131013')
PIDXCommodityCode.n71131014 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131014', tag=u'n71131014')
PIDXCommodityCode.n71131015 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131015', tag=u'n71131015')
PIDXCommodityCode.n71131016 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131016', tag=u'n71131016')
PIDXCommodityCode.n71131018 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131018', tag=u'n71131018')
PIDXCommodityCode.n71131019 = PIDXCommodityCode._CF_enumeration.addEnumeration(unicode_value=u'71131019', tag=u'n71131019')
PIDXCommodityCode._InitializeFacetMap(PIDXCommodityCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PIDXCommodityCode', PIDXCommodityCode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PitType
class PitType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PitType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4559, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}PrimitiveType
class PrimitiveType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The underlying XML Schema primitve type
			Does NOT support "decimal", "QName" or "NOTATION". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PrimitiveType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4625, 1)
    _Documentation = u'The underlying XML Schema primitve type\n\t\t\tDoes NOT support "decimal", "QName" or "NOTATION". '
PrimitiveType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PrimitiveType, enum_prefix=None)
PrimitiveType.string = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'string', tag=u'string')
PrimitiveType.boolean = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'boolean', tag=u'boolean')
PrimitiveType.float = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'float', tag=u'float')
PrimitiveType.double = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'double', tag=u'double')
PrimitiveType.duration = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'duration', tag=u'duration')
PrimitiveType.dateTime = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'dateTime', tag=u'dateTime')
PrimitiveType.time = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'time', tag=u'time')
PrimitiveType.date = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'date', tag=u'date')
PrimitiveType.gYearMonth = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'gYearMonth', tag=u'gYearMonth')
PrimitiveType.gYear = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'gYear', tag=u'gYear')
PrimitiveType.gMonthDay = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'gMonthDay', tag=u'gMonthDay')
PrimitiveType.gDay = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'gDay', tag=u'gDay')
PrimitiveType.gMonth = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'gMonth', tag=u'gMonth')
PrimitiveType.base64Binary = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'base64Binary', tag=u'base64Binary')
PrimitiveType.anyURI = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'anyURI', tag=u'anyURI')
PrimitiveType.unknown = PrimitiveType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
PrimitiveType._InitializeFacetMap(PrimitiveType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PrimitiveType', PrimitiveType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}Projection
class Projection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of coordinate system projection method.
			The source (except for "UserDefined") of the values is Geoshare V13. 
			For a detailed description of each value, see the Geoshare documentation of the 
			indicated "217" object at http://w3.posc.org/GeoshareSIG/technical/GDM/v13.0/."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Projection')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4657, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}ProjectionVariantsObliqueMercator
class ProjectionVariantsObliqueMercator (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProjectionVariantsObliqueMercator')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4785, 1)
    _Documentation = None
ProjectionVariantsObliqueMercator._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProjectionVariantsObliqueMercator, enum_prefix=None)
ProjectionVariantsObliqueMercator.default = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value=u'default', tag=u'default')
ProjectionVariantsObliqueMercator.rectified = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value=u'rectified', tag=u'rectified')
ProjectionVariantsObliqueMercator.rectified_skew = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value=u'rectified skew', tag=u'rectified_skew')
ProjectionVariantsObliqueMercator.rectified_skew_center_origin = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value=u'rectified skew center origin', tag=u'rectified_skew_center_origin')
ProjectionVariantsObliqueMercator.unknown = ProjectionVariantsObliqueMercator._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ProjectionVariantsObliqueMercator._InitializeFacetMap(ProjectionVariantsObliqueMercator._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ProjectionVariantsObliqueMercator', ProjectionVariantsObliqueMercator)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PresTestType
class PresTestType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PresTestType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4817, 1)
    _Documentation = ''
PresTestType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PresTestType, enum_prefix=None)
PresTestType.leak_off_test = PresTestType._CF_enumeration.addEnumeration(unicode_value=u'leak off test', tag=u'leak_off_test')
PresTestType.formation_integrity_test = PresTestType._CF_enumeration.addEnumeration(unicode_value=u'formation integrity test', tag=u'formation_integrity_test')
PresTestType.unknown = PresTestType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
PresTestType._InitializeFacetMap(PresTestType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PresTestType', PresTestType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PrincipalMeridian
class PrincipalMeridian (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Principal Meridians for United States Public Land Surveys."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PrincipalMeridian')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 4847, 1)
    _Documentation = u'Principal Meridians for United States Public Land Surveys.'
PrincipalMeridian._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PrincipalMeridian, enum_prefix=None)
PrincipalMeridian.n1st_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'1st Principal Meridian', tag=u'n1st_Principal_Meridian')
PrincipalMeridian.n2nd_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'2nd Principal Meridian', tag=u'n2nd_Principal_Meridian')
PrincipalMeridian.n3rd_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'3rd Principal Meridian', tag=u'n3rd_Principal_Meridian')
PrincipalMeridian.n4th_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'4th Principal Meridian', tag=u'n4th_Principal_Meridian')
PrincipalMeridian.n5th_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'5th Principal Meridian', tag=u'n5th_Principal_Meridian')
PrincipalMeridian.n6th_Principal_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'6th Principal Meridian', tag=u'n6th_Principal_Meridian')
PrincipalMeridian.Black_Hills_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Black Hills Meridian', tag=u'Black_Hills_Meridian')
PrincipalMeridian.Boise_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Boise Meridian', tag=u'Boise_Meridian')
PrincipalMeridian.Choctaw_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Choctaw Meridian', tag=u'Choctaw_Meridian')
PrincipalMeridian.Chickasaw_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Chickasaw Meridian', tag=u'Chickasaw_Meridian')
PrincipalMeridian.Cimarron_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Cimarron Meridian', tag=u'Cimarron_Meridian')
PrincipalMeridian.Copper_River_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Copper River Meridian', tag=u'Copper_River_Meridian')
PrincipalMeridian.Fairbanks_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Fairbanks Meridian', tag=u'Fairbanks_Meridian')
PrincipalMeridian.Gila_and_Salt_River_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Gila and Salt River Meridian', tag=u'Gila_and_Salt_River_Meridian')
PrincipalMeridian.Humboldt_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Humboldt Meridian', tag=u'Humboldt_Meridian')
PrincipalMeridian.Huntsville_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Huntsville Meridian', tag=u'Huntsville_Meridian')
PrincipalMeridian.Indian_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Indian Meridian', tag=u'Indian_Meridian')
PrincipalMeridian.Kateel_River_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Kateel River Meridian', tag=u'Kateel_River_Meridian')
PrincipalMeridian.Lousiana_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Lousiana Meridian', tag=u'Lousiana_Meridian')
PrincipalMeridian.Michigan_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Michigan Meridian', tag=u'Michigan_Meridian')
PrincipalMeridian.Mount_Diablo_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Mount Diablo Meridian', tag=u'Mount_Diablo_Meridian')
PrincipalMeridian.New_Mexico_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'New Mexico Meridian', tag=u'New_Mexico_Meridian')
PrincipalMeridian.Saint_Stephens_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Saint Stephens Meridian', tag=u'Saint_Stephens_Meridian')
PrincipalMeridian.Saint_Helena_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Saint Helena Meridian', tag=u'Saint_Helena_Meridian')
PrincipalMeridian.Salt_Lake_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Salt Lake Meridian', tag=u'Salt_Lake_Meridian')
PrincipalMeridian.San_Bernardo_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'San Bernardo Meridian', tag=u'San_Bernardo_Meridian')
PrincipalMeridian.Seward_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Seward Meridian', tag=u'Seward_Meridian')
PrincipalMeridian.Tallahassee_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Tallahassee Meridian', tag=u'Tallahassee_Meridian')
PrincipalMeridian.Uintah_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Uintah Meridian', tag=u'Uintah_Meridian')
PrincipalMeridian.Umiat_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Umiat Meridian', tag=u'Umiat_Meridian')
PrincipalMeridian.Ute_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Ute Meridian', tag=u'Ute_Meridian')
PrincipalMeridian.Washington_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Washington Meridian', tag=u'Washington_Meridian')
PrincipalMeridian.Williamette_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Williamette Meridian', tag=u'Williamette_Meridian')
PrincipalMeridian.Wind_River_Meridian = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'Wind River Meridian', tag=u'Wind_River_Meridian')
PrincipalMeridian.unknown = PrincipalMeridian._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
PrincipalMeridian._InitializeFacetMap(PrincipalMeridian._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PrincipalMeridian', PrincipalMeridian)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PumpType
class PumpType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a pump. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PumpType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5033, 1)
    _Documentation = u'These values represent the type of a pump. '
PumpType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PumpType, enum_prefix=None)
PumpType.centrifugal = PumpType._CF_enumeration.addEnumeration(unicode_value=u'centrifugal', tag=u'centrifugal')
PumpType.duplex = PumpType._CF_enumeration.addEnumeration(unicode_value=u'duplex', tag=u'duplex')
PumpType.triplex = PumpType._CF_enumeration.addEnumeration(unicode_value=u'triplex', tag=u'triplex')
PumpType.unknown = PumpType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
PumpType._InitializeFacetMap(PumpType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PumpType', PumpType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PumpOpType
class PumpOpType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PumpOpType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5063, 1)
    _Documentation = None
PumpOpType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PumpOpType, enum_prefix=None)
PumpOpType.drilling = PumpOpType._CF_enumeration.addEnumeration(unicode_value=u'drilling', tag=u'drilling')
PumpOpType.reaming = PumpOpType._CF_enumeration.addEnumeration(unicode_value=u'reaming', tag=u'reaming')
PumpOpType.circulating = PumpOpType._CF_enumeration.addEnumeration(unicode_value=u'circulating', tag=u'circulating')
PumpOpType.slow_pump = PumpOpType._CF_enumeration.addEnumeration(unicode_value=u'slow pump', tag=u'slow_pump')
PumpOpType.unknown = PumpOpType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
PumpOpType._InitializeFacetMap(PumpOpType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PumpOpType', PumpOpType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}QualifierType
class QualifierType (abstractTypeEnum):

    """The type of qualifier of a lithology.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QualifierType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5095, 1)
    _Documentation = u'The type of qualifier of a lithology.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
QualifierType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'QualifierType', QualifierType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ReadingKind
class ReadingKind (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReadingKind')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5104, 1)
    _Documentation = ''
ReadingKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReadingKind, enum_prefix=None)
ReadingKind.measured = ReadingKind._CF_enumeration.addEnumeration(unicode_value=u'measured', tag=u'measured')
ReadingKind.estimated = ReadingKind._CF_enumeration.addEnumeration(unicode_value=u'estimated', tag=u'estimated')
ReadingKind.unknown = ReadingKind._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ReadingKind._InitializeFacetMap(ReadingKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ReadingKind', ReadingKind)

# Atomic simple type: {http://www.witsml.org/schemas/1series}RigType
class RigType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of drilling rig. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RigType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5129, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}RiskAffectedPersonnel
class RiskAffectedPersonnel (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Personnel affected by a risk."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RiskAffectedPersonnel')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5179, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}RiskCategory
class RiskCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of slow circulation rate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RiskCategory')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5322, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}RiskSubCategory
class RiskSubCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Risk Sub-Categories."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RiskSubCategory')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5392, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}RiskType
class RiskType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Types of risk."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RiskType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 5955, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}ScrType
class ScrType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of slow circulation rate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ScrType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6000, 1)
    _Documentation = u'Type of slow circulation rate.'
ScrType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ScrType, enum_prefix=None)
ScrType.string_annulus = ScrType._CF_enumeration.addEnumeration(unicode_value=u'string annulus', tag=u'string_annulus')
ScrType.string_kill_line = ScrType._CF_enumeration.addEnumeration(unicode_value=u'string kill line', tag=u'string_kill_line')
ScrType.string_choke_line = ScrType._CF_enumeration.addEnumeration(unicode_value=u'string choke line', tag=u'string_choke_line')
ScrType.unknown = ScrType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ScrType._InitializeFacetMap(ScrType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ScrType', ScrType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ShowFluorescence
class ShowFluorescence (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ShowFluorescence')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6030, 1)
    _Documentation = None
ShowFluorescence._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowFluorescence, enum_prefix=None)
ShowFluorescence.faint = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value=u'faint', tag=u'faint')
ShowFluorescence.bright = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value=u'bright', tag=u'bright')
ShowFluorescence.none = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
ShowFluorescence.unknown = ShowFluorescence._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ShowFluorescence._InitializeFacetMap(ShowFluorescence._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ShowFluorescence', ShowFluorescence)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ShowLevel
class ShowLevel (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ShowLevel')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6057, 1)
    _Documentation = None
ShowLevel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShowLevel, enum_prefix=None)
ShowLevel.blooming = ShowLevel._CF_enumeration.addEnumeration(unicode_value=u'blooming', tag=u'blooming')
ShowLevel.streaming = ShowLevel._CF_enumeration.addEnumeration(unicode_value=u'streaming', tag=u'streaming')
ShowLevel.unknown = ShowLevel._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ShowLevel._InitializeFacetMap(ShowLevel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ShowLevel', ShowLevel)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ShowRating
class ShowRating (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ShowRating')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6079, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}ShowSpeed
class ShowSpeed (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ShowSpeed')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6121, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}StateDetailActivity
class StateDetailActivity (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StateDetailActivity')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6158, 1)
    _Documentation = ''
StateDetailActivity._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StateDetailActivity, enum_prefix=None)
StateDetailActivity.injury = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value=u'injury', tag=u'injury')
StateDetailActivity.operation_failed = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value=u'operation failed', tag=u'operation_failed')
StateDetailActivity.kick = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value=u'kick', tag=u'kick')
StateDetailActivity.circulation_loss = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value=u'circulation loss', tag=u'circulation_loss')
StateDetailActivity.mud_loss = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value=u'mud loss', tag=u'mud_loss')
StateDetailActivity.stuck_equipment = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value=u'stuck equipment', tag=u'stuck_equipment')
StateDetailActivity.equipment_failure = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value=u'equipment failure', tag=u'equipment_failure')
StateDetailActivity.equipment_hang = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value=u'equipment hang', tag=u'equipment_hang')
StateDetailActivity.success = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value=u'success', tag=u'success')
StateDetailActivity.unknown = StateDetailActivity._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
StateDetailActivity._InitializeFacetMap(StateDetailActivity._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StateDetailActivity', StateDetailActivity)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimAdditiveType
class StimAdditiveType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The types of additives used in a stimulation job."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StimAdditiveType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6219, 1)
    _Documentation = u'The types of additives used in a stimulation job.'
StimAdditiveType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimAdditiveType, enum_prefix=None)
StimAdditiveType.abrasive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'abrasive', tag=u'abrasive')
StimAdditiveType.accelerator = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'accelerator', tag=u'accelerator')
StimAdditiveType.acid_inhibitorretarder = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'acid inhibitor/retarder', tag=u'acid_inhibitorretarder')
StimAdditiveType.acid_material = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'acid material', tag=u'acid_material')
StimAdditiveType.acid_soluble_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'acid soluble additive', tag=u'acid_soluble_additive')
StimAdditiveType.acid_source = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'acid source', tag=u'acid_source')
StimAdditiveType.activator = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'activator', tag=u'activator')
StimAdditiveType.additive_material = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'additive material', tag=u'additive_material')
StimAdditiveType.alcohol = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'alcohol', tag=u'alcohol')
StimAdditiveType.anti_Sludge = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'anti-Sludge', tag=u'anti_Sludge')
StimAdditiveType.anti_sulfide_cracker = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'anti-sulfide cracker', tag=u'anti_sulfide_cracker')
StimAdditiveType.aromatic_solvent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'aromatic solvent', tag=u'aromatic_solvent')
StimAdditiveType.biocide = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'biocide', tag=u'biocide')
StimAdditiveType.borehole_stabilizer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'borehole stabilizer', tag=u'borehole_stabilizer')
StimAdditiveType.breaker = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'breaker', tag=u'breaker')
StimAdditiveType.bridging_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'bridging agent', tag=u'bridging_agent')
StimAdditiveType.buffer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'buffer', tag=u'buffer')
StimAdditiveType.calcium_remover = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'calcium remover', tag=u'calcium_remover')
StimAdditiveType.carrying_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'carrying agent', tag=u'carrying_agent')
StimAdditiveType.catalyst = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'catalyst', tag=u'catalyst')
StimAdditiveType.clay = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'clay', tag=u'clay')
StimAdditiveType.clay_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'clay control', tag=u'clay_control')
StimAdditiveType.conductivity_enhancer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'conductivity enhancer', tag=u'conductivity_enhancer')
StimAdditiveType.conformance_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'conformance control', tag=u'conformance_control')
StimAdditiveType.conformance_caterial = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'conformance caterial', tag=u'conformance_caterial')
StimAdditiveType.corrosion_inhibitor = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'corrosion inhibitor', tag=u'corrosion_inhibitor')
StimAdditiveType.crosslink_enhancer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'crosslink enhancer', tag=u'crosslink_enhancer')
StimAdditiveType.crosslinker = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'crosslinker', tag=u'crosslinker')
StimAdditiveType.curing_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'curing agent', tag=u'curing_agent')
StimAdditiveType.defoamer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'defoamer', tag=u'defoamer')
StimAdditiveType.demulsifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'demulsifier', tag=u'demulsifier')
StimAdditiveType.diluent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'diluent', tag=u'diluent')
StimAdditiveType.dispersant = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'dispersant', tag=u'dispersant')
StimAdditiveType.diverter = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'diverter', tag=u'diverter')
StimAdditiveType.elastomeric_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'elastomeric additive', tag=u'elastomeric_additive')
StimAdditiveType.emulsifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'emulsifier', tag=u'emulsifier')
StimAdditiveType.epoxy_resin = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'epoxy resin', tag=u'epoxy_resin')
StimAdditiveType.expoxy_resin_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'expoxy resin agent', tag=u'expoxy_resin_agent')
StimAdditiveType.expander = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'expander', tag=u'expander')
StimAdditiveType.filtration_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'filtration control', tag=u'filtration_control')
StimAdditiveType.flocculant = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'flocculant', tag=u'flocculant')
StimAdditiveType.fluid_loss_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'fluid loss control', tag=u'fluid_loss_control')
StimAdditiveType.flushspacer_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'flush/spacer additive', tag=u'flushspacer_additive')
StimAdditiveType.foamer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'foamer', tag=u'foamer')
StimAdditiveType.formation_sealer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'formation sealer', tag=u'formation_sealer')
StimAdditiveType.free_water_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'free water control', tag=u'free_water_control')
StimAdditiveType.friction_reducer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'friction reducer', tag=u'friction_reducer')
StimAdditiveType.gas = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'gas', tag=u'gas')
StimAdditiveType.gas_migration_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'gas migration control', tag=u'gas_migration_control')
StimAdditiveType.gel_stabilizer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'gel stabilizer', tag=u'gel_stabilizer')
StimAdditiveType.gelling_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'gelling agent', tag=u'gelling_agent')
StimAdditiveType.H2S_scavenger = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'H2S scavenger', tag=u'H2S_scavenger')
StimAdditiveType.intensifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'intensifier', tag=u'intensifier')
StimAdditiveType.iron_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'iron control', tag=u'iron_control')
StimAdditiveType.lost_circulation_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'lost circulation additive', tag=u'lost_circulation_additive')
StimAdditiveType.low_fluid_loss_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'low fluid loss control', tag=u'low_fluid_loss_control')
StimAdditiveType.lubricant = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'lubricant', tag=u'lubricant')
StimAdditiveType.misc_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'misc additive', tag=u'misc_additive')
StimAdditiveType.mixing_fluid = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'mixing fluid', tag=u'mixing_fluid')
StimAdditiveType.mud_removal_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'mud removal additive', tag=u'mud_removal_additive')
StimAdditiveType.mud_thinner = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'mud thinner', tag=u'mud_thinner')
StimAdditiveType.mutual_solvent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'mutual solvent', tag=u'mutual_solvent')
StimAdditiveType.oxydizer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'oxydizer', tag=u'oxydizer')
StimAdditiveType.oxygen_scavenger = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'oxygen scavenger', tag=u'oxygen_scavenger')
StimAdditiveType.parafin_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'parafin control', tag=u'parafin_control')
StimAdditiveType.penetrating_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'penetrating agent', tag=u'penetrating_agent')
StimAdditiveType.polymer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'polymer', tag=u'polymer')
StimAdditiveType.proppant_stabilizer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'proppant stabilizer', tag=u'proppant_stabilizer')
StimAdditiveType.radioactive_tracer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'radioactive tracer', tag=u'radioactive_tracer')
StimAdditiveType.raw_acid = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'raw acid', tag=u'raw_acid')
StimAdditiveType.relative_perm_modifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'relative perm modifier', tag=u'relative_perm_modifier')
StimAdditiveType.retarder = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'retarder', tag=u'retarder')
StimAdditiveType.salt = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'salt', tag=u'salt')
StimAdditiveType.sand = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'sand', tag=u'sand')
StimAdditiveType.sand_control_material = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'sand control material', tag=u'sand_control_material')
StimAdditiveType.scale_control_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'scale control additive', tag=u'scale_control_additive')
StimAdditiveType.stabilizer = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'stabilizer', tag=u'stabilizer')
StimAdditiveType.strength_retrogression = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'strength retrogression', tag=u'strength_retrogression')
StimAdditiveType.sulfide_scavenger = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'sulfide scavenger', tag=u'sulfide_scavenger')
StimAdditiveType.surfactant = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'surfactant', tag=u'surfactant')
StimAdditiveType.suspension_agent = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'suspension agent', tag=u'suspension_agent')
StimAdditiveType.tactifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'tactifier', tag=u'tactifier')
StimAdditiveType.viscosifier = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'viscosifier', tag=u'viscosifier')
StimAdditiveType.water_additive = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'water additive', tag=u'water_additive')
StimAdditiveType.water_management_material = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'water management material', tag=u'water_management_material')
StimAdditiveType.pH_control = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'pH control', tag=u'pH_control')
StimAdditiveType.unknown = StimAdditiveType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
StimAdditiveType._InitializeFacetMap(StimAdditiveType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StimAdditiveType', StimAdditiveType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimAnalysisMethod
class StimAnalysisMethod (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The analysis method used for the FET test."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StimAnalysisMethod')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6684, 1)
    _Documentation = u'The analysis method used for the FET test.'
StimAnalysisMethod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimAnalysisMethod, enum_prefix=None)
StimAnalysisMethod.average = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'average', tag=u'average')
StimAnalysisMethod.delta_pressure_over_g_time = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'delta pressure over g-time', tag=u'delta_pressure_over_g_time')
StimAnalysisMethod.delta_pressure_over_linear_time = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'delta pressure over linear time', tag=u'delta_pressure_over_linear_time')
StimAnalysisMethod.delta_pressure_over_radial_time = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'delta pressure over radial time', tag=u'delta_pressure_over_radial_time')
StimAnalysisMethod.gdk_2_d = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'gdk 2-d', tag=u'gdk_2_d')
StimAnalysisMethod.horner = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'horner', tag=u'horner')
StimAnalysisMethod.linear = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'linear', tag=u'linear')
StimAnalysisMethod.log_log = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'log-log', tag=u'log_log')
StimAnalysisMethod.nolte = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'nolte', tag=u'nolte')
StimAnalysisMethod.pdl_coefficient = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'pdl coefficient', tag=u'pdl_coefficient')
StimAnalysisMethod.perkins_and_kern_2_d = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'perkins and kern 2-d', tag=u'perkins_and_kern_2_d')
StimAnalysisMethod.radial_2_d = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'radial 2-d', tag=u'radial_2_d')
StimAnalysisMethod.square_root = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'square root', tag=u'square_root')
StimAnalysisMethod.third_party_software = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'third-party software', tag=u'third_party_software')
StimAnalysisMethod.other = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
StimAnalysisMethod.unknown = StimAnalysisMethod._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
StimAnalysisMethod._InitializeFacetMap(StimAnalysisMethod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StimAnalysisMethod', StimAnalysisMethod)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimFluidSubtype
class StimFluidSubtype (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The fluid sub type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StimFluidSubtype')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 6848, 1)
    _Documentation = u'The fluid sub type.'
StimFluidSubtype._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimFluidSubtype, enum_prefix=None)
StimFluidSubtype.acid = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'acid', tag=u'acid')
StimFluidSubtype.base = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'base', tag=u'base')
StimFluidSubtype.carbon_dioxide = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'carbon dioxide', tag=u'carbon_dioxide')
StimFluidSubtype.carbon_dioxide_and_nitrogen = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'carbon dioxide and nitrogen', tag=u'carbon_dioxide_and_nitrogen')
StimFluidSubtype.carbon_dioxide_and_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'carbon dioxide and water', tag=u'carbon_dioxide_and_water')
StimFluidSubtype.condensate = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'condensate', tag=u'condensate')
StimFluidSubtype.cross_linked_gel = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'cross-linked gel', tag=u'cross_linked_gel')
StimFluidSubtype.crude_oil = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'crude oil', tag=u'crude_oil')
StimFluidSubtype.diesel = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'diesel', tag=u'diesel')
StimFluidSubtype.foam = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'foam', tag=u'foam')
StimFluidSubtype.fracturing_oil = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'fracturing oil', tag=u'fracturing_oil')
StimFluidSubtype.fresh_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'fresh water', tag=u'fresh_water')
StimFluidSubtype.gelled_acid = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'gelled acid', tag=u'gelled_acid')
StimFluidSubtype.gelled_condensate = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'gelled condensate', tag=u'gelled_condensate')
StimFluidSubtype.gelled_crude = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'gelled crude', tag=u'gelled_crude')
StimFluidSubtype.gelled_diesel = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'gelled diesel', tag=u'gelled_diesel')
StimFluidSubtype.gelled_oil = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'gelled oil', tag=u'gelled_oil')
StimFluidSubtype.gelled_salt_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'gelled salt water', tag=u'gelled_salt_water')
StimFluidSubtype.hot_condensate = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'hot condensate', tag=u'hot_condensate')
StimFluidSubtype.hot_fresh_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'hot fresh water', tag=u'hot_fresh_water')
StimFluidSubtype.hot_oil = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'hot oil', tag=u'hot_oil')
StimFluidSubtype.hot_salt_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'hot salt water', tag=u'hot_salt_water')
StimFluidSubtype.hybrid = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'hybrid', tag=u'hybrid')
StimFluidSubtype.linear_gel = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'linear gel', tag=u'linear_gel')
StimFluidSubtype.liquefied_petroleum_gas = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'liquefied petroleum gas', tag=u'liquefied_petroleum_gas')
StimFluidSubtype.nitrogen = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'nitrogen', tag=u'nitrogen')
StimFluidSubtype.oil = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'oil', tag=u'oil')
StimFluidSubtype.produced_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'produced water', tag=u'produced_water')
StimFluidSubtype.salt_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'salt water', tag=u'salt_water')
StimFluidSubtype.slick_water = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'slick water', tag=u'slick_water')
StimFluidSubtype.other = StimFluidSubtype._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
StimFluidSubtype._InitializeFacetMap(StimFluidSubtype._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StimFluidSubtype', StimFluidSubtype)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimFluidType
class StimFluidType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The fluid type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StimFluidType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7053, 1)
    _Documentation = u'The fluid type.'
StimFluidType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimFluidType, enum_prefix=None)
StimFluidType.acid_based = StimFluidType._CF_enumeration.addEnumeration(unicode_value=u'acid-based', tag=u'acid_based')
StimFluidType.gas = StimFluidType._CF_enumeration.addEnumeration(unicode_value=u'gas', tag=u'gas')
StimFluidType.oil_based = StimFluidType._CF_enumeration.addEnumeration(unicode_value=u'oil-based', tag=u'oil_based')
StimFluidType.water_based = StimFluidType._CF_enumeration.addEnumeration(unicode_value=u'water-based', tag=u'water_based')
StimFluidType._InitializeFacetMap(StimFluidType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StimFluidType', StimFluidType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimProppantType
class StimProppantType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """
				Sized particles mixed with treatment fluid to hold fractures open after a hydraulic fracturing treatment.
				In addition to naturally occurring sand grains, man-made or specially engineered
				proppants, such as "resin-coated" sand or "high-strength" ceramic materials, may also be
				used. Proppant materials are carefully sorted for size and sphericity to provide an efficient conduit for
				production of fluid from the reservoir to the wellbore.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StimProppantType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7089, 1)
    _Documentation = u'\n\t\t\t\tSized particles mixed with treatment fluid to hold fractures open after a hydraulic fracturing treatment.\n\t\t\t\tIn addition to naturally occurring sand grains, man-made or specially engineered\n\t\t\t\tproppants, such as "resin-coated" sand or "high-strength" ceramic materials, may also be\n\t\t\t\tused. Proppant materials are carefully sorted for size and sphericity to provide an efficient conduit for\n\t\t\t\tproduction of fluid from the reservoir to the wellbore.\n\t\t\t'
StimProppantType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimProppantType, enum_prefix=None)
StimProppantType.sand = StimProppantType._CF_enumeration.addEnumeration(unicode_value=u'sand', tag=u'sand')
StimProppantType.manmade_proppant = StimProppantType._CF_enumeration.addEnumeration(unicode_value=u'manmade proppant', tag=u'manmade_proppant')
StimProppantType.unknown = StimProppantType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
StimProppantType._InitializeFacetMap(StimProppantType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StimProppantType', StimProppantType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimStageFlowPathType
class StimStageFlowPathType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The types of flow paths used in a stimulation job."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StimStageFlowPathType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7120, 1)
    _Documentation = u'The types of flow paths used in a stimulation job.'
StimStageFlowPathType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimStageFlowPathType, enum_prefix=None)
StimStageFlowPathType.annulus = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value=u'annulus', tag=u'annulus')
StimStageFlowPathType.casing = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value=u'casing', tag=u'casing')
StimStageFlowPathType.coiled_tubing = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value=u'coiled tubing', tag=u'coiled_tubing')
StimStageFlowPathType.drill_pipe = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value=u'drill pipe', tag=u'drill_pipe')
StimStageFlowPathType.open_hole = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value=u'open hole', tag=u'open_hole')
StimStageFlowPathType.tubing = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value=u'tubing', tag=u'tubing')
StimStageFlowPathType.tubing_and_annulus = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value=u'tubing and annulus', tag=u'tubing_and_annulus')
StimStageFlowPathType.unknown = StimStageFlowPathType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
StimStageFlowPathType._InitializeFacetMap(StimStageFlowPathType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StimStageFlowPathType', StimStageFlowPathType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StimStageType
class StimStageType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Type of stage for a stimulation job."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StimStageType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7175, 1)
    _Documentation = u'Type of stage for a stimulation job.'
StimStageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StimStageType, enum_prefix=None)
StimStageType.acid = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'acid', tag=u'acid')
StimStageType.acid_spearhead = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'acid spearhead', tag=u'acid_spearhead')
StimStageType.acid_ball_out = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'acid ball out', tag=u'acid_ball_out')
StimStageType.acid_breakdown = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'acid breakdown', tag=u'acid_breakdown')
StimStageType.ball_out = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'ball out', tag=u'ball_out')
StimStageType.breakdown = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'breakdown', tag=u'breakdown')
StimStageType.chemical_wash = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'chemical wash', tag=u'chemical_wash')
StimStageType.circulate = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'circulate', tag=u'circulate')
StimStageType.displacement = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'displacement', tag=u'displacement')
StimStageType.diverter = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'diverter', tag=u'diverter')
StimStageType.fluid_efficiency_test = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'fluid efficiency test', tag=u'fluid_efficiency_test')
StimStageType.flowback = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'flowback', tag=u'flowback')
StimStageType.flush = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'flush', tag=u'flush')
StimStageType.foamed_acid = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'foamed acid', tag=u'foamed_acid')
StimStageType.hydrajet = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'hydrajet', tag=u'hydrajet')
StimStageType.load_well = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'load well', tag=u'load_well')
StimStageType.load_annulus = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'load annulus', tag=u'load_annulus')
StimStageType.overflush = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'overflush', tag=u'overflush')
StimStageType.pad = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'pad', tag=u'pad')
StimStageType.pump_in = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'pump-in', tag=u'pump_in')
StimStageType.pre_Job = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'pre-Job', tag=u'pre_Job')
StimStageType.pre_flush = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'pre-flush', tag=u'pre_flush')
StimStageType.pre_pad = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'pre-pad', tag=u'pre_pad')
StimStageType.shut_in = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'shut-in', tag=u'shut_in')
StimStageType.shut_in_for_FET_analysis = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'shut-in for FET analysis', tag=u'shut_in_for_FET_analysis')
StimStageType.proppant_laden_fluid = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'proppant laden fluid', tag=u'proppant_laden_fluid')
StimStageType.slurry = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'slurry', tag=u'slurry')
StimStageType.sand_slug = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'sand slug', tag=u'sand_slug')
StimStageType.spacer = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'spacer', tag=u'spacer')
StimStageType.spot_acid = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'spot acid', tag=u'spot_acid')
StimStageType.step_rate_test = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'step rate test', tag=u'step_rate_test')
StimStageType.treatment = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'treatment', tag=u'treatment')
StimStageType.other = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
StimStageType.unknown = StimStageType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
StimStageType._InitializeFacetMap(StimStageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StimStageType', StimStageType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}SupportCraft
class SupportCraft (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SupportCraft')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7365, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}SurfEquipType
class SurfEquipType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Surface Equipment Type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SurfEquipType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7412, 1)
    _Documentation = u'Surface Equipment Type.'
SurfEquipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SurfEquipType, enum_prefix=None)
SurfEquipType.IADC = SurfEquipType._CF_enumeration.addEnumeration(unicode_value=u'IADC', tag=u'IADC')
SurfEquipType.custom = SurfEquipType._CF_enumeration.addEnumeration(unicode_value=u'custom', tag=u'custom')
SurfEquipType.coiled_tubing = SurfEquipType._CF_enumeration.addEnumeration(unicode_value=u'coiled tubing', tag=u'coiled_tubing')
SurfEquipType.unknown = SurfEquipType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
SurfEquipType._InitializeFacetMap(SurfEquipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SurfEquipType', SurfEquipType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}SurveyToolOperatingMode
class SurveyToolOperatingMode (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The codes for the iscwsa survey tool operating modes."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SurveyToolOperatingMode')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7442, 1)
    _Documentation = u'The codes for the iscwsa survey tool operating modes.'
SurveyToolOperatingMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SurveyToolOperatingMode, enum_prefix=None)
SurveyToolOperatingMode.stationary = SurveyToolOperatingMode._CF_enumeration.addEnumeration(unicode_value=u'stationary', tag=u'stationary')
SurveyToolOperatingMode.continuous_XY = SurveyToolOperatingMode._CF_enumeration.addEnumeration(unicode_value=u'continuous XY', tag=u'continuous_XY')
SurveyToolOperatingMode.continuous_Z = SurveyToolOperatingMode._CF_enumeration.addEnumeration(unicode_value=u'continuous Z', tag=u'continuous_Z')
SurveyToolOperatingMode.continuous_XYZ = SurveyToolOperatingMode._CF_enumeration.addEnumeration(unicode_value=u'continuous XYZ', tag=u'continuous_XYZ')
SurveyToolOperatingMode.unknown = SurveyToolOperatingMode._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
SurveyToolOperatingMode._InitializeFacetMap(SurveyToolOperatingMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SurveyToolOperatingMode', SurveyToolOperatingMode)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TargetCategory
class TargetCategory (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TargetCategory')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7482, 1)
    _Documentation = None
TargetCategory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetCategory, enum_prefix=None)
TargetCategory.geological = TargetCategory._CF_enumeration.addEnumeration(unicode_value=u'geological', tag=u'geological')
TargetCategory.unknown = TargetCategory._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TargetCategory._InitializeFacetMap(TargetCategory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TargetCategory', TargetCategory)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TargetScope
class TargetScope (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of scope of the drilling target. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TargetScope')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7499, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}TargetSectionScope
class TargetSectionScope (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of scope of a section that describes a target. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TargetSectionScope')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7565, 1)
    _Documentation = u'These values represent the type of scope of a section that describes a target. '
TargetSectionScope._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TargetSectionScope, enum_prefix=None)
TargetSectionScope.arc = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value=u'arc', tag=u'arc')
TargetSectionScope.line = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value=u'line', tag=u'line')
TargetSectionScope.unknown = TargetSectionScope._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TargetSectionScope._InitializeFacetMap(TargetSectionScope._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TargetSectionScope', TargetSectionScope)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TrajStnCalcAlgorithm
class TrajStnCalcAlgorithm (abstractTypeEnum):

    """Trajectory Station Calculation Algorithm.
			The list of standard values is contained in the WITSML enumValues.xml file. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TrajStnCalcAlgorithm')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7590, 1)
    _Documentation = u'Trajectory Station Calculation Algorithm.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file. '
TrajStnCalcAlgorithm._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'TrajStnCalcAlgorithm', TrajStnCalcAlgorithm)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TrajStationStatus
class TrajStationStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """Trajectory Station Status."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TrajStationStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7599, 1)
    _Documentation = u'Trajectory Station Status.'
TrajStationStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TrajStationStatus, enum_prefix=None)
TrajStationStatus.open = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value=u'open', tag=u'open')
TrajStationStatus.rejected = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value=u'rejected', tag=u'rejected')
TrajStationStatus.position = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value=u'position', tag=u'position')
TrajStationStatus.unknown = TrajStationStatus._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
TrajStationStatus._InitializeFacetMap(TrajStationStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TrajStationStatus', TrajStationStatus)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TrajStationType
class TrajStationType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the type of a directional survey station. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TrajStationType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7634, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}TubularAssembly
class TubularAssembly (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TubularAssembly')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7900, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}TubularComponent
class TubularComponent (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TubularComponent')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 7977, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}TypeSurveyTool
class TypeSurveyTool (abstractTypeEnum):

    """Type of direcional survey tool; a very generic classification.
			The list of standard values is contained in the WITSML enumValues.xml file."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TypeSurveyTool')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 8804, 1)
    _Documentation = u'Type of direcional survey tool; a very generic classification.\n\t\t\tThe list of standard values is contained in the WITSML enumValues.xml file.'
TypeSurveyTool._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'TypeSurveyTool', TypeSurveyTool)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellControlIncidentType
class WellControlIncidentType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellControlIncidentType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 8813, 1)
    _Documentation = ''
WellControlIncidentType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellControlIncidentType, enum_prefix=None)
WellControlIncidentType.shallow_gas_kick = WellControlIncidentType._CF_enumeration.addEnumeration(unicode_value=u'shallow gas kick', tag=u'shallow_gas_kick')
WellControlIncidentType.water_kick = WellControlIncidentType._CF_enumeration.addEnumeration(unicode_value=u'water kick', tag=u'water_kick')
WellControlIncidentType.oil_kick = WellControlIncidentType._CF_enumeration.addEnumeration(unicode_value=u'oil kick', tag=u'oil_kick')
WellControlIncidentType.gas_kick = WellControlIncidentType._CF_enumeration.addEnumeration(unicode_value=u'gas kick', tag=u'gas_kick')
WellControlIncidentType.unknown = WellControlIncidentType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellControlIncidentType._InitializeFacetMap(WellControlIncidentType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellControlIncidentType', WellControlIncidentType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellDirection
class WellDirection (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The direction of flow of the fluids in a well facility
			(generally, injected or produced, or some combination)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellDirection')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 8852, 1)
    _Documentation = u'The direction of flow of the fluids in a well facility\n\t\t\t(generally, injected or produced, or some combination).'
WellDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellDirection, enum_prefix=None)
WellDirection.huff_n_puff = WellDirection._CF_enumeration.addEnumeration(unicode_value=u'huff-n-puff', tag=u'huff_n_puff')
WellDirection.injector = WellDirection._CF_enumeration.addEnumeration(unicode_value=u'injector', tag=u'injector')
WellDirection.producer = WellDirection._CF_enumeration.addEnumeration(unicode_value=u'producer', tag=u'producer')
WellDirection.uncertain = WellDirection._CF_enumeration.addEnumeration(unicode_value=u'uncertain', tag=u'uncertain')
WellDirection.unknown = WellDirection._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellDirection._InitializeFacetMap(WellDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellDirection', WellDirection)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellFluid
class WellFluid (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The type of fluid being produced from or injected 
			into a well facility."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellFluid')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 8893, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellKillingProcedureType
class WellKillingProcedureType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellKillingProcedureType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9010, 1)
    _Documentation = ''
WellKillingProcedureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellKillingProcedureType, enum_prefix=None)
WellKillingProcedureType.drillers_method = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value=u'drillers method', tag=u'drillers_method')
WellKillingProcedureType.wait_and_weight = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value=u'wait and weight', tag=u'wait_and_weight')
WellKillingProcedureType.bullheading = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value=u'bullheading', tag=u'bullheading')
WellKillingProcedureType.lubricate_and_bleed = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value=u'lubricate and bleed', tag=u'lubricate_and_bleed')
WellKillingProcedureType.forward_circulation = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value=u'forward circulation', tag=u'forward_circulation')
WellKillingProcedureType.reverse_circulation = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value=u'reverse circulation', tag=u'reverse_circulation')
WellKillingProcedureType.unknown = WellKillingProcedureType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellKillingProcedureType._InitializeFacetMap(WellKillingProcedureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellKillingProcedureType', WellKillingProcedureType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellNamingSystem
class WellNamingSystem (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The types of well/wellbore naming systems."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellNamingSystem')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9070, 1)
    _Documentation = u'The types of well/wellbore naming systems.'
WellNamingSystem._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellNamingSystem, enum_prefix=None)
WellNamingSystem.DTI = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value=u'DTI', tag=u'DTI')
WellNamingSystem.API = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value=u'API', tag=u'API')
WellNamingSystem.NPD_code = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value=u'NPD code', tag=u'NPD_code')
WellNamingSystem.NPD_number = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value=u'NPD number', tag=u'NPD_number')
WellNamingSystem.local_field = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value=u'local field', tag=u'local_field')
WellNamingSystem.prospect = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value=u'prospect', tag=u'prospect')
WellNamingSystem.unknown = WellNamingSystem._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellNamingSystem._InitializeFacetMap(WellNamingSystem._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellNamingSystem', WellNamingSystem)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellTestType
class WellTestType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellTestType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9116, 1)
    _Documentation = ''
WellTestType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellTestType, enum_prefix=None)
WellTestType.drill_stem_test = WellTestType._CF_enumeration.addEnumeration(unicode_value=u'drill stem test', tag=u'drill_stem_test')
WellTestType.production_test = WellTestType._CF_enumeration.addEnumeration(unicode_value=u'production test', tag=u'production_test')
WellTestType.unknown = WellTestType._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
WellTestType._InitializeFacetMap(WellTestType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellTestType', WellTestType)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellboreShape
class WellboreShape (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the classification of a wellbore 
			based on its shape. The source of the values and the descriptions is the 
			POSC V2.2 "facility class" standard instance values in classification system 
			"POSC wellbore trajectory shape". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellboreShape')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9144, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellboreType
class WellboreType (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """The classification of a wellbore with respect to its parent 
			well/wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellboreType')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9200, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellPurpose
class WellPurpose (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the classification of a well or 
			wellbore by the purpose for which it was initially drilled."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellPurpose')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9256, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellStatus
class WellStatus (abstractTypeEnum, pyxb.binding.basis.enumeration_mixin):

    """These values represent the status of a well or wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_catalog.xsd', 9392, 1)
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

# Atomic simple type: {http://www.witsml.org/schemas/1series}timeZone
class timeZone (abstractTimeZone):

    """A time zone conforming to the XSD:dateTime specification."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeZone')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 51, 1)
    _Documentation = u'A time zone conforming to the XSD:dateTime specification.'
timeZone._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'timeZone', timeZone)

# List simple type: {http://www.witsml.org/schemas/1series}listOfString
# superclasses pyxb.binding.datatypes.anySimpleType
class listOfString (pyxb.binding.basis.STD_list):

    """A representation of a list of xsd:string values,
			restricted to strings without embedded whitespace."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'listOfString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 214, 1)
    _Documentation = u'A representation of a list of xsd:string values,\n\t\t\trestricted to strings without embedded whitespace.'

    _ItemType = abstractString32
listOfString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'listOfString', listOfString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}uidString
class uidString (abstractUidString):

    """A locally unique identifier. 
			The value is not intended to convey any semantic content (e.g., it may be computer generated). """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'uidString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 226, 1)
    _Documentation = u'A locally unique identifier. \n\t\t\tThe value is not intended to convey any semantic content (e.g., it may be computer generated). '
uidString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'uidString', uidString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}uidParentString
class uidParentString (abstractUidString):

    """A unique identifier of an object parent. 
			This should only be used for the uid of a parent object (i.e., a foreign key to another object). 
			It should not be used for child nodes of an object.
			The value is not intended to convey any semantic content (e.g., it may be computer generated).
			The purpose of this type is to facilitate modifying the optionality of parentage uids in derived schemas."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'uidParentString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 235, 1)
    _Documentation = u'A unique identifier of an object parent. \n\t\t\tThis should only be used for the uid of a parent object (i.e., a foreign key to another object). \n\t\t\tIt should not be used for child nodes of an object.\n\t\t\tThe value is not intended to convey any semantic content (e.g., it may be computer generated).\n\t\t\tThe purpose of this type is to facilitate modifying the optionality of parentage uids in derived schemas.'
uidParentString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'uidParentString', uidParentString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}refString
class refString (abstractUidString):

    """A reference to the unique identifier of another element. 
			This value represents a foreign key from one element to another.
			The value should match the value of an attribute of type uidString."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'refString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 247, 1)
    _Documentation = u'A reference to the unique identifier of another element. \n\t\t\tThis value represents a foreign key from one element to another.\n\t\t\tThe value should match the value of an attribute of type uidString.'
refString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'refString', refString)

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

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'refWellDatum')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 316, 1)
    _Documentation = u"A reference to a wellDatum in the current well. \n\t\t\tThis value must match the uid value in a WellDatum. \n\t\t\tThis value represents a foreign key from one element to another.\n\t\t\tThis is an exception to the convention that a foreign key must utilize both \n\t\t\ta human contextual name and a uid value. For messages outside the context of\n\t\t\ta server then this value will commonly match the value of the name of the \n\t\t\twellDatum (e.g., 'KB') if uids are not not used in that context.\n\t\t\tThis was a compromise in order to allow the coordinate structures to be simple\n\t\t\tand still be usable both within the context of a server and outside the context of a server."
refWellDatum._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'refWellDatum', refWellDatum)

# Atomic simple type: {http://www.witsml.org/schemas/1series}nameString
class nameString (abstractNameString):

    """A user assigned human recognizable contextual name of something. 
			There should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.
			This type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 333, 1)
    _Documentation = u'A user assigned human recognizable contextual name of something. \n\t\t\tThere should be no assumption that (interoperable) semantic information will be extracted from the name by a third party.\n\t\t\tThis type of value is generally not guaranteed to be unique and is not a candidate to be replaced by an enumeration.'
nameString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'nameString', nameString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}descriptionString
class descriptionString (abstractDescriptionString):

    """A textual description of something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'descriptionString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 352, 1)
    _Documentation = u'A textual description of something.'
descriptionString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'descriptionString', descriptionString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}encodedValueString
class encodedValueString (abstractString32):

    """A single value. The encoding may utilize 
			any of several xsd encodings. Something external to the value must
			define the encoding."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'encodedValueString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 381, 1)
    _Documentation = u'A single value. The encoding may utilize \n\t\t\tany of several xsd encodings. Something external to the value must\n\t\t\tdefine the encoding.'
encodedValueString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'encodedValueString', encodedValueString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}kindString
class kindString (abstractTypeEnum):

    """A community assigned human recognizable name. 
			This type of value is intended to be unique and is generally a candidate to be constrained to an enumerated list."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'kindString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 410, 1)
    _Documentation = u'A community assigned human recognizable name. \n\t\t\tThis type of value is intended to be unique and is generally a candidate to be constrained to an enumerated list.'
kindString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'kindString', kindString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}uomString
class uomString (abstractUomEnum):

    """A unit of measure acronym from the POSC unit of measure file."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'uomString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 419, 1)
    _Documentation = u'A unit of measure acronym from the POSC unit of measure file.'
uomString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'uomString', uomString)

# Atomic simple type: {http://www.witsml.org/schemas/1series}positiveCount
class positiveCount (abstractPositiveCount):

    """A positive integer (one based count or index)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positiveCount')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 766, 1)
    _Documentation = u'A positive integer (one based count or index).'
positiveCount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=positiveCount, value=pyxb.binding.datatypes.short(1))
positiveCount._InitializeFacetMap(positiveCount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'positiveCount', positiveCount)

# Atomic simple type: {http://www.witsml.org/schemas/1series}str32
class str32 (abstractString32):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'str32')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 896, 1)
    _Documentation = ''
str32._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'str32', str32)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PercentUom
class PercentUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PercentUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 31, 1)
    _Documentation = ''
PercentUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PercentUom, enum_prefix=None)
PercentUom.emptyString = PercentUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
PercentUom._InitializeFacetMap(PercentUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PercentUom', PercentUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MeasuredDepthUom
class MeasuredDepthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """The units of measure that are valid for measured depths in a wellbore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MeasuredDepthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 40, 1)
    _Documentation = u'The units of measure that are valid for measured depths in a wellbore.'
MeasuredDepthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MeasuredDepthUom, enum_prefix=None)
MeasuredDepthUom.m = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value=u'm', tag=u'm')
MeasuredDepthUom.ft = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value=u'ft', tag=u'ft')
MeasuredDepthUom.ftUS = MeasuredDepthUom._CF_enumeration.addEnumeration(unicode_value=u'ftUS', tag=u'ftUS')
MeasuredDepthUom._InitializeFacetMap(MeasuredDepthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MeasuredDepthUom', MeasuredDepthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}WellVerticalCoordinateUom
class WellVerticalCoordinateUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """The units of measure that are valid for vertical gravity based 
			coordinates (i.e., elevation or vertical depth) within the context of a well."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WellVerticalCoordinateUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 64, 1)
    _Documentation = u'The units of measure that are valid for vertical gravity based \n\t\t\tcoordinates (i.e., elevation or vertical depth) within the context of a well.'
WellVerticalCoordinateUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WellVerticalCoordinateUom, enum_prefix=None)
WellVerticalCoordinateUom.m = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value=u'm', tag=u'm')
WellVerticalCoordinateUom.ft = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value=u'ft', tag=u'ft')
WellVerticalCoordinateUom.ftUS = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value=u'ftUS', tag=u'ftUS')
WellVerticalCoordinateUom.ftBr65 = WellVerticalCoordinateUom._CF_enumeration.addEnumeration(unicode_value=u'ftBr(65)', tag=u'ftBr65')
WellVerticalCoordinateUom._InitializeFacetMap(WellVerticalCoordinateUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'WellVerticalCoordinateUom', WellVerticalCoordinateUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AccelerationLinearUom
class AccelerationLinearUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AccelerationLinearUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 97, 1)
    _Documentation = ''
AccelerationLinearUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AccelerationLinearUom, enum_prefix=None)
AccelerationLinearUom.ms2 = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'm/s2', tag=u'ms2')
AccelerationLinearUom.cms2 = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'cm/s2', tag=u'cms2')
AccelerationLinearUom.fts2 = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'ft/s2', tag=u'fts2')
AccelerationLinearUom.Gal = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'Gal', tag=u'Gal')
AccelerationLinearUom.mgn = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'mgn', tag=u'mgn')
AccelerationLinearUom.gn = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'gn', tag=u'gn')
AccelerationLinearUom.mGal = AccelerationLinearUom._CF_enumeration.addEnumeration(unicode_value=u'mGal', tag=u'mGal')
AccelerationLinearUom._InitializeFacetMap(AccelerationLinearUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AccelerationLinearUom', AccelerationLinearUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AnglePerLengthUom
class AnglePerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AnglePerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 112, 1)
    _Documentation = ''
AnglePerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AnglePerLengthUom, enum_prefix=None)
AnglePerLengthUom.radm = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'rad/m', tag=u'radm')
AnglePerLengthUom.dega30ft = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dega/30ft', tag=u'dega30ft')
AnglePerLengthUom.degaft = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dega/ft', tag=u'degaft')
AnglePerLengthUom.dega100ft = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dega/100ft', tag=u'dega100ft')
AnglePerLengthUom.degam = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dega/m', tag=u'degam')
AnglePerLengthUom.dega30m = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dega/30m', tag=u'dega30m')
AnglePerLengthUom.radft = AnglePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'rad/ft', tag=u'radft')
AnglePerLengthUom._InitializeFacetMap(AnglePerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AnglePerLengthUom', AnglePerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AnglePerTimeUom
class AnglePerTimeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AnglePerTimeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 127, 1)
    _Documentation = ''
AnglePerTimeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AnglePerTimeUom, enum_prefix=None)
AnglePerTimeUom.rads = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'rad/s', tag=u'rads')
AnglePerTimeUom.cs = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'c/s', tag=u'cs')
AnglePerTimeUom.degah = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'dega/h', tag=u'degah')
AnglePerTimeUom.degamin = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'dega/min', tag=u'degamin')
AnglePerTimeUom.degas = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'dega/s', tag=u'degas')
AnglePerTimeUom.revs = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'rev/s', tag=u'revs')
AnglePerTimeUom.rpm = AnglePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'rpm', tag=u'rpm')
AnglePerTimeUom._InitializeFacetMap(AnglePerTimeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AnglePerTimeUom', AnglePerTimeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AreaUom
class AreaUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AreaUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 142, 1)
    _Documentation = ''
AreaUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AreaUom, enum_prefix=None)
AreaUom.m2 = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'm2', tag=u'm2')
AreaUom.acre = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'acre', tag=u'acre')
AreaUom.b = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'b', tag=u'b')
AreaUom.cm2 = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'cm2', tag=u'cm2')
AreaUom.ft2 = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'ft2', tag=u'ft2')
AreaUom.ha = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'ha', tag=u'ha')
AreaUom.in2 = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'in2', tag=u'in2')
AreaUom.km2 = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'km2', tag=u'km2')
AreaUom.mi2 = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'mi2', tag=u'mi2')
AreaUom.miUS2 = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'miUS2', tag=u'miUS2')
AreaUom.mm2 = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'mm2', tag=u'mm2')
AreaUom.um2 = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'um2', tag=u'um2')
AreaUom.yd2 = AreaUom._CF_enumeration.addEnumeration(unicode_value=u'yd2', tag=u'yd2')
AreaUom._InitializeFacetMap(AreaUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AreaUom', AreaUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}AreaPerAreaUom
class AreaPerAreaUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AreaPerAreaUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 163, 1)
    _Documentation = ''
AreaPerAreaUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AreaPerAreaUom, enum_prefix=None)
AreaPerAreaUom.Euc = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'Euc', tag=u'Euc')
AreaPerAreaUom.emptyString = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
AreaPerAreaUom.in2ft2 = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'in2/ft2', tag=u'in2ft2')
AreaPerAreaUom.in2in2 = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'in2/in2', tag=u'in2in2')
AreaPerAreaUom.m2m2 = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'm2/m2', tag=u'm2m2')
AreaPerAreaUom.mm2mm2 = AreaPerAreaUom._CF_enumeration.addEnumeration(unicode_value=u'mm2/mm2', tag=u'mm2mm2')
AreaPerAreaUom._InitializeFacetMap(AreaPerAreaUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AreaPerAreaUom', AreaPerAreaUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}CompressibilityUom
class CompressibilityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CompressibilityUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 177, 1)
    _Documentation = ''
CompressibilityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CompressibilityUom, enum_prefix=None)
CompressibilityUom.n1psi = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value=u'1/psi', tag=u'n1psi')
CompressibilityUom.n1upsi = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value=u'1/upsi', tag=u'n1upsi')
CompressibilityUom.n1Pa = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value=u'1/Pa', tag=u'n1Pa')
CompressibilityUom.n1bar = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value=u'1/bar', tag=u'n1bar')
CompressibilityUom.n1kPa = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value=u'1/kPa', tag=u'n1kPa')
CompressibilityUom.n1pPa = CompressibilityUom._CF_enumeration.addEnumeration(unicode_value=u'1/pPa', tag=u'n1pPa')
CompressibilityUom._InitializeFacetMap(CompressibilityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CompressibilityUom', CompressibilityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DensityUom
class DensityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DensityUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 191, 1)
    _Documentation = ''
DensityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DensityUom, enum_prefix=None)
DensityUom.kgm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'kg/m3', tag=u'kgm3')
DensityUom.n10Mgm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'10Mg/m3', tag=u'n10Mgm3')
DensityUom.dAPI = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'dAPI', tag=u'dAPI')
DensityUom.gcm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'g/cm3', tag=u'gcm3')
DensityUom.gdm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'g/dm3', tag=u'gdm3')
DensityUom.ggalUK = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'g/galUK', tag=u'ggalUK')
DensityUom.ggalUS = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'g/galUS', tag=u'ggalUS')
DensityUom.gL = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'g/L', tag=u'gL')
DensityUom.gm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'g/m3', tag=u'gm3')
DensityUom.grainft3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'grain/ft3', tag=u'grainft3')
DensityUom.graingalUS = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'grain/galUS', tag=u'graingalUS')
DensityUom.grain100ft3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'grain/100ft3', tag=u'grain100ft3')
DensityUom.kgdm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'kg/dm3', tag=u'kgdm3')
DensityUom.kgL = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'kg/L', tag=u'kgL')
DensityUom.Mgm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'Mg/m3', tag=u'Mgm3')
DensityUom.lbm10bbl = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/10bbl', tag=u'lbm10bbl')
DensityUom.lbmbbl = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/bbl', tag=u'lbmbbl')
DensityUom.lbmft3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/ft3', tag=u'lbmft3')
DensityUom.lbmgalUK = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/galUK', tag=u'lbmgalUK')
DensityUom.lbm1000galUK = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/1000galUK', tag=u'lbm1000galUK')
DensityUom.lbmgalUS = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/galUS', tag=u'lbmgalUS')
DensityUom.lbm1000galUS = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/1000galUS', tag=u'lbm1000galUS')
DensityUom.lbmin3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/in3', tag=u'lbmin3')
DensityUom.lbmMbbl = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/Mbbl', tag=u'lbmMbbl')
DensityUom.mgdm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'mg/dm3', tag=u'mgdm3')
DensityUom.mggalUS = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'mg/galUS', tag=u'mggalUS')
DensityUom.mgL = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'mg/L', tag=u'mgL')
DensityUom.mgm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'mg/m3', tag=u'mgm3')
DensityUom.ugcm3 = DensityUom._CF_enumeration.addEnumeration(unicode_value=u'ug/cm3', tag=u'ugcm3')
DensityUom._InitializeFacetMap(DensityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DensityUom', DensityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DimensionlessUom
class DimensionlessUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DimensionlessUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 228, 1)
    _Documentation = ''
DimensionlessUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DimensionlessUom, enum_prefix=None)
DimensionlessUom.Euc = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'Euc', tag=u'Euc')
DimensionlessUom.emptyString = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
DimensionlessUom.cEuc = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'cEuc', tag=u'cEuc')
DimensionlessUom.mEuc = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'mEuc', tag=u'mEuc')
DimensionlessUom.nEuc = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'nEuc', tag=u'nEuc')
DimensionlessUom.uEuc = DimensionlessUom._CF_enumeration.addEnumeration(unicode_value=u'uEuc', tag=u'uEuc')
DimensionlessUom._InitializeFacetMap(DimensionlessUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DimensionlessUom', DimensionlessUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}DynamicViscosityUom
class DynamicViscosityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DynamicViscosityUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 242, 1)
    _Documentation = ''
DynamicViscosityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DynamicViscosityUom, enum_prefix=None)
DynamicViscosityUom.Pa_s = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'Pa.s', tag=u'Pa_s')
DynamicViscosityUom.cP = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'cP', tag=u'cP')
DynamicViscosityUom.P = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'P', tag=u'P')
DynamicViscosityUom.psi_s = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'psi.s', tag=u'psi_s')
DynamicViscosityUom.dyne_scm2 = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'dyne.s/cm2', tag=u'dyne_scm2')
DynamicViscosityUom.kgf_sm2 = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'kgf.s/m2', tag=u'kgf_sm2')
DynamicViscosityUom.lbf_sft2 = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'lbf.s/ft2', tag=u'lbf_sft2')
DynamicViscosityUom.lbf_sin2 = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'lbf.s/in2', tag=u'lbf_sin2')
DynamicViscosityUom.mPa_s = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'mPa.s', tag=u'mPa_s')
DynamicViscosityUom.N_sm2 = DynamicViscosityUom._CF_enumeration.addEnumeration(unicode_value=u'N.s/m2', tag=u'N_sm2')
DynamicViscosityUom._InitializeFacetMap(DynamicViscosityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'DynamicViscosityUom', DynamicViscosityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ElectricCurrentUom
class ElectricCurrentUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ElectricCurrentUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 260, 1)
    _Documentation = ''
ElectricCurrentUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ElectricCurrentUom, enum_prefix=None)
ElectricCurrentUom.A = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'A', tag=u'A')
ElectricCurrentUom.MA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'MA', tag=u'MA')
ElectricCurrentUom.kA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'kA', tag=u'kA')
ElectricCurrentUom.mA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'mA', tag=u'mA')
ElectricCurrentUom.nA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'nA', tag=u'nA')
ElectricCurrentUom.pA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'pA', tag=u'pA')
ElectricCurrentUom.uA = ElectricCurrentUom._CF_enumeration.addEnumeration(unicode_value=u'uA', tag=u'uA')
ElectricCurrentUom._InitializeFacetMap(ElectricCurrentUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ElectricCurrentUom', ElectricCurrentUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ElectricPotentialUom
class ElectricPotentialUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ElectricPotentialUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 275, 1)
    _Documentation = ''
ElectricPotentialUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ElectricPotentialUom, enum_prefix=None)
ElectricPotentialUom.V = ElectricPotentialUom._CF_enumeration.addEnumeration(unicode_value=u'V', tag=u'V')
ElectricPotentialUom.kV = ElectricPotentialUom._CF_enumeration.addEnumeration(unicode_value=u'kV', tag=u'kV')
ElectricPotentialUom.mV = ElectricPotentialUom._CF_enumeration.addEnumeration(unicode_value=u'mV', tag=u'mV')
ElectricPotentialUom.MV = ElectricPotentialUom._CF_enumeration.addEnumeration(unicode_value=u'MV', tag=u'MV')
ElectricPotentialUom.uV = ElectricPotentialUom._CF_enumeration.addEnumeration(unicode_value=u'uV', tag=u'uV')
ElectricPotentialUom._InitializeFacetMap(ElectricPotentialUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ElectricPotentialUom', ElectricPotentialUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}EquivalentPerMassUom
class EquivalentPerMassUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EquivalentPerMassUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 292, 1)
    _Documentation = ''
EquivalentPerMassUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EquivalentPerMassUom, enum_prefix=None)
EquivalentPerMassUom.eqkg = EquivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value=u'eq/kg', tag=u'eqkg')
EquivalentPerMassUom.meqg = EquivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value=u'meq/g', tag=u'meqg')
EquivalentPerMassUom.meq100g = EquivalentPerMassUom._CF_enumeration.addEnumeration(unicode_value=u'meq/100g', tag=u'meq100g')
EquivalentPerMassUom._InitializeFacetMap(EquivalentPerMassUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'EquivalentPerMassUom', EquivalentPerMassUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ForceUom
class ForceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ForceUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 303, 1)
    _Documentation = ''
ForceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ForceUom, enum_prefix=None)
ForceUom.N = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'N', tag=u'N')
ForceUom.daN = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'daN', tag=u'daN')
ForceUom.dyne = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'dyne', tag=u'dyne')
ForceUom.gf = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'gf', tag=u'gf')
ForceUom.kdyne = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'kdyne', tag=u'kdyne')
ForceUom.kgf = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'kgf', tag=u'kgf')
ForceUom.klbf = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'klbf', tag=u'klbf')
ForceUom.kN = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'kN', tag=u'kN')
ForceUom.lbf = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'lbf', tag=u'lbf')
ForceUom.Mgf = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'Mgf', tag=u'Mgf')
ForceUom.mN = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'mN', tag=u'mN')
ForceUom.MN = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'MN', tag=u'MN')
ForceUom.ozf = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'ozf', tag=u'ozf')
ForceUom.pdl = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'pdl', tag=u'pdl')
ForceUom.tonfUK = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUK', tag=u'tonfUK')
ForceUom.tonfUS = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS', tag=u'tonfUS')
ForceUom.uN = ForceUom._CF_enumeration.addEnumeration(unicode_value=u'uN', tag=u'uN')
ForceUom._InitializeFacetMap(ForceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ForceUom', ForceUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ForcePerLengthUom
class ForcePerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ForcePerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 328, 1)
    _Documentation = ''
ForcePerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ForcePerLengthUom, enum_prefix=None)
ForcePerLengthUom.N30m = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'N/30m', tag=u'N30m')
ForcePerLengthUom.Nm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'N/m', tag=u'Nm')
ForcePerLengthUom.dynecm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dyne/cm', tag=u'dynecm')
ForcePerLengthUom.kNm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'kN/m', tag=u'kNm')
ForcePerLengthUom.kgfcm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'kgf/cm', tag=u'kgfcm')
ForcePerLengthUom.lbf100ft = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/100ft', tag=u'lbf100ft')
ForcePerLengthUom.lbf30m = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/30m', tag=u'lbf30m')
ForcePerLengthUom.lbfft = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/ft', tag=u'lbfft')
ForcePerLengthUom.lbfin = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/in', tag=u'lbfin')
ForcePerLengthUom.mNkm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'mN/km', tag=u'mNkm')
ForcePerLengthUom.mNm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'mN/m', tag=u'mNm')
ForcePerLengthUom.pdlcm = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'pdl/cm', tag=u'pdlcm')
ForcePerLengthUom.tonfUKft = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUK/ft', tag=u'tonfUKft')
ForcePerLengthUom.tonfUSft = ForcePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS/ft', tag=u'tonfUSft')
ForcePerLengthUom._InitializeFacetMap(ForcePerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ForcePerLengthUom', ForcePerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ForcePerVolumeUom
class ForcePerVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ForcePerVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 350, 1)
    _Documentation = ''
ForcePerVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ForcePerVolumeUom, enum_prefix=None)
ForcePerVolumeUom.Nm3 = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'N/m3', tag=u'Nm3')
ForcePerVolumeUom.atm100m = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'atm/100m', tag=u'atm100m')
ForcePerVolumeUom.atmm = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'atm/m', tag=u'atmm')
ForcePerVolumeUom.barkm = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bar/km', tag=u'barkm')
ForcePerVolumeUom.barm = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bar/m', tag=u'barm')
ForcePerVolumeUom.GPacm = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'GPa/cm', tag=u'GPacm')
ForcePerVolumeUom.kPa100m = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'kPa/100m', tag=u'kPa100m')
ForcePerVolumeUom.kPam = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'kPa/m', tag=u'kPam')
ForcePerVolumeUom.lbfft3 = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/ft3', tag=u'lbfft3')
ForcePerVolumeUom.lbfgalUS = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/galUS', tag=u'lbfgalUS')
ForcePerVolumeUom.MPam = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'MPa/m', tag=u'MPam')
ForcePerVolumeUom.psift = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'psi/ft', tag=u'psift')
ForcePerVolumeUom.psi100ft = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'psi/100ft', tag=u'psi100ft')
ForcePerVolumeUom.psikft = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'psi/kft', tag=u'psikft')
ForcePerVolumeUom.psim = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'psi/m', tag=u'psim')
ForcePerVolumeUom.Pam = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Pa/m', tag=u'Pam')
ForcePerVolumeUom.atmft = ForcePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'atm/ft', tag=u'atmft')
ForcePerVolumeUom._InitializeFacetMap(ForcePerVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ForcePerVolumeUom', ForcePerVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}IlluminanceUom
class IlluminanceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IlluminanceUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 375, 1)
    _Documentation = ''
IlluminanceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IlluminanceUom, enum_prefix=None)
IlluminanceUom.lx = IlluminanceUom._CF_enumeration.addEnumeration(unicode_value=u'lx', tag=u'lx')
IlluminanceUom.lmm2 = IlluminanceUom._CF_enumeration.addEnumeration(unicode_value=u'lm/m2', tag=u'lmm2')
IlluminanceUom.footcandle = IlluminanceUom._CF_enumeration.addEnumeration(unicode_value=u'footcandle', tag=u'footcandle')
IlluminanceUom.klx = IlluminanceUom._CF_enumeration.addEnumeration(unicode_value=u'klx', tag=u'klx')
IlluminanceUom._InitializeFacetMap(IlluminanceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'IlluminanceUom', IlluminanceUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LengthUom
class LengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 387, 1)
    _Documentation = ''
LengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthUom, enum_prefix=None)
LengthUom.m = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'm', tag=u'm')
LengthUom.angstrom = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'angstrom', tag=u'angstrom')
LengthUom.chBnA = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'chBnA', tag=u'chBnA')
LengthUom.chBnB = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'chBnB', tag=u'chBnB')
LengthUom.chCla = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'chCla', tag=u'chCla')
LengthUom.chSe = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'chSe', tag=u'chSe')
LengthUom.chUS = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'chUS', tag=u'chUS')
LengthUom.cm = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'cm', tag=u'cm')
LengthUom.dm = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'dm', tag=u'dm')
LengthUom.fathom = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'fathom', tag=u'fathom')
LengthUom.fm = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'fm', tag=u'fm')
LengthUom.ft = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft', tag=u'ft')
LengthUom.ftBnA = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftBnA', tag=u'ftBnA')
LengthUom.ftBnB = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftBnB', tag=u'ftBnB')
LengthUom.ftBr65 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftBr(65)', tag=u'ftBr65')
LengthUom.ftCla = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftCla', tag=u'ftCla')
LengthUom.ftGC = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftGC', tag=u'ftGC')
LengthUom.ftInd = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftInd', tag=u'ftInd')
LengthUom.ftInd37 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftInd(37)', tag=u'ftInd37')
LengthUom.ftInd62 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftInd(62)', tag=u'ftInd62')
LengthUom.ftInd75 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftInd(75)', tag=u'ftInd75')
LengthUom.ftMA = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftMA', tag=u'ftMA')
LengthUom.ftSe = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftSe', tag=u'ftSe')
LengthUom.ftUS = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ftUS', tag=u'ftUS')
LengthUom.in_ = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'in', tag=u'in_')
LengthUom.in10 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'in/10', tag=u'in10')
LengthUom.in16 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'in/16', tag=u'in16')
LengthUom.in32 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'in/32', tag=u'in32')
LengthUom.in64 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'in/64', tag=u'in64')
LengthUom.inUS = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'inUS', tag=u'inUS')
LengthUom.km = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'km', tag=u'km')
LengthUom.lkBnA = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'lkBnA', tag=u'lkBnA')
LengthUom.lkBnB = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'lkBnB', tag=u'lkBnB')
LengthUom.lkCla = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'lkCla', tag=u'lkCla')
LengthUom.lkSe = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'lkSe', tag=u'lkSe')
LengthUom.lkUS = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'lkUS', tag=u'lkUS')
LengthUom.mGer = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'mGer', tag=u'mGer')
LengthUom.mi = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'mi', tag=u'mi')
LengthUom.mil = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'mil', tag=u'mil')
LengthUom.miUS = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'miUS', tag=u'miUS')
LengthUom.mm = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'mm', tag=u'mm')
LengthUom.Mm = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'Mm', tag=u'Mm')
LengthUom.nautmi = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'nautmi', tag=u'nautmi')
LengthUom.nm = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'nm', tag=u'nm')
LengthUom.pm = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'pm', tag=u'pm')
LengthUom.um = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'um', tag=u'um')
LengthUom.yd = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'yd', tag=u'yd')
LengthUom.ydBnA = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydBnA', tag=u'ydBnA')
LengthUom.ydBnB = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydBnB', tag=u'ydBnB')
LengthUom.ydCla = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydCla', tag=u'ydCla')
LengthUom.ydIm = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydIm', tag=u'ydIm')
LengthUom.ydInd = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydInd', tag=u'ydInd')
LengthUom.ydInd37 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydInd(37)', tag=u'ydInd37')
LengthUom.ydInd62 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydInd(62)', tag=u'ydInd62')
LengthUom.ydInd75 = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydInd(75)', tag=u'ydInd75')
LengthUom.ydSe = LengthUom._CF_enumeration.addEnumeration(unicode_value=u'ydSe', tag=u'ydSe')
LengthUom._InitializeFacetMap(LengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LengthUom', LengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}LengthPerLengthUom
class LengthPerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LengthPerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 451, 1)
    _Documentation = ''
LengthPerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthPerLengthUom, enum_prefix=None)
LengthPerLengthUom.emptyString = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
LengthPerLengthUom.ft100ft = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft/100ft', tag=u'ft100ft')
LengthPerLengthUom.ftft = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft/ft', tag=u'ftft')
LengthPerLengthUom.ftin = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft/in', tag=u'ftin')
LengthPerLengthUom.ftm = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft/m', tag=u'ftm')
LengthPerLengthUom.ftmi = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft/mi', tag=u'ftmi')
LengthPerLengthUom.kmcm = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'km/cm', tag=u'kmcm')
LengthPerLengthUom.m30m = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'm/30m', tag=u'm30m')
LengthPerLengthUom.mcm = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'm/cm', tag=u'mcm')
LengthPerLengthUom.mkm = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'm/km', tag=u'mkm')
LengthPerLengthUom.mm = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'm/m', tag=u'mm')
LengthPerLengthUom.miin = LengthPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'mi/in', tag=u'miin')
LengthPerLengthUom._InitializeFacetMap(LengthPerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LengthPerLengthUom', LengthPerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MagneticInductionUom
class MagneticInductionUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MagneticInductionUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 475, 1)
    _Documentation = ''
MagneticInductionUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MagneticInductionUom, enum_prefix=None)
MagneticInductionUom.T = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'T', tag=u'T')
MagneticInductionUom.gauss = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'gauss', tag=u'gauss')
MagneticInductionUom.mT = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'mT', tag=u'mT')
MagneticInductionUom.mgauss = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'mgauss', tag=u'mgauss')
MagneticInductionUom.nT = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'nT', tag=u'nT')
MagneticInductionUom.uT = MagneticInductionUom._CF_enumeration.addEnumeration(unicode_value=u'uT', tag=u'uT')
MagneticInductionUom._InitializeFacetMap(MagneticInductionUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MagneticInductionUom', MagneticInductionUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MassConcentrationUom
class MassConcentrationUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MassConcentrationUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 489, 1)
    _Documentation = ''
MassConcentrationUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MassConcentrationUom, enum_prefix=None)
MassConcentrationUom.Euc = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'Euc', tag=u'Euc')
MassConcentrationUom.emptyString = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
MassConcentrationUom.gkg = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'g/kg', tag=u'gkg')
MassConcentrationUom.kgkg = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'kg/kg', tag=u'kgkg')
MassConcentrationUom.kgsack94 = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'kg/sack94', tag=u'kgsack94')
MassConcentrationUom.mgkg = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'mg/kg', tag=u'mgkg')
MassConcentrationUom.permil = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'permil', tag=u'permil')
MassConcentrationUom.ppdk = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'ppdk', tag=u'ppdk')
MassConcentrationUom.ppk = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'ppk', tag=u'ppk')
MassConcentrationUom.ppm = MassConcentrationUom._CF_enumeration.addEnumeration(unicode_value=u'ppm', tag=u'ppm')
MassConcentrationUom._InitializeFacetMap(MassConcentrationUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MassConcentrationUom', MassConcentrationUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MassUom
class MassUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MassUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 507, 1)
    _Documentation = ''
MassUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MassUom, enum_prefix=None)
MassUom.kg = MassUom._CF_enumeration.addEnumeration(unicode_value=u'kg', tag=u'kg')
MassUom.ag = MassUom._CF_enumeration.addEnumeration(unicode_value=u'ag', tag=u'ag')
MassUom.ct = MassUom._CF_enumeration.addEnumeration(unicode_value=u'ct', tag=u'ct')
MassUom.cwtUK = MassUom._CF_enumeration.addEnumeration(unicode_value=u'cwtUK', tag=u'cwtUK')
MassUom.cwtUS = MassUom._CF_enumeration.addEnumeration(unicode_value=u'cwtUS', tag=u'cwtUS')
MassUom.g = MassUom._CF_enumeration.addEnumeration(unicode_value=u'g', tag=u'g')
MassUom.grain = MassUom._CF_enumeration.addEnumeration(unicode_value=u'grain', tag=u'grain')
MassUom.klbm = MassUom._CF_enumeration.addEnumeration(unicode_value=u'klbm', tag=u'klbm')
MassUom.lbm = MassUom._CF_enumeration.addEnumeration(unicode_value=u'lbm', tag=u'lbm')
MassUom.Mg = MassUom._CF_enumeration.addEnumeration(unicode_value=u'Mg', tag=u'Mg')
MassUom.mg = MassUom._CF_enumeration.addEnumeration(unicode_value=u'mg', tag=u'mg')
MassUom.ozav = MassUom._CF_enumeration.addEnumeration(unicode_value=u'oz(av)', tag=u'ozav')
MassUom.oztroy = MassUom._CF_enumeration.addEnumeration(unicode_value=u'oz(troy)', tag=u'oztroy')
MassUom.ozm = MassUom._CF_enumeration.addEnumeration(unicode_value=u'ozm', tag=u'ozm')
MassUom.sack94 = MassUom._CF_enumeration.addEnumeration(unicode_value=u'sack94', tag=u'sack94')
MassUom.t = MassUom._CF_enumeration.addEnumeration(unicode_value=u't', tag=u't')
MassUom.tonUK = MassUom._CF_enumeration.addEnumeration(unicode_value=u'tonUK', tag=u'tonUK')
MassUom.tonUS = MassUom._CF_enumeration.addEnumeration(unicode_value=u'tonUS', tag=u'tonUS')
MassUom.ug = MassUom._CF_enumeration.addEnumeration(unicode_value=u'ug', tag=u'ug')
MassUom._InitializeFacetMap(MassUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MassUom', MassUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MassPerLengthUom
class MassPerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MassPerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 534, 1)
    _Documentation = ''
MassPerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MassPerLengthUom, enum_prefix=None)
MassPerLengthUom.kgm = MassPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'kg/m', tag=u'kgm')
MassPerLengthUom.klbmin = MassPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'klbm/in', tag=u'klbmin')
MassPerLengthUom.lbmft = MassPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'lbm/ft', tag=u'lbmft')
MassPerLengthUom.Mgin = MassPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'Mg/in', tag=u'Mgin')
MassPerLengthUom.kg_mcm2 = MassPerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'kg.m/cm2', tag=u'kg_mcm2')
MassPerLengthUom._InitializeFacetMap(MassPerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MassPerLengthUom', MassPerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}MomentOfForceUom
class MomentOfForceUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MomentOfForceUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 547, 1)
    _Documentation = ''
MomentOfForceUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MomentOfForceUom, enum_prefix=None)
MomentOfForceUom.J = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'J', tag=u'J')
MomentOfForceUom.dN_m = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'dN.m', tag=u'dN_m')
MomentOfForceUom.daN_m = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'daN.m', tag=u'daN_m')
MomentOfForceUom.ft_lbf = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'ft.lbf', tag=u'ft_lbf')
MomentOfForceUom.kft_lbf = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'kft.lbf', tag=u'kft_lbf')
MomentOfForceUom.kgf_m = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'kgf.m', tag=u'kgf_m')
MomentOfForceUom.kN_m = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'kN.m', tag=u'kN_m')
MomentOfForceUom.lbf_ft = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'lbf.ft', tag=u'lbf_ft')
MomentOfForceUom.lbf_in = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'lbf.in', tag=u'lbf_in')
MomentOfForceUom.lbm_ft2s2 = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'lbm.ft2/s2', tag=u'lbm_ft2s2')
MomentOfForceUom.N_m = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'N.m', tag=u'N_m')
MomentOfForceUom.pdl_ft = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'pdl.ft', tag=u'pdl_ft')
MomentOfForceUom.tonfUS_ft = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS.ft', tag=u'tonfUS_ft')
MomentOfForceUom.tonfUS_mi = MomentOfForceUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS.mi', tag=u'tonfUS_mi')
MomentOfForceUom._InitializeFacetMap(MomentOfForceUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MomentOfForceUom', MomentOfForceUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PerLengthUom
class PerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 569, 1)
    _Documentation = ''
PerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PerLengthUom, enum_prefix=None)
PerLengthUom.n1m = PerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/m', tag=u'n1m')
PerLengthUom.n1angstrom = PerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/angstrom', tag=u'n1angstrom')
PerLengthUom.n1cm = PerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/cm', tag=u'n1cm')
PerLengthUom.n1ft = PerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/ft', tag=u'n1ft')
PerLengthUom.n1in = PerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/in', tag=u'n1in')
PerLengthUom.n1mi = PerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/mi', tag=u'n1mi')
PerLengthUom.n1mm = PerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/mm', tag=u'n1mm')
PerLengthUom.n1nm = PerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/nm', tag=u'n1nm')
PerLengthUom.n1yd = PerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'1/yd', tag=u'n1yd')
PerLengthUom._InitializeFacetMap(PerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PerLengthUom', PerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PermeabilityRockUom
class PermeabilityRockUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PermeabilityRockUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 586, 1)
    _Documentation = ''
PermeabilityRockUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PermeabilityRockUom, enum_prefix=None)
PermeabilityRockUom.D = PermeabilityRockUom._CF_enumeration.addEnumeration(unicode_value=u'D', tag=u'D')
PermeabilityRockUom.mD = PermeabilityRockUom._CF_enumeration.addEnumeration(unicode_value=u'mD', tag=u'mD')
PermeabilityRockUom._InitializeFacetMap(PermeabilityRockUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PermeabilityRockUom', PermeabilityRockUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PlaneAngleUom
class PlaneAngleUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PlaneAngleUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 596, 1)
    _Documentation = ''
PlaneAngleUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PlaneAngleUom, enum_prefix=None)
PlaneAngleUom.rad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'rad', tag=u'rad')
PlaneAngleUom.c = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'c', tag=u'c')
PlaneAngleUom.ccgr = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'ccgr', tag=u'ccgr')
PlaneAngleUom.cgr = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'cgr', tag=u'cgr')
PlaneAngleUom.dega = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'dega', tag=u'dega')
PlaneAngleUom.gon = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'gon', tag=u'gon')
PlaneAngleUom.gr = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'gr', tag=u'gr')
PlaneAngleUom.Grad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'Grad', tag=u'Grad')
PlaneAngleUom.krad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'krad', tag=u'krad')
PlaneAngleUom.mila = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'mila', tag=u'mila')
PlaneAngleUom.mina = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'mina', tag=u'mina')
PlaneAngleUom.mrad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'mrad', tag=u'mrad')
PlaneAngleUom.Mrad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'Mrad', tag=u'Mrad')
PlaneAngleUom.mseca = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'mseca', tag=u'mseca')
PlaneAngleUom.seca = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'seca', tag=u'seca')
PlaneAngleUom.urad = PlaneAngleUom._CF_enumeration.addEnumeration(unicode_value=u'urad', tag=u'urad')
PlaneAngleUom._InitializeFacetMap(PlaneAngleUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PlaneAngleUom', PlaneAngleUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PowerUom
class PowerUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PowerUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 620, 1)
    _Documentation = ''
PowerUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PowerUom, enum_prefix=None)
PowerUom.W = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'W', tag=u'W')
PowerUom.ch = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'ch', tag=u'ch')
PowerUom.CV = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'CV', tag=u'CV')
PowerUom.ehp = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'ehp', tag=u'ehp')
PowerUom.GW = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'GW', tag=u'GW')
PowerUom.hhp = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'hhp', tag=u'hhp')
PowerUom.hp = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'hp', tag=u'hp')
PowerUom.kcalh = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'kcal/h', tag=u'kcalh')
PowerUom.kW = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'kW', tag=u'kW')
PowerUom.MJa = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'MJ/a', tag=u'MJa')
PowerUom.MW = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'MW', tag=u'MW')
PowerUom.mW = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'mW', tag=u'mW')
PowerUom.nW = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'nW', tag=u'nW')
PowerUom.ton_of_refrig = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'ton of refrig', tag=u'ton_of_refrig')
PowerUom.TW = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'TW', tag=u'TW')
PowerUom.uW = PowerUom._CF_enumeration.addEnumeration(unicode_value=u'uW', tag=u'uW')
PowerUom._InitializeFacetMap(PowerUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PowerUom', PowerUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}PressureUom
class PressureUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PressureUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 644, 1)
    _Documentation = ''
PressureUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PressureUom, enum_prefix=None)
PressureUom.Pa = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'Pa', tag=u'Pa')
PressureUom.at = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'at', tag=u'at')
PressureUom.atm = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'atm', tag=u'atm')
PressureUom.bar = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'bar', tag=u'bar')
PressureUom.cmH2O4degC = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'cmH2O(4degC)', tag=u'cmH2O4degC')
PressureUom.dynecm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'dyne/cm2', tag=u'dynecm2')
PressureUom.GPa = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'GPa', tag=u'GPa')
PressureUom.hbar = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'hbar', tag=u'hbar')
PressureUom.inH2O39_2F = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'inH2O(39.2F)', tag=u'inH2O39_2F')
PressureUom.inH2O60F = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'inH2O(60F)', tag=u'inH2O60F')
PressureUom.inHg32F = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'inHg(32F)', tag=u'inHg32F')
PressureUom.inHg60F = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'inHg(60F)', tag=u'inHg60F')
PressureUom.kgfcm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'kgf/cm2', tag=u'kgfcm2')
PressureUom.kgfmm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'kgf/mm2', tag=u'kgfmm2')
PressureUom.kNm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'kN/m2', tag=u'kNm2')
PressureUom.kPa = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'kPa', tag=u'kPa')
PressureUom.kpsi = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'kpsi', tag=u'kpsi')
PressureUom.lbfft2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/ft2', tag=u'lbfft2')
PressureUom.lbf100ft2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/100ft2', tag=u'lbf100ft2')
PressureUom.lbfin2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'lbf/in2', tag=u'lbfin2')
PressureUom.mbar = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'mbar', tag=u'mbar')
PressureUom.mmHg0C = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'mmHg(0C)', tag=u'mmHg0C')
PressureUom.mPa = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'mPa', tag=u'mPa')
PressureUom.MPa = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'MPa', tag=u'MPa')
PressureUom.Mpsi = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'Mpsi', tag=u'Mpsi')
PressureUom.Nm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'N/m2', tag=u'Nm2')
PressureUom.Nmm2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'N/mm2', tag=u'Nmm2')
PressureUom.Pag = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'Pa(g)', tag=u'Pag')
PressureUom.pPa = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'pPa', tag=u'pPa')
PressureUom.psi = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'psi', tag=u'psi')
PressureUom.psia = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'psia', tag=u'psia')
PressureUom.psig = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'psig', tag=u'psig')
PressureUom.tonfUSft2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS/ft2', tag=u'tonfUSft2')
PressureUom.tonfUSin2 = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'tonfUS/in2', tag=u'tonfUSin2')
PressureUom.torr = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'torr', tag=u'torr')
PressureUom.ubar = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'ubar', tag=u'ubar')
PressureUom.umHg0C = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'umHg(0C)', tag=u'umHg0C')
PressureUom.uPa = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'uPa', tag=u'uPa')
PressureUom.upsi = PressureUom._CF_enumeration.addEnumeration(unicode_value=u'upsi', tag=u'upsi')
PressureUom._InitializeFacetMap(PressureUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PressureUom', PressureUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}RelativePowerUom
class RelativePowerUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RelativePowerUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 691, 1)
    _Documentation = ''
RelativePowerUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RelativePowerUom, enum_prefix=None)
RelativePowerUom.emptyString = RelativePowerUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
RelativePowerUom.Btubhp_hr = RelativePowerUom._CF_enumeration.addEnumeration(unicode_value=u'Btu/bhp.hr', tag=u'Btubhp_hr')
RelativePowerUom.WkW = RelativePowerUom._CF_enumeration.addEnumeration(unicode_value=u'W/kW', tag=u'WkW')
RelativePowerUom.WW = RelativePowerUom._CF_enumeration.addEnumeration(unicode_value=u'W/W', tag=u'WW')
RelativePowerUom._InitializeFacetMap(RelativePowerUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RelativePowerUom', RelativePowerUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}SpecificHeatCapacityUom
class SpecificHeatCapacityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpecificHeatCapacityUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 703, 1)
    _Documentation = ''
SpecificHeatCapacityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpecificHeatCapacityUom, enum_prefix=None)
SpecificHeatCapacityUom.Jkg_K = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value=u'J/kg.K', tag=u'Jkg_K')
SpecificHeatCapacityUom.Btulbm_degF = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value=u'Btu/lbm.degF', tag=u'Btulbm_degF')
SpecificHeatCapacityUom.Btulbm_degR = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value=u'Btu/lbm.degR', tag=u'Btulbm_degR')
SpecificHeatCapacityUom.calg_K = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value=u'cal/g.K', tag=u'calg_K')
SpecificHeatCapacityUom.Jg_K = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value=u'J/g.K', tag=u'Jg_K')
SpecificHeatCapacityUom.kcalkg_degC = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value=u'kcal/kg.degC', tag=u'kcalkg_degC')
SpecificHeatCapacityUom.kJkg_K = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value=u'kJ/kg.K', tag=u'kJkg_K')
SpecificHeatCapacityUom.kW_hkg_degC = SpecificHeatCapacityUom._CF_enumeration.addEnumeration(unicode_value=u'kW.h/kg.degC', tag=u'kW_hkg_degC')
SpecificHeatCapacityUom._InitializeFacetMap(SpecificHeatCapacityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SpecificHeatCapacityUom', SpecificHeatCapacityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}SpecificVolumeUom
class SpecificVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpecificVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 719, 1)
    _Documentation = ''
SpecificVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpecificVolumeUom, enum_prefix=None)
SpecificVolumeUom.m3kg = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/kg', tag=u'm3kg')
SpecificVolumeUom.bbltonUK = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/tonUK', tag=u'bbltonUK')
SpecificVolumeUom.bbltonUS = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/tonUS', tag=u'bbltonUS')
SpecificVolumeUom.cm3g = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/g', tag=u'cm3g')
SpecificVolumeUom.dm3kg = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'dm3/kg', tag=u'dm3kg')
SpecificVolumeUom.dm3t = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'dm3/t', tag=u'dm3t')
SpecificVolumeUom.ft3kg = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/kg', tag=u'ft3kg')
SpecificVolumeUom.ft3lbm = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/lbm', tag=u'ft3lbm')
SpecificVolumeUom.ft3sack94 = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/sack94', tag=u'ft3sack94')
SpecificVolumeUom.galUSsack94 = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/sack94', tag=u'galUSsack94')
SpecificVolumeUom.galUKlbm = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/lbm', tag=u'galUKlbm')
SpecificVolumeUom.galUSlbm = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/lbm', tag=u'galUSlbm')
SpecificVolumeUom.galUStonUK = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/tonUK', tag=u'galUStonUK')
SpecificVolumeUom.galUStonUS = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/tonUS', tag=u'galUStonUS')
SpecificVolumeUom.L100kg = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/100kg', tag=u'L100kg')
SpecificVolumeUom.Lkg = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/kg', tag=u'Lkg')
SpecificVolumeUom.Lt = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/t', tag=u'Lt')
SpecificVolumeUom.LtonUK = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/tonUK', tag=u'LtonUK')
SpecificVolumeUom.m3g = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/g', tag=u'm3g')
SpecificVolumeUom.m3t = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/t', tag=u'm3t')
SpecificVolumeUom.m3tonUK = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/tonUK', tag=u'm3tonUK')
SpecificVolumeUom.m3tonUS = SpecificVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/tonUS', tag=u'm3tonUS')
SpecificVolumeUom._InitializeFacetMap(SpecificVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SpecificVolumeUom', SpecificVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StandardVolumeUom
class StandardVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StandardVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 749, 1)
    _Documentation = ''
StandardVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StandardVolumeUom, enum_prefix=None)
StandardVolumeUom.scm15C = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'scm(15C)', tag=u'scm15C')
StandardVolumeUom.scm0C = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'scm(0C)', tag=u'scm0C')
StandardVolumeUom.Gsm3 = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Gsm3', tag=u'Gsm3')
StandardVolumeUom.ksm3 = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ksm3', tag=u'ksm3')
StandardVolumeUom.MMscf60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'MMscf(60F)', tag=u'MMscf60F')
StandardVolumeUom.MMscm15C = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'MMscm(15C)', tag=u'MMscm15C')
StandardVolumeUom.MMstb60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'MMstb(60F)', tag=u'MMstb60F')
StandardVolumeUom.Mscf60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Mscf(60F)', tag=u'Mscf60F')
StandardVolumeUom.Mstb60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Mstb(60F)', tag=u'Mstb60F')
StandardVolumeUom.scf60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'scf(60F)', tag=u'scf60F')
StandardVolumeUom.stb60F = StandardVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb(60F)', tag=u'stb60F')
StandardVolumeUom._InitializeFacetMap(StandardVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StandardVolumeUom', StandardVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}StandardVolumePerTimeUom
class StandardVolumePerTimeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StandardVolumePerTimeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 768, 1)
    _Documentation = ''
StandardVolumePerTimeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StandardVolumePerTimeUom, enum_prefix=None)
StandardVolumePerTimeUom.scf60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'scf(60F)/d', tag=u'scf60Fd')
StandardVolumePerTimeUom.scm15Cs = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'scm(15C)/s', tag=u'scm15Cs')
StandardVolumePerTimeUom.scm15Cd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'scm(15C)/d', tag=u'scm15Cd')
StandardVolumePerTimeUom.stb60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'stb(60F)/d', tag=u'stb60Fd')
StandardVolumePerTimeUom.ksm3d = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'ksm3/d', tag=u'ksm3d')
StandardVolumePerTimeUom.Mscm15Cd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'Mscm(15C)/d', tag=u'Mscm15Cd')
StandardVolumePerTimeUom.MMscm15Cd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'MMscm(15C)/d', tag=u'MMscm15Cd')
StandardVolumePerTimeUom.Mstb60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'Mstb(60F)/d', tag=u'Mstb60Fd')
StandardVolumePerTimeUom.MMstb60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'MMstb(60F)/d', tag=u'MMstb60Fd')
StandardVolumePerTimeUom.Mscf60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'Mscf(60F)/d', tag=u'Mscf60Fd')
StandardVolumePerTimeUom.MMscf60Fd = StandardVolumePerTimeUom._CF_enumeration.addEnumeration(unicode_value=u'MMscf(60F)/d', tag=u'MMscf60Fd')
StandardVolumePerTimeUom._InitializeFacetMap(StandardVolumePerTimeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StandardVolumePerTimeUom', StandardVolumePerTimeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ThermalConductivityUom
class ThermalConductivityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ThermalConductivityUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 787, 1)
    _Documentation = ''
ThermalConductivityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ThermalConductivityUom, enum_prefix=None)
ThermalConductivityUom.Wm_K = ThermalConductivityUom._CF_enumeration.addEnumeration(unicode_value=u'W/m.K', tag=u'Wm_K')
ThermalConductivityUom.Btuhr_ft_degF = ThermalConductivityUom._CF_enumeration.addEnumeration(unicode_value=u'Btu/hr.ft.degF', tag=u'Btuhr_ft_degF')
ThermalConductivityUom.calh_cm_degC = ThermalConductivityUom._CF_enumeration.addEnumeration(unicode_value=u'cal/h.cm.degC', tag=u'calh_cm_degC')
ThermalConductivityUom.kcalh_m_degC = ThermalConductivityUom._CF_enumeration.addEnumeration(unicode_value=u'kcal/h.m.degC', tag=u'kcalh_m_degC')
ThermalConductivityUom.cals_cm_degC = ThermalConductivityUom._CF_enumeration.addEnumeration(unicode_value=u'cal/s.cm.degC', tag=u'cals_cm_degC')
ThermalConductivityUom._InitializeFacetMap(ThermalConductivityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ThermalConductivityUom', ThermalConductivityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ThermalVolumetricExpansionUom
class ThermalVolumetricExpansionUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ThermalVolumetricExpansionUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 800, 1)
    _Documentation = ''
ThermalVolumetricExpansionUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ThermalVolumetricExpansionUom, enum_prefix=None)
ThermalVolumetricExpansionUom.n1K = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value=u'1/K', tag=u'n1K')
ThermalVolumetricExpansionUom.ppmdegC = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value=u'ppm/degC', tag=u'ppmdegC')
ThermalVolumetricExpansionUom.ppmdegF = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value=u'ppm/degF', tag=u'ppmdegF')
ThermalVolumetricExpansionUom.n1degC = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value=u'1/degC', tag=u'n1degC')
ThermalVolumetricExpansionUom.n1degF = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value=u'1/degF', tag=u'n1degF')
ThermalVolumetricExpansionUom.n1degR = ThermalVolumetricExpansionUom._CF_enumeration.addEnumeration(unicode_value=u'1/degR', tag=u'n1degR')
ThermalVolumetricExpansionUom._InitializeFacetMap(ThermalVolumetricExpansionUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ThermalVolumetricExpansionUom', ThermalVolumetricExpansionUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}ThermodynamicTemperatureUom
class ThermodynamicTemperatureUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ThermodynamicTemperatureUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 814, 1)
    _Documentation = ''
ThermodynamicTemperatureUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ThermodynamicTemperatureUom, enum_prefix=None)
ThermodynamicTemperatureUom.K = ThermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value=u'K', tag=u'K')
ThermodynamicTemperatureUom.degC = ThermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value=u'degC', tag=u'degC')
ThermodynamicTemperatureUom.degF = ThermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value=u'degF', tag=u'degF')
ThermodynamicTemperatureUom.degR = ThermodynamicTemperatureUom._CF_enumeration.addEnumeration(unicode_value=u'degR', tag=u'degR')
ThermodynamicTemperatureUom._InitializeFacetMap(ThermodynamicTemperatureUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ThermodynamicTemperatureUom', ThermodynamicTemperatureUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}TimeUom
class TimeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TimeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 826, 1)
    _Documentation = ''
TimeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TimeUom, enum_prefix=None)
TimeUom.s = TimeUom._CF_enumeration.addEnumeration(unicode_value=u's', tag=u's')
TimeUom.a = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'a', tag=u'a')
TimeUom.cs = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'cs', tag=u'cs')
TimeUom.d = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'd', tag=u'd')
TimeUom.Ga = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'Ga', tag=u'Ga')
TimeUom.h = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'h', tag=u'h')
TimeUom.n100s = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'100s', tag=u'n100s')
TimeUom.Ma = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'Ma', tag=u'Ma')
TimeUom.min = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'min', tag=u'min')
TimeUom.ms = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'ms', tag=u'ms')
TimeUom.ms2 = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'ms/2', tag=u'ms2')
TimeUom.ns = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'ns', tag=u'ns')
TimeUom.ps = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'ps', tag=u'ps')
TimeUom.us = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'us', tag=u'us')
TimeUom.wk = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'wk', tag=u'wk')
TimeUom.n100ka = TimeUom._CF_enumeration.addEnumeration(unicode_value=u'100ka', tag=u'n100ka')
TimeUom._InitializeFacetMap(TimeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TimeUom', TimeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}VelocityUom
class VelocityUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VelocityUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 850, 1)
    _Documentation = ''
VelocityUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VelocityUom, enum_prefix=None)
VelocityUom.ms = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'm/s', tag=u'ms')
VelocityUom.cma = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'cm/a', tag=u'cma')
VelocityUom.cms = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'cm/s', tag=u'cms')
VelocityUom.dms = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'dm/s', tag=u'dms')
VelocityUom.ftd = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/d', tag=u'ftd')
VelocityUom.fth = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/h', tag=u'fth')
VelocityUom.ftmin = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/min', tag=u'ftmin')
VelocityUom.ftms = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/ms', tag=u'ftms')
VelocityUom.fts = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/s', tag=u'fts')
VelocityUom.ftus = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'ft/us', tag=u'ftus')
VelocityUom.ina = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'in/a', tag=u'ina')
VelocityUom.inmin = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'in/min', tag=u'inmin')
VelocityUom.ins = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'in/s', tag=u'ins')
VelocityUom.kfth = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'kft/h', tag=u'kfth')
VelocityUom.kfts = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'kft/s', tag=u'kfts')
VelocityUom.kmh = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'km/h', tag=u'kmh')
VelocityUom.kms = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'km/s', tag=u'kms')
VelocityUom.knot = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'knot', tag=u'knot')
VelocityUom.md = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'm/d', tag=u'md')
VelocityUom.mh = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'm/h', tag=u'mh')
VelocityUom.mmin = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'm/min', tag=u'mmin')
VelocityUom.mms = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'm/ms', tag=u'mms')
VelocityUom.mih = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'mi/h', tag=u'mih')
VelocityUom.milyr = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'mil/yr', tag=u'milyr')
VelocityUom.mma = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'mm/a', tag=u'mma')
VelocityUom.mms_ = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'mm/s', tag=u'mms_')
VelocityUom.nms = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'nm/s', tag=u'nms')
VelocityUom.ums = VelocityUom._CF_enumeration.addEnumeration(unicode_value=u'um/s', tag=u'ums')
VelocityUom._InitializeFacetMap(VelocityUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VelocityUom', VelocityUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}VolumeUom
class VolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VolumeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 886, 1)
    _Documentation = ''
VolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumeUom, enum_prefix=None)
VolumeUom.m3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3', tag=u'm3')
VolumeUom.acre_ft = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'acre.ft', tag=u'acre_ft')
VolumeUom.bbl = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl', tag=u'bbl')
VolumeUom.bcf = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bcf', tag=u'bcf')
VolumeUom.cm3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'cm3', tag=u'cm3')
VolumeUom.dm3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'dm3', tag=u'dm3')
VolumeUom.flozUK = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'flozUK', tag=u'flozUK')
VolumeUom.flozUS = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'flozUS', tag=u'flozUS')
VolumeUom.ft3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3', tag=u'ft3')
VolumeUom.galUK = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUK', tag=u'galUK')
VolumeUom.galUS = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS', tag=u'galUS')
VolumeUom.ha_m = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ha.m', tag=u'ha_m')
VolumeUom.hL = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'hL', tag=u'hL')
VolumeUom.in3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'in3', tag=u'in3')
VolumeUom.n1000ft3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'1000ft3', tag=u'n1000ft3')
VolumeUom.km3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'km3', tag=u'km3')
VolumeUom.L = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L', tag=u'L')
VolumeUom.Mbbl = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Mbbl', tag=u'Mbbl')
VolumeUom.Mcf = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Mcf', tag=u'Mcf')
VolumeUom.Mft3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'M(ft3)', tag=u'Mft3')
VolumeUom.mi3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'mi3', tag=u'mi3')
VolumeUom.mL = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'mL', tag=u'mL')
VolumeUom.Mm3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'M(m3)', tag=u'Mm3')
VolumeUom.mm3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'mm3', tag=u'mm3')
VolumeUom.MMbbl = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'MMbbl', tag=u'MMbbl')
VolumeUom.ptUK = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ptUK', tag=u'ptUK')
VolumeUom.ptUS = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ptUS', tag=u'ptUS')
VolumeUom.qtUK = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'qtUK', tag=u'qtUK')
VolumeUom.qtUS = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'qtUS', tag=u'qtUS')
VolumeUom.tcf = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'tcf', tag=u'tcf')
VolumeUom.um2_m = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'um2.m', tag=u'um2_m')
VolumeUom.yd3 = VolumeUom._CF_enumeration.addEnumeration(unicode_value=u'yd3', tag=u'yd3')
VolumeUom._InitializeFacetMap(VolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VolumeUom', VolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}VolumeFlowRateUom
class VolumeFlowRateUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VolumeFlowRateUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 926, 1)
    _Documentation = ''
VolumeFlowRateUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumeFlowRateUom, enum_prefix=None)
VolumeFlowRateUom.m3s = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'm3/s', tag=u'm3s')
VolumeFlowRateUom.bbld = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/d', tag=u'bbld')
VolumeFlowRateUom.bblhr = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/hr', tag=u'bblhr')
VolumeFlowRateUom.bblmin = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/min', tag=u'bblmin')
VolumeFlowRateUom.cm330min = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/30min', tag=u'cm330min')
VolumeFlowRateUom.cm3h = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/h', tag=u'cm3h')
VolumeFlowRateUom.cm3min = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/min', tag=u'cm3min')
VolumeFlowRateUom.cm3s = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/s', tag=u'cm3s')
VolumeFlowRateUom.dm3s = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'dm3/s', tag=u'dm3s')
VolumeFlowRateUom.ft3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/d', tag=u'ft3d')
VolumeFlowRateUom.ft3h = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/h', tag=u'ft3h')
VolumeFlowRateUom.ft3min = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/min', tag=u'ft3min')
VolumeFlowRateUom.ft3s = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/s', tag=u'ft3s')
VolumeFlowRateUom.galUKd = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/d', tag=u'galUKd')
VolumeFlowRateUom.galUKhr = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/hr', tag=u'galUKhr')
VolumeFlowRateUom.galUKmin = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/min', tag=u'galUKmin')
VolumeFlowRateUom.galUSd = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/d', tag=u'galUSd')
VolumeFlowRateUom.galUShr = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/hr', tag=u'galUShr')
VolumeFlowRateUom.galUSmin = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/min', tag=u'galUSmin')
VolumeFlowRateUom.kbbld = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'kbbl/d', tag=u'kbbld')
VolumeFlowRateUom.n1000ft3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'1000ft3/d', tag=u'n1000ft3d')
VolumeFlowRateUom.n1000m3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'1000m3/d', tag=u'n1000m3d')
VolumeFlowRateUom.n1000m3h = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'1000m3/h', tag=u'n1000m3h')
VolumeFlowRateUom.Lh = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'L/h', tag=u'Lh')
VolumeFlowRateUom.Lmin = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'L/min', tag=u'Lmin')
VolumeFlowRateUom.Ls = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'L/s', tag=u'Ls')
VolumeFlowRateUom.m3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'm3/d', tag=u'm3d')
VolumeFlowRateUom.m3h = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'm3/h', tag=u'm3h')
VolumeFlowRateUom.m3min = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'm3/min', tag=u'm3min')
VolumeFlowRateUom.Mbbld = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'Mbbl/d', tag=u'Mbbld')
VolumeFlowRateUom.Mft3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'M(ft3)/d', tag=u'Mft3d')
VolumeFlowRateUom.Mm3d = VolumeFlowRateUom._CF_enumeration.addEnumeration(unicode_value=u'M(m3)/d', tag=u'Mm3d')
VolumeFlowRateUom._InitializeFacetMap(VolumeFlowRateUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VolumeFlowRateUom', VolumeFlowRateUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}VolumePerLengthUom
class VolumePerLengthUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VolumePerLengthUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 966, 1)
    _Documentation = ''
VolumePerLengthUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumePerLengthUom, enum_prefix=None)
VolumePerLengthUom.bblPft = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'bblPft', tag=u'bblPft')
VolumePerLengthUom.bblPin = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'bblPin', tag=u'bblPin')
VolumePerLengthUom.bblPmi = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'bblPmi', tag=u'bblPmi')
VolumePerLengthUom.dm3P100km = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dm3P100km', tag=u'dm3P100km')
VolumePerLengthUom.dm3Pkm100 = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dm3Pkm(100)', tag=u'dm3Pkm100')
VolumePerLengthUom.dm3Pm = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'dm3Pm', tag=u'dm3Pm')
VolumePerLengthUom.ft3Pft = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'ft3Pft', tag=u'ft3Pft')
VolumePerLengthUom.galUKPmi = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'galUKPmi', tag=u'galUKPmi')
VolumePerLengthUom.galUSPft = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'galUSPft', tag=u'galUSPft')
VolumePerLengthUom.galUSPmi = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'galUSPmi', tag=u'galUSPmi')
VolumePerLengthUom.in3Pft = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'in3Pft', tag=u'in3Pft')
VolumePerLengthUom.LP100km = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'LP100km', tag=u'LP100km')
VolumePerLengthUom.LPkm100 = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'LPkm(100)', tag=u'LPkm100')
VolumePerLengthUom.LPm = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'LPm', tag=u'LPm')
VolumePerLengthUom.m3Pkm = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'm3Pkm', tag=u'm3Pkm')
VolumePerLengthUom.m3Pm = VolumePerLengthUom._CF_enumeration.addEnumeration(unicode_value=u'm3Pm', tag=u'm3Pm')
VolumePerLengthUom._InitializeFacetMap(VolumePerLengthUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VolumePerLengthUom', VolumePerLengthUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}VolumePerVolumeUom
class VolumePerVolumeUom (abstractUomEnum, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VolumePerVolumeUom')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_quantityClass.xsd', 990, 1)
    _Documentation = ''
VolumePerVolumeUom._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumePerVolumeUom, enum_prefix=None)
VolumePerVolumeUom.Euc = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Euc', tag=u'Euc')
VolumePerVolumeUom.emptyString = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'%', tag='emptyString')
VolumePerVolumeUom.permil = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'permil', tag=u'permil')
VolumePerVolumeUom.ppdk = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ppdk', tag=u'ppdk')
VolumePerVolumeUom.ppk = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ppk', tag=u'ppk')
VolumePerVolumeUom.ppm = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ppm', tag=u'ppm')
VolumePerVolumeUom.bblacre_ft = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/acre.ft', tag=u'bblacre_ft')
VolumePerVolumeUom.bblbbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/bbl', tag=u'bblbbl')
VolumePerVolumeUom.bblft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/ft3', tag=u'bblft3')
VolumePerVolumeUom.bbl100bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/100bbl', tag=u'bbl100bbl')
VolumePerVolumeUom.bblkft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/k(ft3)', tag=u'bblkft3')
VolumePerVolumeUom.bblMft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'bbl/M(ft3)', tag=u'bblMft3')
VolumePerVolumeUom.cm3cm3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/cm3', tag=u'cm3cm3')
VolumePerVolumeUom.cm3m3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'cm3/m3', tag=u'cm3m3')
VolumePerVolumeUom.dm3m3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'dm3/m3', tag=u'dm3m3')
VolumePerVolumeUom.ft3bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/bbl', tag=u'ft3bbl')
VolumePerVolumeUom.ft3ft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ft3/ft3', tag=u'ft3ft3')
VolumePerVolumeUom.galUSkgalUS = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/kgalUS', tag=u'galUSkgalUS')
VolumePerVolumeUom.galUKkgalUK = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/kgalUK', tag=u'galUKkgalUK')
VolumePerVolumeUom.galUKft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/ft3', tag=u'galUKft3')
VolumePerVolumeUom.galUKMbbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUK/Mbbl', tag=u'galUKMbbl')
VolumePerVolumeUom.galUSbbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/bbl', tag=u'galUSbbl')
VolumePerVolumeUom.galUS10bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/10bbl', tag=u'galUS10bbl')
VolumePerVolumeUom.galUSft3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/ft3', tag=u'galUSft3')
VolumePerVolumeUom.galUSMbbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'galUS/Mbbl', tag=u'galUSMbbl')
VolumePerVolumeUom.n1000ft3bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'1000ft3/bbl', tag=u'n1000ft3bbl')
VolumePerVolumeUom.ksm3sm3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ksm3/sm3', tag=u'ksm3sm3')
VolumePerVolumeUom.L10bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/10bbl', tag=u'L10bbl')
VolumePerVolumeUom.Lm3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'L/m3', tag=u'Lm3')
VolumePerVolumeUom.m3ha_m = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/ha.m', tag=u'm3ha_m')
VolumePerVolumeUom.m3m3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'm3/m3', tag=u'm3m3')
VolumePerVolumeUom.Mft3acre_ft = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'M(ft3)/acre.ft', tag=u'Mft3acre_ft')
VolumePerVolumeUom.mLgalUK = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'mL/galUK', tag=u'mLgalUK')
VolumePerVolumeUom.mLgalUS = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'mL/galUS', tag=u'mLgalUS')
VolumePerVolumeUom.mLmL = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'mL/mL', tag=u'mLmL')
VolumePerVolumeUom.MMbblacre_ft = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'MMbbl/acre.ft', tag=u'MMbblacre_ft')
VolumePerVolumeUom.MMscf60stb60 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'MMscf60/stb60', tag=u'MMscf60stb60')
VolumePerVolumeUom.Mscf60stb60 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'Mscf60/stb60', tag=u'Mscf60stb60')
VolumePerVolumeUom.ptUKMbbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ptUK/Mbbl', tag=u'ptUKMbbl')
VolumePerVolumeUom.ptUS10bbl = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'ptUS/10bbl', tag=u'ptUS10bbl')
VolumePerVolumeUom.pu = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'pu', tag=u'pu')
VolumePerVolumeUom.scm15stb60 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'scm15/stb60', tag=u'scm15stb60')
VolumePerVolumeUom.sm3ksm3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'sm3/ksm3', tag=u'sm3ksm3')
VolumePerVolumeUom.sm3sm3 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'sm3/sm3', tag=u'sm3sm3')
VolumePerVolumeUom.stb60MMscf60 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb60/MMscf60', tag=u'stb60MMscf60')
VolumePerVolumeUom.stb60MMscm15 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb60/MMscm15', tag=u'stb60MMscm15')
VolumePerVolumeUom.stb60Mscf60 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb60/Mscf60', tag=u'stb60Mscf60')
VolumePerVolumeUom.stb60Mscm15 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb60/Mscm15', tag=u'stb60Mscm15')
VolumePerVolumeUom.stb60scm15 = VolumePerVolumeUom._CF_enumeration.addEnumeration(unicode_value=u'stb60/scm15', tag=u'stb60scm15')
VolumePerVolumeUom._InitializeFacetMap(VolumePerVolumeUom._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VolumePerVolumeUom', VolumePerVolumeUom)

# Atomic simple type: {http://www.witsml.org/schemas/1series}commentString
class commentString (abstractCommentString):

    """A comment or remark intended for human consumption. 
			There should be no assumption that semantics can be extracted from this field by a computer. 
			Neither should there be an assumption that any two humans will interpret the information 
			in the same way (i.e., it may not be interoperable)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'commentString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 342, 1)
    _Documentation = u'A comment or remark intended for human consumption. \n\t\t\tThere should be no assumption that semantics can be extracted from this field by a computer. \n\t\t\tNeither should there be an assumption that any two humans will interpret the information \n\t\t\tin the same way (i.e., it may not be interoperable).'
commentString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'commentString', commentString)

# Complex type {http://www.witsml.org/schemas/1series}cs_commonData with content type ELEMENT_ONLY
class cs_commonData (pyxb.binding.basis.complexTypeDefinition):
    """ WITSML - Common Data Component Schema """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_commonData')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}sourceName uses Python identifier sourceName
    __sourceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sourceName'), 'sourceName', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriessourceName', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 26, 3), )

    
    sourceName = property(__sourceName.value, __sourceName.set, None, u'An identifier to indicate the data originator.\n\t\t\t\t\tThis identifies the server that originally created \n\t\t\t\t\tthe object and thus most of the uids in the object (but not \n\t\t\t\t\tnecessarily the uids of the parents). This is typically a url. ')

    
    # Element {http://www.witsml.org/schemas/1series}dTimCreation uses Python identifier dTimCreation
    __dTimCreation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dTimCreation'), 'dTimCreation', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesdTimCreation', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 34, 3), )

    
    dTimCreation = property(__dTimCreation.value, __dTimCreation.set, None, u'When the data was created at the persistent data store. \n\t\t\t\t\tThis is an API server parameter releted to the "Special Handling of Change Information" within a server. \n\t\t\t\t\tSee the relevant API specification for the  behavior related to this element.')

    
    # Element {http://www.witsml.org/schemas/1series}dTimLastChange uses Python identifier dTimLastChange
    __dTimLastChange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dTimLastChange'), 'dTimLastChange', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesdTimLastChange', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 43, 3), )

    
    dTimLastChange = property(__dTimLastChange.value, __dTimLastChange.set, None, u'Last change of any element of the data at the persistent data store.\n\t\t\t\t\tThis is an API server parameter releted to the "Special Handling of Change Information" within a server. \n\t\t\t\t\tSee the relevant API specification for the  behavior related to this element.')

    
    # Element {http://www.witsml.org/schemas/1series}itemState uses Python identifier itemState
    __itemState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'itemState'), 'itemState', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesitemState', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 53, 3), )

    
    itemState = property(__itemState.value, __itemState.set, None, u'The item state for the data object.  ')

    
    # Element {http://www.witsml.org/schemas/1series}serviceCategory uses Python identifier serviceCategory
    __serviceCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'serviceCategory'), 'serviceCategory', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesserviceCategory', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 58, 3), )

    
    serviceCategory = property(__serviceCategory.value, __serviceCategory.set, None, u'The category of the service related to the creation of the object. \n\t\t\t\t\tFor example, "mud log service", "cement service", "LWD service", "rig service", "drilling service".\n\t\t\t\t\t')

    
    # Element {http://www.witsml.org/schemas/1series}comments uses Python identifier comments
    __comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comments'), 'comments', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriescomments', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 67, 3), )

    
    comments = property(__comments.value, __comments.set, None, u'Comments and remarks.  ')

    
    # Element {http://www.witsml.org/schemas/1series}acquisitionTimeZone uses Python identifier acquisitionTimeZone
    __acquisitionTimeZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'acquisitionTimeZone'), 'acquisitionTimeZone', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesacquisitionTimeZone', True, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 72, 3), )

    
    acquisitionTimeZone = property(__acquisitionTimeZone.value, __acquisitionTimeZone.set, None, u'The local time zone of the original acquisition date-time values. \n\t\t\t\t\tIt is the deviation in hours and minutes from UTC.\n\t\t\t\t\tThe first occurrence should be the actual local time zone at the start of acquisition\n\t\t\t\t\tand may represent a seasonally adjusted value such as daylight savings.\n\t\t\t\t\tThe dTim attribute must be populated in the second and subsequent occurrences \n\t\t\t\t\tif the local time zone changes during acquisition.\n\t\t\t\t\tThis knowledge is required because the original time zone in a dateTime\n\t\t\t\t\tvalue may be lost when software converts to a different time zone.')

    
    # Element {http://www.witsml.org/schemas/1series}defaultDatum uses Python identifier defaultDatum
    __defaultDatum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'defaultDatum'), 'defaultDatum', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesdefaultDatum', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 85, 3), )

    
    defaultDatum = property(__defaultDatum.value, __defaultDatum.set, None, u'A pointer to the default wellDatum for measured depth coordinates,\n\t\t\t\t\tvertical depth coordinates and elevation coordinates in this object. \n\t\t\t\t\tDepth coordinates that do not specify a datum attribute shall be \n\t\t\t\t\tassumed to be measured relative to this default vertical datum.\n\t\t\t\t\tThe referenced wellDatum must be defined within the well object associated with this object.')

    
    # Element {http://www.witsml.org/schemas/1series}privateGroupOnly uses Python identifier privateGroupOnly
    __privateGroupOnly = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'privateGroupOnly'), 'privateGroupOnly', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesprivateGroupOnly', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 95, 3), )

    
    privateGroupOnly = property(__privateGroupOnly.value, __privateGroupOnly.set, None, u'This is an API query parameter.\n\t\t\t\t\tSee the API specification for the behavior related to this element.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionAny uses Python identifier extensionAny
    __extensionAny = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'extensionAny'), 'extensionAny', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesextensionAny', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 102, 3), )

    
    extensionAny = property(__extensionAny.value, __extensionAny.set, None, u'Extensions to the schema using an xsd:any construct.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionNameValue uses Python identifier extensionNameValue
    __extensionNameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'extensionNameValue'), 'extensionNameValue', '__httpwww_witsml_orgschemas1series_cs_commonData_httpwww_witsml_orgschemas1seriesextensionNameValue', True, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 108, 3), )

    
    extensionNameValue = property(__extensionNameValue.value, __extensionNameValue.set, None, u'Extensions to the schema based on a name-value construct.')


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
Namespace.addCategoryObject('typeBinding', u'cs_commonData', cs_commonData)


# Complex type {http://www.witsml.org/schemas/1series}cs_customData with content type ELEMENT_ONLY
class cs_customData (pyxb.binding.basis.complexTypeDefinition):
    """ WITSML - Custom or User Defined Element and Attributes Component Schema.
			Specify custom element, attributes, and types in the custom data area."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_customData')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_customData.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_customData', cs_customData)


# Complex type {http://www.witsml.org/schemas/1series}cs_documentAudit with content type ELEMENT_ONLY
class cs_documentAudit (pyxb.binding.basis.complexTypeDefinition):
    """The audit records what happened to the data, to produce 
			the data that is in this file. It consists of one or more events."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_documentAudit')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentAudit.xsd', 20, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}event uses Python identifier event
    __event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'event'), 'event', '__httpwww_witsml_orgschemas1series_cs_documentAudit_httpwww_witsml_orgschemas1seriesevent', True, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentAudit.xsd', 27, 3), )

    
    event = property(__event.value, __event.set, None, u'One event related to the data.')


    _ElementMap = {
        __event.name() : __event
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_documentAudit', cs_documentAudit)


# Complex type {http://www.witsml.org/schemas/1series}cs_documentFileCreation with content type ELEMENT_ONLY
class cs_documentFileCreation (pyxb.binding.basis.complexTypeDefinition):
    """A block of information about the creation of the XML file. 
			This is different than the creation of the data that is included within the file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_documentFileCreation')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 20, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}fileCreationDate uses Python identifier fileCreationDate
    __fileCreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fileCreationDate'), 'fileCreationDate', '__httpwww_witsml_orgschemas1series_cs_documentFileCreation_httpwww_witsml_orgschemas1seriesfileCreationDate', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 27, 3), )

    
    fileCreationDate = property(__fileCreationDate.value, __fileCreationDate.set, None, u'The date and time that the file was created.')

    
    # Element {http://www.witsml.org/schemas/1series}softwareName uses Python identifier softwareName
    __softwareName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'softwareName'), 'softwareName', '__httpwww_witsml_orgschemas1series_cs_documentFileCreation_httpwww_witsml_orgschemas1seriessoftwareName', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 33, 3), )

    
    softwareName = property(__softwareName.value, __softwareName.set, None, u'If appropriate, the software that created the file. \n\t\t\t\t\tThis is a free form string, and may include whatever information \n\t\t\t\t\tis deemed relevant.')

    
    # Element {http://www.witsml.org/schemas/1series}fileCreator uses Python identifier fileCreator
    __fileCreator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fileCreator'), 'fileCreator', '__httpwww_witsml_orgschemas1series_cs_documentFileCreation_httpwww_witsml_orgschemas1seriesfileCreator', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 41, 3), )

    
    fileCreator = property(__fileCreator.value, __fileCreator.set, None, u'The person or business associate that created \n\t\t\t\t\tthe file.')

    
    # Element {http://www.witsml.org/schemas/1series}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comment'), 'comment', '__httpwww_witsml_orgschemas1series_cs_documentFileCreation_httpwww_witsml_orgschemas1seriescomment', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 48, 3), )

    
    comment = property(__comment.value, __comment.set, None, u'Any comment that would be useful to further \n\t\t\t\t\texplain the creation of this instance document.')


    _ElementMap = {
        __fileCreationDate.name() : __fileCreationDate,
        __softwareName.name() : __softwareName,
        __fileCreator.name() : __fileCreator,
        __comment.name() : __comment
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_documentFileCreation', cs_documentFileCreation)


# Complex type {http://www.witsml.org/schemas/1series}cs_documentInfo with content type ELEMENT_ONLY
class cs_documentInfo (pyxb.binding.basis.complexTypeDefinition):
    """A  schema to capture a set of data that is 
			relevant for many exchange documents. It includes information about the 
			file that was created, and high-level information about the data that is 
			being exchanged within the file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_documentInfo')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 23, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}documentName uses Python identifier documentName
    __documentName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'documentName'), 'documentName', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesdocumentName', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 31, 3), )

    
    documentName = property(__documentName.value, __documentName.set, None, u'An identifier for the document. This is \n\t\t\t\t\tintended to be unique within the context of the NamingSystem.')

    
    # Element {http://www.witsml.org/schemas/1series}documentAlias uses Python identifier documentAlias
    __documentAlias = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'documentAlias'), 'documentAlias', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesdocumentAlias', True, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 38, 3), )

    
    documentAlias = property(__documentAlias.value, __documentAlias.set, None, u'Zero or more alternate names for the document. \n\t\t\t\t\tThese names do not need to be unique within the naming system.')

    
    # Element {http://www.witsml.org/schemas/1series}documentDate uses Python identifier documentDate
    __documentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'documentDate'), 'documentDate', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesdocumentDate', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 45, 3), )

    
    documentDate = property(__documentDate.value, __documentDate.set, None, u'The date of the creation of the document. \n\t\t\t\t\tThis is not the same as the date that the file was created. \n\t\t\t\t\tFor this date, the document is considered to be the set of \n\t\t\t\t\tinformation associated with this document information. \n\t\t\t\t\tFor example, the document may be a seismic binset. \n\t\t\t\t\tThis represents the date that the binset was created. \n\t\t\t\t\tThe FileCreation information would capture the date that \n\t\t\t\t\tthe XML file was created to send or exchange the binset.')

    
    # Element {http://www.witsml.org/schemas/1series}documentClass uses Python identifier documentClass
    __documentClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'documentClass'), 'documentClass', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesdocumentClass', True, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 58, 3), )

    
    documentClass = property(__documentClass.value, __documentClass.set, None, u'A document class. Examples of classes would be a \n\t\t\t\t\tmetadata classification or a set of keywords. ')

    
    # Element {http://www.witsml.org/schemas/1series}fileCreationInformation uses Python identifier fileCreationInformation
    __fileCreationInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fileCreationInformation'), 'fileCreationInformation', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesfileCreationInformation', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 64, 3), )

    
    fileCreationInformation = property(__fileCreationInformation.value, __fileCreationInformation.set, None, u'The information about the creation of the \n\t\t\t\t\texchange file. This is not about the creation of the data within \n\t\t\t\t\tthe file, but the creation of the file itself.')

    
    # Element {http://www.witsml.org/schemas/1series}securityInformation uses Python identifier securityInformation
    __securityInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'securityInformation'), 'securityInformation', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriessecurityInformation', True, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 72, 3), )

    
    securityInformation = property(__securityInformation.value, __securityInformation.set, None, u'Information about the security to be applied to \n\t\t\t\t\tthis file. More than one classification can be given.')

    
    # Element {http://www.witsml.org/schemas/1series}disclaimer uses Python identifier disclaimer
    __disclaimer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'disclaimer'), 'disclaimer', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesdisclaimer', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 79, 3), )

    
    disclaimer = property(__disclaimer.value, __disclaimer.set, None, u'A free-form string that allows a disclaimer to \n\t\t\t\t\taccompany the information.')

    
    # Element {http://www.witsml.org/schemas/1series}auditTrail uses Python identifier auditTrail
    __auditTrail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'auditTrail'), 'auditTrail', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesauditTrail', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 86, 3), )

    
    auditTrail = property(__auditTrail.value, __auditTrail.set, None, u'A collection of events that can document the \n\t\t\t\t\thistory of the data.')

    
    # Element {http://www.witsml.org/schemas/1series}owner uses Python identifier owner
    __owner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'owner'), 'owner', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriesowner', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 93, 3), )

    
    owner = property(__owner.value, __owner.set, None, u'The owner of the data.')

    
    # Element {http://www.witsml.org/schemas/1series}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comment'), 'comment', '__httpwww_witsml_orgschemas1series_cs_documentInfo_httpwww_witsml_orgschemas1seriescomment', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 99, 3), )

    
    comment = property(__comment.value, __comment.set, None, u'An optional comment about the document.')


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
Namespace.addCategoryObject('typeBinding', u'cs_documentInfo', cs_documentInfo)


# Complex type {http://www.witsml.org/schemas/1series}cs_extensionAny with content type ELEMENT_ONLY
class cs_extensionAny (pyxb.binding.basis.complexTypeDefinition):
    """WITSML - Extension Schema. The intent is to allow standard WITSML schema 
			extensions which will validate in older clients or servers. A client or server can ignore any schema that it 
			does not recognize. New versions will modify specific elements to replace this type with a type that
			adds new elements, including another element with this type."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_extensionAny')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionAny.xsd', 18, 1)
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cs_extensionAny', cs_extensionAny)


# Complex type {http://www.witsml.org/schemas/1series}abstractMeasure with content type SIMPLE
class abstractMeasure (pyxb.binding.basis.complexTypeDefinition):
    """The intended abstract supertype of all quantities that have a value 
			with a unit of measure. The unit of measure is in the uom attribute of the subtypes. 
			This type allows all quantities to be profiled to be a 'float' instead of a 'double'."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_baseType.xsd', 111, 1)
    # Base type is abstractDouble

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'abstractMeasure', abstractMeasure)


# Complex type {http://www.witsml.org/schemas/1series}obj_messages with content type ELEMENT_ONLY
class obj_messages (_abs.abstractObject):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'obj_messages')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 41, 1)
    # Base type is _abs.abstractObject
    
    # Element {http://www.witsml.org/schemas/1series}documentInfo uses Python identifier documentInfo
    __documentInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'documentInfo'), 'documentInfo', '__httpwww_witsml_orgschemas1series_obj_messages_httpwww_witsml_orgschemas1seriesdocumentInfo', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 48, 5), )

    
    documentInfo = property(__documentInfo.value, __documentInfo.set, None, u'Information about the XML message instance.  ')

    
    # Element {http://www.witsml.org/schemas/1series}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_witsml_orgschemas1series_obj_messages_httpwww_witsml_orgschemas1seriesmessage', True, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 53, 5), )

    
    message = property(__message.value, __message.set, None, u'A single message.  ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_witsml_orgschemas1series_obj_messages_version', schemaVersionString, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 59, 4)
    __version._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 59, 4)
    
    version = property(__version.value, __version.set, None, u'Data object schema version.  The fourth level must match the \n\t\t\t\t\t\tversion of the schema constraints (enumerations and XML loader files) that are assumed\n\t\t\t\t\t\tby the document instance.')


    _ElementMap = _abs.abstractObject._ElementMap.copy()
    _ElementMap.update({
        __documentInfo.name() : __documentInfo,
        __message.name() : __message
    })
    _AttributeMap = _abs.abstractObject._AttributeMap.copy()
    _AttributeMap.update({
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', u'obj_messages', obj_messages)


# Complex type {http://www.witsml.org/schemas/1series}timestampedTimeZone with content type SIMPLE
class timestampedTimeZone (pyxb.binding.basis.complexTypeDefinition):
    """A local time zone conforming to the XSD:dateTime specification.
			The dTim attribute can capture when the local time zone changed.
			The use of this type is generally related to a specific (set of) date and time
			for which the original time zone needs to be captured."""
    _TypeDefinition = abstractTimeZone
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timestampedTimeZone')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 59, 1)
    # Base type is abstractTimeZone
    
    # Attribute dTim uses Python identifier dTim
    __dTim = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dTim'), 'dTim', '__httpwww_witsml_orgschemas1series_timestampedTimeZone_dTim', timestamp)
    __dTim._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 69, 4)
    __dTim._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 69, 4)
    
    dTim = property(__dTim.value, __dTim.set, None, u'The date and time when this local time zone became active.\n\t\t\t\t\t\tThis value must be defined on the second and subsequent occurrences.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __dTim.name() : __dTim
    }
Namespace.addCategoryObject('typeBinding', u'timestampedTimeZone', timestampedTimeZone)


# Complex type {http://www.witsml.org/schemas/1series}cs_documentEvent with content type ELEMENT_ONLY
class cs_documentEvent (pyxb.binding.basis.complexTypeDefinition):
    """An event type captures the basic information about an 
			event that has affected the data."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_documentEvent')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}eventDate uses Python identifier eventDate
    __eventDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'eventDate'), 'eventDate', '__httpwww_witsml_orgschemas1series_cs_documentEvent_httpwww_witsml_orgschemas1serieseventDate', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 28, 3), )

    
    eventDate = property(__eventDate.value, __eventDate.set, None, u'The date on which the event took place.')

    
    # Element {http://www.witsml.org/schemas/1series}eventType uses Python identifier eventType
    __eventType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'eventType'), 'eventType', '__httpwww_witsml_orgschemas1series_cs_documentEvent_httpwww_witsml_orgschemas1serieseventType', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 34, 3), )

    
    eventType = property(__eventType.value, __eventType.set, None, u'The kind of event event.')

    
    # Element {http://www.witsml.org/schemas/1series}responsibleParty uses Python identifier responsibleParty
    __responsibleParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'responsibleParty'), 'responsibleParty', '__httpwww_witsml_orgschemas1series_cs_documentEvent_httpwww_witsml_orgschemas1seriesresponsibleParty', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 40, 3), )

    
    responsibleParty = property(__responsibleParty.value, __responsibleParty.set, None, u'The party responsible for the event.')

    
    # Element {http://www.witsml.org/schemas/1series}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comment'), 'comment', '__httpwww_witsml_orgschemas1series_cs_documentEvent_httpwww_witsml_orgschemas1seriescomment', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 46, 3), )

    
    comment = property(__comment.value, __comment.set, None, u'A free form comment that can further \n\t\t\t\t\tdefine the event that occurred.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionNameValue uses Python identifier extensionNameValue
    __extensionNameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'extensionNameValue'), 'extensionNameValue', '__httpwww_witsml_orgschemas1series_cs_documentEvent_httpwww_witsml_orgschemas1seriesextensionNameValue', True, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 53, 3), )

    
    extensionNameValue = property(__extensionNameValue.value, __extensionNameValue.set, None, u'Extensions to the schema based on a name-value construct.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uid'), 'uid', '__httpwww_witsml_orgschemas1series_cs_documentEvent_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, u'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


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
Namespace.addCategoryObject('typeBinding', u'cs_documentEvent', cs_documentEvent)


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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_documentSecurityInfo')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}class uses Python identifier class_
    __class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'class'), 'class_', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_httpwww_witsml_orgschemas1seriesclass', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 33, 3), )

    
    class_ = property(__class.value, __class.set, None, u'The security class in which this document is \n\t\t\t\t\tclassified. Examples would be confidential, partner confidential, \n\t\t\t\t\ttight. The meaning of the class is determined by the System in which \n\t\t\t\t\tit is defined.')

    
    # Element {http://www.witsml.org/schemas/1series}securitySystem uses Python identifier securitySystem
    __securitySystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'securitySystem'), 'securitySystem', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_httpwww_witsml_orgschemas1seriessecuritySystem', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 42, 3), )

    
    securitySystem = property(__securitySystem.value, __securitySystem.set, None, u'The security classification system. \n\t\t\t\t\tThis gives context to the meaning of the Class value.')

    
    # Element {http://www.witsml.org/schemas/1series}endDate uses Python identifier endDate
    __endDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'endDate'), 'endDate', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_httpwww_witsml_orgschemas1seriesendDate', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 49, 3), )

    
    endDate = property(__endDate.value, __endDate.set, None, u'The date on which this security class is no \n\t\t\t\t\tlonger applicable.')

    
    # Element {http://www.witsml.org/schemas/1series}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comment'), 'comment', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_httpwww_witsml_orgschemas1seriescomment', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 56, 3), )

    
    comment = property(__comment.value, __comment.set, None, u'A general comment to further define the security \n\t\t\t\t\tclass.')

    
    # Element {http://www.witsml.org/schemas/1series}extensionNameValue uses Python identifier extensionNameValue
    __extensionNameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'extensionNameValue'), 'extensionNameValue', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_httpwww_witsml_orgschemas1seriesextensionNameValue', True, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 63, 3), )

    
    extensionNameValue = property(__extensionNameValue.value, __extensionNameValue.set, None, u'Extensions to the schema based on a name-value construct.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uid'), 'uid', '__httpwww_witsml_orgschemas1series_cs_documentSecurityInfo_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, u'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


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
Namespace.addCategoryObject('typeBinding', u'cs_documentSecurityInfo', cs_documentSecurityInfo)


# Complex type {http://www.witsml.org/schemas/1series}cs_extensionNameValue with content type ELEMENT_ONLY
class cs_extensionNameValue (pyxb.binding.basis.complexTypeDefinition):
    """WITSML - Extension values Schema. The intent is to allow standard WITSML "named" 
			extensions without having to modify the schema. A client or server can ignore any name that it 
			does not recognize but certain meta data is required in order to allow 
			generic clients or servers to process the value."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cs_extensionNameValue')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesname', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 29, 3), )

    
    name = property(__name.value, __name.set, None, u'The name of the extension.\n\t\t\t\t\tEach standard name should document the expected measure class.\n\t\t\t\t\tEach standard name should document the expected maximum size. \n\t\t\t\t\tFor numeric values the size should be in terms of xsd types\n\t\t\t\t\tsuch as int, long, short, byte, float or double.\n\t\t\t\t\tFor strings, the maximum length should be defined in number of characters.\n\t\t\t\t\tLocal extensions to the list of standard names are allowed but it is strongly\n\t\t\t\t\trecommended that the names and definitions be approved by the \n\t\t\t\t\tWITSML SIG Technical Team before use.')

    
    # Element {http://www.witsml.org/schemas/1series}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'value'), 'value_', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesvalue', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 42, 3), )

    
    value_ = property(__value.value, __value.set, None, u'The value of the extension. \n\t\t\t\t\tThis may also include a uom attribute. \n\t\t\t\t\tThe content should conform to constraints defined by the data type.')

    
    # Element {http://www.witsml.org/schemas/1series}dataType uses Python identifier dataType
    __dataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dataType'), 'dataType', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesdataType', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 49, 3), )

    
    dataType = property(__dataType.value, __dataType.set, None, u'The underlying XML type of the value.')

    
    # Element {http://www.witsml.org/schemas/1series}dTim uses Python identifier dTim
    __dTim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dTim'), 'dTim', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesdTim', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 54, 3), )

    
    dTim = property(__dTim.value, __dTim.set, None, u'The date-time associated with the value.')

    
    # Element {http://www.witsml.org/schemas/1series}md uses Python identifier md
    __md = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'md'), 'md', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesmd', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 59, 3), )

    
    md = property(__md.value, __md.set, None, u'The measured depth associated with the value.')

    
    # Element {http://www.witsml.org/schemas/1series}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'index'), 'index', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesindex', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 64, 3), )

    
    index = property(__index.value, __index.set, None, u'Indexes things with the same name. \n\t\t\t\t\tThat is, 1 indicates the first one, 2 incidates the second one, etc.')

    
    # Element {http://www.witsml.org/schemas/1series}measureClass uses Python identifier measureClass
    __measureClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'measureClass'), 'measureClass', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesmeasureClass', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 70, 3), )

    
    measureClass = property(__measureClass.value, __measureClass.set, None, u'The kind of the measure. For example, "length".\n\t\t\t\t\tThis should be specified if the value requires a unit of measure.')

    
    # Element {http://www.witsml.org/schemas/1series}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_httpwww_witsml_orgschemas1seriesdescription', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 76, 3), )

    
    description = property(__description.value, __description.set, None, u'A textual description of the extension.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uid'), 'uid', '__httpwww_witsml_orgschemas1series_cs_extensionNameValue_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, u'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')


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
Namespace.addCategoryObject('typeBinding', u'cs_extensionNameValue', cs_extensionNameValue)


# Complex type {http://www.witsml.org/schemas/1series}obj_message with content type ELEMENT_ONLY
class obj_message (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.witsml.org/schemas/1series}obj_message with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'obj_message')
    _XSDLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 70, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.witsml.org/schemas/1series}objectReference uses Python identifier objectReference
    __objectReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'objectReference'), 'objectReference', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesobjectReference', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 25, 3), )

    
    objectReference = property(__objectReference.value, __objectReference.set, None, u'A reference to an object that is defined within the \n\t\t\t\t\tcontext of a wellbore.')

    
    # Element {http://www.witsml.org/schemas/1series}subObjectReference uses Python identifier subObjectReference
    __subObjectReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'subObjectReference'), 'subObjectReference', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriessubObjectReference', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 31, 3), )

    
    subObjectReference = property(__subObjectReference.value, __subObjectReference.set, None, u'A reference to an sub-object that is defined within the \n\t\t\t\t\tcontext of the object referenced by objectReference.\n\t\t\t\t\tThis should only refer to recurring components of a growing object.')

    
    # Element {http://www.witsml.org/schemas/1series}dTim uses Python identifier dTim
    __dTim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dTim'), 'dTim', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesdTim', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 38, 3), )

    
    dTim = property(__dTim.value, __dTim.set, None, u'Date and time the information is related to.  ')

    
    # Element {http://www.witsml.org/schemas/1series}activityCode uses Python identifier activityCode
    __activityCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'activityCode'), 'activityCode', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesactivityCode', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 43, 3), )

    
    activityCode = property(__activityCode.value, __activityCode.set, None, u'A code used to define rig activity.')

    
    # Element {http://www.witsml.org/schemas/1series}detailActivity uses Python identifier detailActivity
    __detailActivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'detailActivity'), 'detailActivity', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesdetailActivity', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 48, 3), )

    
    detailActivity = property(__detailActivity.value, __detailActivity.set, None, u'Custom string to further define an activity.  ')

    
    # Element {http://www.witsml.org/schemas/1series}md uses Python identifier md
    __md = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'md'), 'md', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesmd', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 53, 3), )

    
    md = property(__md.value, __md.set, None, u'Along hole measured depth of measurement from the drill datum.  ')

    
    # Element {http://www.witsml.org/schemas/1series}mdBit uses Python identifier mdBit
    __mdBit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mdBit'), 'mdBit', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesmdBit', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 58, 3), )

    
    mdBit = property(__mdBit.value, __mdBit.set, None, u'Along hole measured depth of measurement from the drill datum.  ')

    
    # Element {http://www.witsml.org/schemas/1series}typeMessage uses Python identifier typeMessage
    __typeMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'typeMessage'), 'typeMessage', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriestypeMessage', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 63, 3), )

    
    typeMessage = property(__typeMessage.value, __typeMessage.set, None, u'Message type.  ')

    
    # Element {http://www.witsml.org/schemas/1series}messageText uses Python identifier messageText
    __messageText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'messageText'), 'messageText', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesmessageText', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 68, 3), )

    
    messageText = property(__messageText.value, __messageText.set, None, u'Message text. ')

    
    # Element {http://www.witsml.org/schemas/1series}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'param'), 'param', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesparam', True, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 73, 3), )

    
    param = property(__param.value, __param.set, None, u'Any extra numeric data.\n\t\t\t\t\tFor this usage the name attribute MUST be specified because it represents the meaning of the data.\n\t\t\t\t\tWhile the index attribute is mandatory, it is only significant if the same name repeats.')

    
    # Element {http://www.witsml.org/schemas/1series}severity uses Python identifier severity
    __severity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'severity'), 'severity', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesseverity', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 81, 3), )

    
    severity = property(__severity.value, __severity.set, None, u'Severity of incident.  ')

    
    # Element {http://www.witsml.org/schemas/1series}warnProbability uses Python identifier warnProbability
    __warnProbability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'warnProbability'), 'warnProbability', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1serieswarnProbability', False, pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 86, 3), )

    
    warnProbability = property(__warnProbability.value, __warnProbability.set, None, u'A warning probability (applies to warning).')

    
    # Element {http://www.witsml.org/schemas/1series}nameWell uses Python identifier nameWell
    __nameWell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'nameWell'), 'nameWell', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesnameWell', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 72, 3), )

    
    nameWell = property(__nameWell.value, __nameWell.set, None, u'Human recognizable context for the well that contains the wellbore.  ')

    
    # Element {http://www.witsml.org/schemas/1series}nameWellbore uses Python identifier nameWellbore
    __nameWellbore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'nameWellbore'), 'nameWellbore', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesnameWellbore', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 77, 3), )

    
    nameWellbore = property(__nameWellbore.value, __nameWellbore.set, None, u'Human recognizable context for the wellbore that contains the message.  ')

    
    # Element {http://www.witsml.org/schemas/1series}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriesname', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 82, 3), )

    
    name = property(__name.value, __name.set, None, u'Human recognizable context for the risk.  ')

    
    # Element {http://www.witsml.org/schemas/1series}commonData uses Python identifier commonData
    __commonData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'commonData'), 'commonData', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriescommonData', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 92, 3), )

    
    commonData = property(__commonData.value, __commonData.set, None, u'A container element that contains elements that are common to all data \n\t\t\t\t\tobjects.  ')

    
    # Element {http://www.witsml.org/schemas/1series}customData uses Python identifier customData
    __customData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'customData'), 'customData', '__httpwww_witsml_orgschemas1series_obj_message_httpwww_witsml_orgschemas1seriescustomData', False, pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 98, 3), )

    
    customData = property(__customData.value, __customData.set, None, u'A container element that can contain custom or user defined \n\t\t\t\t\tdata elements.')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uid'), 'uid', '__httpwww_witsml_orgschemas1series_obj_message_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_objectUid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_objectUid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, u'The unique identifier of an object.\n\t\t\t\tThis should not be used for child nodes within an object.\n\t\t\t\tFor an independent object, the value may be globally unique.\n\t\t\t\tFor a dependent object, the value must be unique (for the same object type) within the context of the parent object.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThe purpose of this type is to facilitate modifying the optionality in derived schemas.')

    
    # Attribute uidWell uses Python identifier uidWell
    __uidWell = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uidWell'), 'uidWell', '__httpwww_witsml_orgschemas1series_obj_message_uidWell', uidParentString)
    __uidWell._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 105, 2)
    __uidWell._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 105, 2)
    
    uidWell = property(__uidWell.value, __uidWell.set, None, u'Unique identifier for the well. This uniquely represents \n\t\t\t\tthe well referenced by the (possibly non-unique) nameWell. ')

    
    # Attribute uidWellbore uses Python identifier uidWellbore
    __uidWellbore = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uidWellbore'), 'uidWellbore', '__httpwww_witsml_orgschemas1series_obj_message_uidWellbore', uidParentString)
    __uidWellbore._DeclarationLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 112, 2)
    __uidWellbore._UseLocation = pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 112, 2)
    
    uidWellbore = property(__uidWellbore.value, __uidWellbore.set, None, u'Unique identifier for the wellbore. This uniquely represents \n\t\t\t\tthe wellbore referenced by the (possibly non-unique) nameWellbore. ')


    _ElementMap = {
        __objectReference.name() : __objectReference,
        __subObjectReference.name() : __subObjectReference,
        __dTim.name() : __dTim,
        __activityCode.name() : __activityCode,
        __detailActivity.name() : __detailActivity,
        __md.name() : __md,
        __mdBit.name() : __mdBit,
        __typeMessage.name() : __typeMessage,
        __messageText.name() : __messageText,
        __param.name() : __param,
        __severity.name() : __severity,
        __warnProbability.name() : __warnProbability,
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
Namespace.addCategoryObject('typeBinding', u'obj_message', obj_message)


# Complex type {http://www.witsml.org/schemas/1series}yAxisAzimuth with content type SIMPLE
class yAxisAzimuth (abstractMeasure):
    """The angle of a Y axis from North.
			This is a variation of planeAngleMeasure with an 
			attribute defining the direction of north."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'yAxisAzimuth')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 102, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_yAxisAzimuth_uom', PlaneAngleUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 111, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 111, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure of the azimuth value.')

    
    # Attribute northDirection uses Python identifier northDirection
    __northDirection = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'northDirection'), 'northDirection', '__httpwww_witsml_orgschemas1series_yAxisAzimuth_northDirection', AziRef)
    __northDirection._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 117, 4)
    __northDirection._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 117, 4)
    
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


# Complex type {http://www.witsml.org/schemas/1series}volumePerVolumeMeasurePercent with content type SIMPLE
class volumePerVolumeMeasurePercent (abstractMeasure):
    """A volume per volume measure that is constrained to a unit of percent."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumePerVolumeMeasurePercent')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 126, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_volumePerVolumeMeasurePercent_uom', PercentUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 133, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 133, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'volumePerVolumeMeasurePercent', volumePerVolumeMeasurePercent)


# Complex type {http://www.witsml.org/schemas/1series}measureOrQuantity with content type SIMPLE
class measureOrQuantity (abstractMeasure):
    """A measure with a uom or a quantity (without a uom).
			This should not be used except in situations where the underlying class of data is 
			captured elsewhere. For example, via a measure class."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'measureOrQuantity')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 146, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_measureOrQuantity_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 154, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 154, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure for the quantity.\n\t\t\t\t\t\tThis value must conform to the values allowed by a measure class. \n\t\t\t\t\t\tIf the value is a measure then the uom must be specified.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'measureOrQuantity', measureOrQuantity)


# Complex type {http://www.witsml.org/schemas/1series}genericMeasure with content type SIMPLE
class genericMeasure (abstractMeasure):
    """A generic measure type.
			This should not be used except in situations where the underlying class of data is 
			captured elsewhere. For example, for a log curve."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'genericMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 165, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_genericMeasure_uom', uomString, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 174, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 174, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure for the quantity.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'genericMeasure', genericMeasure)


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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ratioGenericMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 184, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_ratioGenericMeasure_uom', uomString, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 199, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 199, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure for the quantity.\n\t\t\t\t\t\tIf for some reason a uom is not appropriate for the quantity,\n\t\t\t\t\t\ta unit of "Euc" should be used.')

    
    # Attribute numerator uses Python identifier numerator
    __numerator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numerator'), 'numerator', '__httpwww_witsml_orgschemas1series_ratioGenericMeasure_numerator', unitlessQuantity)
    __numerator._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 206, 4)
    __numerator._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 206, 4)
    
    numerator = property(__numerator.value, __numerator.set, None, None)

    
    # Attribute denominator uses Python identifier denominator
    __denominator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'denominator'), 'denominator', '__httpwww_witsml_orgschemas1series_ratioGenericMeasure_denominator', unitlessQuantity)
    __denominator._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 207, 4)
    __denominator._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 207, 4)
    
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


# Complex type {http://www.witsml.org/schemas/1series}refNameString with content type SIMPLE
class refNameString (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a name in another node of the xml hierachy.
			This value represents a foreign key from one element to another."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'refNameString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 256, 1)
    # Base type is abstractNameString
    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas1series_refNameString_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 263, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 263, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, u'A reference to the unique identifier (uid attribute) in the node\n\t\t\t\t\t\treferenced by the name value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', u'refNameString', refNameString)


# Complex type {http://www.witsml.org/schemas/1series}refObjectString with content type SIMPLE
class refObjectString (pyxb.binding.basis.complexTypeDefinition):
    """The value of a name element in another data-object.
			The information in this type represents a foreign key to a data-object instance.
			Knowledge of the type of object being referenced is defined by an attribute."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'refObjectString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 274, 1)
    # Base type is abstractNameString
    
    # Attribute object uses Python identifier object
    __object = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'object'), 'object', '__httpwww_witsml_orgschemas1series_refObjectString_object', nameString, required=True)
    __object._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 282, 4)
    __object._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 282, 4)
    
    object = property(__object.value, __object.set, None, u'The type of data-object being referenced (e.g., "well", "wellbore").')

    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas1series_refObjectString_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 287, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 287, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, u'A reference to the unique identifier (uid attribute) in the object\n\t\t\t\t\t\treferenced by the name value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __object.name() : __object,
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', u'refObjectString', refObjectString)


# Complex type {http://www.witsml.org/schemas/1series}refPositiveCount with content type SIMPLE
class refPositiveCount (pyxb.binding.basis.complexTypeDefinition):
    """A reference to a index value in another node of the xml hierachy.
			This value represents a foreign key from one element to another."""
    _TypeDefinition = abstractPositiveCount
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'refPositiveCount')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 298, 1)
    # Base type is abstractPositiveCount
    
    # Attribute uidRef uses Python identifier uidRef
    __uidRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uidRef'), 'uidRef', '__httpwww_witsml_orgschemas1series_refPositiveCount_uidRef', refString)
    __uidRef._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 305, 4)
    __uidRef._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 305, 4)
    
    uidRef = property(__uidRef.value, __uidRef.set, None, u'A reference to the unique identifier (uid attribute) in the node\n\t\t\t\t\t\treferenced by the index value. \n\t\t\t\t\t\tThis attribute is required within the context of a WITSML server.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uidRef.name() : __uidRef
    }
Namespace.addCategoryObject('typeBinding', u'refPositiveCount', refPositiveCount)


# Complex type {http://www.witsml.org/schemas/1series}timestampedCommentString with content type SIMPLE
class timestampedCommentString (pyxb.binding.basis.complexTypeDefinition):
    """A timestamped textual description."""
    _TypeDefinition = abstractCommentString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timestampedCommentString')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 369, 1)
    # Base type is abstractCommentString
    
    # Attribute dTim uses Python identifier dTim
    __dTim = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dTim'), 'dTim', '__httpwww_witsml_orgschemas1series_timestampedCommentString_dTim', timestamp, required=True)
    __dTim._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 376, 4)
    __dTim._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 376, 4)
    
    dTim = property(__dTim.value, __dTim.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __dTim.name() : __dTim
    }
Namespace.addCategoryObject('typeBinding', u'timestampedCommentString', timestampedCommentString)


# Complex type {http://www.witsml.org/schemas/1series}extensionvalue with content type SIMPLE
class extensionvalue (pyxb.binding.basis.complexTypeDefinition):
    """A extension value.
			Each standard name should document the expected maximum size. 
			Knowledge of the semantics must be provided with the context of the usage of this type."""
    _TypeDefinition = abstractMaximumLengthString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'extensionvalue')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 391, 1)
    # Base type is abstractMaximumLengthString
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_extensionvalue_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 400, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 400, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure for the value.\n\t\t\t\t\t\tThis value must conform to the values allowed by a measure class.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uom.name() : __uom
    }
Namespace.addCategoryObject('typeBinding', u'extensionvalue', extensionvalue)


# Complex type {http://www.witsml.org/schemas/1series}nameStruct with content type SIMPLE
class nameStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of something within a naming system."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameStruct')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 441, 1)
    # Base type is abstractNameString
    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'namingSystem'), 'namingSystem', '__httpwww_witsml_orgschemas1series_nameStruct_namingSystem', nameString)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 447, 4)
    __namingSystem._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 447, 4)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, u'The naming system within the name is (hopefully) unique.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __namingSystem.name() : __namingSystem
    }
Namespace.addCategoryObject('typeBinding', u'nameStruct', nameStruct)


# Complex type {http://www.witsml.org/schemas/1series}shortNameStruct with content type SIMPLE
class shortNameStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of something within a naming system."""
    _TypeDefinition = abstractString32
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'shortNameStruct')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 456, 1)
    # Base type is abstractString32
    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'namingSystem'), 'namingSystem', '__httpwww_witsml_orgschemas1series_shortNameStruct_namingSystem', nameString)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 462, 4)
    __namingSystem._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 462, 4)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, u'The naming system within the name is (hopefully) unique.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __namingSystem.name() : __namingSystem
    }
Namespace.addCategoryObject('typeBinding', u'shortNameStruct', shortNameStruct)


# Complex type {http://www.witsml.org/schemas/1series}wellKnownNameStruct with content type SIMPLE
class wellKnownNameStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of something within a mandatory naming system 
			with an optional code."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wellKnownNameStruct')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 471, 1)
    # Base type is abstractNameString
    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'namingSystem'), 'namingSystem', '__httpwww_witsml_orgschemas1series_wellKnownNameStruct_namingSystem', nameString, required=True)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 478, 4)
    __namingSystem._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 478, 4)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, u'The naming system within the name is unique.')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'code'), 'code', '__httpwww_witsml_orgschemas1series_wellKnownNameStruct_code', kindString)
    __code._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 483, 4)
    __code._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 483, 4)
    
    code = property(__code.value, __code.set, None, u'A unique (short) code associated with the name.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __namingSystem.name() : __namingSystem,
        __code.name() : __code
    }
Namespace.addCategoryObject('typeBinding', u'wellKnownNameStruct', wellKnownNameStruct)


# Complex type {http://www.witsml.org/schemas/1series}objectSequence with content type SIMPLE
class objectSequence (pyxb.binding.basis.complexTypeDefinition):
    """Defines a sequence number and with an optional description attribute."""
    _TypeDefinition = abstractPositiveCount
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'objectSequence')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 522, 1)
    # Base type is abstractPositiveCount
    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpwww_witsml_orgschemas1series_objectSequence_description', descriptionString)
    __description._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 529, 4)
    __description._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 529, 4)
    
    description = property(__description.value, __description.set, None, u'A description related to the sequence number.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __description.name() : __description
    }
Namespace.addCategoryObject('typeBinding', u'objectSequence', objectSequence)


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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lithostratigraphyStruct')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 538, 1)
    # Base type is abstractNameString
    
    # Attribute kind uses Python identifier kind
    __kind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'kind'), 'kind', '__httpwww_witsml_orgschemas1series_lithostratigraphyStruct_kind', LithostratigraphyUnit)
    __kind._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 549, 4)
    __kind._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 549, 4)
    
    kind = property(__kind.value, __kind.set, None, u'The unit of lithostratigraphy.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __kind.name() : __kind
    }
Namespace.addCategoryObject('typeBinding', u'lithostratigraphyStruct', lithostratigraphyStruct)


# Complex type {http://www.witsml.org/schemas/1series}chronostratigraphyStruct with content type SIMPLE
class chronostratigraphyStruct (pyxb.binding.basis.complexTypeDefinition):
    """The name of a chronostratigraphy, with the "kind" attribute specifying
			the chronostratigraphic unit-hierarchy (Era, Period, Epoch, Stage)."""
    _TypeDefinition = abstractNameString
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'chronostratigraphyStruct')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 558, 1)
    # Base type is abstractNameString
    
    # Attribute kind uses Python identifier kind
    __kind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'kind'), 'kind', '__httpwww_witsml_orgschemas1series_chronostratigraphyStruct_kind', ChronostratigraphyUnit)
    __kind._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 566, 4)
    __kind._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 566, 4)
    
    kind = property(__kind.value, __kind.set, None, u'The unit of chronostratigraphy.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __kind.name() : __kind
    }
Namespace.addCategoryObject('typeBinding', u'chronostratigraphyStruct', chronostratigraphyStruct)


# Complex type {http://www.witsml.org/schemas/1series}measuredDepthCoord with content type SIMPLE
class measuredDepthCoord (abstractMeasure):
    """A measured depth coordinate in a wellbore. 
			Positive moving from the reference datum toward the bottomhole.
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'measuredDepthCoord')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 577, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_measuredDepthCoord_uom', MeasuredDepthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 586, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 586, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure of the quantity value.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'datum'), 'datum', '__httpwww_witsml_orgschemas1series_measuredDepthCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 591, 4)
    __datum._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 591, 4)
    
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


# Complex type {http://www.witsml.org/schemas/1series}wellVerticalDepthCoord with content type SIMPLE
class wellVerticalDepthCoord (abstractMeasure):
    """A vertical (gravity based) depth coordinate within the context of a well.
			Positive moving downward from the reference datum. 
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wellVerticalDepthCoord')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 603, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_wellVerticalDepthCoord_uom', WellVerticalCoordinateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 612, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 612, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure of the quantity value.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'datum'), 'datum', '__httpwww_witsml_orgschemas1series_wellVerticalDepthCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 617, 4)
    __datum._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 617, 4)
    
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


# Complex type {http://www.witsml.org/schemas/1series}wellElevationCoord with content type SIMPLE
class wellElevationCoord (abstractMeasure):
    """A vertical (gravity based) elevation coordinate within the context of a well.
			Positive moving upward from the reference datum.  
			All coordinates with the same datum (and same uom) can be considered to be in the same 
			Coordinate Reference System and are thus directly comparable."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wellElevationCoord')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 628, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_wellElevationCoord_uom', WellVerticalCoordinateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 637, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 637, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure of the quantity value.\n\t\t\t\t\t\tIf not given then the default unit of measure of the explicitly\n\t\t\t\t\t\tor implicitly given datum must be assumed.')

    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'datum'), 'datum', '__httpwww_witsml_orgschemas1series_wellElevationCoord_datum', refWellDatum)
    __datum._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 644, 4)
    __datum._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 644, 4)
    
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


# Complex type {http://www.witsml.org/schemas/1series}footageNorthSouth with content type SIMPLE
class footageNorthSouth (abstractMeasure):
    """The distance to a one minute boundary on the north or south of a point.
			USA Public Land Survey System."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'footageNorthSouth')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 693, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_footageNorthSouth_uom', LengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 701, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 701, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure of the distance value.')

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ref'), 'ref', '__httpwww_witsml_orgschemas1series_footageNorthSouth_ref', NorthOrSouth, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 707, 4)
    __ref._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 707, 4)
    
    ref = property(__ref.value, __ref.set, None, u'Specifies the reference line that is the origin of the distance.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', u'footageNorthSouth', footageNorthSouth)


# Complex type {http://www.witsml.org/schemas/1series}footageEastWest with content type SIMPLE
class footageEastWest (abstractMeasure):
    """The distance to a one minute boundary on the east or west of a point.
			USA Public Land Survey System."""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'footageEastWest')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 716, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_footageEastWest_uom', LengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 724, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 724, 4)
    
    uom = property(__uom.value, __uom.set, None, u'The unit of measure of the distance value.')

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ref'), 'ref', '__httpwww_witsml_orgschemas1series_footageEastWest_ref', EastOrWest, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 730, 4)
    __ref._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 730, 4)
    
    ref = property(__ref.value, __ref.set, None, u'Specifies the reference line that is the origin of the distance.')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom,
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', u'footageEastWest', footageEastWest)


# Complex type {http://www.witsml.org/schemas/1series}cost with content type SIMPLE
class cost (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cost')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 842, 1)
    # Base type is abstractDouble
    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'currency'), 'currency', '__httpwww_witsml_orgschemas1series_cost_currency', kindString)
    __currency._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 848, 4)
    __currency._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 848, 4)
    
    currency = property(__currency.value, __currency.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __currency.name() : __currency
    }
Namespace.addCategoryObject('typeBinding', u'cost', cost)


# Complex type {http://www.witsml.org/schemas/1series}indexedObject with content type SIMPLE
class indexedObject (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = abstractTypeEnum
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'indexedObject')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 853, 1)
    # Base type is abstractTypeEnum
    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uid'), 'uid', '__httpwww_witsml_orgschemas1series_indexedObject_uid', uidString)
    __uid._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    __uid._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\attgrp_uid.xsd', 22, 2)
    
    uid = property(__uid.value, __uid.set, None, u'The unique identifier of a container element.\n\t\t\t\tThis attribute is generally required within the context of a WITSML server.\n\t\t\t\tThere should be no assumption as to the semantic content of this attribute.\n\t\t\t\tThis should only be used with recurring container types (i.e., maxOccurs greater than one).\n\t\t\t\tThe value is only required to be unique within the context of the nearest recurring parent element.')

    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'index'), 'index', '__httpwww_witsml_orgschemas1series_indexedObject_index', positiveCount, required=True)
    __index._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 859, 4)
    __index._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 859, 4)
    
    index = property(__index.value, __index.set, None, u'Indexes things with the same name. \n\t\t\t\t\t\tThat is the first one, the second one, etc.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_witsml_orgschemas1series_indexedObject_name', kindString)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 865, 4)
    __name._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 865, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_indexedObject_uom', uomString)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 866, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 866, 4)
    
    uom = property(__uom.value, __uom.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpwww_witsml_orgschemas1series_indexedObject_description', descriptionString)
    __description._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 867, 4)
    __description._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_dataTypes.xsd', 867, 4)
    
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
Namespace.addCategoryObject('typeBinding', u'indexedObject', indexedObject)


# Complex type {http://www.witsml.org/schemas/1series}accelerationLinearMeasure with content type SIMPLE
class accelerationLinearMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}accelerationLinearMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accelerationLinearMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 26, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_accelerationLinearMeasure_uom', AccelerationLinearUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 29, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 29, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'accelerationLinearMeasure', accelerationLinearMeasure)


# Complex type {http://www.witsml.org/schemas/1series}anglePerLengthMeasure with content type SIMPLE
class anglePerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}anglePerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'anglePerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 38, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_anglePerLengthMeasure_uom', AnglePerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 41, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 41, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'anglePerLengthMeasure', anglePerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}anglePerTimeMeasure with content type SIMPLE
class anglePerTimeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}anglePerTimeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'anglePerTimeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 50, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_anglePerTimeMeasure_uom', AnglePerTimeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 53, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 53, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'anglePerTimeMeasure', anglePerTimeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}areaMeasure with content type SIMPLE
class areaMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}areaMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'areaMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 62, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_areaMeasure_uom', AreaUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 65, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 65, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'areaMeasure', areaMeasure)


# Complex type {http://www.witsml.org/schemas/1series}areaPerAreaMeasure with content type SIMPLE
class areaPerAreaMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}areaPerAreaMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'areaPerAreaMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 74, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_areaPerAreaMeasure_uom', AreaPerAreaUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 77, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 77, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'areaPerAreaMeasure', areaPerAreaMeasure)


# Complex type {http://www.witsml.org/schemas/1series}compressibilityMeasure with content type SIMPLE
class compressibilityMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'compressibilityMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 86, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_compressibilityMeasure_uom', CompressibilityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 92, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 92, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'compressibilityMeasure', compressibilityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}densityMeasure with content type SIMPLE
class densityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}densityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'densityMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 97, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_densityMeasure_uom', DensityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 100, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 100, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'densityMeasure', densityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}dimensionlessMeasure with content type SIMPLE
class dimensionlessMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}dimensionlessMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dimensionlessMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 109, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_dimensionlessMeasure_uom', DimensionlessUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 112, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 112, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'dimensionlessMeasure', dimensionlessMeasure)


# Complex type {http://www.witsml.org/schemas/1series}dynamicViscosityMeasure with content type SIMPLE
class dynamicViscosityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}dynamicViscosityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dynamicViscosityMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 121, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_dynamicViscosityMeasure_uom', DynamicViscosityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 124, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 124, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'dynamicViscosityMeasure', dynamicViscosityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}electricCurrentMeasure with content type SIMPLE
class electricCurrentMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}electricCurrentMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'electricCurrentMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 133, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_electricCurrentMeasure_uom', ElectricCurrentUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 136, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 136, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'electricCurrentMeasure', electricCurrentMeasure)


# Complex type {http://www.witsml.org/schemas/1series}electricPotentialMeasure with content type SIMPLE
class electricPotentialMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}electricPotentialMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'electricPotentialMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 145, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_electricPotentialMeasure_uom', ElectricPotentialUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 148, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 148, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'electricPotentialMeasure', electricPotentialMeasure)


# Complex type {http://www.witsml.org/schemas/1series}equivalentPerMassMeasure with content type SIMPLE
class equivalentPerMassMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}equivalentPerMassMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'equivalentPerMassMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 161, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_equivalentPerMassMeasure_uom', EquivalentPerMassUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 164, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 164, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'equivalentPerMassMeasure', equivalentPerMassMeasure)


# Complex type {http://www.witsml.org/schemas/1series}forceMeasure with content type SIMPLE
class forceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}forceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'forceMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 173, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_forceMeasure_uom', ForceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 176, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 176, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'forceMeasure', forceMeasure)


# Complex type {http://www.witsml.org/schemas/1series}forcePerLengthMeasure with content type SIMPLE
class forcePerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}forcePerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'forcePerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 185, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_forcePerLengthMeasure_uom', ForcePerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 188, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 188, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'forcePerLengthMeasure', forcePerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}forcePerVolumeMeasure with content type SIMPLE
class forcePerVolumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}forcePerVolumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'forcePerVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 197, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_forcePerVolumeMeasure_uom', ForcePerVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 200, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 200, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'forcePerVolumeMeasure', forcePerVolumeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}illuminanceMeasure with content type SIMPLE
class illuminanceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}illuminanceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'illuminanceMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 209, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_illuminanceMeasure_uom', IlluminanceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 212, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 212, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'illuminanceMeasure', illuminanceMeasure)


# Complex type {http://www.witsml.org/schemas/1series}lengthMeasure with content type SIMPLE
class lengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}lengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 221, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_lengthMeasure_uom', LengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 224, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 224, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'lengthMeasure', lengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}lengthPerLengthMeasure with content type SIMPLE
class lengthPerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}lengthPerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lengthPerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 233, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_lengthPerLengthMeasure_uom', LengthPerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 236, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 236, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'lengthPerLengthMeasure', lengthPerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}magneticInductionMeasure with content type SIMPLE
class magneticInductionMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}magneticInductionMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'magneticInductionMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 249, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_magneticInductionMeasure_uom', MagneticInductionUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 252, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 252, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'magneticInductionMeasure', magneticInductionMeasure)


# Complex type {http://www.witsml.org/schemas/1series}massConcentrationMeasure with content type SIMPLE
class massConcentrationMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}massConcentrationMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'massConcentrationMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 261, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_massConcentrationMeasure_uom', MassConcentrationUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 264, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 264, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'massConcentrationMeasure', massConcentrationMeasure)


# Complex type {http://www.witsml.org/schemas/1series}massMeasure with content type SIMPLE
class massMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}massMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'massMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 273, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_massMeasure_uom', MassUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 276, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 276, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'massMeasure', massMeasure)


# Complex type {http://www.witsml.org/schemas/1series}massPerLengthMeasure with content type SIMPLE
class massPerLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}massPerLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'massPerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 285, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_massPerLengthMeasure_uom', MassPerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 288, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 288, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'massPerLengthMeasure', massPerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}momentOfForceMeasure with content type SIMPLE
class momentOfForceMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}momentOfForceMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'momentOfForceMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 297, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_momentOfForceMeasure_uom', MomentOfForceUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 300, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 300, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'momentOfForceMeasure', momentOfForceMeasure)


# Complex type {http://www.witsml.org/schemas/1series}perLengthMeasure with content type SIMPLE
class perLengthMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}perLengthMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'perLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 309, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_perLengthMeasure_uom', PerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 312, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 312, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'perLengthMeasure', perLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}permeabilityRockMeasure with content type SIMPLE
class permeabilityRockMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'permeabilityRockMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 321, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_permeabilityRockMeasure_uom', PermeabilityRockUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 327, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 327, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'permeabilityRockMeasure', permeabilityRockMeasure)


# Complex type {http://www.witsml.org/schemas/1series}planeAngleMeasure with content type SIMPLE
class planeAngleMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}planeAngleMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'planeAngleMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 332, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_planeAngleMeasure_uom', PlaneAngleUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 335, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 335, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'planeAngleMeasure', planeAngleMeasure)


# Complex type {http://www.witsml.org/schemas/1series}powerMeasure with content type SIMPLE
class powerMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}powerMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'powerMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 344, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_powerMeasure_uom', PowerUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 347, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 347, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'powerMeasure', powerMeasure)


# Complex type {http://www.witsml.org/schemas/1series}pressureMeasure with content type SIMPLE
class pressureMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}pressureMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'pressureMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 356, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_pressureMeasure_uom', PressureUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 359, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 359, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'pressureMeasure', pressureMeasure)


# Complex type {http://www.witsml.org/schemas/1series}relativePowerMeasure with content type SIMPLE
class relativePowerMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}relativePowerMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'relativePowerMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 368, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_relativePowerMeasure_uom', RelativePowerUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 371, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 371, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'relativePowerMeasure', relativePowerMeasure)


# Complex type {http://www.witsml.org/schemas/1series}specificHeatCapacityMeasure with content type SIMPLE
class specificHeatCapacityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}specificHeatCapacityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'specificHeatCapacityMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 380, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_specificHeatCapacityMeasure_uom', SpecificHeatCapacityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 383, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 383, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'specificHeatCapacityMeasure', specificHeatCapacityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}specificVolumeMeasure with content type SIMPLE
class specificVolumeMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'specificVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 388, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_specificVolumeMeasure_uom', SpecificVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 394, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 394, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'specificVolumeMeasure', specificVolumeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}standardVolumeMeasure with content type SIMPLE
class standardVolumeMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'standardVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 403, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_standardVolumeMeasure_uom', StandardVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 409, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 409, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'standardVolumeMeasure', standardVolumeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}standardVolumePerTimeMeasure with content type SIMPLE
class standardVolumePerTimeMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'standardVolumePerTimeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 414, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_standardVolumePerTimeMeasure_uom', StandardVolumePerTimeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 420, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 420, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'standardVolumePerTimeMeasure', standardVolumePerTimeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}thermalConductivityMeasure with content type SIMPLE
class thermalConductivityMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'thermalConductivityMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 425, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_thermalConductivityMeasure_uom', ThermalConductivityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 431, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 431, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'thermalConductivityMeasure', thermalConductivityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}thermalVolumetricExpansionMeasure with content type SIMPLE
class thermalVolumetricExpansionMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'thermalVolumetricExpansionMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 436, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_thermalVolumetricExpansionMeasure_uom', ThermalVolumetricExpansionUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 442, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 442, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'thermalVolumetricExpansionMeasure', thermalVolumetricExpansionMeasure)


# Complex type {http://www.witsml.org/schemas/1series}thermodynamicTemperatureMeasure with content type SIMPLE
class thermodynamicTemperatureMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}thermodynamicTemperatureMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'thermodynamicTemperatureMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 447, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_thermodynamicTemperatureMeasure_uom', ThermodynamicTemperatureUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 450, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 450, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'thermodynamicTemperatureMeasure', thermodynamicTemperatureMeasure)


# Complex type {http://www.witsml.org/schemas/1series}timeMeasure with content type SIMPLE
class timeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}timeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 459, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_timeMeasure_uom', TimeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 462, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 462, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'timeMeasure', timeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}velocityMeasure with content type SIMPLE
class velocityMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}velocityMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'velocityMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 471, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_velocityMeasure_uom', VelocityUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 474, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 474, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'velocityMeasure', velocityMeasure)


# Complex type {http://www.witsml.org/schemas/1series}volumeMeasure with content type SIMPLE
class volumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}volumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 483, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_volumeMeasure_uom', VolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 486, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 486, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'volumeMeasure', volumeMeasure)


# Complex type {http://www.witsml.org/schemas/1series}volumeFlowRateMeasure with content type SIMPLE
class volumeFlowRateMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}volumeFlowRateMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumeFlowRateMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 495, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_volumeFlowRateMeasure_uom', VolumeFlowRateUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 498, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 498, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'volumeFlowRateMeasure', volumeFlowRateMeasure)


# Complex type {http://www.witsml.org/schemas/1series}volumePerLengthMeasure with content type SIMPLE
class volumePerLengthMeasure (abstractMeasure):
    """"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumePerLengthMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 507, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_volumePerLengthMeasure_uom', VolumePerLengthUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 513, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 513, 4)
    
    uom = property(__uom.value, __uom.set, None, None)


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'volumePerLengthMeasure', volumePerLengthMeasure)


# Complex type {http://www.witsml.org/schemas/1series}volumePerVolumeMeasure with content type SIMPLE
class volumePerVolumeMeasure (abstractMeasure):
    """Complex type {http://www.witsml.org/schemas/1series}volumePerVolumeMeasure with content type SIMPLE"""
    _TypeDefinition = abstractDouble
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'volumePerVolumeMeasure')
    _XSDLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 518, 1)
    # Base type is abstractMeasure
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_witsml_orgschemas1series_volumePerVolumeMeasure_uom', VolumePerVolumeUom, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 521, 4)
    __uom._UseLocation = pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\typ_measureType.xsd', 521, 4)
    
    uom = property(__uom.value, __uom.set, None, u'')


    _ElementMap = abstractMeasure._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = abstractMeasure._AttributeMap.copy()
    _AttributeMap.update({
        __uom.name() : __uom
    })
Namespace.addCategoryObject('typeBinding', u'volumePerVolumeMeasure', volumePerVolumeMeasure)


messages = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'messages'), obj_messages, documentation=u'The WITSML API mandated plural root element which allows \n\t\t\tmultiple singular objects to be sent. The plural name is formed by adding\n\t\t\tan "s" to the singular name.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 32, 1))
Namespace.addCategoryObject('elementBinding', messages.name().localName(), messages)



cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sourceName'), nameString, scope=cs_commonData, documentation=u'An identifier to indicate the data originator.\n\t\t\t\t\tThis identifies the server that originally created \n\t\t\t\t\tthe object and thus most of the uids in the object (but not \n\t\t\t\t\tnecessarily the uids of the parents). This is typically a url. ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 26, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dTimCreation'), timestamp, scope=cs_commonData, documentation=u'When the data was created at the persistent data store. \n\t\t\t\t\tThis is an API server parameter releted to the "Special Handling of Change Information" within a server. \n\t\t\t\t\tSee the relevant API specification for the  behavior related to this element.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 34, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dTimLastChange'), timestamp, scope=cs_commonData, documentation=u'Last change of any element of the data at the persistent data store.\n\t\t\t\t\tThis is an API server parameter releted to the "Special Handling of Change Information" within a server. \n\t\t\t\t\tSee the relevant API specification for the  behavior related to this element.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 43, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'itemState'), ItemState, scope=cs_commonData, documentation=u'The item state for the data object.  ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 53, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serviceCategory'), kindString, scope=cs_commonData, documentation=u'The category of the service related to the creation of the object. \n\t\t\t\t\tFor example, "mud log service", "cement service", "LWD service", "rig service", "drilling service".\n\t\t\t\t\t', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 58, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comments'), commentString, scope=cs_commonData, documentation=u'Comments and remarks.  ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 67, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'acquisitionTimeZone'), timestampedTimeZone, scope=cs_commonData, documentation=u'The local time zone of the original acquisition date-time values. \n\t\t\t\t\tIt is the deviation in hours and minutes from UTC.\n\t\t\t\t\tThe first occurrence should be the actual local time zone at the start of acquisition\n\t\t\t\t\tand may represent a seasonally adjusted value such as daylight savings.\n\t\t\t\t\tThe dTim attribute must be populated in the second and subsequent occurrences \n\t\t\t\t\tif the local time zone changes during acquisition.\n\t\t\t\t\tThis knowledge is required because the original time zone in a dateTime\n\t\t\t\t\tvalue may be lost when software converts to a different time zone.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 72, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'defaultDatum'), refNameString, scope=cs_commonData, documentation=u'A pointer to the default wellDatum for measured depth coordinates,\n\t\t\t\t\tvertical depth coordinates and elevation coordinates in this object. \n\t\t\t\t\tDepth coordinates that do not specify a datum attribute shall be \n\t\t\t\t\tassumed to be measured relative to this default vertical datum.\n\t\t\t\t\tThe referenced wellDatum must be defined within the well object associated with this object.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 85, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'privateGroupOnly'), pyxb.binding.datatypes.boolean, scope=cs_commonData, documentation=u'This is an API query parameter.\n\t\t\t\t\tSee the API specification for the behavior related to this element.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 95, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extensionAny'), cs_extensionAny, scope=cs_commonData, documentation=u'Extensions to the schema using an xsd:any construct.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 102, 3)))

cs_commonData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extensionNameValue'), cs_extensionNameValue, scope=cs_commonData, documentation=u'Extensions to the schema based on a name-value construct.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 108, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 26, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 34, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 43, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 53, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 58, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 67, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 72, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 85, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 95, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 102, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 108, 3))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sourceName')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dTimCreation')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 34, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dTimLastChange')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 43, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'itemState')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 53, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serviceCategory')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 58, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comments')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 67, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'acquisitionTimeZone')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 72, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'defaultDatum')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 85, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'privateGroupOnly')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 95, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extensionAny')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 102, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(cs_commonData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extensionNameValue')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_commonData.xsd', 108, 3))
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
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_customData.xsd', 24, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_customData.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_customData._Automaton = _BuildAutomaton_()




cs_documentAudit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'event'), cs_documentEvent, scope=cs_documentAudit, documentation=u'One event related to the data.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentAudit.xsd', 27, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_documentAudit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'event')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentAudit.xsd', 27, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cs_documentAudit._Automaton = _BuildAutomaton_2()




cs_documentFileCreation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fileCreationDate'), timestamp, scope=cs_documentFileCreation, documentation=u'The date and time that the file was created.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 27, 3)))

cs_documentFileCreation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'softwareName'), nameString, scope=cs_documentFileCreation, documentation=u'If appropriate, the software that created the file. \n\t\t\t\t\tThis is a free form string, and may include whatever information \n\t\t\t\t\tis deemed relevant.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 33, 3)))

cs_documentFileCreation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fileCreator'), nameString, scope=cs_documentFileCreation, documentation=u'The person or business associate that created \n\t\t\t\t\tthe file.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 41, 3)))

cs_documentFileCreation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), commentString, scope=cs_documentFileCreation, documentation=u'Any comment that would be useful to further \n\t\t\t\t\texplain the creation of this instance document.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 48, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 33, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 41, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 48, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_documentFileCreation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fileCreationDate')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 27, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentFileCreation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'softwareName')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 33, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentFileCreation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fileCreator')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentFileCreation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentFileCreation.xsd', 48, 3))
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




cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'documentName'), nameStruct, scope=cs_documentInfo, documentation=u'An identifier for the document. This is \n\t\t\t\t\tintended to be unique within the context of the NamingSystem.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 31, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'documentAlias'), nameStruct, scope=cs_documentInfo, documentation=u'Zero or more alternate names for the document. \n\t\t\t\t\tThese names do not need to be unique within the naming system.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 38, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'documentDate'), timestamp, scope=cs_documentInfo, documentation=u'The date of the creation of the document. \n\t\t\t\t\tThis is not the same as the date that the file was created. \n\t\t\t\t\tFor this date, the document is considered to be the set of \n\t\t\t\t\tinformation associated with this document information. \n\t\t\t\t\tFor example, the document may be a seismic binset. \n\t\t\t\t\tThis represents the date that the binset was created. \n\t\t\t\t\tThe FileCreation information would capture the date that \n\t\t\t\t\tthe XML file was created to send or exchange the binset.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 45, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'documentClass'), nameStruct, scope=cs_documentInfo, documentation=u'A document class. Examples of classes would be a \n\t\t\t\t\tmetadata classification or a set of keywords. ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 58, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fileCreationInformation'), cs_documentFileCreation, scope=cs_documentInfo, documentation=u'The information about the creation of the \n\t\t\t\t\texchange file. This is not about the creation of the data within \n\t\t\t\t\tthe file, but the creation of the file itself.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 64, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'securityInformation'), cs_documentSecurityInfo, scope=cs_documentInfo, documentation=u'Information about the security to be applied to \n\t\t\t\t\tthis file. More than one classification can be given.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 72, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'disclaimer'), commentString, scope=cs_documentInfo, documentation=u'A free-form string that allows a disclaimer to \n\t\t\t\t\taccompany the information.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 79, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'auditTrail'), cs_documentAudit, scope=cs_documentInfo, documentation=u'A collection of events that can document the \n\t\t\t\t\thistory of the data.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 86, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'owner'), nameString, scope=cs_documentInfo, documentation=u'The owner of the data.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 93, 3)))

cs_documentInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), commentString, scope=cs_documentInfo, documentation=u'An optional comment about the document.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 99, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 38, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 45, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 58, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 64, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=5L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 72, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 79, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 86, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 93, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 99, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'documentName')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 31, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'documentAlias')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 38, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'documentDate')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 45, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'documentClass')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 58, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fileCreationInformation')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 64, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'securityInformation')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 72, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'disclaimer')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 79, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'auditTrail')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 86, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'owner')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 93, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentInfo.xsd', 99, 3))
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
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionAny.xsd', 26, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionAny.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cs_extensionAny._Automaton = _BuildAutomaton_5()




obj_messages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'documentInfo'), cs_documentInfo, scope=obj_messages, documentation=u'Information about the XML message instance.  ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 48, 5)))

obj_messages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), obj_message, scope=obj_messages, documentation=u'A single message.  ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 53, 5)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 48, 5))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_messages._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'documentInfo')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 48, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(obj_messages._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 53, 5))
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
obj_messages._Automaton = _BuildAutomaton_6()




cs_documentEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eventDate'), timestamp, scope=cs_documentEvent, documentation=u'The date on which the event took place.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 28, 3)))

cs_documentEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eventType'), nameString, scope=cs_documentEvent, documentation=u'The kind of event event.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 34, 3)))

cs_documentEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responsibleParty'), nameString, scope=cs_documentEvent, documentation=u'The party responsible for the event.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 40, 3)))

cs_documentEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), commentString, scope=cs_documentEvent, documentation=u'A free form comment that can further \n\t\t\t\t\tdefine the event that occurred.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 46, 3)))

cs_documentEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extensionNameValue'), cs_extensionNameValue, scope=cs_documentEvent, documentation=u'Extensions to the schema based on a name-value construct.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 53, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 34, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 40, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 46, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 53, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_documentEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eventDate')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 28, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eventType')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 34, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responsibleParty')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 40, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 46, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extensionNameValue')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentEvent.xsd', 53, 3))
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
cs_documentEvent._Automaton = _BuildAutomaton_7()




cs_documentSecurityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'class'), kindString, scope=cs_documentSecurityInfo, documentation=u'The security class in which this document is \n\t\t\t\t\tclassified. Examples would be confidential, partner confidential, \n\t\t\t\t\ttight. The meaning of the class is determined by the System in which \n\t\t\t\t\tit is defined.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 33, 3)))

cs_documentSecurityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'securitySystem'), kindString, scope=cs_documentSecurityInfo, documentation=u'The security classification system. \n\t\t\t\t\tThis gives context to the meaning of the Class value.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 42, 3)))

cs_documentSecurityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endDate'), timestamp, scope=cs_documentSecurityInfo, documentation=u'The date on which this security class is no \n\t\t\t\t\tlonger applicable.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 49, 3)))

cs_documentSecurityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), commentString, scope=cs_documentSecurityInfo, documentation=u'A general comment to further define the security \n\t\t\t\t\tclass.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 56, 3)))

cs_documentSecurityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extensionNameValue'), cs_extensionNameValue, scope=cs_documentSecurityInfo, documentation=u'Extensions to the schema based on a name-value construct.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 63, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 33, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 42, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 49, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 56, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 63, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentSecurityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'class')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 33, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentSecurityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'securitySystem')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 42, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentSecurityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'endDate')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 49, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentSecurityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 56, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_documentSecurityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extensionNameValue')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_documentSecurityInfo.xsd', 63, 3))
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
cs_documentSecurityInfo._Automaton = _BuildAutomaton_8()




cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), ExtensionName, scope=cs_extensionNameValue, documentation=u'The name of the extension.\n\t\t\t\t\tEach standard name should document the expected measure class.\n\t\t\t\t\tEach standard name should document the expected maximum size. \n\t\t\t\t\tFor numeric values the size should be in terms of xsd types\n\t\t\t\t\tsuch as int, long, short, byte, float or double.\n\t\t\t\t\tFor strings, the maximum length should be defined in number of characters.\n\t\t\t\t\tLocal extensions to the list of standard names are allowed but it is strongly\n\t\t\t\t\trecommended that the names and definitions be approved by the \n\t\t\t\t\tWITSML SIG Technical Team before use.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 29, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'value'), extensionvalue, scope=cs_extensionNameValue, documentation=u'The value of the extension. \n\t\t\t\t\tThis may also include a uom attribute. \n\t\t\t\t\tThe content should conform to constraints defined by the data type.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 42, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dataType'), PrimitiveType, scope=cs_extensionNameValue, documentation=u'The underlying XML type of the value.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 49, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dTim'), timestamp, scope=cs_extensionNameValue, documentation=u'The date-time associated with the value.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 54, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'md'), measuredDepthCoord, scope=cs_extensionNameValue, documentation=u'The measured depth associated with the value.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 59, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'index'), positiveCount, scope=cs_extensionNameValue, documentation=u'Indexes things with the same name. \n\t\t\t\t\tThat is, 1 indicates the first one, 2 incidates the second one, etc.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 64, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'measureClass'), MeasureClass, scope=cs_extensionNameValue, documentation=u'The kind of the measure. For example, "length".\n\t\t\t\t\tThis should be specified if the value requires a unit of measure.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 70, 3)))

cs_extensionNameValue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), descriptionString, scope=cs_extensionNameValue, documentation=u'A textual description of the extension.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 76, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 54, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 59, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 64, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 70, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 76, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 29, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'value')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 42, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dataType')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 49, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dTim')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 54, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'md')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 59, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'index')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 64, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'measureClass')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 70, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(cs_extensionNameValue._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\cs_extensionNameValue.xsd', 76, 3))
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
cs_extensionNameValue._Automaton = _BuildAutomaton_9()




obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'objectReference'), refObjectString, scope=obj_message, documentation=u'A reference to an object that is defined within the \n\t\t\t\t\tcontext of a wellbore.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 25, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subObjectReference'), refObjectString, scope=obj_message, documentation=u'A reference to an sub-object that is defined within the \n\t\t\t\t\tcontext of the object referenced by objectReference.\n\t\t\t\t\tThis should only refer to recurring components of a growing object.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 31, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dTim'), timestamp, scope=obj_message, documentation=u'Date and time the information is related to.  ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 38, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'activityCode'), ActivityCode, scope=obj_message, documentation=u'A code used to define rig activity.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 43, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'detailActivity'), str32, scope=obj_message, documentation=u'Custom string to further define an activity.  ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 48, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'md'), measuredDepthCoord, scope=obj_message, documentation=u'Along hole measured depth of measurement from the drill datum.  ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 53, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mdBit'), measuredDepthCoord, scope=obj_message, documentation=u'Along hole measured depth of measurement from the drill datum.  ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 58, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'typeMessage'), MessageType, scope=obj_message, documentation=u'Message type.  ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 63, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'messageText'), commentString, scope=obj_message, documentation=u'Message text. ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 68, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param'), indexedObject, scope=obj_message, documentation=u'Any extra numeric data.\n\t\t\t\t\tFor this usage the name attribute MUST be specified because it represents the meaning of the data.\n\t\t\t\t\tWhile the index attribute is mandatory, it is only significant if the same name repeats.', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 73, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'severity'), MessageSeverity, scope=obj_message, documentation=u'Severity of incident.  ', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 81, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'warnProbability'), MessageProbability, scope=obj_message, documentation=u'A warning probability (applies to warning).', location=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 86, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameWell'), nameString, scope=obj_message, documentation=u'Human recognizable context for the well that contains the wellbore.  ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 72, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameWellbore'), nameString, scope=obj_message, documentation=u'Human recognizable context for the wellbore that contains the message.  ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 77, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), nameString, scope=obj_message, documentation=u'Human recognizable context for the risk.  ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 82, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'commonData'), cs_commonData, scope=obj_message, documentation=u'A container element that contains elements that are common to all data \n\t\t\t\t\tobjects.  ', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 92, 3)))

obj_message._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customData'), cs_customData, scope=obj_message, documentation=u'A container element that can contain custom or user defined \n\t\t\t\t\tdata elements.', location=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 98, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 25, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 31, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 43, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 48, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 53, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 58, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 68, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 73, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 81, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 86, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 87, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 92, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 98, 3))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'objectReference')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 25, 3))
    st_0 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subObjectReference')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 31, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dTim')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'activityCode')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 43, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'detailActivity')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 48, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'md')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 53, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mdBit')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 58, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'typeMessage')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 63, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'messageText')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 68, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'param')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 73, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'severity')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 81, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'warnProbability')), pyxb.utils.utility.Location(u'O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\grp_message.xsd', 86, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameWell')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 72, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameWellbore')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 77, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 82, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'commonData')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 92, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(obj_message._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customData')), pyxb.utils.utility.Location('O:\\1\\dataset_comparison\\WITSMLComparison\\schema\\WITSML_v1.4.1.1_Data_Schema\\witsml_v1.4.1.1_data\\xsd_schemas\\obj_message.xsd', 98, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
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
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False),
        fac.UpdateInstruction(cc_10, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False),
        fac.UpdateInstruction(cc_10, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False),
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False),
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
obj_message._Automaton = _BuildAutomaton_10()


messages._setSubstitutionGroup(_abs.abstractDataObject)
