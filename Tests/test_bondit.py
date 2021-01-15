import json
import requests
from Tests.BaseClass import getLogger
from pageObJ.PayLoadB import Payloadb

'''
The tests listed below refer to the site : 
http://external-universe-service-dev.us-east-1.elasticbeanstalk.com/api/v2/ui/#/
'''


class Test_bond:

    def test_universe(self, param, external_universe_id):
        response = requests.post(param["BaseURI"] + param["universe_Resource"], json=Payloadb(external_universe_id),
                                 auth=(param["username"], param["password"]))
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["status"] == "SUCCESS"
        print(json.dumps(response_json, indent=2))
        print(response_json["status"])
        universe_id = response_json["result"]["universe_id"]
        print(universe_id)

    def test_universe_batch(self, param):
        log = getLogger()
        response = requests.post(param["BaseURI"] + param["universe_batch"], json=Payloadb("14020"),
                                 auth=(param["username"], param["password"]))
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["status"] == "SUCCESS"
        print(json.dumps(response_json, indent=2))
        job_id = response_json["result"]["job_id"]
        log.info("job id=" + job_id)
        print(job_id)

    def test_get(self, param, job_id):
        log = getLogger()
        response = requests.get(param["BaseURI"] + "/request/" + job_id, auth=(param["username"], param["password"]))
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["status"] == "SUCCESS"
        print(json.dumps(response_json, indent=2))
        print(response_json["result"]["universe_id"])
        log.info(json.dumps(response_json, indent=2))
        log.info(response_json["result"]["universe_id"])

    def test_health_check(self, param):
        log = getLogger()
        response = requests.get(param["BaseURI"] + "/health_check", auth=(param["username"], param["password"]))
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["status"] == "OK"
        print(json.dumps(response_json, indent=2))
        log.info(json.dumps(response_json, indent=2))
