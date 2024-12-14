# Mini Miner

This will be a solution to hackattic's "Mini miner" coding challenge

In this challenge a JSON is received from the endpoint with two attributes: `block` and `difficulty`. 
The `block` attribute contains `data`, which houses arbitrary `data` and `nonce`. 
The Mini Miner's goal is to find a `nonce` value that causes the SHA256 hash of block to start with difficulty zero bits. 
That is, if difficulty is 4, the hash should start with at least 4 zero bits.

## Running and additional info

All instructions for the challenge can be found at [Hackattic Mini Miner](https://hackattic.com/challenges/mini_miner)!

To run my code for this challenge, simply run `python miniminer.py`

To submit this code for a first run at the challenge, simply remove `&playground=1` from the post method of the Miniminer API!

Please note that this was built using python 3 and consists of the requests, hashlib, and json libraries. Additionally, a token.txt file will have to be created which contains your token for this challenge!
Alternatively, the token can be hardcoded into the `constants.py` module or even into the `miniminer.py` module directly.

If you have read this far, thank you for taking the time and here's to more code challenges and the lessons along the way!
