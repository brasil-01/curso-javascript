#!/usr/bin/env python3
"""Monta o index.html final (arquivo único, sem dependências externas)."""
import json, os, re, sys, importlib.util, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
CONTENT = os.path.join(ROOT, "content")


def load_modules():
    mods = []
    for path in sorted(glob.glob(os.path.join(CONTENT, "mod_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        found = getattr(m, "MODULES", None) or [m.MODULE]
        mods.extend(found)
    return mods


def collect():
    mods = load_modules()
    seen = set()
    for mod in mods:
        for l in mod["lessons"]:
            assert l["id"] not in seen, "id duplicado: " + l["id"]
            seen.add(l["id"])
            for key in ("id", "title", "theory", "starter", "solution", "tests"):
                assert key in l, "lição %s sem campo %s" % (l["id"], key)
            for t in l["tests"]:
                assert t.get("msg") and t.get("code"), "teste incompleto em " + l["id"]
    return mods


SHELL = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Curso de JavaScript — do zero ao avançado</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23f7df1e'/%3E%3Ctext x='16' y='23' font-family='monospace' font-size='15' font-weight='bold' text-anchor='middle' fill='%230b0f14'%3EJS%3C/text%3E%3C/svg%3E">
<meta name="description" content="Curso interativo de JavaScript em português, com editor de código e testes automáticos.">
<style>
__CSS__
</style>
</head>
<body>
<div class="app">
  <header class="topbar">
    <button class="icon-btn menu-btn" id="menuBtn" title="Menu" aria-label="Abrir menu">☰</button>
    <div class="brand" id="brandBtn" role="button" tabindex="0">
      <span class="logo">JS</span>
      <span class="ttl">Curso de JavaScript<small>interativo · em português</small></span>
    </div>
    <div class="spacer"></div>
    <div class="progress-mini">
      <div class="track"><div class="fill" id="progressFill"></div></div>
      <span id="progressTxt">0/0</span>
    </div>
    <button class="icon-btn" id="resetBtn" title="Apagar progresso" aria-label="Apagar progresso">↺</button>
  </header>

  <aside class="sidebar" id="sidebar">
    <div class="side-head">
      <input class="search" id="search" type="search" placeholder="Buscar lição..." autocomplete="off">
    </div>
    <nav class="nav" id="nav"></nav>
  </aside>
  <div class="scrim" id="scrim"></div>

  <main class="main">
    <section class="pane lesson-pane" id="lessonPane"></section>

    <section class="work">
      <div class="editor-shell">
        <div class="ehead">
          <span class="filename"><span class="dirty" id="dirty"></span><span id="fileName">index.js</span></span>
          <span class="spacer"></span>
          <button class="btn small ghost" id="resetCodeBtn" title="Restaurar o código inicial">↺ Restaurar</button>
          <button class="btn small" id="runBtn" title="Ctrl+Enter">▶ Executar</button>
          <button class="btn small gold" id="testBtn" title="Ctrl+Shift+Enter">✓ Testar</button>
        </div>
        <div class="editor-wrap">
          <div class="gutter" id="gutter">1</div>
          <div class="code-area">
            <pre class="hl" aria-hidden="true"><code id="hl"></code></pre>
            <textarea class="editor" id="editor" spellcheck="false" autocapitalize="off" autocomplete="off" autocorrect="off" wrap="off" aria-label="Editor de código"></textarea>
          </div>
        </div>
      </div>

      <div class="out-shell">
        <div class="tabs">
          <button class="tab active" id="tabConsole">Console</button>
          <button class="tab" id="tabPage">Página</button>
          <span class="spacer"></span>
          <span style="font-size:11px;color:var(--mut);padding-right:8px" id="testCount"></span>
          <span class="badge-dot live" title="Sandbox pronta"></span>
        </div>
        <div class="console" id="console"></div>
        <div class="iframe-wrap" id="iframeWrap">
          <iframe id="sandbox" sandbox="allow-scripts" title="Resultado do código"></iframe>
        </div>
      </div>
    </section>
  </main>
</div>
<div class="toast" id="toast"></div>

<script>
window.COURSE = __COURSE__;
</script>
<script>
__APP__
</script>
</body>
</html>
"""


def main():
    mods = collect()
    css = open(os.path.join(SRC, "styles.css"), encoding="utf-8").read()
    app = open(os.path.join(SRC, "app.js"), encoding="utf-8").read()
    course_json = json.dumps(mods, ensure_ascii=False, indent=None, separators=(",", ":"))
    course_json = course_json.replace("</script", "<\\/script")

    html = (SHELL
            .replace("__CSS__", css)
            .replace("__COURSE__", course_json)
            .replace("__APP__", app))

    out = os.path.join(ROOT, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

    n_lessons = sum(len(m["lessons"]) for m in mods)
    n_tests = sum(len(l["tests"]) for m in mods for l in m["lessons"])
    print("index.html gerado: %.1f KB" % (len(html.encode()) / 1024))
    print("%d módulos · %d lições · %d testes" % (len(mods), n_lessons, n_tests))

    # cópia do JSON para as ferramentas de validação
    with open(os.path.join(ROOT, "tools", "course.json"), "w", encoding="utf-8") as f:
        json.dump(mods, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
