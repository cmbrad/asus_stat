from asus_stat.providers.ssh_provider import SSHProvider


class DSLAC68U():
	def __init__(self, username, password, host, port):
		self.provider = SSHProvider(username, password, host, port)

	def dsl_data_rate_up(self):
		return self.provider.get_var('dsllog_datarateup')

	def dsl_data_rate_down(self):
		return self.provider.get_var('dsllog_dataratedown')

	def dsl_snr_margin_up(self):
		return self.provider.get_var('dsllog_snrmarginup')

	def dsl_snr_margin_down(self):
		return self.provider.get_var('dsllog_snrmargindown')

