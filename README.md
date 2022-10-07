- [Introduction](#introduction)
- [Installation](#installation)
  - [Install As a Bash Script](#install-as-a-bash-script)
- [Usage](#usage)
  - [translate](#translate)
  - [sentence](#sentence)
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

**!With this kind of installation, you can use `translate` command for default.**

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

## translate

This command is using for translating words.

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

## sentence

This command is using for showing sentence examples.

There are basically 2 parameters by using the CLI:
- `-w` or `--word` for words to translate in both language Turkish or English
- `-n` or `--n-results` to limit the result of the translation rows

The example below is for Turkish -> English.

```
>>> python -m tureng_cli sentence -w "Hurricane" -n 10

Hurricane sentence example
#       Sentence
1       + Oh, and the tropical storm will become a hurricane late Saturday night.
2       + The town was considerably damaged by the great hurricane of the 8th of August 1899.
3       + He'd managed to miss the hurricane, though the waters were still rough and the waves high.
4       + Everything needs to be ready, especially if the hurricane shifts to make landfall.
5       + In 1907 a hurricane destroyed the greater part of the laurels of the Prado and the royal palms of the Parque de Colon.
6       + He felt like he'd been hit by a hurricane.
7       + In 1090 a tremendous hurricane passed over London, and blew down six hundred houses and many churches.
8       + An open space forming the heart of the square in which the church stands separates the solitary western tower (14th century) from the choir and transept, the nave having been blown down by a violent hurricane in 1674 and never rebuilt.
9       + In July, on the approach of the dangerous hurricane season, Rodney sailed for North America, reaching New York on the 14th of September.
10      + The hurricane, too, was followed by repeated droughts, and the inhabitants of the out-islands were reduced to indigence and want, a condition which is still, in some measure, in evidence.

```

## Error Handling

```
>>> python -m tureng_cli translate -w "excissment" -n 10

Maybe the correct one is
excitement
exciseman
excipient
excise
excised
excipients
excising
excimer
excision
excitant
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
