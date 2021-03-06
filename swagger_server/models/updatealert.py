# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.action import Action  # noqa: F401,E501
from swagger_server.models.meta_data import MetaData  # noqa: F401,E501
from swagger_server import util


class Updatealert(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, info: str=None, is_ack: bool=None, is_read: bool=None, is_discarded: bool=None, is_muted: bool=None, meta_data: MetaData=None, action: Action=None):  # noqa: E501
        """Updatealert - a model defined in Swagger

        :param id: The id of this Updatealert.  # noqa: E501
        :type id: str
        :param info: The info of this Updatealert.  # noqa: E501
        :type info: str
        :param is_ack: The is_ack of this Updatealert.  # noqa: E501
        :type is_ack: bool
        :param is_read: The is_read of this Updatealert.  # noqa: E501
        :type is_read: bool
        :param is_discarded: The is_discarded of this Updatealert.  # noqa: E501
        :type is_discarded: bool
        :param is_muted: The is_muted of this Updatealert.  # noqa: E501
        :type is_muted: bool
        :param meta_data: The meta_data of this Updatealert.  # noqa: E501
        :type meta_data: MetaData
        :param action: The action of this Updatealert.  # noqa: E501
        :type action: Action
        """
        self.swagger_types = {
            'id': str,
            'info': str,
            'is_ack': bool,
            'is_read': bool,
            'is_discarded': bool,
            'is_muted': bool,
            'meta_data': MetaData,
            'action': Action
        }

        self.attribute_map = {
            'id': 'id',
            'info': 'info',
            'is_ack': 'isAck',
            'is_read': 'isRead',
            'is_discarded': 'isDiscarded',
            'is_muted': 'isMuted',
            'meta_data': 'metaData',
            'action': 'action'
        }
        self._id = id
        self._info = info
        self._is_ack = is_ack
        self._is_read = is_read
        self._is_discarded = is_discarded
        self._is_muted = is_muted
        self._meta_data = meta_data
        self._action = action

    @classmethod
    def from_dict(cls, dikt) -> 'Updatealert':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The updatealert of this Updatealert.  # noqa: E501
        :rtype: Updatealert
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Updatealert.

        id of the alert  # noqa: E501

        :return: The id of this Updatealert.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Updatealert.

        id of the alert  # noqa: E501

        :param id: The id of this Updatealert.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def info(self) -> str:
        """Gets the info of this Updatealert.

        info of the alert  # noqa: E501

        :return: The info of this Updatealert.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info: str):
        """Sets the info of this Updatealert.

        info of the alert  # noqa: E501

        :param info: The info of this Updatealert.
        :type info: str
        """

        self._info = info

    @property
    def is_ack(self) -> bool:
        """Gets the is_ack of this Updatealert.

        acknowlegement  # noqa: E501

        :return: The is_ack of this Updatealert.
        :rtype: bool
        """
        return self._is_ack

    @is_ack.setter
    def is_ack(self, is_ack: bool):
        """Sets the is_ack of this Updatealert.

        acknowlegement  # noqa: E501

        :param is_ack: The is_ack of this Updatealert.
        :type is_ack: bool
        """

        self._is_ack = is_ack

    @property
    def is_read(self) -> bool:
        """Gets the is_read of this Updatealert.

        readed or not  # noqa: E501

        :return: The is_read of this Updatealert.
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read: bool):
        """Sets the is_read of this Updatealert.

        readed or not  # noqa: E501

        :param is_read: The is_read of this Updatealert.
        :type is_read: bool
        """

        self._is_read = is_read

    @property
    def is_discarded(self) -> bool:
        """Gets the is_discarded of this Updatealert.

        is it discarded or not   # noqa: E501

        :return: The is_discarded of this Updatealert.
        :rtype: bool
        """
        return self._is_discarded

    @is_discarded.setter
    def is_discarded(self, is_discarded: bool):
        """Sets the is_discarded of this Updatealert.

        is it discarded or not   # noqa: E501

        :param is_discarded: The is_discarded of this Updatealert.
        :type is_discarded: bool
        """

        self._is_discarded = is_discarded

    @property
    def is_muted(self) -> bool:
        """Gets the is_muted of this Updatealert.

        whether muted or not   # noqa: E501

        :return: The is_muted of this Updatealert.
        :rtype: bool
        """
        return self._is_muted

    @is_muted.setter
    def is_muted(self, is_muted: bool):
        """Sets the is_muted of this Updatealert.

        whether muted or not   # noqa: E501

        :param is_muted: The is_muted of this Updatealert.
        :type is_muted: bool
        """

        self._is_muted = is_muted

    @property
    def meta_data(self) -> MetaData:
        """Gets the meta_data of this Updatealert.


        :return: The meta_data of this Updatealert.
        :rtype: MetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data: MetaData):
        """Sets the meta_data of this Updatealert.


        :param meta_data: The meta_data of this Updatealert.
        :type meta_data: MetaData
        """

        self._meta_data = meta_data

    @property
    def action(self) -> Action:
        """Gets the action of this Updatealert.


        :return: The action of this Updatealert.
        :rtype: Action
        """
        return self._action

    @action.setter
    def action(self, action: Action):
        """Sets the action of this Updatealert.


        :param action: The action of this Updatealert.
        :type action: Action
        """

        self._action = action
