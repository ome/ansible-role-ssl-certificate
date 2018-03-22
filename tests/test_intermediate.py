import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('ssl-certificate-u1604')


@pytest.mark.parametrize("cert", [
    'bundled.crt',
    'combined.pem',
])
def test_intermediate(Command, Sudo, cert):
    with Sudo():
        out = Command.check_output(
            'openssl crl2pkcs7 -nocrl -certfile /etc/ssl/%s | '
            'openssl pkcs7 -print_certs -text -noout |grep Subject:'
            % cert)
        lines = out.splitlines()
        assert lines[0].strip().startswith(
            'Subject: C=UK, ST=Scotland, L=Dundee, O=OME, CN=')
        assert lines[1].strip().startswith(
            'Subject: C=UK, ST=Dummy, L=Intermediate, O=Certificate')


@pytest.mark.parametrize("cert", [
    'bundled.crt',
    'combined.pem',
])
def test_combined(Command, Sudo, cert):
    with Sudo():
        out = Command.check_output('grep BEGIN /etc/ssl/%s' % cert)
    lines = out.splitlines()
    assert lines[0] == '-----BEGIN CERTIFICATE-----'
    assert lines[1] == '-----BEGIN CERTIFICATE-----'
    if cert == 'bundled.crt':
        assert len(lines) == 2
    else:
        assert len(lines) == 3
        assert lines[2] == '-----BEGIN PRIVATE KEY-----'
