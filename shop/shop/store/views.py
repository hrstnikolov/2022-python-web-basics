from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

COMPANY_MAIL = "the_boss@company.com"


# The simplest possible view
def show_contact_info(request):
    contact_info = "Sofia, bul. Lomsko Shose, Ivan Ivanov"
    return HttpResponse(contact_info)


class ShirtSizes:
    @staticmethod
    def get_available_shirt_sizes():
        return ["XS", "S", "M", "L", "XL", "XXL"]
        # return ["XS", ]


# View with context
def show_about(request):
    context = {
        "introduction": "We are the best online shop for shirts!\n Men and women.\nTake a look! ",
        "email_address": "ivan.ivanov@company.com",
        "name": {
            "first": "Ivan",
            "last": "Ivanov",
        },
        "shirt_sizes": ShirtSizes(),
    }
    return render(request, "about.html", context=context)


def index(request):
    context = {
        "current_time": datetime.now(),
        # "user": "Gosho",
        "user": "",
    }
    return render(request=request, template_name="index.html", context=context)


def redirect_to_home(request):
    return redirect(to="index")


class Article:
    starting_id = 0

    def __init__(self, headline, tease, full_text, local_path):
        self.headline = headline
        self.tease = tease
        self.full_text = full_text
        self.local_path = local_path
        self.article_id = Article.starting_id
        Article.starting_id += 1

    def get_absolute_url(self):
        return "https://www.shirt_company.com" + self.local_path


articles = [
    Article(
        headline="How to find the size that matches you?",
        tease="It has never been easier to find a perfectly matching shirt. Find how in this article.",
        full_text="{full text of the article}",
        local_path="article/1/",
    ),
    Article(
        headline="The trendiest colors of this summer",
        tease="Can you guess the winner out of purple, blue or orange?",
        full_text="{full text of the article}",
        local_path="article/2/",
    ),
]


def show_articles(request):
    context = {
        "articles": articles,
    }
    return render(request, "articles.html", context)


def show_single_article_by_id(request, article_id):
    article = [a for a in articles if a.article_id == article_id][0]
    context = {
        "article": article,
    }
    return render(request, "article.html", context)


def checkout_basket(request):
    context = {
        "basket": ["milk", "coffee", "bread", ],
        # "basket": [],
        "bill": 134.1214401239,
    }

    return render(request, "checkout.html", context)
