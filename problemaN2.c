std::string reverseInParentheses(std::string inputString) {
    using namespace std;
    vector<string> stack;
    for (auto ch: inputString) {
        if (ch != ')') {
            string item{ch};
            stack.push_back(item);
        } else {
            string whole = "";
            while (!stack.empty()) {
                string item = stack.back();
                stack.pop_back();
                if (item == "(") {
                    break;
                }
                whole = item + whole;
            }
            reverse(whole.begin(), whole.end());
            stack.push_back(whole);
        }
    }
    string res = "";
    for (auto item: stack) {
        res += item;
    }
    return res;
}