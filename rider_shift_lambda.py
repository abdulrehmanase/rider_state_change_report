from utils import *
from sql import *
from datetime import datetime, timedelta

AGENT_ID = 'Agent ID'
AGENT_NAME = 'Agent Name'
AGENT_EMAIL = "Agent Email"
AGENT_LAST_LOGIN = "Agent Last Login"
RIDER_ID = 'Rider ID'
RIDER_NAME = 'Rider Name'
ACTION = 'Action'
MESSAGE = 'Message'
DATETIME = "Date & Time"


def rider_states(start_date, end_date):
    end_date = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)

    print('start',start_date)
    print('end',end_date)
    logs = logs_query(start_date, end_date)
    logs_data = [{
        AGENT_ID: log[0],
        AGENT_NAME: log[1],
        AGENT_EMAIL: log[2],
        AGENT_LAST_LOGIN: log[3],
        RIDER_ID: log[4],
        RIDER_NAME: log[5],
        ACTION: log[6],
        MESSAGE: log[7],
        DATETIME: str(log[8].date()),
    } for log in logs]
    header = [AGENT_ID, AGENT_NAME, AGENT_EMAIL, AGENT_LAST_LOGIN, RIDER_ID, RIDER_NAME, ACTION, MESSAGE, DATETIME]
    file_name = 'Rider Enable Disable Report'
    zip_file = create_csv(file_name, logs_data, header)
    attachments = [{'name': file_name + '.zip', 'content': zip_file.getvalue()}]
    title = 'Rider Enable Disable Report'
    import csv



    # with open('countries.csv', 'w', encoding='UTF8') as f:
    #     writer = csv.writer(f)
    #
    #     # write the header
    #     writer.writerow(header)
    #
    #     # write the data
    #     writer.writerow(logs_data)

rider_states("2021-05-10", "2021-10-10")

