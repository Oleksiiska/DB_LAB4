import data_access
from domain import should_go_outside


def import_csv(path):
    with data_access.connect() as session:
        if data_access.count(session):
            return 0
        records = list(data_access.read_csv(path))
        for record in records:
            record.go_outside = should_go_outside(record.precip_mm)
        data_access.save(session, records)
        session.commit()
        return len(records)


def stats():
    with data_access.connect() as session:
        return data_access.stats(session)


def find(country, day):
    with data_access.connect() as session:
        return data_access.find(session, country, day)
