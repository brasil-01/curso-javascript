const path=require('path');const {chromium}=require('/home/user/node_modules/playwright');
(async()=>{
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+path.join(__dirname,'..','index.html'));
 await p.waitForFunction(()=>window.__app);
 // ver solução em dois cliques
 await p.evaluate(()=>window.__app.render('m5l3'));
 const btn=p.locator('#solBtn');
 await btn.click(); const armado=await btn.textContent();
 await btn.click(); const val=await p.inputValue('#editor');
 console.log('solução: armado =',JSON.stringify(armado),'| carregou =',val.includes('carrinho'));
 // reset progresso em dois cliques
 console.log('progresso antes:',await p.textContent('#progressTxt'));
 await p.click('#resetBtn'); const cls=await p.getAttribute('#resetBtn','class');
 await p.click('#resetBtn');
 console.log('resetBtn armado:',cls.includes('armed'),'| progresso depois:',await p.textContent('#progressTxt'));
 // dica
 await p.evaluate(()=>window.__app.render('m2l4'));
 await p.click('#hintBtn2');
 console.log('dica visível:',await p.isVisible('#hintBox'));
 // screenshot final
 await p.evaluate(()=>{const l=window.__app.flat.find(x=>x.id==='m12l1');window.__app.render('m12l1');
   const ed=document.getElementById('editor');ed.value=l.solution;ed.dispatchEvent(new Event('input'));});
 await p.click('#testBtn'); await p.waitForTimeout(900);
 await p.screenshot({path:'final-desktop.png'});
 await p.setViewportSize({width:400,height:860}); await p.waitForTimeout(400);
 await p.screenshot({path:'final-mobile.png'});
 console.log('erros:',errs.length?errs:'nenhum');
 await b.close();
})();
