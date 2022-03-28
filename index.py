import requests 
from bs4 import BeautifulSoup
import time
import re
import rsa
import base64
import hashlib
import os
import sys

sys.path.append('.')
requests.packages.urllib3.disable_warnings()
try:
    from pusher import pusher
except:
    pass
from urllib import parse

result = '🏆52破解签到姬🏆\n'

cookie = os.environ.get("htVC_2132_seccodecStNq=8813344.b09346254724cd636c; htVC_2132_connect_is_bind=0; htVC_2132_nofavfid=1; __gads=ID=6ea5506af6f6c431-22373c5baed000f5:T=1645172894:RT=1645172894:S=ALNI_MacN_vEhwIw4hYaMN6L8IZPKH5uCA; htVC_2132_st_t=0%7C1645222873%7C2e9ecc93475a56096ca450084893618b; htVC_2132_seccodecSS0L=4709607.aff352eb37265a4aa9; htVC_2132_seccodecSY70=3121770.f0065ab0123c7bf246; KF4=MDwtBD; htVC_2132_smile=1D1; htVC_2132_lastvisit=1647935912; Hm_lvt_46d556462595ed05e05f009cdafff31a=1647654212; htVC_2132_seccodecSu54=6408075.6a212de23a0cdf9f11; htVC_2132_seccodecS=6408121.2c1d2132df03ede83b; htVC_2132_lip=218.13.75.60%2C1648428391; htVC_2132_sid=0; htVC_2132_noticonf=1482601D1D3_3_1; htVC_2132_ttask=1482601%7C20220328; htVC_2132_st_p=1482601%7C1648428936%7C3759881d0fc58072ce7684a770aab971; htVC_2132_visitedfid=2D16D13D59; htVC_2132_viewid=tid_1608278; htVC_2132_secqaaqS0=6411220.847b92b35515debaf4; htVC_2132_ulastactivity=1648457907%7C0; htVC_2132_lastact=1648457907%09home.php%09spacecp; htVC_2132_checkpm=1; htVC_2132_lastcheckfeed=1482601%7C1648457907; htVC_2132_checkfollow=1; BAIDU_SSP_lcr=https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd=%E5%90%BE%E7%88%B1%E7%A0%B4%E8%A7%A3&rn=&fenlei=256&oq=&rsv_pq=c54933b40000b8c4&rsv_t=7fc6CqZV67wE3bxPElVEqCuU%2BVo7qBGh8PX9HloYr3nrC0ga6Ryl8K6qOZM&rqlang=cn&rsv_enter=1&rsv_btype=i&prefixsug=wuai&rsp=0&rsv_dl=is_0&inputT=2025; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1648457909")
TGBOTAPI = os.environ.get("TGBOTAPI")
TGID = os.environ.get("TGID")

def pushtg(data):
    global TGBOTAPI
    global TGID
    requests.post(
        'https://api.telegram.org/bot'+TGBOTAPI+'/sendMessage?chat_id='+TGID+'&text='+data)

# 【BOTAPI】格式为123456:abcdefghi
# 【TGID】格式为123456（人）或者-100123456（群组/频道）

def main():
    global result
    headers={
        'Cookie': cookie,
        'ContentType':'text/html;charset=gbk'
    }
    requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2',headers=headers)
    fa=requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=draw&id=2',headers=headers)
    fb=BeautifulSoup(fa.text,'html.parser')         
    fc=fb.find('div',id='messagetext').find('p').text
    print("🏆52破解签到姬🏆\n")
    print("返回内容")
    print(fc)
    if  "您需要先登录才能继续本操作"  in fc:
        result += "Cookie失效"
    elif "恭喜"  in fc:
        result += "签到成功"
    elif "不是进行中的任务"  in fc:
        result += "不是进行中的任务"
    else:
        result += "签到成功失败"
    
    pushtg(result)
    
    
def main_handler(event, context):
    main()


if __name__ == '__main__':
    main()
