#!/usr/bin/env python3
"""Rebuild inspectable, self-contained SVG teaching figures and screenshot crops.
No generated figure is represented as an observed research result.
"""
from pathlib import Path
from html import escape
import json, hashlib, subprocess, re
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'presentacion/assets/visuals'; OUT.mkdir(parents=True,exist_ok=True)
SHOTS=ROOT/'presentacion/assets/screenshots'
NAVY='#15333D'; TEAL='#087F8C'; MAG='#BF2568'; GOLD='#BC741B'
MUTED='#52666E'; LINE='#C6D5D7'; PAPER='#F6F5F0'; PALE='#E9F4F3'; PINK='#F9EAF0'; WHITE='#FFFFFF'
FONT='Fira Sans, Arial, sans-serif'
fontpath=subprocess.check_output(['fc-match','Arial','--format=%{file}'],text=True).strip()
manifest=[]

def esc(s):return escape(str(s),quote=True)
class Figure:
    def __init__(self,name,title,desc,w=1120,h=430,kind='esquema didáctico'):
        self.name,self.title,self.desc,self.w,self.h,self.kind=name,title,desc,w,h,kind
        self.p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{esc(title)}</title><desc>{esc(desc)}</desc>']
    def rect(self,x,y,w,h,fill=WHITE,stroke='none',r=10,sw=2):
        self.p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>');return self
    def line(self,x1,y1,x2,y2,color=LINE,sw=2,dash=False):
        self.p.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"'+(' stroke-dasharray="7 6"' if dash else '')+'/>');return self
    def path(self,d,color=TEAL,sw=3,dash=False,fill='none'):
        self.p.append(f'<path d="{d}" stroke="{color}" stroke-width="{sw}" fill="{fill}"'+(' stroke-dasharray="7 6"' if dash else '')+'/>');return self
    def arrow(self,x1,y1,x2,y2,color=TEAL,sw=3):
        import math
        self.line(x1,y1,x2,y2,color,sw)
        a=math.atan2(y2-y1,x2-x1);n=10
        pts=[(x2,y2),(x2-n*math.cos(a-.5),y2-n*math.sin(a-.5)),(x2-n*math.cos(a+.5),y2-n*math.sin(a+.5))]
        self.p.append('<polygon points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'" fill="{color}"/>');return self
    def circle(self,x,y,r,fill=TEAL,stroke='none',sw=2):
        self.p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>');return self
    def text(self,x,y,text,size=26,color=NAVY,weight=400,anchor='start',width=None,line=1.3,mono=False):
        lines=str(text).split('\n')
        if width:
            font=ImageFont.truetype(fontpath,size)
            expanded=[]
            for raw in lines:
                words=raw.split(); acc=''
                for word in words:
                    trial=(acc+' '+word).strip()
                    if font.getlength(trial)>width and acc: expanded.append(acc);acc=word
                    else:acc=trial
                expanded.append(acc)
            lines=expanded
        family='monospace' if mono else FONT
        self.p.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">')
        for i,t in enumerate(lines):self.p.append(f'<tspan x="{x}" dy="{0 if i==0 else round(size*line,1)}">{esc(t)}</tspan>')
        self.p.append('</text>');return self
    def badge(self,x,y,s,color=MAG):
        self.circle(x,y,20,color);self.text(x,y+7,s,21,WHITE,700,'middle');return self
    def chip(self,x,y,w,label,color=TEAL,fill=PALE):
        self.rect(x,y,w,52,fill,color,9,1.5);self.text(x+w/2,y+34,label,25,color,600,'middle');return self
    def file(self,x,y,name,desc,w=285,color=TEAL):
        self.rect(x,y,w,102,WHITE,LINE,8,1.5);self.rect(x,y,7,102,color,r=0)
        self.text(x+22,y+36,name,25,color,600);self.text(x+22,y+72,desc,21,MUTED,width=w-40);return self
    def save(self):
        self.p.append('</svg>');p=OUT/(self.name+'.svg');p.write_text('\n'.join(self.p))
        manifest.append(dict(file=str(p.relative_to(ROOT)),kind=self.kind,title=self.title,description=self.desc,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
