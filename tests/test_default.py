import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_certificate(Command, Sudo):
    with Sudo():
        out = Command.check_output(
            'openssl x509 -in /etc/ssl/server.crt -noout -subject')
    assert out.startswith(
        'subject= /C=UK/ST=Scotland/L=Dundee/O=OME/CN=')
