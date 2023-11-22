if(list(reversed(list(str(x)))) == list(str(x))):
return True
else:
return False
위 형식으로도 가능함
x를 리스트로 만들어 뒤집고 리스트로 만든다. 그리고 x를 리스트로 만든 것에 비교한다.
reversed를 무조건 리스트로 묶는다