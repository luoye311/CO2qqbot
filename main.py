import requests
from flask import Flask, request
import json
import urllib.request
app = Flask(__name__)

def ping_server(host, port):
    """
    发送Ping请求并返回服务器响应

    Args:
        host (str): 服务器地址
        port (str): 服务器端口

    Returns:
        dict: 服务器响应的JSON数据
    """
    url = f'http://api.minetools.eu/ping/{host}/{port}'
    req = urllib.request.urlopen(url)
    response_data = req.read()
    response_json = json.loads(response_data.decode('utf-8'))
    a ='服务器名字:' + response_json['description'] + '\n服务器服务器在线人数:' + str(response_json['players']['online']) + '/' + str(response_json['players']['max']) + '\n服务器协议' + str(response_json['version']['protocol']) + '\nmotd:' + response_json['version']['name']
    return a

def ping_server1(host):
    """
    发送Ping请求并返回服务器响应

    Args:
        host (str): 服务器地址
        port (str): 服务器端口

    Returns:
        dict: 服务器响应的JSON数据
    """
    url = f'http://api.minetools.eu/ping/{host}'
    req = urllib.request.urlopen(url)
    response_data = req.read()
    response_json = json.loads(response_data.decode('utf-8'))
    a ='服务器名字:' + response_json['description'] + '\n服务器服务器在线人数:' + str(response_json['players']['online']) + '/' + str(response_json['players']['max']) + '\n服务器协议' + str(response_json['version']['protocol']) + '\nmotd:' + response_json['version']['name']
    return a

def query_server_info(host, port):
    """
    查询服务器信息并返回结果

    Args:
        host (str): 服务器地址
        port (str): 服务器端口

    Returns:
        str: 服务器信息字符串
    """
    try:
        ping_result = ping_server(host, port)
        if 'description' not in ping_result:
            messagecf = '查询失败服务器可能未开启'
        else:
            messagecf = '{0}\n服务器标签：{1}\n服务器在线人数：{2}\n服务器名字：{3}\n服务器协议：{4}'.format(a2, ping_result['description'], str(ping_result['players']['online']), ping_result['version']['name'], str(ping_result['version']['protocol']))
        return messagecf
    except Exception as e:
        # 异常处理的具体代码
        pass

@app.route('/', methods=["POST"])
def post_data():
    print(request.get_json())
    Xingxi = request.get_json().get('raw_message')
    if request.get_json().get('raw_message') == '查服' and request.get_json().get('message_type') == 'private':            # 如果是私聊信息状态码
        # 获取需要的消息
        QQ_name = request.get_json().get('sender').get('nickname')        # 发送者人的昵称叫啥
        QQ_id = request.get_json().get('sender').get('user_id')           # 发送者的QQ号
        Xingxi_text = request.get_json().get('raw_message')
        print(request.get_json().get('raw_message'))
        # 发的什么东西
        if len(Xingxi_text) == 2:
            host = "see.0mc.me"
            port = "20001"
            requests.get("http://127.0.0.1:5900/send_private_msg?user_id={0}&message={1}".format(QQ_id, ping_server(host, port)))
        elif Xingxi_text.find(" "):
            host = Xingxi_text[2:Xingxi_text.find(" ")]
            port = Xingxi_text[Xingxi_text.find(" ") + 1:]
            requests.get("http://127.0.0.1:5900/send_private_msg?user_id={0}&message={1}".format(QQ_id, ping_server(host, port)))
        else:
            host = Xingxi_text[3:]
            requests.get("http://127.0.0.1:5900/send_private_msg?user_id={0}&message={1}".format(QQ_id, ping_server1(host)))
    elif Xingxi[0] == "查" and request.get_json().get('message_type') == 'group' and Xingxi[1] == "服":
        Qun_id = request.get_json().get('group_id')
        Xingxi_text = request.get_json().get('raw_message')
        if len(Xingxi_text) == 2:
            host = "see.0mc.me"
            port = "20001"
            requests.get("http://127.0.0.1:5900/send_group_msg?group_id={0}&message={1}".format(Qun_id, ping_server(host, port)))
        else:
            host1 = Xingxi_text[3:]
            if host1.find(" ") >= 4:
                port = host1[host1.find(" ")+1:]
                host = host1[:host1.find(" ")]
                print(port)
                print(host)
                requests.get("http://127.0.0.1:5900/send_group_msg?group_id={0}&message={1}".format(Qun_id,ping_server(host, port)))
            else:
                host = host1
                print(host)
                requests.get("http://127.0.0.1:5900/send_group_msg?group_id={0}&message={1}".format(Qun_id,ping_server1(host)))




    return 'OK'  

app.run(debug=True, host='127.0.0.1', port=8090)  

