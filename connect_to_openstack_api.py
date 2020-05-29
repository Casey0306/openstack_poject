import requests
import json
from config import Config

env_var = Config()


class Openstackapi:

    project_name = ""
    ip_api = ""
    token = ""
    status_code = 0

    def __init__(self, project_name=env_var.OPENSTACK_PROJECT_NAME, ip_api=env_var.OPENSTACK_API_IP):
        self.project_name = project_name
        self.ip_api = ip_api
        self.token = ""
        self.status_code = 0

    def auth_keystone(self, username, password):
        url = "http://" + self.ip_api + "/identity/v3/auth/tokens"
        headers = {'Content-Type': 'application/json'}
        payload_dict = {"auth": {
                                "identity": {
                                    "methods": ["password"],
                                    "password": {
                                            "user": {
                                                "name": username,
                                                "domain": {"id": "default"},
                                                "password": password
                                            }
                                    }
                                },
                                "scope": {
                                    "project": {
                                        "name": self.project_name,
                                        "domain": {"id": "default"}
                                    }
                                }
                             }
                        }

        payload = json.dumps(payload_dict)
        response = requests.request("POST", url, headers=headers, data=payload)
        self.status_code = response.status_code
        try:
            self.token = response.headers['X-Subject-Token']
        except Exception:
            return {"Error": "No auth there is no token"}

        return self.token

    def check_token_status(self):
        url = "http://" + self.ip_api + "/identity/v3/projects"
        headers = {
                    'Content-Type': 'application/json',
                    'X-Auth-Token': self.token
                  }
        response = requests.request("HEAD", url, headers=headers)
        if response.status_code == 200:
            return 1
        else:
            return 0

    def get_images(self):
        dict_images = {}
        list_images = []
        url = "http://" + self.ip_api + "/image/v2/images"
        headers = {
                      'Content-Type': 'application/json',
                      'X-Auth-Token': self.token
                  }
        response = requests.request("GET", url, headers=headers)
        self.status_code = response.status_code
        try:
            for images_list in json.loads(response.text.encode('utf8'))["images"]:
                list_images.append({"name": images_list["name"], "id": images_list["id"]})
            dict_images["images"] = list_images
        except Exception:
            return {"error": "no available to take images"}

        return dict_images

    def get_flavors(self):
        dict_flavors = {}
        list_flavors = []
        url = "http://" + self.ip_api + "/compute/v2.1/flavors"
        headers = {
                      'Content-Type': 'application/json',
                      'X-Auth-Token': self.token
                  }
        response = requests.request("GET", url, headers=headers)
        self.status_code = response.status_code
        try:
            for flavors_list in json.loads(response.text.encode('utf8'))["flavors"]:
                list_flavors.append({"id": flavors_list["id"], "name": flavors_list["name"],
                                     "href": flavors_list["links"][1]["href"]})
            dict_flavors["flavors"] = list_flavors
        except Exception:
            return {"Error": "Exception format error"}

        return dict_flavors

    def get_networks(self):
        dict_networks = {}
        list_networks = []
        url = "http://" + self.ip_api + ":9696/v2.0/networks.json"
        headers = {
                       'Content-Type': 'application/json',
                       'X-Auth-Token': self.token
                   }
        response = requests.request("GET", url, headers=headers)
        self.status_code = response.status_code
        try:
            for networks_list in json.loads(response.text.encode('utf8'))["networks"]:
                list_networks.append({"id": networks_list["id"], "name": networks_list["name"],
                                      "status": networks_list["status"]})
            dict_networks["networks"] = list_networks
        except Exception:
            return {"Error": "Exception format error"}

        return dict_networks

    def get_vms(self):
        dict_vms = {}
        list_vms = []
        url = "http://" + self.ip_api + "/compute/v2.1/servers/detail"
        headers = {
                      'Content-Type': 'application/json',
                      'X-Auth-Token': self.token
                  }
        response = requests.request("GET", url, headers=headers)
        self.status_code = response.status_code
        try:
            for vms_list in json.loads(response.text.encode('utf8'))["servers"]:
                list_vms.append({"id": vms_list["id"], "name": vms_list["name"], "flavor": vms_list["flavor"],
                                 "status": vms_list["status"], "addresses": vms_list["addresses"]})
            dict_vms["vms"] = list_vms
        except Exception:
            return {"Error": "Exception format error"}

        return dict_vms

    def get_vm(self, vm_id):
        dict_vm = {}
        url = "http://" + self.ip_api + "/compute/v2.1/servers/" + vm_id
        headers = {
            'Content-Type': 'application/json',
            'X-Auth-Token': self.token
        }
        response = requests.request("GET", url, headers=headers)
        self.status_code = response.status_code
        try:
            server = json.loads(response.text.encode('utf8'))["server"]
            dict_vm["id"] = server["id"]
            dict_vm["name"] = server["name"]
            dict_vm["status"] = server["status"]
            dict_vm["addresses"] = server["addresses"]
            dict_vm["flavor"] = server["flavor"]

        except Exception:
            return {"Error": "Exception format error"}

        return dict_vm

    def create_vm(self, vm_name, image_id, flavor_href, networks_id_list):
        payload_dict = {
                          "server": {
                                      "name": vm_name,
                                      "imageRef": image_id,
                                      "flavorRef": flavor_href,
                                      "networks": networks_id_list
                                     }
                       }

        headers = {
                      'Content-Type': 'application/json',
                      'X-Auth-Token': self.token
                   }

        url = "http://" + self.ip_api + "/compute/v2.1/servers"
        payload = json.dumps(payload_dict)
        response = requests.request("POST", url, headers=headers, data=payload)
        self.status_code = response.status_code

        return response.status_code
