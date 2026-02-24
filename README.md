# apic_agent.py
Web-API for [apicagent.com](https://www.apicagent.com) website to detect browser, OS, device from user agent string

## Example
```python
from apic_agent import ApicAgent

apic_agent = ApicAgent(user_agent="")
user_agent_info = apic_agent.get_user_agent_info()
print(user_agent_info)
```
