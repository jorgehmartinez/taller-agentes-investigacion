#!/usr/bin/env node
/** Actual Bento presentation capture via Chromium/CDP; no DOM/content rewrites. */
import {spawn} from 'node:child_process';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const OUT=path.join(ROOT,'output/qa/slides');await fs.mkdir(OUT,{recursive:true});
const profile=await fs.mkdtemp(path.join(ROOT,'output/qa/chromium-'));
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const browser=spawn('/usr/bin/chromium',['--headless=new','--remote-debugging-port=0','--remote-debugging-address=127.0.0.1',`--user-data-dir=${profile}`,'--window-size=1280,720','--no-first-run','--no-default-browser-check','about:blank'],{stdio:['ignore','ignore','pipe']});
let log='';browser.stderr.on('data',c=>log+=c.toString());
let ws,sessionId;const pending=new Map();let serial=0;
function send(method,params={},session=sessionId){
 return new Promise((resolve,reject)=>{
   const id=++serial; const timer=setTimeout(()=>{pending.delete(id);reject(new Error('CDP timeout '+method));},25000);
   pending.set(id,{resolve:v=>{clearTimeout(timer);resolve(v)},reject:e=>{clearTimeout(timer);reject(e)}});
   ws.send(JSON.stringify({id,method,params,...(session?{sessionId:session}:{})}));
 });
}
async function evaluate(expression){
 const r=await send('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true,userGesture:true});
 if(r.exceptionDetails)throw new Error(JSON.stringify(r.exceptionDetails));return r.result.value;
}
try{
 let portInfo;
 for(let i=0;i<100;i++){try{portInfo=(await fs.readFile(path.join(profile,'DevToolsActivePort'),'utf8')).trim().split('\n');break}catch{await sleep(100)}}
 if(!portInfo)throw new Error('Chromium did not initialize: '+log.slice(-1800));
 ws=new WebSocket(`ws://127.0.0.1:${portInfo[0]}${portInfo[1]}`);
 await new Promise((res,rej)=>{ws.addEventListener('open',res,{once:true});ws.addEventListener('error',rej,{once:true})});
 ws.addEventListener('message',ev=>{const m=JSON.parse(ev.data);if(m.id&&pending.has(m.id)){const p=pending.get(m.id);pending.delete(m.id);m.error?p.reject(new Error(JSON.stringify(m.error))):p.resolve(m.result)}});
 const target=await send('Target.createTarget',{url:'about:blank'},null);
 sessionId=(await send('Target.attachToTarget',{targetId:target.targetId,flatten:true},null)).sessionId;
 await send('Page.enable');await send('Runtime.enable');
 await send('Emulation.setDeviceMetricsOverride',{width:1280,height:720,deviceScaleFactor:1,mobile:false,screenWidth:1280,screenHeight:720});
 await send('Page.navigate',{url:pathToFileURL(path.join(ROOT,'presentacion/deck.bento.html')).href});
 for(let i=0;i<100;i++){
   const ready=await evaluate(`Boolean([...document.querySelectorAll('button')].find(b=>b.textContent?.trim()==='Presentar en esta pestaña'))`);
   if(ready)break;if(i===99)throw new Error('Presentation control not found');await sleep(100);
 }
 await evaluate('document.fonts.ready.then(()=>true)');
 const info=await evaluate(`({title:document.title, scripts:[...document.querySelectorAll('script[type="application/json"]')].map(e=>({id:e.id,size:e.textContent.length}))})`);
 await evaluate(`(()=>{const b=[...document.querySelectorAll('button')].find(b=>b.textContent?.trim()==='Presentar en esta pestaña');b.click();return true})()`);
 await sleep(800);
 const doc=JSON.parse(await fs.readFile(path.join(ROOT,'output/qa/native-v2.json'),'utf8'));
 const records=[];
 for(let i=0;i<doc.deck.slides.length;i++){
  await sleep(450);
  const state=await evaluate(`({bodyTail:document.body.innerText.slice(-180),url:location.href,images:[...document.images].filter(x=>x.getBoundingClientRect().width>30).map(x=>({loaded:x.complete&&x.naturalWidth>0,w:Math.round(x.getBoundingClientRect().width),h:Math.round(x.getBoundingClientRect().height)}))})`);
  const image=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
  const file=String(i+1).padStart(2,'0')+'-'+doc.deck.slides[i].id+'.png';await fs.writeFile(path.join(OUT,file),Buffer.from(image.data,'base64'));
  records.push({number:i+1,id:doc.deck.slides[i].id,file,state});
  if((i+1)%10===0)console.log(`Captured ${i+1}/${doc.deck.slides.length}`);
  await send('Input.dispatchKeyEvent',{type:'keyDown',key:'ArrowRight',code:'ArrowRight',windowsVirtualKeyCode:39,nativeVirtualKeyCode:39});
  await send('Input.dispatchKeyEvent',{type:'keyUp',key:'ArrowRight',code:'ArrowRight',windowsVirtualKeyCode:39,nativeVirtualKeyCode:39});
 }
 // Keyboard return and exit are exercised, not inferred from markup.
 await send('Input.dispatchKeyEvent',{type:'keyDown',key:'ArrowLeft',code:'ArrowLeft',windowsVirtualKeyCode:37});
 await send('Input.dispatchKeyEvent',{type:'keyUp',key:'ArrowLeft',code:'ArrowLeft',windowsVirtualKeyCode:37});
 await sleep(300);const afterLeft=await evaluate('document.body.innerText.slice(-100)');
 await send('Input.dispatchKeyEvent',{type:'keyDown',key:'Escape',code:'Escape',windowsVirtualKeyCode:27});
 await send('Input.dispatchKeyEvent',{type:'keyUp',key:'Escape',code:'Escape',windowsVirtualKeyCode:27});
 const afterEscape=await evaluate('document.body.innerText.slice(-180)');
 await fs.writeFile(path.join(ROOT,'output/qa/browser-check.json'),JSON.stringify({captured:new Date().toISOString(),viewport:[1280,720],docId:doc.docId,revision:doc.revision,info,records,afterLeft,afterEscape},null,2));
 console.log(JSON.stringify({slides:records.length,directory:OUT,docId:doc.docId}));
}finally{
 if(ws)ws.close();browser.kill('SIGTERM');await fs.writeFile(path.join(ROOT,'output/qa/chromium.log'),log);
}
