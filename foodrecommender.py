from flask import Flask, render_template
from flask import request
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Recommender system
ratings = pd.read_csv("rating_foodrating.csv",index_col=1)

def standardize(row):
    new_row = (row - row.mean())/(row.max() - row.min())
    return new_row

ratings_std = ratings.apply(standardize)
item_similarity = cosine_similarity(ratings_std.T)
item_similarity_df = pd.DataFrame(item_similarity,index=ratings.columns, columns=ratings.columns)


def get_similar_food(food_name,user_rating):
    similar_score = item_similarity_df[food_name]*(user_rating-2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score

# Views
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        foodName = request.form['foodName']
        foodRating = int(request.form['foodRating'])

        prediction = get_similar_food(foodName, foodRating)
        print(prediction) 
        return render_template('index.html', original_input={'foodName':foodName,'foodRating':foodRating},result=prediction)

# Run app
if __name__ == "__main__":
    app.run()
