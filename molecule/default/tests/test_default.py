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

    config_file = host.file('/usr/local/etc/sshd_config')
    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert config_file.mode == 420

    cmd = host.run('/usr/local/sbin/sshd -p 2222')
    assert cmd.rc == 0
    assert host.socket('tcp://2222').is_listening


def test_ssh_keys(host):
    host_key_file = host.file('/usr/local/etc/ssh_host_dsa_key')

    assert host_key_file.exists
    assert host_key_file.is_file
    assert host_key_file.user == 'root'
    assert host_key_file.group == 'root'
    assert host_key_file.mode == 256


def test_jenkins_user(host):
    jenkins = host.user('jenkins')

    assert jenkins.home == '/home/jenkins'
    assert jenkins.name == 'jenkins'
    assert jenkins.uid == 1500
    assert jenkins.gid == 1500


def test_ci_dirs(host):
    ci_build_dir = host.file('/data/ci-build')
    assert ci_build_dir.exists
    assert ci_build_dir.is_directory
    assert ci_build_dir.user == 'jenkins'
    assert ci_build_dir.group == 'jenkins'
    assert ci_build_dir.mode == 493

    ci_module_dir = host.file('/data/modules')
    assert ci_module_dir.exists
    assert ci_module_dir.is_directory
    assert ci_module_dir.user == 'jenkins'
    assert ci_module_dir.group == 'jenkins'
    assert ci_module_dir.mode == 493


def test_deploy_dirs(host):
    deploy_dir = host.file('/cvmfs/code-rade.africa-grid.org')
    assert deploy_dir.exists
    assert deploy_dir.is_directory
    assert deploy_dir.user == 'jenkins'
    assert deploy_dir.group == 'jenkins'
    assert deploy_dir.mode == 493
