import json,pathlib
d=pathlib.Path(__file__).parent
t=(d/'index.template.html').read_text()
en=(d/'prompts/rubric-prompt.en.md').read_text(); zh=(d/'prompts/rubric-prompt.zh.md').read_text()
(d/'index.html').write_text(t.replace('__PROMPT_EN__',json.dumps(en,ensure_ascii=False)).replace('__PROMPT_ZH__',json.dumps(zh,ensure_ascii=False)))
print('built index.html')
