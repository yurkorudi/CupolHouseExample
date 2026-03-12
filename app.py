from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    domes = [
        {"name": "М'ятний Світанок", "price": "2800", "size": "30 м²", "capacity": "2 особи", 
         "amenities": [("fa-wifi", "Wi-Fi"), ("fa-coffee", "Кавомашина"), ("fa-leaf", "Еко-засоби")]},
        {"name": "Лісова Тінь", "price": "3100", "size": "35 м²", "capacity": "2 особи", 
         "amenities": [("fa-fire", "Камін"), ("fa-utensils", "Міні-кухня"), ("fa-tree", "Вид на ліс")]},
        {"name": "Гірський Кришталь", "price": "3500", "size": "40 м²", "capacity": "3 особи", 
         "amenities": [("fa-tv", "Проектор"), ("fa-couch", "Зона відпочинку"), ("fa-mountain", "Панорама")]},
        {"name": "Озерний Затишок", "price": "3800", "size": "40 м²", "capacity": "2 особи", 
         "amenities": [("fa-hot-tub", "Чан поруч"), ("fa-wind", "Кондиціонер"), ("fa-snowflake", "Холодильник")]},
        {"name": "Зоряне Небо", "price": "4200", "size": "45 м²", "capacity": "2 особи", 
         "amenities": [("fa-star", "Скляний дах"), ("fa-wine-glass", "Винна шафа"), ("fa-bath", "Ванна біля вікна")]},
        {"name": "Сімейний Простір", "price": "5000", "size": "60 м²", "capacity": "4 особи", 
         "amenities": [("fa-users", "2 спальні"), ("fa-baby-carriage", "Дитяче ліжко"), ("fa-parking", "Паркомісце")]},
        {"name": "Скелястий Пік", "price": "5500", "size": "45 м²", "capacity": "2 особи", 
         "amenities": [("fa-dumbbell", "Йога-мат"), ("fa-biking", "Прокат вел."), ("fa-cloud-sun", "Тераса 20м²")]},
        {"name": "Royal Dome Premium", "price": "8000", "size": "80 м²", "capacity": "2 особи", 
         "amenities": [("fa-crown", "Власний SPA"), ("fa-concierge-bell", "Сніданок в номер"), ("fa-infinity", "Безліміт чан")]},
    ]
    return render_template('index.html', domes=domes)

if __name__ == '__main__':
    app.run(debug=True)