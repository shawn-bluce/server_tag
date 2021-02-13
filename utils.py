
import os
import socket
import subprocess


class ColorText:
    def __init__(self):
        self.warning_head = '\033[93m'
        self.success_head = '\033[92m'
        self.error_head = '\033[91m'
        self.end = '\033[0m'

    def success(self, text):
        print('{}{}{}'.format(self.success_head, text, self.end))

    def warning(self, text):
        print('{}{}{}'.format(self.warning_head, text, self.end))

    def error(self, text):
        print('{}{}{}'.format(self.error_head, text, self.end))


def analysis_ssh_config(host: str) -> str:
    """if host in ~/.ssh/config, get it real hostname"""
    home_path = os.environ.get('HOME')
    ssh_config_path = home_path + '/.ssh/config'

    if not os.path.exists(ssh_config_path):
        return host

    ssh_config_lines = open(ssh_config_path).read().split('\n')
    for index, line in enumerate(ssh_config_lines):
        if line.strip() == 'Host {}'.format(host):
            while line:
                line = ssh_config_lines[index + 1].strip()
                key, host = line.split()
                if key == 'HostName':
                    return host


def get_ip_by_host(host: str) -> str:
    """
    :param host: domain or ip or ssh_config
    :return: ip address
    """

    # try to get host from ssh_config, if has ssh_config
    host_from_ssh_config = analysis_ssh_config(host)
    host = host_from_ssh_config or host
    return socket.gethostbyname(host)


def parse_ssh_command(full_command: str) -> str:
    awk_parm = '{print $2}'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cmd = f"{dir_path}/ssh_opt_parse.sh {full_command} | grep 'SSH_HOST' | awk -F ' ' '{awk_parm}'"
    host = subprocess.check_output(cmd, shell=True).strip()
    if isinstance(host, bytes):
        host = host.decode('utf-8')
    return host


color_text = ColorText()
