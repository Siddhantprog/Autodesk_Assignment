#include <string>
#include <cassert>
#include <algorithm>
#include <cctype>
#include <iostream>

using namespace std;

string reverse_words(const string& str)
{
    string res = str;

    int n = res.size();
    int i = 0;

    while (i < n)
    {
        if (isalnum(static_cast<unsigned char>(res[i])))
        {
            int start = i;

            while (i < n && isalnum(static_cast<unsigned char>(res[i])))
            {
                ++i;
            }

            reverse(res.begin() + start, res.begin() + i);
        }
        else
        {
            ++i;
        }
    }

    return res;
}

int main()
{
    string test_str = "String; 2be reversed...";
    assert(reverse_words(test_str) == "gnirtS; eb2 desrever...");
    cout << "Code Execution Successful" << endl;
    return 0;
}