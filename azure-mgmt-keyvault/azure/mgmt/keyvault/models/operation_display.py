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


class OperationDisplay(Model):
    """Display metadata associated with the operation.

    :param provider: Service provider: Microsoft Key Vault.
    :type provider: str
    :param resource: Resource on which the operation is performed etc.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Decription of operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, provider=None, resource=None, operation=None, description=None):
        super(OperationDisplay, self).__init__()
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description
