#!/usr/bin/env bash

grep "POST __PATH__" /var/log/nginx/__DOMAIN__-access.log | grep '" 500 ' || true
