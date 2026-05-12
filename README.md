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

## Notes

- Chart rendering depends on Chart.js from jsDelivr and fonts from Google Fonts.
- Dashboard data is simulated in the browser; it is safe for demos and does not connect to real security tooling.
- The terminal is a browser-side simulator. Commands are rendered safely and do not execute system commands.
