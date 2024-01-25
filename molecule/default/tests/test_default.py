import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_certificate(host):
    with host.sudo():
        out = host.check_output(
            'openssl x509 -in /etc/ssl/localcerts/server.crt -noout -subject')
    assert out.startswith(
        'subject=C = UK, ST = Scotland, L = Dundee, O = OME, CN =')


def test_listener_trigger(host):
    assert host.file('/tmp/ssl-certificate-changed').exists
