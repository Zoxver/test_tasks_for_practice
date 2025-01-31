from HashMap import HashMap


if __name__ == "__main__":

    hashmap = HashMap()

    hashmap['a'] = 10
    hashmap['b'] = 20
    hashmap['c'] = 30
    print("Значение для a", hashmap['a'])
    print("Значение для b", hashmap['b'])
    print("Значение для c", hashmap['c'])

    hashmap['a'] = 100
    print("Новое значение a", hashmap['a'])

    print("\nПроверка существования ключей:")
    print("a", 'a' in hashmap)
    print("b", 'b' in hashmap)
    print("d", 'd' in hashmap)

    print("\nУдаление элемента b")
    del hashmap['b']
    print("b ", 'b' in hashmap)


    print("\nРазмер таблицы:", len(hashmap))

    hashmap.add('h', 40)
    hashmap.add('e', 50)
    hashmap.add('f', 60)
    hashmap.add('h1', 40)
    hashmap.add('e1', 50)
    hashmap.add('f1', 60)
    hashmap.add('h2', 40)
    hashmap.add('e2', 50)
    hashmap.add('f2', 60)
    print("Длина таблицы после добавления", len(hashmap))

    print("Ключи:", hashmap.keys())
    print("Значения:", hashmap.values())
    print("Пары ключ-значение:", hashmap.items())


