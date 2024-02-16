import paramiko
import scp
import getpass

ip = input('Enter the IP address you would like to connect: ')
user = input('User Name: ')
passw = getpass.getpass(stream=None)
command = "/sbin/ifconfig >> test.txt"
ssh = paramiko.SSHClient()

def ssh_funct():
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=22, username=user,
                       password=passw, timeout=3)
    stdin, stdout, stderr = ssh.exec_command(command)
    scpFile = scp.SCPClient(ssh.get_transport())
    for line in stdout.readlines():
        print(line)
    scpFile.get('test.txt')
    ssh.close()

ssh_funct()
