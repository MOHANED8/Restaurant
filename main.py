import http.server
import json
from urllib.parse import urlparse, parse_qs

# Load dataset
with open('dataset.json', 'r') as f:
    dataset = json.load(f)

class RestaurantRequestHandler(http.server.BaseHTTPRequestHandler):
    # Helper function to calculate quality score for a meal
    def calculate_quality_score(self, ingredients):
        total_quality_score = 0
        total_ingredient_count = 0
        for ingredient in ingredients:
            ingredient_name = ingredient['name']
            ingredient_quality = ingredient.get('quality', 'high')
            ingredient_options = [opt for opt in dataset['ingredients'] if opt['name'] == ingredient_name]
            if ingredient_options:
                option = next(opt for opt in ingredient_options[0]['options'] if opt['quality'] == ingredient_quality)
                total_quality_score += option['price']
                total_ingredient_count += 1
        if total_ingredient_count == 0:
            return None
        return total_quality_score / total_ingredient_count

    # Helper function to calculate price for a meal
    def calculate_price(self, ingredients):
        total_price = 0
        for ingredient in ingredients:
            ingredient_name = ingredient['name']
            ingredient_quality = ingredient.get('quality', 'high')
            ingredient_options = [opt for opt in dataset['ingredients'] if opt['name'] == ingredient_name]
            if ingredient_options:
                option = next(opt for opt in ingredient_options[0]['options'] if opt['quality'] == ingredient_quality)
                total_price += option['price']
                # Additional cost for degraded quality
                if ingredient_quality == 'medium':
                    total_price += 0.05
                elif ingredient_quality == 'low':
                    total_price += 0.10
        return total_price

    # Endpoint to list meals with filtering and sorting options
    def list_meals(self):
        parsed_query = parse_qs(urlparse(self.path).query)
        is_vegetarian = parsed_query.get('is_vegetarian', [''])[0].lower() in ['true', '1']
        is_vegan = parsed_query.get('is_vegan', [''])[0].lower() in ['true', '1']

        filtered_meals = []
        for meal in dataset['meals']:
            if (not is_vegetarian or all('vegetarian' in group for group in meal['groups'])) \
                    and (not is_vegan or all('vegan' in group for group in meal['groups'])):
                filtered_meals.append(meal)

        sorted_meals = sorted(filtered_meals, key=lambda x: x['name'])
        return json.dumps(sorted_meals).encode('utf-8')

    # Endpoint to get details of a single meal
    def get_meal(self):
        parsed_query = parse_qs(urlparse(self.path).query)
        meal_id = int(parsed_query.get('id', ['-1'])[0])
        meal = next((meal for meal in dataset['meals'] if meal['id'] == meal_id), None)
        if meal:
            return json.dumps(meal).encode('utf-8')
        else:
            return json.dumps({'error': 'Meal not found'}).encode('utf-8')

    # Endpoint to calculate quality for a given set of quality parameters
    def calculate_quality(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)
        meal_id = int(parsed_data.get('meal_id', ['-1'])[0])
        meal = next((meal for meal in dataset['meals'] if meal['id'] == meal_id), None)
        if not meal:
            return json.dumps({'error': 'Meal not found'}).encode('utf-8')

        quality = self.calculate_quality_score(meal['ingredients'])
        if quality is not None:
            return json.dumps({'quality': quality}).encode('utf-8')
        else:
            return json.dumps({'error': 'Invalid quality parameters for ingredients'}).encode('utf-8')

    # Endpoint to calculate price for a given set of quality parameters
    def calculate_price(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)
        meal_id = int(parsed_data.get('meal_id', ['-1'])[0])
        meal = next((meal for meal in dataset['meals'] if meal['id'] == meal_id), None)
        if not meal:
            return json.dumps({'error': 'Meal not found'}).encode('utf-8')

        price = self.calculate_price(meal['ingredients'])
        return json.dumps({'price': price}).encode('utf-8')

    # Handle GET requests
    def do_GET(self):
        if self.path.startswith('/listMeals'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(self.list_meals())
        elif self.path.startswith('/getMeal'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(self.get_meal())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Not found'}).encode('utf-8'))

    # Handle POST requests
    def do_POST(self):
        if self.path.startswith('/quality'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(self.calculate_quality())
        elif self.path.startswith('/price'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(self.calculate_price())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Not found'}).encode('utf-8'))


if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, RestaurantRequestHandler)
    print('Starting server...')
    httpd.serve_forever()
