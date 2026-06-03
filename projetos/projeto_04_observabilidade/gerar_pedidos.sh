#!/usr/bin/env bash
set -euo pipefail

for i in $(seq 1 256); do
  curl -s "http://localhost:8000/pedido/$i"
  echo
done
