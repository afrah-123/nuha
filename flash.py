from flask import Flask, render_template, request
from form import ReviewForm
import csv
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'


@app.route('/', methods=['GET', 'POST'])
def forms():
    form = ReviewForm()
    if request.method == 'POST':
        name = request.form['fname']
        product = request.form['product']
        review = request.form['review']


        with open('namelist.csv', 'w') as infile:
            fieldnames = ['name', 'product', 'review']

            writer = csv.DictWriter(infile, fieldnames=fieldnames)
            writer.writerow({'name': name, 'product': product, 'review': review})




        with open('namelist.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            return render_template('yelo.html', )


    return render_template('yelo.html', form=form)

if __name__ == '__main__':
   app.run()




