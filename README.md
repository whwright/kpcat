kpcat
=====

cat a keepass file

The goal of this project is to read a keepass file on the command line, enabling usge with other unix tools.


#### Basic usage
```
$ python setup.py develop
$ ↪ kpcat --help
Usage: kpcat [OPTIONS] KEEPASS_FILE

  cat a keepass file

Options:
  --password TEXT              Password for keepass file. Will try to load
                               $KPCAT_PASSWORD from the environment first,
                               which can be overriden by this option. If
                               neither are supplied a prompt will ask for your
                               password. NOTE: using a prompt will not work if
                               piping the output to another command.
  --keyfile FILE               Key file for keepass file.
  --show-passwords             Option to show passwords in output; passwords
                               are redacted by default.
  --output-format [json|text]  Format type for output. Default: text
  --help                       Show this message and exit.
```
