"""
SSH command execution client.

Simple SSH client for executing commands on remote servers.
"""

import paramiko


def ssh_command(ip, port, user, passwd, cmd):
    """
    Execute a command via SSH and print the output.

    Args:
        ip: Server IP address
        port: SSH port
        user: Username
        passwd: Password
        cmd: Command to execute
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()

    if output:
        print('--- output ---')
        for line in output:
            print(line.strip())


if __name__ == '__main__':
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter Server IP: ') or '192.168.1.144'
    port = input('Enter Server Port: ') or 2222
    cmd = input('Enter Server CMD: ') or 'id'
    ssh_command(ip, port, user, password, cmd)
