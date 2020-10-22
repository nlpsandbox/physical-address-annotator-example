import connexion
import pandas as pd
import re
from flask import jsonify
from datetime import datetime
import pytz
import json
from flask import Response

from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.physical_address_annotation import PhysicalAddressAnnotation  # noqa: E501
from openapi_server import util


def physical_addresses_read_all(note=None):  # noqa: E501
    """Get all physical address annotations

    Returns the physical address annotations # noqa: E501

    :param note: 
    :type note: list | bytes

    :rtype: List[PhysicalAddressAnnotation]
    """
    failure = {
        "detail": "Unknown",
        "status": 400,
        "title": "Bad Request",
        "type": "about:blank"
    }

    # Pulled this list from
    # https://raw.githubusercontent.com/datasets/country-list/master/data.csv

    df = pd.read_csv("data/country_list.csv")
    countries = df['Name'].str.lower().unique().tolist()
    return_list = []
    tz_NY = pytz.timezone('Etc/Greenwich')
    currenttime = datetime.now(tz=tz_NY)
    # 2019-08-24T14:15:22Z
    formatted_time = currenttime.strftime("%Y-%m-%d %H:%M:%S%Z")
    if connexion.request.is_json:
        notes = [Note.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
        for note in notes:
            if (note._text is None):
                failure['detail'] = "A Note is missing the required text field"
                return Response(json.dumps(failure), status=400, mimetype='application/json')
                # return jsonify(failure)

            # Match on contry name list
            for country in countries:
                matches = re.finditer(country, note._text, re.IGNORECASE)
                for match in matches:
                    return_list.append({
                        'noteId': note._id,
                        'text': match[0],
                        'start': match.start(),
                        'length': len(match[0]),
                        'created_at': formatted_time,
                        'type': "Country"
                    })
            # Match on 5 digit ZIP code
            match = re.finditer(
                '\\b([0-9][0-9][0-9][1-9][1-9])\\b',
                note._text)
            for m in match:
                return_list.append({
                    'noteId': note._id,
                    'text': m[0],
                    'start': m.start(),
                    'length': len(m[0]),
                    'created_at': formatted_time,
                    'type': "Zip"
                })

    return jsonify(return_list)
