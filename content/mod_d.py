# -*- coding: utf-8 -*-
"""Módulos 10 a 12 — Assincronismo, ES6+ e projetos."""

MODULES = [

# =====================================================================
{
 "id": "assincrono",
 "title": "Assincronismo",
 "icon": "⏳",
 "lessons": [

{
 "id": "m10l1",
 "title": "Callbacks e timers",
 "minutes": 8,
 "theory": r"""
## JavaScript não espera

JavaScript executa uma linha de cada vez, mas não fica parado esperando coisas lentas (rede, arquivo, timer). Ele agenda essas tarefas e continua.

```js
console.log("1");
setTimeout(() => console.log("2"), 1000);
console.log("3");
// imprime: 1, 3, 2
```

Isso é o **assincronismo**: o `setTimeout` registra a função e devolve o controle na hora. Depois de 1000 ms, a função entra na fila e roda quando a pilha principal estiver livre.

## Os timers

```js
const id = setTimeout(() => { /* uma vez, depois de 1s */ }, 1000);
clearTimeout(id);           // cancela antes de rodar

const intervalo = setInterval(() => { /* a cada 500ms */ }, 500);
clearInterval(intervalo);   // para o intervalo
```

## Callbacks: a base de tudo

Uma função passada para ser chamada "depois" é um **callback**. Todo o assincronismo do JavaScript é construído sobre eles — promises e async/await são formas mais organizadas de fazer a mesma coisa.

> [tip] `setTimeout(fn, 0)` não executa na hora: coloca `fn` no fim da fila. Ordem de execução é uma das perguntas clássicas de entrevista.
""",
 "task": r"""
Escreva um código que imprima, **nesta ordem**:

1. `"início"`
2. `"fim"`
3. `"depois de 100ms"` (usando `setTimeout` com 100 ms)

Dica: imprima `"início"`, agende o `setTimeout` e imprima `"fim"` logo em seguida.
""",
 "starter": r"""// imprima na ordem pedida


console.log("fim");
""",
 "solution": r"""console.log("início");

setTimeout(() => {
  console.log("depois de 100ms");
}, 100);

console.log("fim");
""",
 "hint": r"""O `setTimeout` precisa estar **entre** os dois `console.log` — mas ele não bloqueia: o `"fim"` aparece antes do `"depois de 100ms"`.""",
 "tests": [
   {"msg": "A primeira mensagem deve ser \"início\"",
    "code": r'''__logs.length > 0 && __logs[0].text === "início" '''},
   {"msg": "A segunda mensagem deve ser \"fim\" (o setTimeout não bloqueia)",
    "code": r'''__logs.length > 1 && __logs[1].text === "fim" '''},
   {"msg": "Depois de 100ms, deve aparecer \"depois de 100ms\"",
    "code": r'''(async () => { await new Promise((r) => setTimeout(r, 250)); return __printed().includes("depois de 100ms"); })()'''},
   {"msg": "Use setTimeout",
    "code": r'''/setTimeout/.test(__code)'''},
 ],
},

{
 "id": "m10l2",
 "title": "Promises",
 "minutes": 9,
 "theory": r"""
## A promessa

Uma **Promise** representa um valor que existirá no futuro. Ela tem três estados: *pendente*, *resolvida* (com valor) e *rejeitada* (com erro).

```js
const promessa = new Promise((resolve, reject) => {
  const deuCerto = true;

  if (deuCerto) {
    resolve("valor de sucesso");
  } else {
    reject(new Error("algo deu errado"));
  }
});
```

## Consumindo com .then

```js
promessa
  .then((valor) => console.log("ok:", valor))
  .catch((erro) => console.log("erro:", erro.message))
  .finally(() => console.log("terminou"));
```

`then` recebe o valor resolvido; `catch` recebe o erro; `finally` roda nos dois casos. Cada `then` devolve uma **nova** promise — é isso que permite encadear.

```js
esperar(100)
  .then(() => esperar(100))
  .then(() => console.log("200ms se passaram"))
  .catch((e) => console.log(e));
```

## Uma promise útil

```js
function esperar(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
```

> [warn] Uma promise só pode ser resolvida uma vez. Chamadas extras de `resolve`/`reject` depois da primeira são ignoradas.
""",
 "task": r"""
Crie:

1. `esperar(ms)` — função que devolve uma Promise resolvida **com a string** `"pronto"` depois de `ms` milissegundos.
2. Use `.then` para guardar o valor numa variável `mensagem`.
3. Use `.catch` para guardar um possível erro em `erro`.

Chame `esperar(50)`.
""",
 "starter": r"""function esperar(ms) {
  // retorne uma Promise
}

let mensagem = null;
let erro = null;

esperar(50)
  // .then(...)
  // .catch(...)

console.log(mensagem, erro);
""",
 "solution": r"""function esperar(ms) {
  return new Promise((resolve) => {
    setTimeout(() => resolve("pronto"), ms);
  });
}

let mensagem = null;
let erro = null;

esperar(50)
  .then((valor) => {
    mensagem = valor;
  })
  .catch((e) => {
    erro = e.message;
  });

console.log(mensagem, erro);
""",
 "hint": r"""Dentro da Promise você recebe `resolve` e `reject`; chame `resolve("pronto")` dentro do `setTimeout`.""",
 "tests": [
   {"msg": "esperar(50) deve devolver uma Promise",
    "code": r'''typeof esperar === "function" && esperar(10) instanceof Promise '''},
   {"msg": "A promise deve resolver com \"pronto\"",
    "code": r'''(async () => { const v = await esperar(10); return v === "pronto"; })()'''},
   {"msg": "mensagem deve receber o valor resolvido",
    "code": r'''(async () => { await new Promise((r) => setTimeout(r, 200)); return mensagem === "pronto"; })()'''},
   {"msg": "erro deve continuar null",
    "code": r'''erro === null'''},
   {"msg": "Use new Promise, .then e .catch",
    "code": r'''/new Promise/.test(__code) && /\.then\s*\(/.test(__code) && /\.catch\s*\(/.test(__code)'''},
 ],
},

{
 "id": "m10l3",
 "title": "async e await",
 "minutes": 9,
 "theory": r"""
## Promise com cara de código normal

`async/await` é açúcar sintático sobre promises: deixa o código assíncrono parecer sequencial.

```js
function esperar(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function executar() {
  console.log("começou");
  await esperar(100);
  console.log("passaram 100ms");
  return "resultado";
}

executar().then((r) => console.log(r));
```

Duas regras:

1. `async` antes da função faz ela **sempre** devolver uma Promise (mesmo que você use `return 5`).
2. `await` só pode ser usado **dentro** de função `async` — e faz o código dessa função esperar a promise terminar.

## O que o await devolve

```js
const valor = await esperar(50);   // undefined, se a promise não resolve nada
```

Você recebe o valor do `resolve`, não a promise.

## Erros com async/await

Com `await`, erros de promise podem ser capturados com `try/catch` comum:

```js
async function carregar() {
  try {
    const dados = await buscar();
    return dados;
  } catch (e) {
    console.log("falhou:", e.message);
  }
}
```

> [tip] `await` sequencial é lento: `const a = await f(); const b = await g();` espera um depois do outro. Se são independentes, use `Promise.all`.
""",
 "task": r"""
Você tem a função `esperar(ms)` pronta no código inicial.

Crie:

1. `async function somarDepoisDeEsperar(a, b)` — espera 30 ms com `await esperar(30)` e retorna a soma.
2. Chame essa função e guarde o resultado em `resultado` (a chamada acontece em contexto async, então você pode usar `await`).
""",
 "starter": r"""function esperar(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function somarDepoisDeEsperar(a, b) {
  // await esperar(30) e retorne a soma
}

const resultado = await somarDepoisDeEsperar(2, 3);

console.log(resultado);
""",
 "solution": r"""function esperar(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function somarDepoisDeEsperar(a, b) {
  await esperar(30);
  return a + b;
}

const resultado = await somarDepoisDeEsperar(2, 3);

console.log(resultado);
""",
 "hint": r"""`await` antes da chamada de `esperar(30)` faz a função pausar 30ms e continuar depois.""",
 "tests": [
   {"msg": "somarDepoisDeEsperar deve ser uma função async",
    "code": r'''typeof somarDepoisDeEsperar === "function" && somarDepoisDeEsperar.constructor.name === "AsyncFunction" '''},
   {"msg": "resultado deve ser 5",
    "code": r'''resultado === 5'''},
   {"msg": "A função deve funcionar com outros números",
    "code": r'''(async () => (await somarDepoisDeEsperar(10, -3)) === 7)()'''},
   {"msg": "Ela deve esperar de verdade (levar pelo menos ~25ms)",
    "code": r'''(async () => { const t0 = Date.now(); await somarDepoisDeEsperar(1, 1); return Date.now() - t0 >= 25; })()'''},
   {"msg": "Use async e await",
    "code": r'''/async\s+function/.test(__code) && /await\s+/.test(__code)'''},
 ],
},

{
 "id": "m10l4",
 "title": "Tratando erros assíncronos",
 "minutes": 9,
 "theory": r"""
## Erro não é exceção rara: é rotina

Rede cai, API devolve 500, usuário digita besteira. Código bom **prevê** o erro.

```js
async function buscarUsuario(id) {
  if (!id) {
    throw new Error("id obrigatório");   // vira promise rejeitada
  }
  return { id, nome: "Ana" };
}
```

## try / catch / finally

```js
async function executar() {
  try {
    const u = await buscarUsuario(null);
    console.log(u.nome);
  } catch (e) {
    console.log("deu erro:", e.message);   // id obrigatório
  } finally {
    console.log("sempre roda");
  }
}
```

## O `throw` também serve em funções normais

```js
function dividir(a, b) {
  if (b === 0) throw new Error("Divisão por zero");
  return a / b;
}
```

Quem chama precisa envolver em `try/catch` — senão o erro sobe e quebra o programa.

## Alternativa: devolver resultado em vez de lançar

Para situações previstas, muitas equipes preferem devolver um objeto:

```js
return { ok: false, erro: "Divisão por zero" };
```

Assim quem chama decide o que fazer, sem `try/catch` em todo lugar.

> [tip] Nunca engula um erro com `catch (e) {}` vazio: você perde a pista do que aconteceu.
""",
 "task": r"""
Crie:

1. `async function dividir(a, b)` — se `b` for `0`, **lança** `new Error("Divisão por zero")`; senão retorna `a / b`.
2. `async function calcular(a, b)` — chama `dividir` com `try/catch` e devolve:
   - `{ ok: true, valor: resultado }` em caso de sucesso;
   - `{ ok: false, erro: mensagem }` em caso de erro.
3. `const sucesso = await calcular(10, 2);`
4. `const falha = await calcular(10, 0);`
""",
 "starter": r"""async function dividir(a, b) {
  // seu código
}

async function calcular(a, b) {
  // try / catch
}

const sucesso = await calcular(10, 2);
const falha = await calcular(10, 0);

console.log(sucesso, falha);
""",
 "solution": r"""async function dividir(a, b) {
  if (b === 0) {
    throw new Error("Divisão por zero");
  }
  return a / b;
}

async function calcular(a, b) {
  try {
    const valor = await dividir(a, b);
    return { ok: true, valor };
  } catch (e) {
    return { ok: false, erro: e.message };
  }
}

const sucesso = await calcular(10, 2);
const falha = await calcular(10, 0);

console.log(sucesso, falha);
""",
 "hint": r"""Dentro do `catch (e)`, a mensagem está em `e.message`. Devolva o objeto com `ok: false`.""",
 "tests": [
   {"msg": "sucesso deve ser { ok: true, valor: 5 }",
    "code": r'''sucesso && sucesso.ok === true && sucesso.valor === 5'''},
   {"msg": "falha deve ser { ok: false, erro: \"Divisão por zero\" }",
    "code": r'''falha && falha.ok === false && falha.erro === "Divisão por zero" '''},
   {"msg": "dividir(10, 0) deve rejeitar com Error",
    "code": r'''(async () => { try { await dividir(10, 0); return false; } catch (e) { return e instanceof Error; } })()'''},
   {"msg": "dividir(9, 3) deve retornar 3",
    "code": r'''(async () => (await dividir(9, 3)) === 3)()'''},
   {"msg": "Use try e catch",
    "code": r'''/try\s*\{/.test(__code) && /catch\s*\(/.test(__code)'''},
 ],
},

{
 "id": "m10l5",
 "title": "Promise.all e paralelismo",
 "minutes": 8,
 "theory": r"""
## Sequencial é lento

```js
const a = await esperar(100);  // 100ms
const b = await esperar(100);  // mais 100ms → total 200ms
```

Se as tarefas são independentes, não há motivo para esperar uma terminar antes de começar a outra.

## Promise.all

```js
const [a, b] = await Promise.all([esperar(100), esperar(100)]);
// total: ~100ms
```

`Promise.all` recebe um array de promises e devolve uma promise com um **array de resultados, na mesma ordem**. Se qualquer uma falhar, o `Promise.all` inteiro é rejeitado (falha rápida).

## Variações úteis

```js
Promise.allSettled([p1, p2]);   // espera todas, com status de cada uma
Promise.race([p1, p2]);         // resolve com a primeira que terminar
Promise.any([p1, p2]);          // resolve com a primeira que der certo
```

## Exemplo real

```js
const [usuario, posts, comentarios] = await Promise.all([
  fetch("/usuario").then((r) => r.json()),
  fetch("/posts").then((r) => r.json()),
  fetch("/comentarios").then((r) => r.json()),
]);
```

Três requisições ao mesmo tempo em vez de três em fila.

> [warn] Só use `Promise.all` quando as tarefas não dependem uma da outra. Se a segunda precisa do resultado da primeira, tem que ser sequencial.
""",
 "task": r"""
Você tem `esperar(ms, valor)` — devolve uma promise que resolve com `valor` depois de `ms`.

1. Crie a função `async function buscarTudo()` que usa `Promise.all` para esperar três promises ao mesmo tempo:
   - `esperar(30, "usuário")`
   - `esperar(10, "posts")`
   - `esperar(20, "comentários")`
2. Guarde o resultado em `const dados = await buscarTudo();`
3. Guarde em `tempoTotal` quantos milissegundos a operação levou (use `Date.now()` antes e depois).
""",
 "starter": r"""function esperar(ms, valor) {
  return new Promise((resolve) => setTimeout(() => resolve(valor), ms));
}

async function buscarTudo() {
  // use Promise.all
}

const inicio = Date.now();
const dados = await buscarTudo();
const tempoTotal = Date.now() - inicio;

console.log(dados, tempoTotal);
""",
 "solution": r"""function esperar(ms, valor) {
  return new Promise((resolve) => setTimeout(() => resolve(valor), ms));
}

async function buscarTudo() {
  return Promise.all([
    esperar(30, "usuário"),
    esperar(10, "posts"),
    esperar(20, "comentários"),
  ]);
}

const inicio = Date.now();
const dados = await buscarTudo();
const tempoTotal = Date.now() - inicio;

console.log(dados, tempoTotal);
""",
 "hint": r"""Com `Promise.all`, o tempo total fica próximo do maior atraso (30ms) e não da soma (60ms). A ordem dos resultados é a do array.""",
 "tests": [
   {"msg": "dados deve ser [\"usuário\", \"posts\", \"comentários\"]",
    "code": r'''JSON.stringify(dados) === JSON.stringify(["usuário","posts","comentários"])'''},
   {"msg": "tempoTotal deve ser menor que 60ms (rodou em paralelo)",
    "code": r'''tempoTotal < 60'''},
   {"msg": "Use Promise.all",
    "code": r'''/Promise\.all/.test(__code)'''},
 ],
},

{
 "id": "m10l6",
 "title": "Desafio: consumindo uma API",
 "minutes": 12,
 "theory": r"""
## Como é uma chamada de API de verdade

```js
const resposta = await fetch("https://api.exemplo.com/usuarios");
const dados = await resposta.json();
```

- `fetch` devolve uma promise que resolve com a resposta (status, cabeçalhos).
- `.json()` devolve **outra** promise, com o corpo convertido de texto JSON para objeto.
- Erros de rede rejeitam a promise; status como 404 **não** rejeitam — você precisa checar `resposta.ok`.

Nesta lição não acessamos a internet: você vai **simular** uma API com promises e `setTimeout`, que é exatamente o formato do que acontece na vida real.

```js
function buscarUsuario(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id <= 0) reject(new Error("id inválido"));
      else resolve({ id, nome: "Usuário " + id });
    }, 20);
  });
}
```

## Tratando vários de uma vez

```js
const usuarios = await Promise.all(ids.map((id) => buscarUsuario(id)));
```
""",
 "task": r"""
Crie uma API simulada:

1. `buscarUsuario(id)` — promise que resolve, após 20ms, com `{ id, nome: "Usuário " + id }`. Se `id` for menor ou igual a 0, rejeite com `new Error("id inválido")`.
2. `async function listarNomes(ids)` — usa `Promise.all` + `map` para buscar todos e retorna um array só com os nomes.
3. `const nomes = await listarNomes([1, 2, 3]);`
4. `let erroIda = null;` e capture o erro de `buscarUsuario(0)` com `try/catch` em `erroIda` (a mensagem).
""",
 "starter": r"""function buscarUsuario(id) {
  // promise com setTimeout de 20ms
}

async function listarNomes(ids) {
  // Promise.all + map
}

const nomes = await listarNomes([1, 2, 3]);

let erroIda = null;
// try/catch com buscarUsuario(0)

console.log(nomes, erroIda);
""",
 "solution": r"""function buscarUsuario(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id <= 0) {
        reject(new Error("id inválido"));
      } else {
        resolve({ id, nome: `Usuário ${id}` });
      }
    }, 20);
  });
}

async function listarNomes(ids) {
  const usuarios = await Promise.all(ids.map((id) => buscarUsuario(id)));
  return usuarios.map((u) => u.nome);
}

const nomes = await listarNomes([1, 2, 3]);

let erroIda = null;
try {
  await buscarUsuario(0);
} catch (e) {
  erroIda = e.message;
}

console.log(nomes, erroIda);
""",
 "hint": r"""No `listarNomes`: `await Promise.all(ids.map((id) => buscarUsuario(id)))` devolve os objetos; depois use outro `map` para pegar só os nomes.""",
 "tests": [
   {"msg": "nomes deve ser [\"Usuário 1\", \"Usuário 2\", \"Usuário 3\"]",
    "code": r'''JSON.stringify(nomes) === JSON.stringify(["Usuário 1","Usuário 2","Usuário 3"])'''},
   {"msg": "erroIda deve ser \"id inválido\"",
    "code": r'''erroIda === "id inválido" '''},
   {"msg": "buscarUsuario(1) deve resolver com objeto contendo id e nome",
    "code": r'''(async () => { const u = await buscarUsuario(1); return u.id === 1 && u.nome === "Usuário 1"; })()'''},
   {"msg": "buscarUsuario(-1) deve ser rejeitada",
    "code": r'''(async () => { try { await buscarUsuario(-1); return false; } catch (e) { return true; } })()'''},
   {"msg": "Use Promise.all",
    "code": r'''/Promise\.all/.test(__code)'''.replace("'''", "'''")},
 ],
},

]},
# =====================================================================
{
 "id": "es6",
 "title": "JavaScript moderno (ES6+)",
 "icon": "✨",
 "lessons": [

{
 "id": "m11l1",
 "title": "var, let e escopo de bloco",
 "minutes": 8,
 "theory": r"""
## O problema do var

Antes do ES6 só existia `var`, que tem escopo de **função** (ou global), ignorando blocos `{ }`:

```js
if (true) {
  var x = 1;
}
console.log(x);  // 1  ← escapou do bloco!
```

Com `let`:

```js
if (true) {
  let y = 1;
}
console.log(y);  // ReferenceError
```

## O caso clássico: loop com setTimeout

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);   // 3, 3, 3
}

for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log(j), 0);   // 0, 1, 2
}
```

Com `var`, existe **uma** variável `i` compartilhada — quando os callbacks rodam, o loop já terminou e `i` vale 3. Com `let`, cada volta cria uma **nova** variável `j`, e cada callback lembra a sua (closure).

## Temporal Dead Zone

Variáveis `let`/`const` existem no escopo, mas não podem ser acessadas antes da declaração:

```js
console.log(nome);  // ReferenceError
let nome = "Ana";
```

> [tip] Regra de hoje: só use `let` quando o valor mudar; caso contrário, `const`. `var` não se usa mais.
""",
 "task": r"""
1. Crie o array `funcoes` e, com um `for` usando **`let`**, adicione 3 arrow functions que devolvem o próprio índice (`() => i`).
2. Crie `valores` — o resultado de chamar cada função (deve ser `[0, 1, 2]`).
3. Crie `dobrados` — `[0, 2, 4]` usando as mesmas funções com `map` (`f() * 2`).
""",
 "starter": r"""const funcoes = [];

// for com let, empurrando () => i


const valores = funcoes.map((f) => f());
const dobrados = funcoes.map((f) => f() * 2);

console.log(valores, dobrados);
""",
 "solution": r"""const funcoes = [];

for (let i = 0; i < 3; i++) {
  funcoes.push(() => i);
}

const valores = funcoes.map((f) => f());
const dobrados = funcoes.map((f) => f() * 2);

console.log(valores, dobrados);
""",
 "hint": r"""Se você usar `var` no for, todas as funções vão devolver `3` — cada volta com `let` cria uma variável nova.""",
 "tests": [
   {"msg": "valores deve ser [0, 1, 2]",
    "code": r'''JSON.stringify(valores) === JSON.stringify([0,1,2])'''},
   {"msg": "dobrados deve ser [0, 2, 4]",
    "code": r'''JSON.stringify(dobrados) === JSON.stringify([0,2,4])'''},
   {"msg": "Use let no for (não var)",
    "code": r'''/for\s*\(\s*let\s/.test(__code) && !/for\s*\(\s*var\s/.test(__code)'''},
 ],
},

{
 "id": "m11l2",
 "title": "Classes",
 "minutes": 9,
 "theory": r"""
## Molde para objetos

Uma **classe** descreve como criar objetos com as mesmas propriedades e métodos.

```js
class Pessoa {
  constructor(nome, idade) {
    this.nome = nome;
    this.idade = idade;
  }

  apresentar() {
    return `${this.nome}, ${this.idade} anos`;
  }
}

const ana = new Pessoa("Ana", 25);
console.log(ana.apresentar());  // Ana, 25 anos
console.log(ana instanceof Pessoa);  // true
```

- `constructor` roda automaticamente no `new` e recebe os argumentos.
- Métodos ficam no protótipo — compartilhados entre todas as instâncias (economia de memória).
- Sem `new`, uma classe lança erro.

## Propriedades próprias

```js
class Contador {
  total = 0;          // campo de classe (inicializado por instância)

  incrementar() {
    this.total++;
    return this.total;
  }
}
```

> [warn] Métodos de classe **não** são separados por vírgula. Isso não é um objeto literal.
""",
 "task": r"""
Crie a classe `Produto`:

- `constructor(nome, preco)` — guarda as duas propriedades.
- `comDesconto(percentual)` — retorna o preço com desconto (ex.: 10 → preço × 0.9).
- `descricao()` — retorna `` `${nome} custa R$ ${preco}` ``.

Depois:

- `const p1 = new Produto("Teclado", 200);`
- `const precoComDesconto = p1.comDesconto(10);`
""",
 "starter": r"""class Produto {
  constructor(nome, preco) {
    // seu código
  }

  comDesconto(percentual) {
    // seu código
  }

  descricao() {
    // seu código
  }
}

const p1 = new Produto("Teclado", 200);
const precoComDesconto = p1.comDesconto(10);

console.log(precoComDesconto, p1.descricao());
""",
 "solution": r"""class Produto {
  constructor(nome, preco) {
    this.nome = nome;
    this.preco = preco;
  }

  comDesconto(percentual) {
    return this.preco * (1 - percentual / 100);
  }

  descricao() {
    return `${this.nome} custa R$ ${this.preco}`;
  }
}

const p1 = new Produto("Teclado", 200);
const precoComDesconto = p1.comDesconto(10);

console.log(precoComDesconto, p1.descricao());
""",
 "hint": r"""Desconto de 10% = multiplicar por `0.9`, ou seja, `this.preco * (1 - percentual / 100)`.""",
 "tests": [
   {"msg": "p1 deve ser uma instância de Produto com nome e preço",
    "code": r'''p1 instanceof Produto && p1.nome === "Teclado" && p1.preco === 200'''},
   {"msg": "comDesconto(10) deve retornar 180",
    "code": r'''p1.comDesconto(10) === 180 && precoComDesconto === 180'''},
   {"msg": "comDesconto(50) deve retornar 100",
    "code": r'''p1.comDesconto(50) === 100'''},
   {"msg": "descricao() deve mencionar nome e preço",
    "code": r'''p1.descricao().includes("Teclado") && p1.descricao().includes("200")'''},
   {"msg": "Use class e constructor",
    "code": r'''/class\s+Produto/.test(__code) && /constructor\s*\(/.test(__code)'''},
 ],
},

{
 "id": "m11l3",
 "title": "Herança: extends e super",
 "minutes": 9,
 "theory": r"""
## Reaproveitando classes

```js
class Animal {
  constructor(nome) {
    this.nome = nome;
  }

  falar() {
    return `${this.nome} faz um som`;
  }
}

class Cachorro extends Animal {
  constructor(nome, raca) {
    super(nome);        // chama o constructor do pai
    this.raca = raca;
  }

  falar() {             // sobrescreve o método do pai
    return `${this.nome} late: Au au!`;
  }

  buscar() {
    return `${this.nome} foi buscar a bolinha`;
  }
}

const rex = new Cachorro("Rex", "vira-lata");
console.log(rex.falar());   // Rex late: Au au!
console.log(rex.buscar());
console.log(rex instanceof Animal);  // true
```

Três pontos:

1. `extends` declara a herança.
2. `super(...)` no constructor chama o pai — **obrigatório** antes de usar `this`.
3. Métodos com o mesmo nome no filho sobrescrevem os do pai; `super.falar()` chama a versão do pai.
""",
 "task": r"""
Crie:

1. `class Veiculo` com `constructor(marca)` e método `mover()` que retorna `` `${marca} está se movendo` ``.
2. `class Carro extends Veiculo` com `constructor(marca, portas)`: chame `super(marca)`, guarde `portas`, e sobrescreva `mover()` para retornar `` `${marca} está dirigindo com ${portas} portas` ``.
3. `const carro = new Carro("Fiat", 4);`
4. `const movimento = carro.mover();`
""",
 "starter": r"""class Veiculo {
  constructor(marca) {
    // seu código
  }

  mover() {
    // seu código
  }
}

class Carro extends Veiculo {
  constructor(marca, portas) {
    // super + this.portas
  }

  mover() {
    // sobrescreva
  }
}

const carro = new Carro("Fiat", 4);
const movimento = carro.mover();

console.log(movimento, carro instanceof Veiculo);
""",
 "solution": r"""class Veiculo {
  constructor(marca) {
    this.marca = marca;
  }

  mover() {
    return `${this.marca} está se movendo`;
  }
}

class Carro extends Veiculo {
  constructor(marca, portas) {
    super(marca);
    this.portas = portas;
  }

  mover() {
    return `${this.marca} está dirigindo com ${this.portas} portas`;
  }
}

const carro = new Carro("Fiat", 4);
const movimento = carro.mover();

console.log(movimento, carro instanceof Veiculo);
""",
 "hint": r"""`super(marca)` precisa ser a **primeira** linha do constructor do filho.""",
 "tests": [
   {"msg": "carro deve ser instância de Carro e de Veiculo",
    "code": r'''carro instanceof Carro && carro instanceof Veiculo'''},
   {"msg": "carro deve ter marca e portas",
    "code": r'''carro.marca === "Fiat" && carro.portas === 4'''},
   {"msg": "movimento deve ser \"Fiat está dirigindo com 4 portas\"",
    "code": r'''movimento === "Fiat está dirigindo com 4 portas" '''},
   {"msg": "Veiculo.mover() deve continuar funcionando",
    "code": r'''new Veiculo("Bicicleta").mover() === "Bicicleta está se movendo" '''},
   {"msg": "Use extends e super",
    "code": r'''/extends\s+Veiculo/.test(__code) && /super\s*\(/.test(__code)'''},
 ],
},

{
 "id": "m11l4",
 "title": "Getters, setters e static",
 "minutes": 9,
 "theory": r"""
## Propriedades calculadas

`get` cria uma propriedade que parece um valor, mas roda código:

```js
class Circulo {
  constructor(raio) {
    this.raio = raio;
  }

  get area() {
    return Math.PI * this.raio ** 2;
  }

  set diametro(valor) {
    this.raio = valor / 2;
  }
}

const c = new Circulo(2);
console.log(c.area);      // 12.566...  (sem parênteses!)
c.diametro = 10;          // usa o setter
console.log(c.raio);      // 5
```

Note: `get area` é acessado como `c.area`, **não** `c.area()`.

## Por que usar

- Calcular valor derivado sem guardar dado duplicado.
- Validar antes de aceitar (`set idade(v) { if (v < 0) throw ... }`).

## Métodos estáticos

`static` pertence à **classe**, não às instâncias — bom para funções auxiliares:

```js
class Util {
  static somar(a, b) { return a + b; }
}

Util.somar(2, 3);      // 5   (na classe)
new Util().somar;      // undefined (na instância não existe)
```
""",
 "task": r"""
Crie a classe `Temperatura`:

- `constructor(celsius)` guarda `this.celsius`.
- `get fahrenheit()` — retorna `celsius * 9 / 5 + 32`.
- `set fahrenheit(valor)` — converte para celsius e guarda.
- `static deFahrenheit(valor)` — **método estático** que devolve uma nova `Temperatura` a partir de Fahrenheit.

Depois:

- `const t = new Temperatura(30);`
- `const emF = t.fahrenheit;` (86)
- `t.fahrenheit = 212; const celsiusDepois = t.celsius;` (100)
- `const t2 = Temperatura.deFahrenheit(32);` (celsius 0)
""",
 "starter": r"""class Temperatura {
  constructor(celsius) {
    this.celsius = celsius;
  }

  get fahrenheit() {
    // seu código
  }

  set fahrenheit(valor) {
    // seu código
  }

  static deFahrenheit(valor) {
    // seu código
  }
}

const t = new Temperatura(30);
const emF = t.fahrenheit;

t.fahrenheit = 212;
const celsiusDepois = t.celsius;

const t2 = Temperatura.deFahrenheit(32);

console.log(emF, celsiusDepois, t2.celsius);
""",
 "solution": r"""class Temperatura {
  constructor(celsius) {
    this.celsius = celsius;
  }

  get fahrenheit() {
    return (this.celsius * 9) / 5 + 32;
  }

  set fahrenheit(valor) {
    this.celsius = ((valor - 32) * 5) / 9;
  }

  static deFahrenheit(valor) {
    return new Temperatura(((valor - 32) * 5) / 9);
  }
}

const t = new Temperatura(30);
const emF = t.fahrenheit;

t.fahrenheit = 212;
const celsiusDepois = t.celsius;

const t2 = Temperatura.deFahrenheit(32);

console.log(emF, celsiusDepois, t2.celsius);
""",
 "hint": r"""Converter Fahrenheit → Celsius: `(valor - 32) * 5 / 9`. No `get`, acesse sem parênteses: `t.fahrenheit`.""",
 "tests": [
   {"msg": "t.fahrenheit deve ser 86",
    "code": r'''emF === 86'''},
   {"msg": "Definir fahrenheit = 212 deve dar 100 celsius",
    "code": r'''celsiusDepois === 100'''},
   {"msg": "Temperatura.deFahrenheit(32) deve ter celsius 0",
    "code": r'''t2 instanceof Temperatura && t2.celsius === 0'''},
   {"msg": "deFahrenheit deve ser estático",
    "code": r'''typeof Temperatura.deFahrenheit === "function" && t.deFahrenheit === undefined'''},
   {"msg": "Use get, set e static",
    "code": r'''/get\s+fahrenheit/.test(__code) && /set\s+fahrenheit/.test(__code) && /static\s+deFahrenheit/.test(__code)'''},
 ],
},

{
 "id": "m11l5",
 "title": "Map e Set",
 "minutes": 8,
 "theory": r"""
## Set: valores únicos

Um `Set` é uma coleção **sem repetições**:

```js
const s = new Set([1, 2, 2, 3, 3, 3]);
console.log(s);          // Set(3) {1, 2, 3}
console.log(s.size);     // 3

s.add(4);
s.has(2);                // true
s.delete(1);
console.log([...s]);     // [2, 3, 4]
```

Truque famoso para remover duplicados de um array:

```js
const unicos = [...new Set([1, 2, 2, 3])];   // [1, 2, 3]
```

## Map: dicionário com chaves de qualquer tipo

`Map` é parecido com objeto, mas aceita qualquer chave (número, objeto, função) e mantém a ordem de inserção:

```js
const m = new Map();
m.set("ana", 9);
m.set("bruno", 7);

m.get("ana");      // 9
m.has("bruno");    // true
m.size;            // 2

for (const [chave, valor] of m) {
  console.log(chave, valor);
}
```

## Contando ocorrências

```js
const contagem = new Map();

for (const p of ["uva", "maçã", "uva"]) {
  contagem.set(p, (contagem.get(p) || 0) + 1);
}
// Map { "uva" => 2, "maçã" => 1 }
```

> [tip] Escolha: `Map` quando as chaves são dinâmicas ou não são texto; objeto literal para estruturas fixas com `chave: valor`.
""",
 "task": r"""
Você tem `const frutas = ["uva", "maçã", "uva", "pera", "uva", "maçã"];`.

Crie:

1. `unicas` — array só com frutas únicas, na ordem de aparição (use `Set` + spread).
2. `contagem` — um `Map` com quantas vezes cada fruta aparece.
3. `maisFrequente` — a fruta que mais aparece (`"uva"`), percorrendo o Map.
4. `quantidadeUva` — `contagem.get("uva")`.
""",
 "starter": r"""const frutas = ["uva", "maçã", "uva", "pera", "uva", "maçã"];

// 1. unicas
// 2. contagem com Map
// 3. maisFrequente
// 4. quantidadeUva


console.log(unicas, contagem, maisFrequente, quantidadeUva);
""",
 "solution": r"""const frutas = ["uva", "maçã", "uva", "pera", "uva", "maçã"];

const unicas = [...new Set(frutas)];

const contagem = new Map();
for (const f of frutas) {
  contagem.set(f, (contagem.get(f) || 0) + 1);
}

let maisFrequente = null;
let maior = 0;
for (const [fruta, qtd] of contagem) {
  if (qtd > maior) {
    maior = qtd;
    maisFrequente = fruta;
  }
}

const quantidadeUva = contagem.get("uva");

console.log(unicas, contagem, maisFrequente, quantidadeUva);
""",
 "hint": r"""`contagem.get(f) || 0` resolve o primeiro caso, quando a chave ainda não existe.""",
 "tests": [
   {"msg": "unicas deve ser [\"uva\", \"maçã\", \"pera\"]",
    "code": r'''JSON.stringify(unicas) === JSON.stringify(["uva","maçã","pera"])'''},
   {"msg": "contagem deve ser um Map com 3 chaves",
    "code": r'''contagem instanceof Map && contagem.size === 3 && contagem.get("uva") === 3 && contagem.get("pera") === 1'''},
   {"msg": "maisFrequente deve ser \"uva\"",
    "code": r'''maisFrequente === "uva" '''},
   {"msg": "quantidadeUva deve ser 3",
    "code": r'''quantidadeUva === 3'''},
   {"msg": "Use Set e Map",
    "code": r'''/new Set/.test(__code) && /new Map/.test(__code)'''},
 ],
},

{
 "id": "m11l6",
 "title": "Sintaxe moderna do dia a dia",
 "minutes": 9,
 "theory": r"""
## Optional chaining (?.)

Acessa propriedades com segurança quando algo pode ser `null`/`undefined`:

```js
const usuario = null;

usuario.nome;         // TypeError: Cannot read properties of null
usuario?.nome;        // undefined  (sem erro)
usuario?.endereco?.rua;  // undefined
usuario?.falar?.();   // undefined (nem tenta chamar)
```

## Nullish coalescing (??)

`??` devolve o lado direito apenas quando o esquerdo é `null` ou `undefined`:

```js
0 || "padrão";    // "padrão"  ← 0 é falsy, resultado errado em muitos casos
0 ?? "padrão";    // 0         ← correto
"" ?? "padrão";   // ""
null ?? "padrão"; // "padrão"
```

Diferença essencial em relação ao `||`: `0`, `""` e `false` são valores válidos.

## Atribuição com ??=

```js
let config = {};
config.tema ??= "escuro";   // define só se estiver null/undefined
```

## Rest e spread de novo

```js
const { a, ...resto } = { a: 1, b: 2, c: 3 };   // resto = { b: 2, c: 3 }
function f(...args) {}                          // args = array
const copia = [...lista, novoItem];
```

> [tip] Esses operadores são o "cinto de segurança" do código moderno: menos `if (obj && obj.x ...)` e menos bugs com valores falsy.
""",
 "task": r"""
Você tem:

```js
const usuario = { nome: "Ana", endereco: null };
const config = { tema: "", fonte: null };
```

Crie:

- `rua` — tentativa de acessar `usuario.endereco.rua` **sem erro**, usando `?.` (deve ser `undefined`).
- `tema` — `config.tema ?? "claro"` (deve ser `""`, pois string vazia não é nullish).
- `fonte` — `config.fonte ?? "16px"` (deve ser `"16px"`).
- `{ nome, ...restoUsuario }` a partir de `usuario` — e use `Object.keys(restoUsuario)`.
- `comPadrao` — usando `??=`: comece com `let apelido;` e aplique `apelido ??= "anônimo"`.
""",
 "starter": r"""const usuario = { nome: "Ana", endereco: null };
const config = { tema: "", fonte: null };

// crie as variáveis


console.log(rua, tema, fonte, chavesResto, apelido);
""",
 "solution": r"""const usuario = { nome: "Ana", endereco: null };
const config = { tema: "", fonte: null };

const rua = usuario?.endereco?.rua;
const tema = config.tema ?? "claro";
const fonte = config.fonte ?? "16px";
const { nome, ...restoUsuario } = usuario;
const chavesResto = Object.keys(restoUsuario);

let apelido;
apelido ??= "anônimo";

console.log(rua, tema, fonte, chavesResto, apelido);
""",
 "hint": r"""`usuario?.endereco?.rua` devolve `undefined` sem quebrar. Já `config.tema ?? "claro"` mantém `""`, porque `""` não é nullish.""",
 "tests": [
   {"msg": "rua deve ser undefined",
    "code": r'''rua === undefined'''},
   {"msg": "tema deve ser \"\" (string vazia não é nullish)",
    "code": r'''tema === "" '''},
   {"msg": "fonte deve ser \"16px\"",
    "code": r'''fonte === "16px" '''},
   {"msg": "chavesResto deve ser [\"endereco\"]",
    "code": r'''JSON.stringify(chavesResto) === JSON.stringify(["endereco"])'''},
   {"msg": "apelido deve ser \"anônimo\"",
    "code": r'''apelido === "anônimo" '''},
   {"msg": "Use ?. e ??",
    "code": r'''/\?\./.test(__code) && /\?\?/.test(__code)'''},
 ],
},

]},
# =====================================================================
{
 "id": "projetos",
 "title": "Projetos finais",
 "icon": "🏆",
 "lessons": [

{
 "id": "m12l1",
 "title": "Projeto: validador de senha",
 "minutes": 12,
 "theory": r"""
## Regras de negócio viram código

Validador de senha é um clássico porque junta tudo: funções, strings, condicionais, arrays e objetos de resultado.

```js
function validarSenha(senha) {
  const erros = [];

  if (senha.length < 8) erros.push("Mínimo de 8 caracteres");
  if (!/[A-Z]/.test(senha)) erros.push("Falta uma letra maiúscula");
  if (!/[0-9]/.test(senha)) erros.push("Falta um número");

  return { valida: erros.length === 0, erros };
}
```

`/[A-Z]/` é uma expressão regular: "existe alguma letra de A a Z?". `\d` é o mesmo que `[0-9]`.

## Por que devolver erros

Devolver uma **lista** de problemas permite mostrar tudo o que falta de uma vez, em vez de um por vez. Melhor experiência para quem usa.
""",
 "task": r"""
Crie a função `validarSenha(senha)` que devolve `{ valida, erros }`, onde `erros` é um array de mensagens:

- `"Mínimo de 8 caracteres"` se `senha.length < 8`
- `"Falta uma letra maiúscula"` se não houver `/A-Z/`
- `"Falta uma letra minúscula"` se não houver `/a-z/`
- `"Falta um número"` se não houver `/0-9/`

Depois teste com:

- `const fraca = validarSenha("abc");`
- `const forte = validarSenha("Senha123");`
""",
 "starter": r"""function validarSenha(senha) {
  const erros = [];

  // adicione as verificações

  return { valida: erros.length === 0, erros };
}

const fraca = validarSenha("abc");
const forte = validarSenha("Senha123");

console.log(fraca, forte);
""",
 "solution": r"""function validarSenha(senha) {
  const erros = [];

  if (senha.length < 8) erros.push("Mínimo de 8 caracteres");
  if (!/[A-Z]/.test(senha)) erros.push("Falta uma letra maiúscula");
  if (!/[a-z]/.test(senha)) erros.push("Falta uma letra minúscula");
  if (!/[0-9]/.test(senha)) erros.push("Falta um número");

  return { valida: erros.length === 0, erros };
}

const fraca = validarSenha("abc");
const forte = validarSenha("Senha123");

console.log(fraca, forte);
""",
 "hint": r"""`/[A-Z]/.test(senha)` devolve `true` se houver maiúscula. O `!` inverte: se **não** houver, adicione o erro.""",
 "tests": [
   {"msg": "validarSenha(\"Senha123\") deve ser válida",
    "code": r'''forte.valida === true && forte.erros.length === 0'''},
   {"msg": "validarSenha(\"abc\") deve acumular 3 erros",
    "code": r'''fraca.valida === false && fraca.erros.length === 3'''},
   {"msg": "Os erros da senha fraca devem mencionar tamanho, maiúscula e número",
    "code": r'''fraca.erros.join(" | ").includes("8 caracteres") && fraca.erros.join(" | ").includes("maiúscula") && fraca.erros.join(" | ").includes("número")'''},
   {"msg": "Deve reprovar senha sem número",
    "code": r'''validarSenha("SenhaLonga").valida === false'''},
   {"msg": "Deve reprovar senha sem maiúscula",
    "code": r'''validarSenha("senha123").erros.join().includes("maiúscula")'''},
 ],
},

{
 "id": "m12l2",
 "title": "Projeto: análise de frase",
 "minutes": 12,
 "theory": r"""
## Do texto ao relatório

Um analisador de texto devolve estatísticas: número de palavras, palavra mais longa, média de letras, palavras repetidas.

```js
const frase = "o rato roeu a roupa";

const palavras = frase.toLowerCase().split(" ");
const total = palavras.length;
const tamanhos = palavras.map((p) => p.length);
const media = tamanhos.reduce((a, b) => a + b, 0) / total;
```

Cada linha transforma o dado um pouco. É assim que se pensa em JavaScript moderno: **pipeline** de transformações.

## Ordenando por critério

```js
const ordenadas = [...palavras].sort((a, b) => b.length - a.length);
const maisLonga = ordenadas[0];
```
""",
 "task": r"""
Você tem:

```js
const frase = "JavaScript é uma linguagem de programação muito popular";
```

Monte o objeto `relatorio` com:

- `totalPalavras` — quantas palavras (separe por espaço).
- `palavraMaisLonga` — a palavra com mais letras.
- `mediaLetras` — média de letras por palavra, arredondada para 1 casa (`toFixed(1)`) e convertida para número com `Number`.
- `palavrasUnicas` — quantas palavras diferentes existem (use `Set`).
- `temJavaScript` — booleano: aparece `"javascript"` (sem diferenciar maiúsculas).
""",
 "starter": r"""const frase = "JavaScript é uma linguagem de programação muito popular";

const palavras = frase.toLowerCase().split(" ");

const relatorio = {
  totalPalavras: 0,
  palavraMaisLonga: "",
  mediaLetras: 0,
  palavrasUnicas: 0,
  temJavaScript: false,
};

console.log(relatorio);
""",
 "solution": r"""const frase = "JavaScript é uma linguagem de programação muito popular";

const palavras = frase.toLowerCase().split(" ");

const totalPalavras = palavras.length;
const ordenadas = [...palavras].sort((a, b) => b.length - a.length);
const somaLetras = palavras.reduce((soma, p) => soma + p.length, 0);

const relatorio = {
  totalPalavras,
  palavraMaisLonga: ordenadas[0],
  mediaLetras: Number((somaLetras / totalPalavras).toFixed(1)),
  palavrasUnicas: new Set(palavras).size,
  temJavaScript: palavras.includes("javascript"),
};

console.log(relatorio);
""",
 "hint": r"""`new Set(palavras).size` conta valores distintos. A palavra mais longa é a primeira depois de ordenar por tamanho decrescente.""",
 "tests": [
   {"msg": "totalPalavras deve ser 9",
    "code": r'''relatorio.totalPalavras === 8'''},
   {"msg": "palavraMaisLonga deve ser \"programação\"",
    "code": r'''relatorio.palavraMaisLonga === "programação" '''},
   {"msg": "mediaLetras deve ser 6.1",
    "code": r'''relatorio.mediaLetras === 6'''},
   {"msg": "palavrasUnicas deve ser 9",
    "code": r'''relatorio.palavrasUnicas === 8'''},
   {"msg": "temJavaScript deve ser true",
    "code": r'''relatorio.temJavaScript === true'''},
 ],
},

{
 "id": "m12l3",
 "title": "Projeto: lista de tarefas (lógica)",
 "minutes": 14,
 "theory": r"""
## Um mini CRUD

CRUD = Create, Read, Update, Delete. É o esqueleto de quase todo sistema.

```js
const tarefas = [];

function adicionar(texto) {
  tarefas.push({ id: tarefas.length + 1, texto, concluida: false });
}

function concluir(id) {
  const t = tarefas.find((t) => t.id === id);
  if (t) t.concluida = true;
}

function remover(id) {
  const i = tarefas.findIndex((t) => t.id === id);
  if (i > -1) tarefas.splice(i, 1);
}

function listar() {
  return tarefas.filter((t) => !t.concluida).map((t) => t.texto);
}
```

`findIndex` devolve a posição (ou -1) e `splice(i, 1)` remove 1 item a partir dela — este é o `splice` que **altera** o array (diferente do `slice`).

## Por que funções separadas

Cada função faz **uma** coisa. Fica fácil testar, reutilizar e corrigir.
""",
 "task": r"""
Você tem um array `tarefas` vazio e deve criar:

- `adicionar(texto)` — adiciona `{ id, texto, concluida: false }`, com `id` sequencial começando em 1.
- `concluir(id)` — marca a tarefa como concluída.
- `remover(id)` — remove a tarefa pelo id (`findIndex` + `splice`).
- `pendentes()` — retorna só os textos das tarefas não concluídas.

Depois execute, nesta ordem:

1. `adicionar("Estudar")`
2. `adicionar("Praticar")`
3. `adicionar("Revisar")`
4. `concluir(2)`
5. `remover(3)`
""",
 "starter": r"""const tarefas = [];

function adicionar(texto) {
  // seu código
}

function concluir(id) {
  // seu código
}

function remover(id) {
  // seu código
}

function pendentes() {
  // seu código
}

adicionar("Estudar");
adicionar("Praticar");
adicionar("Revisar");
concluir(2);
remover(3);

console.log(tarefas, pendentes());
""",
 "solution": r"""const tarefas = [];

function adicionar(texto) {
  tarefas.push({ id: tarefas.length + 1, texto, concluida: false });
}

function concluir(id) {
  const tarefa = tarefas.find((t) => t.id === id);
  if (tarefa) tarefa.concluida = true;
}

function remover(id) {
  const indice = tarefas.findIndex((t) => t.id === id);
  if (indice > -1) tarefas.splice(indice, 1);
}

function pendentes() {
  return tarefas.filter((t) => !t.concluida).map((t) => t.texto);
}

adicionar("Estudar");
adicionar("Praticar");
adicionar("Revisar");
concluir(2);
remover(3);

console.log(tarefas, pendentes());
""",
 "hint": r"""Cuidado com o `id` depois de remover: use `tarefas.length + 1` como fizemos aqui ou mantenha um contador separado.""",
 "tests": [
   {"msg": "Devem restar 2 tarefas após concluir e remover",
    "code": r'''tarefas.length === 2'''},
   {"msg": "A tarefa 1 deve estar pendente e a 2 concluída",
    "code": r'''tarefas[0].id === 1 && tarefas[0].concluida === false && tarefas[1].id === 2 && tarefas[1].concluida === true'''},
   {"msg": "pendentes() deve retornar [\"Estudar\"]",
    "code": r'''JSON.stringify(pendentes()) === JSON.stringify(["Estudar"])'''},
   {"msg": "remover(1) deve funcionar em tarefa existente",
    "code": r'''(function(){ const copia = [...tarefas]; tarefas.length = 0; tarefas.push(...copia); remover(1); const ok = tarefas.length === 1 && tarefas[0].id === 2; tarefas.length = 0; tarefas.push(...copia); return ok; })()'''},
   {"msg": "Use findIndex e splice",
    "code": r'''/findIndex/.test(__code) && /splice/.test(__code)'''},
 ],
},

{
 "id": "m12l4",
 "title": "Projeto: lista de tarefas no DOM",
 "minutes": 15,
 "html": r"""<h2>Minhas tarefas</h2>
<input id="campo" placeholder="Nova tarefa">
<button id="adicionar">Adicionar</button>
<ul id="lista"></ul>
<p id="resumo"></p>""",
 "theory": r"""
## Juntando DOM + arrays + eventos

Agora o CRUD ganha interface. O padrão profissional é:

1. **Estado**: um array com os dados (`tarefas`).
2. **Renderização**: uma função que redesenha a lista a partir do estado.
3. **Ações**: eventos alteram o estado e chamam a renderização.

```js
const tarefas = [];

function renderizar() {
  lista.innerHTML = "";
  tarefas.forEach((t) => {
    const li = document.createElement("li");
    li.textContent = t.texto;
    lista.appendChild(li);
  });
}
```

Assim a tela **sempre** reflete os dados. Você nunca atualiza a tela "na mão" em vários lugares diferentes — só muda o estado e re-renderiza. (É exatamente a ideia por trás de React, Vue e Angular.)
""",
 "task": r"""
Na página ao lado existem `input#campo`, `button#adicionar`, `ul#lista` e `p#resumo`.

Implemente:

1. `const tarefas = []` e uma função `renderizar()` que:
   - limpa a lista,
   - recria um `li` por tarefa,
   - atualiza o `#resumo` com `` `${tarefas.length} tarefa(s)` ``.
2. No clique do botão: leia `campo.value.trim()`; se não estiver vazio, adicione ao array, limpe o campo e chame `renderizar()`.
3. Chame `renderizar()` uma vez no início.
""",
 "starter": r"""const campo = document.getElementById("campo");
const botaoAdicionar = document.getElementById("adicionar");
const lista = document.getElementById("lista");
const resumo = document.getElementById("resumo");

const tarefas = [];

function renderizar() {
  // limpe a lista, crie os li e atualize o resumo
}

botaoAdicionar.addEventListener("click", () => {
  // adicione a tarefa
});

renderizar();
""",
 "solution": r"""const campo = document.getElementById("campo");
const botaoAdicionar = document.getElementById("adicionar");
const lista = document.getElementById("lista");
const resumo = document.getElementById("resumo");

const tarefas = [];

function renderizar() {
  lista.innerHTML = "";

  tarefas.forEach((texto) => {
    const li = document.createElement("li");
    li.textContent = texto;
    lista.appendChild(li);
  });

  resumo.textContent = `${tarefas.length} tarefa(s)`;
}

botaoAdicionar.addEventListener("click", () => {
  const valor = campo.value.trim();
  if (valor === "") return;

  tarefas.push(valor);
  campo.value = "";
  renderizar();
});

renderizar();
""",
 "hint": r"""A ordem importa: adicione ao array, limpe o campo e **depois** chame `renderizar()`.""",
 "tests": [
   {"msg": "Ao começar, o resumo deve mostrar 0 tarefa(s)",
    "code": r'''document.getElementById("resumo").textContent === "0 tarefa(s)" '''},
   {"msg": "Adicionar uma tarefa deve criar um li na lista",
    "code": r'''(function(){ const c = document.getElementById("campo"); c.value = "Comprar pão"; document.getElementById("adicionar").click(); return document.querySelectorAll("#lista li").length === 1 && document.querySelector("#lista li").textContent === "Comprar pão"; })()'''},
   {"msg": "O resumo deve ser atualizado",
    "code": r'''document.getElementById("resumo").textContent === "1 tarefa(s)" '''},
   {"msg": "O campo deve ser limpo depois de adicionar",
    "code": r'''document.getElementById("campo").value === "" '''},
   {"msg": "Campo vazio não deve adicionar tarefa",
    "code": r'''(function(){ const c = document.getElementById("campo"); c.value = "   "; document.getElementById("adicionar").click(); return document.querySelectorAll("#lista li").length === 1; })()'''},
   {"msg": "Adicionar mais uma deve resultar em 2 itens",
    "code": r'''(function(){ const c = document.getElementById("campo"); c.value = "Estudar JS"; document.getElementById("adicionar").click(); return document.querySelectorAll("#lista li").length === 2; })()'''},
 ],
},

{
 "id": "m12l5",
 "title": "Projeto: quiz de programação",
 "minutes": 14,
 "theory": r"""
## Dados + lógica de jogo

Um quiz é um array de perguntas e um placar. A lógica é curta; o valor está na organização dos dados.

```js
const perguntas = [
  { pergunta: "Quanto é 2 + 2?", alternativas: ["3", "4", "5"], correta: 1 },
];

function responder(quiz, indicePergunta, indiceResposta) {
  const p = quiz[indicePergunta];
  return indiceResposta === p.correta;
}
```

## Um placar funcional

```js
function corrigir(quiz, respostas) {
  const acertos = quiz.filter((p, i) => respostas[i] === p.correta).length;
  return {
    acertos,
    total: quiz.length,
    percentual: Math.round((acertos / quiz.length) * 100),
    aprovado: acertos / quiz.length >= 0.6,
  };
}
```

`filter` com o índice (segundo parâmetro do callback) é o truque para comparar duas listas em paralelo.

## Fechando o curso

Você já usou aqui: objetos, arrays, `map`, `filter`, `reduce`, arrow functions, template strings, `Math` e funções. É exatamente o repertório de quem programa em JavaScript de verdade.
""",
 "task": r"""
Você tem `const quiz` com 4 perguntas (array de objetos com `pergunta`, `alternativas` e `correta`).

Crie:

1. `corrigir(quiz, respostas)` — devolve `{ acertos, total, percentual, aprovado }`
   (`aprovado` se o percentual for 60% ou mais).
2. `const respostas = [1, 1, 2, 1];` (uma resposta por pergunta).
3. `const resultado = corrigir(quiz, respostas);`
4. `const gabarito = quiz.map((p) => p.correta);`
""",
 "starter": r"""const quiz = [
  { pergunta: "Qual palavra cria uma constante?", alternativas: ["let", "const", "var"], correta: 1 },
  { pergunta: "O que 10 % 3 retorna?", alternativas: ["3", "1", "0"], correta: 1 },
  { pergunta: "Qual método transforma itens?", alternativas: ["filter", "find", "map"], correta: 2 },
  { pergunta: "Qual tipo typeof 42 retorna?", alternativas: ["number", "string", "int"], correta: 0 },
];

function corrigir(quiz, respostas) {
  // seu código
}

const respostas = [1, 1, 2, 1];
const resultado = corrigir(quiz, respostas);
const gabarito = quiz.map((p) => p.correta);

console.log(resultado, gabarito);
""",
 "solution": r"""const quiz = [
  { pergunta: "Qual palavra cria uma constante?", alternativas: ["let", "const", "var"], correta: 1 },
  { pergunta: "O que 10 % 3 retorna?", alternativas: ["3", "1", "0"], correta: 1 },
  { pergunta: "Qual método transforma itens?", alternativas: ["filter", "find", "map"], correta: 2 },
  { pergunta: "Qual tipo typeof 42 retorna?", alternativas: ["number", "string", "int"], correta: 0 },
];

function corrigir(quiz, respostas) {
  const acertos = quiz.filter((p, i) => respostas[i] === p.correta).length;
  const total = quiz.length;
  const percentual = Math.round((acertos / total) * 100);

  return {
    acertos,
    total,
    percentual,
    aprovado: percentual >= 60,
  };
}

const respostas = [1, 1, 2, 1];
const resultado = corrigir(quiz, respostas);
const gabarito = quiz.map((p) => p.correta);

console.log(resultado, gabarito);
""",
 "hint": r"""Com `respostas = [1, 1, 2, 1]` você acerta 3 de 4 (75%): a última resposta deveria ser 0, não 1.""",
 "tests": [
   {"msg": "resultado.acertos deve ser 3",
    "code": r'''resultado.acertos === 3'''},
   {"msg": "resultado.total deve ser 4",
    "code": r'''resultado.total === 4'''},
   {"msg": "resultado.percentual deve ser 75",
    "code": r'''resultado.percentual === 75'''},
   {"msg": "resultado.aprovado deve ser true",
    "code": r'''resultado.aprovado === true'''},
   {"msg": "gabarito deve ser [1, 1, 2, 0]",
    "code": r'''JSON.stringify(gabarito) === JSON.stringify([1,1,2,0])'''},
   {"msg": "corrigir deve reprovar com menos de 60%",
    "code": r'''corrigir(quiz, [0, 0, 0, 0]).aprovado === false'''},
 ],
},

{
 "id": "m12l6",
 "title": "Desafio final: sistema de notas",
 "minutes": 18,
 "theory": r"""
## O exame final

Este é o desafio que reúne tudo o que vimos no curso. Leia com calma, divida em partes e resolva uma de cada vez. É assim que se resolve problema grande: **quebrando em problemas pequenos**.

```js
const alunos = [
  { nome: "Ana", notas: [9, 8.5, 10] },
  { nome: "Bruno", notas: [6, 5.5, 7] },
];
```

O que precisamos:

1. A **média** de cada aluno: `reduce` + `length`.
2. A **situação** de cada aluno: `if/else` ou ternário.
3. A **média da turma**: outra média sobre as médias.
4. Listas derivadas: aprovados, ordenação por média.

Não existe uma única resposta certa. Se os testes passarem e o código estiver legível, você acertou.
""",
 "task": r"""
Você tem:

```js
const alunos = [
  { nome: "Ana", notas: [9, 8.5, 10] },
  { nome: "Bruno", notas: [6, 5.5, 7] },
  { nome: "Carla", notas: [4, 6, 5] },
  { nome: "Davi", notas: [10, 9.5, 9] },
];
```

Crie:

1. `medias` — array de objetos `{ nome, media }` (média arredondada para 1 casa, como número).
2. `situacoes` — array de objetos `{ nome, media, situacao }` com situação:
   - `"Aprovado"` se média ≥ 7
   - `"Recuperação"` se média ≥ 5 e < 7
   - `"Reprovado"` se < 5
3. `mediaTurma` — média das médias, com 1 casa decimal (número).
4. `aprovados` — nomes dos aprovados.
5. `melhorAluno` — o nome do aluno com maior média.
6. `ordenados` — `situacoes` ordenadas da maior média para a menor (sem alterar `situacoes`).
""",
 "starter": r"""const alunos = [
  { nome: "Ana", notas: [9, 8.5, 10] },
  { nome: "Bruno", notas: [6, 5.5, 7] },
  { nome: "Carla", notas: [4, 6, 5] },
  { nome: "Davi", notas: [10, 9.5, 9] },
];

// 1. medias
// 2. situacoes
// 3. mediaTurma
// 4. aprovados
// 5. melhorAluno
// 6. ordenados


console.log(medias, situacoes, mediaTurma, aprovados, melhorAluno);
""",
 "solution": r"""const alunos = [
  { nome: "Ana", notas: [9, 8.5, 10] },
  { nome: "Bruno", notas: [6, 5.5, 7] },
  { nome: "Carla", notas: [4, 6, 5] },
  { nome: "Davi", notas: [10, 9.5, 9] },
];

const calcularMedia = (notas) =>
  Number((notas.reduce((soma, n) => soma + n, 0) / notas.length).toFixed(1));

const medias = alunos.map((a) => ({
  nome: a.nome,
  media: calcularMedia(a.notas),
}));

const situacoes = medias.map((m) => ({
  nome: m.nome,
  media: m.media,
  situacao: m.media >= 7 ? "Aprovado" : m.media >= 5 ? "Recuperação" : "Reprovado",
}));

const mediaTurma = Number(
  (medias.reduce((soma, m) => soma + m.media, 0) / medias.length).toFixed(1)
);

const aprovados = situacoes.filter((s) => s.situacao === "Aprovado").map((s) => s.nome);

const melhorAluno = medias.reduce((melhor, m) => (m.media > melhor.media ? m : melhor)).nome;

const ordenados = [...situacoes].sort((a, b) => b.media - a.media);

console.log(medias, situacoes, mediaTurma, aprovados, melhorAluno, ordenados);
""",
 "hint": r"""Crie uma função auxiliar `calcularMedia(notas)` para não repetir a conta. Nas `situacoes`, use ternário encadeado com cuidado na ordem: primeiro `>= 7`, depois `>= 5`.""",
 "tests": [
   {"msg": "medias deve ter as 4 médias corretas",
    "code": r'''JSON.stringify(medias) === JSON.stringify([{nome:"Ana",media:9.2},{nome:"Bruno",media:6.2},{nome:"Carla",media:5},{nome:"Davi",media:9.5}])'''},
   {"msg": "situacoes deve classificar Ana e Davi como Aprovado",
    "code": r'''situacoes[0].situacao === "Aprovado" && situacoes[3].situacao === "Aprovado" && situacoes[1].situacao === "Recuperação" '''},
   {"msg": "Carla deve estar em Recuperação (média 5)",
    "code": r'''situacoes[2].situacao === "Recuperação" '''},
   {"msg": "mediaTurma deve ser 7.5",
    "code": r'''mediaTurma === 7.5'''},
   {"msg": "aprovados deve ser [\"Ana\", \"Davi\"]",
    "code": r'''JSON.stringify(aprovados) === JSON.stringify(["Ana","Davi"])'''},
   {"msg": "melhorAluno deve ser \"Davi\"",
    "code": r'''melhorAluno === "Davi" '''},
   {"msg": "ordenados deve começar com Davi e terminar com Carla",
    "code": r'''ordenados[0].nome === "Davi" && ordenados[3].nome === "Carla" && ordenados.length === 4'''},
   {"msg": "situacoes não pode ter sido reordenado",
    "code": r'''situacoes[0].nome === "Ana" '''},
 ],
},

]},
]
