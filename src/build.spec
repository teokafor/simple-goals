# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('roboto-light.ttf','resources\\roboto-light.ttf', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          exclude_binaries=False,
          name='simple-goals',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)
