import requests


class MyHttpUtil:
	def __init__(self, x_dm_authorization: str):
		self.x_dm_authorization = x_dm_authorization

	def get(self, url: str, params: dict, handle_result):
		header = {
			'x-dm-authorization': self.x_dm_authorization
		}
		resp = requests.get(url=url, params=params, headers=header)
		js = resp.json()
		handle_result(js)


if __name__ == '__main__':
	pass
