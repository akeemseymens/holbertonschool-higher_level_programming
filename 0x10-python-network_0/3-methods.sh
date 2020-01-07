#!/bin/bash
#some note
curl -sI "$1" | awk '/Allow/' | cut -d' ' -f2-
