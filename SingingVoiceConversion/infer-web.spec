# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

datas = [('fairseq','.')]
datas += collect_data_files('gradio_client')
datas += collect_data_files('gradio')

a = Analysis(
    ['infer-web.py'],
    pathex=['E:\Retrieval-based-Voice-Conversion-WebUI-main',
            'E:\ANACONDA\envs\RVC\Library\bin'],
    binaries=[],
    datas=datas,
    hiddenimports=['numpy','fairseq'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    module_collection_mode={'fairseq': 'py', 'gradio': 'py',}
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='infer-web',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='infer-web',
)
