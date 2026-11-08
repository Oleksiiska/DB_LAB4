import data_access


def import_csv(path):
    with data_access.connect() as session:
        if data_access.count(session):
            return 0
        records = list(data_access.read_csv(path))
        data_access.save(session, records)
        session.commit()
        return len(records)


def stats():
    with data_access.connect() as session:
        return data_access.stats(session)
