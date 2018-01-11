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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.database_accounts_operations import DatabaseAccountsOperations
from .operations.operations import Operations
from .operations.database_operations import DatabaseOperations
from .operations.collection_operations import CollectionOperations
from .operations.collection_region_operations import CollectionRegionOperations
from .operations.database_account_region_operations import DatabaseAccountRegionOperations
from . import models


class CosmosDBConfiguration(AzureConfiguration):
    """Configuration for CosmosDB
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(CosmosDBConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-cosmosdb/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class CosmosDB(object):
    """Azure Cosmos DB Database Service Resource Provider REST API

    :ivar config: Configuration for client.
    :vartype config: CosmosDBConfiguration

    :ivar database_accounts: DatabaseAccounts operations
    :vartype database_accounts: azure.mgmt.cosmosdb.operations.DatabaseAccountsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.cosmosdb.operations.Operations
    :ivar database: Database operations
    :vartype database: azure.mgmt.cosmosdb.operations.DatabaseOperations
    :ivar collection: Collection operations
    :vartype collection: azure.mgmt.cosmosdb.operations.CollectionOperations
    :ivar collection_region: CollectionRegion operations
    :vartype collection_region: azure.mgmt.cosmosdb.operations.CollectionRegionOperations
    :ivar database_account_region: DatabaseAccountRegion operations
    :vartype database_account_region: azure.mgmt.cosmosdb.operations.DatabaseAccountRegionOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = CosmosDBConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-04-08'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.database_accounts = DatabaseAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.database = DatabaseOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.collection = CollectionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.collection_region = CollectionRegionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.database_account_region = DatabaseAccountRegionOperations(
            self._client, self.config, self._serialize, self._deserialize)
