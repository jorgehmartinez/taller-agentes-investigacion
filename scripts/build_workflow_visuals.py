#!/usr/bin/env python3
"""Teaching schematics, not observed runs. Rebuild only new workflow assets."""
from visual_primitives import *
import base64

def icon(f,name,x,y,size):
 p=ROOT/'presentacion/assets/brands'/name
 f.p.append(f'<image x="{x}" y="{y}" width="{size}" height="{size}" href="data:image/png;base64,{base64.b64encode(p.read_bytes()).decode()}"/>')
def window(f,x,y,w,h,title,accent=TEAL):
 f.rect(x,y,w,h,WHITE,LINE,13,1.5);f.rect(x,y,w,43,PALE if accent==TEAL else PINK,r=13)
 for i in range(3):f.circle(x+18+16*i,y+21,4,accent)
 f.text(x+77,y+29,title,21,NAVY,600)
def code(f,x,y,lines,size=23,color=NAVY):
 for i,s in enumerate(lines):f.text(x,y+i*30,s,size,color,mono=True)

f=Figure('encuadre','Qué aprenderemos y qué no','Objetivos de la introducción y límites de su alcance.')
f.text(34,44,'SÍ: UN MÉTODO DE TRABAJO',26,TEAL,600)
f.text(609,44,'NO: UN REEMPLAZO DEL INVESTIGADOR',25,MAG,600)
f.line(560,25,560,361,LINE,2)
for i,(a,b) in enumerate([('Comprender agentes y herramientas','Dejar de aprender R o metodología'),('Dirigir un análisis con contexto','Delegar decisiones científicas'),('Revisar y continuar el código','Dominar todos los modelos en 3 horas')]):
 y=115+i*96;f.circle(49,y-8,15,TEAL);f.text(49,y,'✓',22,WHITE,700,'middle');f.text(82,y,a,28,NAVY,width=440)
 f.text(615,y,'×',29,MAG,600);f.text(655,y,b,27,NAVY,width=420)
f.save()

f=Figure('ruta-investigacion','El recorrido','De entender el modelo a dirigir un análisis revisable en R.')
labels=[('Entender','LLM y agentes'),('Reconocer','Fricciones y código'),('Orientar','Contexto y skills'),('Practicar','Positron y R')]
for i,(title,subtitle) in enumerate(labels):
 x=50+i*273;f.circle(x+82,126,53,PALE if i%2==0 else PINK);f.text(x+82,143,f'0{i+1}',45,TEAL if i%2==0 else MAG,600,'middle')
 f.text(x+82,234,title,31,NAVY,600,'middle');f.text(x+82,280,subtitle,24,MUTED,400,'middle')
 if i<3:f.arrow(x+150,126,x+205,126,LINE,3)
f.line(38,337,1080,337,LINE,2);f.text(560,385,'Un hilo común: no perder el control del análisis',28,NAVY,500,'middle');f.save()

f=Figure('llm-lenguaje','Un redactor con contexto','Analogía de continuaciones posibles, sin probabilidades ni frecuencias medidas.')
f.rect(22,111,400,182,NAVY,r=14);f.text(47,151,'ENCARGO + CONTEXTO',22,'#9EDADE',600)
f.text(47,205,'«Para interpretar una escala,',29,WHITE);f.text(47,248,'primero necesitamos…»',29,WHITE)
for i,t in enumerate(['conocer el constructo','revisar cómo se respondió','entender el uso previsto']):
 y=33+i*121;f.arrow(435,205,580,y+40,TEAL if i!=1 else MAG,2)
 f.rect(596,y,490,91,PALE if i!=1 else PINK,r=10);f.text(624,y+55,t,28,NAVY,500)
f.text(27,390,'Generación probabilística: propone continuaciones a partir del contexto.',25,MUTED);f.save()

f=Figure('marcas-llm','Marcas conocidas','GPT/ChatGPT de OpenAI, Claude de Anthropic y Gemini de Google, sin ranking ni versiones.')
for i,(file,name,sub) in enumerate([('chatgpt.png','GPT / ChatGPT','OpenAI'),('claude.png','Claude','Anthropic'),('gemini.png','Gemini','Google')]):
 cx=185+i*375;icon(f,file,cx-57,53,114);f.text(cx,231,name,38,NAVY,600,'middle');f.text(cx,276,sub,25,MUTED,400,'middle')
f.line(65,326,1055,326,LINE,2);f.text(560,376,'Modelo ≠ producto ≠ herramientas disponibles',29,NAVY,500,'middle');f.save()

f=Figure('chat-agente-directo','Conversar o actuar','Una interfaz de chat sin herramientas locales frente a un agente con acceso autorizado.')
window(f,22,60,410,250,'CHAT SIN ACCESO LOCAL',MAG)
f.rect(55,128,339,61,PINK,r=12);f.text(76,168,'«Aquí tienes un código…»',26,NAVY)
f.text(58,253,'La persona lo lleva al entorno.',25,MUTED)
f.arrow(454,188,526,188,LINE,3)
f.rect(551,60,547,250,WHITE,TEAL,13,2);f.text(580,103,'AGENTE DE CODIFICACIÓN',24,TEAL,600)
for i,(lab,detail) in enumerate([('Archivos','lee y edita'),('Terminal','ejecuta'),('Iteración','observa y sigue')]):
 x=577+i*172;f.rect(x,137,148,71,PALE,r=9);f.text(x+74,181,lab,25,TEAL,600,'middle');f.text(x+74,249,detail,21,MUTED,400,'middle')
f.text(560,378,'Con permisos, límites y puntos de revisión humana.',28,NAVY,500,'middle');f.save()

f=Figure('analista-aumentado','Asistencia al investigador','El agente puede asumir mecánica sin asumir la responsabilidad científica.')
f.circle(175,185,90,NAVY);f.circle(175,158,21,WHITE);f.path('M 132 219 Q 175 167 218 219',WHITE,9);f.text(175,316,'INVESTIGADOR',26,NAVY,600,'middle')
f.text(340,103,'PUEDE APOYARSE EN EL AGENTE',25,TEAL,600)
for i,(a,b) in enumerate([('Preparar código','Revisar documentación'),('Ejecutar tareas','Inspeccionar errores')]):
 for j,l in enumerate([a,b]):f.chip(342+j*377,142+i*104,345,l,TEAL,PALE)
f.arrow(273,185,326,185,TEAL,3)
f.rect(339,370,731,44,PINK,r=8);f.text(365,400,'Potencial de productividad, no una ganancia garantizada.',23,MAG,500);f.save()

f=Figure('codigo-apropiable','Código que podemos continuar','El script se conecta con cinco capacidades que el investigador conserva.')
f.rect(365,95,390,204,NAVY,r=12);f.text(560,151,'analisis.R',40,WHITE,600,'middle');f.text(560,204,'modelos · datos · diagnósticos',24,'#9EDADE',400,'middle');f.text(560,260,'Decisiones a la vista',27,WHITE,500,'middle')
for x,y,label in [(38,48,'Leer'),(38,289,'Revisar'),(854,48,'Ejecutar'),(854,289,'Modificar')]:
 f.rect(x,y,222,72,PALE,TEAL,10,1.5);f.text(x+111,y+47,label,29,TEAL,600,'middle')
 f.arrow(x+222 if x<300 else x,y+36,365 if x<300 else 755,154 if y<200 else 253,LINE,2)
f.text(560,379,'Y depurar o continuar sin depender de la conversación.',26,NAVY,500,'middle');f.save()

# A stable two-window layout: same request, same code; manual exchange changes.
for state in ['necesidad','traslado','error']:
 f=Figure('chat-'+state,'Del chat al entorno','Recreación esquemática ficticia de ChatGPT web y RStudio. No reproduce una conversación real.',kind='recreación ficticia de interfaz')
 window(f,10,17,487,370,'ChatGPT · ejemplo ficticio',MAG)
 window(f,634,17,476,370,'RStudio · ejemplo ficticio')
 f.rect(29,82,449,72,PINK,r=10);f.text(46,110,'«Quiero evaluar dos factores',24,NAVY);f.text(46,140,'en 12 ítems ordinales.»',24,NAVY)
 if state!='error':
  f.text(31,188,'Revisa el diccionario. Luego:',23,NAVY)
  f.rect(30,209,447,119,NAVY,r=9);f.text(53,238,'R',18,'#9EDADE',600);f.text(449,238,'Copiar',18,'#9EDADE',400,'end')
  code(f,52,275,['ajuste <- cfa(modelo,', '  data = datos, ordered = items)'],21,WHITE)
 else:
  f.rect(30,183,447,112,PINK,MAG,9,1.5);f.text(50,217,'«No encuentra cfa().',26,MAG,500);f.text(50,255,'¿Qué tengo que cambiar?»',26,MAG,500)
  f.text(31,338,'¿Paquete, ruta o estado de R?',24,MUTED)
 f.line(651,244,1091,244,LINE,2);f.text(655,104,'SCRIPT',19,TEAL,600);f.text(655,275,'CONSOLA',19,TEAL,600)
 if state=='necesidad':
  f.text(655,160,'Aquí habrá que ejecutar',25,MUTED);f.text(655,197,'el código recibido.',25,MUTED);f.text(655,333,'>',25,TEAL,mono=True)
 elif state=='traslado':
  code(f,655,152,['ajuste <- cfa(modelo,','  data = datos,','  ordered = items)'],22)
  f.arrow(510,219,619,219,TEAL,5);f.text(565,186,'copiar',23,TEAL,500,'middle');f.text(565,267,'pegar',23,TEAL,500,'middle');f.text(655,331,'> Ejecutar el fragmento…',23,MUTED,mono=True)
 else:
  code(f,655,152,['ajuste <- cfa(modelo,','  data = datos,','  ordered = items)'],22)
  f.text(655,317,'Error: no se pudo encontrar',23,MAG,mono=True);f.text(655,353,'la función "cfa"',23,MAG,mono=True)
  f.arrow(620,320,510,320,MAG,5);f.text(565,285,'volver',22,MAG,500,'middle')
 f.save()

f=Figure('agente-operando','El ciclo con herramientas','Un agente lee el proyecto, ejecuta, observa resultados y corrige dentro del alcance autorizado.')
f.rect(24,65,263,285,WHITE,LINE,12,2);f.text(50,107,'PROYECTO LOCAL',23,TEAL,600)
for i,lab in enumerate(['protocolo.md','datos.csv','analisis.R']):f.text(53,167+i*61,lab,26,NAVY,mono=True)
f.circle(500,202,89,NAVY);f.text(500,193,'AGENTE',30,WHITE,600,'middle');f.text(500,237,'elige la acción',21,'#9EDADE',400,'middle')
f.arrow(300,166,398,166,TEAL,3);f.arrow(398,243,300,243,TEAL,3)
f.rect(728,65,367,285,WHITE,LINE,12,2);f.text(751,108,'TERMINAL / R',24,TEAL,600)
f.text(753,171,'Ejecuta el script',27,NAVY);f.text(753,237,'Observa la salida',27,NAVY);f.text(753,303,'Revisa y vuelve a probar',24,NAVY)
f.arrow(603,166,711,166,TEAL,3);f.arrow(711,243,603,243,MAG,3)
f.text(560,402,'La persona define alcance, método y cambios que requieren aprobación.',24,MUTED,400,'middle');f.save()

f=Figure('safe-cfa-mapa','La decisión fragmentada','Escenario ficticio con configuración, envoltura, ciclo y selección separados.')
f.text(21,35,'NECESIDAD: «QUIERO CAMBIAR UN SOLO AFC»',26,MAG,600)
for x,y,fn,body in [(18,81,'config/modelos.R','Lista de modelos'),(597,81,'R/helpers.R','safe_cfa()'),(18,247,'scripts/ajustar.R','Bucle for'),(597,247,'R/comparar.R','Ordenar y seleccionar')]:
 f.file(x,y,fn,body,490,TEAL if x<400 else MAG)
f.arrow(512,132,578,132,LINE,3);f.arrow(842,194,842,235,LINE,3);f.arrow(578,297,512,297,LINE,3)
f.text(560,409,'¿Dónde están la hipótesis, el estimador y los fallos?',29,NAVY,600,'middle');f.save()

f=Figure('dos-estilos','Dos necesidades de trabajo','Las abstracciones se ajustan a la estabilidad de las decisiones, no a una jerarquía entre industria e investigación.')
f.text(32,43,'TAREA ESTABLE Y REPETIDA',25,TEAL,600);f.text(616,43,'INVESTIGACIÓN ITERATIVA',25,MAG,600);f.line(560,30,560,367,LINE,2)
for i,s in enumerate(['Una regla acordada','Muchas ejecuciones','Automatización explícita']):
 y=103+i*91;f.rect(37,y,460,62,PALE,r=8);f.text(65,y+41,s,28,NAVY)
 if i<2:f.arrow(267,y+64,267,y+86,TEAL,2)
f.rect(622,104,450,217,PINK,r=12);f.text(650,153,'Especificar → estimar → revisar',25,NAVY,500);f.text(650,208,'Cambiar una decisión',28,NAVY);f.text(650,262,'Volver a inspeccionar',28,NAVY)
f.text(560,400,'Ambos necesitan rigor y reproducibilidad; cambia la organización.',25,MUTED,400,'middle');f.save()

# Same geometry across the overview and focus state.
for focus in [False,True]:
 name='ecosistema-foco' if focus else 'ecosistema-agente'
 f=Figure(name,'El entorno del agente','Mapa conjunto de harness, reglas, AGENTS.md, skills, plugins y MCP.')
 f.rect(331,58,453,300,PAPER,LINE,16,2);f.text(557,98,'HARNESS',29,NAVY,600,'middle');f.text(557,133,'programa que coordina el trabajo',22,MUTED,400,'middle')
 f.circle(557,231,68,NAVY);f.text(557,225,'LLM',32,WHITE,600,'middle');f.text(557,259,'modelo',22,'#9EDADE',400,'middle')
 items=[(8,37,'SYSTEM PROMPT','Reglas del producto',False),(8,206,'AGENTS.md','Guía del proyecto',True),(832,37,'SKILLS / PLUGINS','Procedimientos y recursos',True),(832,206,'HERRAMIENTAS / MCP','Acceso a archivos, R y más',False)]
 for x,y,label,detail,highlight in items:
  color=MAG if focus and highlight else TEAL if not focus else MUTED
  fill=PINK if focus and highlight else WHITE
  f.rect(x,y,280,131,fill,color,11,3 if focus and highlight else 1.4)
  f.text(x+18,y+44,label,23,color,600);f.text(x+18,y+88,detail,22,NAVY,width=248)
  f.line(x+280 if x<300 else x,y+65,331 if x<300 else 784,178 if y<200 else 278,LINE,2)
 f.text(557,398,'Contexto · acciones · permisos · límites',26,NAVY,500,'middle');f.save()

f=Figure('proyecto-skills','Proyecto y procedimiento','El proyecto describe la ciencia; AGENTS.md enlaza las fuentes y las skills orientan trabajo reutilizable.')
f.rect(14,25,498,245,WHITE,LINE,12,1.5);f.text(40,65,'ESTE ESTUDIO',25,MAG,600)
for i,(a,b) in enumerate([('Protocolo','objetivos y diseño'),('Especificación','hipótesis y modelos'),('Diccionario','variables y códigos')]):
 y=115+i*61;f.text(42,y,a,25,NAVY,600);f.text(245,y,b,23,MUTED)
f.rect(610,25,495,245,WHITE,LINE,12,1.5);f.text(638,65,'FORMA DE TRABAJAR',25,TEAL,600)
f.text(639,121,'Skill de codificación R',28,NAVY,600);f.text(639,164,'legibilidad, edición y diagnósticos',24,MUTED)
f.text(639,216,'Skills de análisis',28,NAVY,600);f.text(639,250,'procedimientos y condiciones',24,MUTED)
f.rect(278,324,565,80,NAVY,r=12);f.text(560,358,'AGENTS.md',30,WHITE,600,'middle');f.text(560,388,'rutas + límites + expectativas del proyecto',22,'#9EDADE',400,'middle')
f.arrow(390,317,278,279,MAG,2);f.arrow(733,317,858,279,TEAL,2);f.save()

f=Figure('skills-catalogo','Las skills del taller','Base R ya inspeccionable y dos áreas del EPIC todavía en desarrollo.')
for i,(a,b,c,ready) in enumerate([('r-analytic-core','Código de investigación','Disponible para revisar',True),('Manejo de datos','Lectura y preparación','EPIC en desarrollo',False),('Análisis psicométrico','Modelos y diagnósticos','EPIC en desarrollo',False)]):
 x=20+i*370;f.rect(x,60,340,274,WHITE,TEAL if ready else LINE,13,2);f.rect(x,60,340,10,TEAL if ready else MAG,r=3)
 f.text(x+22,123,a,27,NAVY,600,width=299);f.text(x+22,205,b,24,MUTED,width=295)
 f.rect(x+19,260,302,49,PALE if ready else PINK,r=8);f.text(x+170,292,c,22,TEAL if ready else MAG,500,'middle')
f.text(560,398,'r-workflow-plugins · una fuente, sin copias paralelas',27,NAVY,500,'middle');f.save()

(OUT/'workflow-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'created':len(manifest),'files':[Path(x['file']).name for x in manifest]},ensure_ascii=False))
