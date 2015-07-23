/* https://leetcode.com/problems/isomorphic-strings/ */
bool isIsomorphic(char* s, char* t) {
    char map1[128] = {0};
    char map2[128] = {0};
    
    int i = 0;
    while ('\0' != s[i]) {
        if (map1[s[i]] != 0 && map1[s[i]] != t[i])
            return false;
        if (map2[t[i]] != 0 && map2[t[i]] != s[i])
            return false;
        
        map1[s[i]] = t[i];
        map2[t[i]] = s[i];
        
        i++;
    }
    
    return true;
}
