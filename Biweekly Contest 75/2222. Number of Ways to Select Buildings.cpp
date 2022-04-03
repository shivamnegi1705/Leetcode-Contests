/**
ll dp[index][size of selected subseq][previous selected char];
**/
#define ll long long int
class Solution {
public:
    ll dp[100005][3][3];
    ll n;
    ll solve(ll ind,ll cnt,ll prev, string &s){
        // selected subsequence size becomes 3 then return 1 count.
        if(cnt==3){
            return 1;
        }
        // reached end of string but selected subseq size is not 3.
        if(ind==n){
            return 0;
        }
        // if state is already calculated.
        if(dp[ind][cnt][prev]!=-1){
            return dp[ind][cnt][prev];
        }
        ll ans = 0;
        ll cur = s[ind]-'0';
        // if subseq is not started. start the new subseq. (010 or 101)
        if(prev==2){
            ans = ans + solve(ind+1,1,cur,s);
        }
        // if prev selected is 1 or 0 then if prev==cur^1 then we can select it or skip it.
        else{
            if((prev^1)==cur){
                ans = ans + solve(ind+1,cnt+1,cur,s);
            }
        }
        ans = ans + solve(ind+1,cnt,prev,s);
        return dp[ind][cnt][prev] = ans;
    }
    ll numberOfWays(string s) {
        n = s.size();
        memset(dp,-1,sizeof(dp));
        return solve(0,0,2,s);
    }
};