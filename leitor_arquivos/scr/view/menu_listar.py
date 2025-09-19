import sys
from pathlib import Path
src_path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(src_path))

from scr.controller import controllerListarLayout

def menu_listar():
    print("### Layouts cadastrados ### \n")
    for layout in controllerListarLayout.listar_layouts():
        print(layout)
