from common.singleton import singleton
import struct
import json

class MySocket:
    def __init__(self, sock):
        self.sock = sock
            
    def recvDict(self):
        length_bytes = self.sock.recv(4)
        if len(length_bytes) < 4:
            return None
        length = struct.unpack('!I', length_bytes)[0]
        result = ""
        while length > 1024:
            result += self._recvStr(1024)
            length -= 1024
        if length > 0:
            result += self._recvStr(length)
        return json.loads(result)
        
    def _recvStr(self, length):
        return self.sock.recv(length).decode('utf-8')
    
    def sendDict(self, d):
        message = json.dumps(d)
        message_bytes = message.encode('utf-8')

        length = len(message_bytes)
        packed_length = struct.pack('!I', length)

        self.sock.sendall(packed_length)
        self.sock.sendall(message_bytes)