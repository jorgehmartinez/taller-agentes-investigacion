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

# Opening: a worked microexample, repeated with a single controlled change.
for state in ['pregunta','ejecucion','correccion']:
    f=Figure('micro-'+state,'Cinco respuestas y una decisión','Cinco respuestas ficticias. El código 99 se trata como valor o como perdido según el diccionario.',kind='microejemplo ficticio; medias ejecutadas en R')
    for i,v in enumerate(['1','2','3','4','99']):
        x=80+i*126;special=i==4
        f.rect(x,52,102,100,PINK if special else PALE,MAG if special else TEAL,14)
        f.text(x+51,118,'NA' if state=='correccion' and special else v,44,MAG if special else TEAL,700,'middle')
    f.text(82,27,'RESPUESTAS FICTICIAS · UN ÍTEM',19,MUTED,600)
    f.arrow(730,103,800,103)
    if state=='pregunta':
        f.text(918,120,'?',66,MAG,600,'middle');f.text(918,172,'¿Qué revisarías?',24,NAVY,600,'middle')
        f.rect(80,230,950,112,NAVY,r=12);f.text(110,275,'mean(respuestas)',31,WHITE,mono=True)
        f.text(110,314,'Antes de aceptar una respuesta, mira los datos.',23,'#BDD9DD')
    else:
        result='21.8' if state=='ejecucion' else '2.5'
        f.text(918,126,result,62,MAG if state=='ejecucion' else TEAL,700,'middle')
        f.text(918,174,'media calculada en R',20,MUTED,400,'middle')
        if state=='ejecucion':
            f.rect(80,230,950,115,PINK,r=12);f.text(110,272,'El código terminó. El significado está mal.',31,MAG,600)
            f.text(110,315,'R no sabe que 99 representa una respuesta perdida.',24,NAVY)
        else:
            f.rect(80,230,950,115,PALE,r=12);f.text(110,272,'El diccionario cambia el cálculo.',31,TEAL,600)
            f.text(110,315,'4 respuestas válidas · 1 perdido · misma entrada original',24,NAVY)
    f.save()

f=Figure('ruta','Mapa de aprendizaje','Tres etapas del taller con un caso conductor y controles humanos.')
for i,(a,b,c) in enumerate([('01','COMPRENDER','Modelo, agente y R'),('02','DIRIGIR','Contexto e instrucciones'),('03','VERIFICAR','Datos, método y evidencia')]):
    x=40+i*365;f.text(x,98,a,72,TEAL if i!=1 else MAG,600);f.text(x,150,b,26,NAVY,600);f.text(x,197,c,23,MUTED,width=320)
    if i<2:f.arrow(x+270,98,x+330,98,LINE,3)
f.line(40,275,1070,275,LINE,3);f.circle(80,275,9,MAG);f.circle(560,275,9,MAG);f.circle(1030,275,9,MAG)
f.text(560,331,'Un mismo caso · decisiones visibles · resultados comprobables',27,NAVY,500,'middle');f.save()

f=Figure('generacion','Generación condicionada por el contexto','Esquema de continuaciones posibles del modelo. No representa probabilidades medidas.')
f.rect(15,120,330,155,NAVY,r=14);f.text(42,160,'CONTEXTO',20,'#87CDD0',600);f.text(42,204,'«Describe estos ítems»',28,WHITE,500,width=275)
for i,(code,note) in enumerate([('table(respuestas)','Contar categorías'),('summary(respuestas)','Resumir valores'),('mean(respuestas)','Calcular una media')]):
    y=12+i*130;f.arrow(355,198,560,y+51,MAG if i==2 else TEAL);f.rect(575,y,520,105,PINK if i==2 else PALE,r=10)
    f.text(600,y+40,code,26,NAVY,500,mono=True);f.text(600,y+78,note,22,MUTED)
f.text(20,386,'Opciones ilustrativas; la configuración y la decodificación afectan la variabilidad.',22,MUTED);f.save()

f=Figure('chatbot-vs-agente','Dos formas de llegar a R','Contraste controlado: misma tarea y mismo R; cambia quién opera las herramientas.')
f.text(12,34,'CHATBOT',23,MAG,600);f.text(605,34,'AGENTE CON HERRAMIENTAS',23,TEAL,600)
f.line(550,30,550,390,LINE,2)
for xbase,mode in [(10,0),(603,1)]:
    names=['Solicitud','Código sugerido','Pegar resultado','Copiar / ejecutar'] if mode==0 else ['Objetivo','Propuesta','Inspección','Ejecución en R']
    for i,name in enumerate(names):
        x=xbase+(i%2)*260;y=90+(i//2)*168
        f.rect(x,y,225,76,PALE if mode else PINK,r=10);f.text(x+112,y+46,name,23,NAVY,500,'middle')
    f.arrow(xbase+225,128,xbase+260,128)
    f.arrow(xbase+373,166,xbase+373,258)
    f.arrow(xbase+260,296,xbase+225,296)
    f.path(f'M {xbase+112} 258 L {xbase+112} 208 L {xbase+112} 166',MAG if mode==0 else TEAL,3)
f.text(10,410,'La persona opera cada intercambio.',23,MAG);f.text(603,410,'La persona fija y revisa las decisiones.',23,TEAL);f.save()

f=Figure('modelo-r-investigador','Separación de responsabilidades','El modelo propone, R ejecuta y el investigador evalúa; las revisiones retornan al procedimiento.')
for x,label,sub,color in [(15,'MODELO','Propuesta y código',MAG),(403,'R','Ejecución y salidas',TEAL),(790,'INVESTIGADOR','Criterio y decisión',NAVY)]:
    f.circle(x+147,136,70,PALE if color!=MAG else PINK)
    f.text(x+147,147,label,25,color,600,'middle');f.text(x+147,250,sub,24,NAVY,500,'middle')
f.arrow(247,136,394,136,MAG);f.arrow(635,136,782,136,TEAL)
f.path('M 937 283 L 937 345 L 163 345 L 163 285',MUTED,3);f.text(550,387,'La revisión puede cambiar el procedimiento, no solo la redacción.',24,MUTED,400,'middle');f.save()

f=Figure('anatomia','Componentes de un agente','Modelo en el centro, herramientas conectadas y un perímetro de contexto y permisos.')
f.rect(20,25,1080,370,WHITE,LINE,20,2);f.text(52,70,'CONTEXTO + PERMISOS + OBJETIVO',24,MAG,600)
f.circle(550,220,87,NAVY);f.text(550,214,'MODELO',29,WHITE,600,'middle');f.text(550,250,'genera acciones',21,'#BCD9DC',400,'middle')
for x,y,label in [(150,155,'Archivos'),(150,290,'Documentación'),(920,155,'R / terminal'),(920,290,'Gráficos')]:
    f.rect(x-115,y-35,230,70,PALE,r=10);f.text(x,y+9,label,24,TEAL,500,'middle')
    if x<550:f.arrow(x+115,y,460,205 if y<220 else 245)
    else:f.arrow(640,205 if y<220 else 245,x-115,y)
f.save()

f=Figure('verificaciones','Tres controles, no una garantía automática','Comprobar ejecución, pertinencia del método y alcance científico son tareas diferentes.')
for i,(name,q,color) in enumerate([('CÓMPUTO','¿Produce esta salida?',TEAL),('MÉTODO','¿Es el análisis pertinente?',MAG),('INFERENCIA','¿Qué podemos concluir?',NAVY)]):
    x=35+i*365;f.circle(x+38,97,37,color);f.text(x+38,108,str(i+1),33,WHITE,700,'middle');f.text(x,183,name,25,color,700);f.text(x,231,q,26,NAVY,width=315)
    if i<2:f.arrow(x+120,97,x+318,97,LINE)
    f.line(x,300,x+305,300,LINE);f.text(x,342,['Reejecutar','Revisar decisiones','Acotar afirmaciones'][i],23,MUTED)
f.save()

f=Figure('capas','Modelo, agente, editor y motor','Cuatro capas distintas; un protocolo conecta herramientas, no sustituye a R.')
rows=[('MODELO','GPT · Claude · Gemini','Generación',MAG),('AGENTE','Codex · Claude Code · Gemini CLI','Operación',TEAL),('ENTORNO','Positron · RStudio','Proyecto y sesión',NAVY),('MOTOR','R + paquetes','Cálculos',TEAL)]
for i,(a,b,c,col) in enumerate(rows):
    y=8+i*100;f.rect(10,y,210,76,col,r=8);f.text(32,y+48,a,25,WHITE,600);f.rect(240,y,585,76,WHITE,LINE,8,1)
    f.text(266,y+47,b,26,NAVY,500);f.text(850,y+47,c,23,MUTED)
    if i<3:f.arrow(112,y+78,112,y+98,LINE,2)
f.save()

f=Figure('mcp','MCP y una sesión persistente','Ruta de llamadas desde un agente hasta la sesión R de Positron y retorno de resultados.')
f.rect(15,115,250,155,NAVY,r=12);f.text(140,160,'AGENTE',25,WHITE,600,'middle');f.text(140,205,'lee / propone',23,'#C5DDE0',400,'middle');f.text(140,241,'elige herramientas',21,'#C5DDE0',400,'middle')
f.rect(400,115,260,155,PALE,TEAL,12);f.text(530,162,'SERVIDOR MCP',24,TEAL,600,'middle');f.text(530,204,'de Positron',24,NAVY,500,'middle');f.text(530,242,'conecta herramientas',20,MUTED,400,'middle')
f.rect(805,115,300,155,WHITE,TEAL,12);f.text(955,160,'SESIÓN R',26,TEAL,600,'middle');f.text(955,204,'objetos + cálculos',24,NAVY,500,'middle');f.text(955,242,'consola + gráficos',22,MUTED,400,'middle')
f.arrow(275,148,390,148,MAG);f.text(332,103,'llamada',20,MAG,400,'middle');f.arrow(670,148,795,148,MAG)
f.arrow(795,240,670,240,TEAL);f.arrow(390,240,275,240,TEAL);f.text(530,340,'El estado compartido facilita explorar; los scripts permiten reproducir.',26,NAVY,500,'middle');f.save()

f=Figure('onboarding','Onboarding de un analista','Un estudio exige ciencia, semántica de datos y reglas de colaboración antes de modelar.')
f.circle(140,190,65,NAVY);f.circle(140,165,20,WHITE);f.path('M 102 229 Q 140 178 178 229',WHITE,9)
f.text(140,302,'Nuevo analista',27,NAVY,600,'middle')
for i,(name,desc,col) in enumerate([('Estudio','Pregunta, diseño e hipótesis',MAG),('Datos','Variables, categorías y códigos',TEAL),('Equipo','Permisos, estilo y entregables',NAVY)]):
    y=12+i*132;f.file(465,y,name,desc,600,col);f.arrow(220,190,450,y+51,col,2.5)
f.save()

f=Figure('documentos','Dónde vive cada información','Los documentos científicos conservan las decisiones; AGENTS.md señala reglas y rutas; skills contienen procedimientos.')
f.file(18,18,'protocolo.md','Qué se investiga',335,MAG);f.file(392,18,'diccionario.csv','Qué significa cada variable',335,TEAL);f.file(765,18,'README.md','Cómo recorrer el proyecto',335,NAVY)
f.rect(200,240,710,125,NAVY,r=14);f.text(555,283,'AGENTS.md',34,WHITE,600,'middle');f.text(555,326,'Reglas estables + rutas a las fuentes',26,'#CEE3E5',400,'middle')
for x in [183,559,932]:f.arrow(555,230,x,135,TEAL,2.5)
f.save()

f=Figure('clasificar','Separar tipo de información','Actividad: asignar cada afirmación a un documento apropiado; solución se explica en la siguiente etapa.')
items=[('«99 = perdido»','diccionario.csv',TEAL),('«Dos dimensiones hipotéticas»','protocolo.md',MAG),('«No sobrescribir originales»','AGENTS.md',NAVY),('«Cómo auditar ítems»','SKILL.md',TEAL)]
for i,(text,dst,color) in enumerate(items):
    y=8+i*100;f.badge(35,y+38,str(i+1),color);f.text(80,y+48,text,29,NAVY,500);f.line(600,y+40,710,y+40,LINE,3,True);f.rect(755,y+4,330,72,WHITE,LINE,9,1);f.text(920,y+49,dst,26,color,500,'middle')
f.save()

f=Figure('agents-limites','Límites de AGENTS.md','Reglas operativas y rutas son útiles; secretos, resultados y recetas universales no pertenecen a esas instrucciones.')
f.text(20,42,'SÍ: CÓMO TRABAJAR',25,TEAL,600);f.text(605,42,'NO: ALMACENAR TODO',25,MAG,600);f.line(555,50,555,390,LINE)
for i,(a,b) in enumerate([('Conservar datos originales','Claves o contraseñas'),('Leer protocolo y diccionario','Todo el protocolo duplicado'),('Justificar cambios de modelo','«Usa siempre el mismo estimador»')]):
    y=115+i*105;f.circle(37,y-8,13,TEAL);f.text(75,y,a,26,NAVY,width=430);f.text(608,y,'×',36,MAG,600);f.text(653,y,b,26,NAVY,width=430)
f.save()

f=Figure('plan','Planificación proporcional','Dos tareas de distinto riesgo: una inspección breve no exige un archivo de plan; decisiones encadenadas requieren mayor explicitud.')
f.rect(23,95,325,170,NAVY,r=14);f.text(185,145,'¿Cuánto puede cambiar',25,WHITE,500,'middle');f.text(185,182,'esta tarea?',30,WHITE,600,'middle');f.text(185,227,'riesgo + complejidad',22,'#BAD7DB',400,'middle')
f.arrow(360,160,560,80,TEAL);f.arrow(360,205,560,303,MAG)
f.rect(580,14,510,145,PALE,r=12);f.text(610,58,'Inspección acotada',28,TEAL,600);f.text(610,102,'Objetivo + criterios claros.',25,NAVY);f.text(610,137,'Sin un plan.md obligatorio.',23,MUTED)
f.rect(580,239,510,155,PINK,r=12);f.text(610,281,'Decisiones encadenadas',28,MAG,600);f.text(610,324,'Pasos, dependencias y revisiones.',25,NAVY);f.text(610,365,'Un plan escrito puede ser útil.',23,MUTED);f.save()

f=Figure('pedido','Un encargo con información accionable','La tarea se descompone en propósito, contexto, límites y evidencia de entrega.')
f.text(10,45,'«Haz el análisis factorial»',36,MAG,600);f.arrow(430,35,520,35,LINE)
f.text(550,46,'¿Qué falta para empezar?',30,NAVY,500)
for i,(title,body) in enumerate([('PREGUNTA','Estructura interna propuesta'),('CONTEXTO','Protocolo y diccionario'),('LÍMITES','No recodificar ambigüedades'),('ENTREGA','Código, salidas y diagnósticos')]):
    x=15+(i%2)*563;y=100+(i//2)*155
    f.text(x,y+24,title,20,TEAL,600);f.line(x,y+44,x+520,y+44,LINE,2);f.text(x,y+89,body,28,NAVY,500,width=500)
f.save()

f=Figure('skill-carga','Cómo entra una skill en el trabajo','Metadatos orientan la selección; instrucciones y referencias se incorporan cuando la tarea lo necesita.')
for i,(a,b,c) in enumerate([('1','DESCUBRIR','Nombre + descripción'),('2','APLICAR','Instrucciones pertinentes'),('3','CONSULTAR','Referencias / scripts')]):
    x=20+i*370;f.rect(x,85,325,185,PALE if i!=1 else PINK,r=12);f.badge(x+35,118,a,TEAL if i!=1 else MAG);f.text(x+25,174,b,24,NAVY,600);f.text(x+25,223,c,23,MUTED,width=275)
    if i<2:f.arrow(x+330,180,x+360,180,TEAL)
f.text(560,344,'La skill orienta el trabajo; no reentrena el modelo ni certifica el resultado.',25,NAVY,500,'middle');f.save()

f=Figure('skill-herramienta','Procedimiento frente a capacidad','La skill define cómo abordar una tarea; MCP conecta capacidades de ejecución; ninguno decide la pertinencia científica.')
f.rect(15,70,510,235,PINK,r=15);f.text(45,119,'SKILL',30,MAG,600);f.text(45,170,'«Inspecciona códigos antes de',28,NAVY);f.text(45,208,'ajustar el modelo»',28,NAVY);f.text(45,264,'Procedimiento reutilizable',23,MUTED)
f.rect(595,70,510,235,PALE,r=15);f.text(625,119,'HERRAMIENTA / MCP',30,TEAL,600);f.text(625,170,'Leer un archivo, ejecutar R,',28,NAVY);f.text(625,208,'consultar un gráfico.',28,NAVY);f.text(625,264,'Capacidad operativa',23,MUTED)
f.text(560,383,'El investigador evalúa cuándo corresponde utilizar ambas.',27,NAVY,600,'middle');f.save()

f=Figure('skill-confianza','Inspeccionar antes de adoptar','Cadena de revisión desde la procedencia de una skill hasta una prueba reproducible.')
for i,(a,b) in enumerate([('ORIGEN','Autor y versión'),('CONTENIDO','Método y límites'),('PERMISOS','Scripts y accesos'),('PRUEBA','Caso + error conocido')]):
    x=15+i*280;f.circle(x+120,110,43,TEAL if i%2==0 else MAG);f.text(x+120,123,str(i+1),34,WHITE,700,'middle');f.text(x+120,209,a,23,NAVY,600,'middle');f.text(x+120,252,b,22,MUTED,400,'middle')
    if i<3:f.arrow(x+174,110,x+270,110,LINE)
f.rect(40,325,1040,65,NAVY,r=10);f.text(560,367,'Una instrucción externa también puede inducir acciones incorrectas.',25,WHITE,500,'middle');f.save()

f=Figure('repo','Skills disponibles y trabajo en curso','Instantánea del monorepo del autor. El núcleo de estilo R existe; los módulos especializados no se presentan como finalizados.')
f.file(20,30,'r-analytic-core','Estilo de código de investigación',450,TEAL);f.chip(45,169,245,'Disponible para revisar',TEAL,PALE)
f.file(650,30,'EPIC en desarrollo','Datos + análisis + psicometría',450,MAG);f.chip(675,169,290,'Integrar cuando se valide',MAG,PINK)
f.arrow(485,85,630,85,LINE);f.text(560,310,'Misma fuente de skills; versión fijada para la demostración.',29,NAVY,600,'middle');f.text(560,361,'No mantener una copia paralela e inconsistente dentro del taller.',24,MUTED,400,'middle');f.save()

f=Figure('datos-ordinales','Matriz de respuestas','Extracto inventado para aprender a inspeccionar categorías; no es una muestra estimada.',kind='matriz ilustrativa ficticia')
headers=['Caso','ítem 1','ítem 2','ítem 3','ítem 4','ítem 5','ítem 6']
rows=[['A','1','2','3','4','2','1'],['B','3','99','2','1','4','2'],['C','2','1','4','2','3','4'],['D','4','3','1','3','1','2']]
left=20;col=145;top=52;rh=64
for j,t in enumerate(headers):f.rect(left+j*col,top,col-3,rh,NAVY,r=0);f.text(left+j*col+(col-3)/2,top+42,t,24,WHITE,600,'middle')
for i,row in enumerate(rows):
    for j,t in enumerate(row):
        bad=t=='99'; x=left+j*col;y=top+(i+1)*rh
        f.rect(x,y,col-3,rh-3,PINK if bad else (WHITE if i%2==0 else PALE),r=0);f.text(x+(col-3)/2,y+41,t,27,MAG if bad else NAVY,700 if bad else 400,'middle')
f.badge(1060,top+2*rh+30,'!',MAG);f.text(20,408,'El dato no explica por sí solo qué significa su código.',26,NAVY,500);f.save()

f=Figure('invertir','Recodificación inversa documentada','Escala de 1 a 4: la transformación 5 menos respuesta invierte la puntuación solo cuando lo indica la clave.')
f.text(20,44,'RESPUESTA ORIGINAL',23,NAVY,600);f.text(20,278,'PUNTUACIÓN INVERTIDA',23,NAVY,600)
for i,v in enumerate([1,2,3,4]):
    x=340+i*180;f.chip(x-55,63,110,str(v));f.chip(x-55,298,110,str(5-v),MAG,PINK);f.arrow(x,129,x,281,MAG,3)
f.rect(420,161,420,65,NAVY,r=9);f.text(630,204,'5 - respuesta',31,WHITE,500,'middle',mono=True)
f.text(560,404,'La clave del instrumento autoriza la inversión, no el signo de una correlación.',24,MUTED,400,'middle');f.save()

f=Figure('modelo-factorial','Dos dimensiones hipotéticas','Esquema de dos factores correlacionados y doce indicadores. Se omiten residuos para simplificar; no hay coeficientes estimados.')
for k,(cx,lab,color) in enumerate([(270,'Planificación',TEAL),(850,'Persistencia',MAG)]):
    f.circle(cx,90,71,PALE if k==0 else PINK,color,2)
    f.text(cx,98,lab,23,color,600,'middle')
    for j in range(6):
        x=20+k*580+j*85
        f.arrow(cx,164,x+34,279,color,2)
        f.rect(x,290,69,61,WHITE,color,8,1.5)
        f.text(x+34,330,f'i{1+j+k*6:02}',23,color,600,'middle')
f.line(356,90,764,90,MUTED,3)
f.arrow(400,90,356,90,MUTED,3);f.arrow(720,90,764,90,MUTED,3)
f.text(560,62,'correlación propuesta',22,MUTED,400,'middle')
f.text(560,408,'Sin parámetros estimados. Residuos omitidos en este esquema didáctico.',23,MUTED,400,'middle');f.save()

f=Figure('controles-humanos','Puntos de revisión','Tres carriles separan decisiones humanas, trabajo del agente y operaciones en R.')
ys=[74,204,334]
for y,lab,col in zip(ys,['INVESTIGADOR','AGENTE','R'],[MAG,NAVY,TEAL]):f.rect(0,y-38,210,72,col,r=8);f.text(105,y+8,lab,22,WHITE,600,'middle');f.line(225,y,1110,y,LINE,2,True)
for x,y,label,col in [(278,74,'Define objetivo',MAG),(480,204,'Audita / propone',NAVY),(690,74,'Aprueba método',MAG),(885,334,'Ejecuta',TEAL),(885,74,'Revisa evidencia',MAG)]:
    f.rect(x-75,y-33,187,66,WHITE,col,8,2);f.text(x+18,y+9,label,20,col,600,'middle')
f.arrow(390,87,480,167);f.arrow(575,178,680,109);f.arrow(800,109,902,296);f.arrow(1000,302,1000,110,MAG)
f.save()

f=Figure('diagnostico','Qué revisar después de la convergencia','La finalización de un algoritmo no sustituye las comprobaciones de solución, ajuste y sentido sustantivo.')
f.rect(5,139,250,120,PALE,TEAL,12);f.text(130,184,'CONVERGIÓ',28,TEAL,600,'middle');f.text(130,224,'El algoritmo terminó',21,MUTED,400,'middle')
for i,(a,b) in enumerate([('Solución','¿Parámetros admisibles?'),('Ajuste','¿Problemas globales o locales?'),('Sentido','¿Modelo e inferencia defendibles?')]):
    y=10+i*137;f.arrow(270,199,520,y+50,LINE,2);f.rect(540,y,565,108,WHITE,LINE,10,1.5);f.text(564,y+42,a,28,NAVY,600);f.text(564,y+81,b,23,MUTED)
f.save()

f=Figure('sesion-limpia','Sesión persistente frente a reproducción','La memoria interactiva agiliza el trabajo. La reproducción exige reconstruir el análisis desde los archivos.')
f.text(15,36,'EXPLORACIÓN',24,MAG,600);f.text(665,36,'REPRODUCCIÓN',24,TEAL,600)
f.rect(15,80,430,190,PINK,r=14);f.text(45,127,'.GlobalEnv',30,MAG,600,mono=True);f.text(45,179,'Objetos creados durante la sesión',24,NAVY,width=360);f.text(45,238,'¿Están todos en el script?',24,MAG,500)
f.arrow(470,175,615,175,LINE);f.text(540,130,'reiniciar',21,MUTED,400,'middle')
f.file(665,76,'01_microcaso.R','Entrada y pasos explícitos',440,TEAL);f.file(665,215,'salida_referencia.txt','21.8 → 2.5; n válido = 4',440,TEAL)
f.text(560,388,'El historial de la conversación no sustituye al código canónico.',27,NAVY,500,'middle');f.save()

f=Figure('validez','Del resultado a la afirmación','Cada conclusión necesita evidencia pertinente. Un ajuste favorable no prueba todos los usos de una escala.')
f.rect(25,40,1050,110,NAVY,r=10);f.text(550,86,'«El modelo ajustó bien; por tanto, la escala es válida»',30,WHITE,500,'middle');f.text(550,128,'AFIRMACIÓN PARA AUDITAR, NO RESULTADO DEL TALLER',18,'#B9D5D9',600,'middle')
f.arrow(550,165,550,230,MAG);f.text(550,284,'¿Qué parte está respaldada?',34,MAG,600,'middle')
f.text(550,346,'Datos → especificación → diagnósticos → alcance del uso',27,NAVY,500,'middle');f.save()

f=Figure('seguridad','Cuatro controles','Datos, código, método e instrucciones externas requieren controles diferentes.')
for i,(title,sub,col) in enumerate([('DATOS','Minimizar y proteger',TEAL),('CÓDIGO','Leer y reproducir',NAVY),('MÉTODO','Justificar y revisar',MAG),('SKILLS','Verificar procedencia',GOLD)]):
    x=24+(i%2)*562;y=15+(i//2)*205
    f.circle(x+52,y+70,42,col);f.text(x+52,y+82,str(i+1),34,WHITE,600,'middle');f.text(x+115,y+61,title,28,col,600);f.text(x+115,y+108,sub,25,NAVY,width=390)
f.save()

f=Figure('transferencia','Transferencia a otros análisis','El método de colaboración se mantiene y la especificación estadística cambia.')
f.rect(280,116,560,162,NAVY,r=16);f.text(560,166,'PREGUNTAR · CONTEXTUALIZAR',27,WHITE,600,'middle');f.text(560,217,'EJECUTAR · VERIFICAR',29,'#9DDADE',600,'middle');f.text(560,254,'con decisiones humanas',22,WHITE,400,'middle')
for x,y,txt,col in [(35,30,'Regresión',TEAL),(850,30,'Psicometría',MAG),(35,322,'Encuestas',NAVY),(850,322,'Longitudinal',TEAL)]:
    f.rect(x,y,235,70,PALE if col!=MAG else PINK,r=10);f.text(x+117,y+44,txt,26,col,600,'middle')
f.arrow(280,148,200,109,LINE);f.arrow(840,148,930,109,LINE);f.arrow(280,251,200,311,LINE);f.arrow(840,251,930,311,LINE);f.save()

f=Figure('hero','Pregunta, código y evidencia','Motivo visual del taller: instrucciones y decisiones humanas conectadas con R y resultados.',w=400,h=390)
f.circle(205,185,140,'none','#29505A',2);f.circle(205,185,100,'none','#29505A',1.5)
for x,y,t,col in [(58,65,'?',MAG),(330,95,'R',TEAL),(330,305,'✓',MAG),(80,300,'{ }',TEAL)]:f.circle(x,y,41,col);f.text(x,y+12,t,34,WHITE,600,'middle')
f.text(205,169,'CRITERIO',27,WHITE,600,'middle');f.text(205,211,'CIENTÍFICO',27,'#83D1D6',600,'middle')
f.arrow(101,65,288,95,'#71939C',2);f.arrow(330,140,330,257,'#71939C',2);f.arrow(284,304,128,300,'#71939C',2);f.save()

# Screenshot transformations retain original pixels; crop and annotation only.
def crop(name,src,box,marks=()):
    im=Image.open(SHOTS/src).convert('RGB').crop(box);d=ImageDraw.Draw(im)
    ff=ImageFont.truetype(fontpath,27)
    for x,y,label,rect in marks:
        if rect:d.rectangle(rect,outline=MAG,width=4)
        d.ellipse((x-22,y-22,x+22,y+22),fill=MAG,outline=WHITE,width=2)
        bb=d.textbbox((0,0),label,font=ff);d.text((x-(bb[2]-bb[0])/2,y-(bb[3]-bb[1])/2-bb[1]),label,font=ff,fill=WHITE)
    p=SHOTS/(name+'.png');im.save(p)
    manifest.append(dict(file=str(p.relative_to(ROOT)),kind='captura real recortada/anotada',source=str(src),crop=list(box),marks=[list(m[:3]) for m in marks],sha256=hashlib.sha256(p.read_bytes()).hexdigest()))

crop('mcp-vista','originales/positron-mcp.png',(56,103,1394,883),[(90,165,'1',(67,149,753,216)),(813,185,'2',(781,151,1327,312)),(802,388,'3',(781,373,1329,764))])
crop('mcp-ejecutar','originales/positron-mcp.png',(120,252,420,286))
crop('mcp-consola','originales/positron-mcp.png',(842,270,1150,306))
crop('assistant-flujo','originales/positron-assistant.png',(104,388,1417,757),[(24,102,'1',(8,83,445,184)),(530,55,'2',(470,4,1300,355))])
crop('proveedor','originales/positron-proveedor.png',(0,0,1184,392))
# Local captures are actual screenshots of an isolated Positron profile, no agent run is implied.
p=SHOTS/'propias/positron-microcaso.png'
if p.exists():
    crop('r-editor','propias/positron-microcaso.png',(312,145,1550,600))
    crop('r-consola','propias/positron-microcaso.png',(320,787,1090,966))
    crop('r-entorno','propias/positron-microcaso.png',(312,63,1548,967),[(24,110,'1',None),(24,580,'2',None),(24,770,'3',None)])
p=SHOTS/'propias/positron-skill.png'
if p.exists():crop('skill-real','propias/positron-skill.png',(315,145,1550,585))
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'visuals':len([x for x in manifest if x['file'].endswith('.svg')]),'screenshot_derivatives':len([x for x in manifest if x['file'].endswith('.png')])}))
