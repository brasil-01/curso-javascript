const path=require('path');const {chromium}=require('/home/user/node_modules/playwright');
(async()=>{
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:950}});
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+path.join(__dirname,'..','index.html'));
 await p.waitForFunction(()=>window.__app);

 console.log('boot -> cards:',await p.locator('.card').count(),'| editor visível:',await p.isVisible('#editor'));
 console.log('chips:',await p.locator('.chip').allTextContents());
 await p.screenshot({path:'home-grade.png'});

 // filtro: pendentes (nada concluído ainda) e depois concluídas
 await p.click('.chip[data-filter="pending"]');
 console.log('pendentes -> cards:',await p.locator('.card').count());
 // conclui uma lição
 await p.evaluate(()=>{const l=window.__app.flat[2];window.__app.render(l.id);const ed=document.getElementById('editor');ed.value=l.solution;ed.dispatchEvent(new Event('input'));});
 await p.click('#testBtn');
 await p.waitForFunction(()=>document.getElementById('doneBanner').classList.contains('show'),{timeout:15000});
 await p.click('#brandBtn');
 console.log('filtro mantido (pendentes) -> cards:',await p.locator('.card').count());
 await p.click('.chip[data-filter="done"]');
 console.log('concluídas -> cards:',await p.locator('.card').count());
 await p.click('.chip[data-filter="dom"]');
 console.log('com DOM -> cards:',await p.locator('.card').count());
 // busca vazia -> estado vazio
 await p.click('.chip[data-filter="all"]');

 // visão trilha
 await p.click('.vs[data-view="trail"]');
 await p.waitForSelector('.node-row');
 const nodes=await p.locator('.node-row').count();
 const nextNode=await p.locator('.node-row.next').count();
 const doneNode=await p.locator('.node-row.done').count();
 console.log('trilha -> nós:',nodes,'| marcado como próximo:',nextNode,'| concluídos:',doneNode);
 await p.screenshot({path:'home-trilha.png'});
 // clicar num nó abre a lição
 await p.locator('.node-row').nth(6).click();
 console.log('nó abriu:',JSON.stringify(await p.textContent('#lessonPane h1')));
 // voltar: preferência de visão persistiu
 await p.click('#brandBtn');
 console.log('volta em trilha:',await p.isVisible('.node-row'));
 // botão "próxima pendente" do módulo 2
 await p.click('.vs[data-view="grid"]');
 const modNext=p.locator('.mod-sec').nth(1).locator('.mod-next');
 const label=await modNext.textContent();
 await modNext.click();
 console.log('mod-next:',JSON.stringify(label),'->',JSON.stringify(await p.textContent('#lessonPane h1')));
 // recarregar mantém preferências
 await p.click('#brandBtn'); await p.reload(); await p.waitForFunction(()=>window.__app);
 console.log('após reload -> visão grade:',await p.isVisible('.card'),'| chips ok:',await p.locator('.chip').count()===4);
 // mobile
 await p.setViewportSize({width:400,height:860});
 await p.click('.vs[data-view="trail"]'); await p.waitForTimeout(300);
 await p.screenshot({path:'home-trilha-mobile.png'});
 console.log('erros:',errs.length?errs:'nenhum');
 await b.close();
})();
