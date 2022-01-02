def Y(**B):B['m']==D and A('Slept for 0.5 seconds');sleep(0.5)
def d(i,m):i[B]=200;i[C]=2;m==D and A('Set duration and pitch level to default')
def Z(i,m):c=i[C]-1;not c and m==D and A(f'Lowest level of pitch reached: {i[C]}');i[C]=i[C]-1 if c else i[C];m==D and c and A(f'Decreased pitch to level: {i[C]}')
def a(i,m):c=i[C]+1==17;A(f'Reached highest pitch possible: {i[C]}') if c and m==D else None;i[C]=i[C]+1 if not c else i[C];m==D and not c and A(f'Increased pitch to level: {i[C]}')
def b(i,m):c=i[B]-100<0;A(f'Reached lowest duration possible: {i[B]}ms') if c and m==D else None;i[B]=i[B]-100 if not c else i[B];not c and m==D and A(f'Decreased duration to: {i[B]}ms')
def c(i,m):c=i[B]+100>15000;A(f'Reached highest duration possible: {i[B]}ms') if c and m==D else None;i[B]=i[B]+100 if not c else i[B];not c and m==D and A(f'Increased duration to: {i[B]}ms')
def e(a,m):
 for K in a:L,G=K;m==D and A(f"\nexecuting line {L}: {G}");[J.Beep(H[E]*F[C],F[B])if E in H else E in I and I[E](i=F,m=m)for E in G]
o='>';n='<';m='+';l='!';k=True;j='r';i=FileNotFoundError;h=len;D='debug';C='pitch_level';B='duration';A=print;import winsound as J,argparse as K,os,re;from time import sleep;L=440;M=466;N=494;O=262;P=277;Q=294;R=311;S=330;T=349;U=370;V=392;W=415;X=524;H={'q':O,'a':P,'w':Q,'s':R,'e':S,j:T,'d':U,'u':V,'j':W,'i':L,'k':M,'o':N,'p':X};F={B:200,C:2};G=K.ArgumentParser();G.add_argument('-m','--m',choices=['interpret',D],required=k);G.add_argument('-f','--f',required=k);E=G.parse_args();I={l:Y,'-':Z,m:a,n:b,o:c,':':d}
def f(x):
 if not x:return
 try:
  if not x.endswith('.marble'):A(f"error: invalid file extension '{x[x.index('.'):]}'\nvalid extension: '*.marble'");return
  with open(f"./{x}",j,encoding='utf8')as F:
   G=F.readlines();D=[]
   for (H,C) in enumerate(G,start=1):C=re.sub('[^qweruiopasdjk!:<>\\+-]','',re.match('^[^"]*',C).group());D.append((H,C))if(not '\n'in C or not h(C)==1)and C else None
   e(D,E.m)
 except i:A(f"error: file '{x}' not found in {os.getcwd()}");return
 except ValueError:A(f"error: '{x}' is not recognized as a file");return
 except KeyboardInterrupt:A('error: proccess has been interrupted');return
def g():
 I='"';H='/';D='\\';B=E.f.split(D)if D in E.f else E.f.split(H);not B[-1]and B.pop();F=B[-1];G=[I,'~',l,'@','#','$','%','^','&','*','(','),',m,'{','}',D,I,'|',n,o,'?','`','=','[',']',";",D,H]
 for C in B:
  if any((A in C for A in G)):A(f"error: invalid syntax '{E.f}'");return
 if h(B)!=1:
  for C in B[:-1]:
   try:os.chdir(C)
   except i:A(f"error: directory '{C}' doesn't exist in {os.getcwd()}");return
   except OSError:A(f"error: invalid syntax '{E.f}'");return
 return F
f(g())