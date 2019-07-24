import requests
from requests.packages import urllib3
from fake_useragent import UserAgent
import datetime,time


timestamp=time.time()
timestamp=str(timestamp).replace('.','')[:-3]
print(timestamp)
# view_url ='//bbs.pcauto.com.cn/intf/topic/counter.ajax?tid=17997663&fid=25445&agent=0&currentUrl=&currentReferer=%s&'%
view_url='http://bbs.pcauto.com.cn/intf/topic/counter.ajax?tid=17997663&fid=25445&agent=0&uid=33902507&currentUrl=&currentReferer=1560742677693&'

ua = UserAgent()
headers={"User-Agent":ua.random}
urllib3.disable_warnings()
res = requests.get(url=view_url,headers=headers,verify=False,timeout=30)
print(res.status_code)

