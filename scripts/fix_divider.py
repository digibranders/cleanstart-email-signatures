import os
import glob

directory = '/Users/siddiqueahmed/Desktop/AI/cleanstart email signatures'
html_files = glob.glob(os.path.join(directory, '*.html'))

old_target = '<td width="1" style="border-left: 1px solid #000000; padding: 0; font-size: 0; line-height: 0;">&nbsp;</td>'

# Advanced robust vertical divider for email clients
new_target = '<td width="1" bgcolor="#000000" style="background-color: #000000; width: 1px; min-width: 1px; padding: 0; font-size: 1px; line-height: 1px;"></td>'

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We should handle potential whitespace differences like linebreaks, though the grep showed exactly the string in one line
    if old_target in content:
        content = content.replace(old_target, new_target)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")
        count += 1
    else:
        # try a regex or whitespace agnostic replace
        import re
        old_pattern = re.compile(r'<td\s+width="1"\s+style="border-left:\s*1px\s+solid\s+#000000;\s*padding:\s*0;\s*font-size:\s*0;\s*line-height:\s*0;">&nbsp;</td>')
        if old_pattern.search(content):
            content = old_pattern.sub(new_target, content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {os.path.basename(file_path)} (via regex)")
            count += 1

print(f"Total files updated: {count}")
