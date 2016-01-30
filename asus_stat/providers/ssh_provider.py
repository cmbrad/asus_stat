import paramiko
from . import CommandErrorException


class SSHProvider():
	def __init__(self, username, password, host='192.168.1.1', port=22):
		self.username = username
		self.password = password
		self.host = host
		self.port = port

		self.ssh = self.setup_ssh()


	def setup_ssh(self):
		ssh = paramiko.SSHClient()

		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(self.host, username=self.username, password=self.password, port=self.port)

		return ssh


	def execute_command(self, command):
		(ssh_stdin, ssh_stdout, ssh_stderr) = self.ssh.exec_command(command)

		stderr = ssh_stderr.read()
		if stderr:
			raise CommandErrorException(stderr)
	
		return ssh_stdout.read()
	

	def get_var(self, variable):
		return self.execute_command('nvram get {0}'.format(variable)).strip()

