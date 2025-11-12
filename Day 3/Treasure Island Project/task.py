print(r'''
                           ;\ 
                            |' \ 
         _                  ; : ; 
        / `-.              /: : | 
       |  ,-.`-.          ,': : | 
       \  :  `. `.       ,'-. : | 
        \ ;    ;  `-.__,'    `-.| 
         \ ;   ;  :::  ,::'`:.  `. 
          \ `-. :  `    :.    `.  \ 
           \   \    ,   ;   ,:    (\ 
            \   :., :.    ,'o)): ` `-. 
           ,/,' ;' ,::"'`.`---'   `.  `-._ 
         ,/  :  ; '"      `;'          ,--`. 
        ;/   :; ;             ,:'     (   ,:) 
          ,.,:.    ; ,:.,  ,-._ `.     \""'/ 
          '::'     `:'`  ,'(  \`._____.-'"' 
             ;,   ;  `.  `. `._`-.  \\ 
             ;:.  ;:       `-._`-.\  \`. 
              '`:. :        |' `. `\  ) \ 
      -hrr-      ` ;:       |    `--\__,' 
                   '`      ,' 
                        ,-'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a=input("you'r at the cross road where do you want to go (left or right): ")
if a=="left":
    b=input("You've reached beside of a lake do you want to swim or wait for the boat")
    if b=="wait":
        c=input("Now you have three door ahead which on you choose(yellow,red and blue)")
        if c=="yellow":
            print("Yaay you got the treasure")
        elif c=="blue":
            print("Game over")
        elif c=="red":
            print("Game over")
        else:
            print("you typed a wrong input")
    elif b=="swim":
        print("game over")
    else:
        print("you typed a wrong input")
elif a=="right":
    print("game over")
else:
    print("you typed a wrong input")