# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MetaData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, source: str=None, channel_name: str=None):  # noqa: E501
        """MetaData - a model defined in Swagger

        :param source: The source of this MetaData.  # noqa: E501
        :type source: str
        :param channel_name: The channel_name of this MetaData.  # noqa: E501
        :type channel_name: str
        """
        self.swagger_types = {
            'source': str,
            'channel_name': str
        }

        self.attribute_map = {
            'source': 'source',
            'channel_name': 'channelName'
        }
        self._source = source
        self._channel_name = channel_name

    @classmethod
    def from_dict(cls, dikt) -> 'MetaData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The metaData of this MetaData.  # noqa: E501
        :rtype: MetaData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source(self) -> str:
        """Gets the source of this MetaData.

        dscribes where it comes from   # noqa: E501

        :return: The source of this MetaData.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this MetaData.

        dscribes where it comes from   # noqa: E501

        :param source: The source of this MetaData.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def channel_name(self) -> str:
        """Gets the channel_name of this MetaData.

        channel where it is came from  # noqa: E501

        :return: The channel_name of this MetaData.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name: str):
        """Sets the channel_name of this MetaData.

        channel where it is came from  # noqa: E501

        :param channel_name: The channel_name of this MetaData.
        :type channel_name: str
        """
        if channel_name is None:
            raise ValueError("Invalid value for `channel_name`, must not be `None`")  # noqa: E501

        self._channel_name = channel_name