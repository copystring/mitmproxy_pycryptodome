# -*- mode: python ; coding: utf-8 -*-

for tool in ["mitmproxy", "mitmdump", "mitmweb"]:
    excludes = []
    if tool != "mitmweb":
        excludes.append("mitmproxy.tools.web")
    if tool != "mitmproxy":
        excludes.append("mitmproxy.tools.console")

    a = Analysis(
        [tool],
        excludes=excludes,
		hiddenimports=['Cryptodome']
    )
    pyz = PYZ(a.pure, a.zipped_data)

    EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        [],
        name=tool,
        console=True,
        icon='icon.ico',
    )
