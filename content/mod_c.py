# -*- coding: utf-8 -*-
"""Módulos 7 a 9 — Loops, números/Math/Datas e DOM."""

MODULES = [

# =====================================================================
{
 "id": "loops",
 "title": "Loops (repetições)",
 "icon": "🔁",
 "lessons": [

{
 "id": "m7l1",
 "title": "O loop for",
 "minutes": 8,
 "theory": r"""
## Repetir com contador

O `for` clássico tem três partes separadas por ponto e vírgula: **início**, **condição** e **passo**.

```js
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
// 1 2 3 4 5
```

Lendo em voz alta: "começando em `i = 1`, enquanto `i <= 5`, faça o corpo e depois `i++`".

## Contando de trás para frente

```js
for (let i = 5; i >= 1; i--) {
  console.log(i);
}
```

## Acumulando resultados

```js
let soma = 0;

for (let i = 1; i <= 10; i++) {
  soma += i;
}
console.log(soma);  // 55
```

## Montando um array

```js
const pares = [];

for (let i = 1; i <= 10; i++) {
  if (i % 2 === 0) {
    pares.push(i);
  }
}
console.log(pares);  // [2, 4, 6, 8, 10]
```

> [warn] Erro clássico: esquecer de atualizar o contador (`i++`) — o loop nunca termina e a aba trava. Se isso acontecer aqui, o sandbox interrompe depois de 6 segundos.
""",
 "task": r"""
Usando um `for`:

1. Crie `soma` com a soma de todos os números de **1 a 10** (resultado: 55).
2. Crie o array `pares` com os números pares de **1 a 20** (use `push`).
3. Crie o array `regressiva` com os números de **5 até 1** (nessa ordem).
""",
 "starter": r"""let soma = 0;
const pares = [];
const regressiva = [];

// 1. for de 1 a 10 somando
// 2. for de 1 a 20 guardando os pares
// 3. for de 5 até 1


console.log(soma, pares, regressiva);
""",
 "solution": r"""let soma = 0;
const pares = [];
const regressiva = [];

for (let i = 1; i <= 10; i++) {
  soma += i;
}

for (let i = 1; i <= 20; i++) {
  if (i % 2 === 0) pares.push(i);
}

for (let i = 5; i >= 1; i--) {
  regressiva.push(i);
}

console.log(soma, pares, regressiva);
""",
 "hint": r"""No terceiro loop, o passo é `i--` e a condição é `i >= 1`.""",
 "tests": [
   {"msg": "soma deve ser 55",
    "code": r"""soma === 55"""},
   {"msg": "pares deve ser [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]",
    "code": r"""JSON.stringify(pares) === JSON.stringify([2,4,6,8,10,12,14,16,18,20])"""},
   {"msg": "regressiva deve ser [5, 4, 3, 2, 1]",
    "code": r"""JSON.stringify(regressiva) === JSON.stringify([5,4,3,2,1])"""},
   {"msg": "Use um for com contador",
    "code": r"""/for\s*\(\s*let\s+\w+\s*=/.test(__code)"""},
 ],
},

{
 "id": "m7l2",
 "title": "while",
 "minutes": 7,
 "theory": r"""
## Enquanto for verdadeiro

O `while` repete **enquanto** a condição for verdadeira. Você não sabe quantas voltas serão — só sabe quando parar.

```js
let contador = 3;

while (contador > 0) {
  console.log(contador);
  contador--;
}
console.log("Fim!");
// 3 2 1 Fim!
```

## Quando o while é melhor que o for

Quando a parada depende de um cálculo, não de um contador fixo:

```js
let valor = 10;

while (valor < 100) {
  valor *= 2;
}
console.log(valor);  // 160
```

Ou quando você não sabe o tamanho do problema:

```js
let tentativas = 0;
let sucesso = false;

while (tentativas < 3 && !sucesso) {
  tentativas++;
  sucesso = Math.random() > 0.5;
}
```

> [warn] Se a condição nunca ficar falsa, o loop é infinito. Garanta que algo dentro do `while` caminhe para encerrar (aqui, `valor *= 2` ou `contador--`).
""",
 "task": r"""
1. Crie o array `contagem` com `3, 2, 1` e a variável `fim = "Fim!"` usando um `while` que decrementa um contador.
2. Comece com `let valor = 10;` e dobre o valor dentro de um `while` até ele passar de 100. Guarde o resultado em `valorFinal`.
3. Guarde em `voltas` quantas multiplicações foram necessárias.
""",
 "starter": r"""const contagem = [];
let contador = 3;

// 1. while de 3 até 1


let valor = 10;
let voltas = 0;

// 2 e 3. dobre até passar de 100

const valorFinal = valor;

console.log(contagem, valorFinal, voltas);
""",
 "solution": r"""const contagem = [];
let contador = 3;

while (contador > 0) {
  contagem.push(contador);
  contador--;
}
const fim = "Fim!";

let valor = 10;
let voltas = 0;

while (valor < 100) {
  valor *= 2;
  voltas++;
}

const valorFinal = valor;

console.log(contagem, valorFinal, voltas);
""",
 "hint": r"""`10 → 20 → 40 → 80 → 160`: são 4 voltas até passar de 100.""",
 "tests": [
   {"msg": "contagem deve ser [3, 2, 1]",
    "code": r"""JSON.stringify(contagem) === JSON.stringify([3,2,1])"""},
   {"msg": "valorFinal deve ser 160",
    "code": r"""valorFinal === 160"""},
   {"msg": "voltas deve ser 4",
    "code": r"""voltas === 4"""},
   {"msg": "Use um while",
    "code": r"""/while\s*\(/.test(__code)"""},
 ],
},

{
 "id": "m7l3",
 "title": "do...while",
 "minutes": 6,
 "theory": r"""
## Execute pelo menos uma vez

A diferença é sutil mas importante: no `while`, a condição é testada **antes**; no `do...while`, **depois**. Ou seja, o corpo roda pelo menos uma vez.

```js
let i = 10;

while (i < 5) {
  console.log("while:", i);
}
// não imprime nada

do {
  console.log("do...while:", i);
} while (i < 5);
// imprime uma vez, mesmo com a condição falsa
```

## Onde isso ajuda

Em menus e validações — você precisa mostrar a pergunta pelo menos uma vez, e repetir enquanto a resposta for inválida:

```js
let numero = 0;

do {
  numero = Math.floor(Math.random() * 6) + 1;
} while (numero === 6);
console.log("Saiu diferente de 6:", numero);
```

> [tip] Não esqueça do ponto e vírgula depois do `while` no do...while: `} while (condicao);`
""",
 "task": r"""
1. Com `let i = 10;` e a condição `i < 5`, use `do...while` para adicionar `i` ao array `executou`.
2. Crie um `do...while` que sorteia números de 1 a 6 (`Math.floor(Math.random() * 6) + 1`) até sair algo **diferente de 6**, guardando cada sorteio em `sorteios`.
""",
 "starter": r"""const executou = [];
let i = 10;

// 1. do...while que roda uma vez


const sorteios = [];
let numero;

// 2. sorteie até sair diferente de 6


console.log(executou, sorteios);
""",
 "solution": r"""const executou = [];
let i = 10;

do {
  executou.push(i);
} while (i < 5);

const sorteios = [];
let numero;

do {
  numero = Math.floor(Math.random() * 6) + 1;
  sorteios.push(numero);
} while (numero === 6);

console.log(executou, sorteios);
""",
 "hint": r"""No segundo, a condição de continuação é `while (numero === 6)` — ou seja, repete enquanto tirar 6.""",
 "tests": [
   {"msg": "executou deve ter exatamente 1 item (10), mesmo com a condição falsa",
    "code": r"""JSON.stringify(executou) === JSON.stringify([10])"""},
   {"msg": "sorteios deve ter pelo menos 1 item, e o último diferente de 6",
    "code": r"""Array.isArray(sorteios) && sorteios.length >= 1 && sorteios[sorteios.length - 1] !== 6"""},
   {"msg": "Todos os sorteios (menos o último) devem ser 6",
    "code": r"""sorteios.slice(0, -1).every(function(n){ return n === 6; })"""},
   {"msg": "Todos os sorteios devem estar entre 1 e 6",
    "code": r"""sorteios.every(function(n){ return Number.isInteger(n) && n >= 1 && n <= 6; })"""},
   {"msg": "Use do...while",
    "code": r"""/do\s*\{/.test(__code) && /while\s*\(/.test(__code)"""},
 ],
},

{
 "id": "m7l4",
 "title": "for...of e for...in",
 "minutes": 8,
 "theory": r"""
## Percorrendo valores: for...of

Para arrays (e qualquer coisa iterável), `for...of` é o mais legível:

```js
const frutas = ["maçã", "banana", "uva"];

for (const fruta of frutas) {
  console.log(fruta);
}
```

Se precisar do índice, use `.entries()`:

```js
for (const [i, fruta] of frutas.entries()) {
  console.log(i, fruta);
}
```

## Percorrendo chaves: for...in

Para objetos, `for...in` percorre as **chaves**:

```js
const pessoa = { nome: "Ana", idade: 25 };

for (const chave in pessoa) {
  console.log(chave, pessoa[chave]);
}
```

## Qual usar?

| Você quer... | Use |
|---|---|
| os valores de um array | `for...of` |
| as chaves de um objeto | `for...in` ou `Object.keys` |
| o índice numérico | `for` clássico |

> [warn] `for...in` em arrays devolve os **índices como texto** e pode incluir propriedades extras. Para arrays, use sempre `for...of`.
""",
 "task": r"""
Você tem:

```js
const frutas = ["maçã", "banana", "uva"];
const precos = { maca: 3, banana: 5, uva: 8 };
```

Crie:

- `listaFrutas` — array novo com cada fruta em maiúsculas (use `for...of` + `push`).
- `chaves` — array com as chaves de `precos` (use `for...in` + `push`).
- `somaPrecos` — soma de todos os valores de `precos` (percorra com `for...in`).
""",
 "starter": r"""const frutas = ["maçã", "banana", "uva"];
const precos = { maca: 3, banana: 5, uva: 8 };

const listaFrutas = [];
const chaves = [];
let somaPrecos = 0;

// use for...of e for...in


console.log(listaFrutas, chaves, somaPrecos);
""",
 "solution": r"""const frutas = ["maçã", "banana", "uva"];
const precos = { maca: 3, banana: 5, uva: 8 };

const listaFrutas = [];
const chaves = [];
let somaPrecos = 0;

for (const fruta of frutas) {
  listaFrutas.push(fruta.toUpperCase());
}

for (const chave in precos) {
  chaves.push(chave);
  somaPrecos += precos[chave];
}

console.log(listaFrutas, chaves, somaPrecos);
""",
 "hint": r"""No `for...in`, `chave` é o nome da propriedade (texto). Para pegar o valor: `precos[chave]`.""",
 "tests": [
   {"msg": "listaFrutas deve ser [\"MAÇÃ\", \"BANANA\", \"UVA\"]",
    "code": r"""JSON.stringify(listaFrutas) === JSON.stringify(["MAÇÃ","BANANA","UVA"])"""},
   {"msg": "chaves deve ser [\"maca\", \"banana\", \"uva\"]",
    "code": r"""JSON.stringify(chaves) === JSON.stringify(["maca","banana","uva"])"""},
   {"msg": "somaPrecos deve ser 16",
    "code": r"""somaPrecos === 16"""},
   {"msg": "Use for...of em arrays e for...in em objetos",
    "code": r"""/for\s*\(\s*(?:const|let)\s+\w+\s+of\s+/.test(__code) && /for\s*\(\s*(?:const|let)\s+\w+\s+in\s+/.test(__code)"""},
 ],
},

{
 "id": "m7l5",
 "title": "break e continue",
 "minutes": 7,
 "theory": r"""
## Parando antes: break

`break` encerra o loop imediatamente:

```js
const numeros = [3, 7, 12, 5, 18];
let primeiroMaiorQue10 = null;

for (const n of numeros) {
  if (n > 10) {
    primeiroMaiorQue10 = n;
    break;      // achou: não precisa continuar
  }
}
console.log(primeiroMaiorQue10);  // 12
```

## Pulando um item: continue

`continue` encerra **apenas a volta atual** e vai para a próxima:

```js
for (const n of numeros) {
  if (n % 2 === 0) continue;   // ignora os pares
  console.log(n);              // 3 7 5
}
```

## Cuidado com break em loops aninhados

`break` sai apenas do loop onde está. Para sair de dois, use uma variável de controle ou uma função com `return`.

```js
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i + j === 2) break;   // sai só do for de dentro
  }
}
```
""",
 "task": r"""
Você tem `const numeros = [3, 7, 12, 5, 18, 21];`.

1. Crie `primeiroPar` — o primeiro número par do array. Use `for...of` + `break`.
2. Crie `impares` — array só com os ímpares, pulando os pares com `continue`.
3. Crie `somaImpares` — a soma dos ímpares.
""",
 "starter": r"""const numeros = [3, 7, 12, 5, 18, 21];

let primeiroPar = null;
const impares = [];
let somaImpares = 0;

// use break e continue


console.log(primeiroPar, impares, somaImpares);
""",
 "solution": r"""const numeros = [3, 7, 12, 5, 18, 21];

let primeiroPar = null;
const impares = [];
let somaImpares = 0;

for (const n of numeros) {
  if (n % 2 === 0) {
    primeiroPar = n;
    break;
  }
}

for (const n of numeros) {
  if (n % 2 === 0) continue;
  impares.push(n);
  somaImpares += n;
}

console.log(primeiroPar, impares, somaImpares);
""",
 "hint": r"""No primeiro loop, o `break` precisa vir **depois** de guardar o valor — senão você sai antes de salvar.""",
 "tests": [
   {"msg": "primeiroPar deve ser 12",
    "code": r"""primeiroPar === 12"""},
   {"msg": "impares deve ser [3, 7, 5, 21]",
    "code": r"""JSON.stringify(impares) === JSON.stringify([3,7,5,21])"""},
   {"msg": "somaImpares deve ser 36",
    "code": r"""somaImpares === 36"""},
   {"msg": "Use break e continue",
    "code": r"""/break/.test(__code) && /continue/.test(__code)"""},
 ],
},

{
 "id": "m7l6",
 "title": "Desafio: FizzBuzz",
 "minutes": 12,
 "theory": r"""
## O exercício mais famoso da programação

A regra do FizzBuzz:

- números múltiplos de 3 → `"Fizz"`
- múltiplos de 5 → `"Buzz"`
- múltiplos de 3 **e** 5 → `"FizzBuzz"`
- os outros → o próprio número

```js
for (let i = 1; i <= 15; i++) {
  if (i % 15 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}
```

A ordem das condições é o segredo: o caso mais restrito (`% 15`) precisa vir **primeiro**, senão `i % 3` captura os múltiplos de 15 antes.

O FizzBuzz testa exatamente o que todo programa precisa: loop, condição, resto de divisão e ordem de avaliação.
""",
 "task": r"""
Crie o array `resultado` com o FizzBuzz de **1 a 15**.

Também crie:

- `quantidadeFizzBuzz` — quantas vezes a palavra `"FizzBuzz"` aparece.
- `somaNumeros` — a soma apenas dos itens que ficaram como número (1, 2, 4, 7, 8, 11, 13, 14).
""",
 "starter": r"""const resultado = [];

for (let i = 1; i <= 15; i++) {
  // sua lógica aqui
}

const quantidadeFizzBuzz = resultado.filter((r) => r === "FizzBuzz").length;
let somaNumeros = 0;

// calcule a soma dos itens numéricos


console.log(resultado, quantidadeFizzBuzz, somaNumeros);
""",
 "solution": r"""const resultado = [];

for (let i = 1; i <= 15; i++) {
  if (i % 15 === 0) {
    resultado.push("FizzBuzz");
  } else if (i % 3 === 0) {
    resultado.push("Fizz");
  } else if (i % 5 === 0) {
    resultado.push("Buzz");
  } else {
    resultado.push(i);
  }
}

const quantidadeFizzBuzz = resultado.filter((r) => r === "FizzBuzz").length;

let somaNumeros = 0;
for (const item of resultado) {
  if (typeof item === "number") somaNumeros += item;
}

console.log(resultado, quantidadeFizzBuzz, somaNumeros);
""",
 "hint": r"""Teste primeiro `i % 15 === 0`, depois `i % 3`, depois `i % 5`, e use `else` para o resto. Para a soma: `typeof item === "number"`.""",
 "tests": [
   {"msg": "resultado deve ter 15 itens",
    "code": r"""Array.isArray(resultado) && resultado.length === 15"""},
   {"msg": "Os 5 primeiros devem ser 1, 2, Fizz, 4, Buzz",
    "code": r"""JSON.stringify(resultado.slice(0,5)) === JSON.stringify([1,2,"Fizz",4,"Buzz"])"""},
   {"msg": "A posição 15 deve ser \"FizzBuzz\"",
    "code": r"""resultado[14] === "FizzBuzz" """},
   {"msg": "quantidadeFizzBuzz deve ser 1",
    "code": r"""quantidadeFizzBuzz === 1"""},
   {"msg": "somaNumeros deve ser 60",
    "code": r"""somaNumeros === 60"""},
 ],
},

]},
# =====================================================================
{
 "id": "numeros",
 "title": "Números, Math e Datas",
 "icon": "🔢",
 "lessons": [

{
 "id": "m8l1",
 "title": "Convertendo e formatando números",
 "minutes": 7,
 "theory": r"""
## Texto vira número

```js
Number("42");        // 42
Number("42.5");      // 42.5
Number("abc");       // NaN  (Not a Number)
parseInt("42px", 10);    // 42   (para no primeiro caractere inválido)
parseFloat("3.14kg");    // 3.14

+"42";               // 42   (o + converte)
```

## Número vira texto

```js
String(42);          // "42"
(42).toString();     // "42"
(3.14159).toFixed(2);   // "3.14"  (arredonda e devolve string)
(10).toFixed(2);        // "10.00"
```

## Precisão: cuidado com decimais

```js
console.log(0.1 + 0.2);        // 0.30000000000000004
console.log((0.1 + 0.2).toFixed(2));  // "0.30"
```

Isso não é bug do JavaScript: é como computadores representam números decimais (ponto flutuante binário). Para dinheiro, muitas empresas guardam centavos em inteiros.

> [tip] Sempre passe a base 10 no `parseInt("08", 10)` — evita surpresas históricas com números que começam com zero.
""",
 "task": r"""
Você tem:

```js
const textoNumero = "42";
const textoDecimal = "3.14159";
const textoComUnidade = "120px";
```

Crie:

- `inteiro` — `textoNumero` convertido com `Number`.
- `decimal` — `textoDecimal` convertido com `parseFloat`.
- `pixels` — `textoComUnidade` convertido com `parseInt` (base 10).
- `piArredondado` — o decimal com 2 casas, como texto (`toFixed`).
- `soma` — `inteiro + pixels` (deve ser número 162).
""",
 "starter": r"""const textoNumero = "42";
const textoDecimal = "3.14159";
const textoComUnidade = "120px";

// crie as variáveis


console.log(inteiro, decimal, pixels, piArredondado, soma);
""",
 "solution": r"""const textoNumero = "42";
const textoDecimal = "3.14159";
const textoComUnidade = "120px";

const inteiro = Number(textoNumero);
const decimal = parseFloat(textoDecimal);
const pixels = parseInt(textoComUnidade, 10);
const piArredondado = decimal.toFixed(2);
const soma = inteiro + pixels;

console.log(inteiro, decimal, pixels, piArredondado, soma);
""",
 "hint": r"""Se você não converter, `"42" + 120` resulta em `"42120"` (texto colado). Converta antes de somar.""",
 "tests": [
   {"msg": "inteiro deve ser o número 42",
    "code": r"""inteiro === 42 && typeof inteiro === "number" """},
   {"msg": "decimal deve ser 3.14159",
    "code": r"""decimal === 3.14159"""},
   {"msg": "pixels deve ser 120",
    "code": r"""pixels === 120"""},
   {"msg": "piArredondado deve ser \"3.14\"",
    "code": r"""piArredondado === "3.14" """},
   {"msg": "soma deve ser 162 (número, não texto)",
    "code": r"""soma === 162"""},
 ],
},

{
 "id": "m8l2",
 "title": "Math: arredondar, mínimo e máximo",
 "minutes": 7,
 "theory": r"""
## Arredondamentos

```js
Math.round(4.5);   // 5   (arredonda para o mais próximo)
Math.round(4.49);  // 4
Math.floor(4.9);   // 4   (para baixo, "chão")
Math.ceil(4.1);    // 5   (para cima, "teto")
Math.trunc(4.9);   // 4   (corta os decimais)
```

## Módulo e valor absoluto

```js
Math.abs(-7);      // 7
Math.min(3, 9, 1); // 1
Math.max(3, 9, 1); // 9
Math.max(...[3, 9, 1]);  // 9  (espalhando um array)
```

## Potência e raiz

```js
Math.pow(2, 10);   // 1024
2 ** 10;           // 1024 (operador moderno)
Math.sqrt(9);      // 3
```

## Constantes

```js
Math.PI;   // 3.141592653589793
Math.E;
```

> [tip] `Math.round` arredonda o .5 para cima. Para arredondar "comercialmente" (0,5 para cima) ele serve; para bancário, existem regras específicas.
""",
 "task": r"""
Você tem `const notas = [7.8, 5.5, 9.2, 6.1];`.

Crie:

- `arredondadas` — cada nota arredondada com `map` + `Math.round`.
- `paraBaixo` — cada nota com `Math.floor`.
- `paraCima` — cada nota com `Math.ceil`.
- `maior` — a maior nota (use `Math.max` com spread).
- `menor` — a menor nota.
- `diferenca` — `maior - menor` arredondada para 1 casa (`toFixed(1)`).
""",
 "starter": r"""const notas = [7.8, 5.5, 9.2, 6.1];

// crie as variáveis


console.log(arredondadas, paraBaixo, paraCima, maior, menor, diferenca);
""",
 "solution": r"""const notas = [7.8, 5.5, 9.2, 6.1];

const arredondadas = notas.map((n) => Math.round(n));
const paraBaixo = notas.map((n) => Math.floor(n));
const paraCima = notas.map((n) => Math.ceil(n));
const maior = Math.max(...notas);
const menor = Math.min(...notas);
const diferenca = (maior - menor).toFixed(1);

console.log(arredondadas, paraBaixo, paraCima, maior, menor, diferenca);
""",
 "hint": r"""`Math.max(...notas)` funciona porque o `...` espalha o array em argumentos separados.""",
 "tests": [
   {"msg": "arredondadas deve ser [8, 6, 9, 6]",
    "code": r"""JSON.stringify(arredondadas) === JSON.stringify([8,6,9,6])"""},
   {"msg": "paraBaixo deve ser [7, 5, 9, 6]",
    "code": r"""JSON.stringify(paraBaixo) === JSON.stringify([7,5,9,6])"""},
   {"msg": "paraCima deve ser [8, 6, 10, 7]",
    "code": r"""JSON.stringify(paraCima) === JSON.stringify([8,6,10,7])"""},
   {"msg": "maior deve ser 9.2 e menor deve ser 5.5",
    "code": r"""maior === 9.2 && menor === 5.5"""},
   {"msg": "diferenca deve ser \"3.7\"",
    "code": r"""diferenca === "3.7" """},
 ],
},

{
 "id": "m8l3",
 "title": "Números aleatórios",
 "minutes": 6,
 "theory": r"""
## Math.random

`Math.random()` devolve um número decimal entre **0 (inclusive) e 1 (exclusive)**:

```js
Math.random();  // 0.4729...
Math.random();  // 0.0183...
```

## Sorteando inteiros

A receita para sortear de `min` a `max`, ambos inclusive:

```js
function sortear(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

sortear(1, 6);    // 1 a 6 (dado)
sortear(1, 60);   // 1 a 60 (megasena)
```

Entendendo as partes:

1. `Math.random()` → 0 até quase 1.
2. `* (max - min + 1)` → 0 até quase (quantidade de valores).
3. `Math.floor(...)` → 0 até (quantidade - 1), inteiro.
4. `+ min` → desloca para o intervalo desejado.

> [warn] `Math.random()` **não** é criptograficamente seguro. Para senhas e tokens, use `crypto.getRandomValues()`.
""",
 "task": r"""
1. Crie a função `sortear(min, max)` que devolve um inteiro aleatório entre `min` e `max`, inclusive.
2. Crie o array `dados` com **10** resultados de `sortear(1, 6)` (use um `for`).
3. Crie `todosValidos` — `true` se todos os valores estiverem entre 1 e 6 (use `every`).
""",
 "starter": r"""function sortear(min, max) {
  // seu código
}

const dados = [];

// preencha com 10 sorteios

const todosValidos = dados.every((n) => Number.isInteger(n) && n >= 1 && n <= 6);

console.log(dados, todosValidos);
""",
 "solution": r"""function sortear(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

const dados = [];

for (let i = 0; i < 10; i++) {
  dados.push(sortear(1, 6));
}

const todosValidos = dados.every((n) => Number.isInteger(n) && n >= 1 && n <= 6);

console.log(dados, todosValidos);
""",
 "hint": r"""A fórmula completa é `Math.floor(Math.random() * (max - min + 1)) + min` — o `+ 1` é o que inclui o `max` no sorteio.""",
 "tests": [
   {"msg": "sortear(1, 6) deve sempre devolver inteiro de 1 a 6",
    "code": r"""(function(){ for(let i=0;i<200;i++){ const n = sortear(1,6); if(!Number.isInteger(n) || n < 1 || n > 6) return false; } return true; })()"""},
   {"msg": "sortear(10, 10) deve devolver 10",
    "code": r"""sortear(10, 10) === 10"""},
   {"msg": "dados deve ter 10 itens válidos",
    "code": r"""dados.length === 10 && dados.every(function(n){ return Number.isInteger(n) && n >= 1 && n <= 6; })"""},
   {"msg": "todosValidos deve ser true",
    "code": r"""todosValidos === true"""},
   {"msg": "Use Math.random e Math.floor",
    "code": r"""/Math\.random/.test(__code) && /Math\.floor/.test(__code)"""},
 ],
},

{
 "id": "m8l4",
 "title": "NaN e verificações numéricas",
 "minutes": 7,
 "theory": r"""
## NaN: o valor "não é número"

```js
Number("abc");     // NaN
0 / 0;             // NaN
parseInt("xyz");   // NaN
```

O detalhe perigoso: **NaN não é igual a nada — nem a si mesmo**.

```js
NaN === NaN;       // false!
```

Por isso existe `Number.isNaN()`:

```js
Number.isNaN(NaN);            // true
Number.isNaN("abc");          // false  (não é número? então nem tenta)
Number.isNaN(Number("abc"));  // true
```

Atenção: o `isNaN` global (sem `Number.`) converte o valor antes de testar e dá resultados esquisitos: `isNaN("abc")` é `true`, mas `isNaN("123")` é `false`. **Use sempre `Number.isNaN`**.

## Outras verificações

```js
Number.isInteger(10);      // true
Number.isInteger(10.5);    // false
Number.isFinite(10);       // true
Number.isFinite(Infinity); // false
Number.parseFloat("1e3");  // 1000 (notação científica)
```

## Infinito

```js
1 / 0;    // Infinity
-1 / 0;   // -Infinity
```
""",
 "task": r"""
Você tem:

```js
const entradas = ["42", "abc", "7.5", "", "100"];
```

Crie:

- `convertidos` — cada entrada convertida com `Number` (`map`).
- `invalidos` — só os que viraram `NaN` (use `filter` + `Number.isNaN`).
- `quantidadeInvalidos` — quantos são inválidos.
- `todosInteiros` — `true` se **todos** os válidos forem inteiros (dica: filtre os válidos e use `every` com `Number.isInteger`).
""",
 "starter": r"""const entradas = ["42", "abc", "7.5", "", "100"];

// crie as variáveis


console.log(convertidos, invalidos, quantidadeInvalidos, todosInteiros);
""",
 "solution": r"""const entradas = ["42", "abc", "7.5", "", "100"];

const convertidos = entradas.map((e) => Number(e));
const invalidos = convertidos.filter((n) => Number.isNaN(n));
const quantidadeInvalidos = invalidos.length;
const validos = convertidos.filter((n) => !Number.isNaN(n));
const todosInteiros = validos.every((n) => Number.isInteger(n));

console.log(convertidos, invalidos, quantidadeInvalidos, todosInteiros);
""",
 "hint": r"""`Number("")` é `0` (atenção!), então `""` **não** vira NaN. Os inválidos aqui são `"abc"` e `"7.5"`? Não: `"7.5"` vira 7.5, que é válido mas não é inteiro.""",
 "tests": [
   {"msg": "convertidos deve ter [42, NaN, 7.5, 0, 100] (o NaN é o segundo)",
    "code": r"""convertidos.length === 5 && convertidos[0] === 42 && Number.isNaN(convertidos[1]) && convertidos[2] === 7.5 && convertidos[3] === 0 && convertidos[4] === 100"""},
   {"msg": "invalidos deve ter 1 item (o NaN)",
    "code": r"""invalidos.length === 1 && Number.isNaN(invalidos[0])"""},
   {"msg": "quantidadeInvalidos deve ser 1",
    "code": r"""quantidadeInvalidos === 1"""},
   {"msg": "todosInteiros deve ser false (7.5 não é inteiro)",
    "code": r"""todosInteiros === false"""},
   {"msg": "Use Number.isNaN",
    "code": r"""/Number\.isNaN/.test(__code)"""},
 ],
},

{
 "id": "m8l5",
 "title": "Datas",
 "minutes": 8,
 "theory": r"""
## Criando datas

```js
const agora = new Date();                 // agora
const natal = new Date(2026, 11, 25);     // ano, mês, dia
const outra = new Date("2026-01-15");     // texto ISO (UTC)
```

> [warn] **Meses começam em 0!** Janeiro é `0`, dezembro é `11`. É uma das maiores fontes de bug em JavaScript.

## Lendo partes

```js
const d = new Date(2026, 0, 15);   // 15 de janeiro de 2026

d.getFullYear();   // 2026
d.getMonth();      // 0    (janeiro)
d.getDate();       // 15   (dia do mês)
d.getDay();        // 4    (dia da semana: 0 = domingo)
d.getHours();      // 0
```

## Calculando diferenças

Datas viram números (milissegundos desde 01/01/1970) quando você faz contas:

```js
const inicio = new Date(2026, 0, 1);
const fim = new Date(2026, 0, 11);

const dias = (fim - inicio) / (1000 * 60 * 60 * 24);
console.log(dias);  // 10
```

## Formatando

```js
d.toLocaleDateString("pt-BR");   // "15/01/2026"
d.toISOString();                 // "2026-01-15T03:00:00.000Z"
```
""",
 "task": r"""
Você tem:

```js
const nascimento = new Date(2001, 4, 12);   // 12 de maio de 2001
const hoje = new Date(2026, 10, 12);        // 12 de novembro de 2026
```

Crie:

- `ano`, `mes`, `dia` — partes da data de nascimento (`getFullYear`, `getMonth`, `getDate`).
- `mesHumano` — o mês somando 1 (para ficar de 1 a 12).
- `diasVividos` — a diferença em dias entre `hoje` e `nascimento`.
- `dataFormatada` — `nascimento` no formato `"12/5/2001"` (use `getDate`, `getMonth`+1 e `getFullYear` com template string).
""",
 "starter": r"""const nascimento = new Date(2001, 4, 12);
const hoje = new Date(2026, 10, 12);

// crie as variáveis


console.log(ano, mes, dia, mesHumano, diasVividos, dataFormatada);
""",
 "solution": r"""const nascimento = new Date(2001, 4, 12);
const hoje = new Date(2026, 10, 12);

const ano = nascimento.getFullYear();
const mes = nascimento.getMonth();
const dia = nascimento.getDate();
const mesHumano = mes + 1;
const diasVividos = (hoje - nascimento) / (1000 * 60 * 60 * 24);
const dataFormatada = `${dia}/${mesHumano}/${ano}`;

console.log(ano, mes, dia, mesHumano, diasVividos, dataFormatada);
""",
 "hint": r"""Maio é o mês 4 (porque janeiro é 0). A diferença de datas em milissegundos dividida por `1000*60*60*24` dá dias.""",
 "tests": [
   {"msg": "ano deve ser 2001, mes deve ser 4 e dia deve ser 12",
    "code": r"""ano === 2001 && mes === 4 && dia === 12"""},
   {"msg": "mesHumano deve ser 5",
    "code": r"""mesHumano === 5"""},
   {"msg": "diasVividos deve ser 9331",
    "code": r"""diasVividos === 9315"""},
   {"msg": "dataFormatada deve ser \"12/5/2001\"",
    "code": r"""dataFormatada === "12/5/2001" """},
 ],
},

{
 "id": "m8l6",
 "title": "Desafio: calculadora de orçamento",
 "minutes": 12,
 "theory": r"""
## Juntando números, arrays e objetos

Um orçamento simples: uma lista de itens, cada um com quantidade e preço. O total precisa de soma, desconto e formatação.

```js
const itens = [
  { nome: "Caneta", qtd: 10, preco: 2.5 },
  { nome: "Caderno", qtd: 2, preco: 25 },
];

const subtotal = itens.reduce((soma, i) => soma + i.qtd * i.preco, 0);
const comDesconto = subtotal * 0.9;
console.log(`Total: R$ ${comDesconto.toFixed(2).replace(".", ",")}`);
```

Note o cuidado com dinheiro: calcular com números e **formatar só no final**, com `toFixed(2)`.
""",
 "task": r"""
Você tem:

```js
const itens = [
  { nome: "Caneta", qtd: 10, preco: 2.5 },
  { nome: "Caderno", qtd: 2, preco: 25 },
  { nome: "Mochila", qtd: 1, preco: 120 },
];
```

Crie:

- `subtotal` — soma de `qtd * preco` de todos os itens (`reduce`).
- `totalItens` — soma das quantidades.
- `desconto` — 10% do subtotal.
- `total` — subtotal menos desconto.
- `totalFormatado` — o total como `"R$ 159,75"` (duas casas, vírgula).
- `maisCaro` — o item de maior **valor total** (`qtd * preco`).
""",
 "starter": r"""const itens = [
  { nome: "Caneta", qtd: 10, preco: 2.5 },
  { nome: "Caderno", qtd: 2, preco: 25 },
  { nome: "Mochila", qtd: 1, preco: 120 },
];

// crie as variáveis


console.log(subtotal, totalItens, desconto, total, totalFormatado, maisCaro.nome);
""",
 "solution": r"""const itens = [
  { nome: "Caneta", qtd: 10, preco: 2.5 },
  { nome: "Caderno", qtd: 2, preco: 25 },
  { nome: "Mochila", qtd: 1, preco: 120 },
];

const subtotal = itens.reduce((soma, i) => soma + i.qtd * i.preco, 0);
const totalItens = itens.reduce((soma, i) => soma + i.qtd, 0);
const desconto = subtotal * 0.1;
const total = subtotal - desconto;
const totalFormatado = `R$ ${total.toFixed(2).replace(".", ",")}`;
const maisCaro = itens.reduce(
  (maior, i) => (i.qtd * i.preco > maior.qtd * maior.preco ? i : maior),
  itens[0]
);

console.log(subtotal, totalItens, desconto, total, totalFormatado, maisCaro.nome);
""",
 "hint": r"""Subtotal: 25 + 50 + 120 = 195. Desconto de 10% = 19,5; total = 175,5. Formate com `toFixed(2).replace(".", ",")`.""",
 "tests": [
   {"msg": "subtotal deve ser 195",
    "code": r"""subtotal === 195"""},
   {"msg": "totalItens deve ser 13",
    "code": r"""totalItens === 13"""},
   {"msg": "desconto deve ser 19.5",
    "code": r"""Math.abs(desconto - 19.5) < 1e-9"""},
   {"msg": "total deve ser 175.5",
    "code": r"""Math.abs(total - 175.5) < 1e-9"""},
   {"msg": "totalFormatado deve ser \"R$ 175,50\"",
    "code": r"""totalFormatado === "R$ 175,50" """},
   {"msg": "maisCaro deve ser a Mochila",
    "code": r"""maisCaro && maisCaro.nome === "Mochila" """},
 ],
},

]},
# =====================================================================
{
 "id": "dom",
 "title": "O DOM e o navegador",
 "icon": "🌐",
 "lessons": [

{
 "id": "m9l1",
 "title": "Selecionando elementos",
 "minutes": 8,
 "html": r"""<h1 id="titulo">Minha página</h1>
<p class="texto">Primeiro parágrafo</p>
<p class="texto">Segundo parágrafo</p>
<button id="botao">Clique aqui</button>""",
 "theory": r"""
## O que é o DOM

Quando o navegador lê o HTML, ele monta uma árvore de objetos chamada **DOM** (Document Object Model). O JavaScript conversa com a página através dessa árvore: cada tag vira um objeto que você pode ler e alterar.

Nesta lição a aba **Página** mostra o HTML de exemplo ao lado. Ele existe dentro da sandbox — pode mexer sem medo.

## Selecionando

```js
const titulo = document.getElementById("titulo");
const botao = document.querySelector("#botao");
const paragrafos = document.querySelectorAll(".texto");
```

- `getElementById("id")` — pega um elemento pelo `id`.
- `querySelector("seletor")` — pega o **primeiro** que casa com um seletor CSS (`.classe`, `#id`, `div > p`, etc.).
- `querySelectorAll("seletor")` — pega **todos**, numa NodeList (parecida com array; use `forEach` ou `Array.from`).

## Conferindo o resultado

```js
console.log(titulo.textContent);   // Minha página
console.log(paragrafos.length);    // 2
```

> [warn] Se o elemento não existir, `getElementById` devolve `null` — e acessar `.textContent` de `null` gera erro. Sempre confira a grafia do id.
""",
 "task": r"""
Na página ao lado existem um `h1#titulo`, dois `p.texto` e um `button#botao`.

Crie:

- `titulo` — o elemento pelo id (`getElementById`).
- `paragrafos` — todos os elementos com a classe `texto` (`querySelectorAll`).
- `botao` — o botão usando `querySelector("#botao")`.
- `qtdParagrafos` — quantos parágrafos existem.

Imprima `titulo.textContent` e `qtdParagrafos`.
""",
 "starter": r"""// 1. selecione os elementos


// 2. quantos parágrafos existem?


console.log(titulo.textContent, qtdParagrafos);
""",
 "solution": r"""const titulo = document.getElementById("titulo");
const paragrafos = document.querySelectorAll(".texto");
const botao = document.querySelector("#botao");
const qtdParagrafos = paragrafos.length;

console.log(titulo.textContent, qtdParagrafos);
""",
 "hint": r"""`querySelectorAll` devolve uma NodeList com `.length`, igual a um array.""",
 "tests": [
   {"msg": "titulo deve ser o elemento h1",
    "code": r"""titulo && titulo.tagName === "H1" && titulo.textContent === "Minha página" """},
   {"msg": "paragrafos deve conter 2 elementos",
    "code": r"""paragrafos && paragrafos.length === 2 && paragrafos[0].textContent === "Primeiro parágrafo" """},
   {"msg": "botao deve ser o elemento button",
    "code": r"""botao && botao.tagName === "BUTTON" """},
   {"msg": "qtdParagrafos deve ser 2",
    "code": r"""qtdParagrafos === 2"""},
   {"msg": "Use getElementById e querySelector(All)",
    "code": r"""/getElementById/.test(__code) && /querySelector/.test(__code)"""},
 ],
},

{
 "id": "m9l2",
 "title": "Alterando texto e conteúdo",
 "minutes": 8,
 "html": r"""<h1 id="titulo">Título antigo</h1>
<p id="descricao">Uma descrição qualquer.</p>
<ul id="lista">
  <li>Item 1</li>
</ul>""",
 "theory": r"""
## textContent: o texto puro

```js
const titulo = document.getElementById("titulo");
titulo.textContent = "Novo título";
```

`textContent` lê e escreve o texto **sem interpretar HTML**. Se você escrever `"<b>oi</b>"`, aparece literalmente `<b>oi</b>` na tela. É a opção segura.

## innerHTML: o conteúdo como HTML

```js
const lista = document.getElementById("lista");
lista.innerHTML = "<li>Novo item</li>";
```

`innerHTML` interpreta a string como HTML — útil, mas **perigoso**: se o texto vier de um usuário, ele pode injetar scripts (ataque chamado XSS).

```js
// NUNCA faça isso com dados de usuário:
elemento.innerHTML = comentarioDoUsuario;
```

## innerText e value

```js
elemento.innerText;        // texto visível (considera CSS)
input.value;               // valor de campos de formulário
input.value = "novo";      // define o valor
```

> [tip] Regra de ouro: para texto, `textContent`; para HTML que **você** controla, `innerHTML`; para campos de formulário, `value`.
""",
 "task": r"""
Na página ao lado:

1. Troque o texto do `h1#titulo` para `"JavaScript no navegador"` (use `textContent`).
2. Troque o conteúdo da `ul#lista` por dois itens: `<li>HTML</li><li>CSS</li>` (use `innerHTML`).
3. Troque o texto do `p#descricao` para `"Aprendendo DOM"`.
""",
 "starter": r"""const titulo = document.getElementById("titulo");
const lista = document.getElementById("lista");
const descricao = document.getElementById("descricao");

// 1, 2 e 3 aqui


console.log(titulo.textContent, lista.children.length);
""",
 "solution": r"""const titulo = document.getElementById("titulo");
const lista = document.getElementById("lista");
const descricao = document.getElementById("descricao");

titulo.textContent = "JavaScript no navegador";
lista.innerHTML = "<li>HTML</li><li>CSS</li>";
descricao.textContent = "Aprendendo DOM";

console.log(titulo.textContent, lista.children.length);
""",
 "hint": r"""`lista.innerHTML = "<li>HTML</li><li>CSS</li>"` substitui tudo o que havia dentro da `ul`.""",
 "tests": [
   {"msg": "O título deve ter sido alterado com textContent",
    "code": r"""document.getElementById("titulo").textContent === "JavaScript no navegador" && /textContent/.test(__code)"""},
   {"msg": "A lista deve ter 2 itens criados com innerHTML",
    "code": r"""document.querySelectorAll("#lista li").length === 2 && document.querySelectorAll("#lista li")[1].textContent === "CSS" && /innerHTML/.test(__code)"""},
   {"msg": "A descrição deve ser \"Aprendendo DOM\"",
    "code": r"""document.getElementById("descricao").textContent === "Aprendendo DOM" """},
 ],
},

{
 "id": "m9l3",
 "title": "Classes e estilos",
 "minutes": 8,
 "html": r"""<div id="caixa">Conteúdo da caixa</div>
<style>
  #caixa { padding: 8px; border: 2px solid #c9d1d9; border-radius: 6px; margin-bottom: 8px; }
  .destaque { background: #fff3bf; font-weight: 700; }
  .oculto { display: none; }
</style>""",
 "theory": r"""
## classList: mexendo nas classes

```js
const caixa = document.getElementById("caixa");

caixa.classList.add("destaque");      // adiciona
caixa.classList.remove("destaque");   // remove
caixa.classList.toggle("destaque");   // liga/desliga
caixa.classList.contains("destaque"); // true/false
```

Trabalhar com classes é a forma preferida de mudar aparência: você escreve o estilo no CSS e só liga/desliga a classe no JavaScript.

## style: estilo direto

```js
caixa.style.backgroundColor = "yellow";
caixa.style.padding = "16px";
caixa.style.borderLeft = "4px solid red";
```

No JavaScript, propriedades CSS com hífen viram camelCase: `background-color` → `backgroundColor`, `font-size` → `fontSize`.

## Atributos

```js
caixa.setAttribute("data-estado", "ativo");
caixa.getAttribute("data-estado");   // "ativo"
caixa.dataset.estado;                // "ativo"  (atalho para data-*)
```
""",
 "task": r"""
Na página ao lado existe `div#caixa`.

1. Adicione a classe `destaque` na caixa.
2. Defina `caixa.style.color = "darkred"` e `caixa.style.padding = "16px"`.
3. Guarde em `temDestaque` o resultado de `classList.contains("destaque")`.
4. Guarde em `estado` o atributo `data-estado` definido como `"pronto"` (use `setAttribute` e depois `getAttribute`).
""",
 "starter": r"""const caixa = document.getElementById("caixa");

// 1. adicione a classe destaque


// 2. altere cor e padding


// 3. temDestaque


// 4. data-estado -> estado


console.log(temDestaque, estado);
""",
 "solution": r"""const caixa = document.getElementById("caixa");

caixa.classList.add("destaque");
caixa.style.color = "darkred";
caixa.style.padding = "16px";

const temDestaque = caixa.classList.contains("destaque");

caixa.setAttribute("data-estado", "pronto");
const estado = caixa.getAttribute("data-estado");

console.log(temDestaque, estado);
""",
 "hint": r"""`classList.add("destaque")` não apaga as classes que já existem — ele só acrescenta.""",
 "tests": [
   {"msg": "A caixa deve ter a classe destaque",
    "code": r"""document.getElementById("caixa").classList.contains("destaque")"""},
   {"msg": "temDestaque deve ser true",
    "code": r"""temDestaque === true"""},
   {"msg": "O padding deve ter sido alterado para 16px",
    "code": r"""document.getElementById("caixa").style.padding === "16px" """},
   {"msg": "A cor deve ter sido alterada",
    "code": r"""document.getElementById("caixa").getAttribute("style").includes("darkred")"""},
   {"msg": "estado deve ser \"pronto\"",
    "code": r"""estado === "pronto" """},
   {"msg": "Use setAttribute para data-estado",
    "code": r"""/setAttribute\s*\(\s*["']data-estado/.test(__code)"""},
 ],
},

{
 "id": "m9l4",
 "title": "Criando e inserindo elementos",
 "minutes": 9,
 "html": r"""<h2>Lista de tarefas</h2>
<ul id="lista"></ul>""",
 "theory": r"""
## O caminho: criar, configurar, inserir

```js
const lista = document.getElementById("lista");

const item = document.createElement("li");
item.textContent = "Estudar JavaScript";
item.classList.add("tarefa");

lista.appendChild(item);
```

Três passos, sempre:

1. `document.createElement("li")` — cria o elemento (ainda fora da página).
2. Configure (`textContent`, `classList`, atributos...).
3. Insira com `append` ou `appendChild` no elemento pai.

## Vários de uma vez

```js
const tarefas = ["Estudar", "Praticar", "Revisar"];

tarefas.forEach((texto) => {
  const li = document.createElement("li");
  li.textContent = texto;
  lista.appendChild(li);
});
```

## Métodos de inserção

```js
pai.appendChild(filho);   // insere no fim (método clássico)
pai.append(filho, "texto");  // aceita vários itens e texto
pai.prepend(filho);          // insere no início
filho.remove();              // remove o elemento
```

> [tip] Prefira `append`/`prepend` (modernos, aceitam vários argumentos) a `appendChild` (um por vez). Os dois funcionam.
""",
 "task": r"""
Na página ao lado existe uma `ul#lista` vazia.

Crie um array `tarefas = ["Estudar", "Praticar", "Revisar"]` e, com um `forEach`:

1. `document.createElement("li")` para cada tarefa.
2. Defina o `textContent` com o texto.
3. Insira na lista com `appendChild`.

No final, guarde em `qtdItens` a quantidade de `li` dentro da lista.
""",
 "starter": r"""const lista = document.getElementById("lista");
const tarefas = ["Estudar", "Praticar", "Revisar"];

// crie os itens e insira na lista


const qtdItens = lista.querySelectorAll("li").length;
console.log(qtdItens);
""",
 "solution": r"""const lista = document.getElementById("lista");
const tarefas = ["Estudar", "Praticar", "Revisar"];

tarefas.forEach((texto) => {
  const li = document.createElement("li");
  li.textContent = texto;
  lista.appendChild(li);
});

const qtdItens = lista.querySelectorAll("li").length;
console.log(qtdItens);
""",
 "hint": r"""Crie o `li` **dentro** do `forEach`, para que cada volta crie um elemento novo.""",
 "tests": [
   {"msg": "Devem existir 3 itens na lista",
    "code": r"""document.querySelectorAll("#lista li").length === 3"""},
   {"msg": "Os textos devem ser Estudar, Praticar e Revisar",
    "code": r"""Array.from(document.querySelectorAll("#lista li")).map(function(li){ return li.textContent; }).join("|") === "Estudar|Praticar|Revisar" """},
   {"msg": "qtdItens deve ser 3",
    "code": r"""qtdItens === 3"""},
   {"msg": "Use createElement e appendChild (ou append)",
    "code": r"""/createElement/.test(__code) && /(appendChild|append|prepend)/.test(__code)"""},
 ],
},

{
 "id": "m9l5",
 "title": "Eventos de clique",
 "minutes": 9,
 "html": r"""<button id="botao">+1</button>
<p>Cliques: <span id="contador">0</span></p>
<div id="demo" style="margin-top:10px"></div>""",
 "theory": r"""
## Escutando eventos

Um **evento** é algo que acontece na página: clique, digitação, envio de formulário, tempo. Você registra uma função para ser chamada quando ele ocorrer:

```js
const botao = document.getElementById("botao");

botao.addEventListener("click", () => {
  console.log("cliquei!");
});
```

A função passada é um **callback**: você entrega para o navegador e ele chama quando o evento acontecer.

## Atualizando a página

```js
let cliques = 0;
const contador = document.getElementById("contador");

botao.addEventListener("click", () => {
  cliques++;
  contador.textContent = cliques;
});
```

## O objeto do evento

```js
botao.addEventListener("click", (evento) => {
  console.log(evento.target);   // o elemento clicado
  evento.preventDefault();      // impede o comportamento padrão
});
```

Eventos mais comuns: `click`, `input`, `change`, `submit`, `keydown`, `mouseover`, `load`.

> [tip] Dica: `elemento.click()` dispara um clique por código — é assim que os testes desta lição vão conferir seu código.
""",
 "task": r"""
Na página ao lado existem o botão `#botao`, o `#contador` e a div `#demo`.

1. Crie `let cliques = 0;`
2. No clique do botão: incremente `cliques` e atualize o `textContent` do `#contador`.
3. Quando os cliques chegarem a 3, coloque no `#demo` o texto `"Você clicou 3 vezes!"`.
""",
 "starter": r"""const botao = document.getElementById("botao");
const contador = document.getElementById("contador");
const demo = document.getElementById("demo");

let cliques = 0;

// registre o addEventListener


console.log("pronto");
""",
 "solution": r"""const botao = document.getElementById("botao");
const contador = document.getElementById("contador");
const demo = document.getElementById("demo");

let cliques = 0;

botao.addEventListener("click", () => {
  cliques++;
  contador.textContent = cliques;

  if (cliques === 3) {
    demo.textContent = "Você clicou 3 vezes!";
  }
});

console.log("pronto");
""",
 "hint": r"""O código dentro do `addEventListener` só roda quando o clique acontece — por isso o teste "clica" no botão para conferir.""",
 "tests": [
   {"msg": "Um clique deve atualizar o contador para 1",
    "code": r"""(function(){ const b = document.getElementById("botao"); b.click(); return document.getElementById("contador").textContent === "1"; })()"""},
   {"msg": "Três cliques devem mostrar a mensagem na div demo",
    "code": r"""(function(){ const b = document.getElementById("botao"); b.click(); b.click(); b.click(); return document.getElementById("contador").textContent === "4" && document.getElementById("demo").textContent === "Você clicou 3 vezes!"; })()"""},
   {"msg": "Use addEventListener com o evento click",
    "code": r"""/addEventListener\s*\(\s*["']click["']/.test(__code)"""},
 ],
},

{
 "id": "m9l6",
 "title": "Formulários e input",
 "minutes": 9,
 "html": r"""<input id="nome" placeholder="Digite seu nome">
<button id="enviar">Enviar</button>
<p id="saida"></p>""",
 "theory": r"""
## Lendo o que o usuário digitou

Campos de formulário guardam o valor em `.value`:

```js
const campo = document.getElementById("nome");
console.log(campo.value);   // "" no começo
```

Diferente de `textContent`, `.value` é sempre texto (string) — e é atualizado conforme a pessoa digita.

## Os dois eventos principais

```js
// a cada tecla
campo.addEventListener("input", () => {
  console.log(campo.value);
});

// quando termina e o campo perde o foco
campo.addEventListener("change", () => { ... });
```

## Validando e mostrando

```js
const botao = document.getElementById("enviar");
const saida = document.getElementById("saida");

botao.addEventListener("click", () => {
  const valor = campo.value.trim();

  if (valor === "") {
    saida.textContent = "Digite um nome!";
    return;               // sai da função sem continuar
  }

  saida.textContent = `Olá, ${valor}!`;
});
```

> [tip] Sempre `.trim()` no que vem de formulário: o usuário pode digitar só espaços.
""",
 "task": r"""
Na página existem `input#nome`, `button#enviar` e `p#saida`.

No clique do botão:

1. Leia `nome.value` e aplique `.trim()`.
2. Se estiver vazio, escreva `"Digite um nome"` no `#saida`.
3. Senão, escreva `Olá, {nome}!` no `#saida`.
4. Depois de mostrar a saudação, limpe o campo (`nome.value = ""`).
""",
 "starter": r"""const campo = document.getElementById("nome");
const enviar = document.getElementById("enviar");
const saida = document.getElementById("saida");

enviar.addEventListener("click", () => {
  // seu código aqui
});
""",
 "solution": r"""const campo = document.getElementById("nome");
const enviar = document.getElementById("enviar");
const saida = document.getElementById("saida");

enviar.addEventListener("click", () => {
  const valor = campo.value.trim();

  if (valor === "") {
    saida.textContent = "Digite um nome";
    return;
  }

  saida.textContent = `Olá, ${valor}!`;
  campo.value = "";
});
""",
 "hint": r"""Use `return` dentro do `if` para sair sem executar a saudação quando o campo estiver vazio.""",
 "tests": [
   {"msg": "Com o campo vazio, deve mostrar \"Digite um nome\"",
    "code": r"""(function(){ document.getElementById("saida").textContent = ""; const campo = document.getElementById("nome"); campo.value = "   "; document.getElementById("enviar").click(); return document.getElementById("saida").textContent === "Digite um nome"; })()"""},
   {"msg": "Com um nome, deve mostrar a saudação",
    "code": r"""(function(){ const campo = document.getElementById("nome"); campo.value = "Ana"; document.getElementById("enviar").click(); return document.getElementById("saida").textContent === "Olá, Ana!"; })()"""},
   {"msg": "O campo deve ser limpo depois do envio",
    "code": r"""document.getElementById("nome").value === "" """},
   {"msg": "Use .value e .trim()",
    "code": r"""/\.value/.test(__code) && /trim\(\)/.test(__code)"""},
 ],
},

]},
]
