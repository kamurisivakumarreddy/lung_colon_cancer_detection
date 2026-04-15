import zipfile, json, shutil, re

src = r'C:\Users\sivak\Downloads\final_combined_model.keras'
dst = r'C:\Users\sivak\Downloads\fixed_model.keras'

shutil.copy(src, dst)

# Read config
with zipfile.ZipFile(dst, 'r') as z:
    config_str = z.read('config.json').decode('utf-8')

# Remove quantization_config entries
config_str = re.sub(r',\s*"quantization_config":\s*null', '', config_str)
config_str = re.sub(r'"quantization_config":\s*null,\s*', '', config_str)

# Write back
with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
    with zipfile.ZipFile(src, 'r') as zin:
        for item in zin.infolist():
            if item.filename == 'config.json':
                zout.writestr(item, config_str)
            else:
                zout.writestr(item, zin.read(item.filename))

print('Done! fixed_model.keras saved to Downloads')
