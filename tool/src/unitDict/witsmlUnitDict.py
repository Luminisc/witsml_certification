# .\witsmlUnitDict.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:de5669d245f178776916647737ebc73cda75213c
# Generated 2013-06-15 09:37:57.341000 by PyXB version 1.2.1
# Namespace http://www.posc.org/schemas

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2b93b761-d5c9-11e2-b6f8-402cf4641f59')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.posc.org/schemas', create_if_missing=True)
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 4, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}DocumentInformation uses Python identifier DocumentInformation
    __DocumentInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DocumentInformation'), 'DocumentInformation', '__httpwww_posc_orgschemas_CTD_ANON_httpwww_posc_orgschemasDocumentInformation', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 6, 8), )

    
    DocumentInformation = property(__DocumentInformation.value, __DocumentInformation.set, None, None)

    
    # Element {http://www.posc.org/schemas}UnitsDefinition uses Python identifier UnitsDefinition
    __UnitsDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'UnitsDefinition'), 'UnitsDefinition', '__httpwww_posc_orgschemas_CTD_ANON_httpwww_posc_orgschemasUnitsDefinition', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 47, 8), )

    
    UnitsDefinition = property(__UnitsDefinition.value, __UnitsDefinition.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_posc_orgschemas_CTD_ANON_version', pyxb.binding.datatypes.decimal, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 118, 6)
    __version._UseLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 118, 6)
    
    version = property(__version.value, __version.set, None, None)


    _ElementMap = {
        __DocumentInformation.name() : __DocumentInformation,
        __UnitsDefinition.name() : __UnitsDefinition
    }
    _AttributeMap = {
        __version.name() : __version
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 7, 10)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}DocumentName uses Python identifier DocumentName
    __DocumentName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DocumentName'), 'DocumentName', '__httpwww_posc_orgschemas_CTD_ANON__httpwww_posc_orgschemasDocumentName', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 9, 14), )

    
    DocumentName = property(__DocumentName.value, __DocumentName.set, None, None)

    
    # Element {http://www.posc.org/schemas}DocumentDate uses Python identifier DocumentDate
    __DocumentDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DocumentDate'), 'DocumentDate', '__httpwww_posc_orgschemas_CTD_ANON__httpwww_posc_orgschemasDocumentDate', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 16, 14), )

    
    DocumentDate = property(__DocumentDate.value, __DocumentDate.set, None, None)

    
    # Element {http://www.posc.org/schemas}FileCreationInformation uses Python identifier FileCreationInformation
    __FileCreationInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileCreationInformation'), 'FileCreationInformation', '__httpwww_posc_orgschemas_CTD_ANON__httpwww_posc_orgschemasFileCreationInformation', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 17, 14), )

    
    FileCreationInformation = property(__FileCreationInformation.value, __FileCreationInformation.set, None, None)

    
    # Element {http://www.posc.org/schemas}Disclaimer uses Python identifier Disclaimer
    __Disclaimer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Disclaimer'), 'Disclaimer', '__httpwww_posc_orgschemas_CTD_ANON__httpwww_posc_orgschemasDisclaimer', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 26, 14), )

    
    Disclaimer = property(__Disclaimer.value, __Disclaimer.set, None, None)

    
    # Element {http://www.posc.org/schemas}AuditTrail uses Python identifier AuditTrail
    __AuditTrail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AuditTrail'), 'AuditTrail', '__httpwww_posc_orgschemas_CTD_ANON__httpwww_posc_orgschemasAuditTrail', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 27, 14), )

    
    AuditTrail = property(__AuditTrail.value, __AuditTrail.set, None, None)

    
    # Element {http://www.posc.org/schemas}DataOwnerID uses Python identifier DataOwnerID
    __DataOwnerID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DataOwnerID'), 'DataOwnerID', '__httpwww_posc_orgschemas_CTD_ANON__httpwww_posc_orgschemasDataOwnerID', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 42, 14), )

    
    DataOwnerID = property(__DataOwnerID.value, __DataOwnerID.set, None, None)

    
    # Element {http://www.posc.org/schemas}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Comment'), 'Comment', '__httpwww_posc_orgschemas_CTD_ANON__httpwww_posc_orgschemasComment', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 43, 14), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)


    _ElementMap = {
        __DocumentName.name() : __DocumentName,
        __DocumentDate.name() : __DocumentDate,
        __FileCreationInformation.name() : __FileCreationInformation,
        __Disclaimer.name() : __Disclaimer,
        __AuditTrail.name() : __AuditTrail,
        __DataOwnerID.name() : __DataOwnerID,
        __Comment.name() : __Comment
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 10, 16)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpwww_posc_orgschemas_CTD_ANON_2_httpwww_posc_orgschemasName', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 12, 20), )

    
    Name = property(__Name.value, __Name.set, None, None)


    _ElementMap = {
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 18, 16)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}FileCreationDate uses Python identifier FileCreationDate
    __FileCreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileCreationDate'), 'FileCreationDate', '__httpwww_posc_orgschemas_CTD_ANON_3_httpwww_posc_orgschemasFileCreationDate', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 20, 20), )

    
    FileCreationDate = property(__FileCreationDate.value, __FileCreationDate.set, None, None)

    
    # Element {http://www.posc.org/schemas}FileCreator uses Python identifier FileCreator
    __FileCreator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileCreator'), 'FileCreator', '__httpwww_posc_orgschemas_CTD_ANON_3_httpwww_posc_orgschemasFileCreator', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 21, 20), )

    
    FileCreator = property(__FileCreator.value, __FileCreator.set, None, None)

    
    # Element {http://www.posc.org/schemas}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Comment'), 'Comment', '__httpwww_posc_orgschemas_CTD_ANON_3_httpwww_posc_orgschemasComment', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 22, 20), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)


    _ElementMap = {
        __FileCreationDate.name() : __FileCreationDate,
        __FileCreator.name() : __FileCreator,
        __Comment.name() : __Comment
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 28, 16)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}Event uses Python identifier Event
    __Event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Event'), 'Event', '__httpwww_posc_orgschemas_CTD_ANON_4_httpwww_posc_orgschemasEvent', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 30, 20), )

    
    Event = property(__Event.value, __Event.set, None, None)


    _ElementMap = {
        __Event.name() : __Event
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 31, 22)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}EventDate uses Python identifier EventDate
    __EventDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EventDate'), 'EventDate', '__httpwww_posc_orgschemas_CTD_ANON_5_httpwww_posc_orgschemasEventDate', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 33, 26), )

    
    EventDate = property(__EventDate.value, __EventDate.set, None, None)

    
    # Element {http://www.posc.org/schemas}ResponsiblePartyID uses Python identifier ResponsiblePartyID
    __ResponsiblePartyID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ResponsiblePartyID'), 'ResponsiblePartyID', '__httpwww_posc_orgschemas_CTD_ANON_5_httpwww_posc_orgschemasResponsiblePartyID', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 34, 26), )

    
    ResponsiblePartyID = property(__ResponsiblePartyID.value, __ResponsiblePartyID.set, None, None)

    
    # Element {http://www.posc.org/schemas}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Comment'), 'Comment', '__httpwww_posc_orgschemas_CTD_ANON_5_httpwww_posc_orgschemasComment', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 35, 26), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)


    _ElementMap = {
        __EventDate.name() : __EventDate,
        __ResponsiblePartyID.name() : __ResponsiblePartyID,
        __Comment.name() : __Comment
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 48, 10)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}UnitOfMeasure uses Python identifier UnitOfMeasure
    __UnitOfMeasure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'UnitOfMeasure'), 'UnitOfMeasure', '__httpwww_posc_orgschemas_CTD_ANON_6_httpwww_posc_orgschemasUnitOfMeasure', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 50, 14), )

    
    UnitOfMeasure = property(__UnitOfMeasure.value, __UnitOfMeasure.set, None, None)


    _ElementMap = {
        __UnitOfMeasure.name() : __UnitOfMeasure
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 51, 16)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpwww_posc_orgschemas_CTD_ANON_7_httpwww_posc_orgschemasName', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 54, 22), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {http://www.posc.org/schemas}QuantityType uses Python identifier QuantityType
    __QuantityType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'QuantityType'), 'QuantityType', '__httpwww_posc_orgschemas_CTD_ANON_7_httpwww_posc_orgschemasQuantityType', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 55, 22), )

    
    QuantityType = property(__QuantityType.value, __QuantityType.set, None, None)

    
    # Element {http://www.posc.org/schemas}DimensionalClass uses Python identifier DimensionalClass
    __DimensionalClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DimensionalClass'), 'DimensionalClass', '__httpwww_posc_orgschemas_CTD_ANON_7_httpwww_posc_orgschemasDimensionalClass', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 56, 22), )

    
    DimensionalClass = property(__DimensionalClass.value, __DimensionalClass.set, None, None)

    
    # Element {http://www.posc.org/schemas}SameUnit uses Python identifier SameUnit
    __SameUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SameUnit'), 'SameUnit', '__httpwww_posc_orgschemas_CTD_ANON_7_httpwww_posc_orgschemasSameUnit', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 57, 22), )

    
    SameUnit = property(__SameUnit.value, __SameUnit.set, None, None)

    
    # Element {http://www.posc.org/schemas}CatalogName uses Python identifier CatalogName
    __CatalogName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CatalogName'), 'CatalogName', '__httpwww_posc_orgschemas_CTD_ANON_7_httpwww_posc_orgschemasCatalogName', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 63, 22), )

    
    CatalogName = property(__CatalogName.value, __CatalogName.set, None, None)

    
    # Element {http://www.posc.org/schemas}CatalogSymbol uses Python identifier CatalogSymbol
    __CatalogSymbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CatalogSymbol'), 'CatalogSymbol', '__httpwww_posc_orgschemas_CTD_ANON_7_httpwww_posc_orgschemasCatalogSymbol', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 64, 22), )

    
    CatalogSymbol = property(__CatalogSymbol.value, __CatalogSymbol.set, None, None)

    
    # Element {http://www.posc.org/schemas}ConversionToBaseUnit uses Python identifier ConversionToBaseUnit
    __ConversionToBaseUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ConversionToBaseUnit'), 'ConversionToBaseUnit', '__httpwww_posc_orgschemas_CTD_ANON_7_httpwww_posc_orgschemasConversionToBaseUnit', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 73, 22), )

    
    ConversionToBaseUnit = property(__ConversionToBaseUnit.value, __ConversionToBaseUnit.set, None, None)

    
    # Element {http://www.posc.org/schemas}Deprecated uses Python identifier Deprecated
    __Deprecated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Deprecated'), 'Deprecated', '__httpwww_posc_orgschemas_CTD_ANON_7_httpwww_posc_orgschemasDeprecated', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 99, 22), )

    
    Deprecated = property(__Deprecated.value, __Deprecated.set, None, None)

    
    # Element {http://www.posc.org/schemas}BaseUnit uses Python identifier BaseUnit
    __BaseUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'BaseUnit'), 'BaseUnit', '__httpwww_posc_orgschemas_CTD_ANON_7_httpwww_posc_orgschemasBaseUnit', True, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 100, 22), )

    
    BaseUnit = property(__BaseUnit.value, __BaseUnit.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_posc_orgschemas_CTD_ANON_7_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 110, 18)
    __id._UseLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 110, 18)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'annotation'), 'annotation', '__httpwww_posc_orgschemas_CTD_ANON_7_annotation', pyxb.binding.datatypes.string, required=True)
    __annotation._DeclarationLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 111, 18)
    __annotation._UseLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 111, 18)
    
    annotation = property(__annotation.value, __annotation.set, None, None)


    _ElementMap = {
        __Name.name() : __Name,
        __QuantityType.name() : __QuantityType,
        __DimensionalClass.name() : __DimensionalClass,
        __SameUnit.name() : __SameUnit,
        __CatalogName.name() : __CatalogName,
        __CatalogSymbol.name() : __CatalogSymbol,
        __ConversionToBaseUnit.name() : __ConversionToBaseUnit,
        __Deprecated.name() : __Deprecated,
        __BaseUnit.name() : __BaseUnit
    }
    _AttributeMap = {
        __id.name() : __id,
        __annotation.name() : __annotation
    }



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 58, 24)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_posc_orgschemas_CTD_ANON_8_uom', pyxb.binding.datatypes.string, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 59, 26)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 59, 26)
    
    uom = property(__uom.value, __uom.set, None, None)

    
    # Attribute namingSystem uses Python identifier namingSystem
    __namingSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'namingSystem'), 'namingSystem', '__httpwww_posc_orgschemas_CTD_ANON_8_namingSystem', pyxb.binding.datatypes.string, required=True)
    __namingSystem._DeclarationLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 60, 26)
    __namingSystem._UseLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 60, 26)
    
    namingSystem = property(__namingSystem.value, __namingSystem.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __uom.name() : __uom,
        __namingSystem.name() : __namingSystem
    }



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 65, 24)
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute isExplicit uses Python identifier isExplicit
    __isExplicit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'isExplicit'), 'isExplicit', '__httpwww_posc_orgschemas_CTD_ANON_9_isExplicit', pyxb.binding.datatypes.boolean, required=True)
    __isExplicit._DeclarationLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 68, 30)
    __isExplicit._UseLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 68, 30)
    
    isExplicit = property(__isExplicit.value, __isExplicit.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __isExplicit.name() : __isExplicit
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 74, 24)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}Formula uses Python identifier Formula
    __Formula = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Formula'), 'Formula', '__httpwww_posc_orgschemas_CTD_ANON_10_httpwww_posc_orgschemasFormula', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 76, 28), )

    
    Formula = property(__Formula.value, __Formula.set, None, None)

    
    # Element {http://www.posc.org/schemas}Fraction uses Python identifier Fraction
    __Fraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Fraction'), 'Fraction', '__httpwww_posc_orgschemas_CTD_ANON_10_httpwww_posc_orgschemasFraction', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 86, 28), )

    
    Fraction = property(__Fraction.value, __Fraction.set, None, None)

    
    # Element {http://www.posc.org/schemas}Factor uses Python identifier Factor
    __Factor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Factor'), 'Factor', '__httpwww_posc_orgschemas_CTD_ANON_10_httpwww_posc_orgschemasFactor', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 94, 28), )

    
    Factor = property(__Factor.value, __Factor.set, None, None)

    
    # Attribute baseUnit uses Python identifier baseUnit
    __baseUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'baseUnit'), 'baseUnit', '__httpwww_posc_orgschemas_CTD_ANON_10_baseUnit', pyxb.binding.datatypes.string, required=True)
    __baseUnit._DeclarationLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 96, 26)
    __baseUnit._UseLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 96, 26)
    
    baseUnit = property(__baseUnit.value, __baseUnit.set, None, None)


    _ElementMap = {
        __Formula.name() : __Formula,
        __Fraction.name() : __Fraction,
        __Factor.name() : __Factor
    }
    _AttributeMap = {
        __baseUnit.name() : __baseUnit
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 77, 30)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}A uses Python identifier A
    __A = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'A'), 'A', '__httpwww_posc_orgschemas_CTD_ANON_11_httpwww_posc_orgschemasA', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 79, 34), )

    
    A = property(__A.value, __A.set, None, None)

    
    # Element {http://www.posc.org/schemas}B uses Python identifier B
    __B = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'B'), 'B', '__httpwww_posc_orgschemas_CTD_ANON_11_httpwww_posc_orgschemasB', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 80, 34), )

    
    B = property(__B.value, __B.set, None, None)

    
    # Element {http://www.posc.org/schemas}C uses Python identifier C
    __C = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'C'), 'C', '__httpwww_posc_orgschemas_CTD_ANON_11_httpwww_posc_orgschemasC', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 81, 34), )

    
    C = property(__C.value, __C.set, None, None)

    
    # Element {http://www.posc.org/schemas}D uses Python identifier D
    __D = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'D'), 'D', '__httpwww_posc_orgschemas_CTD_ANON_11_httpwww_posc_orgschemasD', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 82, 34), )

    
    D = property(__D.value, __D.set, None, None)


    _ElementMap = {
        __A.name() : __A,
        __B.name() : __B,
        __C.name() : __C,
        __D.name() : __D
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 87, 30)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}Numerator uses Python identifier Numerator
    __Numerator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Numerator'), 'Numerator', '__httpwww_posc_orgschemas_CTD_ANON_12_httpwww_posc_orgschemasNumerator', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 89, 34), )

    
    Numerator = property(__Numerator.value, __Numerator.set, None, None)

    
    # Element {http://www.posc.org/schemas}Denominator uses Python identifier Denominator
    __Denominator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Denominator'), 'Denominator', '__httpwww_posc_orgschemas_CTD_ANON_12_httpwww_posc_orgschemasDenominator', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 90, 34), )

    
    Denominator = property(__Denominator.value, __Denominator.set, None, None)


    _ElementMap = {
        __Numerator.name() : __Numerator,
        __Denominator.name() : __Denominator
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 101, 24)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.posc.org/schemas}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpwww_posc_orgschemas_CTD_ANON_13_httpwww_posc_orgschemasDescription', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 103, 28), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://www.posc.org/schemas}BasicAuthority uses Python identifier BasicAuthority
    __BasicAuthority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'BasicAuthority'), 'BasicAuthority', '__httpwww_posc_orgschemas_CTD_ANON_13_httpwww_posc_orgschemasBasicAuthority', False, pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 104, 28), )

    
    BasicAuthority = property(__BasicAuthority.value, __BasicAuthority.set, None, None)


    _ElementMap = {
        __Description.name() : __Description,
        __BasicAuthority.name() : __BasicAuthority
    }
    _AttributeMap = {
        
    }



UnitOfMeasureDictionary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UnitOfMeasureDictionary'), CTD_ANON, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', UnitOfMeasureDictionary.name().localName(), UnitOfMeasureDictionary)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DocumentInformation'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 6, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UnitsDefinition'), CTD_ANON_6, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 47, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DocumentInformation')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 6, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UnitsDefinition')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 47, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DocumentName'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 9, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DocumentDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 16, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileCreationInformation'), CTD_ANON_3, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 17, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Disclaimer'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 26, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AuditTrail'), CTD_ANON_4, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 27, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataOwnerID'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 42, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Comment'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 43, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DocumentName')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 9, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DocumentDate')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 16, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileCreationInformation')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 17, 14))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Disclaimer')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 26, 14))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AuditTrail')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 27, 14))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataOwnerID')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 42, 14))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Comment')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 43, 14))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 12, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 12, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileCreationDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 20, 20)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileCreator'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 21, 20)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Comment'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 22, 20)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileCreationDate')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 20, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileCreator')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 21, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Comment')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 22, 20))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Event'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 30, 20)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Event')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 30, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EventDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 33, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ResponsiblePartyID'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 34, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Comment'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 35, 26)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EventDate')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 33, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ResponsiblePartyID')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 34, 26))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Comment')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 35, 26))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UnitOfMeasure'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 50, 14)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UnitOfMeasure')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 50, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 54, 22)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuantityType'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 55, 22)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DimensionalClass'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 56, 22)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SameUnit'), CTD_ANON_8, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 57, 22)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogName'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 63, 22)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CatalogSymbol'), CTD_ANON_9, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 64, 22)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConversionToBaseUnit'), CTD_ANON_10, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 73, 22)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Deprecated'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 99, 22)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BaseUnit'), CTD_ANON_13, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 100, 22)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 54, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'QuantityType')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 55, 22))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DimensionalClass')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 56, 22))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SameUnit')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 57, 22))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogName')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 63, 22))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CatalogSymbol')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 64, 22))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConversionToBaseUnit')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 73, 22))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Deprecated')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 99, 22))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BaseUnit')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 100, 22))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    st_0._set_transitionSet(transitions)
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
    st_1._set_transitionSet(transitions)
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
    st_2._set_transitionSet(transitions)
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
    st_3._set_transitionSet(transitions)
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
    st_4._set_transitionSet(transitions)
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
    st_5._set_transitionSet(transitions)
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
    st_6._set_transitionSet(transitions)
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
    st_7._set_transitionSet(transitions)
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
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Formula'), CTD_ANON_11, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 76, 28)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fraction'), CTD_ANON_12, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 86, 28)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Factor'), pyxb.binding.datatypes.double, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 94, 28)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 76, 28))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 86, 28))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 94, 28))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Formula')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 76, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fraction')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 86, 28))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Factor')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 94, 28))
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
CTD_ANON_10._Automaton = _BuildAutomaton_8()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'A'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 79, 34)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'B'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 80, 34)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'C'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 81, 34)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'D'), pyxb.binding.datatypes.unsignedByte, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 82, 34)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'A')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 79, 34))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'B')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 80, 34))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'C')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 81, 34))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'D')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 82, 34))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_9()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Numerator'), pyxb.binding.datatypes.double, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 89, 34)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Denominator'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 90, 34)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Numerator')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 89, 34))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Denominator')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 90, 34))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_10()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 103, 28)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BasicAuthority'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 104, 28)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 102, 26))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 103, 28))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 104, 28))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 103, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BasicAuthority')), pyxb.utils.utility.Location('C:\\TEMP\\witsmlUnit\\witsmlUnitDict.xsd', 104, 28))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_11()

