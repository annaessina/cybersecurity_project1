from sqlalchemy.sql import text
from db import db


def get_all_spas():
    result = db.session.execute(text("SELECT * FROM spas"))
    return result.fetchall()

def search_spas(substring):
    sql = text("SELECT * FROM spas WHERE LOWER(name) LIKE '%' || LOWER('" + substring + "') || '%'")
    '''
    FLAW 3. How to fix.
    sql = text("SELECT * FROM spas WHERE LOWER(name) LIKE '%' || LOWER(:substring) || '%'")
    '''
    result = db.session.execute(sql, {"substring":substring})
    filtered_spas = result.fetchall()
    print(filtered_spas)

    returnfiltered_spas

def delete_spa(spa_id):
    sql1 = text("DELETE FROM locations WHERE spa_id=:spa_id")
    db.session.execute(sql1, {"spa_id": spa_id})
    sql2 = text("DELETE FROM reviews WHERE spa_id=:spa_id")
    db.session.execute(sql2, {"spa_id": spa_id})


    sql3 = text("DELETE FROM categories WHERE spa_id=:spa_id")
    db.session.execute(sql3, {"spa_id": spa_id})


    sql4 = text("DELETE FROM spas WHERE id=:spa_id")
    db.session.execute(sql4, {"spa_id": spa_id})

    db.session.commit()

def add_spa(name, address, city, categories):
    check_for_name = text("SELECT * FROM spas WHERE name = :name")

    existing_spa = db.session.execute(check_for_name, {"name": name}).fetchone()
    if existing_spa:
        print('ollaa ifis')
        return False

    sql1 = text("INSERT INTO spas (name) VALUES (:name)")
    db.session.execute(sql1, {"name": name})
    spa_id = db.session.execute(text("SELECT currval('spas_id_seq')")).fetchone()[0]
    sql2 = text("INSERT INTO locations (spa_id, address, city) VALUES (:spa_id, :address, :city)")
    db.session.execute(sql2, {"spa_id": spa_id, "address": address, "city": city})

    sql3 = text("INSERT INTO categories (name, spa_id) VALUES (:name, :spa_id)")
    db.session.execute(sql3, {"name": categories, "spa_id": spa_id})
    db.session.commit()

    return True
