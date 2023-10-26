SSL Certificates
================

[![Actions Status](https://github.com/ome/ansible-role-ssl-certificate/workflows/Molecule/badge.svg)](https://github.com/ome/ansible-role-ssl-certificate/actions)
[![Ansible Role](https://img.shields.io/badge/ansible--galaxy-ssl_certificate-blue.svg)](https://galaxy.ansible.com/ui/standalone/roles/ome/ssl_certificate/)

Manage SSL certificates for web-servers.

Optionally generate self-signed SSL certificates for internal testing.


Role Variables
--------------

Defaults: `defaults/main.yml`

Optional variables:

- `ssl_certificate_public_path`: Server path to SSL public certificate
- `ssl_certificate_intermediate_path`: Server path to SSL intermediate certificate(s)
- `ssl_certificate_bundled_path`: Server path to SSL bundled public and intermediate certificates (e.g. for Nginx)
- `ssl_certificate_key_path`: Server path to SSL certificate key
- `ssl_certificate_combined_path`: Server path to SSL combined certificate and key (e.g. for Haproxy), set to empty to disable
- `ssl_certificate_public_content`: Text content of the certificate, for instance from vault
- `ssl_certificate_intermediate_content`: Text content of the intermediate certificate(s)
- `ssl_certificate_key_content`: Text content of the certificate key
- `ssl_certificate_selfsigned_create`: Create a self-signed certificate if necessary, default `True`
- `ssl_certificate_selfsigned_subject`: Self-signed certificate subject
- `ssl_certificate_selfsigned_days`: Self-signed certificate validity (days)
- `ssl_certificate_install_openssl`: Install OpenSSL, default `True`

Listeners/Handlers
------------------

This role notifies a listener `ssl certificate changed` when any changes are made.
This should be used to trigger a restart of any services dependent on the certificates.


Example Playbooks
-----------------

Create a self-signed certificate with defaults and restart Nginx (assumed to be already installed and configured):

    - hosts: all
      roles:
        - role: ome.ssl_certificate
      handlers:
        - name: restart nginx
          listen: ssl certificate changed
          service:
            name: nginx
            state: restarted

Install certificates stored locally on machine running Ansible:

    - hosts: all
      roles:
        - role: ssl-certificate
          ssl_certificate_public_content: "{{ lookup('file', '/path/to/server.crt') + '\n' }}"
          ssl_certificate_key_content: "{{ lookup('file', '/path/to/server.key') + '\n' }}"
          ssl_certificate_selfsigned_create: False


Note: the additional newline being added after the lookup content is to correct Ansible bug https://github.com/ansible/ansible/issues/30829.

Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
