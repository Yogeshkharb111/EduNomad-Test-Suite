import org.junit.Assert.*
import org.junit.Test

class ChatbotLogicTest {

    @Test
    fun testQueryFormatting() {
        val input = " What is Kotlin? \n"
        val expected = "What is Kotlin?"
        val actual = ChatbotHelper.formatUserQuery(input)
        assertEquals(expected, actual)
    }

    @Test
    fun testEmptyInput() {
        val input = "    "
        val actual = ChatbotHelper.formatUserQuery(input)
        assertEquals("", actual)
    }
}
