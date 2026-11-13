# -*- coding: utf-8 -*-
"""Módulos 1 a 3 — Fundamentos, lógica e funções."""

MODULE_A = None

MODULES = [

# =====================================================================
{
 "id": "intro",
 "title": "Introdução ao JavaScript",
 "icon": "🚀",
 "lessons": [

{
 "id": "m1l1",
 "title": "Seu primeiro código",
 "minutes": 5,
 "theory": r"""
## Bem-vindo ao curso

JavaScript é a linguagem de programação da web. Ela roda no seu navegador agora mesmo — e também em servidores (com Node.js), aplicativos, jogos e até robôs.

Neste curso você escreve código de verdade desde a primeira lição. O painel da direita é um editor real: você digita, executa e vê o resultado na hora. Não existe botão de "assistir vídeo" — aqui se aprende fazendo.

## console.log

A instrução mais usada por quem está começando é `console.log()`. Ela **imprime** um valor no console, que é o painel onde os programadores observam o que o programa está fazendo.

```js
console.log("Olá, mundo!");
// Console:  Olá, mundo!
```

Você pode imprimir qualquer coisa: textos (entre aspas), números, resultados de contas e variáveis.

```js
console.log(2 + 2);        // 4
console.log("2 + 2");      // 2 + 2  (entre aspas é texto!)
```

> [tip] O console é o seu melhor amigo. Sempre que quiser saber o valor de algo, imprima.
""",
 "task": r"""
Escreva **duas linhas** usando `console.log`:

1. A mensagem `Olá, mundo!`
2. Uma segunda linha com o seu nome (ou o que você quiser)
""",
 "starter": r"""// Escreva seu primeiro código abaixo

""",
 "solution": r"""console.log("Olá, mundo!");
console.log("Meu nome é Ana");
""",
 "hint": r"""Texto sempre entre aspas: `console.log("Olá, mundo!");` — e não esqueça do ponto e vírgula no final (ele é opcional em JavaScript, mas ajuda a organizar).""",
 "tests": [
   {"msg": "Você deve imprimir a mensagem Olá, mundo! com console.log",
    "code": r"""__normalize(__printed()).includes("olá, mundo")"""},
   {"msg": "Imprima pelo menos duas linhas no console",
    "code": r"""__logs.length >= 2"""},
 ],
},

{
 "id": "m1l2",
 "title": "Variáveis: let e const",
 "minutes": 6,
 "theory": r"""
## Guardando valores

Uma **variável** é um espaço com nome para guardar um valor. Em JavaScript moderno existem duas palavras-chave para criar variáveis:

- `const` — valor que **não** será trocado (constante). Use sempre que puder.
- `let` — valor que **pode** mudar durante o programa.

```js
const nome = "Ana";
let idade = 25;

idade = 26;              // ok, let pode mudar
console.log(nome, idade); // Ana 26
```

Se você tentar trocar uma `const`, o JavaScript reclama:

```js
const pi = 3.14;
pi = 3;   // TypeError: Assignment to constant variable.
```

> [warn] Evite `var`: é a forma antiga, tem regras de escopo confusas e hoje só aparece em código legado.

## Nomes de variáveis

Use nomes descritivos, sem espaços nem acentos, começando com letra, `_` ou `$`. O padrão da comunidade é **camelCase**: `nomeCompleto`, `precoTotal`, `idadeMinima`.
""",
 "task": r"""
Crie duas variáveis:

- `nome` — uma **constante** (`const`) com o seu nome, como texto.
- `idade` — uma variável (`let`) com a sua idade, como **número** (sem aspas).

No final, imprima as duas com `console.log(nome, idade)`.
""",
 "starter": r"""// 1. Crie a constante `nome`


// 2. Crie a variável `idade`


// 3. Imprima as duas

""",
 "solution": r"""const nome = "Ana";
let idade = 25;

console.log(nome, idade);
""",
 "hint": r"""Número não leva aspas: `let idade = 25;` (com aspas viraria texto `"25"`).""",
 "tests": [
   {"msg": "Crie uma variável chamada nome",
    "code": r"""typeof nome !== "undefined" """},
   {"msg": "nome deve ser um texto (string) não vazio",
    "code": r"""typeof nome === "string" && nome.trim().length > 0"""},
   {"msg": "Crie uma variável chamada idade",
    "code": r"""typeof idade !== "undefined" """},
   {"msg": "idade deve ser um número",
    "code": r"""typeof idade === "number" && Number.isFinite(idade)"""},
   {"msg": "Use let para a idade (ela vai poder mudar)",
    "code": r"""/\blet\s+idade\b/.test(__code)"""},
   {"msg": "Use const para o nome",
    "code": r"""/\bconst\s+nome\b/.test(__code)"""},
 ],
},

{
 "id": "m1l3",
 "title": "Tipos de dados",
 "minutes": 7,
 "theory": r"""
## Os tipos primitivos

JavaScript tem poucos tipos básicos, e você vai usar quase sempre os quatro primeiros:

| Tipo | Exemplos | Para que serve |
|---|---|---|
| `string` | `"Ana"`, `'oi'`, `` `tchau` `` | textos |
| `number` | `10`, `-3.5`, `0.1` | números (inteiros e decimais) |
| `boolean` | `true`, `false` | sim/não, ligado/desligado |
| `undefined` | `undefined` | "ainda não tem valor" |
| `null` | `null` | "vazio, de propósito" |
| `object` | `{}`, `[]` | estruturas (vêm mais adiante) |

## Descobrindo o tipo com typeof

O operador `typeof` devolve o tipo de um valor, como texto:

```js
console.log(typeof "Ana");   // string
console.log(typeof 42);      // number
console.log(typeof true);    // boolean
console.log(typeof undefined); // undefined
console.log(typeof null);    // object  ← peculiaridade histórica do JS
```

> [warn] `typeof null` devolve `"object"`. É um bug antigo da linguagem que nunca foi corrigido. Guarde isso: `null` é um primitivo.
""",
 "task": r"""
Crie quatro variáveis:

- `produto` — texto: `"Caneta"`.
- `preco` — número: `2.5`.
- `disponivel` — booleano: `true`.
- `desconto` — uma variável **sem valor** (use `let` e não atribua nada).

Depois imprima `typeof` de cada uma.
""",
 "starter": r"""// Crie as quatro variáveis


// Imprima os tipos
console.log(typeof produto);

""",
 "solution": r"""const produto = "Caneta";
const preco = 2.5;
const disponivel = true;
let desconto;

console.log(typeof produto, typeof preco, typeof disponivel, typeof desconto);
""",
 "hint": r"""Para deixar uma variável sem valor, basta declarar: `let desconto;` — o valor dela será `undefined`.""",
 "tests": [
   {"msg": "produto deve ser o texto \"Caneta\"",
    "code": r"""produto === "Caneta" """},
   {"msg": "preco deve ser o número 2.5",
    "code": r"""preco === 2.5"""},
   {"msg": "disponivel deve ser o booleano true",
    "code": r"""disponivel === true"""},
   {"msg": "desconto deve existir e valer undefined (declarada sem valor)",
    "code": r"""typeof desconto === "undefined" && /\b(?:let|var)\s+desconto\b/.test(__code)"""},
 ],
},

{
 "id": "m1l4",
 "title": "Operadores aritméticos",
 "minutes": 7,
 "theory": r"""
## Contas em JavaScript

```js
console.log(10 + 3);   // 13  soma
console.log(10 - 3);   // 7   subtração
console.log(10 * 3);   // 30  multiplicação
console.log(10 / 4);   // 2.5 divisão
console.log(10 % 3);   // 1   resto da divisão
console.log(2 ** 5);   // 32  potência
```

O `%` (módulo) parece estranho, mas é utilíssimo: `n % 2 === 0` descobre se um número é par.

## Precedência

A ordem é a da matemática: parênteses primeiro, depois potência, multiplicação/divisão, soma/subtração.

```js
console.log(2 + 3 * 4);    // 14
console.log((2 + 3) * 4);  // 20
```

## Atalhos que você vai ver muito

```js
let total = 10;
total += 5;   // total = 15
total -= 2;   // total = 13
total *= 2;   // total = 26
total++;      // total = 27
```

> [warn] Cuidado com `+` e texto: `"5" + 1` resulta em `"51"`, porque o `+` cola textos (concatena). Já `"5" - 1` resulta em `4`, porque a subtração converte para número. Confuso, né? Por isso usamos números de verdade.
""",
 "task": r"""
Uma loja vendeu **3 canetas a R$ 30 cada**. Comece com:

```js
const preco = 30;
const quantidade = 3;
```

Calcule:

- `total` — preço × quantidade.
- `troco` — quanto sobra de uma nota de R$ 100 (ou seja, `100 - total`).
- `resto` — o resto da divisão de `total` por `7`.

Imprima os três valores.
""",
 "starter": r"""const preco = 30;
const quantidade = 3;

// calcule total, troco e resto


console.log(total, troco, resto);
""",
 "solution": r"""const preco = 30;
const quantidade = 3;

const total = preco * quantidade;
const troco = 100 - total;
const resto = total % 7;

console.log(total, troco, resto);
""",
 "hint": r"""Multiplicação usa `*` (e não `x` nem `·`). O resto da divisão usa `%`: `total % 7`.""",
 "tests": [
   {"msg": "total deve ser preco * quantidade (90)",
    "code": r"""total === 90"""},
   {"msg": "troco deve ser 100 - total (10)",
    "code": r"""troco === 10"""},
   {"msg": "resto deve ser o resto da divisão de total por 7 (6)",
    "code": r"""resto === 90 % 7"""},
   {"msg": "Use os operadores no cálculo (não digite os resultados na mão)",
    "code": r"""/\*/.test(__code) && /%/.test(__code)"""},
 ],
},

{
 "id": "m1l5",
 "title": "Template strings",
 "minutes": 6,
 "theory": r"""
## Juntando texto e valores

Antigamente a gente colava textos com `+`:

```js
const nome = "Ana";
console.log("Olá, " + nome + "! Você tem " + 25 + " anos.");
```

Funciona, mas é fácil errar um espaço ou uma aspa. A solução moderna são as **template strings** (ou templates literais): textos escritos com **crase** (`` ` ``), onde qualquer expressão JavaScript entra dentro de `${ }`.

```js
const nome = "Ana";
const idade = 25;

console.log(`Olá, ${nome}! Você tem ${idade} anos.`);
// Olá, Ana! Você tem 25 anos.

console.log(`Daqui a 10 anos você terá ${idade + 10}.`);
```

## Vantagem extra: várias linhas

```js
const recado = `Primeira linha
segunda linha
terceira linha`;
```

Com crase, a quebra de linha do seu código faz parte do texto. Sem crase, isso exigiria `\n` em cada linha.

> [tip] A tecla de crase fica ao lado do 1 no teclado (com Shift + ´ ou no teclado numérico, dependendo do layout).
""",
 "task": r"""
Você recebeu estas duas variáveis:

```js
const nome = "Ana";
const idade = 25;
```

Crie uma constante `mensagem` usando **template string** (com crase) que produza exatamente:

```
Ana tem 25 anos
```

Imprima `mensagem`.
""",
 "starter": r"""const nome = "Ana";
const idade = 25;

// use crase e ${ } para montar a mensagem
const mensagem = "";

console.log(mensagem);
""",
 "solution": r"""const nome = "Ana";
const idade = 25;

const mensagem = `${nome} tem ${idade} anos`;

console.log(mensagem);
""",
 "hint": r"""Fica assim: `` const mensagem = `${nome} tem ${idade} anos`; `` — crase no começo e no fim, e as variáveis dentro de `${ }`.""",
 "tests": [
   {"msg": "mensagem deve ser exatamente \"Ana tem 25 anos\"",
    "code": r"""typeof mensagem === "string" && mensagem.trim() === 'Ana tem 25 anos'"""},
   {"msg": "Use template string (crase + ${ }) em vez de concatenar com +",
    "code": r"""__code.includes("`") && __code.includes("${")"""},
 ],
},

{
 "id": "m1l6",
 "title": "Desafio: ficha de cadastro",
 "minutes": 10,
 "theory": r"""
## Hora de juntar tudo

Até aqui você viu: variáveis (`const`/`let`), tipos (`string`, `number`, `boolean`), contas e template strings. Vamos montar uma ficha de cadastro completa.

```js
const ANO_ATUAL = 2026;
const nome = "Ana";
const nascimento = 2001;

const idade = ANO_ATUAL - nascimento;
console.log(`${nome} tem ${idade} anos.`);
```

Repare em dois detalhes:

1. `ANO_ATUAL` está em MAIÚSCULAS — é uma convenção para constantes "globais", valores fixos que o programa inteiro usa.
2. A idade é **calculada**, não digitada. Código bom calcula em vez de repetir números soltos.
""",
 "task": r"""
Monte a ficha de uma pessoa. Comece com:

```js
const ANO_ATUAL = 2026;
const nome = "Ana";
const sobrenome = "Silva";
const anoNascimento = 2001;
```

Você deve criar:

- `nomeCompleto` — nome + sobrenome separados por um espaço (use template string ou concatenação).
- `idade` — `ANO_ATUAL - anoNascimento`.
- `apresentacao` — um texto como `Ana Silva tem 25 anos e nasceu em 2001.` (use as variáveis, não digite os valores).

Imprima `apresentacao`.
""",
 "starter": r"""const ANO_ATUAL = 2026;
const nome = "Ana";
const sobrenome = "Silva";
const anoNascimento = 2001;

// 1. nomeCompleto
const nomeCompleto = "";

// 2. idade
const idade = 0;

// 3. apresentacao
const apresentacao = "";

console.log(apresentacao);
""",
 "solution": r"""const ANO_ATUAL = 2026;
const nome = "Ana";
const sobrenome = "Silva";
const anoNascimento = 2001;

const nomeCompleto = `${nome} ${sobrenome}`;
const idade = ANO_ATUAL - anoNascimento;
const apresentacao = `${nomeCompleto} tem ${idade} anos e nasceu em ${anoNascimento}.`;

console.log(apresentacao);
""",
 "hint": r"""Para juntar nome e sobrenome: `` `${nome} ${sobrenome}` `` — note o espaço entre os dois `${ }`.""",
 "tests": [
   {"msg": "nomeCompleto deve ser \"Ana Silva\"",
    "code": r"""typeof nomeCompleto === "string" && nomeCompleto.replace(/\s+/g," ").trim() === 'Ana Silva'"""},
   {"msg": "idade deve ser calculada como ANO_ATUAL - anoNascimento (25)",
    "code": r"""idade === 25"""},
   {"msg": "apresentacao deve conter o nome completo",
    "code": r"""typeof apresentacao === "string" && apresentacao.includes(nomeCompleto)"""},
   {"msg": "apresentacao deve conter a idade calculada",
    "code": r"""apresentacao.includes(String(idade))"""},
   {"msg": "apresentacao deve conter o ano de nascimento",
    "code": r"""apresentacao.includes(String(anoNascimento))"""},
 ],
},

]},
# =====================================================================
{
 "id": "logica",
 "title": "Lógica e controle de fluxo",
 "icon": "🔀",
 "lessons": [

{
 "id": "m2l1",
 "title": "Booleanos e comparações",
 "minutes": 7,
 "theory": r"""
## Comparando valores

Toda decisão em um programa começa com uma comparação, e toda comparação devolve um **booleano**: `true` ou `false`.

```js
console.log(10 > 3);    // true
console.log(10 < 3);    // false
console.log(10 >= 10);  // true
console.log(10 <= 9);   // false
console.log(10 === 10); // true  (igual)
console.log(10 !== 10); // false (diferente)
```

## === versus ==

JavaScript tem dois operadores de igualdade, e isso causa confusão:

```js
console.log(5 == "5");   // true   ← converte o texto para número!
console.log(5 === "5");  // false  ← tipos diferentes
```

O `==` faz conversão automática de tipos (chamada de *coerção*) e cria surpresas como `"" == 0` ser `true`. O `===` compara valor **e** tipo, sem mágica.

> [warn] Regra prática: use sempre `===` e `!==`. Só use `==` em situações muito específicas (como `valor == null`, que pega `null` e `undefined` juntos).
""",
 "task": r"""
Comece com `const idade = 20;` e crie três constantes:

- `maiorDeIdade` — `true` se a idade for 18 ou mais.
- `temDezoito` — `true` apenas se a idade for exatamente 18.
- `idadeComoTexto` — `true` se `idade !== "20"` (comparando número com texto).

Imprima as três.
""",
 "starter": r"""const idade = 20;

// crie as três constantes


console.log(maiorDeIdade, temDezoito, idadeComoTexto);
""",
 "solution": r"""const idade = 20;

const maiorDeIdade = idade >= 18;
const temDezoito = idade === 18;
const idadeComoTexto = idade !== "20";

console.log(maiorDeIdade, temDezoito, idadeComoTexto);
""",
 "hint": r"""`idade >= 18` já devolve um booleano — não precisa de `if` para isso. E `idade !== "20"` é `true` porque `20` (número) e `"20"` (texto) são diferentes em tipo.""",
 "tests": [
   {"msg": "maiorDeIdade deve ser true",
    "code": r"""maiorDeIdade === true"""},
   {"msg": "temDezoito deve ser false (a idade é 20)",
    "code": r"""temDezoito === false"""},
   {"msg": "idadeComoTexto deve ser true (número é diferente de texto)",
    "code": r"""idadeComoTexto === true"""},
   {"msg": "Use comparações estritas (=== ou !==)",
    "code": r"""__code.includes("===") || __code.includes("!==")"""},
 ],
},

{
 "id": "m2l2",
 "title": "Operadores lógicos",
 "minutes": 7,
 "theory": r"""
## E, ou, não

Três operadores combinam condições:

- `&&` (**e**) — só é `true` se **as duas** condições forem verdadeiras.
- `||` (**ou**) — é `true` se **pelo menos uma** for verdadeira.
- `!` (**não**) — inverte: `!true` é `false`.

```js
const temIngresso = true;
const temDocumento = false;

console.log(temIngresso && temDocumento); // false
console.log(temIngresso || temDocumento); // true
console.log(!temIngresso);                // false
```

## Faixas de valores

Para testar "está entre 18 e 65", você precisa das duas condições:

```js
const idade = 30;
const adulto = idade >= 18 && idade < 65;  // true
```

Escrever `18 <= idade < 65` **não funciona** em JavaScript (ele avalia da esquerda para a direita e compara booleanos com números).

## Curto-circuito

`&&` e `||` param de avaliar assim que sabem a resposta. Com `||` isso vira um truque para valores padrão:

```js
const apelido = nomeDigitado || "anônimo";
```
""",
 "task": r"""
No cinema, para entrar é preciso **ter ingresso E documento**. Comece com:

```js
const temIngresso = true;
const temDocumento = false;
```

Crie:

- `podeEntrar` — usa `&&`.
- `temAlgumDosDois` — usa `||`.
- `precisaResolver` — o contrário de `podeEntrar` (use `!`).

Imprima os três.
""",
 "starter": r"""const temIngresso = true;
const temDocumento = false;

// crie podeEntrar, temAlgumDosDois e precisaResolver


console.log(podeEntrar, temAlgumDosDois, precisaResolver);
""",
 "solution": r"""const temIngresso = true;
const temDocumento = false;

const podeEntrar = temIngresso && temDocumento;
const temAlgumDosDois = temIngresso || temDocumento;
const precisaResolver = !podeEntrar;

console.log(podeEntrar, temAlgumDosDois, precisaResolver);
""",
 "hint": r"""`podeEntrar` será `false`, porque `temDocumento` é `false` — e com `&&` basta uma condição falsa para o resultado ser falso.""",
 "tests": [
   {"msg": "podeEntrar deve ser false",
    "code": r"""podeEntrar === false"""},
   {"msg": "temAlgumDosDois deve ser true",
    "code": r"""temAlgumDosDois === true"""},
   {"msg": "precisaResolver deve ser true (negação de podeEntrar)",
    "code": r"""precisaResolver === true"""},
   {"msg": "Use os três operadores: && , || e !",
    "code": r"""__code.includes("&&") && __code.includes("||") && __code.includes("!")"""},
 ],
},

{
 "id": "m2l3",
 "title": "if, else if e else",
 "minutes": 8,
 "theory": r"""
## Tomando decisões

O `if` executa um bloco **somente se** a condição for verdadeira:

```js
const idade = 20;

if (idade >= 18) {
  console.log("Pode entrar");
}
```

Com `else`, você diz o que fazer caso contrário:

```js
if (idade >= 18) {
  console.log("Pode entrar");
} else {
  console.log("Não pode entrar");
}
```

## Várias possibilidades: else if

As condições são testadas **de cima para baixo** e o primeiro `if` verdadeiro ganha. O `else` final é o "resto":

```js
const nota = 7.5;

if (nota >= 9) {
  console.log("Excelente");
} else if (nota >= 7) {
  console.log("Bom");
} else if (nota >= 5) {
  console.log("Regular");
} else {
  console.log("Reprovado");
}
```

> [warn] A ordem importa. Se o primeiro teste fosse `nota >= 5`, uma nota 9,5 cairia em "Regular" — o programa nunca chegaria ao `nota >= 9`.

## Boas práticas

Sempre use chaves `{ }`, mesmo com uma linha só. Isso evita bugs difíceis quando alguém adiciona uma linha depois.
""",
 "task": r"""
Comece com `const temperatura = 28;`. Usando `if` / `else if` / `else`, defina a variável `clima`:

- acima de 25 → `"quente"`
- de 18 até 25 → `"agradável"`
- abaixo de 18 → `"frio"`

Como 28 é maior que 25, o resultado esperado é `"quente"`. Mas escreva a lógica completa para os três casos: os testes verificam que você usou as três ramificações.

Imprima `clima`.
""",
 "starter": r"""const temperatura = 28;

let clima;

// escreva o if / else if / else


console.log(clima);
""",
 "solution": r"""const temperatura = 28;

let clima;

if (temperatura > 25) {
  clima = "quente";
} else if (temperatura >= 18) {
  clima = "agradável";
} else {
  clima = "frio";
}

console.log(clima);
""",
 "hint": r"""Comece pelo caso mais extremo (`temperatura > 25`) e vá descendo. A última condição pode ser só `else`, porque tudo o que sobra é "frio".""",
 "tests": [
   {"msg": "clima deve ser \"quente\" para 28 graus",
    "code": r"""clima === "quente" """},
   {"msg": "Use um if",
    "code": r"""/if\s*\(/.test(__code)"""},
   {"msg": "Use else if para o caso intermediário",
    "code": r"""/else\s+if\s*\(/.test(__code)"""},
   {"msg": "Use um else final para o caso frio",
    "code": r"""/else\s*\{/.test(__code)"""},
 ],
},

{
 "id": "m2l4",
 "title": "switch",
 "minutes": 7,
 "theory": r"""
## Quando há muitos casos iguais

Quando você compara **o mesmo valor** com várias opções, `switch` fica mais legível que uma escada de `if`:

```js
const dia = "segunda";

switch (dia) {
  case "segunda":
  case "terça":
  case "quarta":
  case "quinta":
  case "sexta":
    console.log("Dia útil");
    break;
  case "sábado":
  case "domingo":
    console.log("Fim de semana");
    break;
  default:
    console.log("Dia inválido");
}
```

Três detalhes essenciais:

1. O `case` é comparado com `===` (valor e tipo).
2. O `break` encerra o `switch`. **Sem ele**, a execução "escorrega" para o próximo caso (isso se chama *fallthrough*) — às vezes é útil, como no exemplo acima, mas normalmente é um bug.
3. `default` é o caso "nenhum dos anteriores"; pode ficar em qualquer posição, mas o usual é no fim.

> [tip] `switch` só serve para igualdade. Para faixas (`nota >= 7`), use `if`.
""",
 "task": r"""
Comece com `const dia = "segunda";`.

Usando `switch`, defina a variável `mensagem`:

- `"segunda"` → `"Começo de semana"`
- `"sexta"` → `"Sexta-feira!"`
- `"sábado"` ou `"domingo"` → `"Fim de semana"`
- qualquer outra coisa → `"Dia comum"`

Imprima `mensagem`.
""",
 "starter": r"""const dia = "segunda";

let mensagem;

// escreva o switch


console.log(mensagem);
""",
 "solution": r"""const dia = "segunda";

let mensagem;

switch (dia) {
  case "segunda":
    mensagem = "Começo de semana";
    break;
  case "sexta":
    mensagem = "Sexta-feira!";
    break;
  case "sábado":
  case "domingo":
    mensagem = "Fim de semana";
    break;
  default:
    mensagem = "Dia comum";
}

console.log(mensagem);
""",
 "hint": r"""Para dois casos com a mesma ação, empilhe os `case` sem `break` entre eles: `case "sábado": case "domingo": mensagem = "Fim de semana"; break;`""",
 "tests": [
   {"msg": "mensagem deve ser \"Começo de semana\" para segunda",
    "code": r"""mensagem === "Começo de semana" """},
   {"msg": "Use switch",
    "code": r"""/switch\s*\(/.test(__code)"""},
   {"msg": "Use case para segunda, sexta e o fim de semana",
    "code": r"""(/case\s*["']segunda["']/.test(__code)) && (/case\s*["']sexta["']/.test(__code)) && (/case\s*["']domingo["']/.test(__code))"""},
   {"msg": "Use break (ou um return) para encerrar os casos",
    "code": r"""/break/.test(__code)"""},
   {"msg": "Use default para os outros dias",
    "code": r"""/default\s*:/.test(__code)"""},
 ],
},

{
 "id": "m2l5",
 "title": "Ternário e valores truthy/falsy",
 "minutes": 7,
 "theory": r"""
## if de uma linha: o operador ternário

Para escolher entre dois valores, existe uma forma curta:

```js
condição ? valorSeVerdadeiro : valorSeFalso
```

```js
const idade = 20;
const status = idade >= 18 ? "adulto" : "menor";
console.log(status); // adulto
```

Isso é ótimo para atribuições simples. **Não** é bom para lógica com vários passos: ternários aninhados viram um quebra-cabeça.

## Truthy e falsy

Em qualquer lugar onde o JS espera um booleano, ele converte o valor. Os valores **falsy** (que viram `false`) são apenas oito:

```js
false, 0, -0, 0n, "", null, undefined, NaN
```

Todo o resto é **truthy** — incluindo `"0"`, `"false"`, `[]` e `{}`.

```js
if ("0") console.log("passa!");   // imprime: texto não vazio é truthy
if ([])  console.log("passa!");   // imprime: array vazio é truthy
```

## Convertendo de propósito

```js
Boolean(0);      // false
Boolean("oi");   // true
!!"";            // false  (o ! duplo converte para booleano)
```
""",
 "task": r"""
Comece com:

```js
const pontos = 72;
const nomeDigitado = "";
```

Crie:

- `resultado` — usando **ternário**: `"Aprovado"` se `pontos >= 60`, senão `"Reprovado"`.
- `nomeFinal` — usando `||`: `nomeDigitado` se ele tiver valor, senão `"Anônimo"`.
- `temNome` — o valor de `nomeDigitado` convertido para booleano (use `Boolean(...)`).

Imprima os três.
""",
 "starter": r"""const pontos = 72;
const nomeDigitado = "";

// 1. resultado com ternário
const resultado = "";

// 2. nomeFinal com ||
const nomeFinal = "";

// 3. temNome com Boolean()
const temNome = false;

console.log(resultado, nomeFinal, temNome);
""",
 "solution": r"""const pontos = 72;
const nomeDigitado = "";

const resultado = pontos >= 60 ? "Aprovado" : "Reprovado";
const nomeFinal = nomeDigitado || "Anônimo";
const temNome = Boolean(nomeDigitado);

console.log(resultado, nomeFinal, temNome);
""",
 "hint": r"""Texto vazio `""` é falsy, então `"" || "Anônimo"` resulta em `"Anônimo"`.""",
 "tests": [
   {"msg": "resultado deve ser \"Aprovado\"",
    "code": r"""resultado === "Aprovado" """},
   {"msg": "nomeFinal deve ser \"Anônimo\" (texto vazio é falsy)",
    "code": r"""nomeFinal === "Anônimo" """},
   {"msg": "temNome deve ser false",
    "code": r"""temNome === false"""},
   {"msg": "Use o operador ternário ( ? : )",
    "code": r"""/\?[^;]*:/.test(__code)"""},
   {"msg": "Use || para o valor padrão do nome",
    "code": r"""__code.includes("||")"""},
 ],
},

{
 "id": "m2l6",
 "title": "Desafio: classificação de notas",
 "minutes": 12,
 "theory": r"""
## Um problema real

Escolas precisam converter notas numéricas em conceitos. Esse tipo de regra aparece o tempo todo em software de verdade: definir faixas, validar entradas, decidir o que mostrar.

```js
const nota = 7.5;
let conceito;

if (nota >= 9) {
  conceito = "A";
} else if (nota >= 7) {
  conceito = "B";
} else if (nota >= 5) {
  conceito = "C";
} else {
  conceito = "D";
}
```

Repare que a nota 9,5 não é testada em `nota >= 7`: o primeiro `if` já capturou. Isso é o que torna a ordem das condições tão importante.
""",
 "task": r"""
Comece com `const nota = 7.5;`.

Crie as variáveis:

- `conceito` — `"A"` se nota ≥ 9; `"B"` se ≥ 7; `"C"` se ≥ 5; `"D"` se for menor que 5. Use `if` / `else if` / `else`.
- `valida` — `true` só se a nota estiver entre 0 e 10 (inclusive). Use `&&`.
- `situacao` — com ternário: `"Aprovado"` se o conceito for `"A"`, `"B"` ou `"C"`; senão `"Reprovado"`.

Imprima tudo.
""",
 "starter": r"""const nota = 7.5;

let conceito;
const valida = false;
let situacao;

// 1. conceito com if / else if / else


// 2. valida (entre 0 e 10)


// 3. situacao com ternário


console.log(nota, conceito, valida, situacao);
""",
 "solution": r"""const nota = 7.5;

let conceito;

if (nota >= 9) {
  conceito = "A";
} else if (nota >= 7) {
  conceito = "B";
} else if (nota >= 5) {
  conceito = "C";
} else {
  conceito = "D";
}

const valida = nota >= 0 && nota <= 10;
const situacao = conceito !== "D" ? "Aprovado" : "Reprovado";

console.log(nota, conceito, valida, situacao);
""",
 "hint": r"""Para `situacao` sem escrever três comparações, use: `conceito !== "D" ? "Aprovado" : "Reprovado"` — ou `["A","B","C"].includes(conceito)`.""",
 "tests": [
   {"msg": "conceito deve ser \"B\" para a nota 7.5",
    "code": r"""conceito === "B" """},
   {"msg": "Use if / else if / else para o conceito",
    "code": r"""/else\s+if\s*\(/.test(__code)"""},
   {"msg": "valida deve ser true (7.5 está entre 0 e 10)",
    "code": r"""valida === true"""},
   {"msg": "Use uma condição de faixa com &&",
    "code": r"""/nota\s*>=\s*0\s*&&/.test(__code)"""},
   {"msg": "situacao deve ser \"Aprovado\"",
    "code": r"""situacao === "Aprovado" """},
 ],
},

]},
# =====================================================================
{
 "id": "funcoes",
 "title": "Funções",
 "icon": "🧩",
 "lessons": [

{
 "id": "m3l1",
 "title": "Declarando e chamando funções",
 "minutes": 7,
 "theory": r"""
## Blocos de código com nome

Uma **função** agrupa instruções que você pode executar quantas vezes quiser, quando quiser. Sem funções, todo código vira uma receita repetida e difícil de manter.

```js
function saudacao() {
  console.log("Olá, tudo bem?");
}

saudacao();  // Olá, tudo bem?
saudacao();  // Olá, tudo bem?
```

Três partes:

1. `function` — palavra-chave.
2. `saudacao` — o nome (verbo, camelCase: `calcularTotal`, `mostrarMensagem`).
3. `{ ... }` — o corpo, o que a função faz.

**Declarar** é escrever a receita. **Chamar** (ou invocar) é usar a receita: `saudacao()`.

## Por que isso importa

```js
function mostrarCabecalho() {
  console.log("==============");
  console.log("  MEU SISTEMA");
  console.log("==============");
}

mostrarCabecalho();
mostrarCabecalho();
```

Se amanhã o cabeçalho mudar, você altera em **um** lugar.

> [warn] Sem os parênteses, `saudacao` é só a função em si (um valor). `saudacao()` é a execução dela. Confundir os dois é um erro clássico.
""",
 "task": r"""
1. Declare uma função chamada `apresentar` que imprime `Olá! Eu estou aprendendo JavaScript`.
2. Chame a função **duas vezes**.
""",
 "starter": r"""// 1. declare a função apresentar


// 2. chame a função duas vezes

""",
 "solution": r"""function apresentar() {
  console.log("Olá! Eu estou aprendendo JavaScript");
}

apresentar();
apresentar();
""",
 "hint": r"""A chamada fica fora das chaves, no final: `apresentar();` duas vezes.""",
 "tests": [
   {"msg": "Crie uma função chamada apresentar",
    "code": r"""typeof apresentar === "function" """},
   {"msg": "A função deve imprimir a mensagem pedida",
    "code": r"""__normalize(__printed()).includes("olá! eu estou aprendendo javascript")"""},
   {"msg": "Chame a função duas vezes (a mensagem deve aparecer 2 vezes)",
    "code": r"""__logs.filter(function(l){ return l.text.toLowerCase().includes("aprendendo javascript"); }).length >= 2"""},
 ],
},

{
 "id": "m3l2",
 "title": "Parâmetros e return",
 "minutes": 8,
 "theory": r"""
## Entrada: parâmetros

Parâmetros são os "ingredientes" da função:

```js
function saudar(nome) {
  console.log("Olá, " + nome + "!");
}

saudar("Ana");   // Olá, Ana!
saudar("Bruno"); // Olá, Bruno!
```

Com vários parâmetros, a ordem importa: `function somar(a, b)` — ao chamar `somar(2, 3)`, `a` recebe 2 e `b` recebe 3.

## Saída: return

`return` devolve um valor para quem chamou. Ele também **encerra** a função imediatamente.

```js
function somar(a, b) {
  return a + b;
}

const resultado = somar(2, 3);  // 5
console.log(resultado * 10);    // 50
```

A diferença entre `console.log` e `return` é enorme:

- `console.log` **mostra** o valor no console (para humanos).
- `return` **entrega** o valor ao programa (para o código continuar usando).

```js
function semReturn(a, b) {
  a + b;
}
console.log(semReturn(2, 3));  // undefined  ← não devolveu nada
```

> [tip] Uma função que só imprime não pode ser reaproveitada em cálculos. Prefira funções que **retornam** e imprima o resultado na chamada.
""",
 "task": r"""
Crie duas funções:

1. `somar(a, b)` — **retorna** a soma dos dois números.
2. `media(a, b, c)` — **retorna** a média aritmética dos três (some e divida por 3).

Depois imprima `somar(2, 3)` e `media(10, 20, 30)`.
""",
 "starter": r"""// 1. função somar


// 2. função media


console.log(somar(2, 3));
console.log(media(10, 20, 30));
""",
 "solution": r"""function somar(a, b) {
  return a + b;
}

function media(a, b, c) {
  return (a + b + c) / 3;
}

console.log(somar(2, 3));
console.log(media(10, 20, 30));
""",
 "hint": r"""Não esqueça dos parênteses na soma da média: `(a + b + c) / 3`. Sem eles, a divisão só valeria para o `c`.""",
 "tests": [
   {"msg": "somar deve retornar 5 para somar(2, 3)",
    "code": r"""typeof somar === "function" && somar(2, 3) === 5"""},
   {"msg": "somar deve funcionar com outros números também",
    "code": r"""somar(10, -4) === 6 && somar(0, 0) === 0"""},
   {"msg": "media deve retornar 20 para media(10, 20, 30)",
    "code": r"""typeof media === "function" && media(10, 20, 30) === 20"""},
   {"msg": "Use return (e não apenas imprimir)",
    "code": r"""/return/.test(__code)"""},
 ],
},

{
 "id": "m3l3",
 "title": "Parâmetros padrão e resto",
 "minutes": 8,
 "theory": r"""
## Valor padrão

Se o argumento não for passado, o parâmetro vale `undefined`. Você pode definir um padrão:

```js
function criarUsuario(nome, papel = "aluno") {
  return `${nome} (${papel})`;
}

console.log(criarUsuario("Ana"));            // Ana (aluno)
console.log(criarUsuario("Bruno", "admin")); // Bruno (admin)
```

O padrão só é usado quando o argumento é `undefined` — passar `null` **não** ativa o padrão.

## Quantidade variável: rest (...)

O operador rest junta todos os argumentos que sobrarem em um **array**:

```js
function somarTudo(...numeros) {
  let total = 0;
  for (const n of numeros) {
    total += n;
  }
  return total;
}

console.log(somarTudo(1, 2, 3, 4)); // 10
```

`...numeros` precisa ser o **último** parâmetro. E note: `numeros` é um array de verdade, então você pode usar `.length`, `.map`, etc.

## Argumentos de verdade: arguments

Toda função tradicional tem o objeto `arguments`, com todos os argumentos recebidos. É antigo; prefira `...rest`.
""",
 "task": r"""
Crie duas funções:

1. `criarUsuario(nome, papel = "aluno")` — retorna `` `${nome} (${papel})` ``.
2. `somarTudo(...numeros)` — retorna a soma de todos os números recebidos (use `for...of`).

Imprima `criarUsuario("Ana")` e `somarTudo(1, 2, 3, 4)`.
""",
 "starter": r"""// 1. criarUsuario com valor padrão


// 2. somarTudo usando rest (...)


console.log(criarUsuario("Ana"));
console.log(somarTudo(1, 2, 3, 4));
""",
 "solution": r"""function criarUsuario(nome, papel = "aluno") {
  return `${nome} (${papel})`;
}

function somarTudo(...numeros) {
  let total = 0;
  for (const n of numeros) {
    total += n;
  }
  return total;
}

console.log(criarUsuario("Ana"));
console.log(somarTudo(1, 2, 3, 4));
""",
 "hint": r"""O valor padrão vai na declaração: `function criarUsuario(nome, papel = "aluno")`. E `for (const n of numeros)` percorre o array criado pelo rest.""",
 "tests": [
   {"msg": "criarUsuario(\"Ana\") deve retornar \"Ana (aluno)\"",
    "code": r"""typeof criarUsuario === "function" && criarUsuario("Ana") === 'Ana (aluno)'"""},
   {"msg": "criarUsuario deve aceitar o papel informado",
    "code": r"""criarUsuario("Bruno", "admin") === 'Bruno (admin)'"""},
   {"msg": "somarTudo(1, 2, 3, 4) deve retornar 10",
    "code": r"""typeof somarTudo === "function" && somarTudo(1, 2, 3, 4) === 10"""},
   {"msg": "somarTudo deve funcionar com qualquer quantidade de números",
    "code": r"""somarTudo(5) === 5 && somarTudo() === 0 && somarTudo(1,1,1,1,1,1) === 6"""},
   {"msg": "Use o operador rest (...) na função somarTudo",
    "code": r"""/\.\.\.\s*\w+/.test(__code)"""},
 ],
},

{
 "id": "m3l4",
 "title": "Arrow functions",
 "minutes": 8,
 "theory": r"""
## A forma curta

Arrow functions (funções seta) são uma sintaxe mais curta, criada no ES6:

```js
// função tradicional
function dobro(n) {
  return n * 2;
}

// arrow function
const dobro = (n) => {
  return n * 2;
};

// arrow com corpo de expressão (return implícito)
const dobro = (n) => n * 2;
```

Quando a função tem **uma só expressão**, as chaves e o `return` são opcionais — o valor da expressão é devolvido automaticamente.

```js
const somar = (a, b) => a + b;
const quadrado = n => n ** 2;        // um parâmetro dispensa parênteses
const aleatorio = () => Math.random(); // nenhum parâmetro: parênteses vazios
const criarObjeto = (n) => ({ nome: n }); // objeto precisa de parênteses
```

As arrow functions aparecem em todo código moderno, principalmente como **callbacks**:

```js
const numeros = [1, 2, 3];
const dobrados = numeros.map((n) => n * 2); // [2, 4, 6]
```

> [warn] Arrow functions **não têm** seu próprio `this` — elas herdam o `this` de onde foram escritas. Em métodos de objeto, use função tradicional.
""",
 "task": r"""
Escreva as três como **arrow functions** (usando `=>`), com return implícito quando possível:

- `dobro(n)` — retorna `n * 2`.
- `somar(a, b)` — retorna a soma.
- `ehPar(n)` — retorna `true` se `n` for par (dica: `n % 2 === 0`).

Imprima `dobro(4)`, `somar(2, 3)` e `ehPar(7)`.
""",
 "starter": r"""// 1. const dobro = ...


// 2. const somar = ...


// 3. const ehPar = ...


console.log(dobro(4), somar(2, 3), ehPar(7));
""",
 "solution": r"""const dobro = (n) => n * 2;
const somar = (a, b) => a + b;
const ehPar = (n) => n % 2 === 0;

console.log(dobro(4), somar(2, 3), ehPar(7));
""",
 "hint": r"""Sem chaves não precisa de `return`: `const dobro = (n) => n * 2;`. Mas atenção: `const ehPar = (n) => { n % 2 === 0 }` com chaves retornaria `undefined`.""",
 "tests": [
   {"msg": "dobro(4) deve ser 8",
    "code": r"""typeof dobro === "function" && dobro(4) === 8"""},
   {"msg": "somar(2, 3) deve ser 5",
    "code": r"""typeof somar === "function" && somar(2, 3) === 5"""},
   {"msg": "ehPar(7) deve ser false e ehPar(8) deve ser true",
    "code": r"""typeof ehPar === "function" && ehPar(7) === false && ehPar(8) === true"""},
   {"msg": "Use arrow functions (=>)",
    "code": r"""/=>/.test(__code)"""},
 ],
},

{
 "id": "m3l5",
 "title": "Escopo e closures",
 "minutes": 9,
 "theory": r"""
## Onde cada variável existe

O **escopo** define onde uma variável pode ser acessada:

```js
const global = "visível em todo lugar";

function exemplo() {
  const interna = "só existe aqui dentro";
  console.log(global);  // ok
  console.log(interna); // ok
}

exemplo();
console.log(interna); // ReferenceError: interna is not defined
```

Variáveis criadas com `let`/`const` dentro de `{ }` vivem só naquele bloco:

```js
if (true) {
  const dentro = 1;
}
console.log(dentro); // ReferenceError
```

## Closure: a memória da função

Uma função "lembra" do escopo onde nasceu, mesmo depois de ele terminar. Isso é uma **closure**:

```js
function criarContador() {
  let contagem = 0;         // variável privada

  return function () {
    contagem++;
    return contagem;
  };
}

const contar = criarContador();
console.log(contar()); // 1
console.log(contar()); // 2
console.log(contar()); // 3
```

`contagem` não existe fora de `criarContador` — ninguém pode estragá-la. É a base de encapsulamento em JavaScript e o que permite coisas como estado privado, memoização e módulos.

> [tip] Pensou "essa variável não deveria sumir quando a função termina?" — deveria, mas a closure a mantém viva porque a função interna ainda pode precisar dela.
""",
 "task": r"""
Crie a função `criarContador`, que:

1. Cria uma variável `contagem` começando em 0.
2. Retorna uma função que **incrementa** `contagem` e a retorna.

Depois: `const contar = criarContador();` e chame três vezes, imprimindo cada resultado (1, 2, 3).

Bônus: crie `outro = criarContador()` e mostre que ele começa do zero — cada contador tem sua própria `contagem`.
""",
 "starter": r"""function criarContador() {
  // seu código aqui
}

const contar = criarContador();
console.log(contar());
console.log(contar());
console.log(contar());
""",
 "solution": r"""function criarContador() {
  let contagem = 0;

  return function () {
    contagem++;
    return contagem;
  };
}

const contar = criarContador();
console.log(contar());
console.log(contar());
console.log(contar());

const outro = criarContador();
console.log(outro()); // 1 — independente
""",
 "hint": r"""A variável `let contagem = 0` precisa ficar **dentro** de `criarContador`, mas **fora** da função retornada. Assim cada contador criado tem a sua.""",
 "tests": [
   {"msg": "Crie a função criarContador",
    "code": r"""typeof criarContador === "function" """},
   {"msg": "O contador deve retornar 1, 2 e 3 nas chamadas seguidas",
    "code": r"""(function(){ const c = criarContador(); return c() === 1 && c() === 2 && c() === 3; })()"""},
   {"msg": "Cada contador criado deve ser independente",
    "code": r"""(function(){ const a = criarContador(); a(); const b = criarContador(); return b() === 1; })()"""},
   {"msg": "A variável de contagem deve ser privada (use variável dentro da função)",
    "code": r"""/let\s+contagem|let\s+\w+\s*=\s*0/.test(__code)"""},
 ],
},

{
 "id": "m3l6",
 "title": "Funções como valores e callbacks",
 "minutes": 8,
 "theory": r"""
## Funções são valores

Em JavaScript, função é um valor como número ou texto: pode ser guardada em variável, passada como argumento e devolvida por outra função.

```js
function gritar(texto) {
  return texto.toUpperCase() + "!";
}

function sussurrar(texto) {
  return texto.toLowerCase() + "...";
}

function falar(texto, estilo) {
  console.log(estilo(texto));   // chama a função recebida
}

falar("Olá", gritar);      // OLÁ!
falar("Olá", sussurrar);   // olá...
```

Uma função passada para outra é chamada de **callback** ("chame de volta"). Quem recebe decide *quando* chamar.

## Callbacks no dia a dia

```js
const numeros = [1, 2, 3, 4];

numeros.forEach((n) => console.log(n));
const pares = numeros.filter((n) => n % 2 === 0);
setTimeout(() => console.log("depois de 1s"), 1000);
```

Note: passamos `gritar` (a função), **não** `gritar()` (o resultado da chamada).

> [warn] `falar("Olá", gritar())` executaria `gritar` imediatamente e passaria o resultado. Sem parênteses!
""",
 "task": r"""
Crie:

1. Duas funções: `gritar(texto)` → texto em maiúsculas com `!` no fim; `sussurrar(texto)` → texto em minúsculas com `...` no fim.
2. `falar(texto, estilo)` — recebe um texto e uma **função**, imprime `estilo(texto)`.
3. Chame `falar("Olá", gritar)` e `falar("Olá", sussurrar)`.
""",
 "starter": r"""// 1. as duas funções de estilo
function gritar(texto) {
}

function sussurrar(texto) {
}

// 2. falar(texto, estilo)


// 3. as duas chamadas

""",
 "solution": r"""function gritar(texto) {
  return texto.toUpperCase() + "!";
}

function sussurrar(texto) {
  return texto.toLowerCase() + "...";
}

function falar(texto, estilo) {
  console.log(estilo(texto));
}

falar("Olá", gritar);
falar("Olá", sussurrar);
""",
 "hint": r"""Dentro de `falar`, chame o parâmetro como função: `estilo(texto)`. Na chamada, passe a função sem parênteses: `falar("Olá", gritar)`.""",
 "tests": [
   {"msg": "gritar(\"oi\") deve retornar \"OI!\"",
    "code": r"""typeof gritar === "function" && gritar("oi") === "OI!" """},
   {"msg": "sussurrar(\"OI\") deve retornar \"oi...\"",
    "code": r"""typeof sussurrar === "function" && sussurrar("OI") === "oi..." """},
   {"msg": "falar deve chamar a função recebida e imprimir o resultado",
    "code": r"""(function(){ const antes = __logs.length; falar("teste", gritar); return __logs.length > antes && __logs[__logs.length-1].text === "TESTE!"; })()"""},
   {"msg": "Chame falar com as duas funções diferentes",
    "code": r"""__printed().includes("OLÁ!") && __printed().toLowerCase().includes("olá...")"""},
 ],
},

]},
]
