from mongoengine import *


def cluster_connection():
    cluster_uri = "mongodb+srv://Arina:arina270799@cluster27-pldc3.gcp.mongodb.net/cluster_new?retryWrites=true&w=1"
    conn = connect("cluster_new", host=cluster_uri)
    print("Successfully connected!")
    mydb = conn['cluster_new']
    mycoll = mydb['supplier']

    return mycoll


