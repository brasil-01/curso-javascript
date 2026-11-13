# Publicar o curso (GitHub + Vercel)

## Status

| Onde | Situação | Link |
|---|---|---|
| **GitHub** | ✅ publicado (branch `main`, 7 commits) | <https://github.com/brasil-01/curso-javascript> |
| **GitHub Pages** | ✅ **no ar e testado** | **<https://brasil-01.github.io/curso-javascript/>** |
| **Vercel** | ⏳ projeto `curso-javascript` criado, deploy aguardando 1 passo | — |

O app já está público pelo GitHub Pages, que serve o mesmo `index.html` do repositório
(site estático, sem build). Verificado em Chromium contra a URL pública: 72 cards na
home, lição `m1l1` com 2/2 testes passando, lição com DOM em `iframe sandbox="allow-scripts"`,
progresso persistindo após reload e **zero erros de console**.

### Por que a Vercel ainda não está no ar

Dois bloqueios que só existem do lado da conta/provedor:

1. O **conector do Vercel** não expõe o parâmetro `projectSettings`, exigido no primeiro
   deploy de um projeto — a API respondeu `400 The projectSettings object is required for
   new projects`.
2. A **integração GitHub → Vercel não tem permissão sobre o repositório novo** — a API
   respondeu `To link a GitHub repository, you need to install the GitHub integration first`.
   Um token do GitHub não autoriza o Vercel (são provedores distintos).

Qualquer um dos três caminhos abaixo resolve — o **Caminho C é o mais rápido** e não
exige terminal nem instalar nada.

---

## Caminho A — GitHub Actions + segredo (sem terminal)

O repositório já tem o workflow `.github/workflows/deploy-vercel.yml`. Ele roda a cada
push na `main` e fica **verde sem fazer nada** enquanto o segredo não existir.

1. Crie um token em <https://vercel.com/account/tokens> → *Create* → nome `deploy-curso`
   → escopo da conta/team → copie.
2. No GitHub: <https://github.com/brasil-01/curso-javascript/settings/secrets/actions> →
   **New repository secret** → nome **`VERCEL_TOKEN`** → cole o token → *Add secret*.
3. Aba **Actions** → **Deploy no Vercel** → **Run workflow**.

Em ~1 minuto o deploy de produção é criado no projeto `curso-javascript`, com o domínio
`https://curso-javascript.vercel.app`.

## Caminho B — deploy automático pelo Git (mais “oficial”)

1. Libere o repositório para o app do Vercel:
   <https://github.com/settings/installations> → **Vercel** → *Configure* →
   **Repository access** → marque **curso-javascript** → *Save*.
2. <https://vercel.com/new> → importe `brasil-01/curso-javascript` →
   *Framework Preset*: **Other**, *Build/Output*: vazios → **Deploy**.

A partir daí cada push gera deploy de produção e cada PR ganha preview.

## Caminho C — pelo terminal

```bash
npx vercel@latest deploy --prod --yes
```

Dentro da pasta do projeto (o `.vercel/project.json` já aponta para `curso-javascript`,
então o deploy cai direto nele). Na primeira vez o Vercel pede login no navegador.

> Nos três caminhos: se o site pedir login, vá em projeto → **Settings** →
> **Deployment Protection** → *Vercel Authentication* → **Disabled** → *Save*.
> (Sua conta vem com essa proteção ligada por padrão.)

---

## Referência rápida

```bash
# --- Conteúdo -----------------------------------------------------
python3 build.py                   # regenera index.html a partir de src/ + content/
node tools/validate.js             # roda a solução das 72 lições contra os testes
node tools/e2e.js                  # testa no Chromium real (precisa de playwright)

# --- Git / GitHub -------------------------------------------------
git remote -v                      # origin → github.com/brasil-01/curso-javascript
git push origin main               # publica (Pages reconstrói sozinho)

# --- Deploy Vercel ------------------------------------------------
npx vercel@latest deploy --prod --yes
./publicar.sh                      # git push + deploy de produção
```

## Checklist

- [x] repositório público no GitHub com código e histórico
- [x] GitHub Pages ativo servindo `index.html` (`.nojekyll` incluído)
- [x] workflow de deploy no Vercel criado (verde, aguardando `VERCEL_TOKEN`)
- [ ] `VERCEL_TOKEN` configurado nos segredos do repositório
- [ ] deploy no Vercel em estado **Ready**
- [ ] `Deployment Protection` desativada (site público)
- [ ] abrir a URL e concluir uma lição para confirmar editor, sandbox e testes

## Estrutura do repositório

```
index.html          ← app final (tudo embutido: CSS, JS e as 72 lições)
README.md           ← descrição do projeto
LICENSE             ← MIT
PUBLICAR.md         ← este arquivo
publicar.sh         ← script de publicação (git push + deploy Vercel)
build.py            ← gera o index.html a partir de src/ + content/
src/                ← styles.css e app.js (engine: editor, sandbox, testes)
content/            ← módulos 1–12 (formato de autoria em Python)
tools/              ← validate.js, e2e.js, qa.js, qa-home.js
.github/workflows/  ← deploy-vercel.yml
.vercel/project.json← vínculo com o projeto Vercel (fora do Git, de propósito)
```

---

### Sobre o token do GitHub

Os tokens enviados foram usados **apenas** para criar o repositório, dar push e ativar o
Pages. Ficaram em arquivo temporário fora do workspace (`/tmp`, já apagado) e **não** foram
gravados no `.git/config` nem em nenhum arquivo do projeto. Como foram colados em uma
conversa, revogue-os e gere outro: <https://github.com/settings/tokens>.
