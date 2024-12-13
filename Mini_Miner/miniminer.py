import json
from hashlib import sha256
import requests as req
from constants import challenge_url, challenge_complete_url

def main():
    miniminer = Miniminer(challenge_url, challenge_complete_url)
    try:
        result = miniminer.run()
        print(result)
    except req.RequestException as e:
        print(e)

class _MiniminerINIT():
    def __init__(self, challengeUrl, challenge_complete_url):
        self.challengeUrl = challengeUrl
        self.challengeCompleteUrl = challenge_complete_url

class MiniminerAPI(_MiniminerINIT):
    def get(self):
        response = req.get(self.challengeUrl)
        return response

    def post(self, nonce):
        answer = {'nonce':nonce}
        response = req.post(self.challengeCompleteUrl+"&playground=1", json = answer)
        return response

class Miniminer(_MiniminerINIT):
    def connect(self):
        api = MiniminerAPI(self.challengeUrl, self.challengeCompleteUrl)
        print("\nsending GET request...")
        response = api.get()
        if response.status_code != 200:
            raise req.RequestException(f"BAD REQUEST! Status Code: {response.status_code}")
        print(f"Received successful response! Status Code: {response.status_code}\n")
        return api, response

    def run(self):
        api, response = self.connect()

        json_contents = response.json()
        print(json_contents)
        difficulty = json_contents["difficulty"]
        nonce, digest = self.nonce_machine(json_contents, difficulty)
        print(f"\nNonce: {nonce},\nDigest: {digest}\n") 
        
        response = api.post(nonce)
        return response.json()

    def nonce_machine(self, json_object, diff):
        print("\nStarting up Nonce Machine...")
        expected = "0" * ((diff//4)+1)
        nonce = 0

        while True:
            nonce += 1
            json_object["block"]["nonce"] = nonce
            json_data = json.dumps(json_object["block"], 
                                  sort_keys=True, 
                                  separators=(",",":"))
            digest = sha256(json_data.encode()).hexdigest()

            if digest.startswith(str(expected)):
                print("Success!")
                return nonce, digest

if __name__ == "__main__":
    main()
