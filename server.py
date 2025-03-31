import socket
import threading

# 存储所有客户端连接
clients = {}

def broadcast_message(sender, message):
    """广播消息给除发送者外的所有客户端"""
    for client_name, client_socket in clients.items():
        if client_name != sender:
            try:
                client_socket.sendall(message.encode('utf-8'))
            except:
                # 如果发送失败，可能是客户端断开连接
                print(f"无法发送消息给 {client_name}")
                del clients[client_name]
                client_socket.close()

def handle_client(client_socket, client_name):
    """处理单个客户端的逻辑"""
    try:
        while True:
            # 接收客户端消息
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"{client_name} 断开连接")
                del clients[client_name]
                break

            # 广播消息给其他客户端
            print(f"{client_name} 出牌: {message}")
            broadcast_message(client_name, f"{client_name} 出牌: {message}")
    except Exception as e:
        print(f"{client_name} 出现错误: {e}")
    finally:
        # 客户端断开连接时清理资源
        if client_name in clients:
            del clients[client_name]
        client_socket.close()

def start_server():
    """启动服务端"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)
    print("服务器已启动，等待客户端连接...")

    while True:
        client_socket, client_address = server.accept()
        client_name = client_socket.recv(1024).decode('utf-8')  # 接收客户端名称
        clients[client_name] = client_socket
        print(f"{client_name} 已连接")

        # 启动线程处理该客户端
        threading.Thread(target=handle_client, args=(client_socket, client_name)).start()

if __name__ == "__main__":
    start_server()