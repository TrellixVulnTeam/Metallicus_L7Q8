import junit.framework.TestCase;

public class TruncTest extends TestCase {

    public void testtruncate() {
        assertEquals("te", StringUtils.truncate("test", 2, "START", false, "<...>"));
        assertEquals("foobar", StringUtils.truncate("foobar", 10, "START", false, "<...>"));
        assertEquals("fo...", StringUtils.truncate("foobar", 5, "START", false, "<...>"));
        assertEquals("foobar", StringUtils.truncate("foobar", 6, "START", false, "<...>"));
        assertEquals(null, StringUtils.truncate(null, 2, null, false, "<...>"));
        assertEquals(null, StringUtils.truncate(null, 2, null, false, "<...>"));
        assertEquals("", StringUtils.truncate("", 2, "", false, "<...>"));
        assertEquals("", StringUtils.truncate("", 2, "", false, "<...>"));
        assertEquals("abc", StringUtils.truncate("abcdefghij", 2, "abc", false, "<...>"));
        assertEquals("fghij", StringUtils.truncate("abcdefghij", 2, "fghij", false, "<...>"));
        assertEquals("", StringUtils.truncate("abcdefghij", 2, "", false, "<...>"));
        assertEquals("peach", StringUtils.truncate("raspberry peach", 2, "peach", false, "<...>"));
        assertEquals("abcdefghij", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghij", false, "<...>"));
        assertEquals("abcdefghijklmno", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("bcdefghijk", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("cdefghijkl", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("defghijklm", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("efghijklmn", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("fghijklmno", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("fghij", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("fgh", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("klm", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("klmno", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("n", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("no", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("o", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("o", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals("", StringUtils.truncate("abcdefghijklmno", 2, "abcdefghijklmno", false, "<...>"));
        assertEquals(null, StringUtils.truncate(null, 2, "START", false, "<...>"));
        assertEquals(null, StringUtils.truncate(null, 2, "START", false, "<...>"));
        assertEquals("", StringUtils.truncate("", 2, "START", false, "<...>"));
        assertEquals("", StringUtils.truncate("", 2, "START", false, "<...>"));
        assertEquals("abc", StringUtils.truncate("abcdefghij", 2, "START", false, "<...>"));
        assertEquals("fghij", StringUtils.truncate("abcdefghij", 2, "START", false, "<...>"));
        assertEquals("", StringUtils.truncate("abcdefghij", 2, "START", false, "<...>"));
        assertEquals("peach", StringUtils.truncate("raspberry peach", 2, "START", false, "<...>"));
        assertEquals("abcdefghij", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("abcdefghijklmno", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("bcdefghijk", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("cdefghijkl", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("defghijklm", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("efghijklmn", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("fghijklmno", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("fghij", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("fgh", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("klm", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("klmno", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("n", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("no", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("o", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("o", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals("", StringUtils.truncate("abcdefghijklmno", 2, "START", false, "<...>"));
        assertEquals(null, StringUtils.truncate(null, 2, null, false, "<...>"));
        assertEquals(null, StringUtils.truncate(null, 2, null, false, "<...>"));
        assertEquals(null, StringUtils.truncate(null, 2, null, false, "<...>"));
        assertEquals(null, StringUtils.truncate(null, 2, "", false, "<...>"));
        assertEquals(null, StringUtils.truncate(null, 2, "x", false, "<...>"));
        assertEquals("", StringUtils.truncate("", 2, null, false, "<...>"));
        assertEquals("", StringUtils.truncate("", 2, null, false, "<...>"));
        assertEquals("", StringUtils.truncate("", 2, null, false, "<...>"));
        assertEquals("", StringUtils.truncate("", 2, "", false, "<...>"));
        assertEquals("", StringUtils.truncate("", 2, "x", false, "<...>"));
        assertEquals("abc", StringUtils.truncate("abc", 2, null, false, "<...>"));
        assertEquals("abc", StringUtils.truncate("abc", 2, "", false, "<...>"));
        assertEquals("abc", StringUtils.truncate("abc", 2, "x", false, "<...>"));
        assertEquals("abc", StringUtils.truncate("abc", 2, null, false, "<...>"));
        assertEquals("abc", StringUtils.truncate("abc", 2, "", false, "<...>"));
        assertEquals("abc", StringUtils.truncate("abc", 2, "x", false, "<...>"));
        assertEquals("ac", StringUtils.truncate("abc", 2, null, false, "<...>"));
        assertEquals("ac", StringUtils.truncate("abc", 2, "", false, "<...>"));
        assertEquals("axc", StringUtils.truncate("abc", 2, "x", false, "<...>"));
        assertEquals("ayzya", StringUtils.truncate("abcba", 2, "yz", false, "<...>"));
        assertEquals("ayya", StringUtils.truncate("abcba", 2, "y", false, "<...>"));
        assertEquals("ayzya", StringUtils.truncate("abcba", 2, "yzx", false, "<...>"));
        assertEquals("abcba", StringUtils.truncate("abcba", 2, "w", false, "<...>"));
        assertEquals("abcba", StringUtils.truncate("abcba", 2, "w", false, "<...>"));
        assertEquals("jelly", StringUtils.truncate("hello", 2, "jy", false, "<...>"));
        assertEquals("ayzya", StringUtils.truncate("abcba", 2, "yz", false, "<...>"));
        assertEquals("ayya", StringUtils.truncate("abcba", 2, "y", false, "<...>"));
        assertEquals("ayzya", StringUtils.truncate("abcba", 2, "yzx", false, "<...>"));
        assertEquals("bcc", StringUtils.truncate("abc", 2, "bc", false, "<...>"));
        assertEquals("q651.506bera", StringUtils.truncate("d216.102oren", 2, "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM567891234", false, "<...>"));
    }
}