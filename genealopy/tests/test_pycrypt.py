from genealopy.pycrypt import decrypt, encrypt


class TestPycrypt:
    def test_decrypt(self) -> None:
        # Arrange
        string: str = "==g2zHVPI54siULK8syRf/A+aPfU9gkjzKStowzKH99D4r98R1DSOOrI1iCPrc03Pgv2zHVPI54siULK8syRf/A+aPfU9gkjzKStowzKH99D4r98R1DSOOrI1iCPrc03Pgv2zHVPI54siULK8syRf/A+aPfU9gkjzKStowzKH99D4r98R1DSOOrI1iCPrc03Pgv2zHVPI54siULK8syRf/A+aPfU9gkjzKStowzKH99D4r98R1DSOOrI1iCPrc03Pgv2zHVPI54siULK8syRf/A+aPfU9gkjzKStowzKH99D4r98R1DSOOrI1iCPrc03Pgvupi4Vi/iLmtma5yPhR8KQ"
        key: str = "key"
        salt: str = "salt"
        expected: str = "string"
        
        # Act
        actual: str = decrypt(string, key, salt)

        # Assert
        assert actual == expected
    
    def test_encrypt(self) -> None:
        # Arrange
        string: str = "string"
        key: str = "key"
        salt: str = "salt"
        expected: str = "==g2zHVPI54siULK8syRf/A+aPfU9gkjzKStowzKH99D4r98R1DSOOrI1iCPrc03Pgv2zHVPI54siULK8syRf/A+aPfU9gkjzKStowzKH99D4r98R1DSOOrI1iCPrc03Pgv2zHVPI54siULK8syRf/A+aPfU9gkjzKStowzKH99D4r98R1DSOOrI1iCPrc03Pgv2zHVPI54siULK8syRf/A+aPfU9gkjzKStowzKH99D4r98R1DSOOrI1iCPrc03Pgv2zHVPI54siULK8syRf/A+aPfU9gkjzKStowzKH99D4r98R1DSOOrI1iCPrc03Pgvupi4Vi/iLmtma5yPhR8KQ"
        
        # Act
        actual: str = encrypt(string, key, salt)

        # Assert
        assert actual == expected
