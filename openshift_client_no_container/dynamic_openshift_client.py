import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient

k8s_client = config.new_client_from_config()
dyn_client = DynamicClient(k8s_client)

v1_routes = dyn_client.resources.get(api_version='route.openshift.io/v1', kind='Route')

route = """
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: redhat-route
spec:
  host: basic-rest-client.rest-project.svc
  to:
    kind: Service
    name: basic-rest-client
"""

route_data = yaml.load(route)
resp = v1_routes.create(body=route_data, namespace='rest-project')

# resp is a ResourceInstance object
print(resp.metadata)