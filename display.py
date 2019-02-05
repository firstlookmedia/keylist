#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import subprocess


def main():
    with open('keylist.json') as f:
        data = json.load(f)
        for key in data['keys']:
            print('🔑 {}'.format(key['fingerprint']))
            subprocess.call(['gpg', '--list-keys', key['fingerprint']])
            print('―'*80+'\n')


if __name__ == '__main__':
    main()
