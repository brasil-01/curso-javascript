#!/usr/bin/env bash
# Publica o curso no GitHub e no Vercel.
# Uso:  ./publicar.sh
set -euo pipefail
cd "$(dirname "$0")"

echo "▶ 1/2 · GitHub"
if [ ! -d .git ]; then
  git init -b main >/dev/null
  git add -A
  git commit -m "Curso de JavaScript interativo: 12 módulos, 72 lições, 336 testes" >/dev/null
  echo "  repositório criado e commit inicial feito"
fi

if command -v gh >/dev/null 2>&1; then
  if git remote get-url origin >/dev/null 2>&1; then
    git push -u origin main
  else
    gh repo create curso-javascript --public --source=. --remote=origin --push
  fi
  echo "  enviado: $(git remote get-url origin)"
else
  echo "  gh (GitHub CLI) não encontrado. Faça manualmente:"
  echo "    1) crie o repositório em https://github.com/new (nome: curso-javascript, sem README)"
  echo "    2) git remote add origin git@github.com:SEU-USUARIO/curso-javascript.git"
  echo "    3) git push -u origin main"
fi

echo "▶ 2/2 · Vercel"
npx vercel@latest deploy --prod --yes
