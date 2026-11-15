from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
P=Path(__file__).resolve().parent
parts=json.loads((P/'preview_mesh.json').read_text())
for name,elev,azim in [('isometric',22,-58),('rear',22,120)]:
 fig=plt.figure(figsize=(12,10),facecolor='white');ax=fig.add_subplot(111,projection='3d')
 for p in parts:
  verts=p['vertices'];polys=[[verts[i] for i in t] for t in p['triangles']]
  ax.add_collection3d(Poly3DCollection(polys,facecolor=p['color'],edgecolor='none',alpha=.20 if p['name']=='Chassis' else 1))
 ax.set(xlim=(-165,165),ylim=(-155,90),zlim=(0,305));ax.set_box_aspect((330,245,305));ax.view_init(elev,azim);ax.set_axis_off()
 fig.suptitle('Drive module / R01 concept',fontsize=22,x=.08,ha='left');fig.text(.08,.89,'Actual FreeCAD geometry | nominal dimensions | interfaces unverified',fontsize=11,color='#52616c')
 fig.text(.08,.05,'Blue: fixed frame   Green: moving adapter   Grey: existing component approximation\nYellow: springs   Orange: wheel   |   Not for manufacturing',fontsize=11,color='#52616c')
 fig.savefig(P/(name+'.png'),dpi=150);plt.close(fig)
