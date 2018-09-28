import yaml
import openshift.config
import openshift.client
from openshift.dynamic import DynamicClient

openshift.config.load_incluster_config()

api_client = openshift.client.ApiClient()
dyn_client = DynamicClient(api_client)

v1_routes = dyn_client.resources.get(api_version='route.openshift.io/v1', kind='Route')

route_list = v1_routes.get(namespace='rest-project')

print("+++++++++++++++")
print(route_list)
print("+++++++++++++++")

for route in route_list.items:
    print(route.metadata.name)