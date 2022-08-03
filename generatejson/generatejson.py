with open('countries2.json', 'w') as f:
    with open('List2.txt', 'r') as r:
        lines = r.readlines()
        f.write("{\"countries\":[\n")
        for l in lines:
            f.write("   { \"country\":\""+ l.strip() + "\", \"id\":\"aa\", \"visited\":false},\n")
            print(l)
        f.write("]}")
        r.close()
    f.close()
