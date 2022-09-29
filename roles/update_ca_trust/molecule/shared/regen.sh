#!/usr/bin/env bash

target="$(cd "$(dirname "${0}")" &>/dev/null; pwd)"
dest=$(mktemp -d)
pushd "${dest}"

# Create server cert and key
openssl req -x509 -sha256 -days 30000 -nodes -newkey rsa:2048 -subj "/CN=demo.nothing/C=US/L=Nowhere" -keyout rootCA.key -out rootCA.crt

# Create server key
openssl genrsa -out server.key 2048
# Create csr.conf
cat > csr.conf <<EOF
[ req ]
default_bits = 2048
prompt = no
default_md = sha256
req_extensions = req_ext
distinguished_name = dn

[ dn ]
C = US
ST = Texas
L = Nowhere
O = Nope Inc
OU = Nope Inc Dev
CN = sign.local.dev

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = ns1.sign.local.dev
DNS.2 = ns2.sign.local.dev
IP.1 = 192.168.1.5
IP.2 = 192.168.1.6

EOF
# Create CSR
openssl req -new -key server.key -out server.csr -config csr.conf
# Create the cert.conf
cat > cert.conf <<EOF

authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = ns1.sign.local.dev

EOF
# Sign the certificate
openssl x509 -req -in server.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out server.crt -days 30000 -sha256 -extfile cert.conf

# Move them into place
mv server.crt "${target}/localhost.localdomain.crt"
mv rootCA.crt "${target}/rootCA.crt"
