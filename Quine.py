#This program prints itself
quine = "print('''#This program prints itself\nquine = %r'''%quine + '''\nexec(quine)''')"
exec(quine)
