from genealopy.helper import get_function_name


class TestHelper:
    def test_get_function_name(self) -> None:
        # Arrange
        expected: str = "test_get_function_name"
        
        # Act
        actual: str = get_function_name()

        # Assert
        assert actual == expected

    def test_get_function_name_current(self) -> None:
        # Arrange
        back: int = 0
        expected: str = "get_function_name"
        
        # Act
        actual: str = get_function_name(back)

        # Assert
        assert actual == expected
