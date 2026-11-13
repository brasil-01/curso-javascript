/* Teste end-to-end no Chromium real: abre o app, roda a solução de cada lição
   pelo botão "Testar" e confere se todos os testes passam.
   Uso: node tools/e2e.js [filtro] [--shot] */
const path = require('path');
const { chromium } = require('/home/user/node_modules/playwright');

const file = 'file://' + path.join(__dirname, '..', 'index.html');
const filter = process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : '';
const shot = process.argv.includes('--shot');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  const errors = [];
  page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
  page.on('console', (m) => { if (m.type() === 'error') errors.push('console.error: ' + m.text()); });

  await page.goto(file);
  await page.waitForFunction(() => window.__app && window.__app.flat.length > 0);
  const lessons = await page.evaluate(() => window.__app.flat.map((l) => ({ id: l.id, title: l.title })));
  const target = lessons.filter((l) => !filter || l.id.includes(filter));

  let fails = 0;
  const problems = [];

  for (const lesson of target) {
    await page.evaluate((id) => {
      window.__app.render(id);
      const l = window.__app.flat.find((x) => x.id === id);
      const ed = document.getElementById('editor');
      ed.value = l.solution;
      ed.dispatchEvent(new Event('input'));
    }, lesson.id);

    await page.click('#testBtn');

    let res = null;
    try {
      await page.waitForFunction(() => {
        const box = document.getElementById('tests');
        return box && box.classList.contains('show') && box.querySelectorAll('li').length > 0;
      }, { timeout: 9000 });
      res = await page.evaluate(() => Array.from(document.querySelectorAll('#tests li')).map((li) => ({
        ok: li.classList.contains('pass'),
        msg: li.querySelector('.msg') ? li.querySelector('.msg').childNodes[0].textContent : '',
        why: li.querySelector('.why') ? li.querySelector('.why').textContent : '',
      })));
    } catch (e) {
      fails++;
      problems.push(`${lesson.id} — ${lesson.title}\n   ✕ sem resultado (timeout)`);
      continue;
    }

    const bad = res.filter((r) => !r.ok);
    if (bad.length) {
      fails++;
      problems.push(`${lesson.id} — ${lesson.title}\n` + bad.map((b) => `   ✕ ${b.msg} ${b.why}`).join('\n'));
    } else {
      process.stdout.write('.');
    }
  }

  // checagens de interface
  const uiOk = await page.evaluate(() => ({
    nav: document.querySelectorAll('.lnk').length > 0,
    highlighted: document.getElementById('hl').innerHTML.includes('span'),
    progress: document.getElementById('progressTxt').textContent,
    editorVisible: !!document.getElementById('editor').offsetHeight,
  }));

  if (shot) {
    await page.evaluate(() => {
      window.__app.render(window.__app.flat[0].id);
      const ed = document.getElementById('editor');
      ed.value = 'const nome = "Ana";\nlet idade = 25;\n\nconsole.log(`Olá, ${nome}! Você tem ${idade} anos.`);\n';
      ed.dispatchEvent(new Event('input'));
      ed.dispatchEvent(new Event('scroll'));
    });
    await page.click('#runBtn');
    await page.waitForTimeout(900);
    await page.screenshot({ path: path.join(__dirname, '..', 'preview-desktop.png') });
    await page.setViewportSize({ width: 420, height: 860 });
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(__dirname, '..', 'preview-mobile.png'), fullPage: false });
  }

  console.log('\n');
  if (problems.length) console.log(problems.join('\n') + '\n');
  console.log('UI:', JSON.stringify(uiOk));
  if (errors.length) console.log('ERROS DE PÁGINA:\n' + errors.slice(0, 15).join('\n'));
  console.log(`e2e: ${target.length - fails}/${target.length} lições passaram`);
  await browser.close();
  process.exit(fails || errors.length ? 1 : 0);
})();
