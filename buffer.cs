public class Solution {
    public bool IsAnagram(string s, string t) {
		if (s.Length != t.Length) return false;

		// are these the right structures?
        var countS = new Dictionary<char, int>(); 
        var countT = new Dictionary<char, int>();

        for (int i = 0; i < s.Length; i++)
		{
			// any += construct?
            countS[s[i]] = countS.GetValueOrDefault(s[i]) + 1;
            countS[s[i]] = countS.GetValueOrDefault(s[i]) + 1;
        }
    }
}
