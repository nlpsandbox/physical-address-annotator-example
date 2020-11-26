# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.note import Note
from openapi_server import util

from openapi_server.models.note import Note  # noqa: E501

class TextPhysicalAddressAnnotationRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, note=None):  # noqa: E501
        """TextPhysicalAddressAnnotationRequest - a model defined in OpenAPI

        :param note: The note of this TextPhysicalAddressAnnotationRequest.  # noqa: E501
        :type note: Note
        """
        self.openapi_types = {
            'note': Note
        }

        self.attribute_map = {
            'note': 'note'
        }

        self._note = note

    @classmethod
    def from_dict(cls, dikt) -> 'TextPhysicalAddressAnnotationRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextPhysicalAddressAnnotationRequest of this TextPhysicalAddressAnnotationRequest.  # noqa: E501
        :rtype: TextPhysicalAddressAnnotationRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def note(self):
        """Gets the note of this TextPhysicalAddressAnnotationRequest.


        :return: The note of this TextPhysicalAddressAnnotationRequest.
        :rtype: Note
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this TextPhysicalAddressAnnotationRequest.


        :param note: The note of this TextPhysicalAddressAnnotationRequest.
        :type note: Note
        """

        self._note = note
