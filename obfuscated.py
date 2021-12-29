o=True;n='>';m='<';l='+';k='!';j='r';i=FileNotFoundError;h=len;D='debug';C='duration';B='pitch_level';A=print
import argparse as J,os,re,winsound as K;from time import sleep
def L(**B):B['m']==D and A('slept for 0.5 seconds');sleep(0.5)
def M(w,m):
	C=w
	if not C[B]-1:A(f"Lowest level of pitch reached: {C[B]}");return
	C[B]=C[B]-1;m==D and A(f"Decreased pitch to level: {C[B]}")
def N(w,m):
	C=w
	if C[B]+1==17 and m==D:A(f"Reached highest pitch possible: {C[B]}");return
	C[B]=C[B]+1;m==D and A(f"Increased pitch to level: {C[B]}")
def O(w,m):
	B=w
	if B[C]-100<0 and m==D:A(f"Reached lowest duration possible: {B[C]}ms");return
	B[C]=B[C]-100;m==D and A(f"Decreased duration to: {B[C]}ms")
def P(w,m):
	B=w
	if B[C]+100>15000 and m==D:A(f"Reached highest duration possible: {B[C]}ms");return
	B[C]=B[C]+100;m==D and A(f"Increased duration to: {B[C]}ms")
def Q(w,m):w[C]=200;w[B]=2;m==D and A('Set duration and pitch level to default')
F={C:200,B:2};R=440;S=466;T=494;U=262;V=277;W=294;X=311;Y=330;Z=349;a=370;b=392;c=415;d=524;H={'q':U,'a':V,'w':W,'s':X,'e':Y,j:Z,'d':a,'u':b,'j':c,'i':R,'k':S,'o':T,'p':d};I={k:L,'-':M,l:N,m:O,n:P,':':Q}
def e(a,m):
	for J in a:
		L,G=J;m==D and A(f"\nexecuting line {L}: {G}")
		for E in G:
			E in H and K.Beep(H[E]*F[B],F[C])
			E in I and I[E](w=F,m=m)
G=J.ArgumentParser();G.add_argument('-m','--m',choices=['interpret',D],required=o);G.add_argument('-f','--f',required=o);E=G.parse_args()
def f(file_name):
	B=file_name
	if not B:return
	try:
		if not B.endswith('.marble'):A(f"error: invalid file extension '{B[B.index('.'):]}'\nvalid extension: '*.marble'");return
		with open(f"./{B}",j,encoding='utf8')as F:
			G=F.readlines();D=[]
			for (H,C) in enumerate(G,start=1):
				C=re.sub('[^qweruiopasdjk!:<>\\+-]','',re.match('^[^"]*',C).group())
				if h(C)==1 and'\n'in C or not C:continue
				D.append((H,C))
			e(D,E.m)
	except i:A(f"error: file '{B}' not found in {os.getcwd()}");return
	except ValueError:A(f"error: '{B}' is not recognized as a file");return
	except KeyboardInterrupt:A('error: proccess has been interrupted');return
def g():
	I='"';H='/';D='\\';B=E.f.split(D)if D in E.f else E.f.split(H);not B[-1] and B.pop();F=B[-1];G=[I,'~',k,'@','#','$','%','^','&','*','(','),',l,'{','}',D,I,'|',m,n,'?','`','=','[',']',";'",D,H]
	for C in B:
		if any((A in C for A in G)):A(f"error: invalid syntax '{E.f}'");return
	if h(B)!=1:
		for C in B[:-1]:
			try:os.chdir(C)
			except i:A(f"error: directory '{C}' doesn't exist in {os.getcwd()}");return
			except OSError:A(f"error: invalid syntax '{E.file}'");return
	return F
f(g())
