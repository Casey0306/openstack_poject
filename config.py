import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENSTACK_API_IP = os.getenv('OPENSTACK_API_IP')
    OPENSTACK_PROJECT_NAME = os.getenv('OPENSTACK_PROJECT_NAME')
