---
name: reference-vps-proxy
description: Personal Xray VLESS+Reality proxy on the Hetzner VPS - where it lives, how to manage it, gotchas
metadata:
  type: reference
---

Repo ~/Projects/vps-proxy, pushed to github.com/boyalyn/vps-proxy (private). The installer is `install_xray_reality.sh`. It does a SHA256-verified official Xray download, runs as the `xray` user on 443/tcp under a hardened systemd unit, and opens only that port in ufw. Installed 2026-10-05.

For use from Singapore and possibly mainland China, on iPhone (Shadowrocket/V2Box) and Mac (V2Box). Exit IP is in Germany.

Secrets live only on the server:
- /usr/local/etc/xray/secrets.env
- /root/xray-client.txt
- /root/xray-qr.png (the QR was sent to the user)

Rotate by deleting secrets.env and re-running the installer.

Gotchas: a REALITY target of www.microsoft.com fails handshakes (Xray 26.3.27), so www.apple.com is used. New Xray client JSON names the public key `password` (the link param is still `pbk`). The Claude Code auto-mode classifier blocked the first attempt as an "External Ingress Tunnel"; it worked once the user explicitly authorized it in chat. Don't use this proxy to get around Polymarket's geoblock (Germany is blocked anyway). Related: [[project-status]].
