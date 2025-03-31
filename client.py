import socket
from config import Config
from common.communicate import MySocket

class Client:
    def __init__(self):
        pass
    
    def connect(self):
        """启动客户端"""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect(Config().SERVER_ADDRESS)
            self.sock = MySocket(client_socket)
        except Exception as e:
            print(f"连接服务器时出错: {e}")
            
        
        

if __name__ == "__main__":
    c = Client()
    c.connect()
    re = c.sock.recvDict()
    c.id = re["id"]
    print(f"我是{c.id}号玩家！")
    
    while True:
        d = c.sock.recvDict()
        if d["type"] == "invite":
            msg = input(">")
            c.sock.sendDict({
                "msg": msg
            })
            if msg == "quit":
                break
        else:
            print(d['msg'])