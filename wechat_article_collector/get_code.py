import  requests
def unlock(antiurl, oldcookies):
    retries = 0
    while retries < 3:
        r = requests.ohRequests()
        tc = int(round(time.time() * 1000))
        captcha = r.get('http://weixin.sogou.com/antispider/util/seccode.php?tc={}'.format(tc), cookies=oldcookies)

        with open('captcha.jpg', 'wb') as file:
            file.write(captcha.content)

        c = input("请输入captcha.jpg中的验证码:")

        thank_url = 'http://weixin.sogou.com/antispider/thank.php'
        formdata = {
            'c': c,
            'r': '%2F' + antiurl,
            'v': 5
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://weixin.sogou.com/antispider/?from=%2f' + antiurl
        }

        resp = r.post(thank_url, data=formdata, headers=headers, cookies=oldcookies)

        resp = json.loads(resp.text)

        if resp.get('code') != 0:
            print("解锁失败。重试次数:{0:d}".format(3 - retries))
            retries += 1
            continue

        oldcookies['SNUID'] = resp.get('id')
        oldcookies['SUV'] = '00D80B85458CAE4B5B299A407EA3A580'
        # print ("更新Cookies。", oldcookies)

        return oldcookies