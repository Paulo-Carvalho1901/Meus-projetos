#!/usr/bin/env bash
set -euo pipefail

SLACK_API_URL="https://slack.com/api/chat.postMessage"
TOKEN="${SLACK_BOT_TOKEN}"
CHANNEL="${SLACK_CHANNEL_ID}"
MESSAGE="${1:-🚨 Falha detectada na aplicação de observabilidade. Verifique o dashboard do Grafana.}"
export CHANNEL MESSAGE

if [[ -z "$TOKEN" ]]; then
  echo "Erro: defina SLACK_BOT_TOKEN com um Bot User OAuth Token (xoxb-...)." >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "Erro: python3 não encontrado para montar payload JSON." >&2
  exit 1
fi

PAYLOAD="$(python3 - <<'PY'
import json, os
print(json.dumps({
    "channel": os.environ["CHANNEL"],
    "text": os.environ["MESSAGE"]
}, ensure_ascii=False))
PY
)"

RESPONSE="$(curl -sS -X POST "$SLACK_API_URL" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json; charset=utf-8" \
  --data "$PAYLOAD")"
export RESPONSE

OK="$(python3 - <<'PY'
import json, os
try:
    data = json.loads(os.environ["RESPONSE"])
    print("true" if data.get("ok") else "false")
except Exception:
    print("false")
PY
)"

if [[ "$OK" != "true" ]]; then
  echo "Falha ao enviar para Slack:" >&2
  echo "$RESPONSE" >&2
  exit 1
fi

echo "Mensagem enviada para Slack no canal/DM $CHANNEL"
