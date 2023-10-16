from datetime import datetime, timedelta
from genealopy.datetime_ import get_execution_time, get_year, get_years


class TestDatetime:
    def test_get_execution_time(self) -> None:
        # Arrange
        expected: float = 5.0
        start: datetime = datetime.now() - timedelta(seconds=expected)
        
        # Act
        actual: float = get_execution_time(start)

        # Assert
        assert actual >= expected

    def test_get_execution_time_days(self) -> None:
        # Arrange
        days: int = 5.0
        start: datetime = datetime.now() - timedelta(days)
        expected: float = 432000.0
        
        # Act
        actual: float = get_execution_time(start)

        # Assert
        assert actual >= expected

    def test_get_year(self) -> None:
        # Arrange
        expected: int = 2023
        
        # Act
        actual: int = get_year()

        # Assert
        assert actual == expected

    def test_get_year(self) -> None:
        # Arrange
        first_year: int = 2020
        expected: str = "2020-2023"
        
        # Act
        actual: str = get_years(first_year)

        # Assert
        assert actual == expected
