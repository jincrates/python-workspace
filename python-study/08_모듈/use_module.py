import my_module  #사용할 모듈이 같은 폴더에 있어야함

selected = my_module.random_rsp()
print(selected)
print('가위?', my_module.SCISSOR == selected)