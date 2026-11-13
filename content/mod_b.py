# -*- coding: utf-8 -*-
"""Módulos 4 a 6 — Arrays, objetos e strings."""

MODULES = [

# =====================================================================
{
 "id": "arrays",
 "title": "Arrays",
 "icon": "📚",
 "lessons": [

{
 "id": "m4l1",
 "title": "Criando e acessando arrays",
 "minutes": 7,
 "theory": r"""
## Listas

Um **array** é uma lista ordenada de valores. Em JavaScript ele é escrito entre colchetes:

```js
const frutas = ["maçã", "banana", "uva"];
const numeros = [10, 20, 30, 40];
const misturado = ["Ana", 25, true];   // tipos diferentes podem conviver
const vazio = [];
```

Cada posição tem um **índice**, que começa em **zero**:

```js
console.log(frutas[0]);  // maçã
console.log(frutas[1]);  // banana
console.log(frutas[3]);  // undefined (não existe)
```

## Tamanho e último item

```js
console.log(frutas.length);                  // 3
console.log(frutas[frutas.length - 1]);      // uva  ← última posição
```

O `.length` é atualizado automaticamente: ele sempre diz quantos itens o array tem. O último índice é `length - 1`, porque o primeiro é 0.

## Alterando um item

```js
frutas[1] = "morango";
console.log(frutas); // ["maçã", "morango", "uva"]
```

> [warn] `const` impede trocar o array por outro, mas **não** impede alterar o conteúdo: `frutas[0] = "pera"` funciona. Use `Object.freeze()` se quiser bloquear de verdade.
""",
 "task": r"""
Crie um array chamado `cores` com **três cores** (textos) à sua escolha, e depois:

- `primeira` — a primeira cor (índice 0).
- `ultima` — a última cor, usando `cores.length - 1` (não escreva o número na mão).
- `quantidade` — quantos itens o array tem.

Imprima as três variáveis.
""",
 "starter": r"""// 1. crie o array cores


// 2. primeira, ultima e quantidade


console.log(primeira, ultima, quantidade);
""",
 "solution": r"""const cores = ["azul", "verde", "vermelho"];

const primeira = cores[0];
const ultima = cores[cores.length - 1];
const quantidade = cores.length;

console.log(primeira, ultima, quantidade);
""",
 "hint": r"""A última posição é `cores[cores.length - 1]`. Escrever `cores[-1]` não funciona em JavaScript (devolve `undefined`).""",
 "tests": [
   {"msg": "Crie um array `cores` com 3 itens",
    "code": r"""Array.isArray(cores) && cores.length === 3"""},
   {"msg": "primeira deve ser o primeiro item do array",
    "code": r"""primeira === cores[0]"""},
   {"msg": "ultima deve ser o último item (use length - 1)",
    "code": r"""ultima === cores[2] && /length\s*-\s*1/.test(__code)"""},
   {"msg": "quantidade deve ser 3",
    "code": r"""quantidade === 3"""},
 ],
},

{
 "id": "m4l2",
 "title": "Adicionando e removendo itens",
 "minutes": 8,
 "theory": r"""
## No fim da lista

```js
const fila = ["Ana", "Bruno"];

fila.push("Carla");     // adiciona no fim
console.log(fila);      // ["Ana", "Bruno", "Carla"]

const ultimo = fila.pop();   // remove e devolve o último
console.log(ultimo);         // Carla
console.log(fila);           // ["Ana", "Bruno"]
```

## No começo da lista

```js
fila.unshift("Davi");   // adiciona no início → ["Davi", "Ana", "Bruno"]
const primeiro = fila.shift();  // remove e devolve o primeiro → "Davi"
```

## Resumo

| Método | Onde age | O que devolve |
|---|---|---|
| `push(item)` | fim | novo `length` |
| `pop()` | fim | o item removido |
| `unshift(item)` | início | novo `length` |
| `shift()` | início | o item removido |

Todos esses métodos **alteram** o array original (são mutáveis) e são rápidos no fim, mas `shift`/`unshift` precisam reindexar tudo — em listas gigantes, prefira `push`/`pop`.

> [tip] `push` e `unshift` aceitam vários itens: `fila.push("Carla", "Davi")`.
""",
 "task": r"""
Você tem a fila de atendimento:

```js
const fila = ["Ana", "Bruno"];
```

Faça, nesta ordem:

1. Adicione `"Carla"` no **fim**.
2. Remova a primeira pessoa e guarde na variável `atendido`.
3. Adicione `"Davi"` no **início**.
4. Guarde em `restantes` quantas pessoas sobraram.

Imprima `atendido`, `restantes` e `fila`.
""",
 "starter": r"""const fila = ["Ana", "Bruno"];

// 1. adicione Carla no fim


// 2. remova a primeira pessoa -> atendido


// 3. adicione Davi no início


// 4. quantas sobraram


console.log(atendido, restantes, fila);
""",
 "solution": r"""const fila = ["Ana", "Bruno"];

fila.push("Carla");
const atendido = fila.shift();
fila.unshift("Davi");
const restantes = fila.length;

console.log(atendido, restantes, fila);
""",
 "hint": r"""`shift()` remove do início e devolve quem saiu — perfeito para "atender a próxima pessoa". Depois de tudo, a fila deve ser `["Davi", "Bruno", "Carla"]`.""",
 "tests": [
   {"msg": "atendido deve ser \"Ana\" (a primeira da fila)",
    "code": r"""atendido === "Ana" """},
   {"msg": "A fila final deve ser Davi, Bruno, Carla",
    "code": r"""JSON.stringify(fila) === JSON.stringify(["Davi","Bruno","Carla"])"""},
   {"msg": "restantes deve ser 3",
    "code": r"""restantes === 3"""},
   {"msg": "Use push, shift e unshift",
    "code": r"""/push/.test(__code) && /shift\(/.test(__code) && /unshift/.test(__code)"""},
 ],
},

{
 "id": "m4l3",
 "title": "Buscando dentro de arrays",
 "minutes": 8,
 "theory": r"""
## Onde está? Existe?

```js
const nums = [10, 20, 30, 40, 50];

nums.indexOf(30);     // 2    (posição)
nums.indexOf(99);     // -1   (não encontrado)
nums.includes(40);    // true
nums.includes(99);    // false
```

`indexOf` devolve a posição ou `-1`. `includes` devolve um booleano — muito mais legível quando você só quer saber se existe.

## Encontrando por uma condição

```js
const pessoas = [
  { nome: "Ana", idade: 25 },
  { nome: "Bruno", idade: 17 },
  { nome: "Carla", idade: 32 },
];

const primeiroAdulto = pessoas.find((p) => p.idade >= 18);
console.log(primeiroAdulto.nome);  // Ana

const posicao = pessoas.findIndex((p) => p.idade < 18);
console.log(posicao);              // 1
```

- `find` devolve o **primeiro item** que satisfaz a condição (ou `undefined`).
- `findIndex` devolve a **posição** desse item (ou `-1`).

## Fatiando sem estragar

```js
const fatia = nums.slice(1, 3);   // [20, 30]  (do índice 1 até o 3, sem incluir o 3)
const fim = nums.slice(-2);       // [40, 50]  (últimos dois)
nums.slice();                     // cópia completa
```

`slice` **não altera** o array original: devolve um pedaço novo.

> [warn] Não confunda `slice` (fatia, não muda nada) com `splice` (cirurgia, altera o array). Essa é uma das pegadinhas mais comuns.
""",
 "task": r"""
Você tem:

```js
const nums = [10, 20, 30, 40, 50];
```

Crie:

- `posicao` — o índice do valor 30 (use `indexOf`).
- `temQuarenta` — booleano: o array inclui 40?
- `primeiroMaiorQue25` — o primeiro número maior que 25 (use `find` com arrow function).
- `fatia` — um novo array com os itens dos índices 1 e 2 (use `slice`).

Imprima tudo.
""",
 "starter": r"""const nums = [10, 20, 30, 40, 50];

// posicao, temQuarenta, primeiroMaiorQue25, fatia


console.log(posicao, temQuarenta, primeiroMaiorQue25, fatia);
""",
 "solution": r"""const nums = [10, 20, 30, 40, 50];

const posicao = nums.indexOf(30);
const temQuarenta = nums.includes(40);
const primeiroMaiorQue25 = nums.find((n) => n > 25);
const fatia = nums.slice(1, 3);

console.log(posicao, temQuarenta, primeiroMaiorQue25, fatia);
""",
 "hint": r"""`slice(1, 3)` pega os índices 1 e 2 — o segundo número é **exclusivo**.""",
 "tests": [
   {"msg": "posicao deve ser 2",
    "code": r"""posicao === 2"""},
   {"msg": "temQuarenta deve ser true",
    "code": r"""temQuarenta === true"""},
   {"msg": "primeiroMaiorQue25 deve ser 30",
    "code": r"""primeiroMaiorQue25 === 30"""},
   {"msg": "fatia deve ser [20, 30] e não pode alterar nums",
    "code": r"""JSON.stringify(fatia) === JSON.stringify([20,30]) && nums.length === 5"""},
   {"msg": "Use find com uma arrow function",
    "code": r"""/\.find\s*\(/.test(__code) && /=>/.test(__code)"""},
 ],
},

{
 "id": "m4l4",
 "title": "Transformando: map e filter",
 "minutes": 9,
 "theory": r"""
## map: transforme cada item

`map` cria um **novo array** com o resultado da função aplicada a cada item:

```js
const precos = [10, 20, 30];

const comDesconto = precos.map((p) => p * 0.9);
console.log(comDesconto);  // [9, 18, 27]

console.log(precos);       // [10, 20, 30]  ← o original não muda
```

Mesma quantidade de itens, valores transformados.

## filter: escolha alguns itens

`filter` cria um **novo array** só com os itens que passam no teste (a função precisa devolver `true` ou `false`):

```js
const caros = precos.filter((p) => p > 15);
console.log(caros);  // [20, 30]
```

## Encadeando

O poder está em combinar: `map` devolve array, `filter` devolve array, então você pode emendar um no outro.

```js
const nomes = ["ana", "bruno", "carla"];
const resultado = nomes
  .filter((n) => n.length > 3)
  .map((n) => n.toUpperCase());
console.log(resultado);  // ["BRUNO", "CARLA"]
```

> [tip] A função recebida pelo `map`/`filter` pode ter um segundo parâmetro: o índice. `precos.map((p, i) => `${i}: ${p}`)`.
""",
 "task": r"""
Você tem:

```js
const precos = [10, 20, 30, 40];
```

Crie:

- `comDesconto` — cada preço com 10% de desconto (`p * 0.9`), usando `map`.
- `caros` — só os preços acima de 15, usando `filter`.
- `carosComDesconto` — os preços acima de 15, **já** com desconto (encadeie os dois).
- `emReais` — cada preço formatado como `"R$ 10"` (template string no `map`).

Imprima tudo.
""",
 "starter": r"""const precos = [10, 20, 30, 40];

// crie as quatro variáveis


console.log(comDesconto, caros, carosComDesconto, emReais);
""",
 "solution": r"""const precos = [10, 20, 30, 40];

const comDesconto = precos.map((p) => p * 0.9);
const caros = precos.filter((p) => p > 15);
const carosComDesconto = precos.filter((p) => p > 15).map((p) => p * 0.9);
const emReais = precos.map((p) => `R$ ${p}`);

console.log(comDesconto, caros, carosComDesconto, emReais);
""",
 "hint": r"""Para o encadeamento: `precos.filter((p) => p > 15).map((p) => p * 0.9)` — o `filter` vem primeiro porque devolve o array filtrado.""",
 "tests": [
   {"msg": "comDesconto deve ser [9, 18, 27, 36]",
    "code": r"""JSON.stringify(comDesconto) === JSON.stringify([9,18,27,36])"""},
   {"msg": "caros deve ser [20, 30, 40]",
    "code": r"""JSON.stringify(caros) === JSON.stringify([20,30,40])"""},
   {"msg": "carosComDesconto deve ser [18, 27, 36]",
    "code": r"""JSON.stringify(carosComDesconto) === JSON.stringify([18,27,36])"""},
   {"msg": "emReais deve ser [\"R$ 10\", \"R$ 20\", \"R$ 30\", \"R$ 40\"]",
    "code": r"""JSON.stringify(emReais) === JSON.stringify(["R$ 10","R$ 20","R$ 30","R$ 40"])"""},
   {"msg": "precos original deve continuar com 4 itens",
    "code": r"""precos.length === 4 && precos[0] === 10"""},
 ],
},

{
 "id": "m4l5",
 "title": "reduce e sort",
 "minutes": 9,
 "theory": r"""
## reduce: resumindo um array em um valor

`reduce` percorre o array acumulando um resultado. Ele recebe uma função com dois parâmetros: o **acumulador** e o item atual — e no final, o valor inicial do acumulador.

```js
const nums = [5, 1, 4, 2];

const soma = nums.reduce((total, n) => total + n, 0);
console.log(soma);  // 12
```

O `0` do final é o valor inicial. Sem ele, o primeiro item vira o acumulador.

`reduce` também monta objetos — é assim que se conta ocorrências:

```js
const frutas = ["uva", "maçã", "uva", "pera", "uva"];
const contagem = frutas.reduce((acc, f) => {
  acc[f] = (acc[f] || 0) + 1;
  return acc;
}, {});
console.log(contagem);  // { uva: 3, "maçã": 1, pera: 1 }
```

## sort

`sort` **altera** o array e, por padrão, ordena como texto (o que dá errado com números!):

```js
console.log([10, 9, 100].sort());  // [10, 100, 9]  ← ordem alfabética

console.log([10, 9, 100].sort((a, b) => a - b));  // [9, 10, 100] crescente
console.log([10, 9, 100].sort((a, b) => b - a));  // [100, 10, 9] decrescente
```

> [warn] Como `sort` altera o array original, use `[...nums].sort(...)` para ordenar uma cópia.
""",
 "task": r"""
Você tem `const nums = [5, 1, 4, 2];`.

Crie:

- `soma` — a soma de todos os números, com `reduce` e valor inicial 0.
- `crescente` — uma **cópia** ordenada do menor para o maior.
- `decrescente` — uma **cópia** ordenada do maior para o menor.
- `maior` — o maior número (dica: `reduce` comparando, ou `Math.max(...nums)`).

Depois de tudo, `nums` deve continuar na ordem original.
""",
 "starter": r"""const nums = [5, 1, 4, 2];

// soma, crescente, decrescente, maior


console.log(soma, crescente, decrescente, maior);
console.log("original:", nums);
""",
 "solution": r"""const nums = [5, 1, 4, 2];

const soma = nums.reduce((total, n) => total + n, 0);
const crescente = [...nums].sort((a, b) => a - b);
const decrescente = [...nums].sort((a, b) => b - a);
const maior = nums.reduce((max, n) => (n > max ? n : max), nums[0]);

console.log(soma, crescente, decrescente, maior);
console.log("original:", nums);
""",
 "hint": r"""`[...nums]` cria uma cópia rasa — assim o `sort` não bagunça o original. O comparador `(a, b) => a - b` ordena numericamente.""",
 "tests": [
   {"msg": "soma deve ser 12",
    "code": r"""soma === 12"""},
   {"msg": "crescente deve ser [1, 2, 4, 5]",
    "code": r"""JSON.stringify(crescente) === JSON.stringify([1,2,4,5])"""},
   {"msg": "decrescente deve ser [5, 4, 2, 1]",
    "code": r"""JSON.stringify(decrescente) === JSON.stringify([5,4,2,1])"""},
   {"msg": "maior deve ser 5",
    "code": r"""maior === 5"""},
   {"msg": "nums deve continuar na ordem original [5, 1, 4, 2]",
    "code": r"""JSON.stringify(nums) === JSON.stringify([5,1,4,2])"""},
   {"msg": "Use reduce",
    "code": r"""/\.reduce\s*\(/.test(__code)"""},
 ],
},

{
 "id": "m4l6",
 "title": "Desafio: análise de vendas",
 "minutes": 12,
 "theory": r"""
## Arrays + objetos = o dia a dia

A maior parte do trabalho real com dados é exatamente isto: uma lista de objetos, filtrada e resumida.

```js
const vendas = [
  { produto: "Caneta", valor: 10, pago: true },
  { produto: "Caderno", valor: 25, pago: false },
];

const totalPago = vendas
  .filter((v) => v.pago)
  .reduce((soma, v) => soma + v.valor, 0);
console.log(totalPago);  // 10
```

Observe o encadeamento: `filter` escolhe, `reduce` soma. Cada método devolve um array (ou um valor), então dá para ir emendando até chegar no que você precisa.

Leia essa linha em voz alta: "das vendas, pegue as pagas, e some os valores".
""",
 "task": r"""
Você recebeu:

```js
const vendas = [
  { produto: "Caneta", valor: 10, pago: true },
  { produto: "Caderno", valor: 25, pago: false },
  { produto: "Mochila", valor: 120, pago: true },
  { produto: "Lápis", valor: 3, pago: true },
];
```

Crie:

- `produtos` — array só com os nomes (`map`).
- `pagas` — array só com as vendas pagas (`filter`).
- `totalPago` — soma dos valores das vendas pagas (`filter` + `reduce`).
- `temPendente` — booleano: existe alguma venda não paga? (`some`)
- `maisCara` — a venda de maior valor (`reduce`).
""",
 "starter": r"""const vendas = [
  { produto: "Caneta", valor: 10, pago: true },
  { produto: "Caderno", valor: 25, pago: false },
  { produto: "Mochila", valor: 120, pago: true },
  { produto: "Lápis", valor: 3, pago: true },
];

// crie produtos, pagas, totalPago, temPendente e maisCara


console.log(produtos, totalPago, temPendente, maisCara);
""",
 "solution": r"""const vendas = [
  { produto: "Caneta", valor: 10, pago: true },
  { produto: "Caderno", valor: 25, pago: false },
  { produto: "Mochila", valor: 120, pago: true },
  { produto: "Lápis", valor: 3, pago: true },
];

const produtos = vendas.map((v) => v.produto);
const pagas = vendas.filter((v) => v.pago);
const totalPago = vendas.filter((v) => v.pago).reduce((soma, v) => soma + v.valor, 0);
const temPendente = vendas.some((v) => !v.pago);
const maisCara = vendas.reduce((maior, v) => (v.valor > maior.valor ? v : maior), vendas[0]);

console.log(produtos, totalPago, temPendente, maisCara);
""",
 "hint": r"""`some` devolve `true` se **pelo menos um** item passar no teste. Para `maisCara`, comece com `vendas[0]` como acumulador e troque quando achar um valor maior.""",
 "tests": [
   {"msg": "produtos deve ser [\"Caneta\", \"Caderno\", \"Mochila\", \"Lápis\"]",
    "code": r"""JSON.stringify(produtos) === JSON.stringify(["Caneta","Caderno","Mochila","Lápis"])"""},
   {"msg": "pagas deve ter 3 itens",
    "code": r"""Array.isArray(pagas) && pagas.length === 3"""},
   {"msg": "totalPago deve ser 133",
    "code": r"""totalPago === 133"""},
   {"msg": "temPendente deve ser true",
    "code": r"""temPendente === true"""},
   {"msg": "maisCara deve ser a Mochila",
    "code": r"""maisCara && maisCara.produto === "Mochila" """},
 ],
},

]},
# =====================================================================
{
 "id": "objetos",
 "title": "Objetos",
 "icon": "🗂️",
 "lessons": [

{
 "id": "m5l1",
 "title": "Criando e acessando objetos",
 "minutes": 8,
 "theory": r"""
## Dados com nome

Array é bom para listas. Para descrever **uma coisa com várias características**, usamos objetos: pares de chave e valor.

```js
const pessoa = {
  nome: "Ana",
  idade: 25,
  cidade: "Porto Alegre",
};

console.log(pessoa.nome);        // Ana         (notação de ponto)
console.log(pessoa["idade"]);    // 25          (notação de colchetes)
console.log(pessoa.profissao);   // undefined   (não existe)
```

## Quando usar colchetes

A notação de colchetes serve quando a chave está em uma variável, ou quando o nome tem caracteres especiais:

```js
const chave = "cidade";
console.log(pessoa[chave]);        // Porto Alegre

const dados = { "nome-completo": "Ana Silva" };
console.log(dados["nome-completo"]);  // Ana Silva
```

## Objetos aninhados

```js
const usuario = {
  nome: "Bruno",
  endereco: { rua: "Xavier", numero: 100 },
  interesses: ["música", "corrida"],
};

console.log(usuario.endereco.rua);     // Xavier
console.log(usuario.interesses[0]);    // música
```

> [tip] Objetos são a estrutura mais usada em JavaScript — praticamente toda API devolve objetos (JSON).
""",
 "task": r"""
Crie um objeto `livro` com estas propriedades:

- `titulo`: `"Dom Casmurro"`
- `autor`: `"Machado de Assis"`
- `ano`: `1899` (número)
- `generos`: um array com `"romance"` e `"clássico"`

Depois crie:

- `tituloLivro` — o título usando notação de ponto.
- `primeiroGenero` — o primeiro gênero do array.
""",
 "starter": r"""// 1. crie o objeto livro


// 2. tituloLivro e primeiroGenero


console.log(tituloLivro, primeiroGenero);
""",
 "solution": r"""const livro = {
  titulo: "Dom Casmurro",
  autor: "Machado de Assis",
  ano: 1899,
  generos: ["romance", "clássico"],
};

const tituloLivro = livro.titulo;
const primeiroGenero = livro.generos[0];

console.log(tituloLivro, primeiroGenero);
""",
 "hint": r"""Dentro do objeto, separe as propriedades por vírgula: `{ titulo: "Dom Casmurro", ano: 1899 }`.""",
 "tests": [
   {"msg": "livro deve ser um objeto com título, autor, ano e gêneros",
    "code": r"""typeof livro === "object" && livro !== null && livro.titulo === "Dom Casmurro" && livro.autor === "Machado de Assis" && livro.ano === 1899"""},
   {"msg": "generos deve ser um array com 2 itens",
    "code": r"""Array.isArray(livro.generos) && livro.generos.length === 2 && livro.generos[0] === "romance" """},
   {"msg": "tituloLivro deve ser acessado com notação de ponto",
    "code": r"""tituloLivro === livro.titulo && /livro\.titulo/.test(__code)"""},
   {"msg": "primeiroGenero deve ser \"romance\"",
    "code": r"""primeiroGenero === "romance" """},
 ],
},

{
 "id": "m5l2",
 "title": "Alterando, adicionando e removendo",
 "minutes": 7,
 "theory": r"""
## Objetos são mutáveis

```js
const pessoa = { nome: "Ana", idade: 25 };

pessoa.idade = 26;              // alterar
pessoa.cidade = "Porto Alegre"; // adicionar
delete pessoa.idade;            // remover
```

Também é possível usar colchetes e variáveis:

```js
const campo = "email";
pessoa[campo] = "ana@exemplo.com";
```

## Verificando se existe

```js
console.log("nome" in pessoa);                       // true
console.log(pessoa.telefone !== undefined);          // false
console.log(Object.hasOwn(pessoa, "nome"));          // true
```

## Cópia: cuidado com referência

Isto é uma armadilha importante:

```js
const a = { x: 1 };
const b = a;      // NÃO é uma cópia: b aponta para o mesmo objeto
b.x = 99;
console.log(a.x); // 99
```

Para copiar de verdade, use o spread:

```js
const copia = { ...a };      // cópia rasa
const copia2 = { ...a, x: 5 }; // cópia com alteração
```

> [warn] `delete` remove a propriedade, mas é lento e raramente a melhor opção. Muitas vezes vale mais criar um objeto novo sem a chave: `const { idade, ...resto } = pessoa;`
""",
 "task": r"""
Você tem:

```js
const pessoa = { nome: "Ana", idade: 25 };
```

Faça:

1. Altere `idade` para `26`.
2. Adicione a propriedade `cidade` com `"Porto Alegre"`.
3. Remova a propriedade `nome` (use `delete`).
4. Crie `copia` — um objeto novo com as mesmas propriedades de `pessoa`, mas com `ativo: true` (use spread).

Imprima `pessoa` e `copia`.
""",
 "starter": r"""const pessoa = { nome: "Ana", idade: 25 };

// 1, 2, 3 - altere o objeto pessoa


// 4 - copie com spread e adicione ativo: true


console.log(pessoa);
console.log(copia);
""",
 "solution": r"""const pessoa = { nome: "Ana", idade: 25 };

pessoa.idade = 26;
pessoa.cidade = "Porto Alegre";
delete pessoa.nome;

const copia = { ...pessoa, ativo: true };

console.log(pessoa);
console.log(copia);
""",
 "hint": r"""`{ ...pessoa, ativo: true }` copia todas as propriedades e ainda adiciona `ativo`. O objeto original não é alterado.""",
 "tests": [
   {"msg": "idade deve ser 26",
    "code": r"""pessoa.idade === 26"""},
   {"msg": "Adicione a propriedade cidade",
    "code": r"""pessoa.cidade === "Porto Alegre" """},
   {"msg": "A propriedade nome deve ter sido removida",
    "code": r"""!("nome" in pessoa) && /delete/.test(__code)"""},
   {"msg": "copia deve ter as propriedades e ativo: true",
    "code": r"""copia && copia.idade === 26 && copia.ativo === true && !("nome" in copia)"""},
   {"msg": "copia deve ser um objeto diferente de pessoa",
    "code": r"""copia !== pessoa"""},
 ],
},

{
 "id": "m5l3",
 "title": "Métodos e this",
 "minutes": 8,
 "theory": r"""
## Funções dentro de objetos

Quando uma função é uma propriedade de um objeto, ela é chamada de **método**:

```js
const pessoa = {
  nome: "Ana",
  idade: 25,
  apresentar: function () {
    return `Olá, eu sou ${this.nome}`;
  },
};

console.log(pessoa.apresentar());  // Olá, eu sou Ana
```

## O que é this

`this` é uma referência ao objeto que está **executando** a chamada. Em `pessoa.apresentar()`, `this` é `pessoa`. Isso permite escrever um método e reutilizar em vários objetos:

```js
const conta = {
  titular: "Bruno",
  saldo: 100,
  depositar(valor) {
    this.saldo += valor;
    return this.saldo;
  },
};

conta.depositar(50);   // 150
```

## Sintaxe curta

No ES6 você pode escrever `depositar(valor) { ... }` em vez de `depositar: function (valor) { ... }`.

> [warn] Arrow functions **não** têm `this` próprio — elas usam o `this` de fora. Métodos que dependem de `this` devem usar função tradicional (ou a sintaxe curta).
""",
 "task": r"""
Crie o objeto `carrinho` com:

- `itens`: um array vazio `[]`.
- `adicionar(nome, preco)` — adiciona `{ nome, preco }` ao array e retorna `this.itens.length`.
- `total()` — retorna a soma dos preços dos itens (use `reduce`).

Depois:
1. `carrinho.adicionar("Caneta", 10)`
2. `carrinho.adicionar("Caderno", 25)`
3. Guarde `carrinho.total()` em `totalCarrinho`.
""",
 "starter": r"""const carrinho = {
  itens: [],

  adicionar(nome, preco) {
    // seu código
  },

  total() {
    // seu código
  },
};

carrinho.adicionar("Caneta", 10);
carrinho.adicionar("Caderno", 25);
const totalCarrinho = carrinho.total();

console.log(carrinho.itens, totalCarrinho);
""",
 "solution": r"""const carrinho = {
  itens: [],

  adicionar(nome, preco) {
    this.itens.push({ nome, preco });
    return this.itens.length;
  },

  total() {
    return this.itens.reduce((soma, item) => soma + item.preco, 0);
  },
};

carrinho.adicionar("Caneta", 10);
carrinho.adicionar("Caderno", 25);
const totalCarrinho = carrinho.total();

console.log(carrinho.itens, totalCarrinho);
""",
 "hint": r"""Dentro do método use `this.itens` (e não `carrinho.itens`): assim ele continua funcionando se o objeto for copiado.""",
 "tests": [
   {"msg": "carrinho.itens deve ter 2 itens",
    "code": r"""carrinho.itens.length === 2"""},
   {"msg": "Cada item deve ter nome e preço",
    "code": r"""carrinho.itens[0].nome === "Caneta" && carrinho.itens[0].preco === 10"""},
   {"msg": "total() deve retornar 35",
    "code": r"""carrinho.total() === 35"""},
   {"msg": "totalCarrinho deve ser 35",
    "code": r"""totalCarrinho === 35"""},
   {"msg": "Use this dentro dos métodos",
    "code": r"""/this\./.test(__code)"""},
   {"msg": "adicionar() deve devolver a quantidade de itens",
    "code": r"""(function(){ const c = { itens: [], adicionar: carrinho.adicionar, total: carrinho.total }; return c.adicionar("X", 1) === 1; })()"""},
 ],
},

{
 "id": "m5l4",
 "title": "Destructuring e spread",
 "minutes": 9,
 "theory": r"""
## Tirando valores: destructuring

Em vez de acessar propriedade por propriedade, você pode "desmontar" o objeto de uma vez:

```js
const pessoa = { nome: "Ana", idade: 25, cidade: "Porto Alegre" };

const { nome, idade } = pessoa;
console.log(nome, idade);  // Ana 25
```

Também funciona com arrays, pela posição:

```js
const [primeiro, segundo] = ["azul", "verde"];
console.log(primeiro);   // azul
```

## Renomeando e definindo padrão

```js
const { nome: nomeCompleto, telefone = "não informado" } = pessoa;
console.log(nomeCompleto);  // Ana
console.log(telefone);      // não informado
```

## Destructuring em parâmetros

Isto é o que mais se vê em código real:

```js
function mostrar({ nome, idade }) {
  return `${nome}, ${idade} anos`;
}

mostrar({ nome: "Ana", idade: 25 });
```

## Spread: espalhando

```js
const base = { tema: "escuro", fonte: "14px" };
const novo = { ...base, fonte: "16px" };

const a = [1, 2];
const b = [3, 4];
const junto = [...a, ...b];  // [1, 2, 3, 4]
```
""",
 "task": r"""
Você tem:

```js
const produto = { nome: "Teclado", preco: 150, estoque: 8 };
```

1. Faça destructuring para criar `nome` e `preco` de uma vez.
2. Crie `estoque`, mas com nome trocado para `quantidade` (renomeie no destructuring).
3. Crie `garantia` com valor padrão `"12 meses"` (a propriedade não existe no objeto).
4. Crie `produtoAtualizado` — uma cópia com `preco: 120` (use spread).
5. Crie `combo` — array com `...produto`? Não: crie `etiquetas` = `["novo", ...["promoção", "limitado"]]`.
""",
 "starter": r"""const produto = { nome: "Teclado", preco: 150, estoque: 8 };

// 1. nome e preco
// 2. quantidade (renomeando estoque)
// 3. garantia (valor padrão)
// 4. produtoAtualizado com spread
// 5. etiquetas


console.log(nome, preco, quantidade, garantia, produtoAtualizado, etiquetas);
""",
 "solution": r"""const produto = { nome: "Teclado", preco: 150, estoque: 8 };

const { nome, preco } = produto;
const { estoque: quantidade } = produto;
const { garantia = "12 meses" } = produto;
const produtoAtualizado = { ...produto, preco: 120 };
const etiquetas = ["novo", ...["promoção", "limitado"]];

console.log(nome, preco, quantidade, garantia, produtoAtualizado, etiquetas);
""",
 "hint": r"""Renomear: `const { estoque: quantidade } = produto;`. Valor padrão: `const { garantia = "12 meses" } = produto;`.""",
 "tests": [
   {"msg": "nome e preco devem vir do produto",
    "code": r"""nome === "Teclado" && preco === 150"""},
   {"msg": "quantidade deve valer o estoque (8)",
    "code": r"""quantidade === 8 && /estoque\s*:\s*quantidade/.test(__code)"""},
   {"msg": "garantia deve ter o valor padrão \"12 meses\"",
    "code": r"""garantia === "12 meses" """},
   {"msg": "produtoAtualizado deve ter preco 120 e manter as outras propriedades",
    "code": r"""produtoAtualizado.preco === 120 && produtoAtualizado.nome === "Teclado" && produtoAtualizado.estoque === 8"""},
   {"msg": "produto original não pode ser alterado",
    "code": r"""produto.preco === 150"""},
   {"msg": "etiquetas deve ser [\"novo\", \"promoção\", \"limitado\"]",
    "code": r"""JSON.stringify(etiquetas) === JSON.stringify(["novo","promoção","limitado"])"""},
 ],
},

{
 "id": "m5l5",
 "title": "Object.keys, values e entries",
 "minutes": 8,
 "theory": r"""
## Percorrendo um objeto

Objetos não têm `forEach` nem `map`. Para percorrê-los, transformamos em array:

```js
const pessoa = { nome: "Ana", idade: 25, cidade: "POA" };

Object.keys(pessoa);    // ["nome", "idade", "cidade"]
Object.values(pessoa);  // ["Ana", 25, "POA"]
Object.entries(pessoa); // [["nome","Ana"], ["idade",25], ["cidade","POA"]]
```

Com `for...of` nas entries:

```js
for (const [chave, valor] of Object.entries(pessoa)) {
  console.log(`${chave}: ${valor}`);
}
```

## Casos práticos

```js
// quantas propriedades?
Object.keys(pessoa).length;   // 3

// transformar valores
const dobrados = Object.fromEntries(
  Object.entries({ a: 1, b: 2 }).map(([k, v]) => [k, v * 2])
);
// { a: 2, b: 4 }

// somar todos os valores
Object.values({ a: 1, b: 2, c: 3 }).reduce((s, n) => s + n, 0);  // 6
```

> [tip] `Object.entries` + `map` + `Object.fromEntries` é o trio para transformar objetos sem `for`.
""",
 "task": r"""
Você tem:

```js
const notas = { ana: 9, bruno: 6.5, carla: 8 };
```

Crie:

- `alunos` — array com os nomes (`Object.keys`).
- `valores` — array com as notas (`Object.values`).
- `quantidadeAlunos` — quantos alunos existem.
- `media` — a média das notas (use `reduce` nos valores).
- `pares` — `Object.entries(notas)` (array de pares chave/valor).
""",
 "starter": r"""const notas = { ana: 9, bruno: 6.5, carla: 8 };

// crie as variáveis


console.log(alunos, valores, quantidadeAlunos, media, pares);
""",
 "solution": r"""const notas = { ana: 9, bruno: 6.5, carla: 8 };

const alunos = Object.keys(notas);
const valores = Object.values(notas);
const quantidadeAlunos = alunos.length;
const media = valores.reduce((soma, n) => soma + n, 0) / valores.length;
const pares = Object.entries(notas);

console.log(alunos, valores, quantidadeAlunos, media, pares);
""",
 "hint": r"""`Object.values(notas)` devolve `[9, 6.5, 8]`; a média é a soma dividida por `valores.length`.""",
 "tests": [
   {"msg": "alunos deve ser [\"ana\", \"bruno\", \"carla\"]",
    "code": r"""JSON.stringify(alunos) === JSON.stringify(["ana","bruno","carla"])"""},
   {"msg": "valores deve ser [9, 6.5, 8]",
    "code": r"""JSON.stringify(valores) === JSON.stringify([9,6.5,8])"""},
   {"msg": "quantidadeAlunos deve ser 3",
    "code": r"""quantidadeAlunos === 3"""},
   {"msg": "media deve ser aproximadamente 7.83",
    "code": r"""Math.abs(media - 23.5/3) < 1e-9"""},
   {"msg": "pares deve ser o resultado de Object.entries",
    "code": r"""Array.isArray(pares) && pares.length === 3 && pares[0][0] === "ana" && pares[0][1] === 9"""},
 ],
},

{
 "id": "m5l6",
 "title": "Desafio: agenda de contatos",
 "minutes": 12,
 "theory": r"""
## Modelando dados reais

Uma agenda é um array de objetos. As operações clássicas são: adicionar, buscar, atualizar e remover.

```js
const contatos = [
  { nome: "Ana", telefone: "99999-1111" },
  { nome: "Bruno", telefone: "99999-2222" },
];

// buscar
const ana = contatos.find((c) => c.nome === "Ana");

// atualizar (sem mutar o array, criando um novo)
const atualizados = contatos.map((c) =>
  c.nome === "Ana" ? { ...c, telefone: "98888-0000" } : c
);

// remover
const semAna = contatos.filter((c) => c.nome !== "Ana");
```

Repare no padrão com `map` + spread: devolvemos um array novo, alterando só o item desejado. Isso é o coração da programação funcional — previsível, sem efeitos colaterais escondidos.
""",
 "task": r"""
Você tem:

```js
const contatos = [
  { nome: "Ana", telefone: "99999-1111" },
  { nome: "Bruno", telefone: "99999-2222" },
];
```

Crie:

1. `novoContato` — a lista com um contato a mais: `{ nome: "Carla", telefone: "99999-3333" }` (use spread).
2. `busca` — o contato chamado `"Bruno"` (use `find`).
3. `atualizados` — lista com o telefone da Ana trocado para `"98888-0000"` (use `map` + spread).
4. `semBruno` — lista sem o Bruno (use `filter`).
5. `nomes` — array com todos os nomes (use `map`).

O array `contatos` original deve continuar intacto.
""",
 "starter": r"""const contatos = [
  { nome: "Ana", telefone: "99999-1111" },
  { nome: "Bruno", telefone: "99999-2222" },
];

// crie as cinco variáveis


console.log(novoContato.length, busca, atualizados, semBruno, nomes);
""",
 "solution": r"""const contatos = [
  { nome: "Ana", telefone: "99999-1111" },
  { nome: "Bruno", telefone: "99999-2222" },
];

const novoContato = [...contatos, { nome: "Carla", telefone: "99999-3333" }];
const busca = contatos.find((c) => c.nome === "Bruno");
const atualizados = contatos.map((c) =>
  c.nome === "Ana" ? { ...c, telefone: "98888-0000" } : c
);
const semBruno = contatos.filter((c) => c.nome !== "Bruno");
const nomes = contatos.map((c) => c.nome);

console.log(novoContato.length, busca, atualizados, semBruno, nomes);
""",
 "hint": r"""No `map` com ternário: se for a Ana, devolva `{ ...c, telefone: "98888-0000" }`; senão devolva o próprio `c`.""",
 "tests": [
   {"msg": "novoContato deve ter 3 contatos",
    "code": r"""novoContato.length === 3 && novoContato[2].nome === "Carla" """},
   {"msg": "busca deve ser o Bruno",
    "code": r"""busca && busca.nome === "Bruno" && busca.telefone === "99999-2222" """},
   {"msg": "atualizados deve ter o telefone da Ana alterado",
    "code": r"""atualizados[0].nome === "Ana" && atualizados[0].telefone === "98888-0000" && atualizados[1].telefone === "99999-2222" """},
   {"msg": "semBruno deve ter apenas a Ana",
    "code": r"""semBruno.length === 1 && semBruno[0].nome === "Ana" """},
   {"msg": "nomes deve ser [\"Ana\", \"Bruno\"]",
    "code": r"""JSON.stringify(nomes) === JSON.stringify(["Ana","Bruno"])"""},
   {"msg": "O array contatos original deve continuar intacto",
    "code": r"""contatos.length === 2 && contatos[0].nome === "Ana" && contatos[0].telefone === "99999-1111" """},
 ],
},

]},
# =====================================================================
{
 "id": "strings",
 "title": "Strings",
 "icon": "🔤",
 "lessons": [

{
 "id": "m6l1",
 "title": "Tamanho, acesso e maiúsculas",
 "minutes": 7,
 "theory": r"""
## Textos são sequências

Uma string é uma sequência de caracteres, e cada caractere tem um índice — igual a um array:

```js
const nome = "JavaScript";

console.log(nome.length);     // 10
console.log(nome[0]);         // J
console.log(nome[4]);         // S
console.log(nome.at(-1));     // t  (último, forma moderna)
```

## Mudando a caixa

```js
const texto = "Olá Mundo";

texto.toUpperCase();   // "OLÁ MUNDO"
texto.toLowerCase();   // "olá mundo"
```

Strings são **imutáveis**: nenhum método muda o texto original — eles devolvem um novo texto. Você precisa guardar o resultado:

```js
let nome = "ana";
nome = nome.toUpperCase();   // agora sim: "ANA"
```

## Outros úteis

```js
"  oi  ".trim();          // "oi"     (remove espaços das pontas)
"oi".charAt(0);           // "o"
"a,b".length;             // 3       (a vírgula conta!)
```

> [warn] Comparações de string diferenciam maiúsculas: `"Ana" === "ana"` é `false`. Normalize com `toLowerCase()` antes de comparar.
""",
 "task": r"""
Você tem `const frase = "  Aprender JavaScript é divertido  ";`.

Crie:

- `semEspacos` — a frase sem os espaços das pontas (`trim`).
- `maiuscula` — a frase sem espaços, em MAIÚSCULAS.
- `minuscula` — a frase sem espaços, em minúsculas.
- `tamanho` — quantos caracteres tem `semEspacos`.
- `primeiraLetra` — o primeiro caractere de `semEspacos`.
""",
 "starter": r"""const frase = "  Aprender JavaScript é divertido  ";

// crie as variáveis


console.log(semEspacos, maiuscula, minuscula, tamanho, primeiraLetra);
""",
 "solution": r"""const frase = "  Aprender JavaScript é divertido  ";

const semEspacos = frase.trim();
const maiuscula = semEspacos.toUpperCase();
const minuscula = semEspacos.toLowerCase();
const tamanho = semEspacos.length;
const primeiraLetra = semEspacos[0];

console.log(semEspacos, maiuscula, minuscula, tamanho, primeiraLetra);
""",
 "hint": r"""Você pode encadear: `frase.trim().toUpperCase()`. O `.length` de `semEspacos` é 30.""",
 "tests": [
   {"msg": "semEspacos deve começar com A e terminar com o",
    "code": r"""semEspacos === "Aprender JavaScript é divertido" """},
   {"msg": "maiuscula deve estar em maiúsculas",
    "code": r"""maiuscula === semEspacos.toUpperCase() && maiuscula.includes("JAVASCRIPT")"""},
   {"msg": "minuscula deve estar em minúsculas",
    "code": r"""minuscula === semEspacos.toLowerCase()"""},
   {"msg": "tamanho deve ser semEspacos.length",
    "code": r"""tamanho === semEspacos.length && tamanho > 20"""},
   {"msg": "primeiraLetra deve ser \"A\"",
    "code": r"""primeiraLetra === "A" """},
 ],
},

{
 "id": "m6l2",
 "title": "Buscando dentro de textos",
 "minutes": 7,
 "theory": r"""
## A substring existe?

```js
const frase = "Eu amo programar em JavaScript";

frase.includes("JavaScript");   // true
frase.includes("python");       // false
frase.indexOf("amo");           // 3   (posição)
frase.indexOf("python");        // -1  (não achou)
```

## Começo e fim

```js
frase.startsWith("Eu");    // true
frase.endsWith("Script");  // true
```

Esses três métodos aceitam um segundo parâmetro com a posição inicial:

```js
"abcabc".indexOf("b", 2);  // 4
```

## Diferença entre maiúsculas

Nenhum desses métodos ignora maiúsculas/minúsculas. Para busca sem diferenciar caixa, normalize os dois lados:

```js
const termo = "javascript";
frase.toLowerCase().includes(termo.toLowerCase());
```

> [tip] Para procurar com padrões (CPF, e-mail, datas), use **expressões regulares** com `match`/`test` — fica para o módulo avançado.
""",
 "task": r"""
Você tem:

```js
const email = "ana.silva@exemplo.com.br";
```

Crie:

- `temArroba` — booleano com `includes`.
- `posicaoArroba` — a posição do `@` com `indexOf`.
- `dominio` — o texto que vem **depois** do `@` (dica: `slice(posicaoArroba + 1)`).
- `terminaComBr` — booleano com `endsWith`.
- `emailValido` — `true` se tem `@` **e** termina com `.br` (use `&&`).
""",
 "starter": r"""const email = "ana.silva@exemplo.com.br";

// crie as variáveis


console.log(temArroba, posicaoArroba, dominio, terminaComBr, emailValido);
""",
 "solution": r"""const email = "ana.silva@exemplo.com.br";

const temArroba = email.includes("@");
const posicaoArroba = email.indexOf("@");
const dominio = email.slice(posicaoArroba + 1);
const terminaComBr = email.endsWith(".br");
const emailValido = temArroba && terminaComBr;

console.log(temArroba, posicaoArroba, dominio, terminaComBr, emailValido);
""",
 "hint": r"""`slice(posicaoArroba + 1)` pega do caractere seguinte ao `@` até o fim da string.""",
 "tests": [
   {"msg": "temArroba deve ser true",
    "code": r"""temArroba === true"""},
   {"msg": "posicaoArroba deve ser 9",
    "code": r"""posicaoArroba === 9"""},
   {"msg": "dominio deve ser \"exemplo.com.br\"",
    "code": r"""dominio === "exemplo.com.br" """},
   {"msg": "terminaComBr deve ser true",
    "code": r"""terminaComBr === true"""},
   {"msg": "emailValido deve ser true",
    "code": r"""emailValido === true"""},
 ],
},

{
 "id": "m6l3",
 "title": "Separando e juntando",
 "minutes": 8,
 "theory": r"""
## split: texto → array

```js
const csv = "maçã,banana,uva";
console.log(csv.split(","));      // ["maçã", "banana", "uva"]

console.log("a b  c".split(" ")); // ["a", "b", "", "c"]  (espaço duplo gera vazio)
console.log("abc".split(""));     // ["a", "b", "c"]
console.log("a,b,c".split(",", 2)); // ["a", "b"] (limite de itens)
```

## join: array → texto

```js
console.log(["maçã", "banana"].join(" e "));  // maçã e banana
console.log([1, 2, 3].join("-"));             // 1-2-3
console.log([1, 2, 3].join(""));              // 123
```

## O par clássico

```js
const palavras = "javascript é divertido".split(" ");
const capitalizado = palavras.map((p) => p[0].toUpperCase() + p.slice(1)).join(" ");
console.log(capitalizado);  // Javascript É Divertido
```

## Outras fatias

```js
const data = "2026-11-12";
data.slice(0, 4);    // "2026"
data.slice(5);       // "11-12"
data.slice(-2);      // "12"
data.substring(0, 4); // parecido com slice, mas sem índices negativos
```
""",
 "task": r"""
Você tem `const nomes = "ana,bruno,carla";`.

Crie:

- `lista` — o texto separado em array pela vírgula (`split`).
- `quantidade` — quantos nomes existem.
- `capitalizados` — array com cada nome com a primeira letra maiúscula (use `map`).
- `frase` — os nomes capitalizados unidos por `", "` (`join`).
- `sigla` — a primeira letra de cada nome em maiúsculas, unidas sem separador → `"ABC"` (use `map` + `join("")`).
""",
 "starter": r"""const nomes = "ana,bruno,carla";

// crie as variáveis


console.log(lista, quantidade, capitalizados, frase, sigla);
""",
 "solution": r"""const nomes = "ana,bruno,carla";

const lista = nomes.split(",");
const quantidade = lista.length;
const capitalizados = lista.map((n) => n[0].toUpperCase() + n.slice(1));
const frase = capitalizados.join(", ");
const sigla = lista.map((n) => n[0].toUpperCase()).join("");

console.log(lista, quantidade, capitalizados, frase, sigla);
""",
 "hint": r"""Para capitalizar: `n[0].toUpperCase() + n.slice(1)` — a primeira letra em maiúscula concatenada com o resto da string.""",
 "tests": [
   {"msg": "lista deve ser [\"ana\", \"bruno\", \"carla\"]",
    "code": r"""JSON.stringify(lista) === JSON.stringify(["ana","bruno","carla"])"""},
   {"msg": "quantidade deve ser 3",
    "code": r"""quantidade === 3"""},
   {"msg": "capitalizados deve ser [\"Ana\", \"Bruno\", \"Carla\"]",
    "code": r"""JSON.stringify(capitalizados) === JSON.stringify(["Ana","Bruno","Carla"])"""},
   {"msg": "frase deve ser \"Ana, Bruno, Carla\"",
    "code": r"""frase === "Ana, Bruno, Carla" """},
   {"msg": "sigla deve ser \"ABC\"",
    "code": r"""sigla === "ABC" """},
 ],
},

{
 "id": "m6l4",
 "title": "Substituindo trechos",
 "minutes": 7,
 "theory": r"""
## replace

```js
const texto = "Eu amo Java. Java é legal.";

texto.replace("Java", "JavaScript");   // troca só a PRIMEIRA ocorrência
texto.replaceAll("Java", "JavaScript"); // troca todas
```

Com expressão regular e a flag `g` você também troca todas:

```js
"a-b-c".replace(/-/g, " ");   // "a b c"
```

## Substituindo com função

`replace` aceita uma função para decidir a troca:

```js
"preço: 10".replace(/\d+/, (n) => n * 2);   // "preço: 20"
```

## Censurando e limpando

```js
const cpf = "123.456.789-00";
cpf.replaceAll(".", "").replace("-", "");   // "12345678900"
cpf.replace(/[.-]/g, "");                   // mesma coisa, com regex
```

> [warn] `replace` e `replaceAll` devolvem **nova** string — não alteram a original. Guarde o resultado.
""",
 "task": r"""
Você tem `const frase = "O rato roeu a roupa do rei de Roma";`.

Crie:

1. `primeiraTroca` — troque só o primeiro `"r"` maiúsculo... ou seja, use `replace("rato", "gato")`.
2. `semEspacos` — a frase com todos os espaços trocados por `_` (use `replaceAll`).
3. `trocado` — a frase com todas as letras `"r"` trocadas por `"l"` (use `replaceAll`).
4. `cpfLimpo` — a partir de `const cpf = "123.456.789-00"`, remova pontos e traço.
""",
 "starter": r"""const frase = "O rato roeu a roupa do rei de Roma";
const cpf = "123.456.789-00";

// crie as variáveis


console.log(primeiraTroca, semEspacos, trocado, cpfLimpo);
""",
 "solution": r"""const frase = "O rato roeu a roupa do rei de Roma";
const cpf = "123.456.789-00";

const primeiraTroca = frase.replace("rato", "gato");
const semEspacos = frase.replaceAll(" ", "_");
const trocado = frase.replaceAll("r", "l");
const cpfLimpo = cpf.replaceAll(".", "").replace("-", "");

console.log(primeiraTroca, semEspacos, trocado, cpfLimpo);
""",
 "hint": r"""`replaceAll(".", "")` troca **todas** as ocorrências. Encadear `.replace("-", "")` remove o traço que sobrou.""",
 "tests": [
   {"msg": "primeiraTroca deve conter \"gato\"",
    "code": r"""primeiraTroca === "O gato roeu a roupa do rei de Roma" """},
   {"msg": "semEspacos deve usar _ no lugar dos espaços",
    "code": r"""semEspacos === "O_rato_roeu_a_roupa_do_rei_de_Roma" """},
   {"msg": "trocado deve ter todos os r virados l",
    "code": r"""trocado === "O lato loeu a loupa do lei de Roma" """},
   {"msg": "cpfLimpo deve ser \"12345678900\"",
    "code": r"""cpfLimpo === "12345678900" """},
 ],
},

{
 "id": "m6l5",
 "title": "Formatando textos",
 "minutes": 7,
 "theory": r"""
## Repetir e preencher

```js
"ab".repeat(3);          // "ababab"
"7".padStart(3, "0");    // "007"   (preenche no início)
"7".padEnd(3, ".");      // "7.."   (preenche no fim)
```

`padStart` é perfeito para números com largura fixa: códigos, horas, placas.

## Números e textos

```js
const preco = 1234.5;
preco.toFixed(2);                    // "1234.50"  (string!)
`R$ ${preco.toFixed(2).replace(".", ",")}`;  // "R$ 1234,50"

(1234.5).toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
// "R$ 1.234,50"
```

## Template strings de novo

```js
const nome = "ana";
const inicial = nome[0].toUpperCase() + nome.slice(1);
console.log(`${inicial} tem ${nome.length} letras`);
```

## Limpando entradas

```js
const entrada = "  42  ";
Number(entrada.trim());      // 42
parseInt("42px", 10);        // 42
```
""",
 "task": r"""
Você tem:

```js
const numero = 7;
const preco = 1234.5;
const nome = "ana";
```

Crie:

- `codigo` — `numero` com 3 dígitos, preenchido com zeros: `"007"` (use `padStart`).
- `linha` — 10 asteriscos seguidos (use `repeat`).
- `precoFormatado` — `"R$ 1234,50"` (use `toFixed(2)` e troque o ponto por vírgula).
- `nomeCapitalizado` — `"Ana"`.
""",
 "starter": r"""const numero = 7;
const preco = 1234.5;
const nome = "ana";

// crie as variáveis


console.log(codigo, linha, precoFormatado, nomeCapitalizado);
""",
 "solution": r"""const numero = 7;
const preco = 1234.5;
const nome = "ana";

const codigo = String(numero).padStart(3, "0");
const linha = "*".repeat(10);
const precoFormatado = `R$ ${preco.toFixed(2).replace(".", ",")}`;
const nomeCapitalizado = nome[0].toUpperCase() + nome.slice(1);

console.log(codigo, linha, precoFormatado, nomeCapitalizado);
""",
 "hint": r"""`padStart` só funciona em strings: converta antes com `String(numero)`. E `toFixed(2)` devolve `"1234.50"` — troque o `.` por `,` depois.""",
 "tests": [
   {"msg": "codigo deve ser \"007\"",
    "code": r"""codigo === "007" """},
   {"msg": "linha deve ter 10 asteriscos",
    "code": r"""linha === "*".repeat(10)"""},
   {"msg": "precoFormatado deve ser \"R$ 1234,50\"",
    "code": r"""precoFormatado === "R$ 1234,50" """},
   {"msg": "nomeCapitalizado deve ser \"Ana\"",
    "code": r"""nomeCapitalizado === "Ana" """},
   {"msg": "Use padStart e repeat",
    "code": r"""/padStart/.test(__code) && /repeat/.test(__code)"""},
 ],
},

{
 "id": "m6l6",
 "title": "Desafio: analisador de texto",
 "minutes": 12,
 "theory": r"""
## Contando caracteres

```js
const vogais = "aeiou";
const texto = "programar";
let total = 0;

for (const letra of texto) {
  if (vogais.includes(letra)) {
    total++;
  }
}
console.log(total);   // 3
```

Outra abordagem, mais "funcional":

```js
[...texto].filter((l) => vogais.includes(l)).length;
```

## Invertendo

```js
const invertida = texto.split("").reverse().join("");
```

## Palíndromo

Um palíndromo se lê igual nos dois sentidos ("arara", "ovo", "A base do teto desaba"). Teste:

```js
function ehPalindromo(t) {
  const limpo = t.toLowerCase().replaceAll(" ", "");
  return limpo === limpo.split("").reverse().join("");
}
```

Repare no padrão: normalizar, transformar em array, inverter, juntar de volta, comparar.
""",
 "task": r"""
Você tem `const texto = "JavaScript é uma linguagem fantástica";`.

Crie:

1. `quantidadeVogais` — quantas vogais (a, e, i, o, u) existem no texto, ignorando maiúsculas.
2. `palavras` — array com as palavras (`split(" ")`).
3. `quantidadePalavras` — quantas palavras.
4. `invertido` — o texto com as letras na ordem inversa.
5. `ehPalindromo` — `true` se `"arara"` invertida for igual a ela mesma (use uma variável `const palavra = "arara";`, inverta e compare).
""",
 "starter": r"""const texto = "JavaScript é uma linguagem fantástica";
const palavra = "arara";

// crie as variáveis


console.log(quantidadeVogais, quantidadePalavras, invertido, ehPalindromo);
""",
 "solution": r"""const texto = "JavaScript é uma linguagem fantástica";
const palavra = "arara";

const vogais = "aeiou";
const minusculo = texto.toLowerCase();

let contador = 0;
for (const letra of minusculo) {
  if (vogais.includes(letra)) contador++;
}
const quantidadeVogais = contador;

const palavras = texto.split(" ");
const quantidadePalavras = palavras.length;
const invertido = texto.split("").reverse().join("");
const invertida = palavra.split("").reverse().join("");
const ehPalindromo = palavra === invertida;

console.log(quantidadeVogais, quantidadePalavras, invertido, ehPalindromo);
""",
 "hint": r"""Normalize antes de contar: `texto.toLowerCase()`. Para o palíndromo, inverta `palavra` e compare com ela mesma.""",
 "tests": [
   {"msg": "quantidadeVogais deve ser 16",
    "code": r"""quantidadeVogais === 12"""},
   {"msg": "palavras deve ter 5 itens",
    "code": r"""Array.isArray(palavras) && palavras.length === 5 && palavras[0] === "JavaScript" """},
   {"msg": "quantidadePalavras deve ser 5",
    "code": r"""quantidadePalavras === 5"""},
   {"msg": "invertido deve ser o texto ao contrário",
    "code": r"""invertido === texto.split("").reverse().join("") && invertido[0] === "a" && invertido.length === texto.length"""},
   {"msg": "ehPalindromo deve ser true para \"arara\"",
    "code": r"""ehPalindromo === true"""},
 ],
},

]},
]
