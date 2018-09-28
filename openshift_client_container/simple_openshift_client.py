import openshift.client
import openshift.config

openshift.config.load_incluster_config()

api_client = openshift.client.ApiClient()
oapi_client = openshift.client.OapiApi(api_client)

namespace = "rest-project"
route_list = oapi_client.list_namespaced_route(namespace)