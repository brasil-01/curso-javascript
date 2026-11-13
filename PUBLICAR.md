# Publicar o curso (GitHub + Vercel)

## Status

| Onde | Situação | Link |
|---|---|---|
| **GitHub** | ✅ publicado (3 commits, branch `main`) | <https://github.com/brasil-01/curso-javascript> |
| **Vercel** | ⏳ projeto `curso-javascript` criado, **deploy pendente** | — |

O projeto Vercel existe na sua conta (`curso-javascript`, framework *Other*, sem build).
Falta apenas o deploy — e ele não pôde ser disparado de dentro da conversa porque:

1. o conector do Vercel só envia arquivos pelo chat (o `index.html` tem 266 KB) e não
   aceita o parâmetro `projectSettings` exigido no primeiro deploy;
2. a **integração GitHub → Vercel** ainda não tem permissão sobre o repositório novo
   (a API respondeu: *"To link a GitHub repository, you need to install the GitHub
   integration first"*).

Qualquer um dos dois caminhos abaixo resolve em menos de um minuto.

---

## Caminho A — deploy automático a cada push (recomendado)

**1. Dê acesso ao repositório para o app do Vercel no GitHub**

<https://github.com/settings/installations> → **Vercel** → *Configure* →
**Repository access** → *Only select repositories* → marque **curso-javascript** → *Save*.

**2. Importe o repositório no Vercel**

<https://vercel.com/new> → escolha `brasil-01/curso-javascript` → **Import**:

- *Framework Preset*: **Other**
- *Build Command*: vazio
- *Output Directory*: vazio
- *Root Directory*: `./`

Clique em **Deploy**. A partir daí, todo `git push` na `main` gera um deploy de produção.

> Se quiser, pode apontar esse import para o projeto que já existe (`curso-javascript`)
> em vez de criar outro — o Vercel oferece isso na tela de import.

**Depois do primeiro deploy:** o site ficará em `https://curso-javascript.vercel.app`.
Se pedir login (Vercel Authentication), vá em projeto → **Settings** →
**Deployment Protection** → *Vercel Authentication* → **Disabled** → *Save*.

---

## Caminho B — deploy pelo terminal (não precisa de GitHub)

Baixe o `curso-javascript.zip`, extraia e, dentro da pasta:

```bash
npx vercel@latest deploy --prod --yes
```

O arquivo `.vercel/project.json` já aponta para o projeto `curso-javascript`, então o
deploy cai direto nele. Na primeira execução o Vercel pede login no navegador.

> Depois, para conectar esse projeto ao Git: Vercel → **Settings** → **Git** →
> *Connect Git Repository* → `brasil-01/curso-javascript`.

---

## Referência rápida

```bash
# --- Git / GitHub -------------------------------------------------
git remote -v                      # origin → github.com/brasil-01/curso-javascript
git push origin main               # já está tudo publicado

# --- Conteúdo -----------------------------------------------------
python3 build.py                   # regenera index.html a partir de src/ + content/
node tools/validate.js             # roda a solução das 72 lições contra os testes
node tools/e2e.js                  # testa no Chromium real (precisa de playwright)

# --- Deploy -------------------------------------------------------
npx vercel@latest deploy --prod --yes

# --- publicar.sh (faz git push + deploy) --------------------------
./publicar.sh
```

## Checklist

- [x] repositório público no GitHub com o código e o histórico
- [ ] permissão do app Vercel no GitHub para `curso-javascript`
- [ ] deploy no Vercel em estado **Ready**
- [ ] `Deployment Protection` desativada (site público)
- [ ] abrir o site publicado e concluir uma lição para confirmar que editor,
      sandbox e testes funcionam em produção

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
.vercel/project.json← vínculo com o projeto Vercel (fora do Git, de propósito)
```

---

### Sobre o token do GitHub

O token que você enviou foi usado **apenas** para criar o repositório e fazer o push,
ficou em um arquivo temporário fora do workspace (`/tmp`, já apagado) e **não** foi
gravado no `.git/config` nem em nenhum arquivo do projeto. Como ele foi colado em uma
conversa, o mais seguro é **revogá-lo e gerar outro**:

<https://github.com/settings/tokens> → localize o token → *Delete* → *Generate new token*.
