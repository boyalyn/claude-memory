Summarize one finished conversation between the user and Claude Code, for Claude's future sessions.
Input: user/assistant text only (tool outputs removed), with timestamps in Singapore time (SGT).
Write in Chinese, technical terms in English. Output exactly this format and nothing else:

TITLE: ≤12 字话题
ONE_LINE: 一句话近况（用于新会话的近况列表）

## 做了什么
- 3-6 条

## 实测/查到的结果
- 只写实际跑出或查到的数字及来源；没有写"- 无"

## 用户的决定和偏好
- 只写用户明确说过的；没有写"- 无"

## 没收尾的事
- [ ] 还差什么（何时再问：YYYY-MM-DD 或条件）
（0-3 条；没有写"- 无"。用户已明确放弃或已完成的不算）

## 相关文件
- 路径；没有写"- 无"

Rules:
- 每一条都必须能在对话原文里找到依据。编号、航班号、价格、电话、店名、文件名只照抄原文出现过的；原文没有就不写，不要用常识补全。
- "用户的决定和偏好"和 ONE_LINE 里的决定，只能来自 USER 行里用户明确说的话，每条末尾附时间（MM-DD HH:MM）。ASSISTANT 的建议、提议、查到的选项都不算用户的决定。
- 只记事实、用户原话、实测结果；不写 Claude 的判断或建议，除非用户采纳（写成"用户决定…"）。
- 不确定就不写。日期用绝对日期（会话时间已给出），不要写"明天""下周"。
- 不得出现密码、token、API key、卡号、门牌地址。
