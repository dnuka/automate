#!/usr/bin/env python

import pwd
import sys
import shlex
import json

def main():
    # parsing argument file
    args = {}
    args_file = sys.argv[1]
    args_data = file(args_file).read()
    arguments = shlex.split(args_data)
    for arg in arguments:
        if '=' in arg:
            (key, value) = arg.split('=')
            args[key] = value
    user = args['user']

    # check if user exists
    try:
        pwd.getpwnam(user)
        success = True
        ret_msg = 'user %s exists' % user
    except KeyError:
        success = False
        ret_msg = 'user %s does not exists' % user

    # error handling and JSON return
    if success:
        print json.dumps({
            'msg': ret_msg
        })
        sys.exit(0)
    else:
        print json.dumps({
            'falied': True,
            'msg': ret_msg
        })
        sys.exit(1)

main()
