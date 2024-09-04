def spam():
    print(eggs)  # error!
    eggs = "spam local"  # if this isn't. then error won't happend.


eggs = "global"
spam()
