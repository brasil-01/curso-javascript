const path=require('path');const {chromium}=require('/home/user/node_modules/playwright');
(async()=>{
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
 await p.goto('file://'+path.join(__dirname,'..','index.html'));
 await p.waitForFunction(()=>window.__app);
 // 1) lição de DOM, solução rodando, aba Página
 await p.evaluate(()=>{const l=window.__app.flat.find(x=>x.id==='m9l5');
   window.__app.render('m9l5');const ed=document.getElementById('editor');ed.value=l.solution;ed.dispatchEvent(new Event('input'));});
 await p.click('#testBtn'); await p.waitForTimeout(1200);
 await p.screenshot({path:'shot-dom.png'});
 // 2) teste falhando
 await p.evaluate(()=>{window.__app.render('m2l3');const ed=document.getElementById('editor');
   ed.value='const temperatura = 28;\nlet clima = "quente";\nconsole.log(clima);';ed.dispatchEvent(new Event('input'));});
 await p.click('#testBtn'); await p.waitForTimeout(1200);
 await p.screenshot({path:'shot-fail.png'});
 // 3) erro de código
 await p.evaluate(()=>{window.__app.render('m4l1');const ed=document.getElementById('editor');
   ed.value='const cores = ["a","b",\nconsole.log(cores)';ed.dispatchEvent(new Event('input'));});
 await p.click('#testBtn'); await p.waitForTimeout(1200);
 await p.screenshot({path:'shot-error.png'});
 await b.close();
})();
