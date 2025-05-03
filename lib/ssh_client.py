import paramiko

class SSHClient:
    def __init__(self, hostname, username, password):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.hostname = hostname
        self.username = username
        self.password = password

    def connect(self):
        self.client.connect(self.hostname, username=self.username, password=self.password)

    def run_cmd(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return stdout.read().decode(), stderr.read().decode()
