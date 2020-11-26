# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_physical_address_annotation_request import TextPhysicalAddressAnnotationRequest  # noqa: E501
from openapi_server.models.text_physical_address_annotations import TextPhysicalAddressAnnotations  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTextPhysicalAddressAnnotationController(BaseTestCase):
    """TextPhysicalAddressAnnotationController integration test stubs"""

    def test_create_text_physical_address_annotations(self):
        """Test case for create_text_physical_address_annotations

        Annotate physical addresses in a clinical note
        """
        text_physical_address_annotation_request = {
  "note" : {
    "noteType" : "loinc:LP29684-5",
    "patientId" : "507f1f77bcf86cd799439011",
    "text" : "On 12/26/2020, Ms. Chloe Price met with Dr. Prescott."
  }
}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/textPhysicalAddressAnnotations',
            method='POST',
            headers=headers,
            data=json.dumps(text_physical_address_annotation_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
