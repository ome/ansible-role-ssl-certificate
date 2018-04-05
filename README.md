SSL Certificates
================

[![Build Status](https://travis-ci.org/openmicroscopy/ansible-role-ssl-certificate.svg)](https://travis-ci.org/openmicroscopy/ansible-role-ssl-certificate)
[![Ansible Role](https://img.shields.io/ansible/role/24524.svg)](https://galaxy.ansible.com/openmicroscopy/ssl-certificate/)

Manage SSL certificates for web-servers.

Optionally generate self-signed SSL certificates for internal testing.


Role Variables
--------------

Defaults: `defaults/main.yml`

Optional variables:
- `ssl_certificate_public_path`: Server path to SSL public certificate
- `ssl_certificate_intermediate_path`: Server path to SSL intermediate certificate(s)
- `ssl_certificate_key_path`: Server path to SSL certificate key
- `ssl_certificate_combined_path`: Server path to SSL combined certificate and key (e.g. for Haproxy), set to empty to disable
- `ssl_certificate_content`: Text content of the certificate, for instance from vault
- `ssl_certificate_key_content`: Text content of the certificate key
- `ssl_certificate_selfsigned_create`: Create a self-signed certificate if necessary, default `True`
- `ssl_certificate_selfsigned_subject`: Self-signed certificate subject
- `ssl_certificate_selfsigned_days`: Self-signed certificate validity (days)


Note this role does not configure or restart any webserver for SSL.
This should be handled elsewhere.


Example Playbooks
-----------------

Create a self-signed certificate with defaults:

    - hosts: all
      roles:
        - role: ssl-certificate

Install certificates stored locally on machine running Ansible:

    - hosts: all
      roles:
        - role: ssl-certificate
          ssl_certificate_public_content: "{{ lookup('file', '/path/to/server.crt') }}"
          ssl_certificate_key_content: "{{ lookup('file', '/path/to/server.key') }}"
          ssl_certificate_selfsigned_create: False


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
