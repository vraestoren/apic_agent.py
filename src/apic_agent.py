from requests import Session

class ApicAgent:
	def __init__(self, user_agent: str) -> None:
		self.api = "https://api.apicagent.com"
		self.session = Session()
		self.session.headers = {
			"user-agent": user_agent
		}
		self.ua_info = self.session.get(f"{self.api}?ua={user_agent}").json()
		
	def get_user_agent_info(self) -> dict:
		return self.ua_info
	
	def get_user_agent_browser(self) -> str:
		return self.ua_info["browser_family"]
	
	def get_user_agent_client(self) -> str:
		return self.ua_info["client"]
	
	def get_user_agent_device(self) -> str:
		return self.ua_info["device"]
	
	def get_user_agent_os(self) -> str:
		return self.ua_info["os"]
