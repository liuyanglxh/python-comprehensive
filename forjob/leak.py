import requests

params = {
	"command":"objgraph.show_backrefs(objgraph.by_type('OBJ')[0], max_depth = 10, filename = 'obj.dot')"
}
url = 'http://10.0.20.37:9097/api/recommend-engine/memory/show'

requests.get(url, params)