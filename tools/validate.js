/* Validador de conteúdo.
   Para cada lição, executa a SOLUÇÃO dentro da MESMA sandbox usada pelo app
   (o documento do runner, com srcdoc + postMessage) e confere se todos os
   testes passam. Uso: node tools/validate.js [filtro] [limite] */
const fs = require('fs');
const path = require('path');
const { JSDOM, VirtualConsole } = require('jsdom');

const file = path.join(__dirname, '..', 'index.html');
const filter = process.argv[2] || '';
const limit = process.argv[3] ? parseInt(process.argv[3], 10) : Infinity;

const vc = new VirtualConsole();
vc.on('jsdomError', (e) => { if (!/Not implemented/.test(e.message)) console.error('JSDOM:', e.message); });

const dom = new JSDOM(fs.readFileSync(file, 'utf8'), { runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc });
const app = dom.window.__app;
if (!app) { console.error('app não inicializou'); process.exit(1); }

const lessons = app.flat.filter((l) => !filter || l.id.includes(filter) ||
  l.title.toLowerCase().includes(filter.toLowerCase()));

function runInSandbox(lesson, code) {
  return new Promise((resolve) => {
    const bodyHTML = lesson.html || '<div id="demo"></div>';
    const doc = app.sandboxDoc(bodyHTML, 1);
    const sandbox = new JSDOM(doc, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://sandbox.local/' });
    const win = sandbox.window;
    let done = false;
    const finish = (v) => { if (!done) { done = true; resolve(v); try { win.close(); } catch (e) {} } };
    const timer = setTimeout(() => finish({ error: 'TIMEOUT (possível loop infinito)' }), 8000);

    win.addEventListener('message', (ev) => {
      const d = ev.data;
      if (!d || d.runId !== 1) return;
      if (d.type === 'result') {
        clearTimeout(timer);
        finish({ results: d.results || [], error: d.error });
      }
    });

    setTimeout(() => {
      win.postMessage({ type: 'run', runId: 1, source: app.buildHarnessSource(code, lesson.tests || []) }, '*');
    }, 30);
  });
}

function syntaxCheck(code) {
  try { new Function('return ( ' + code + ' );'); return null; }
  catch (e) { return e.message; }
}

(async () => {
  let fails = 0, checked = 0;
  const problems = [];

  for (const lesson of lessons.slice(0, limit)) {
    // pré-checagem: cada teste precisa ser uma expressão JS válida
    const badSyntax = lesson.tests.map((t, i) => ({ i, t, err: syntaxCheck(t.code) })).filter((x) => x.err);
    if (badSyntax.length) {
      fails++;
      problems.push(`${lesson.id} — ${lesson.title}\n` + badSyntax.map((b) => `   ✕ teste ${b.i + 1} com erro de sintaxe: ${b.err}\n     ${b.t.code}`).join('\n'));
      continue;
    }
    let solErr = null;
    try { new (Object.getPrototypeOf(async function () {}).constructor)(lesson.solution); } catch (e) { solErr = e.message; }
    if (solErr) { fails++; problems.push(`${lesson.id} — solução com erro de sintaxe: ${solErr}`); continue; }

    const out = await runInSandbox(lesson, lesson.solution);
    checked++;
    if (out.error) {
      fails++;
      problems.push(`${lesson.id} — ${lesson.title}\n   ✕ erro de execução: ${out.error}`);
      continue;
    }
    const bad = out.results.map((r, i) => ({ ...r, msg: (lesson.tests[i] || {}).msg })).filter((r) => !r.ok);
    if (out.results.length !== lesson.tests.length) {
      fails++;
      problems.push(`${lesson.id} — ${lesson.title}\n   ! esperava ${lesson.tests.length} resultados, veio ${out.results.length}`);
    } else if (bad.length) {
      fails++;
      problems.push(`${lesson.id} — ${lesson.title}\n` + bad.map((b) => `   ✕ ${b.msg}${b.err ? '  [' + b.err + ']' : ''}`).join('\n'));
    } else {
      process.stdout.write('.');
    }
  }

  console.log('\n');
  if (problems.length) console.log(problems.join('\n') + '\n');
  console.log(`validadas: ${checked}/${lessons.length} lições · com problema: ${fails}`);
  process.exit(fails ? 1 : 0);
})();
