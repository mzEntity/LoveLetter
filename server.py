import socket
from config import Config
from common.communicate import MySocket

class Server:
    def __init__(self, player_count):
        self.player_count = player_count
        self.client_sock_dict = {}
        
    def accept_all(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind(Config().SERVER_ADDRESS)
        server_sock.listen(self.player_count)
        print("服务器已启动，等待客户端连接...")

        for i in range(self.player_count):
            client_socket, client_address = server_sock.accept()
            sock = MySocket(client_socket)
            self.client_sock_dict[i] = sock
            print(f"client id:{i} 已连接")
            
        print("已全部连接")


if __name__ == "__main__":
    s = Server(3)
    s.accept_all()
    for k, sock in s.client_sock_dict.items():
        sock.sendDict({
            "id": k
        })
    turn = 0
    while True:
        if not s.client_sock_dict:
            break
        cur_idx = turn % s.player_count
        if cur_idx not in s.client_sock_dict:
            turn += 1
            continue
        s.client_sock_dict[cur_idx].sendDict({
            "type": "invite"
        })
        re = s.client_sock_dict[cur_idx].recvDict()
        print(re)
        if re["msg"] == "quit":
            for id, sock in s.client_sock_dict.items():
                sock.sendDict({
                    "type": "msg",
                    "msg": f"bye bye player {cur_idx}."
                })
            del s.client_sock_dict[cur_idx]
        else:
            for id, sock in s.client_sock_dict.items():
                sock.sendDict({
                    "type": "msg",
                    "msg": f"player{cur_idx} says: {re['msg']}"
                })
        turn += 1
                
            
        
        
        