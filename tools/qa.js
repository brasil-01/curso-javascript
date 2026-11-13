const path=require('path');const {chromium}=require('/home/user/node_modules/playwright');
const file='file://'+path.join(__dirname,'..','index.html');
(async()=>{
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1440,height:900}});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto(file);await p.waitForFunction(()=>window.__app);

 // 1) persistência: conclui uma lição, recarrega
 await p.evaluate(()=>{const l=window.__app.flat[0];window.__app.render(l.id);
   const ed=document.getElementById('editor');ed.value=l.solution;ed.dispatchEvent(new Event('input'));});
 await p.click('#testBtn');
 await p.waitForFunction(()=>document.getElementById('doneBanner').classList.contains('show'));
 const prog1=await p.textContent('#progressTxt');
 await p.reload();await p.waitForFunction(()=>window.__app);
 const prog2=await p.textContent('#progressTxt');
 console.log('progresso antes/depois do reload:',prog1,prog2, prog1===prog2?'OK':'FALHOU');

 // 2) editor: auto-indentação e tab
 await p.evaluate(()=>{window.__app.render('m1l1');const ed=document.getElementById('editor');ed.value='';ed.dispatchEvent(new Event('input'));});
 await p.click('#editor');
 await p.keyboard.type('function f() {');
 await p.keyboard.press('Enter');
 await p.keyboard.type('return 1;');
 await p.keyboard.press('Enter');
 await p.keyboard.type('}');
 const val=await p.inputValue('#editor');
 console.log('auto-indent:',JSON.stringify(val));

 // 3) atalho Ctrl+Enter executa
 await p.evaluate(()=>{const ed=document.getElementById('editor');ed.value='console.log("atalho ok");';ed.dispatchEvent(new Event('input'));});
 await p.click('#editor');await p.keyboard.press('Control+Enter');
 await p.waitForFunction(()=>document.getElementById('console').textContent.includes('atalho ok'),{timeout:5000});
 console.log('Ctrl+Enter: OK');

 // 4) busca filtra a navegação
 await p.fill('#search','fizzbuzz');
 await p.waitForTimeout(200);
 const n=await p.evaluate(()=>document.querySelectorAll('.lnk').length);
 console.log('busca "fizzbuzz" -> itens:',n);

 // 5) lição de DOM mostra aba Página; lição normal esconde
 await p.evaluate(()=>window.__app.render('m9l4'));
 const visDom=await p.isVisible('#tabPage');
 await p.evaluate(()=>window.__app.render('m3l2'));
 const visNormal=await p.isVisible('#tabPage');
 console.log('aba Página (DOM / comum):',visDom,visNormal);

 // 6) loop infinito -> timeout
 await p.evaluate(()=>{const ed=document.getElementById('editor');ed.value='while(true){}';ed.dispatchEvent(new Event('input'));});
 await p.click('#testBtn');
 await p.waitForFunction(()=>document.getElementById('console').textContent.includes('Tempo esgotado'),{timeout:12000});
 console.log('proteção de loop infinito: OK');

 // 7) mobile
 await p.setViewportSize({width:400,height:850});
 await p.evaluate(()=>window.__app.render('m4l4'));
 await p.waitForTimeout(300);
 
 console.log('erros de página:',errs.length?errs:'nenhum');
 await b.close();
})();
