"""
Extract clinical resources from WordPress XML export.
Saves to organized folders:
  - clinical-skills/        (23 HTML files: 984-1010-skills-*)
  - diagnostic-reasoning/   (72 HTML files: *-drx-reference-*)
  - minor-ailments/
      community-pharmacy/   (32 HTML files: *-cp-*)
      gp-advice/            (34 HTML files: *-gp-*)
"""

import xml.etree.ElementTree as ET
import re
import os

XML_PATH = r'C:/Users/amjid/Downloads/clinicalreasoningknowledgebase.WordPress.2026-02-28.xml'
BASE_OUT = r'C:/Users/amjid/GitHub/Clinical Reasoning'

FOLDERS = {
    'skills':     os.path.join(BASE_OUT, 'clinical-skills'),
    'drx':        os.path.join(BASE_OUT, 'diagnostic-reasoning'),
    'cp':         os.path.join(BASE_OUT, 'minor-ailments', 'community-pharmacy'),
    'gp':         os.path.join(BASE_OUT, 'minor-ailments', 'gp-advice'),
}

for folder in FOLDERS.values():
    os.makedirs(folder, exist_ok=True)

print("Parsing XML...")
tree = ET.parse(XML_PATH)
root = tree.getroot()

ns = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
}

counts = {'skills': 0, 'drx': 0, 'cp': 0, 'gp': 0, 'skipped': 0}

for item in root.findall('.//item'):
    title_el = item.find('title')
    if title_el is None or not title_el.text:
        counts['skipped'] += 1
        continue

    title = title_el.text.strip()
    content_el = item.find('content:encoded', ns)
    content = content_el.text if content_el is not None else ''

    # Determine category
    if re.match(r'^\d+-skills-', title):
        folder = FOLDERS['skills']
        category = 'skills'
    elif re.search(r'-drx-reference-', title):
        folder = FOLDERS['drx']
        category = 'drx'
    elif re.match(r'^\d+-cp-', title):
        folder = FOLDERS['cp']
        category = 'cp'
    elif re.match(r'^\d+-gp-', title):
        folder = FOLDERS['gp']
        category = 'gp'
    else:
        counts['skipped'] += 1
        continue

    filename = f"{title}.html"
    filepath = os.path.join(folder, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content or '')

    counts[category] += 1
    print(f"  [{category.upper()}] {filename}")

print()
print("=== Extraction complete ===")
print(f"  Clinical skills:      {counts['skills']}")
print(f"  Diagnostic reasoning: {counts['drx']}")
print(f"  Community pharmacy:   {counts['cp']}")
print(f"  GP advice:            {counts['gp']}")
print(f"  Skipped (other):      {counts['skipped']}")
print()
print("Files saved to:")
for k, v in FOLDERS.items():
    print(f"  {v}")
