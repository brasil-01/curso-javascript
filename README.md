# Curso de JavaScript — interativo, em português

Um app de curso de programação no estilo freeCodeCamp: **tela inicial com todas as
lições para o aluno escolher**, lição à esquerda, editor de código real à direita,
execução isolada e **testes automáticos** que verificam se o seu código está correto.

Tudo em **um único arquivo** (`index.html`, ~240 KB), sem dependências, sem
build, sem servidor. Basta abrir no navegador — funciona offline.

## Conteúdo

**12 módulos · 72 lições · 336 testes automáticos**

| # | Módulo | Lições |
|---|---|---|
| 1 | Introdução ao JavaScript | 6 |
| 2 | Lógica e controle de fluxo | 6 |
| 3 | Funções | 6 |
| 4 | Arrays | 6 |
| 5 | Objetos | 6 |
| 6 | Strings | 6 |
| 7 | Loops (repetições) | 6 |
| 8 | Números, Math e Datas | 6 |
| 9 | O DOM e o navegador | 6 |
| 10 | Assincronismo | 6 |
| 11 | JavaScript moderno (ES6+) | 6 |
| 12 | Projetos finais | 6 |

Cada lição tem: teoria curta com exemplos, uma tarefa prática, código inicial,
dica opcional, solução comentada e testes que rodam o seu código.

## Recursos do app

- **Tela inicial com a trilha completa**: o app abre em um índice com as 72 lições
  agrupadas por módulo (número, título, duração, selo `DOM` e marca de concluída),
  barra de progresso e botão **Continuar** que leva de volta à lição onde o aluno
  parou. Dá para voltar ao início a qualquer momento pelo logo ou pelo item
  "Início do curso" na barra lateral.
- **Duas visões do curso**: `▦ Grade` (cards) e `🧭 Trilha` (mapa de fases em
  zigue-zague, com a lição atual destacada em dourado e as concluídas em verde).
  A escolha fica salva.
- **Filtros rápidos** na tela inicial: Todas / Pendentes / Concluídas / Com DOM,
  com contagem em cada chip.
- **"próxima pendente →"** no cabeçalho de cada módulo: pula direto para a
  primeira lição ainda não concluída daquele módulo.
- **Editor com destaque de sintaxe**, números de linha, auto-indentação,
  fechamento automático de parênteses/chaves, `Tab`/`Shift+Tab` e `Ctrl+/`
  para comentar.
- **Execução em sandbox**: lições sem DOM rodam em um **Web Worker** (seu código
  é morto se entrar em loop infinito); lições de DOM rodam em um
  `iframe` isolado com `sandbox="allow-scripts"` — o código do aluno não tem
  acesso à página do curso.
- **Console** com `log`, `warn`, `error` e formatação de arrays/objetos, além da
  aba **Página** para ver o HTML/DOM ao vivo nas lições de DOM.
- **Testes** com mensagem por item, aprovado/reprovado e proteção contra timeout.
- **Progresso salvo** no `localStorage` (com fallback em memória quando o
  armazenamento é bloqueado) e código de cada lição preservado.
- **Busca** de lições, navegação por módulos recolhíveis, atalhos
  `Ctrl+Enter` (executar) e `Ctrl+Shift+Enter` (testar).
- Layout responsivo (desktop em duas colunas, celular empilhado com menu lateral).

## Como usar

```bash
# abrir direto
xdg-open index.html      # ou dê duplo clique no arquivo

# ou servir localmente
python3 -m http.server 8000
```

## Estrutura do projeto

```
index.html          ← app final (autocontido, é o entregável)
build.py            ← gera o index.html a partir de src/ + content/
src/styles.css      ← todo o CSS
src/app.js          ← engine: editor, destaque, runner, testes, navegação
content/mod_a.py    ← módulos 1–3 (Python só como "formato de autoria")
content/mod_b.py    ← módulos 4–6
content/mod_c.py    ← módulos 7–9
content/mod_d.py    ← módulos 10–12
tools/validate.js   ← roda a solução de cada lição contra os testes (jsdom)
tools/e2e.js        ← testa o app de verdade no Chromium (Playwright)
tools/qa.js         ← checagens extras: progresso, editor, atalhos, loop infinito
tools/qa-home.js    ← checagens da tela inicial: filtros, trilha, botão continuar, módulo
```

O conteúdo é escrito em Python porque as strings literais (`r"""`) permitem
colar JavaScript e Markdown sem escapar aspas. `build.py` converte tudo em JSON
e injeta no HTML.

## Como adicionar uma lição

Em qualquer arquivo de `content/`, acrescente um item em `lessons`:

```python
{
 "id": "m4l7",                      # único
 "title": "Novo método",
 "minutes": 7,
 "theory": r"""
## Título
Texto em Markdown: **negrito**, `código`, listas, blocos ```js e notas:
> [tip] dica
""",
 "task": r"""O que o aluno deve fazer.""",
 "starter": r"""// código inicial""",
 "solution": r"""// solução de referência""",
 "hint": r"""Dica opcional (aceita Markdown inline).""",
 "html": r"""<div id="app">…</div>""",   # opcional: só lições de DOM
 "tests": [
   {"msg": "Mensagem mostrada ao aluno",
    "code": r"""typeof minhaFuncao === "function" && minhaFuncao(2) === 4"""},
 ],
}
```

Cada teste é uma **expressão JavaScript** avaliada no mesmo escopo do código do
aluno (pode usar `await`). Variáveis disponíveis nos testes:

| variável | o que é |
|---|---|
| `__code` | o código-fonte que o aluno escreveu (texto) |
| `__logs` | array `{ level, text }` do que foi impresso |
| `__printed()` | todo o console como um único texto |
| `__normalize(s)` | texto em minúsculas, sem espaços repetidos |

Depois de editar:

```bash
python3 build.py            # regenera index.html
node tools/validate.js      # confere todas as soluções contra os testes
node tools/e2e.js           # confere no Chromium real (precisa de playwright)
```

## Notas técnicas

- A sandbox recebe o código por `postMessage` e executa com `AsyncFunction`, que
  permite `await` no nível superior (necessário nas lições de assincronismo).
- `console`, `alert`, `prompt` e `confirm` são substituídos dentro do harness,
  então nada vaza para a página do curso.
- O runner do Worker e o documento do `iframe` são strings geradas no cliente;
  nenhum código do aluno é inserido no HTML por concatenação.
