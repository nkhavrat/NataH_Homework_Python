from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:1804@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_add_teacher():
    """Тест на добавление ."""
    test_email = "testuser@example.com"
    test_group_id = 1

    with db.connect() as connection:
        connection.execute(
            text("INSERT INTO teacher (email, group_id) "
                 "VALUES (:email, :group_id)"),
            {"email": test_email, "group_id": test_group_id}
        )

        result = connection.execute(
            text("SELECT * FROM teacher WHERE email = :email"),
            {"email": test_email}
        )
        rows = result.all()  # без mappings()

        assert len(rows) == 1, "Пользователь не был добавлен"
        assert rows[0][1] == test_email, "Email не совпадает"
        assert rows[0][2] == test_group_id, "group_id не совпадает"

        connection.execute(
            text("DELETE FROM teacher WHERE email = :email"),
            {"email": test_email}
        )


def test_update_teacher():
    """Тест на редактирование."""
    test_email = "testuser@example.com"
    test_group_id = 1
    new_email = "new_email"
    new_group_id = 2

    with db.connect() as connection:
        connection.execute(
            text("INSERT INTO teacher (email, group_id) "
                 "VALUES (:email, :group_id)"),
            {"email": test_email, "group_id": test_group_id}
        )
        connection.execute(
            text(
                "UPDATE teacher SET email = :new_email, "
                "group_id = :new_group_id WHERE email = :old_email"),
            {"new_email": new_email, "new_group_id": new_group_id,
             "old_email": test_email}
        )

        result = connection.execute(
            text("SELECT * FROM teacher WHERE email = :email"),
            {"email": new_email}
        )
        rows = result.all()

        assert len(rows) == 1, "Пользователь не был добавлен"
        assert rows[0][1] == new_email, "Email не совпадает"
        assert rows[0][2] == new_group_id, "group_id не совпадает"

        connection.execute(
            text("DELETE FROM teacher WHERE email = :email"),
            {"email": new_email}
        )


def test_delete_teacher():
    """Тест на удаление"""
    test_email = "teacher@mail.ru"
    test_group_id = 6

    with db.connect() as connection:
        connection.execute(
            text("INSERT INTO teacher (email, group_id) "
                 "VALUES (:email, :group_id)"),
            {"email": test_email, "group_id": test_group_id}
        )

        connection.execute(
            text("SELECT * FROM teacher WHERE email = :email"),
            {"email": test_email}
        )

        connection.execute(
            text("DELETE FROM teacher WHERE email = :email"),
            {"email": test_email}
        )

        rows = ()
        assert len(rows) == 0
