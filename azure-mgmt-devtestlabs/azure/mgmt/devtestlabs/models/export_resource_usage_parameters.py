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


class ExportResourceUsageParameters(Model):
    """The parameters of the export operation.

    :param blob_storage_absolute_sas_uri: The blob storage absolute sas uri
     with write permission to the container which the usage data needs to be
     uploaded to.
    :type blob_storage_absolute_sas_uri: str
    :param usage_start_date: The start time of the usage. If not provided,
     usage will be reported since the beginning of data collection.
    :type usage_start_date: datetime
    """

    _attribute_map = {
        'blob_storage_absolute_sas_uri': {'key': 'blobStorageAbsoluteSasUri', 'type': 'str'},
        'usage_start_date': {'key': 'usageStartDate', 'type': 'iso-8601'},
    }

    def __init__(self, blob_storage_absolute_sas_uri=None, usage_start_date=None):
        super(ExportResourceUsageParameters, self).__init__()
        self.blob_storage_absolute_sas_uri = blob_storage_absolute_sas_uri
        self.usage_start_date = usage_start_date
