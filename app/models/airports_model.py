from app import conn


def airport_movements_max():
    data = {}
    try:
        cursor = conn.connection.cursor()
        sql = "SELECT a.id_airport, name, count(id_movement_type) movements FROM airports a left join mecate_airports_management.flights f on a.id_airport = f.id_airport group by a.id_airport order by movements desc"
        cursor.execute(sql)
        movements = cursor.fetchall()

        try:
            movements
        except NameError as e:
            raise Exception("No se encontraron movimientos")

        most_active = movements[0]
        data['movements'] = {
            'airport': most_active[1],
            'movements': most_active[2],
        }
    except Exception as ex:
        data['msg'] = "error: " + str(ex)

    return data
