#!/bin/bash
set -x
mktorrent -a udp://tracker.openbittorrent.com:80 -a udp://open.demonii.com:1337 -a udp://tracker.coppersurfer.tk:6969 -a udp://tracker.leechers-paradise.org:6969 "${1}" -o "${2}"
