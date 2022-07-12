# 2- Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.



def truth():
    result = True
    for x in [False, True]:
        for y in [False, True]:
            for z in [False, True]:
                result = result and (not(x or y or z) ==
                                     (not x and not y and not z))
                if not result:
                    return False
    return True


print(truth())