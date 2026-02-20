from flask import Flask, render_template

app = Flask(__name__)

# Mock Data for Cakes
cakes = [
    {
        "id": 1,
        "name": "Malou's Signature Banana Cake",
        "description": "Our best-seller! Moist, rich, and bursting with real banana flavor. Made with organic bananas and a hint of cinnamon.",
        "price": 1200.00,
        "image": "hero-banana-cake.svg",
        "featured": True,  # High converting
        "badge": "Best Seller"
    },
    {
        "id": 2,
        "name": "Classic Chocolate Fudge",
        "description": "Decadent chocolate layers with a smooth ganache finish.",
        "price": 1500.00,
        "image": "cake-chocolate.svg",
        "featured": False
    },
    {
        "id": 3,
        "name": "Strawberry Delight",
        "description": "Fresh strawberries and light whipped cream sponge.",
        "price": 1400.00,
        "image": "cake-strawberry.svg",
        "featured": False
    },
    {
        "id": 4,
        "name": "New York Cheesecake",
        "description": "Creamy, dense, and perfectly baked cheesecake with a graham cracker crust.",
        "price": 1600.00,
        "image": "cake-cheesecake.svg",
        "featured": False
    },
    {
        "id": 5,
        "name": "Vanilla Bean Dream",
        "description": "Classic vanilla cake with buttercream frosting and sprinkles.",
        "price": 1100.00,
        "image": "cake-vanilla.svg",
        "featured": False
    },
    {
        "id": 6,
        "name": "Banana Walnut Loaf",
        "description": "A rustic take on our signature banana cake, loaded with crunchy walnuts.",
        "price": 900.00,
        "image": "cake-banana.svg",
        "featured": True,
        "badge": "New Arrival"
    }
]

@app.route('/')
def index():
    featured_banana = next((c for c in cakes if c['id'] == 1), None)
    other_cakes = [c for c in cakes if c['id'] != 1]
    return render_template('index.html', featured_banana=featured_banana, cakes=other_cakes)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/product/<int:cake_id>')
def product(cake_id):
    cake = next((c for c in cakes if c['id'] == cake_id), None)
    if cake:
        return f"<h1>{cake['name']}</h1><p>{cake['description']}</p><p>₱{cake['price']}</p>"
    return "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)
