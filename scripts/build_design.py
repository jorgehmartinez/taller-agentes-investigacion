#!/usr/bin/env python3
"""Create the content-free native Bento workshop design. Does not apply it."""
from pathlib import Path
import json,copy
root=Path(__file__).resolve().parents[1]
old=json.loads((root/'design/spp-classroom.design.json').read_text())
N='#15333D';T='#087F8C';M='#BF2568';P='#F6F5F0';W='#FFFFFF';G='#52666E'
F=lambda x,y,w,h:dict(x=x,y=y,w=w,h=h)
def slot(x,y,w,h,style=None):
 d={'frame':F(x,y,w,h)}
 if style:d['style']=style
 return d
styles=copy.deepcopy(old['registry']['themes']['spp-classroom']['namedStyles'])
for name,props in {
 'kicker':dict(fontSize=17,color=T,fontWeight=600),
 'caption':dict(fontSize=17,color=G,lineHeight=1.15),
 'takeaway':dict(fontSize=25,color=N,lineHeight=1.22,fontWeight=500),
 'aside':dict(fontSize=25,color=N,lineHeight=1.25),
 'question-large':dict(fontSize=48,color=W,lineHeight=1.17,fontWeight=600),
 'light-body':dict(fontSize=28,color='#D4E6E8',lineHeight=1.3),
 'light-small':dict(fontSize=19,color='#9EDADE',lineHeight=1.2),
 'section-number':dict(fontSize=112,color='#E45691',fontWeight=600),
 'label':dict(fontSize=21,color=T,fontWeight=600),
 'summary':dict(fontSize=32,color=N,lineHeight=1.22,fontWeight=500),
 'references':dict(fontSize=22,color=G,lineHeight=1.25)
}.items():styles[name]={'target':'text','properties':props}
base={'titleFrame':F(64,56,1152,70),'contentFrame':F(64,154,1152,435),
 'decorations':[dict(id='top-mark',x=64,y=41,w=72,h=5,fill=M,radius=0),dict(id='footer-rule',x=64,y=665,w=1152,h=1,fill='#C6D5D7',radius=0)],
 'slots':{
 'kicker':slot(64,10,1152,26,'kicker'),
 'visual':slot(64,155,1152,442),
 'takeaway':slot(64,604,1152,54,'takeaway'),
 'citation':slot(64,679,1152,24,'caption')}}
variants={'visual':copy.deepcopy(base),'content':copy.deepcopy(base)}
s=copy.deepcopy(base)
s['slots'].update({'visual':slot(64,162,780,429),'side1':slot(876,174,340,116,'aside'),'side2':slot(876,315,340,116,'aside'),'side3':slot(876,456,340,116,'aside')})
variants['screenshot']=s
s=copy.deepcopy(base)
s['slots'].update({'left-label':slot(64,142,550,38,'label'),'right-label':slot(666,142,550,38,'label'),
 'left':slot(64,195,550,374),'right':slot(666,195,550,374)})
s['decorations']+= [dict(id='left-panel',x=48,y=181,w=582,h=400,fill=W,radius=12),dict(id='right-panel',x=650,y=181,w=582,h=400,fill='#E9F4F3',radius=12)]
variants['comparison']=s
s=copy.deepcopy(base)
s['slots']['visual']=slot(64,149,1152,475);s['slots']['takeaway']=slot(64,628,1152,32,'caption')
variants['wide']=s
variants['hero']={
 'background':N,'title':dict(fontSize=52,fontWeight=600,color=W,lineHeight=1.12),
 'titleFrame':F(64,142,725,275),'contentFrame':F(64,465,720,130),
 'decorations':[dict(id='hero-line',x=64,y=107,w=100,h=7,fill=M,radius=1),dict(id='hero-footer',x=64,y=609,w=1152,h=1,fill='#3D606A',radius=0)],
 'slots':{'kicker':slot(64,59,1120,35,'light-small'),'visual':slot(824,150,370,365),
 'subtitle':slot(64,460,710,115,'light-body'),'citation':slot(64,637,1152,38,'light-small')}}
variants['section']={
 'background':N,'title':dict(fontSize=59,fontWeight=600,color=W,lineHeight=1.15),
 'titleFrame':F(266,174,950,195),'contentFrame':F(266,410,900,150),
 'decorations':[dict(id='section-accent',x=64,y=110,w=1152,h=4,fill=M,radius=0)],
 'slots':{'kicker':slot(64,57,1120,35,'light-small'),'number':slot(64,187,170,170,'section-number'),
 'subtitle':slot(266,410,900,140,'light-body'),'citation':slot(64,655,1152,32,'light-small')}}
variants['question']={
 'background':N,'title':dict(fontSize=38,fontWeight=600,color='#C7E0E3'),
 'titleFrame':F(64,72,1152,76),'contentFrame':F(64,205,1120,245),
 'decorations':[dict(id='question-accent',x=64,y=176,w=86,h=6,fill=M,radius=0)],
 'slots':{'kicker':slot(64,19,1152,30,'light-small'),'question':slot(64,219,1120,215,'question-large'),
 'prompt':slot(64,481,1120,109,'light-body'),'citation':slot(64,663,1152,32,'light-small')}}
s=copy.deepcopy(base)
s['slots'].update({'left':slot(64,165,547,425,'references'),'right':slot(668,165,547,425,'references')})
variants['references']=s
s=copy.deepcopy(base)
s['slots'].update({'first':slot(64,165,1152,78,'summary'),'second':slot(64,277,1152,78,'summary'),'third':slot(64,389,1152,78,'summary'),'fourth':slot(64,501,1152,78,'summary')})
variants['summary']=s
pkg={'format':'qbento/design','version':1,'name':'SPP · Taller visual con agentes · v2','registry':copy.deepcopy(old['registry'])}
pkg['registry']['themes']['spp-workshop-v2']={
 'background':P,'color':N,'accent':M,'fontFamily':'Fira Sans, Arial, sans-serif',
 'styles':{'title':dict(fontSize=40,fontWeight=600,color=N,lineHeight=1.15),
 'heading':dict(fontSize=29,fontWeight=600,color=N),'body':dict(fontSize=26,lineHeight=1.25,color=N),
 'code':dict(fontSize=23,fontFamily='monospace',color=N,lineHeight=1.25),
 'card':dict(fill=W,stroke='#C6D5D7',strokeWidth=1,radius=10)},
 'namedStyles':styles,'variants':variants,'defaultVariant':'visual'}
pkg['registry']['activeTheme']='spp-workshop-v2'
(root/'design/spp-workshop-v2.design.json').write_text(json.dumps(pkg,indent=2,ensure_ascii=False)+'\n')
print('Native variants:',', '.join(variants))
