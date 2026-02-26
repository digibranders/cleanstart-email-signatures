import os
import glob

directory = '/Users/siddiqueahmed/Desktop/AI/cleanstart email signatures'
html_files = glob.glob(os.path.join(directory, '*.html'))

old_target = '<td width="1" bgcolor="#000000" style="background-color: #000000; width: 1px; min-width: 1px; padding: 0; font-size: 1px; line-height: 1px;"></td>'

# The absolute most bulletproof version handles empty cell collapse in Outlook/Yahoo by adding &nbsp; and mso-line-height-rule
new_target = '<td width="1" bgcolor="#000000" style="background-color: #000000; width: 1px; min-width: 1px; padding: 0; font-size: 1px; line-height: 1px; mso-line-height-rule: exactly;">&nbsp;</td>'

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_target in content:
        content = content.replace(old_target, new_target)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated {count} files to be 100% bulletproof")
