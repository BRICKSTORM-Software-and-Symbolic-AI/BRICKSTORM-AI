import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon, Ellipse, Circle
import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","assets","diagrams")+os.sep
G="#d9f0d3"; B="#cfe2f3"; Y="#fff2b3"; O="#ffe6c9"; R="#f4c7c3"; P="#e6dcf2"; E="#333333"
def fig(w,h,title):
    f,ax=plt.subplots(figsize=(w,h),dpi=100); ax.set_xlim(0,w); ax.set_ylim(-0.5,h); ax.axis("off")
    if title: ax.text(0.25,h-0.45,title,fontsize=17,fontweight="bold",va="center")
    return f,ax
def box(ax,x,y,w,h,t,c=B,fs=12,bold=False):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=0.02,rounding_size=0.08",fc=c,ec=E,lw=2))
    ax.text(x,y,t,ha="center",va="center",fontsize=fs,fontweight="bold" if bold else "normal")
def diamond(ax,x,y,w,h,t,c=Y,fs=11):
    ax.add_patch(Polygon([(x-w/2,y),(x,y+h/2),(x+w/2,y),(x,y-h/2)],closed=True,fc=c,ec=E,lw=2))
    ax.text(x,y,t,ha="center",va="center",fontsize=fs)
def oval(ax,x,y,w,h,t,c=G,fs=12):
    ax.add_patch(Ellipse((x,y),w,h,fc=c,ec=E,lw=2)); ax.text(x,y,t,ha="center",va="center",fontsize=fs)
def arr(ax,x1,y1,x2,y2,lab=None,rad=0,fs=11,ls="-",lw=2.2,lc="#555"):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=20,color=E,lw=lw,linestyle=ls,connectionstyle=f"arc3,rad={rad}"))
    if lab: ax.text((x1+x2)/2+0.1,(y1+y2)/2+0.12,lab,fontsize=fs,color=lc)
def line(ax,x1,y1,x2,y2,lw=2.2,ls="-",c=E): ax.plot([x1,x2],[y1,y2],color=c,lw=lw,ls=ls,zorder=0)
def save(f,n): f.savefig(OUT+n,bbox_inches="tight",facecolor="white"); plt.close(f); print(n)

# 01 software layers
f,ax=fig(11,6.4,"Layers of a computer system")
layers=[("User",O,"you: clicking, typing, touching"),("Application software",B,"Weixin, Chrome, Word, games"),
("Operating system + drivers (system software)",Y,"Windows, macOS, Linux, Android, iOS"),("Hardware",G,"CPU, RAM, storage, screen, keyboard")]
for i,(t,c,ex) in enumerate(layers):
    y=4.9-i*1.25; box(ax,3.9,y,7.0,0.95,t,c,13,True); ax.text(7.7,y,ex,fontsize=11.5,va="center",color="#333")
    if i<3:
        arr(ax,3.0,y-0.5,3.0,y-0.78); arr(ax,4.8,y-0.78,4.8,y-0.5)
ax.text(1.0,0.2,"Down arrows = requests (e.g. \"open this file\")    Up arrows = results",fontsize=11.5)
save(f,"software-layers.png")

# 02 compiler vs interpreter
f,ax=fig(12,6,"Compiler vs interpreter")
ax.text(0.3,4.9,"Compiler",fontsize=14,fontweight="bold")
box(ax,1.6,4.0,2.4,1.0,"Source code\n(whole program)",O,11)
box(ax,4.6,4.0,2.0,1.0,"Compiler",Y,12,True)
box(ax,7.6,4.0,2.4,1.0,"Machine-code\nfile (.exe)",B,11)
box(ax,10.5,4.0,2.2,1.0,"CPU runs it\n(any time later)",G,11)
arr(ax,2.8,4,3.6,4); arr(ax,5.6,4,6.4,4); arr(ax,8.8,4,9.4,4)
ax.text(3.6,3.15,"Step 1: translate everything once",fontsize=11,color="#555"); ax.text(8.0,3.15,"Step 2: run",fontsize=11,color="#555")
ax.text(0.3,2.2,"Interpreter",fontsize=14,fontweight="bold")
box(ax,1.6,1.2,2.4,1.0,"Source code",O,11)
box(ax,5.4,1.2,3.4,1.0,"Interpreter: read one\nstatement → run it",Y,11)
box(ax,9.8,1.2,3.0,1.0,"Output appears as\neach line runs",G,11)
arr(ax,2.8,1.2,3.7,1.2); arr(ax,7.1,1.2,8.3,1.2)
arr(ax,6.4,0.68,4.4,0.68,rad=-0.6); ax.text(4.5,-0.35,"repeat for the next statement",fontsize=11,color="#555")
save(f,"compiler-vs-interpreter.png")

# 03 waterfall vs agile
f,ax=fig(13.5,6.3,"Two process models")
ax.text(0.3,5.2,"Waterfall: each stage once, in order",fontsize=13,fontweight="bold")
st=["Requirements","Design","Coding","Testing","Deployment","Maintenance"]
for i,s in enumerate(st):
    x=1.1+i*0.95; y=4.4-i*0.7; box(ax,x+0.4,y,1.75,0.5,s,B,10)
    if i<5: arr(ax,x+1.27,y,x+1.35,y-0.45,rad=-0.4)
ax.text(7.3,5.2,"Agile: repeat a short cycle (sprint)",fontsize=13,fontweight="bold")
cx,cy,r=9.6,2.85,1.55
import math
names=["Plan","Design","Build","Test","Review\nwith users"]
pts=[]
for i,n in enumerate(names):
    a=math.pi/2-i*2*math.pi/5; pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
for i,(x,y) in enumerate(pts):
    x2,y2=pts[(i+1)%5]; arr(ax,x,y,x2,y2,rad=-0.25)
for (x,y),n in zip(pts,names): box(ax,x,y,1.45,0.62,n,Y,10.5)
ax.text(cx,cy,"1–4\nweeks",ha="center",va="center",fontsize=11,color="#555")
box(ax,12.6,2.85,1.3,0.7,"v1, v2,\nv3 …",G,10)
arr(ax,11.0,2.75,11.9,2.85)
ax.text(7.3,0.45,"Each cycle delivers a small working version.",fontsize=11,color="#333")
save(f,"waterfall-vs-agile.png")

# 04 database relationship
f,ax=fig(12.5,5.6,"Three linked tables")
def table(x,y,title,rows,key_rows,w=3.2,c=B):
    box(ax,x,y,w,0.55,title,c,12,True)
    for i,r in enumerate(rows):
        yy=y-0.55*(i+1)
        ax.add_patch(FancyBboxPatch((x-w/2,yy-0.275),w,0.55,boxstyle="square,pad=0",fc="white",ec=E,lw=1.2))
        ax.text(x-w/2+0.12,yy,r,va="center",fontsize=10.5,fontweight="bold" if i in key_rows else "normal")
table(1.9,4.4,"Students",["student_id  (PK)","name","major","year","gpa"],[0])
table(6.25,4.4,"Enrolments",["student_id  (FK)","course_id  (FK)"],[0,1],c=Y)
table(10.6,4.4,"Courses",["course_id  (PK)","title","credits"],[0])
arr(ax,4.65,3.85,3.5,3.85,lab=None); ax.text(3.6,3.35,"refers to",fontsize=10.5,color="#555")
arr(ax,7.85,3.3,9.0,3.85); ax.text(8.0,3.2,"refers to",fontsize=10.5,color="#555")
ax.text(0.3,0.5,"PK = primary key (unique for each row)    FK = foreign key (holds a primary key from another table)",fontsize=11)
ax.text(0.3,0.05,"Example: Enrolments row (104, CS101) means Dana takes Foundations of CS & AI.",fontsize=11,color="#333")
save(f,"database-relationship.png")

# 05 linear search flowchart
f,ax=fig(9,10.5,"Linear search as a flowchart")
oval(ax,4,9.4,2.4,0.8,"Start")
box(ax,4,8.2,3.6,0.8,"i = 0  (first position)",B,12)
diamond(ax,4,6.75,3.8,1.4,"Is i past the\nend of the list?",Y,11.5)
diamond(ax,4,4.85,3.8,1.4,"Is item[i] =\ntarget?",Y,11.5)
box(ax,4,3.2,3.6,0.8,"i = i + 1  (next item)",B,12)
oval(ax,8.0,6.75,1.9,0.9,"Stop:\nnot found",R,11)
oval(ax,8.0,4.85,1.9,0.9,"Stop:\nfound at i",G,11)
arr(ax,4,9.0,4,8.6); arr(ax,4,7.8,4,7.45); arr(ax,4,6.05,4,5.55,"No"); arr(ax,4,4.15,4,3.6,"No")
arr(ax,5.9,6.75,7.05,6.75,"Yes"); arr(ax,5.9,4.85,7.05,4.85,"Yes")
line(ax,2.2,3.2,1.0,3.2); line(ax,1.0,3.2,1.0,6.75); arr(ax,1.0,6.75,2.1,6.75)
ax.text(0.2,1.9,"Oval = start/stop   Rectangle = process step\nDiamond = decision   Arrow = order of steps",fontsize=11.5)
save(f,"linear-search-flowchart.png")

# 06 linked list
f,ax=fig(12,4.6,"A linked list: inserting \"Cara\"")
ax.text(0.3,3.55,"Before",fontsize=12,fontweight="bold")
xs=[1.6,4.2,6.8]; names=["Ann","Bo","Dan"]
def node(x,y,n,c=B):
    box(ax,x,y,1.3,0.7,n,c,12); box(ax,x+0.95,y,0.6,0.7,"•",Y,14)
for x,n in zip(xs,names): node(x,2.95,n)
arr(ax,2.55,2.95,3.5,2.95); arr(ax,5.15,2.95,6.1,2.95); arr(ax,7.75,2.95,8.6,2.95); ax.text(8.7,2.9,"end (null)",fontsize=11)
ax.text(0.3,1.6,"After",fontsize=12,fontweight="bold")
xs2=[1.6,4.2,6.8,9.4]; n2=["Ann","Bo","Cara","Dan"]
for x,n in zip(xs2,n2): node(x,1.0,n,G if n=="Cara" else B)
for x in xs2[:3]: arr(ax,x+1.25,1.0,x+1.9,1.0,lw=3 if x in(4.2,6.8) else 2.2)
ax.text(4.3,0.2,"Only two links change: Bo → Cara and Cara → Dan.  Nothing shifts.",fontsize=11.5)
ax.text(0.3,0.0+3.95-0.0,"",fontsize=1)
save(f,"linked-list.png")

# 06 stack and queue
f,ax=fig(12,6.4,"Stack (LIFO) and queue (FIFO)")
ax.text(0.5,5.3,"Stack",fontsize=14,fontweight="bold")
for i,t in enumerate(["Home","News","Sports"]): box(ax,2.4,1.2+i*0.95,2.2,0.8,t,B if i<2 else O,12)
ax.text(3.65,3.1,"← top",fontsize=12)
arr(ax,0.9,4.6,1.9,3.7); ax.text(0.2,4.75,"push",fontsize=12)
arr(ax,2.9,3.7,3.9,4.6); ax.text(3.8,4.75,"pop",fontsize=12)
ax.text(0.6,0.35,"Add and remove at the same end",fontsize=11.5)
ax.text(6.3,5.3,"Queue",fontsize=14,fontweight="bold")
for i,t in enumerate(["A","B","C"]): box(ax,7.6+i*1.4,3.0,1.2,0.9,t,B if i else O,13)
arr(ax,11.9,3.0,10.9,3.0); ax.text(11.2,3.55,"enqueue\n(back)",fontsize=11.5)
arr(ax,6.9,3.0,6.0,3.0); ax.text(5.7,3.55,"dequeue\n(front)",fontsize=11.5)
ax.text(6.3,1.9,"Add at the back, remove from the front",fontsize=11.5)
ax.text(6.3,1.3,"Printer prints A, then B, then C",fontsize=11.5,color="#555")
save(f,"stack-and-queue.png")

# 06 BST
f,ax=fig(10,5.6,"Binary search tree")
pos={50:(5,4.3),30:(2.8,2.9),70:(7.2,2.9),20:(1.6,1.4),40:(4.0,1.4),60:(6.0,1.4),80:(8.4,1.4)}
for a,b in [(50,30),(50,70),(30,20),(30,40),(70,60),(70,80)]:
    line(ax,*pos[a],*pos[b],lw=2.5 if (a,b) in [(50,70),(70,60)] else 2.2, c="#c0392b" if (a,b) in [(50,70),(70,60)] else E)
for k,(x,y) in pos.items():
    ax.add_patch(Circle((x,y),0.45,fc=O if k in(50,70,60) else B,ec=E,lw=2,zorder=3)); ax.text(x,y,str(k),ha="center",va="center",fontsize=13,zorder=4)
ax.text(5.6,4.5,"root",fontsize=11,color="#555")
ax.text(0.3,0.3,"Left child < parent < right child.   Orange/red path: search for 60 (50 → 70 → 60).",fontsize=11.5)
save(f,"binary-search-tree.png")

# 07 animal tree
f,ax=fig(13,7.2,"Animal-guessing decision tree")
diamond(ax,6,5.8,3.4,1.2,"Has feathers?")
diamond(ax,3,3.9,3.0,1.1,"Can fly?")
diamond(ax,9,3.9,3.0,1.1,"Has fur?")
box(ax,1.5,1.9,2.0,0.8,"Eagle (R1)",G,12); box(ax,4.3,1.9,2.2,0.8,"Penguin (R2)",G,12)
box(ax,7.4,1.9,1.9,0.8,"Dog (R3)",G,12)
diamond(ax,10.4,1.9,2.6,1.0,"Has fins?",Y,11)
box(ax,9.2,0.25,2.1,0.7,"Shark (R4)",G,11.5); box(ax,11.7,0.25,2.4,0.7,"Unknown animal",R,10.5)
arr(ax,4.6,5.5,3.4,4.45,"yes"); arr(ax,7.4,5.5,8.6,4.45,"no")
arr(ax,2.4,3.4,1.7,2.3,"yes"); arr(ax,3.6,3.4,4.1,2.3,"no")
arr(ax,8.4,3.4,7.6,2.3,"yes"); arr(ax,9.6,3.4,10.1,2.4,"no")
arr(ax,9.9,1.45,9.4,0.6,"yes"); arr(ax,10.9,1.45,11.3,0.6,"no")
save(f,"animal-guessing-tree.png")

# 11 map
f,ax=fig(9,5.6,"Map: start A, goal F")
P={"A":(1,2.5),"B":(3.3,4.0),"C":(3.3,1.0),"D":(5.7,2.5),"E":(5.7,0.4),"F":(8,2.0)}
for a,b in [("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","F"),("E","F")]: line(ax,*P[a],*P[b],lw=2.5)
for k,(x,y) in P.items():
    ax.add_patch(Circle((x,y),0.42,fc=G if k=="A" else (O if k=="F" else B),ec=E,lw=2,zorder=3)); ax.text(x,y,k,ha="center",va="center",fontsize=15,fontweight="bold",zorder=4)
ax.text(0.3,4.7,"green = start, orange = goal; every road takes one step",fontsize=11)
save(f,"search-map.png")

# 11 bfs vs dfs trees
f,ax=fig(13,6.4,"Search trees: BFS (level by level) vs DFS (deep first)")
def tnode(x,y,t,n,c=B):
    ax.add_patch(Circle((x,y),0.38,fc=c,ec=E,lw=2,zorder=3)); ax.text(x,y,t,ha="center",va="center",fontsize=13,fontweight="bold",zorder=4)
    ax.text(x+0.42,y+0.3,str(n),fontsize=10,color="#c0392b",zorder=4)
ax.text(0.3,5.3,"BFS: path A→B→D→F (3 roads)",fontsize=12.5,fontweight="bold")
bp={"A":(3,4.4),"B":(1.6,3.0),"C":(4.4,3.0),"D":(1.6,1.6),"E":(4.4,1.6),"F":(1.6,0.3)}
for a,b in [("A","B"),("A","C"),("B","D"),("C","E"),("D","F")]: line(ax,*bp[a],*bp[b],lw=3 if (a,b) in[("A","B"),("B","D"),("D","F")] else 2, c="#c0392b" if (a,b) in[("A","B"),("B","D"),("D","F")] else E)
for i,k in enumerate("ABCDEF"): tnode(*bp[k],k,i+1,O if k=="F" else (G if k=="A" else B))
ax.text(5.4,4.4,"level 0",fontsize=10.5,color="#555"); ax.text(5.4,3.0,"level 1",fontsize=10.5,color="#555"); ax.text(5.4,1.6,"level 2",fontsize=10.5,color="#555"); ax.text(5.4,0.3,"level 3",fontsize=10.5,color="#555")
ax.text(7.0,5.3,"DFS: path A→B→D→C→E→F (5 roads)",fontsize=12.5,fontweight="bold")
dp={"A":(8,4.6),"B":(8.9,3.8),"D":(9.8,3.0),"C":(10.7,2.2),"E":(11.6,1.4),"F":(12.5,0.6)}
for a,b in [("A","B"),("B","D"),("D","C"),("C","E"),("E","F")]: line(ax,*dp[a],*dp[b],lw=3,c="#c0392b")
for i,k in enumerate("ABDCEF"): tnode(*dp[k],k,i+1,O if k=="F" else (G if k=="A" else B))
ax.text(7.0,-0.3,"Small red numbers = order visited",fontsize=11)
save(f,"bfs-vs-dfs.png")

# 12 parse tree
f,ax=fig(8,6,"Parse tree: \"The cat sat\"")
N={"S":(4,4.8,"S","G1"),"NP":(2.3,3.5,"NP","G2"),"VP":(5.7,3.5,"VP","G3"),"Det":(1.4,2.2,"Det",""),"N":(3.2,2.2,"N",""),"V":(5.7,2.2,"V",""),
"w1":(1.4,0.9,"The",""),"w2":(3.2,0.9,"cat",""),"w3":(5.7,0.9,"sat","")}
for a,b in [("S","NP"),("S","VP"),("NP","Det"),("NP","N"),("VP","V"),("Det","w1"),("N","w2"),("V","w3")]: line(ax,N[a][0],N[a][1],N[b][0],N[b][1])
for k,(x,y,t,r) in N.items():
    c=G if k.startswith("w") else (Y if k in("Det","N","V") else B)
    box(ax,x,y,1.2,0.6,t,c,13,not k.startswith("w"))
    if r: ax.text(x+0.7,y+0.15,r,fontsize=10.5,color="#c0392b")
ax.text(0.2,0.05,"blue = phrases, yellow = word tags (lexicon), green = words; red = rule used",fontsize=10.5)
save(f,"parse-tree.png")

# 13 study chain
f,ax=fig(12,4.8,"Forward chaining: study-method advisor")
box(ax,1.9,3.5,3.2,0.8,"F1: exam is more than\n3 days away",G,10.5)
box(ax,1.9,2.3,3.2,0.7,"F2: topic is new",G,11)
box(ax,1.9,0.8,3.2,0.7,"F3: learner likes diagrams",G,10.5)
box(ax,4.5,2.9,0.9,0.6,"R1",Y,13); box(ax,6.7,2.9,2.6,0.9,"F4: plan:\nspaced study",B,11)
box(ax,8.6,1.6,0.9,0.6,"R4",Y,13); box(ax,10.6,1.6,2.6,1.1,"F5: advice: make a\nconcept map over\nseveral sessions",B,10.5)
arr(ax,3.5,3.4,4.05,3.0); arr(ax,3.5,2.35,4.05,2.8); arr(ax,4.95,2.9,5.4,2.9)
arr(ax,7.4,2.45,8.2,1.85); arr(ax,3.5,0.8,8.15,1.45,rad=0.1); arr(ax,9.05,1.6,9.3,1.6)
ax.text(0.3,-0.2,"Green = starting facts   Blue = new facts   Yellow = rule that fired",fontsize=11)
save(f,"study-advisor-chain.png")
