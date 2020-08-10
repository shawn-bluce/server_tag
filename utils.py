
import os
import socket
import ipaddress


def is_ip_address(host):
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


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

    # try to get host from ssh_config, if has ssh_config
    host_from_ssh_config = analysis_ssh_config(host)
    host = host_from_ssh_config or host

    if is_ip_address(host):
        return host
    else:
        return socket.gethostbyname(host)
