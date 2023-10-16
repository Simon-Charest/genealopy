from genealopy.data import exists_in, get_count, get_gender, get_name


class TestData:
    def test_exists_in(self) -> None:
        # Arrange
        collection: dict = {"key": "value"}
        expected: bool = True

        # Act
        actual: bool = exists_in(collection, "key", "value")

        # Assert
        assert actual == expected

    def test_exists_in_key_only(self) -> None:
        # Arrange
        collection: list = ["key"]
        expected: bool = True

        # Act
        actual: bool = exists_in(collection, "key")

        # Assert
        assert actual == expected

    def test_get_count(self) -> None:
        # Arrange
        collection: dict = {
            "obj1": {"key": "value1"},
            "obj2": {"key": "value1"},
            "obj3": {"key": "value2"},
            "obj4": {"key": "value3"},
            "obj5": {"key": "value4"}
        }
        field: str = "key"
        minimum: int = 2

        # Act
        actual: list = get_count(collection, field, minimum)

        # Assert
        assert len(actual) == 1
        assert actual[0] == ("value1", 2)

    def test_get_gender(self) -> None:
        # Arrange
        collection: dict = {
            "obj1": {
                "first_name": "first_name1",
                "last_name": "last_name1",
                "gender": "gender1"
            },
            "obj2": {
                "first_name": "first_name2",
                "last_name": "last_name2",
                "gender": "gender2"
            }
        }
        id: str = "first_name2\nlast_name2"
        expected: str = "gender2"

        # Act
        actual: str = get_gender(collection, id)

        # Assert
        assert actual == expected

    def test_get_name(self) -> None:
        # Arrange
        collection: dict = {
            "first_name": "first_name",
            "last_name": "last_name"
        }
        expected: str = "first_name\nlast_name"

        # Act
        actual: str = get_name(collection)

        # Assert
        assert actual == expected
