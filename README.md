# CyberShield OS

CyberShield OS is a static, single-page security operations center demo. It includes simulated dashboards for alerts, threat intelligence, incidents, firewall rules, endpoints, IDS/IPS, logs, analytics, assets, compliance, playbooks, reports, notifications, theming, language selection, and an interactive terminal.

## Run locally

No build step is required. Serve the repository root with any static file server, then open `index.html`.

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.

## Validate changes

The repository includes a lightweight validation script that checks:

- duplicate HTML IDs,
- JavaScript `getElementById` references to missing elements,
- inline JavaScript syntax with `node --check`.

```bash
python3 scripts/validate.py
```

The same script runs on every pull request via [`.github/workflows/validate.yml`](.github/workflows/validate.yml).

## Deploy to Vercel

The repo ships with a [`vercel.json`](vercel.json) so it can be deployed as a static site with sensible cache and security headers — no build step required.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Falwibohell-max%2Fcyber-security-os)

### One-click

Click the button above, point Vercel at this repository, and confirm. Vercel will detect it as a static project and serve `index.html` from the repository root.

### From the dashboard

1. In <https://vercel.com/new>, import the GitHub repository `alwibohell-max/cyber-security-os`.
2. When prompted for framework preset, choose **Other** (a.k.a. static).
3. Leave the build and output settings empty — there is no build step.
4. Click **Deploy**.

### From the CLI

```bash
npm i -g vercel
vercel        # preview deployment
vercel --prod # production deployment
```

The included `vercel.json` configures:

- `cleanUrls` so `/foo` resolves without the `.html` extension,
- a custom `404.html` page for unknown routes,
- baseline security headers (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`),
- a `Cache-Control: no-cache` policy for `index.html` so deploys roll out immediately.

## Notes

- Chart rendering depends on Chart.js from jsDelivr and fonts from Google Fonts.
- Dashboard data is simulated in the browser; it is safe for demos and does not connect to real security tooling.
- The terminal is a browser-side simulator. Commands are rendered safely and do not execute system commands.
