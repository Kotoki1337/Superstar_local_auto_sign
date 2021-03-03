# =================配置区start===================

# 学习通账号密码,可添加多个账号
USER_INFOS = [
    {
        'username': '',
        'password': '',
        'schoolid': ''  # 学号登录才需要填写
    },
]

# 签到间隔时间设置,时分秒, 默认是每间隔5分钟执行一次
i_hours = 0
i_minutes = 0
i_seconds = 40

# 学习通账号cookies缓存文件路径
COOKIES_PATH = "./"
COOKIES_FILE_PATH = COOKIES_PATH + "cookies.json"

# activeid保存文件路径
ACTIVEID_PATH = "./"
ACTIVEID_FILE_PATH = ACTIVEID_PATH + "activeid.json"

# 拍照签到的图片文件
IMAGE_PATH = "./image/"

# 位置信息
latitude = "-2"
longitude = "-1"

# ip地址
clientip = "0.0.0.0"

# 状态码
STATUS_CODE_DICT = {
    1000: '登录成功',
    1001: '登录信息有误',
    1002: '拒绝访问',
    2000: '当前暂无签到任务',
    2001: '有任务且签到成功',
    4000: '未知错误'
}

# cqhttp请求地址
cqhttpAddress = "http://127.0.0.1:5700"
group_id = ""
access_token = ""

# Discord WEBHOOK请求地址
WEBHOOK_ADDRESS = ""

# =================配置区end===================
