/* https://leetcode.com/problems/length-of-last-word/ */
int lengthOfLastWord(char* s) {
    int ret = 0, cur = 0;
    while ('\0' != *s) {
        cur = (' ' == *s) ? 0 : cur + 1;
        ret = (0 == cur) ? ret : cur;
        s++;
    }
    return ret;
}
