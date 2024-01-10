#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def get_stats(collection):
    """Provides some stats about Nginx logs stored in MongoDB"""
    n_logs = collection.count_documents({})
    print(f'{n_logs} logs')

    print('Methods:')
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')


if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    get_stats(nginx_collection)
