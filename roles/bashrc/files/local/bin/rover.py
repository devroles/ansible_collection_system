#!/usr/bin/python
# (c) Michael Scherer <mscherer@redhat.com>
# use it as you want under MIT license

from __future__ import print_function
import requests
from bs4 import BeautifulSoup
from requests_kerberos import HTTPKerberosAuth, DISABLED
import sys


def main(user):
    kerberos_auth = HTTPKerberosAuth(mutual_authentication=DISABLED)

    s = requests.Session()
    r = s.get("https://rover.redhat.com/people/rest/user/%s" % user)
    soup = BeautifulSoup(r.text, 'html.parser')

    r = s.post(soup.form['action'],
               data={"SAMLRequest": soup.form.input['value']},
               auth=kerberos_auth)

    soup = BeautifulSoup(r.text, 'html.parser')

    data = s.post(soup.form['action'],
                  data={"SAMLResponse": soup.form.input['value']}).json()
    print("Given name:", data['cn'])
    if 'rhatPronoun' in data:
        print("Pronouns:  ", data['rhatPronoun'])
    else:
        print("No pronouns defined currently")


for user in sys.argv[1:]:
    main(user)
