def V(t):J(t);return F
def W(**B):B['m']==D and A('Slept for 0.5 seconds');sleep(0.5)
def X(i,m):i[C]=200;i[B]=2;m==D and A('Set duration and pitch level to default')
def Y(i,m):C=i[B]-1;not C and m==D and A(f"Lowest level of pitch reached: {i[B]}");i[B]=i[B]-1 if C else i[B];m==D and C and A(f"Decreased pitch to level: {i[B]}")
def Z(i,m):C=i[B]+1==17;A(f"Reached highest pitch possible: {i[B]}")if C and m==D else G;i[B]=i[B]+1 if not C else i[B];m==D and not C and A(f"Increased pitch to level: {i[B]}")
def a(i,m):B=i[C]-100<0;A(f"Reached lowest duration possible: {i[C]}ms")if B and m==D else G;i[C]=i[C]-100 if not B else i[C];not B and m==D and A(f"Decreased duration to: {i[C]}ms")
def b(i,m):B=i[C]+100>15000;A(f"Reached highest duration possible: {i[C]}ms")if B and m==D else G;i[C]=i[C]+100 if not B else i[C];not B and m==D and A(f"Increased duration to: {i[C]}ms")
def c(a,m):
	for F in a:G,E=F;m==D and A(f"\nexecuting line {G}: {E}");[d.Beep(S[A]*H[B],H[C])if A in S else A in T and T[A](i=H,m=m)for A in E]
def U(H,B,G,Q,F,C):
	for (H,B) in enumerate(G,start=1):B=re.sub('[^qweruiopasdjk!:<>\\+-]','',re.match('^[^"]*',B).group());C.append((H,B))if(not'\n'in B or not Q(B)==1)and B else F
J=print;F=None;G=F;K='>';L='<';M='+';N='!';O=True;P='r';Q=FileNotFoundError;R=len;D='debug';B='pitch_level';C='duration';A=J;import winsound as d,argparse as e,os,re;from time import sleep;f=440;g=466;h=494;i=262;j=277;k=294;l=311;m=330;n=349;o=370;p=392;q=415;r=524;S={'q':i,'a':j,'w':k,'s':l,'e':m,P:n,'d':o,'u':p,'j':q,'i':f,'k':g,'o':h,'p':r};H={C:200,B:2};I=e.ArgumentParser();I.add_argument('-m','--m',choices=['interpret',D],required=O);I.add_argument('-f','--f',required=O);E=I.parse_args();T={N:W,'-':Y,M:Z,L:a,K:b,':':X}
def s(x):
	if not x:return
	try:
		if not x.endswith('.marble'):A(f"error: invalid file extension '{x[x.index('.'):]}'\nvalid extension: '*.marble'");return
		with open(f"./{x}",P,encoding='utf8')as D:F=D.readlines();C=[];U(H,B,F,R,G,C);c(C,E.m)
	except Q:A(f"error: file '{x}' not found in {os.getcwd()}");return
	except ValueError:A(f"error: '{x}' is not recognized as a file");return
	except KeyboardInterrupt:A('error: proccess has been interrupted');return
def t():
	D='"';G='/';C='\\';B=E.f.split(C)if C in E.f else E.f.split(G);not B[-1]and B.pop();J=B[-1];O=[D,'~',N,'@','#','$','%','^','&','*','(','),',M,'{','}',C,D,'|',L,K,'?','`','=','[',']',";'",C,G];H=[V(f"error: invalid syntax '{E.f}'")for A in B if any((B in A for B in O))]
	if R(B)!=1 and F not in H:
		for I in B[:-1]:
			try:os.chdir(I)
			except Q:A(f"error: directory '{I}' doesn't exist in {os.getcwd()}");return
			except OSError:A(f"error: invalid syntax '{E.f}'");return
	return J if F not in H else F
s(t())