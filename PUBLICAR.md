# Publicar o curso (GitHub + Vercel)

O projeto já sai pronto: `index.html` autocontido, `README.md`, `LICENSE` (MIT),
`.gitignore`, repositório Git com o commit inicial e, em `.vercel/project.json`,
o vínculo com o projeto **curso-javascript** que já criei na sua conta Vercel.

> **Por que não publiquei direto daqui?** O conector do Vercel só aceita deploy
> enviando o conteúdo dos arquivos pela conversa, e o `index.html` tem 266 KB —
> acima do que é viável transmitir por esse canal (e o sandbox não tem token nem
> CLI autenticada). O GitHub nem existe como conector nesta plataforma. Por isso
> deixei tudo a **um comando de distância** — abaixo.

---

## Opção 1 — um comando para tudo (recomendado)

No seu computador, dentro da pasta do projeto:

```bash
./publicar.sh
```

O script faz, em ordem:

1. **GitHub** — se o [GitHub CLI](https://cli.github.com) (`gh`) estiver instalado
   e autenticado, cria o repositório público `curso-javascript` e dá push. Sem `gh`,
   ele imprime os 3 comandos para você fazer manualmente.
2. **Vercel** — roda `npx vercel deploy --prod --yes`. Como o `.vercel/project.json`
   já aponta para o projeto certo, o deploy vai direto para produção e o site fica
   em `https://curso-javascript.vercel.app`.

Pré-requisitos: `git` e Node 18+ (para o `npx`). Na primeira vez o Vercel pede login
no navegador.

---

## Opção 2 — só o Vercel (sem GitHub)

```bash
npx vercel@latest deploy --prod --yes
```

Ou, sem instalar nada: entre em [vercel.com/new](https://vercel.com/new) →
aba **"Deploy" / upload** → arraste esta pasta. O projeto `curso-javascript`
já existe na sua conta e pode ser reaproveitado.

### Se o site pedir login para abrir

Sua conta está com **Deployment Protection (Vercel Authentication)** ligada por
padrão. Para o curso ser público:

1. Vercel → projeto **curso-javascript** → **Settings** → **Deployment Protection**
2. Em *Vercel Authentication*, selecione **Disabled** (ou *Only Preview Deployments*)
3. **Save** e recarregue o site.

---

## Opção 3 — só o GitHub

**Com GitHub CLI:**

```bash
gh repo create curso-javascript --public --source=. --remote=origin --push
```

**Sem CLI (pelo site):**

1. Crie o repositório em <https://github.com/new> — nome `curso-javascript`,
   **sem** README/gitignore/license (o projeto já tem).
2. No terminal, dentro da pasta:

```bash
git remote add origin git@github.com:SEU-USUARIO/curso-javascript.git
git push -u origin main
```

**Sem terminal nenhum:** em <https://github.com/new> crie o repositório, clique em
*"uploading an existing file"* e arraste **index.html**, **README.md**, **LICENSE**,
**build.py**, `src/`, `content/` e `tools/`.

> O commit inicial foi assinado como `Curso de JavaScript
> <curso-javascript@users.noreply.github.com>`. Para usar a sua identidade:
> `git commit --amend --reset-author --no-edit`.

---

## Depois: deploy automático a cada push

1. Vercel → projeto **curso-javascript** → **Settings** → **Git**
2. **Connect Git Repository** → escolha o repositório `curso-javascript`
3. *Framework Preset*: **Other** · *Build Command*: vazio · *Output Directory*: vazio

A partir daí, cada `git push` na branch `main` gera um deploy de produção, e cada
pull request ganha um preview próprio.

---

## Checklist rápido

```bash
# 1. testar localmente (opcional, precisa de node)
python3 build.py            # regenera index.html a partir de src/ e content/
node tools/validate.js      # 72/72 lições passam nos próprios testes

# 2. publicar
./publicar.sh
```

- [ ] repositório no GitHub criado e com push feito
- [ ] deploy no Vercel em estado **Ready**
- [ ] `Deployment Protection` desligada (site público)
- [ ] abrir `https://curso-javascript.vercel.app` e concluir a primeira lição para confirmar
      que editor, sandbox e testes funcionam em produção

---

## Estrutura publicada

```
index.html          ← app final (tudo embutido: CSS, JS e as 72 lições)
README.md           ← descrição do projeto
LICENSE             ← MIT
publicar.sh         ← script de publicação (GitHub + Vercel)
build.py            ← gera o index.html a partir de src/ + content/
src/                ← styles.css e app.js (engine)
content/            ← módulos 1–12 em arquivos Python (formato de autoria)
tools/              ← validadores e testes automatizados
.vercel/project.json← vínculo com o projeto Vercel (fora do Git, de propósito)
```
