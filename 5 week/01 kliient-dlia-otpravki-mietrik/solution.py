import time
import socket


class ClientError(Exception):
    "base exception for client"
    pass


class Client():

    def __init__(self, address, port, timeout=None):

        self.address = address
        self.port = port
        self.timeout = timeout

        try:
            self.connection = socket.create_connection((address, port), timeout)
        except socket.error as err:
            raise ClientError("Cannot create connection", err)


    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientError("Cannot close connection", err)    
    

    def parse_result(self, data):
        
        result = {}
        
        for line in data.split('\n'):
            if line:
                (metric, value, timestamp) = line.split(' ')
                result[metric] = result.get(metric, [])
                result[metric].append((int(timestamp), float(value)))

        return {metric: sorted(values, key=lambda x:x[0]) for metric, values in result.items()}

    def put(self, metric, value, timestamp=None):
        timestamp = timestamp or int(time.time())
    
        try:
            request_str = f"put {metric} {value} {timestamp}\n"
            self.connection.sendall(request_str.encode())
            data = self.connection.recv(1024)
            data = data.decode('utf-8')
            status, data = data.split('\n', 1)
            if status != 'ok':
                raise ClientError('Server returns bad status')
                
        except:
            raise ClientError('Server returns an error')

    def get(self, metric):

        try:
            request_str = f"get {metric}\n"
            self.connection.sendall(request_str.encode())
            data = self.connection.recv(1024)
            data = data.decode('utf-8')
            status, data = data.split('\n', 1)
            if status != 'ok':
                raise ClientError('Server returns bad status')

            return self.parse_result(data)

        except:
            raise ClientError('Server returns invalid data')