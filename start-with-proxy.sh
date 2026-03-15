#!/bin/bash
# MiroFish + LiteLLM proxy launcher
# Usage: ./start-with-proxy.sh
# Prerequisites: .env configured, litellm installed in .venv-proxy

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Load env
if [ ! -f .env ]; then
  echo "❌ .env not found. Copy .env.example.litellm → .env and fill in keys."
  exit 1
fi
source .env

# Start LiteLLM proxy in background
echo "🚀 Starting LiteLLM proxy on :4000..."
source .venv-proxy/bin/activate
litellm --config litellm-config.yaml --port 4000 &
LITELLM_PID=$!
echo "   LiteLLM PID: $LITELLM_PID"

# Wait for proxy to be ready
sleep 3
curl -s http://localhost:4000/health > /dev/null && echo "✅ LiteLLM proxy ready" || echo "⚠️  Proxy health check failed"

# Start MiroFish
echo "🐟 Starting MiroFish (frontend :3000, backend :5001)..."
npm run dev &
MIROFISH_PID=$!

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  MiroFish:      http://localhost:3000"
echo "  Backend API:   http://localhost:5001"
echo "  LiteLLM proxy: http://localhost:4000"
echo "  LiteLLM UI:    http://localhost:4000/ui  (usage dashboard)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Press Ctrl+C to stop all services"

# Cleanup on exit
trap "echo 'Shutting down...'; kill $LITELLM_PID $MIROFISH_PID 2>/dev/null; exit" INT TERM

wait
