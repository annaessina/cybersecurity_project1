from sqlalchemy.sql import text
from db import db

def get_reviews():
    result = db.session.execute(text("SELECT spas.*, locations.address, locations.city, categories.name,\
                                    AVG(reviews.stars) AS avg_stars, COUNT(reviews.id) AS review_count,\
                                    array_agg(reviews.comment) AS comments FROM spas \
                                    LEFT JOIN locations ON spas.id = locations.spa_id \
                                    LEFT JOIN reviews ON spas.id = reviews.spa_id \
                                    LEFT JOIN categories ON spas.id = categories.spa_id \
                                    GROUP BY spas.id , locations.id, categories.id"))
    return result.fetchall()

def add_review(spa_id, stars, comment):
    sql = text("INSERT INTO reviews (spa_id, stars, comment) VALUES (:spa_id, :stars, :comment)")
    db.session.execute(sql, {"spa_id":spa_id, "stars":stars, "comment":comment})
    db.session.commit()
