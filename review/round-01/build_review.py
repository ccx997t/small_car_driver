from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, Circle
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
P=Path(__file__).resolve().parent
font=font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')
plt.rcParams.update({'font.family':font.get_name(),'axes.unicode_minus':False,'font.size':11})
C={'fixed':'#4387af','new':'#81b6b2','old':'#41494f','spring':'#e6b948','wheel':'#e48c38'}
def box(ax,x,y,z,a,b,c,color,alpha=1):
 v=np.array([[x,y,z],[x+a,y,z],[x+a,y+b,z],[x,y+b,z],[x,y,z+c],[x+a,y,z+c],[x+a,y+b,z+c],[x,y+b,z+c]])
 faces=[[v[j] for j in f] for f in [[0,1,2,3],[4,5,6,7],[0,1,5,4],[1,2,6,5],[2,3,7,6],[3,0,4,7]]]
 ax.add_collection3d(Poly3DCollection(faces,facecolors=color,edgecolors='#33434c',linewidths=.5,alpha=alpha))
def spring(ax,x,y,z0,z1):
 t=np.linspace(0,12*np.pi,350);ax.plot(x+7*np.cos(t),y+7*np.sin(t),np.linspace(z0,z1,len(t)),color=C['spring'],lw=2)
def title(fig,t,sub):
 fig.suptitle(t,x=.05,ha='left',fontsize=22,fontweight='bold');fig.text(.05,.91,sub,color='#56636e',fontsize=11)
 fig.text(.05,.025,'R01 · 2026-11-14  |  概念布局；无实测尺寸；非加工图／非承载结论',color='#56636e')
with PdfPages(P/'第一轮方案评审.pdf') as pdf:
 fig=plt.figure(figsize=(15,9),facecolor='white');title(fig,'01 / 总体结构意向','蓝：底盘固定端   绿：新增活动件   深灰：已有组件包络   黄：弹簧   橙：轮胎')
 ax=fig.add_axes([.02,.13,.65,.73],projection='3d')
 # Arbitrary layout coordinates, intentionally not manufacturing dimensions.
 box(ax,-100,-70,220,200,140,12,C['fixed'],.2)
 for x in [-75,75]:
  box(ax,x-13,-18,65,26,36,145,C['fixed'],.7)
  ax.plot([x,x],[0,0],[70,210],color='#97a1aa',lw=4)
  spring(ax,x,0,144,202)
  box(ax,x-16,-22,116,32,44,27,C['new'])
 box(ax,-92,-20,102,184,40,14,C['new'])
 box(ax,-62,-18,82,124,36,16,C['old'])
 box(ax,-42,-85,60,84,55,48,C['old'])
 t=np.linspace(0,2*np.pi,75);yy=np.linspace(8,42,2);T,Y=np.meshgrid(t,yy)
 ax.plot_surface(57*np.cos(T),Y,62+57*np.sin(T),color=C['wheel'],alpha=.95)
 ax.plot_surface(22*np.cos(T),Y-2,62+22*np.sin(T),color='#67727b')
 ax.set(xlim=(-115,115),ylim=(-110,85),zlim=(0,245));ax.set_box_aspect((230,195,245));ax.view_init(23,-57);ax.set_axis_off()
 fig.text(.7,.78,'推荐：双弹簧＋直线导向',fontsize=16,fontweight='bold')
 fig.text(.7,.70,'① 局部底盘与固定框架\n\n② 双侧导向与弹簧\n\n③ 新增活动过渡件\n\n④ 已有黑色架／电机／轮组件',linespacing=1.5,va='top')
 fig.text(.7,.30,'深灰件仅为位置包络，非安装架复刻。\n新增件优先适配已有接口；\n不能据此决定钻孔或更改原件。\n\n轮轴方向、架体姿态、安装空间待核实。',fontsize=11,linespacing=1.6)
 fig.savefig(P/'01_总体结构意向.png',dpi=160);fig.savefig(P/'01_总体结构意向.svg');pdf.savefig(fig);plt.close(fig)
 fig,axs=plt.subplots(1,2,figsize=(15,9));title(fig,'02 / 运动关系与接口约束','左：沿轮轴看模块的功能示意；右：黑色安装架照片中的可见特征')
 ax=axs[0];ax.set_xlim(-125,125);ax.set_ylim(-15,265);ax.set_aspect('equal');ax.axis('off')
 ax.add_patch(Rectangle((-110,225),220,12,color=C['fixed'],alpha=.5));ax.text(0,245,'局部底盘 / 固定端',ha='center')
 ax.add_patch(Circle((0,65),57,color=C['wheel'],alpha=.8));ax.add_patch(Circle((0,65),20,color=C['old']))
 for x in [-80,80]:
  ax.plot([x,x],[80,225],color=C['fixed'],lw=4)
  ax.add_patch(Rectangle((x-12,125),24,22,color=C['new']))
  yy=np.linspace(150,215,100);xx=x+8*np.sin(np.linspace(0,12*np.pi,100));ax.plot(xx,yy,color=C['spring'],lw=2)
  ax.plot([x-17,x+17],[218,218],color=C['fixed'],lw=3)
  ax.plot([x-15,x+15],[150,150],color=C['new'],lw=3)
  ax.plot([x-13,x+13],[95,95],color=C['fixed'],lw=3)
 ax.add_patch(Rectangle((-94,111),188,14,color=C['new']));ax.add_patch(Rectangle((-57,94),114,17,color=C['old']))
 ax.annotate('',xy=(112,165),xytext=(112,110),arrowprops=dict(arrowstyle='<->',color='#386583',lw=2));ax.text(115,139,'上下\n运动',fontsize=10)
 ax.text(0,20,'轮／电机／已有架：建议整体随动',ha='center',fontsize=10)
 ax.text(0,-8,'导向约束侧向及力矩；弹簧提供竖向弹性\n限位须独立设置，图中位置仅作意向',ha='center',fontsize=10)
 ax=axs[1];ax.axis('off');im=plt.imread(P/'references/31794630548_.pic.jpg');ax.imshow(im)
 for xy,txt in [((800,490),'A 中央圆形接口'),((940,565),'B 周边孔位'),((515,470),'C 端部开口')]:
  ax.annotate(txt,xy=xy,xytext=(40,120+(['A','B','C'].index(txt[0]))*105),color='white',fontsize=12,bbox=dict(facecolor='#263844',alpha=.9),arrowprops=dict(arrowstyle='->',color='#e6b948',lw=2))
 ax.set_title('保留：主体、中央接口、孔位、端部开口\n用途、尺寸及受力能力均待核实',fontsize=12)
 fig.subplots_adjust(top=.84,bottom=.13,wspace=.2);fig.savefig(P/'02_运动与安装架约束.png',dpi=160);pdf.savefig(fig);plt.close(fig)
print('Created PNG / SVG / two-page PDF')
