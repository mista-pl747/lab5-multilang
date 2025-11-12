package calculator;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    private final Calculator calc = new Calculator();

    @Test
    void divide_validInput_returnsCorrectResult() {
        assertEquals(5, calc.divide(10, 2));
    }

    @Test
    void divide_byZero_throwsArithmeticException() {
        assertThrows(ArithmeticException.class, () -> calc.divide(10, 0));
    }
}
