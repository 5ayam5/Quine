# Simple [Quine](https://en.wikipedia.org/wiki/Quine_(computing)) Program
The main idea behind developing this quine was using the functionality of the `exec` function.
`exec(s)` is equivalent to executing the text which is stored in `s`. Thus, the following line is executed
```
print('''#This program prints itself\nquine = %r'''%quine + '''\nexec(quine)''')
```
`'''` is used to write a multiline string and `%r` prints the `repr` value of the variable, thus including the quotation marks which is useful to print the exact assignment of `s`.