from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4

ROOT=Path(__file__).resolve().parent
NAVY=colors.HexColor('#15333D'); TEAL=colors.HexColor('#087F8C'); MAG=colors.HexColor('#BF2568')
MUTED=colors.HexColor('#52666E'); PALE=colors.HexColor('#EAF4F3'); LINE=colors.HexColor('#D5E0E0')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle('KickerX',fontName='Helvetica-Bold',fontSize=9,leading=12,textColor=TEAL,spaceAfter=9))
styles.add(ParagraphStyle('TitleX',fontName='Helvetica-Bold',fontSize=24,leading=28,textColor=NAVY,spaceAfter=12))
styles.add(ParagraphStyle('SubX',fontName='Helvetica',fontSize=12,leading=17,textColor=MUTED,spaceAfter=14))
styles.add(ParagraphStyle('BodyX',fontName='Helvetica',fontSize=10.5,leading=15.3,textColor=NAVY,spaceAfter=8))
styles.add(ParagraphStyle('SmallX',fontName='Helvetica',fontSize=9,leading=12.5,textColor=MUTED,spaceAfter=6))
styles.add(ParagraphStyle('HeadX',fontName='Helvetica-Bold',fontSize=12.3,leading=16,textColor=TEAL,spaceBefore=10,spaceAfter=7,keepWithNext=True))
styles.add(ParagraphStyle('CellX',fontName='Helvetica',fontSize=10,leading=14,textColor=NAVY))
styles.add(ParagraphStyle('CellHeadX',fontName='Helvetica-Bold',fontSize=9.6,leading=13,textColor=colors.white))
P=lambda text,kind='BodyX': Paragraph(text,styles[kind])
def header_footer(c,d):
    w,h=A4
    c.setFillColor(TEAL);c.rect(48,h-32,70,4,fill=1,stroke=0)
    c.setFont('Helvetica',8);c.setFillColor(MUTED)
    c.drawRightString(w-48,h-31,'TALLER SPP  |  CASO SIMULADO')
    c.setStrokeColor(LINE);c.line(48,40,w-48,40)
    c.drawString(48,26,'Autorregulación académica · Material ficticio para formación')
    c.drawRightString(w-48,26,str(d.page))
def table(rows,widths,header=True):
    content=[]
    for i,row in enumerate(rows):
        content.append([P(str(x),'CellHeadX' if i==0 and header else 'CellX') for x in row])
    t=Table(content,colWidths=widths,hAlign='LEFT',repeatRows=1 if header else 0)
    cmds=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),('LINEBELOW',(0,-1),(-1,-1),.5,LINE)]
    if header:cmds+=[('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE])]
    else:cmds+=[('BACKGROUND',(0,0),(-1,-1),PALE)]
    t.setStyle(TableStyle(cmds));return t
def build(name,story):
    d=SimpleDocTemplate(str(ROOT/name),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=56,bottomMargin=54,title=name.replace('.pdf',''),author='Brian Norman Peña Calero',subject='Caso sintético de formación en análisis psicométrico',pageCompression=1)
    d.build(story,onFirstPage=header_footer,onLaterPages=header_footer)

s=[P('ENCARGO DEL EQUIPO DE INVESTIGACIÓN','KickerX'),P('Autorregulación académica','TitleX'),P('Estructura interna y fiabilidad de una escala breve de planificación y persistencia en el estudio.','SubX')]
s+=[table([['Carácter del material','Muestra del escenario'],['Instrumento ficticio y respuestas simuladas. No se realizó trabajo de campo con personas reales.','Se prevén 500 participantes en el estudio principal. El número efectivo debe comprobarse en los archivos recibidos.']],[250,249]),Spacer(1,8)]
s+=[P('El problema de investigación','HeadX'),P('Un equipo universitario desea examinar una medida breve de autorregulación académica. La propuesta distingue dos procesos relacionados: <b>planificar</b> el trabajo de estudio y <b>persistir</b> ante dificultades o interrupciones. Necesitamos valorar si las respuestas respaldan esta estructura y qué fiabilidad tienen las puntuaciones de cada dimensión.')]
s+=[P('Diseño del escenario','HeadX'),P('Se representa un estudio <b>instrumental, transversal y no experimental</b>, con estudiantes universitarios adultos de 18 a 30 años. La selección se plantea como no probabilística. Cada participante debería aportar una única respuesta al cuestionario. Edad, ciclo y modalidad se incluyen para describir la muestra, no para justificar inferencias causales ni comparaciones entre grupos.')]
s+=[P('Qué medida se propone','HeadX'),P('La escala didáctica EA-12 contiene doce ítems con cuatro categorías ordenadas. Se propone <b>Planificación</b> para los ítems i01 a i06 y <b>Persistencia</b> para i07 a i12. La redacción, las categorías y la clave se encuentran en <i>Cuestionario y clave.pdf</i> y en <i>diccionario_variables.csv</i>. No asumimos de antemano que sea apropiado obtener una puntuación total de los doce ítems.')]
s+=[P('Hipótesis que orientan el análisis','HeadX'),P('<b>H1.</b> Una estructura de dos factores correlacionados representa mejor la propuesta conceptual que un único factor general.<br/><b>H2.</b> Planificación y Persistencia presentan una asociación positiva, sin que eso implique que sean indistinguibles.')]
s+=[P('Estas hipótesis son parte del encargo, no resultados. El carácter simulado impide usar el ejercicio como evidencia de validación de una escala real.','SmallX'),PageBreak()]
s+=[P('PREGUNTAS, DECISIONES Y ENTREGA','KickerX'),P('Qué necesitamos averiguar','TitleX')]
rows=[['Objetivo','Qué debe responder el análisis'],['1 · Describir y auditar','¿Cómo se distribuyen las respuestas? ¿Qué omisiones, códigos, registros repetidos o problemas de exportación deben resolverse antes de modelar?'],['2 · Examinar la estructura','Contrastar el modelo propuesto de dos factores correlacionados con un modelo unidimensional de referencia. Examinar estimación, parámetros y ajuste global y local.'],['3 · Estimar la fiabilidad','Estimar la fiabilidad de las puntuaciones de cada dimensión, justificando qué coeficiente se utiliza y a qué puntuación corresponde. No equiparar fiabilidad con validez.']]
s+=[table(rows,[145,354]),Spacer(1,7)]
s+=[P('Decisiones que debemos revisar antes de ejecutar','HeadX'),P('Solicitamos una propuesta breve sobre el tratamiento de respuestas ordinales, datos faltantes y posibles registros repetidos. La elección del estimador y cualquier exclusión o cambio de modelo deben justificarse. Los ítems no deben eliminarse ni invertirse por el mero signo de una correlación. Si aparece una ambigüedad documental, debe consultarse, no resolverse por adivinación.')]
s+=[P('Qué esperamos recibir','HeadX'),P('Un análisis en <b>R</b> con código legible y editable; un registro de las decisiones; tablas descriptivas y diagnósticos; una comparación razonada de los modelos; y una interpretación breve con límites explícitos. Otra persona del equipo debe poder ejecutar el código desde una sesión limpia y continuar el trabajo sin depender de la conversación que lo originó.')]
s+=[P('Alcance de esta entrega','HeadX'),P('El encargo no incluye baremos, puntos de corte, diagnóstico individual, equivalencia entre grupos ni inferencias causales. Tampoco solicita una búsqueda mecánica de modelos para maximizar el ajuste. La interpretación se limita a la estructura interna y a la fiabilidad de las puntuaciones propuestas, dentro de este caso didáctico.')]
s+=[P('Documentación recibida','HeadX'),P('Consultar también las notas del equipo para distinguir el estudio principal del piloto. Mantener los archivos recibidos sin sobrescritura y documentar los productos derivados. La organización del proyecto y la forma de trabajo todavía deben acordarse.','BodyX')]
build('Encargo de investigacion.pdf',s)

items=[
('i01','Antes de estudiar, defino qué quiero completar.'),('i02','Distribuyo mi tiempo entre las tareas que tengo pendientes.'),('i03','Empiezo a estudiar sin decidir qué tareas haré.'),('i04','Organizo los materiales que necesito antes de comenzar.'),('i05','Divido los trabajos extensos en pasos más pequeños.'),('i06','Reviso mi planificación cuando cambian los plazos.'),
('i07','Continúo trabajando aunque una tarea requiera más esfuerzo del previsto.'),('i08','Retomo el estudio después de una interrupción.'),('i09','Cuando una actividad se complica, suelo abandonarla.'),('i10','Busco otra manera de avanzar cuando no entiendo un ejercicio.'),('i11','Mantengo el esfuerzo hasta terminar las actividades que me propongo.'),('i12','Vuelvo a intentar una tarea después de equivocarme.')]
s=[P('INSTRUMENTO FICTICIO · EA-12','KickerX'),P('Cuestionario y clave','TitleX'),P('Versión utilizada para el escenario principal de octubre. Los ítems se crearon para el taller y no pertenecen a una escala validada.','SubX'),P('Instrucción al responder','HeadX'),P('Piensa en tus actividades de estudio de las últimas cuatro semanas. Indica con qué frecuencia realizas cada una de las siguientes acciones.')]
s+=[table([['1','2','3','4'],['Casi nunca','Algunas veces','Muchas veces','Casi siempre']],[124.75]*4),Spacer(1,12),P('Dimensión propuesta: Planificación','HeadX'),table([['Código','Redacción']]+[list(x) for x in items[:6]],[62,437]),Spacer(1,12),P('Los códigos se corresponden con las columnas de los archivos CSV. La dirección de puntuación no es equivalente a la redacción original: revisar la clave en la página siguiente.','SmallX'),PageBreak()]
s+=[P('INSTRUMENTO FICTICIO · EA-12','KickerX'),P('Persistencia y puntuación','TitleX'),P('Dimensión propuesta: Persistencia','HeadX'),table([['Código','Redacción']]+[list(x) for x in items[6:]],[62,437]),Spacer(1,9)]
s+=[P('Clave de dirección','HeadX'),P('<b>i03 e i09 son inversos.</b> Para orientar una puntuación de modo que un valor mayor represente más autorregulación, los valores válidos se corresponden así: 1 pasa a 4, 2 a 3, 3 a 2 y 4 a 1. El resto de ítems mantiene su dirección. La exportación contiene respuestas originales: no se ha aplicado esta recodificación.')]
s+=[P('Omisiones y exportación','HeadX'),P('El código <b>99</b> significa <b>sin respuesta</b>. Una celda vacía significa que el dato no quedó registrado en la exportación. Ninguno es una quinta categoría. Los códigos faltantes no se invierten ni se convierten en puntuaciones válidas. La estrategia de tratamiento de omisiones debe explicitarse antes del análisis.')]
s+=[P('Puntuaciones que interesa evaluar','HeadX'),P('Interesa la fiabilidad de las puntuaciones de seis ítems de cada dimensión, con igual ponderación y dirección coherente. La regla para calcular una suma o media cuando falten respuestas aún debe acordarse. No se incluyen puntuaciones precalculadas. La obtención de una puntuación total requiere justificación adicional y no forma parte de la hipótesis principal.')]
s+=[P('Uso exclusivamente formativo. No utilizar este instrumento para evaluar o tomar decisiones sobre personas.','SmallX')]
build('Cuestionario y clave.pdf',s)

from pypdf import PdfReader
for p in ROOT.glob('*.pdf'):
    r=PdfReader(p)
    print(p.name,len(r.pages),'pages',p.stat().st_size,'bytes')
    assert len(r.pages)==2
