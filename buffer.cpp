#include <vector>
using namespace std;

class Solution {
public:
  int maxArea(vector<int> &heights) {
    int max_vol = 0;
    int l = 0;
    int r = heights.size() - 1;

    while(l < r) {
      int volume = (min(heights[r], heights[l]) * (r - l));
      int max_vol = max(max_vol, volume);
      if (heights[r] > heights[l])
        r--;
      else
        l++;
      }
      return max_vol;
    }
  };
