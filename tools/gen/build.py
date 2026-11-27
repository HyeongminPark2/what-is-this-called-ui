import sys, pathlib, importlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from tmpl import page
OUT = HERE.parent.parent / "items"
for name in sys.argv[1:]:
    mod = importlib.import_module("d_" + name)
    html = page(mod.D)
    (OUT / (mod.D["slug"] + ".html")).write_text(html)
    print(mod.D["slug"] + ".html", len(html.splitlines()), "lines")
