question_url = 'https://hackattic.com/challenges/mini_miner/problem?access_token='
answer_url =  'https://hackattic.com/challenges/mini_miner/solve?access_token='
with open("token.txt", "r") as file:
    #reads token in and removes whitespace + newline characters
    token = file.readline().strip()

challenge_url = question_url+token
challenge_complete_url = answer_url+token

if __name__ == "__main__":
    print(token)
    print(challenge_url)
