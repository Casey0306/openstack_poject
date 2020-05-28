from connect_to_openstack_api import Openstackapi
from config import Config


env_var = Config()

openstack = Openstackapi()

token = openstack.auth_keystone("admin", "P@sswordOpenSt@ck")
print("token number:" + openstack.token)
if openstack.token:
    print("Sam duirak")
print(openstack.get_images())
print(openstack.get_flavors())
print(openstack.get_networks())
print(openstack.get_vms())
print(openstack.check_token_status())
if openstack.check_token_status():
    print("good")
else:
    print("fuck")
#openstack.create_vm("Super", "cd052dcb-28f2-463d-9c87-812e59017aac", "http://31.41.155.230/compute/flavors/1",
#                    [{"uuid": "83831421-a25c-4032-b9d0-2ccc08e1f4c6"}, {"uuid": "bd2e0b09-0a5e-4931-b294-522eee99e605"}])





