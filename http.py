# 文件创建时间 ：2018/10/21 15:17

import requests
__author__ = "碎心咒"


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text()



