/**
- From each piles we can take 0,1,2,3... coins
- As, it asks for maximum value we will take maximum of all options.
- dp[index][k --> coins to choose]

**/
#define ll long long int
class Solution {
public:
    // dp[ith pile][remaining coins to choose]
    ll dp[1004][2004];
    ll n;
    ll p;
    ll solve(ll i,ll rem,vector<vector<int>>& arr) {
        // if we have reached the end of the pile or we have exhausted our options.
        if(i==n || rem==0){
            return 0;
        }
        // if we have already calculated the value of the state.
        if(dp[i][rem]!=-1){
            return dp[i][rem];
        }
        ll ans = INT_MIN;
        ll tot = 0;
        // traversing through the ith pile and try to take 0,1,2,3,4... coins from this pile[i].
        for(ll j=0;j<arr[i].size();j++){
            tot+=arr[i][j];
            if(rem>=j+1) {
                ans = max(ans, tot+solve(i+1,rem-j-1,arr));
            }
            else{
                break;
            }
        }
        // taking max of all the options.
        ans = max(ans, solve(i+1,rem,arr));
        return dp[i][rem] = ans;
    }
    
    int maxValueOfCoins(vector<vector<int>>& piles, int k) {
        n = piles.size();
        p = k;
        memset(dp,-1,sizeof(dp));
        return solve(0,k,piles);
    }
};