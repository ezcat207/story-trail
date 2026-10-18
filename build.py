import json,pathlib,markdown,re
d=pathlib.Path(__file__).parent
t=(d/'index.template.html').read_text()
en=(d/'prompts/rubric-prompt.en.md').read_text(); zh=(d/'prompts/rubric-prompt.zh.md').read_text()
G=[]
for f in sorted((d/'guide').glob('[0-9]*.md')):
    m=f.read_text(); G.append({'title':re.match(r'# (.*)',m).group(1),'html':markdown.markdown(m,extensions=['tables'])})
t=t.replace('__GUIDE__',json.dumps(G,ensure_ascii=False))
(d/'index.html').write_text(t.replace('__PROMPT_EN__',json.dumps(en,ensure_ascii=False)).replace('__PROMPT_ZH__',json.dumps(zh,ensure_ascii=False)))
print('built index.html')
