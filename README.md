kpcat
=====

cat a keepass file - with style

This is still in development. The goal of the project is to be able to read a keepass file from the command line,
and use other unix tools to parse some information out of the file.

Note that this will remain in beta until https://github.com/pschmitt/pykeepass/issues/115 is resolved. (This is why
pykeepass is currently installed from my fork.)


#### Basic usage
```
$ python setup.py develop
$ kpcat yourfile
```

#### TODO
- write docs
- write examples
- eggsecute to a binary
