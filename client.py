import socket
import threading

def receive_messages(client_socket):
    """接收服务端消息并打印"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("与服务器断开连接")
                break
            print(message)
        except Exception as e:
            print(f"接收消息时出错: {e}")
            break

def start_client():
    """启动客户端"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)  # 服务端地址
    client_name = input("请输入你的名字: ")

    try:
        client_socket.connect(server_address)
        client_socket.sendall(client_name.encode('utf-8'))  # 发送客户端名称到服务端

        # 启动线程接收消息
        threading.Thread(target=receive_messages, args=(client_socket,)).start()

        # 主线程用于发送消息
        while True:
            message = input("请输入你要出的牌（或输入 'exit' 退出）: ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode('utf-8'))
    except Exception as e:
        print(f"连接服务器时出错: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()