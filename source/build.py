"""Rebuild index.html from the template: python3 build.py (run from this folder)."""
import json
s=open('tpl.html').read()
img=json.load(open('img.json'))
mv={'app':open('mv/app.html').read(),'web':open('mv/web.html').read()}
import os
cv=json.load(open('cv.json')) if os.path.exists('cv.json') else {}
mvj=json.dumps(mv,ensure_ascii=False).replace('</','<\\/')
open('../index.html','w').write(s.replace('/*CV*/{}',json.dumps(cv)).replace('/*MV*/{}',mvj).replace('/*IMG*/{}',json.dumps(img)))
