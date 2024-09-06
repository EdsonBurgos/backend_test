from app import conn


def flights_per_airline_max():
    data = {}
    try:
        cursor = conn.connection.cursor()
        sql = "SELECT a.id_airline, name, count(*) flights FROM airlines a left join mecate_airports_management.flights f on a.id_airline = f.id_airline group by a.id_airline order by flights desc"
        cursor.execute(sql)
        flights = cursor.fetchall()

        try:
            flights
        except NameError as e:
            raise Exception("No se encontraron vuelos")

        most_active = flights[0]
        data['flights'] = {
            'airline': most_active[1],
            'flights': most_active[2],
        }
    except Exception as ex:
        data['msg'] = "error"

    return data


def flights_day_max():
    data = {}
    try:
        cursor = conn.connection.cursor()
        sql = "SELECT day, count(day) flights FROM flights GROUP BY day order by flights desc"
        cursor.execute(sql)
        flights = cursor.fetchall()

        try:
            flights
        except NameError as e:
            raise Exception("No se encontraron vuelos")

        most_active = flights[0]
        data['flights'] = {
            'day': most_active[0],
            'flights': most_active[1],
        }
    except Exception as ex:
        data['msg'] = "error"

    return data


def airline_day_flights():
    data = {}
    try:
        cursor = conn.connection.cursor()
        sql = ("SELECT a.id_airline, name, day, count(*) flights "
               "FROM airlines a "
               "left join mecate_airports_management.flights f on a.id_airline = f.id_airline "
               "group by a.id_airline, day "
               "order by flights desc")
        cursor.execute(sql)
        flights = cursor.fetchall()

        try:
            flights
        except NameError as e:
            raise Exception("No se encontraron vuelos")

        airlines = {}

        for flight in flights:
            if flight[3] >= 2:
                airlines[flight[0]] = {
                    'airline': flight[1],
                    'day': flight[2],
                    'flights': flight[3],
                }

        data['airlines'] = airlines
    except Exception as ex:
        data['msg'] = "Error: " + str(ex)

    return data
