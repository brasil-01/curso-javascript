/* ================================================================
   Curso de JavaScript — engine
   Editor + sandbox de execução + testes automáticos
   ================================================================ */
(function () {
  'use strict';

  var COURSE = window.COURSE || [];
  var $ = function (id) { return document.getElementById(id); };
  var KEY = 'jscurso.progress.v1';

  /* ---------------- storage (tolerante a sandbox sem localStorage) ---- */
  var mem = null;
  var store = {
    read: function () {
      try {
        var raw = localStorage.getItem(KEY);
        return raw ? JSON.parse(raw) : (mem || { done: {}, last: null, code: {} });
      } catch (e) { return mem || { done: {}, last: null, code: {} }; }
    },
    write: function (v) {
      mem = v;
      try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) {}
    }
  };
  var state = store.read();
  if (!state.done) state.done = {};
  if (!state.code) state.code = {};
  function save() { store.write(state); }

  /* ---------------- flatten ------------- */
  var flat = [];
  COURSE.forEach(function (mod, mi) {
    (mod.lessons || []).forEach(function (l, li) {
      l._mod = mod; l._mi = mi; l._li = li; l._n = flat.length + 1;
      flat.push(l);
    });
  });
  var total = flat.length;
  function byId(id) { for (var i = 0; i < flat.length; i++) if (flat[i].id === id) return flat[i]; return null; }

  /* ---------------- highlighter ------------- */
  var KW = /^(?:const|let|var|function|return|if|else|for|while|do|switch|case|break|continue|new|typeof|instanceof|class|extends|super|this|try|catch|finally|throw|async|await|yield|import|export|from|default|null|undefined|true|false|in|of|delete|void|static|get|set|NaN|Infinity)$/;

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  var TOKEN = /(\/\/[^\n]*|\/\*[\s\S]*?\*\/)|(`(?:\\[\s\S]|[^`\\])*`|"(?:\\[\s\S]|[^"\\\n])*"|'(?:\\[\s\S]|[^'\\\n])*')|(\b\d[\d_]*(?:\.\d+)?(?:[eE][+-]?\d+)?n?\b)|([A-Za-z_$][\w$]*)|(\s+)|([^\s\w$])/g;

  function hlJS(src) {
    var out = '', last = 0, m;
    TOKEN.lastIndex = 0;
    while ((m = TOKEN.exec(src))) {
      if (m.index > last) out += esc(src.slice(last, m.index));
      if (m[1]) out += '<span class="c">' + esc(m[0]) + '</span>';
      else if (m[2]) out += '<span class="s">' + esc(m[0]) + '</span>';
      else if (m[3]) out += '<span class="n">' + esc(m[0]) + '</span>';
      else if (m[4]) {
        if (KW.test(m[0])) out += '<span class="k">' + esc(m[0]) + '</span>';
        else if (/^\s*\(/.test(src.slice(TOKEN.lastIndex))) out += '<span class="f">' + esc(m[0]) + '</span>';
        else if (/^[A-Z]/.test(m[0])) out += '<span class="f">' + esc(m[0]) + '</span>';
        else out += esc(m[0]);
      } else if (m[5]) out += m[0];
      else out += '<span class="p">' + esc(m[0]) + '</span>';
      last = TOKEN.lastIndex;
    }
    out += esc(src.slice(last));
    return out;
  }

  /* ---------------- mini markdown ------------- */
  function inline(s) {
    var out = esc(s);
    out = out.replace(/`([^`]+)`/g, function (_, c) { return '<code>' + c + '</code>'; });
    out = out.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    out = out.replace(/(^|[\s(])\*([^*\n]+)\*/g, '$1<em>$2</em>');
    out = out.replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
    return out;
  }

  function md(src) {
    if (!src) return '';
    var lines = String(src).replace(/\r/g, '').split('\n');
    var html = '', i = 0, list = null, para = [];

    function flushPara() {
      if (para.length) { html += '<p>' + para.join(' ') + '</p>'; para = []; }
    }
    function flushList() {
      if (list) { html += '</' + list + '>'; list = null; }
    }

    while (i < lines.length) {
      var line = lines[i];

      // fenced code
      var fence = line.match(/^```(\w*)\s*$/);
      if (fence) {
        flushPara(); flushList();
        var buf = [], lang = fence[1];
        i++;
        while (i < lines.length && !/^```\s*$/.test(lines[i])) { buf.push(lines[i]); i++; }
        i++;
        var code = buf.join('\n');
        html += '<pre><code>' + (lang === '' || lang === 'js' || lang === 'javascript' ? hlJS(code) : esc(code)) + '</code></pre>';
        continue;
      }

      if (/^\s*$/.test(line)) { flushPara(); flushList(); i++; continue; }

      var h = line.match(/^(#{2,4})\s+(.*)$/);
      if (h) { flushPara(); flushList(); var lv = h[1].length; html += '<h' + lv + '>' + inline(h[2]) + '</h' + lv + '>'; i++; continue; }

      var note = line.match(/^>\s?\[?(\w*)\]?\s*(.*)$/);
      if (note) {
        flushPara(); flushList();
        var kind = note[1].toLowerCase(), cls = 'note';
        if (kind === 'warn' || kind === 'atencao' || kind === 'atenção') cls = 'note warn';
        if (kind === 'tip' || kind === 'dica') cls = 'note tip';
        var body = note[2];
        i++;
        while (i < lines.length && /^>\s?/.test(lines[i])) { body += ' ' + lines[i].replace(/^>\s?/, ''); i++; }
        html += '<div class="' + cls + '">' + inline(body) + '</div>';
        continue;
      }

      if (/^---+$/.test(line)) { flushPara(); flushList(); html += '<hr>'; i++; continue; }

      var ul = line.match(/^\s*[-*]\s+(.*)$/);
      if (ul) {
        flushPara();
        if (list !== 'ul') { flushList(); html += '<ul>'; list = 'ul'; }
        html += '<li>' + inline(ul[1]) + '</li>'; i++; continue;
      }
      var ol = line.match(/^\s*\d+[.)]\s+(.*)$/);
      if (ol) {
        flushPara();
        if (list !== 'ol') { flushList(); html += '<ol>'; list = 'ol'; }
        html += '<li>' + inline(ol[1]) + '</li>'; i++; continue;
      }

      flushList();
      para.push(inline(line.trim()));
      i++;
    }
    flushPara(); flushList();
    return html;
  }

  /* ---------------- sandbox runner ------------- */
  // fmtValue é serializado (toString) para dentro do harness: use só globais.
  function fmtValue(v) {
    var t = typeof v;
    if (v === null) return 'null';
    if (t === 'undefined') return 'undefined';
    if (t === 'string') return v;
    if (t === 'number' || t === 'boolean' || t === 'bigint') return String(v);
    if (t === 'function') return 'ƒ ' + (v.name || 'anônima') + '()';
    if (t === 'symbol') return v.toString();
    if (v instanceof Error) return v.name + ': ' + v.message;
    if (typeof Node !== 'undefined' && v instanceof Node) return '<' + String(v.nodeName).toLowerCase() + (v.id ? '#' + v.id : '') + '>';
    if (Array.isArray(v)) return '[' + v.map(fmtValue).join(', ') + ']';
    try { var s = JSON.stringify(v); return s === undefined ? String(v) : s; } catch (e) { return String(v); }
  }

  function buildTestsSource(tests) {
    return (tests || []).map(function (t) {
      return 'try { __res.push({ ok: !!( await (async function () { return ( ' + t.code + ' ); })() ), err: null }); } ' +
        'catch (e) { __res.push({ ok: false, err: (e && e.message) ? ((e.name || "Error") + ": " + e.message) : String(e) }); }';
    }).join('\n');
  }

  function buildHarnessSource(code, tests) {
    var head = [
      'var __logs = [];',
      'var __fmt = ' + fmtValue.toString() + ';',
      'function __emit(level, args) {',
      '  var text;',
      '  try { text = Array.prototype.map.call(args, __fmt).join(" "); } catch (e) { text = String(args); }',
      '  __logs.push({ level: level, text: text });',
      '  try { if (typeof __RID !== "undefined" && typeof parent !== "undefined" && parent !== window) parent.postMessage({ type: "log", runId: __RID, level: level, text: text }, "*"); } catch (e) {}',
      '}',
      'var console = {',
      '  log: function () { __emit("log", arguments); }, info: function () { __emit("log", arguments); },',
      '  warn: function () { __emit("warn", arguments); }, error: function () { __emit("error", arguments); },',
      '  debug: function () { __emit("log", arguments); }, table: function () { __emit("log", arguments); }',
      '};',
      'var alert = function () { __emit("warn", arguments); };',
      'var prompt = function () { __emit("warn", ["prompt() não funciona dentro do sandbox"]); return null; };',
      'var confirm = function () { __emit("warn", ["confirm() não funciona dentro do sandbox — retornando true"]); return true; };',
      'var __res = [];',
      'function __printed() { return __logs.map(function (l) { return l.text; }).join("\\n"); }',
      'function __normalize(s) { return String(s).toLowerCase().replace(/\\s+/g, " ").trim(); }',
      'var __code = ' + JSON.stringify(String(code)) + ';'
    ].join('\n');

    var tail = buildTestsSource(tests) + '\nreturn { results: __res, logs: __logs };';
    return head + '\n' + code + '\n' + tail;
  }

  // A sandbox é um iframe com srcdoc + sandbox="allow-scripts": o código do aluno
  // roda isolado, sem acesso à página do curso. A comunicação é via postMessage.
  var RUNNER = [
    '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">',
    '<style>',
    'html,body{margin:0}',
    'body{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;font-size:15px;line-height:1.55;color:#0b0f14;background:#fff;padding:14px}',
    'h1{font-size:20px;margin:0 0 8px}h2{font-size:17px;margin:14px 0 6px;font-weight:700}',
    'button{font:inherit;cursor:pointer;padding:6px 12px;border-radius:7px;border:1px solid #c9d1d9;background:#f6f8fa}',
    'button:hover{background:#eaeef2}input{font:inherit;padding:6px 9px;border:1px solid #c9d1d9;border-radius:7px}',
    'ul{padding-left:20px}li{margin:3px 0}',
    '#demo{padding:10px;border:1px dashed #c9d1d9;border-radius:8px}',
    '</style></head><body>',
    '{{BODY}}',
    '<scr' + 'ipt>',
    '(function () {',
    '  var RID = {{RID}};',
    '  function post(m) { m.runId = RID; try { parent.postMessage(m, "*"); } catch (e) {} }',
    '  window.onerror = function (msg) { post({ type: "runtime-error", message: String(msg) }); return true; };',
    '  var AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;',
    '  window.addEventListener("message", function (ev) {',
    '    var d = ev.data;',
    '    if (!d || d.type !== "run" || d.runId !== RID) return;',
    '    (async function () {',
    '      try {',
    '        var fn = new AsyncFunction("__RID", d.source);',
    '        var r = await fn(RID);',
    '        post({ type: "result", results: (r && r.results) || [], error: null });',
    '      } catch (e) {',
    '        post({ type: "result", results: [], error: (e && e.message) ? ((e.name || "Error") + ": " + e.message) : String(e) });',
    '      }',
    '    })();',
    '  });',
    '  post({ type: "ready" });',
    '})();',
    '</scr' + 'ipt></body></html>'
  ].join('\n');

  // ---- Execução isolada: Worker (lições sem DOM) ou iframe (lições com DOM) ----
  // O Worker pode ser encerrado à força (terminate), o que protege o app de
  // loops infinitos digitados pelo aluno.
  var WORKER_SRC = [
    'self.onmessage = async function (e) {',
    '  var d = e.data;',
    '  if (!d || d.type !== "run") return;',
    '  var AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;',
    '  try {',
    '    var fn = new AsyncFunction(d.source);',
    '    var r = await fn(0);',
    '    self.postMessage({ type: "result", runId: d.runId, results: (r && r.results) || [], logs: (r && r.logs) || [], error: null });',
    '  } catch (err) {',
    '    self.postMessage({ type: "result", runId: d.runId, results: [], logs: [], error: (err && err.message) ? ((err.name || "Error") + ": " + err.message) : String(err) });',
    '  }',
    '};'
  ].join('\n');

  var workerOK = null;
  function canUseWorker() {
    if (workerOK !== null) return workerOK;
    try {
      var url = URL.createObjectURL(new Blob(['self.close()'], { type: 'text/javascript' }));
      var w = new Worker(url);
      w.terminate();
      URL.revokeObjectURL(url);
      workerOK = true;
    } catch (e) {
      workerOK = false;
    }
    return workerOK;
  }

  var iframe = $('sandbox');
  var runSeq = 0, pending = null, pendingTimer = null, curCode = '', curTests = [], pageMode = false;

  function clearPending() {
    if (pendingTimer) { clearTimeout(pendingTimer); pendingTimer = null; }
    if (pending && pending.worker) { try { pending.worker.terminate(); } catch (e) {} }
    pending = null;
  }

  var AsyncFunc = Object.getPrototypeOf(async function () {}).constructor;

  function syntaxProblem(code) {
    try { new AsyncFunc(code); return null; } catch (e) { return e.message || String(e); }
  }

  function startRun(code, tests, kind) {
    clearPending();

    var iss = syntaxProblem(code);
    if (iss) {
      var dica = 'Erro de sintaxe: ' + iss + '. Confira parênteses, chaves { }, colchetes [ ] e aspas — e o ponto e vírgula no fim?';
      addLine('error', dica);
      showTab('console');
      if (kind === 'test') { showTests([]); setTestBadge(0, (tests || []).length); }
      toast('Erro de sintaxe no seu código', 'error');
      return;
    }

    var runId = ++runSeq;
    var useWorker = !(current && current.html) && canUseWorker();
    pending = { runId: runId, kind: kind || 'run' };
    curTests = tests || [];
    pageMode = !!(current && current.html);

    if (kind !== 'run') clearConsole();

    if (useWorker) {
      try {
        var wurl = URL.createObjectURL(new Blob([WORKER_SRC], { type: 'text/javascript' }));
        var w = new Worker(wurl);
        pending.worker = w;
        w.onmessage = function (ev) {
          var d = ev.data;
          if (d && d.type === 'result' && pending && d.runId === pending.runId) { finishRun(d); }
        };
        w.onerror = function (ev) {
          if (pending) addLine('error', 'Erro no worker: ' + (ev.message || 'desconhecido'));
        };
        w.postMessage({ type: 'run', runId: runId, source: buildHarnessSource(code, tests) });

        pendingTimer = setTimeout(function () {
          if (pending && pending.runId === runId) {
            addLine('error', 'Tempo esgotado (5s). Seu código parece estar em loop infinito — verifique as condições dos seus while/for.');
            if (pending.kind === 'test') {
              showTests(curTests.map(function () { return { ok: false, err: 'Execução interrompida (timeout)' }; }));
              setTestBadge(0, curTests.length);
            }
            toast('Loop infinito? Execução interrompida', 'error');
            clearPending();
          }
        }, 5000);
        return;
      } catch (e) {
        // se o Worker falhar (ex.: sandbox sem blob), cai no iframe
      }
    }

    var body = (current && current.html) ? current.html : '<div id="demo"></div>';
    var html = RUNNER.replace('{{BODY}}', body).replace('{{RID}}', String(runId));
    html += '<!--' + runId + '-->';

    iframe.srcdoc = html;

    pendingTimer = setTimeout(function () {
      if (pending && pending.runId === runId) {
        addLine('error', 'Tempo esgotado (6s). Seu código pode estar em loop infinito — verifique seus while/for.');
        if (pending.kind === 'test') showTests(curTests.map(function () { return { ok: false, err: 'Execução interrompida (timeout)' }; }));
        clearPending();
      }
    }, 6000);

    window.__pendingRun = { runId: runId, code: code, tests: tests || [] };
  }

  window.addEventListener('message', function (ev) {
    var d = ev.data;
    if (!d || typeof d !== 'object') return;
    if (!pending || d.runId !== pending.runId) return;

    if (d.type === 'ready') {
      var p = window.__pendingRun;
      if (p && p.runId === d.runId) {
        try {
          iframe.contentWindow.postMessage({ type: 'run', runId: d.runId, source: buildHarnessSource(p.code, p.tests) }, '*');
        } catch (e) {}
      }
      return;
    }
    if (d.type === 'log') { addLine(d.level, d.text); return; }
    if (d.type === 'runtime-error') { addLine('error', d.message); return; }
    if (d.type === 'result') {
      finishRun(d);
      return;
    }
  });

  function finishRun(d) {
    {
      var kind = pending ? pending.kind : 'run';
      clearPending();
      if (d.logs && d.logs.length) {
        d.logs.forEach(function (l) { addLine(l.level, l.text); });
      }
      if (d.error) {
        addLine('error', d.error);
        showTab('console');
        if (kind === 'test') {
          showTests([]);
          setTestBadge(0, curTests.length);
        }
        toast('Erro no código — leia o console', 'error');
      } else {
        if (kind === 'test') {
          var results = d.results || [];
          showTests(results);
          var passed = results.filter(function (r) { return r.ok; }).length;
          setTestBadge(passed, results.length);
          if (results.length && passed === results.length) onAllPassed();
          else if (results.length) toast('Faltam ' + (results.length - passed) + ' teste(s)', 'error');
        } else {
          toast('Código executado', 'ok');
        }
      }
    }
  }

  /* ---------------- editor ---------------- */
  var editor = $('editor'), hl = $('hl'), gutter = $('gutter');
  var dirty = false;

  function setDirty(v) { dirty = v; $('dirty').classList.toggle('on', v); }

  function paint() {
    var v = editor.value;
    hl.innerHTML = hlJS(v) + '\n';
    var lines = v.split('\n').length;
    var out = '';
    for (var i = 1; i <= Math.max(lines, 1); i++) out += i + '\n';
    gutter.textContent = out;
    hl.scrollTop = editor.scrollTop; hl.scrollLeft = editor.scrollLeft;
    gutter.scrollTop = editor.scrollTop;
    setDirty(editor.value !== (editor.dataset.base || ''));
  }

  function insertText(txt) {
    var s = editor.selectionStart, e = editor.selectionEnd;
    editor.value = editor.value.slice(0, s) + txt + editor.value.slice(e);
    editor.selectionStart = editor.selectionEnd = s + txt.length;
    paint();
  }

  editor.addEventListener('input', paint);
  editor.addEventListener('scroll', function () {
    hl.scrollTop = editor.scrollTop; hl.scrollLeft = editor.scrollLeft;
    gutter.scrollTop = editor.scrollTop;
  });

  var PAIRS = { '(': ')', '[': ']', '{': '}', '"': '"', "'": "'", '`': '`' };

  editor.addEventListener('keydown', function (ev) {
    var s = editor.selectionStart, e = editor.selectionEnd, v = editor.value;
    var mod = ev.ctrlKey || ev.metaKey;

    if (mod && ev.key === 'Enter') {
      ev.preventDefault();
      if (ev.shiftKey) doTest(); else doRun();
      return;
    }
    if (mod && (ev.key === '/' || ev.code === 'Slash')) {
      ev.preventDefault();
      toggleComment();
      return;
    }
    if (ev.key === 'Tab') {
      ev.preventDefault();
      if (s !== e) {
        var start = v.lastIndexOf('\n', s - 1) + 1;
        var chunk = v.slice(start, e);
        var newChunk = ev.shiftKey
          ? chunk.replace(/^ {1,2}/gm, '')
          : chunk.replace(/^/gm, '  ');
        editor.value = v.slice(0, start) + newChunk + v.slice(e);
        editor.selectionStart = start; editor.selectionEnd = start + newChunk.length;
      } else {
        insertText('  ');
      }
      return;
    }
    if (ev.key === 'Enter') {
      ev.preventDefault();
      var lineStart = v.lastIndexOf('\n', s - 1) + 1;
      var indent = (v.slice(lineStart, s).match(/^[ \t]*/) || [''])[0];
      var before = v.slice(s - 1, s);
      var after = v.slice(s, s + 1);
      var extra = (before === '{' || before === '[' || before === '(') ? '  ' : '';
      var closing = (before === '{' && after === '}') ? '\n' + indent : '';
      insertText('\n' + indent + extra + closing);
      if (closing) { editor.selectionStart = editor.selectionEnd = s + 1 + indent.length + extra.length; paint(); }
      return;
    }
    // fechamento em linha só com espaços: dedenta um nível
    if (s === e && '}])'.indexOf(ev.key) > -1) {
      var ls = v.lastIndexOf('\n', s - 1) + 1;
      var beforeCaret = v.slice(ls, s);
      if (/^\s+$/.test(beforeCaret) && beforeCaret.length >= 2) {
        ev.preventDefault();
        editor.value = v.slice(0, s - 2) + ev.key + v.slice(s);
        editor.selectionStart = editor.selectionEnd = s - 1;
        paint();
        return;
      }
    }
    // digitar um fechamento que já existe apenas "passa por cima"
    if (s === e && ')]}"\'`'.indexOf(ev.key) > -1 && v.slice(s, s + 1) === ev.key) {
      ev.preventDefault();
      editor.selectionStart = editor.selectionEnd = s + 1;
      return;
    }
    if (PAIRS[ev.key] && s === e) {
      var next = v.slice(s, s + 1);
      if (ev.key === next) { // pular
        ev.preventDefault(); editor.selectionStart = editor.selectionEnd = s + 1; return;
      }
      if (next === '' || /[\s)\]},;]/.test(next)) {
        ev.preventDefault();
        editor.value = v.slice(0, s) + ev.key + PAIRS[ev.key] + v.slice(e);
        editor.selectionStart = editor.selectionEnd = s + 1;
        paint();
        return;
      }
    }
    if (ev.key === 'Backspace' && s === e) {
      var pair = v.slice(s - 1, s + 1);
      if (pair.length === 2 && PAIRS[pair[0]] === pair[1]) {
        ev.preventDefault();
        editor.value = v.slice(0, s - 1) + v.slice(s + 1);
        editor.selectionStart = editor.selectionEnd = s - 1;
        paint();
      }
    }
  });

  function toggleComment() {
    var v = editor.value, s = editor.selectionStart, e = editor.selectionEnd;
    var start = v.lastIndexOf('\n', s - 1) + 1;
    var endNl = v.indexOf('\n', e);
    var end = endNl === -1 ? v.length : endNl;
    var chunk = v.slice(start, end);
    var lines = chunk.split('\n');
    var allCommented = lines.every(function (l) { return /^\s*\/\//.test(l) || /^\s*$/.test(l); });
    var out = lines.map(function (l) {
      if (allCommented) return l.replace(/^(\s*)\/\/ ?/, '$1');
      return l.replace(/^(\s*)(?=\S)/, '$1// ');
    }).join('\n');
    editor.value = v.slice(0, start) + out + v.slice(end);
    editor.selectionStart = start; editor.selectionEnd = start + out.length;
    paint();
  }

  /* ---------------- console ---------------- */
  function clearConsole() { $('console').innerHTML = ''; }

  function addLine(level, text) {
    var c = $('console');
    if (c.querySelector('.empty')) c.innerHTML = '';
    var div = document.createElement('div');
    div.className = 'ln ' + (level || 'log');
    var icons = { log: '›', warn: '▲', error: '✕', sys: '·', ok: '✓' };
    div.innerHTML = '<span class="ic">' + (icons[level] || '›') + '</span><span class="tx"></span>';
    div.querySelector('.tx').textContent = text;
    c.appendChild(div);
    c.scrollTop = c.scrollHeight;
  }

  function emptyConsole(msg) {
    $('console').innerHTML = '<div class="empty">' + esc(msg || 'Nada aqui ainda. Clique em Executar (Ctrl+Enter) para rodar seu código.') + '</div>';
  }

  /* ---------------- lesson rendering ---------------- */
  var current = null;
  var viewMode = 'home';
  var totalTestes = flat.reduce(function (acc, l) { return acc + (l.tests || []).length; }, 0);

  function render(lessonId) {
    var l = byId(lessonId) || flat[0];
    if (!l) return;
    viewMode = 'lesson';
    document.body.classList.remove('view-home');
    current = l;
    state.last = l.id; save();

    var saved = state.code[l.id];
    var code = (saved !== undefined ? saved : l.starter) || '';

    editor.value = code;
    editor.dataset.base = l.starter || '';
    paint();
    clearConsole();
    emptyConsole(l.html ? 'O resultado aparece na aba "Página" depois de executar.' : null);
    var oldTests = $('tests'); if (oldTests) { oldTests.classList.remove('show'); oldTests.innerHTML = ''; }
    $('fileName').textContent = l.file || 'index.js';
    $('tabPage').style.display = l.html ? '' : 'none';
    showTab('console');

    $('lessonPane').innerHTML =
      '<div class="crumb">Módulo ' + (l._mi + 1) + ' <span class="sep">/</span> ' + esc(l._mod.title) + '</div>' +
      '<h1>' + esc(l.title) + '</h1>' +
      '<div class="meta">' +
        '<span class="pill">Lição ' + l._n + ' de ' + total + '</span>' +
        '<span>⏱ ' + (l.minutes || 6) + ' min</span>' +
        (l.html ? '<span class="pill">DOM / navegador</span>' : '') +
      '</div>' +
      '<div class="md">' + md(l.theory) + '</div>' +
      (l.task ? '<div class="task"><h3>🎯 Sua tarefa</h3><div class="md">' + md(l.task) + '</div></div>' : '') +
      '<div class="hintbox" id="hintBox"></div>' +
      '<div class="row-btns">' +
        '<button class="btn blue" id="testBtn2">▶ Executar testes</button>' +
        (l.hint ? '<button class="btn ghost" id="hintBtn2">💡 Ver dica</button>' : '') +
        (l.solution ? '<button class="btn ghost" id="solBtn">👁 Ver solução</button>' : '') +
      '</div>' +
      '<div class="tests" id="tests"></div>' +
      '<div class="done-banner" id="doneBanner">' +
        '<span class="em">🎉</span><div><b>Lição concluída!</b><span>Você acertou todos os testes.</span></div>' +
        '<div style="flex:1"></div>' +
        '<button class="btn gold" id="nextBtn">Próxima lição →</button>' +
      '</div>' +
      '<div class="row-btns" style="margin-top:26px;border-top:1px solid var(--line);padding-top:16px">' +
        '<button class="btn ghost small" id="prevBtn">← Anterior</button>' +
        '<div style="flex:1"></div>' +
        '<button class="btn ghost small" id="nextBtn2">Próxima →</button>' +
      '</div>';

    // rebind (o HTML do painel é recriado)
    $('hintBox').innerHTML = l.hint ? '<strong>Dica:</strong> ' + inline(l.hint) : '';
    $('testBtn2').onclick = doTest;
    if ($('hintBtn2')) $('hintBtn2').onclick = function () {
      var hb = $('hintBox');
      hb.classList.toggle('show');
    };
    if ($('solBtn')) $('solBtn').onclick = function () {
      var btn = $('solBtn');
      askConfirm(btn, '👁 Ver solução', function () { setSolution(l); });
    };
    $('prevBtn').onclick = function () { go(-1); };
    $('nextBtn2').onclick = function () { go(1); };
    $('nextBtn').onclick = function () { go(1); };

    if (state.done[l.id]) $('doneBanner').classList.add('show');

    renderNav();
    $('lessonPane').scrollTop = 0;
    document.body.classList.remove('nav-open');
    search.value = '';
  }

  // ---------------- tela inicial: escolha de lições ----------------
  function homePrefs() {
    if (!state.home) state.home = { view: 'grid', filter: 'all' };
    if (!state.home.view) state.home.view = 'grid';
    if (!state.home.filter) state.home.filter = 'all';
    return state.home;
  }

  function matchesFilter(l, filter) {
    if (filter === 'pending') return !state.done[l.id];
    if (filter === 'done') return !!state.done[l.id];
    if (filter === 'dom') return !!l.html;
    return true;
  }

  function renderHome() {
    viewMode = 'home';
    current = null;
    document.body.classList.add('view-home');

    var prefs = homePrefs();
    var view = prefs.view;
    var filter = prefs.filter;

    var done = Object.keys(state.done).length;
    var pct = total ? Math.round(done / total * 100) : 0;
    var nDom = flat.filter(function (l) { return l.html; }).length;
    var nPend = total - done;

    // "continuar" aponta para onde o aluno parou; se já concluiu, a próxima pendente
    var ultima = (state.last && byId(state.last)) ? byId(state.last) : null;
    var proxima = null;
    if (ultima) {
      if (!state.done[ultima.id]) {
        proxima = ultima;
      } else {
        var pos = flat.indexOf(ultima);
        for (var j = pos + 1; j < flat.length; j++) { if (!state.done[flat[j].id]) { proxima = flat[j]; break; } }
      }
    }
    if (!proxima) {
      for (var i = 0; i < flat.length; i++) { if (!state.done[flat[i].id]) { proxima = flat[i]; break; } }
    }
    var alvo = proxima || flat[0];

    var html = '<div class="home">';

    // ----- hero -----
    html += '<section class="hero">';
    html += '<span class="hero-tag">' + COURSE.length + ' módulos · ' + total + ' lições · ' + totalTestes + ' testes</span>';
    html += '<h1>Aprenda JavaScript escrevendo código</h1>';
    html += '<p class="hero-sub">Escolha uma lição abaixo — todas estão liberadas. Cada uma traz uma explicação curta, uma tarefa prática no editor e testes automáticos que conferem o seu código na hora.</p>';
    html += '<div class="hero-actions">' +
      '<button class="btn gold big" id="continueBtn">' +
      (done === total
        ? 'Curso concluído — revisar a primeira lição →'
        : (ultima ? 'Continuar: ' + esc(alvo.title) + ' →' : 'Começar pela lição 1 →')) +
      '</button>' +
      (done ? '<button class="btn ghost big" id="restartBtn">Ver do começo</button>' : '') +
      '</div>';
    html += '<div class="hero-progress"><div class="track"><div class="fill" style="width:' + pct + '%"></div></div>' +
      '<span>' + done + ' de ' + total + ' lições concluídas · ' + pct + '%</span></div>';
    html += '</section>';

    // ----- barra de ferramentas: filtros + visão -----
    var chips = [
      { id: 'all', label: 'Todas', n: total },
      { id: 'pending', label: 'Pendentes', n: nPend },
      { id: 'done', label: 'Concluídas', n: done },
      { id: 'dom', label: 'Com DOM', n: nDom }
    ];
    html += '<div class="home-tools">';
    html += '<div class="chips" role="tablist" aria-label="Filtrar lições">';
    chips.forEach(function (c) {
      html += '<button class="chip' + (filter === c.id ? ' on' : '') + '" data-filter="' + c.id + '" role="tab" aria-selected="' + (filter === c.id) + '">' +
        c.label + ' <b>' + c.n + '</b></button>';
    });
    html += '</div>';
    html += '<div class="viewswitch" role="group" aria-label="Modo de exibição">' +
      '<button class="vs' + (view === 'grid' ? ' on' : '') + '" data-view="grid" title="Ver em grade">▦ Grade</button>' +
      '<button class="vs' + (view === 'trail' ? ' on' : '') + '" data-view="trail" title="Ver como trilha">🧭 Trilha</button>' +
      '</div>';
    html += '</div>';

    // ----- módulos -----
    var mostrando = 0;
    COURSE.forEach(function (mod, mi) {
      var todas = mod.lessons || [];
      var lessons = todas.filter(function (l) { return matchesFilter(l, filter); });
      if (!lessons.length) return;
      mostrando += lessons.length;

      var feitas = todas.filter(function (l) { return state.done[l.id]; }).length;
      var pendenteMod = null;
      for (var k = 0; k < todas.length; k++) { if (!state.done[todas[k].id]) { pendenteMod = todas[k]; break; } }

      html += '<section class="mod-sec" data-mi="' + mi + '">' +
        '<header class="mod-sec-head">' +
        '<span class="ico">' + (mod.icon || '📦') + '</span>' +
        '<h2>' + esc(mod.title) + '</h2>' +
        '<span class="mod-sec-count' + (feitas === todas.length ? ' full' : '') + '">' + feitas + '/' + todas.length + '</span>' +
        (pendenteMod
          ? '<button class="mod-next" data-goto="' + pendenteMod.id + '" title="Abrir a próxima lição pendente deste módulo">próxima pendente →</button>'
          : '<span class="mod-complete">✓ módulo completo</span>') +
        '</header>';

      if (view === 'grid') {
        html += '<div class="lesson-grid">';
        lessons.forEach(function (l) {
          var isDone = !!state.done[l.id];
          html += '<button class="card' + (isDone ? ' done' : '') + '" data-id="' + l.id + '" title="' + esc(l.title) + '">' +
            '<span class="card-top">' +
            '<span class="card-num">' + (isDone ? '✓' : l._n) + '</span>' +
            (l.html ? '<span class="card-tag">DOM</span>' : '') +
            '<span class="card-min">⏱ ' + (l.minutes || 6) + ' min</span>' +
            '</span>' +
            '<span class="card-title">' + esc(l.title) + '</span>' +
            '</button>';
        });
        html += '</div>';
      } else {
        html += '<div class="trail">';
        lessons.forEach(function (l, idx) {
          var isDone = !!state.done[l.id];
          var isNext = proxima && proxima.id === l.id;
          var side = idx % 2 === 0 ? 'L' : 'R';
          html += '<button class="node-row ' + side + (isDone ? ' done' : '') + (isNext ? ' next' : '') + '" data-id="' + l.id + '" title="' + esc(l.title) + '">' +
            '<span class="node">' + (isDone ? '✓' : l._n) + '</span>' +
            '<span class="node-card">' +
            '<span class="node-title">' + esc(l.title) + '</span>' +
            '<span class="node-meta">⏱ ' + (l.minutes || 6) + ' min' + (l.html ? ' · <span class="card-tag">DOM</span>' : '') +
            (isNext ? ' · <b class="node-here">você está aqui</b>' : '') + '</span>' +
            '</span></button>';
        });
        html += '</div>';
      }
      html += '</section>';
    });

    if (!mostrando) {
      html += '<div class="home-empty"><span>🔍</span><b>Nenhuma lição neste filtro.</b>' +
        '<button class="btn small" id="clearFilter">Ver todas as lições</button></div>';
    }

    html += '</div>';

    var pane = $('lessonPane');
    var scrollAnterior = pane.scrollTop;
    pane.innerHTML = html;
    pane.scrollTop = scrollAnterior;

    // ----- bindings -----
    $('continueBtn').onclick = function () { render(alvo.id); };
    if ($('restartBtn')) $('restartBtn').onclick = function () { render(flat[0].id); };
    if ($('clearFilter')) $('clearFilter').onclick = function () { prefs.filter = 'all'; save(); renderHome(); };

    Array.prototype.forEach.call(pane.querySelectorAll('.chip'), function (c) {
      c.onclick = function () {
        prefs.filter = c.dataset.filter;
        save();
        pane.scrollTop = 0;
        renderHome();
      };
    });
    Array.prototype.forEach.call(pane.querySelectorAll('.vs'), function (v) {
      v.onclick = function () {
        prefs.view = v.dataset.view;
        save();
        renderHome();
      };
    });
    Array.prototype.forEach.call(pane.querySelectorAll('[data-goto]'), function (b) {
      b.onclick = function () { render(b.dataset.goto); };
    });
    Array.prototype.forEach.call(pane.querySelectorAll('[data-id]'), function (c) {
      c.onclick = function () { render(c.dataset.id); };
    });

    renderNav();
    document.body.classList.remove('nav-open');
  }

  // confirmação em dois cliques (confirm() nativo é bloqueado em iframes sandbox)
  function askConfirm(btn, label, fn) {
    if (!btn) { fn(); return; }
    var isIcon = btn.classList.contains('icon-btn');
    function arm(on) {
      btn.dataset.armed = on ? '1' : '';
      if (isIcon) btn.classList.toggle('armed', on);
      else btn.textContent = on ? 'Confirmar?' : label;
    }
    if (btn.dataset.armed === '1') { arm(false); fn(); return; }
    arm(true);
    clearTimeout(btn._t);
    btn._t = setTimeout(function () { if (btn.dataset.armed === '1') arm(false); }, 3500);
  }

  function setSolution(l) {
    editor.value = l.solution || '';
    paint();
    toast('Solução carregada — estude e clique em Executar testes', 'ok');
  }

  function go(dir) {
    if (!current) return;
    var i = flat.indexOf(current);
    var n = flat[Math.max(0, Math.min(flat.length - 1, i + dir))];
    if (n) render(n.id);
  }

  /* ---------------- nav ---------------- */
  function renderNav() {
    var q = ($('search').value || '').toLowerCase().trim();
    var html = q ? '' : '<button class="lnk home-link' + (viewMode === 'home' ? ' active' : '') + '" data-home="1">' +
      '<span class="home-ico">⌂</span><span class="txt">Início do curso</span></button>';
    COURSE.forEach(function (mod, mi) {
      var lessons = (mod.lessons || []).filter(function (l) {
        return !q || l.title.toLowerCase().indexOf(q) > -1 || mod.title.toLowerCase().indexOf(q) > -1;
      });
      if (!lessons.length) return;
      var doneCount = (mod.lessons || []).filter(function (l) { return state.done[l.id]; }).length;
      var isOpen = q ? true : (current && current._mi === mi);
      html += '<div class="mod' + (isOpen ? ' open' : '') + '" data-mi="' + mi + '">' +
        '<button class="mod-head"><span class="ico">' + (mod.icon || '📦') + '</span>' +
        '<span style="flex:1">' + esc(mod.title) + '</span>' +
        '<span class="cnt">' + doneCount + '/' + (mod.lessons || []).length + '</span>' +
        '<span class="chev">▶</span></button><div class="lessons">';
      lessons.forEach(function (l) {
        var done = !!state.done[l.id];
        html += '<button class="lnk' + (done ? ' done' : '') + (current && current.id === l.id ? ' active' : '') + '" data-id="' + l.id + '">' +
          '<span class="dot">' + (done ? '✓' : '') + '</span><span class="txt">' + esc(l.title) + '</span></button>';
      });
      html += '</div></div>';
    });
    var nav = $('nav');
    nav.innerHTML = html || '<div style="padding:20px 12px;color:var(--mut);font-size:13px">Nenhuma lição encontrada.</div>';

    Array.prototype.forEach.call(nav.querySelectorAll('.mod-head'), function (b) {
      b.onclick = function () { b.parentNode.classList.toggle('open'); };
    });
    Array.prototype.forEach.call(nav.querySelectorAll('.lnk'), function (b) {
      if (b.dataset.home) { b.onclick = renderHome; return; }
      b.onclick = function () { render(b.dataset.id); };
    });

    var active = nav.querySelector('.lnk.active');
    if (active) {
      var r = active.getBoundingClientRect(), nr = nav.getBoundingClientRect();
      if (r.top < nr.top || r.bottom > nr.bottom) active.scrollIntoView({ block: 'center' });
    }
  }

  /* ---------------- progress ---------------- */
  function updateProgress() {
    var done = Object.keys(state.done).length;
    var pct = total ? Math.round(done / total * 100) : 0;
    $('progressFill').style.width = pct + '%';
    $('progressTxt').textContent = done + '/' + total + ' · ' + pct + '%';
  }

  /* ---------------- tests UI ---------------- */
  function hideTests() { var t = $('tests'); if (t) { t.classList.remove('show'); t.innerHTML = ''; } }
  function setTestBadge(p, t) {
    var el = $('testCount');
    if (el) el.textContent = p + '/' + t;
  }

  function showTests(results) {
    var l = current;
    var box = $('tests');
    if (!box) return;
    var tests = l.tests || [];
    var passed = results.filter(function (r) { return r.ok; }).length;
    var allOk = results.length && passed === results.length;

    var label = results.length ? (passed + ' de ' + results.length + ' passaram') : 'não executado';
    var html = '<div class="head">Resultado ' +
      '<span class="badge ' + (allOk ? 'ok' : 'bad') + '">' + label + '</span></div>';

    if (!results.length) {
      html += '<ul class="tlist"><li class="fail"><span class="mk">✕</span><span class="msg">Não foi possível executar os testes porque o código lançou um erro. Corrija o erro mostrado no console e tente novamente.</span></li></ul>';
    } else {
      html += '<ul class="tlist">';
      results.forEach(function (r, i) {
        var msg = (tests[i] && tests[i].msg) || ('Teste ' + (i + 1));
        html += '<li class="' + (r.ok ? 'pass' : 'fail') + '"><span class="mk">' + (r.ok ? '✓' : '✕') + '</span>' +
          '<span class="msg">' + esc(msg) + (r.err ? '<span class="why">' + esc(r.err) + '</span>' : '') + '</span></li>';
      });
      html += '</ul>';
    }
    box.innerHTML = html;
    box.classList.add('show');

    var pane = $('lessonPane');
    var r = box.getBoundingClientRect(), pr = pane.getBoundingClientRect();
    if (r.bottom > pr.bottom || r.top < pr.top) pane.scrollTop += (r.top - pr.top) - 12;
  }

  function onAllPassed() {
    var l = current;
    if (!state.done[l.id]) {
      state.done[l.id] = true;
      save();
      updateProgress();
      renderNav();
      toast('Lição concluída! 🎉', 'ok');
    }
    var b = $('doneBanner');
    if (b) b.classList.add('show');
    if (b) b.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  }

  /* ---------------- actions ---------------- */
  function doRun() {
    if (!current || viewMode !== 'lesson') return;
    startRun(editor.value, [], 'run');
    if (current.html) showTab('page');
  }

  function doTest() {
    if (!current || viewMode !== 'lesson') return;
    startRun(editor.value, current.tests || [], 'test');
    if (current.html) showTab('page');
  }

  function showTab(which) {
    var isPage = which === 'page';
    $('tabConsole').classList.toggle('active', !isPage);
    $('tabPage').classList.toggle('active', isPage);
    $('console').style.display = isPage ? 'none' : '';
    $('iframeWrap').classList.toggle('show', isPage);
  }

  function toast(msg, kind) {
    var t = $('toast');
    t.textContent = (kind === 'ok' ? '✓ ' : kind === 'error' ? '✕ ' : '') + msg;
    t.style.background = kind === 'error' ? '#ff6b6b' : kind === 'ok' ? '#3fb950' : '#f7df1e';
    t.style.color = kind === 'error' || kind === 'ok' ? '#0b0f14' : '#141000';
    t.classList.add('show');
    clearTimeout(t._t);
    t._t = setTimeout(function () { t.classList.remove('show'); }, 2200);
  }

  /* ---------------- wire up ---------------- */
  $('runBtn').onclick = doRun;
  $('testBtn').onclick = function () {
    if (!current || viewMode !== 'lesson') return;
    startRun(editor.value, current.tests || [], 'test');
    if (current.html) showTab('page');
  };
  $('resetCodeBtn').onclick = function () {
    if (!current || viewMode !== 'lesson') return;
    editor.value = current.starter || '';
    paint();
    clearConsole(); emptyConsole();
    hideTests();
    toast('Código restaurado');
  };
  $('tabConsole').onclick = function () { showTab('console'); };
  $('tabPage').onclick = function () { showTab('page'); };
  $('search').addEventListener('input', renderNav);
  $('menuBtn').onclick = function () { document.body.classList.toggle('nav-open'); };
  $('scrim').onclick = function () { document.body.classList.remove('nav-open'); };
  $('resetBtn').onclick = function () {
    var btn = $('resetBtn');
    askConfirm(btn, '↺', function () {
      state = { done: {}, last: null, code: {} };
      save(); updateProgress(); render(flat[0].id);
      toast('Progresso apagado');
    });
  };

  // salva o código digitado (debounce)
  var saveTimer;
  editor.addEventListener('input', function () {
    if (!current) return;
    clearTimeout(saveTimer);
    saveTimer = setTimeout(function () {
      if (!current) return;
      state.code[current.id] = editor.value;
      save();
    }, 700);
  });

  document.addEventListener('keydown', function (ev) {
    if ((ev.ctrlKey || ev.metaKey) && ev.key === 'Enter') {
      if (document.activeElement !== editor) { ev.preventDefault(); ev.shiftKey ? doTest() : doRun(); }
    }
  });

  /* ---------------- boot ---------------- */
  var search = $('search');
  updateProgress();
  renderHome();
  $('brandBtn').onclick = renderHome;
  $('brandBtn').style.cursor = 'pointer';
  $('brandBtn').title = 'Ir para o início do curso';
  window.__app = { render: render, home: renderHome, flat: flat, state: state, buildHarnessSource: buildHarnessSource, sandboxDoc: function (body, rid) { return RUNNER.replace('{{BODY}}', body).replace('{{RID}}', String(rid)); } };
})();
