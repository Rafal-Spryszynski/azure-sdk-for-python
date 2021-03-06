# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PropertyDescription(Model):
    """Description of a Service Fabric property.

    :param property_name:
    :type property_name: str
    :param custom_type_id:
    :type custom_type_id: str
    :param value:
    :type value: :class:`PropertyValue
     <azure.servicefabric.models.PropertyValue>`
    """

    _validation = {
        'property_name': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'property_name': {'key': 'PropertyName', 'type': 'str'},
        'custom_type_id': {'key': 'CustomTypeId', 'type': 'str'},
        'value': {'key': 'Value', 'type': 'PropertyValue'},
    }

    def __init__(self, property_name, value, custom_type_id=None):
        self.property_name = property_name
        self.custom_type_id = custom_type_id
        self.value = value
