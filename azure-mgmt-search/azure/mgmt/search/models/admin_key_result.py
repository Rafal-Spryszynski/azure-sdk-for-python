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


class AdminKeyResult(Model):
    """Response containing the primary and secondary admin API keys for a given
    Azure Search service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar primary_key: The primary admin API key of the Search service.
    :vartype primary_key: str
    :ivar secondary_key: The secondary admin API key of the Search service.
    :vartype secondary_key: str
    """

    _validation = {
        'primary_key': {'readonly': True},
        'secondary_key': {'readonly': True},
    }

    _attribute_map = {
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
    }

    def __init__(self):
        super(AdminKeyResult, self).__init__()
        self.primary_key = None
        self.secondary_key = None
