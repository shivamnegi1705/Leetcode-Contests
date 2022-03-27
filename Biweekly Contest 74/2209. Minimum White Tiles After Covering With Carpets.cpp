/**

- We will use inclusion and exclusion priciple by using carpet for ith index or will skip the ith index.
- dp[index][number of carpets remaining]

**/
class Solution {
public:
    // n--> size of floor
    // m --> size of carpet.
    int n,m;
    // s --> floor string
    string s;
    // dp[index][number of carpets remaining]
    int dp[1002][1002];
    int solve(int i,int rem){
        // if we go out of bounds
        if(i>=n){
            return 0;
        }
        // if state has been already been calculated
        if(dp[i][rem]!=-1){
            return dp[i][rem];
        }

        int ans = INT_MAX;
        // if we have carpet to use for ith index.
        if(rem>0){
            ans = min(ans,solve(i+m,rem-1));
        }
        int cnt = 0;
        if(s[i]=='1'){
            cnt = 1;
        }
        // not using carpet for ith index.
        ans = min(ans,cnt+solve(i+1,rem));
        return dp[i][rem] = ans;
    }
    int minimumWhiteTiles(string floor, int numCarpets, int carpetLen) {
        n = floor.size();
        m = carpetLen;
        s = floor;  
        memset(dp,-1,sizeof(dp));
        return solve(0,numCarpets);
    }
};