import os 
import paramiko
import socket
import sys
import threading

CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename = os.path.join(CWD, '~/.ssh/gitkraken_rsa'))

class Server (paramiko.ServerInterface):
    def __init__(self) -> None:
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'foo') and (password == 'bar'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    if __name__ == '__main__':
        server = '192.168.1.144'
        ssh_port = 2222

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((server, ssh_port))
            sock.listen(100)

            print('[*] Listening for connection ...')
            client, addr = sock.accept()
        except Exception as e:
            print('[-] Listening Failed: ' + str(e))
            sys.exit()

        else:
            print('[*] Connection: ', client, addr)

        bhSession = paramiko.Transport(client)
        bhSession.add_server_key(HOSTKEY)
        bhSession.set_subsystem_handler('sftp', paramiko.SFTPServer)
        bhSession.start_server(Server())

        chan = bhSession.accept(20)
        if chan is None:
            print('[*] No Channel')
            sys.exit(1)
        
        print('[*] Authenticated!')
        print(chan.recv(4086))
        chan.send('Welcome to my SSH Server')

        try:
            while True:
                command = input('Enter Command: ')

                if command != 'exit':
                    chan.send(command)
                    r = chan.recv(8192)
                    print(r.decode())
                else:
                    chan.send('exit')
                    print('Exiting')
                    bhSession.close()
                    break
        except Exception as e:
            bhSession.close()

                    



