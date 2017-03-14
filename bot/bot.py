import random

import requests


class Bot:
    serverAPI = 'http://127.0.0.1:8000'
    signupURL = '/my_auth/api/signup/'
    signinURL = '/api-token-auth/'
    postURL = '/post/posts/'

    def __init__(self, number_of_users, max_posts_per_users, max_likes_per_users, email, password):
        self.number_of_users = number_of_users
        self.max_posts_per_users = max_posts_per_users
        self.max_likes_per_users = max_likes_per_users
        self.email = email
        self.password = password
        self.post_text = "Random bot's text"

    def run(self):
        self.signup(self.email, self.password)

    def signup(self, email, password):
        response = requests.post(
                "{}{}".format(self.serverAPI, self.signupURL),
                data={'email': email, 'password': password}
        )
        print(response)
        if response.status_code == 201:
            self.signin()

    def signin(self):
        response = requests.post(
            "{}{}".format(self.serverAPI, self.signinURL),
            data={'email': self.email, 'password': self.password}
        )
        if response.status_code == 200:
            self.token = response.json()['token']
            self.auth_header = {'Authorization': 'Bearer {}'.format(self.token)}
            self.create_posts(self.max_posts_per_users)

    def create_posts(self, max_posts_per_users):
        post_count = random.randint(1, max_posts_per_users)
        for i in range(0, post_count):
            response = requests.post(
                "{}{}".format(self.serverAPI, self.postURL),
                data={'text': self.post_text},
                headers=self.auth_header
            )
            print(response)
            if response.status_code == 201:
                self.make_likes()

    def make_likes(self):
        pass




bot = Bot(1, 2, 3, 'andrew.begel@microsoft.com', '11111111')
bot.run()


