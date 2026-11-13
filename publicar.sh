#!/usr/bin/env bash
# Publica o curso: git push no GitHub + deploy de produção no Vercel.
# Uso:  ./publicar.sh
set -euo pipefail
cd "$(dirname "$0")"

echo "▶ 1/2 · GitHub"
if [ ! -d .git ]; then
  git init -b main >/dev/null
  git add -A
  git commit -m "Curso de JavaScript interativo: 12 módulos, 72 lições, 336 testes" >/dev/null
fi

if git remote get-url origin >/dev/null 2>&1; then
  git push -u origin main
elif command -v gh >/dev/null 2>&1; then
  gh repo create curso-javascript --public --source=. --remote=origin --push
else
  echo "  Sem remote 'origin'. Crie o repositório em https://github.com/new e rode:"
  echo "    git remote add origin git@github.com:SEU-USUARIO/curso-javascript.git"
  echo "    git push -u origin main"
fi

echo "▶ 2/2 · Vercel"
npx vercel@latest deploy --prod --yes
