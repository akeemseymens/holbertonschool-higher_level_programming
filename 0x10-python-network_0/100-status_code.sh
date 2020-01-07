#!/bin/bash
#some code
curl -sLI "$1"-o /dev/null -w '%{http_code}'
