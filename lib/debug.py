#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

author1 = Author("Alice")

author2 = Author("Bob")

# Create some magazines
mag1 = Magazine ("TechNow", "Technology")
mag2 = Magazine("HealthPlus", "Health")

# Create some articles

article1 = Article(author1, mag1, "The Future of AI")

article2 = Article(author1, mag2, "Healthy Living Tips")

article3 = Article(author2, mag1, "AI in Everyday Life")

article4 = Article(author2, mag1, "Deep Learning Explained")

article5 = Article(author2, mag1, "Robots and You")


print(author1.articles())

print(author1.magazines())

print(author1.topic_areas())

print(mag1.articles())

print(mag1.contributors())

print(mag1.article_titles())

print(mag1.contributing_authors())

print(Magazine.top_publisher())

    # don't remove this line, it's for debugging!
ipdb.set_trace()
