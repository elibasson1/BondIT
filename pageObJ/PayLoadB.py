def Payloadb(external_universe_id):
    payload_data = {
        "external_universe_id": external_universe_id,
        "universe_name": "A Universe",
        "instruments": [
            {
                "idn_type": "isin",
                "idn_val": "AU3CB0122448"
            }
        ]
    }

    return payload_data


def head_data():
    head = {
        "content-type": "application/json"
    }

    return head
