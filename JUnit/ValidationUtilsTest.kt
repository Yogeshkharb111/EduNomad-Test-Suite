import org.junit.Assert.*
import org.junit.Test

class ValidationUtilsTest {

    @Test
    fun validEmailTest() {
        assertTrue(ValidationUtils.isValidEmail("test@gmail.com"))
    }

    @Test
    fun invalidEmailTest() {
        assertFalse(ValidationUtils.isValidEmail("test@.com"))
    }

    @Test
    fun validPasswordTest() {
        assertTrue(ValidationUtils.isValidPassword("123456"))
    }

    @Test
    fun shortPasswordTest() {
        assertFalse(ValidationUtils.isValidPassword("123"))
    }
}
