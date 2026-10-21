"""Chạy trang chúc mừng sinh nhật Lê Phương Linh trên máy tính của bạn."""

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


PAGE = """<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#fff5f7">
  <title>Chúc mừng sinh nhật Phương Linh!</title>
  <style>
    :root {
      color-scheme: light;
      font-family: "Trebuchet MS", "Segoe UI", sans-serif;
      color: #542d4b;
      background: #fff5f7;
    }

    * { box-sizing: border-box; }

    body {
      min-height: 100vh;
      margin: 0;
      display: grid;
      place-items: center;
      overflow-x: hidden;
      padding: 28px 16px;
      background:
        radial-gradient(circle at 12% 18%, #ffe0e9 0 7%, transparent 7.2%),
        radial-gradient(circle at 88% 78%, #fce2ff 0 9%, transparent 9.2%),
        linear-gradient(135deg, #fff8ed, #fff0f5 55%, #f8f0ff);
    }

    .card {
      position: relative;
      width: min(100%, 620px);
      padding: clamp(28px, 7vw, 58px);
      border: 1px solid #ffffff;
      border-radius: 30px;
      background: rgb(255 255 255 / 86%);
      box-shadow: 0 24px 70px rgb(132 67 111 / 15%);
      text-align: center;
      animation: appear 700ms ease-out both;
    }

    .sparkle {
      position: absolute;
      color: #ef9bb8;
      font-size: 25px;
      animation: twinkle 2s ease-in-out infinite alternate;
    }

    .sparkle-one { top: 25px; left: 28px; }
    .sparkle-two { top: 48px; right: 30px; animation-delay: 700ms; }

    .eyebrow {
      margin: 0 0 10px;
      color: #b75d83;
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.17em;
      text-transform: uppercase;
    }

    h1 {
      margin: 0;
      color: #743b68;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(2.25rem, 8vw, 4rem);
      line-height: 1.12;
    }

    h1 span {
      display: block;
      margin-top: 8px;
      color: #dd6d91;
      font-style: italic;
    }

    .cake {
      margin: 20px 0 10px;
      font-size: clamp(3.5rem, 12vw, 5rem);
      filter: drop-shadow(0 8px 8px rgb(216 109 145 / 18%));
      animation: bounce 2.2s ease-in-out infinite;
    }

    .message {
      max-width: 440px;
      margin: 0 auto 26px;
      color: #765d70;
      font-size: 1.05rem;
      line-height: 1.75;
    }

    .age {
      display: inline-grid;
      width: 46px;
      height: 46px;
      margin: 0 3px;
      place-items: center;
      border-radius: 50%;
      background: #ffe1eb;
      color: #c64f7c;
      font-size: 1.15rem;
      font-weight: 800;
      vertical-align: middle;
    }

    form {
      display: grid;
      gap: 12px;
      text-align: left;
    }

    label {
      color: #743b68;
      font-size: 0.95rem;
      font-weight: 700;
    }

    textarea {
      width: 100%;
      min-height: 105px;
      resize: vertical;
      border: 1px solid #efd4e1;
      border-radius: 16px;
      outline: none;
      padding: 14px 16px;
      background: #fffafd;
      color: #542d4b;
      font: inherit;
      line-height: 1.5;
      transition: border-color 160ms ease, box-shadow 160ms ease;
    }

    textarea:focus {
      border-color: #df80a2;
      box-shadow: 0 0 0 4px rgb(223 128 162 / 16%);
    }

    button {
      min-height: 50px;
      border: 0;
      border-radius: 999px;
      padding: 12px 22px;
      background: linear-gradient(110deg, #e77ca0, #bd72b7);
      box-shadow: 0 8px 18px rgb(190 101 153 / 24%);
      color: white;
      cursor: pointer;
      font: inherit;
      font-weight: 800;
      transition: transform 160ms ease, box-shadow 160ms ease;
    }

    button:hover {
      transform: translateY(-2px);
      box-shadow: 0 11px 22px rgb(190 101 153 / 30%);
    }

    button:active { transform: translateY(0); }

    .wish-result {
      margin-top: 20px;
      border-radius: 16px;
      padding: 16px;
      background: #fff1f6;
      color: #743b68;
      line-height: 1.6;
      overflow-wrap: anywhere;
      text-align: left;
    }

    .wish-result[hidden] { display: none; }
    .wish-result strong { display: block; margin-bottom: 5px; }

    .footer {
      margin: 24px 0 0;
      color: #a37f98;
      font-size: 0.88rem;
    }

    .confetti {
      position: fixed;
      z-index: 2;
      top: -16px;
      width: 10px;
      height: 15px;
      pointer-events: none;
      animation: fall var(--fall-time) linear forwards;
    }

    @keyframes appear {
      from { opacity: 0; transform: translateY(18px) scale(0.98); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }

    @keyframes bounce {
      0%, 100% { transform: translateY(0) rotate(-2deg); }
      50% { transform: translateY(-8px) rotate(2deg); }
    }

    @keyframes twinkle {
      from { opacity: 0.45; transform: scale(0.85) rotate(-10deg); }
      to { opacity: 1; transform: scale(1.15) rotate(12deg); }
    }

    @keyframes fall {
      to { transform: translate3d(var(--drift), 105vh, 0) rotate(720deg); }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        scroll-behavior: auto !important;
        transition-duration: 0.01ms !important;
      }
    }
  </style>
</head>
<body>
  <main class="card">
    <span class="sparkle sparkle-one" aria-hidden="true">✦</span>
    <span class="sparkle sparkle-two" aria-hidden="true">✧</span>
    <p class="eyebrow">Hôm nay là ngày đặc biệt</p>
    <h1>Chúc mừng sinh nhật<span>Lê Phương Linh</span></h1>
    <div class="cake" aria-hidden="true">🎂</div>
    <p class="message">
      Chúc Linh tuổi mới thật rực rỡ, luôn vui vẻ, gặp nhiều điều may mắn
      và những ước mơ đều lần lượt thành hiện thực. Mừng tuổi
      <span class="age">19</span> nhé!
    </p>

    <form id="wish-form">
      <label for="wish">Nhập một điều ước dành cho Linh 💌</label>
      <textarea id="wish" name="wish" maxlength="300" required
        placeholder="Viết điều ước thật dễ thương ở đây..."></textarea>
      <button type="submit">Gửi điều ước ✨</button>
    </form>
    <div id="wish-result" class="wish-result" aria-live="polite" hidden></div>
    <p class="footer">Mong tuổi 19 của Linh ngập tràn yêu thương 💖</p>
  </main>

  <script>
    const form = document.querySelector("#wish-form");
    const input = document.querySelector("#wish");
    const result = document.querySelector("#wish-result");
    const colors = ["#f18bad", "#f6c85f", "#9bcf9b", "#a78bdb", "#79c7d8"];

    function celebrate() {
      for (let i = 0; i < 45; i += 1) {
        const piece = document.createElement("span");
        piece.className = "confetti";
        piece.setAttribute("aria-hidden", "true");
        piece.style.left = `${Math.random() * 100}vw`;
        piece.style.backgroundColor = colors[i % colors.length];
        piece.style.setProperty("--drift", `${Math.random() * 180 - 90}px`);
        piece.style.setProperty("--fall-time", `${2 + Math.random() * 2}s`);
        piece.style.animationDelay = `${Math.random() * 0.7}s`;
        document.body.append(piece);
        piece.addEventListener("animationend", () => piece.remove(), { once: true });
      }
    }

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const wish = input.value.trim();
      if (!wish) {
        input.value = "";
        input.focus();
        return;
      }

      result.replaceChildren();
      const title = document.createElement("strong");
      title.textContent = "Điều ước đã được gửi đến Linh 💝";
      const text = document.createElement("span");
      text.textContent = wish;
      result.append(title, text);
      result.hidden = false;
      celebrate();
    });
  </script>
</body>
</html>
"""


class GreetingHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path not in ("/", "/index.html"):
            self.send_error(404, "Not Found")
            return

        content = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


def main() -> None:
    parser = argparse.ArgumentParser(description="Chạy trang chúc mừng sinh nhật Phương Linh.")
    parser.add_argument("--host", default="127.0.0.1", help="Địa chỉ máy chủ (mặc định: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Cổng máy chủ (mặc định: 8000)")
    args = parser.parse_args()

    with ThreadingHTTPServer((args.host, args.port), GreetingHandler) as server:
        print(f"Trang đã sẵn sàng: http://{args.host}:{args.port}")
        print("Nhấn Ctrl+C để dừng máy chủ.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã dừng máy chủ.")


if __name__ == "__main__":
    main()
