# LangageFrenchy

Mini langage de programmation créé en utilisant SLY (Sly Lex Yacc) et Python.

## Version

1.0.0

## Description

Ce programme utilise SLY (Sly Lex Yacc) et Python afin de compilé un nouveau langage de programmation nommé "LangageFrenchy" capable d'interpréter les instructions suivantes :
 - Déclaration et appel de variable
 - Appel de variable
 - Opération simple (+, -, *, /)
 - Comparaisons (==, <, <=, >, >=, !=)
 - Condition IF/ELSE
 - Boucle FOR
 - Commentaire
 - Création et appel de fonction
 - Retour de chaîne

## Auteur

Jeremy Fouquet

## Clone Projet

git clone https://github.com/jeremyfouquet/LangageFrenchy.git

## license

MIT License

## Exigences

Python >= 3.6

## Packages

Dans `requirements.txt`

## Utilisation

Executer le programme
```
$ make
```

Nettoyer le cache
```
$ make clean
```

Executer les tests
```
$ make tests
```

Installer environnement virtuel venv pour linux
```
$ make install-venv
```

Exemple d'instruction
```
LangageFrenchy > 1+1
2
LangageFrenchy > 1+1*2
3
LangageFrenchy > 1==1
Vrai
LangageFrenchy > SI 1==1 ALORS 1 SINON 0
1
LangageFrenchy > POUR x=0 VERS 2 ALORS x
0
1
LangageFrenchy > #commentaire
LangageFrenchy > FONC mafonction() -> a=1
LangageFrenchy > mafonction()
LangageFrenchy > a
1
LangageFrenchy > ECRIT "salut"
"salut"
```

## Structure
     .
    ├── app
        ├── main.py
        ├── lexer.py
        ├── parser.py
        └── interpreter.py
        └── test.py
    ├── LICENSE
    ├── Makefile
    ├── README.md
    └── requirements.txt
