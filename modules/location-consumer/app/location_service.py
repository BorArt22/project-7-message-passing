import logging
import psycopg2
import json

from schemas import LocationSchema
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-consumer")

def location_save_to_database(location_value, cursor):
    try:
        location_dict = json.loads(location_value)
    except Exception as exception:
        logger.warning(f"Invalid extract data from json. Reason: {exception}")
        return

    validation_results: Dict = LocationSchema().validate(location_dict)
    if validation_results:
        logger.warning(f"Unexpected data format in payload: {validation_results}")
        raise (f"Invalid payload: {validation_results}")

    query = '''
    insert into public.location (person_id, coordinate, creation_time) 
    values ({}, ST_Point({}, {}), timestamp '{}');
    '''.format(int(location_dict["person_id"]), 
               location_dict["latitude"], 
               location_dict["longitude"],
               location_dict["creation_time"]
               )
    try:
        cursor.execute(query)
        cursor.execute('commit;')
    except Exception as exception:
        logger.warning(f"Invalid insert into database. Reason: {exception}")
