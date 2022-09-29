- [Introduction](#introduction)
- [Installation](#installation)
  - [Install As a Bash Script](#install-as-a-bash-script)
- [Usage](#usage)
  - [Error Handling](#error-handling)
  - [Help about parameters](#help-about-parameters)

# Introduction

I created this repo to easily translate English and Turkish words by using very good project, [Tureng](https://tureng.com/en/turkish-english).

This CLI basically scrapes [https://tureng.com/en/turkish-english](https://tureng.com/en/turkish-english) link to parse translation results. You can just pass the word as a parameter to translate. 


# Installation

You can easily start using the CLI by installing it as a package on your Python environment.

```
pip install .
```

Or you can install it by using the command below

```
pip install git+https://github.com/BaysanSoft/Tureng-Translation-CLI.git
```

Or you can just use `sudo make install`.

## Install As a Bash Script

If you want to use it from bash, you can just move [tureng-cli.sh](tureng-cli.sh) to `/usr/sbin/`.

```
>>> sudo mv tureng-cli.sh /usr/sbin/
>>> turenh-cli.sh "hurricane"

Meanings of "hurricane" in Turkish English Dictionary : 15 result(s)
#       Category        English         Turkish
1       + Common Usage  + hurricane     + kasırga
2       + General       + hurricane     + fırtına
3       + General       + hurricane     + urağan
4       + General       + hurricane     + kasırga
5       + General       + hurricane     + (güç veya hız bakımından) kasırgaya benzeyen şey
6       + Technical     + hurricane     + bora
7       + Technical     + hurricane     + kasırga
8       + Environment   + hurricane     + tropik siklon
9       + Geography     + hurricane     + kasırga
10      + Geography     + hurricane     + batı virginia eyaletinde şehir
11      + Geography     + hurricane     + utah eyaletinde şehir
12      + Meteorology   + hurricane     + bora
13      + Meteorology   + hurricane     + hortum
14      + Meteorology   + hurricane     + kasırga
15      + Military      + hurricane     + ikinci dünya savaşı'nda ingilizler tarafından kullanılan bir savaş uçağı
```

# Usage

There are basically 2 parameters by using the CLI:
- `-w` or `--word` for words to translate in both language Turkish or English
- `-n` or `--n-results` to limit the result of the translation rows

The example below is for Turkish -> English.

```
>>> python -m tureng_cli translate -w Kasırga -n 10

Meanings of "kasırga" in English Turkish Dictionary : 33 result(s)
#       Category        Turkish         English
1       + Common Usage  + kasırga       + hurricane
2       + Common Usage  + kasırga       + whirlwind
3       + General       + kasırga       + wind
4       + General       + kasırga       + cyclone
5       + General       + kasırga       + twist
6       + General       + kasırga       + squall
7       + General       + kasırga       + windstorm
8       + General       + kasırga       + whirlwind
9       + General       + kasırga       + twister
10      + General       + kasırga       + tourbillion

```


The example below is for English -> Turkish.
```
>>> python -m tureng_cli translate -w Hurricane -n 10

Meanings of "hurricane" in Turkish English Dictionary : 15 result(s)
#       Category        English         Turkish
1       + Common Usage  + hurricane     + kasırga
2       + General       + hurricane     + fırtına
3       + General       + hurricane     + urağan
4       + General       + hurricane     + kasırga
5       + General       + hurricane     + (güç veya hız bakımından) kasırgaya benzeyen şey
6       + Technical     + hurricane     + bora
7       + Technical     + hurricane     + kasırga
8       + Environment   + hurricane     + tropik siklon
9       + Geography     + hurricane     + kasırga
10      + Geography     + hurricane     + batı virginia eyaletinde şehir

```

## Error Handling

```
>>> python -m tureng_cli translate -w "excissment" -n 10

There is no translation for this word: excissment
```

## Help about parameters

You can use `--help` flag to get help.

```
>>> python -m tureng_cli --help

Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  translate  Command to translate a Turkish word to English
```

Or you can get help for specific commands.


```
>>> python -m tureng_cli translate --help

Usage: cli.py translate [OPTIONS]

  Command to translate a Turkish word to English

  Args:     word (str): Turkish word     n (int): The range of the list of
  translated results

Options:
  -w, --word TEXT         A word to translate from Turkish.
  -n, --n-result INTEGER  N rows to show.
  --help                  Show this message and exit.
```
