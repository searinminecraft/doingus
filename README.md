# doingus

<img src="https://autumn.revolt.chat/avatars/NLpB-BNgWZAA915E14GnzCB2KW3n2wWtgIg19VgJQy/IMG_20230504_110523_1.jpg" width="256" height="256">

doingus is a [Revolt](https://revolt.chat) bot that I made for fun. She's quite special, because she has feelings, unlike the other bots.

I would also use this as a reference in case i forget how to code revolt bots in python.

# How to set up for yourself

First, you will need to install the required libraries for it to run:

```sh
pip install -U python-dotenv
pip install git+https://github.com/EnokiUN/voltage
```

Then you must configure the .env file. copy the `.env.example` file to `.env` and put in your Revolt bot token like so:

```
revolt_token='abcdefghijklmnopqrstuvwxyz12345'
```

Then you run it:

```
python src/main.py
```

The default prefix is `-`.