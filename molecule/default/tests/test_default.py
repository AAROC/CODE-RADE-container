import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ssh(host):
    s = host.socket('tcp://22')
    assert s.is_listening
    
    config_file = host.file('/usr/local/etc/sshd_config')
    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert config_file.mode == '0640'


def test_ssh_keys(host):
    host_key_file = host.file('/usr/local/etc/ssh_host_dsa_key')

    assert host_key_file.exists
    assert host_key_file.is_file
    assert host_key_file.user == 'root'
    assert host_key_file.group == 'root'
    assert host_key_file.mode == '0600'


def test_jenkins(host):
    jenkins = host.user('jenkins')

    assert jenkins.home == '/home/jenkins'
    assert jenkins.name == 'jenkins'
    assert jenkins.uid == 1500
    assert jenkins.gid == 1500
