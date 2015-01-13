# .\_abs.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8303e32165e8ecb1e71ee1daf2c80a31c9900992
# Generated 2013-06-21 14:43:43.197000 by PyXB version 1.2.1
# Namespace http://www.energistics.org/schemas/abstract [xmlns:abs]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dfed69f0-daaa-11e2-b5f8-08002718187b')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.energistics.org/schemas/abstract', create_if_missing=True)
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


# Complex type {http://www.energistics.org/schemas/abstract}abstractObject with content type EMPTY
class abstractObject (pyxb.binding.basis.complexTypeDefinition):
    """The intended abstract supertype of all schema roots 
			that may be a member of a substitution group (whether contextual or data).
			The type of root global elements should be extended from this type and the 
			root global element should be declared to be a member of one of the above substitution groups."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'abstractObject')
    _XSDLocation = pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.4.1.0_Data_Schema\\abstract_v1.0\\xsd_schemas\\sub_abstractSubstitutionGroup.xsd', 30, 1)
    # Base type is pyxb.binding.datatypes.anyType

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'abstractObject', abstractObject)


abstractDataObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'abstractDataObject'), abstractObject, abstract=pyxb.binding.datatypes.boolean(1), documentation=u'Substitution group for normative data objects.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.4.1.0_Data_Schema\\abstract_v1.0\\xsd_schemas\\sub_abstractSubstitutionGroup.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', abstractDataObject.name().localName(), abstractDataObject)

abstractContextualObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'abstractContextualObject'), abstractObject, abstract=pyxb.binding.datatypes.boolean(1), documentation=u'Substitution group for contextual objects.', location=pyxb.utils.utility.Location(u'o:\\1\\witsml_certification\\trunk\\src\\wsvt\\schemas\\WITSML_v1.4.1.0_Data_Schema\\abstract_v1.0\\xsd_schemas\\sub_abstractSubstitutionGroup.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', abstractContextualObject.name().localName(), abstractContextualObject)
