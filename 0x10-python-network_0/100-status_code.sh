#!/bin/bash
#some code
curl -sL -I "$1"-o /dev/null -w '%{http_code}'
