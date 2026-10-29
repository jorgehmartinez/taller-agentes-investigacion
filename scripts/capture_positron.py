#!/usr/bin/env python3
"""Capture a real, isolated Positron window. Never touches the main profile.

Only the synthetic microexample is executed. No model provider is configured.
The private X display prevents desktop/email/workspace content from appearing.
"""
from pathlib import Path
import subprocess, os, json, time, signal, tempfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'presentacion/assets/screenshots/propias'
OUT.mkdir(parents=True, exist_ok=True)
RUNTIME = ROOT / 'output/capture-runtime'
RUNTIME.mkdir(parents=True, exist_ok=True)
profile = Path(tempfile.mkdtemp(prefix='positron-', dir=RUNTIME))
(profile/'User').mkdir()
settings = {'workbench.startupEditor':'none', 'window.restoreWindows':'none',
            'workbench.colorTheme':'Default Light Modern', 'editor.fontSize':22,
            'terminal.integrated.fontSize':20, 'editor.minimap.enabled':False,
            'editor.wordWrap':'on', 'window.zoomLevel':0,
            'workbench.secondarySideBar.defaultVisibility':'hidden',
            'files.autoSave':'off', 'update.mode':'none', 'extensions.autoUpdate':False,
            'telemetry.telemetryLevel':'off'}
(profile/'User/settings.json').write_text(json.dumps(settings))
log = (RUNTIME/'positron.log').open('w')
xvfb = subprocess.Popen(['Xvfb','-displayfd','1','-screen','0','1600x1000x24','-nolisten','tcp'],stdout=subprocess.PIPE,stderr=log,text=True)
display = ':' + xvfb.stdout.readline().strip()
env = dict(os.environ, DISPLAY=display, GDK_BACKEND='x11', QT_QPA_PLATFORM='xcb')
env.pop('WAYLAND_DISPLAY',None)
app = None
try:
    app = subprocess.Popen(['/usr/bin/positron','--user-data-dir',str(profile),'--new-window','--skip-welcome','--ozone-platform=x11',str(ROOT/'materiales/microcaso/01_microcaso.R')],env=env,stdout=log,stderr=log,start_new_session=True)
    (RUNTIME/'session.json').write_text(json.dumps({'display':display,'pid':app.pid,'profile':str(profile)}))
    time.sleep(12)
    def key(*args):
        subprocess.run(['xdotool',*args],env=env,check=True,timeout=10,stdout=subprocess.DEVNULL)
    windows=subprocess.check_output(['xdotool','search','--onlyvisible','--class','positron'],env=env,text=True).strip().splitlines()
    wid=windows[-1]
    key('windowsize',wid,'1600','1000');key('windowmove',wid,'0','0');key('windowfocus',wid)
    time.sleep(2)
    subprocess.run(['import','-display',display,'-window','root',str(OUT/'positron-inicio.png')],check=True,timeout=15)
    print('INITIAL_CAPTURE',flush=True)
    time.sleep(2)
    # Focus the editor by clicking inside its text area, then run selected script.
    key('mousemove','610','250'); key('click','1');key('key','ctrl+a');key('key','ctrl+Return')
    time.sleep(18)
    key('mousemove','610','250');key('click','1');key('key','ctrl+Home')
    key('key','ctrl+shift+p');time.sleep(1)
    key('type','--clearmodifiers','Notifications: Clear All Notifications');key('key','Return');time.sleep(1)
    key('key','Escape')
    subprocess.run(['import','-display',display,'-window','root',str(OUT/'positron-microcaso.png')],check=True,timeout=15)
    print('MICROCASE_CAPTURE',flush=True)
    # Read-only opening of the real skill, without changing its source.
    key('key','ctrl+o');time.sleep(1)
    key('type','--clearmodifiers',str(ROOT.parent/'r-workflow-plugins/plugins/r-analytic-core/skills/r-analytic-coding-principles/SKILL.md'))
    key('key','Return');time.sleep(4)
    subprocess.run(['import','-display',display,'-window','root',str(OUT/'positron-skill.png')],check=True,timeout=15)
    print('SKILL_CAPTURE',flush=True)
    time.sleep(20)
finally:
    if app:
        try: os.killpg(app.pid,signal.SIGTERM)
        except ProcessLookupError: pass
    xvfb.terminate()
    log.close()
