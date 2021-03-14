from urllib import request,parse
import json,sys,time
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
def printe(text,ode="\n",sde="\r"):
    sys.stdout.write(ode + "" * 60 + sde)
    sys.stdout.flush()
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
def inpute(text,ode="\n",sde="\r"):
    printe(text,ode,sde)
    a = input("")
    return a
while True:
    keyword = inpute("请输入需要翻译的内容(直接按回车退出)：","\n")
    if keyword == '':
        printe("感谢您使用本款软件，下次再见！")
        printe("网易有道翻译 提供翻译技术")
        sys.exit(0)
    formdata = {
        "i":keyword,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"16129446513132",
        "sign":"ba74294484fdfa7c459c5a8f9f5a4893",
        "lts":"1612944651313",
        "bv":"db6b9693e24ea152843dd96fcd289f0f",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTlME",
    }
    data = parse.urlencode(formdata).encode("utf-8")
    request1 = request.Request(url,data = data)
    target = request.urlopen(request1).read().decode("utf-8")
    result = json.loads(target)
    result = result['translateResult']
    result = result.pop(0)
    result = result.pop(0)
    printe(result['tgt'],"","")
