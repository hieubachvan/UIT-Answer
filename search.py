import pymongo
from flask import Blueprint, render_template, url_for, request, flash

# create views blueprint
search = Blueprint('search', __name__, template_folder='templates')


@search.route('/')
def home():
    if 'search' in request.args:
        connect_uri = 'mongodb+srv://hieubachvan:0914351748@cluster0.vezt7.mongodb.net/search?retryWrites=true&w=majority'
        client = pymongo.MongoClient(connect_uri)

        # create db client
        db = client.search
        search_results = db.search_results.find({'$text': {'$search': request.args.get('search')}})

        for entry in search_results:
            flash(entry, 'success')

        client.close()
    return render_template('search.html')


@search.route('/search_results')
def search_results():
    if 'search' in request.args:
        connect_uri = 'mongodb+srv://hieubachvan:0914351748@cluster0.vezt7.mongodb.net/search?retryWrites=true&w=majority'
        client = pymongo.MongoClient(connect_uri)

        # create db client
        db = client.search
        query = db.search_results.find({'$text': {'$search': request.args.get('search')}})
        search_results = []

        for doc in query:
            search_results.append(doc)

        client.close()
        return render_template('search.html', search_results=search_results)
