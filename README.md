<img align="right" src="assets/doingus.png" width="30%" height="30%" alt="Avatar hand drawn by me!">

# doingus

doingus is a [Revolt](https://revolt.chat) bot that I made for fun.

I would also use this as a reference in case I forget how to code Revolt bots in Python.

# How to set up for yourself

First, you will need to install the required libraries for it to run:

```sh
pip install -U python-dotenv
pip install git+https://github.com/EnokiUN/voltage # since voltage from pypi is broken, use git version instead.
```

Then you must configure the .env file. copy the `.env.example` file to `.env` and put in the following stuff:

```
revolt_token='abcdefghijklmnopqrstuvwxyz12345' # Your Revolt bot's token
prefix='owo!' # You can change it to anything you want.
```

Then you run it:

```
python src/main.py
```

The default prefix is `owo!`.
