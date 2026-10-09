---
name: reference-tailscale
description: User's personal tailnet (GitHub login) - nodes, Funnel, and the school-account pitfall
metadata:
  type: reference
---

Tailnet: tail8bd3c4.ts.net, logged in with the user's **GitHub** account (personal). Do NOT use the NTU email: it joins the shared e.ntu.edu.sg org tailnet, which is at the free-plan user limit. The VPS was briefly joined there and was logged out.

Nodes: `hetzner-de` (VPS, 100.121.113.41) runs Funnel `https://hetzner-de.tail8bd3c4.ts.net` -> http://127.0.0.1:8765 (travel MCP). The home server and the phone are not joined yet (planned).

Gotchas:
- Never `pkill -f "tailscale up"` over ssh: the pattern matches the ssh command itself and drops the session. Use `pkill -x tailscale`.
- `tailscale up` login URLs are single-use.

SSH aliases: de-server (trader), de-root (root). Related: [[project-mcp-servers]], [[reference-home-server]].
