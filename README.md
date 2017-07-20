# seminar-170721-demo

## Preparation

```bash
$ pyenv local 2.7.13 pypy2-5.7.0-src
```

## Usage

### CPython

```bash
$ python fib.py
```


### PyPy

```bash
$ pypy fib.py
```

### RPython

```bash
$ pypy/rpython/bin/rpython -O2 rpythonsample.py
```
