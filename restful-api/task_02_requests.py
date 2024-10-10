#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():

    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = r.json()
        print("Titles for all posts:\n")
        for post in posts:
            print(f"{post['title']}")
    else:
            print(f"Failed to fetch posts. Status code: {r.status_code}")

def fetch_and_save_posts():
    
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = r.json()
        structured_posts = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csv_file:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(structured_posts)
        print("Data has benn succesfully written to posts.csv")
    else:
        print(f"Failed to fetch posts. Status code: {r.status_code}")
        
fetch_and_save()

