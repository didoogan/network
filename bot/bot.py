import random

import requests


class Bot:
    serverAPI = 'http://127.0.0.1:8000'
    signupURL = '/my_auth/api/signup/'
    signinURL = '/api-token-auth/'
    postURL = '/post/posts/'
    get_max_post_user = '/post/posts/get_max_posts_user/'

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
        if self._signin():
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
        response = requests.get(
            '{}{}'.format(self.serverAPI, self.get_max_post_user),
            headers=self.auth_header
        )
        if response.status_code == 200:
            self.email = response.json()['email']
            if self._signin():
                pass

    def _signin(self):
        response = requests.post(
            "{}{}".format(self.serverAPI, self.signinURL),
            data={'email': self.email, 'password': self.password}
        )
        if response.status_code == 200:
            self.token = response.json()['token']
            self.auth_header = {'Authorization': 'Bearer {}'.format(self.token)}
            return True
        else:
            return False


bot = Bot(1, 2, 3, 'tech.press@nokia.com', '11111111')
bot.run()


