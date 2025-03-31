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
            re = self.sock.recvDict()
            self.id = re["id"]
            print(f"我是{self.id}号玩家！")
        except Exception as e:
            print(f"连接服务器时出错: {e}")
            
    def send(self, msg):
        self.sock.sendDict({
            "msg": msg
        })
        

if __name__ == "__main__":
    c = Client()
    c.connect()
    while True:
        d = c.sock.recvDict()
        if d["type"] == "invite":
            msg = input(">")
            c.send(msg)
            if msg == "quit":
                break
        else:
            print(d['msg'])