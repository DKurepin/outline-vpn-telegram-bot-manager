import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../utils'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../pb2_module/proxy'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../pb2_module/country'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../pb2_module/key'))
from proxy_pb2_grpc import *
from country_pb2_grpc import *
from key_pb2_grpc import *
from errors import *

from exceptions.server_error_exception import *
from google.protobuf.empty_pb2 import Empty


class VPNService:

    def __init__(self, server_host):
        channel = grpc.insecure_channel(server_host)
        self.proxy_stub = ProxyServiceStub(channel)
        self.country_stub = CountryServiceStub(channel)
        self.key_stub = KeyServiceStub(channel)

    def get_countries(self) -> list:
        empty_request = Empty()
        response = self.country_stub.GetAllCountries(empty_request)
        if response is None:
            raise ServerErrorException(errors['server_error']())

        countries = [country for country in response.countries]
        return countries

    def get_country_by_name(self, country_name):
        c_name = country__pb2.CountryName(name=country_name)
        response = self.country_stub.GetCountryByName(c_name)
        if response is None:
            raise ServerErrorException(errors['server_error']())
        return response

    def get_key(self, subscription_id):
        request = key__pb2.KeyRequest(subscription_id=subscription_id)
        response = self.key_stub.GetKey(request)

        if response is None:
            raise ServerErrorException(errors['server_error']())

        key = response.data.decode('utf-8')
        return key
